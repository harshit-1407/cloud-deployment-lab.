# Cloud Deployment Lab

## Objective
To containerize and deploy a Flask web application
using GitHub, Docker, and AWS EC2.

## Application Details
- Developer: Harshit Bansal
- Framework: Python Flask
- Application Version: 1.0.0
- Containerization: Docker
- Cloud Platform: AWS EC2

## Run Locally
1. Install Docker Desktop.
2. Build the image:
   docker build -t cloud-deployment-lab .
3. Run the container:
   docker run -d --name cloud-lab -p 5000:5000 cloud-deployment-lab
4. Open http://localhost:5000

## Deployment
The Docker image is built and run on an AWS EC2
Ubuntu instance. HTTP traffic is permitted through
the EC2 security group on port 80.

## Troubleshooting
Document the actual errors encountered and their
solutions during local testing and cloud deployment.