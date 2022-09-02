from flask import Flask, render_template, session, redirect# Import Flask to allow us to create our app
app = Flask(__name__)  
app.secret_key = "yeah"




@app.route('/')          # The "@" decorator associates this route with the function immediately following
def html_table():
    if "counter" in session:
        session["counter"] += 1
    else:
        session["counter"] = 1
    return render_template('index.html')

@app.route('/destroy_session')
def destroy_dem():
    session.clear()
    return redirect('/')
    




if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.