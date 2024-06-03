

from flask import Flask, render_template

# Create a Flask application instance
app = Flask(__name__)

# Define a route for the root path ('/')
@app.route('/')
def index():
  """Render the index.html template"""
  # Pass any variables you want to access in the template here (optional)
  return render_template("index.html")

# Run the development server (only if script is run directly)
if __name__ == '__main__':
  app.run(debug=True)
