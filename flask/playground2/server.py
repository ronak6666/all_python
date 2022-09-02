from flask import Flask,render_template # Import Flask to allow us to create our app
app = Flask(__name__)    # Create a new instance of the Flask class called "app"
@app.route('/box/<int:num>/<color>')          # The "@" decorator associates this route with the function immediately following
def hello_world(num,color):
    return render_template("index.html", num=num, color=color) 
    
@app.route('/')          # The "@" decorator associates this route with the function immediately following
def something():
    return render_template("index.html") # Return the string 'Hello World!' as a response
if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.

