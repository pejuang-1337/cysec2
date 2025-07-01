from flask import Flask, render_template, request
from modules import osint, webscan, soceng, location_tracker

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/run', methods=['POST'])
def run_tool():
    tool = request.form['tool']
    target = request.form.get('target', '')
    result = ""

    if tool == 'osint':
        result = osint.run_osint(target)
    elif tool == 'webscan':
        result = webscan.run_scan(target)
    elif tool == 'soceng':
        result = soceng.run_soceng(target)
    elif tool == 'location':
        result = location_tracker.run_location_tracker(target)

    return render_template('result.html', tool=tool, result=result)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)