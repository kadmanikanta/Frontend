# app.py
from flask import Flask, render_template, request

app = Flask(__name__)

# Route to display the registration form
@app.route('/')
def index():
    return render_template('index.html')  # Renders the index page (index.html)

# Route to handle form submission
@app.route('/submit', methods=['POST'])
def submit():
    if request.method == 'POST':
        # Collect form data using request.form
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        email = request.form['email']
        dob = request.form['dob']
        username = request.form['username']
        password = request.form['password']
        gender = request.form['gender']
        course = request.form['course']

        # Conditional logic based on the selected course
        if course == 'ML':  # Machine Learning selected
            message = "You selected Machine Learning! Please specify your experience with ML tools."
            show_ml_field = True  # Boolean to show the additional ML-specific field
        else:
            message = "You have selected a different course."
            show_ml_field = False  # No additional fields for other courses

        # Process the data (for example, save to a database or show it)
        # For now, we'll just print the data to the console
        print(f"First Name: {first_name}")
        print(f"Last Name: {last_name}")
        print(f"Email: {email}")
        print(f"Date of Birth: {dob}")
        print(f"Username: {username}")
        print(f"Password: {password}")
        print(f"Gender: {gender}")
        print(f"Course: {course}")

        # Redirect to the success page or show a success message with context
        return render_template('successful.html', message=message, show_ml_field=show_ml_field)

if __name__ == '__main__':
    app.run(debug=True)
