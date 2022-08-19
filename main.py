from flask import abort, request
from flask import Flask, render_template

app = Flask(__name__)

blacklist = ["1.1.1.1", "255.255.255.255"]

@app.before_request
def limit_remote_addr():
    if request.remote_addr in blacklist:
        abort(403)  # Forbidden

@app.errorhandler(404)
def page_not_found(error):
	app.logger.error(error)
	return render_template('404.html'), 404

@app.route('/')
def index():
    return render_template('index.html')
    
if __name__ == '__main__':
    app.run(port=5000, debug=False)