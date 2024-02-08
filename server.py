from flask import Flask, render_template, redirect, request
app = Flask(__name__)
from user import User
    
@app.route('/')
def new_user_register():
    return render_template('index.html')

@app.route('/users')
def display_users():
    all_users = User.get_all_users()
    return render_template('show.html', all_users = all_users)

@app.route ('/create_user',methods=["POST"])
def create_user():
    data = {
        'first_name': request.form['first_name'],
        'last_name': request.form['last_name'],
        'email': request.form['email']
    }
    User.save_user(data)
    return redirect('/')





if __name__=="__main__":
    app.run(debug=True)