from flask import Flask, request, render_template
import aiohttp
import asyncio
import subprocess
import time
import re

app = Flask(__name__)

# Hugging Face API Setup (Replace with your own API key)
API_URL = "https://api-inference.huggingface.co/models/bigcode/starcoder"
HEADERS = {"Authorization": "Bearer YOUR_API_KEY"}

# Home Route with Friendly Interface
@app.route('/')
def home():
    return render_template('index.html')

# Perform Static Analysis
def static_analysis(code):
    with open('temp_code.py', 'w') as f:
        f.write(code)
    result = subprocess.run(['pylint', '--disable=all', '--enable=E,F', 'temp_code.py'], capture_output=True, text=True)
    return result.stdout if result.stdout else "No critical issues detected!"

# Send Async Request to Hugging Face API
async def async_request(payload):
    async with aiohttp.ClientSession() as session:
        async with session.post(API_URL, headers=HEADERS, json=payload) as response:
            result = await response.json()
            return result[0]['generated_text'] if isinstance(result, list) else "No feedback available."

# Analyze Code Route
@app.route('/analyze', methods=['POST'])
async def analyze():
    try:
        code = request.form.get('code', '')
        user_input = request.form.get('user_input', '')

        if not code:
            return render_template('error.html', message="Oops! You forgot to add your code.")
        
        # Detect and replace multiple input() calls with user input
        user_inputs = user_input.split(',')
        input_count = len(re.findall(r'\binput\s*\(', code))
        
        if len(user_inputs) < input_count:
            return render_template('error.html', message=f"Not enough inputs provided. Expected {input_count}, but got {len(user_inputs)}.")
        elif len(user_inputs) > input_count:
            return render_template('error.html', message=f"Too many inputs provided. Expected {input_count}, but got {len(user_inputs)}.")

        # Replace input() calls with provided values
        for user_value in user_inputs:
            code = re.sub(r'input\(\)', f'"{user_value.strip()}"', code, 1)
        
        # Perform Static Analysis
        static_result = static_analysis(code)
        
        # Benchmark Code Execution
        try:
            start_time = time.time()
            exec_globals = {}
            exec(code, exec_globals)
            exec_time = f"The code ran in {time.time() - start_time:.4f} seconds."
            exec_output = exec_globals.get('output', 'Code executed successfully!')
        except Exception as runtime_error:
            exec_time = f"Oops! Your code had an error: {str(runtime_error)}"
            exec_output = str(runtime_error)
        
        # Perform Async API Requests for AI Feedback and Explanation
        feedback_payload = {"inputs": code}
        explanation_payload = {"inputs": f"Explain this code like I'm 10: {code}"}
        
        feedback_task = asyncio.create_task(async_request(feedback_payload))
        explanation_task = asyncio.create_task(async_request(explanation_payload))
        
        ai_feedback, explanation = await asyncio.gather(feedback_task, explanation_task)
        
        return render_template('result.html', static_analysis=static_result, execution_time=exec_time, code_output=exec_output, ai_feedback=ai_feedback, code_explanation=explanation)
    
    except Exception as e:
        return render_template('error.html', message=str(e))

if __name__ == '__main__':
    app.run(debug=True, use_reloader=False)
