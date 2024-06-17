### Beginner Friendly Course: Deploying a Python Hello World Web Server with Docker and Kubernetes (Stretch Goal)

---

#### **Course Overview:**

This course is designed for a 15-year-old student on work experience to learn the basics of deploying a Python web server. It introduces containerization with Docker and, as a stretch goal, touches on Kubernetes for orchestration. The course is structured into simple, manageable steps with practical exercises, spanning a week with approximately 15 hours of content.

---

### **Day 1: Introduction to Web Servers and Python (3 hours)**

**Objective:** Understand what a web server is and create a simple "Hello World" web server using Python.

1. **Introduction to Web Servers (1 hour)**
    - **Explanation of Web Servers:** Discuss what web servers are, their role in serving web pages, and how they work (e.g., receiving requests and sending responses).
    - **Real-World Examples:** Show examples like Apache, Nginx, and lightweight servers used in development.
    - **Interactive Activity:** Have the student research a few popular web servers and their use cases.

2. **Setting Up Python (1 hour)**
    - **Installing Python:**
      - **Windows:** Download and install Python from [python.org](https://www.python.org/downloads/).
      - **Mac/Linux:** Use the terminal to install Python (e.g., `brew install python` for Mac, `sudo apt-get install python3` for Linux).
    - **Introduction to Python Environment:**
      - **IDLE:** Walk through using Python’s Integrated Development and Learning Environment.
      - **VS Code:** Introduction to using VS Code for writing Python code, including installing the Python extension.

3. **Creating a Simple Web Server (1 hour)**
    - **Writing the Code:**
      - Guide the student through writing a simple "Hello World" web server using Python's `http.server` module. Explain each part of the code.
    - **Running the Server:**
      - Show how to run the Python script from the command line.
      - **Testing:** Open a web browser and navigate to `http://localhost:8080` to see the "Hello, World!" message.
    - **Interactive Exercise:** Modify the message to display the student's name or a custom message.

```python
# hello.py
from http.server import BaseHTTPRequestHandler, HTTPServer

class HelloHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(b"Hello, World!")

def run(server_class=HTTPServer, handler_class=HelloHandler, port=8080):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f"Server running on port {port}")
    httpd.serve_forever()

if __name__ == "__main__":
    run()
```

---

### **Day 2: Introduction to Docker and Containerization (3 hours)**

**Objective:** Understand containerization and create a Docker container for the Python web server.

1. **What is Docker? (1 hour)**
    - **Explanation of Docker and Containers:**
      - Discuss the concept of containerization and how it differs from traditional virtualization.
      - Benefits of using Docker (e.g., consistency across environments, isolation, efficiency).
    - **Real-World Examples:**
      - Examples of companies or projects using Docker.
    - **Interactive Activity:** Have the student explore Docker's official website and note down key benefits and use cases.

2. **Installing Docker (1 hour)**
    - **Guide to Install Docker:**
      - **Windows/Mac:** Use Docker Desktop.
      - **Linux:** Use the terminal to install Docker (e.g., `sudo apt-get install docker-ce`).
    - **Post-Installation Setup:**
      - Basic Docker commands (`docker --version`, `docker info`).
    - **Interactive Exercise:** Run a test container (e.g., `docker run hello-world`) to verify the installation.

3. **Creating a Dockerfile (1 hour)**
    - **Introduction to Dockerfile:**
      - Explain what a Dockerfile is and its purpose.
      - Walk through each line of the Dockerfile provided for the Python web server.
    - **Building and Running Docker Container:**
      - Show how to build a Docker image using `docker build -t hello-world-app .`.
      - Run the Docker container with `docker run -p 8080:8080 hello-world-app`.
      - **Testing:** Access the web server in the browser using `localhost:8080`.
    - **Interactive Exercise:** Modify the Dockerfile to use a different base image or add additional files.

```dockerfile
# Dockerfile
FROM python:3.9-slim

WORKDIR /app

COPY hello.py .

CMD ["python", "hello.py"]
```

---

### **Day 3: Basics of Kubernetes (Stretch Goal) (3 hours)**

**Objective:** Understand the basics of Kubernetes and deploy the Dockerized web server on a local Kubernetes cluster.

1. **Introduction to Kubernetes (1 hour)**
    - **Explanation of Kubernetes:**
      - Discuss the role of Kubernetes in container orchestration.
      - Explain key components: Pods, Nodes, Services, Deployments.
    - **Real-World Examples:**
      - Examples of companies or projects using Kubernetes.
    - **Interactive Activity:** Research a few Kubernetes case studies and note down the benefits observed.

2. **Setting Up Minikube (1 hour)**
    - **Guide to Install Minikube:**
      - Download and install Minikube for running a local Kubernetes cluster.
    - **Post-Installation Setup:**
      - Basic Minikube commands (`minikube start`, `minikube status`).
    - **Interactive Exercise:** Start Minikube and explore the dashboard.

3. **Creating Kubernetes Manifests (1 hour)**
    - **Writing YAML Files:**
      - Explain the purpose of deployment and service manifests.
      - Walk through the provided deployment and service YAML files.
    - **Deploying to Kubernetes:**
      - Commands to deploy the application (`kubectl apply -f deployment.yaml`, `kubectl apply -f service.yaml`).
      - **Testing:** Get the Minikube IP and access the web server using the NodePort.
    - **Interactive Exercise:** Modify the number of replicas in the deployment or change the NodePort.

```yaml
# Deployment Manifest (deployment.yaml)
apiVersion: apps/v1
kind: Deployment
metadata:
  name: hello-world-deployment
spec:
  replicas: 2
  selector:
    matchLabels:
      app: hello-world
  template:
    metadata:
      labels:
        app: hello-world
    spec:
      containers:
      - name: hello-world
        image: hello-world-app
        ports:
        - containerPort: 8080
```

```yaml
# Service Manifest (service.yaml)
apiVersion: v1
kind: Service
metadata:
  name: hello-world-service
spec:
  type: NodePort
  selector:
    app: hello-world
  ports:
    - protocol: TCP
      port: 8080
      targetPort: 8080
      nodePort: 30007
```

```bash
# Start Minikube
minikube start

# Apply the deployment
kubectl apply -f deployment.yaml

# Apply the service
kubectl apply -f service.yaml

# Get Minikube IP
minikube ip

# Access the web server at http://<minikube-ip>:30007
```

---

### **Day 4: Advanced Docker and Kubernetes Concepts (3 hours)**

**Objective:** Deepen the understanding of Docker and Kubernetes by exploring more advanced features and best practices.

1. **Advanced Docker Concepts (1.5 hours)**
    - **Docker Compose:**
      - Introduction to Docker Compose for multi-container applications.
      - Example Docker Compose file to run the web server alongside another service (e.g., a simple database).
    - **Docker Volumes and Networks:**
      - Explanation of persistent storage with Docker volumes.
      - Overview of Docker networks for container communication.
    - **Interactive Exercise:** Create a Docker Compose file and explore volume and network settings.

2. **Advanced Kubernetes Concepts (1.5 hours)**
    - **ConfigMaps and Secrets:**
      - Explanation of ConfigMaps and Secrets for configuration management in Kubernetes.
    - **Health Checks and Probes:**
      - Introduction to liveness and readiness probes for application health monitoring.
    - **Interactive Exercise:** Add ConfigMaps or Secrets to the existing deployment and configure a simple health check probe.

---

### **Day 5: Project Work and Review (3 hours)**

**Objective:** Apply the learned concepts in a project and review the week's work.

1. **Project Extension (2 hours)**
    - **Customizing the Web Server:**
      - Add new features to the Python web server (e.g., a simple form or different endpoints).
    - **Deploying Updates:**
      - Update the Docker image and redeploy the container.
      - Apply updates to the Kubernetes deployment.
    - **Interactive Exercise:** Allow the student to brainstorm and implement a small feature or improvement.

2. **Review and Q&A (1 hour)**
    - **Recap the Week:**
      - Review key concepts from web servers to Docker and Kubernetes.
    - **Answering Questions:**
      - Address any questions or uncertainties the student has.
    - **Discussion:**
      - Discuss potential next steps for learning and exploring more advanced topics.
    - **Feedback Session:**
      - Ask for the student's feedback on the course and any suggestions for improvement.

---

### **Additional

 Resources and Practice**

- **Documentation:**
  - [Python Official Documentation](https://docs.python.org/3/)
  - [Docker Official Documentation](https://docs.docker.com/)
  - [Kubernetes Official Documentation](https://kubernetes.io/docs/)

- **Interactive Tutorials:**
  - [Docker Playground](https://labs.play-with-docker.com/)
  - [Katacoda Kubernetes Playground](https://www.katacoda.com/courses/kubernetes/playground)

---

By following this course, the student will gain a solid foundation in web servers, Docker, and Kubernetes, setting them up for further exploration and learning in the world of DevOps and containerization.
