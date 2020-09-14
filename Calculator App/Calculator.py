# Import required libraries/methods/packages
from flask import Flask, render_template, request

calculator = Flask(__name__)


def calc(app):

    @app.route('/')   # To start the server with initial template
    def main():
        return render_template('calc_front_end.html')

    @app.route('/send', methods=['POST'])  # To pass the input to the server
    def send():
        if request.method == 'POST':
            num1 = request.form['num1']     # First input
            num2 = request.form['num2']     # Second input
            try:
                # Input should be numeric
                float(num1)
                float(num2)
            except ValueError :
                # If not numeric throw error
                return render_template('calc_front_end.html', result='Value Error :Input should be numeric')

            operation = request.form['operation']   # Operand to perform calculation

            if operation == 'add':     # addition logic
                result = float(num1) + float(num2)
                # str_result = str(float(num1)) + '+' + str(float(num2)) + '=' + str(result)
                return render_template('calc_front_end.html', result=result)

            elif operation == 'subtract':    # subtraction logic
                result = float(num1) - float(num2)
                return render_template('calc_front_end.html', result=result)

            elif operation == 'multiply':    # multiplication logic
                result = float(num1) * float(num2)
                return render_template('calc_front_end.html', result=result)

            elif operation == 'divide':      # division logic
                try:       # should not divide by zero
                    result = float(num1) / float(num2)
                    return render_template('calc_front_end.html', result=result)
                except ZeroDivisionError :
                    return render_template('calc_front_end.html', result='Zero Division Error :Sorry ! You are dividing by zero')
            else:
                return render_template('calc_front_end.html')


if __name__ == '__main__':
    calculator.debug = False
    calc(calculator)
    calculator.run()
