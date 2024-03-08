from flask import Flask,redirect,render_template,request

def myCalc(NUM1,NUM2,operation):
    if operation == 'add':
        result = NUM1 + NUM2
    elif operation == 'Subtract':
        result = NUM1 - NUM2
    if operation == 'Multiply':
        result = NUM1 * NUM2
    if operation == 'Divide':
        if NUM2 ==0:
            result = 'invalid division by zero'
            return result
        result = NUM1 / NUM2
    return result
    
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    num1 = request.form['num1']
    num2 = request.form['num2']
    operation = request.form['operation']
    
    try:
        N1 = float(num1)
        N2 = float(num2)
        result = myCalc(N1,N2,operation)
        return render_template('index.html' ,result = result)
    
    except Exception as e:
        error_message = f"Error: {str(e)}"
        result = 'error'
        return render_template('index.html' ,result = result)
    

if __name__ == '__main__':
    app.run(debug=True , port = 5001)
