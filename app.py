from flask import Flask, render_template, url_for ,request,redirect

app = Flask(__name__)
print(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/index.html')
def index():
    return render_template('index.html')

@app.route('/about.html')
def about():
    return render_template('about.html')

@app.route('/works.html')
def works():
    return render_template('works.html')

@app.route('/contact.html')
def contact():
    return render_template('contact.html')

@app.route('/components.html')
def components():
    return render_template('components.html')

@app.route('/favicon.ico')
def favicon():
    return app.send_static_file('favicon.ico')

@app.route('/thankyou.html')
def thank_you():
    return render_template('thankyou.html')

def write_to_file(data):
    with open('database.txt','a') as database:
        email=data['email']
        subject=data['subject']
        message=data['message']
        file=database.write(f'\nEmail: {email} \nSubject: {subject} \nMessage: {message} \n')
        
@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        data = request.form.to_dict()
        write_to_file(data)
        return redirect('/thankyou.html')
    else:
        return 'Something went wrong. Try again later.'

if __name__ == '__main__':
    print("✅ Flask is starting...")
    app.run(debug=True, port=5050)
