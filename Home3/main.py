from flask import Flask, render_template, request, redirect, make_response

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/welcome', methods=['POST'])
def welcome():
    name = request.form['name']
    email = request.form['email']

    responce = make_response(redirect('/hello'))
    responce.set_cookie('user_name', name)
    responce.set_cookie('user_email', email)

    return responce


@app.route('/hello')
def hello():
    user_name = request.cookies.get('user_name')
    user_email = request.cookies.get('user_email')
    if user_name:
        return render_template('hello.html', name=user_name, email=user_email)
    return redirect('/')

@app.route('/logout', methods=['GET','POST'])
def logout():
    response = make_response(redirect('/'))
    response.delete_cookie('user_name')
    response.delete_cookie('user_email')
    return response


if __name__ == '__main__':
    app.run(debug=True)