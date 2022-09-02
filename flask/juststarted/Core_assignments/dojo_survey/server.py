from flask import Flask, render_template, session, redirect, request# Import Flask to allow us to create our app
app = Flask(__name__)  
app.secret_key = "yeah"




@app.route('/')          # The "@" decorator associates this route with the function immediately following
def html_table():
    return render_template('index.html')


@app.route('/user_info', methods = ['post'] )
def form_submit():
    session['name'] = request.form ['name']
    session['location'] = request.form ['location']
    session['language'] = request.form ['lang']
    session['comment'] = request.form ['comment']
    return redirect('/results')

# @app.route("/test", methods =["posts"])
# def

@app.route('/results')
def dashboard_results():
    return render_template('dashboard.html')


if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.