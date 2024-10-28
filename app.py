from flask import Flask, send_from_directory

app = Flask(__name__, static_folder='.')

@app.route('/')
def serve_index():
    return send_from_directory('.', 'index.html')

@app.route('/style.css')
def serve_css():
    return send_from_directory('.', 'style.css')

@app.route('/assets/<path:filename>')
def serve_assets(filename):
    return send_from_directory('assets', filename)

if __name__ == '__main__':
    app.run(port=8082)
