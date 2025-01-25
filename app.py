from flask import Flask, render_template
import aws_config

app = Flask(__name__)

@app.route('/')
def index():
    # Call AWS EC2 scanning function
    ec2_instances = aws_config.scan_ec2_instances()
    return render_template('index.html', ec2_instances=ec2_instances)

if __name__ == '__main__':
    app.run(debug=True)
