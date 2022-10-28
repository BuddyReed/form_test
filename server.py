from flask import Flask, render_template, request, redirect, session  # Import Flask to allow us to create our app
app = Flask(__name__)    # Create a new instance(object) of the Flask class called "app" basically assingmnet Flask class to app
app.secret_key = 'kepp it secret, keep it safe'
# @app.route('/')          # The "@" decorator associates this route with the function immediately following
# def hello_world():
#     return 'Hello Buddy!'  # Return the string 'Hello World!' as a response

@app.route('/') #This forward / is the route of the web page
def index():
    return render_template("index.html") 

@app.route("/users", methods=['POST'])
def create_user():
    print('Got Post Info')
    print(request.form)
#     name = request.form['name']
#     name = request.form['email']
#     session['username'] = request.form['name']
#     session['useremail'] = request.form['email']
#     return redirect('/')

# app.route('/show')
# def show_user():
#     print('Showing the User Info From the Form')
#     print(request.form)
#     return redirect('/show')




if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.





