# Cloud-Service-Misconfiguration-Scanner

This project is a simple Flask-based web application that scans AWS resources for potential misconfigurations. It currently supports scanning the following AWS services:
- **EC2 Instances**: Retrieves information about instance states and public IPs.
- **S3 Buckets**: Lists available buckets.
- **RDS Instances**: Lists database instance identifiers.

---

## Features
- **EC2 Scanner**: Lists instance ID, type, state, and public IP.
- **S3 Scanner**: Displays all available S3 bucket names.
- **RDS Scanner**: Displays identifiers of all RDS instances.
- **Web Interface**: Results are displayed on a user-friendly dashboard built using Flask and Jinja2 templates.

---

## Prerequisites
Before running this project, ensure you have the following:
1. **Python 3.9+** installed on your machine.
2. **AWS Account** with IAM permissions for:
   - EC2 (`ec2:DescribeInstances`)
   - S3 (`s3:ListAllMyBuckets`)
   - RDS (`rds:DescribeDBInstances`)
3. **AWS CLI** installed and configured:
   - Run `aws configure` to set up your AWS credentials.
4. **Python Libraries** installed as listed in `requirements.txt`.

---

## Installation and Setup
1. **Clone the Repository**:
   ```bash
   git clone https://github.com/rajanarahul93/Cloud-Service-Misconfiguration-Scanner-Jazzee-Technologies-Task.git
   cd Cloud-Service-Misconfiguration-Scanner-Jazzee-Technologies-Task
   ```

2. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure AWS**:
   - Use the AWS CLI to configure your credentials:
     ```bash
     aws configure
     ```
   - Ensure your AWS user has the required IAM permissions.

4. **Edit Configuration** (Optional):
   - Open `config.json` and verify or update the AWS region and security group IDs:
     ```json
     {
       "aws_region": "us-east-1",
       "ec2_security_groups": ["sg-12345", "sg-67890"]
     }
     ```

5. **Run the Application**:
   ```bash
   python app.py
   ```

6. **Access the Application**:
   - Open your browser and navigate to: [http://127.0.0.1:5000](http://127.0.0.1:5000).

---

## File Structure
```
aws-misconfiguration-scanner/
│
├── app.py                # Main Flask application
├── aws_config.py         # AWS scanning functions
├── config.json           # AWS configuration file
├── requirements.txt      # Python dependencies
├── templates/
│   └── index.html        # HTML template for the dashboard
└── README.md             # Project documentation
```

---

## Technologies Used
- **Python**: Core programming language.
- **Flask**: Lightweight web framework.
- **Boto3**: AWS SDK for Python to interact with AWS services.
- **Jinja2**: Template engine for rendering dynamic web pages.
- **HTML/CSS**: For creating the user interface.

---

## Known Issues
- Ensure you have valid AWS credentials and permissions.
- If you face issues related to `boto3` or region configuration, verify `config.json` and your AWS CLI settings.

---

## Future Enhancements
- Add detailed scanning for S3 bucket policies.
- Include IAM role misconfiguration checks.
- Enhance the web interface with additional visualization tools like **Plotly**.
