# TAQC_T3

Test automation using Playwright to perform a complete checkout flow in an online store.

---

## Goals

The goal of this project is to automate the online store purchasing process, from new user registration to checkout, ensuring that each step runs smoothly.

---

## Technologies used

- **Playwright** – Test automation framework.
- **Python** – Programming language.
- **Git** – Version control.
- **Docker** – Containerization.
- **Jenkins** – CI/CD

---

## Individual Automation Flow

1. **User Registration:** Create a new account in the online store.
2. **Login:** Authenticate with the registered user's credentials.
3. **Product Search:** Locate a specific product in the store.
4. **Add to Cart:** Add a specific quantity of the product to the shopping cart.
5. **Checkout:** Complete the product checkout process.

---

## Installation and Launch

1. Clone the repository:

```bash
git clone https://github.com/PedroRamirez01/TAQC_T3.git
cd TAQC_T3
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Run the tests:

```bash
pytest --html=ecomus/report/report.html --self-contained-html
```

---

## Jenkins + Docker Setup

This project uses a custom Jenkins Docker environment that comes pre-installed with Python, Playwright, and all the necessary dependencies for test automation.

### What's Included in Our Docker Setup
- Jenkins LTS as base image
- Python 3 environment with virtual environment 
- Pre-installed Playwright with browser dependencies
- Automatic handling of test dependencies
- Secure configuration with proper user permissions

### Step 1: Launch Jenkins

```bash
docker-compose up -d
```

This single command builds the Docker image and starts the Jenkins container with all necessary components.

### Step 2: Access Jenkins UI

Open your browser and go to:
```
http://localhost:8080
```

To get the initial admin password:
```bash
docker exec jenkins cat /var/jenkins_home/secrets/initialAdminPassword
```

### Step 3: Create a 'TOKEN' Credential And Download Plugin 'HTML Publisher'

In the Jenkins web interface:

1. Go to Manage Jenkins > Credentials.
2. Select the credential store.
3. Create a new credential:
   - Type: Secret text
   - Scope: Global
   - ID: TOKEN
   - Secret: ****************
4. Go to Manage Jenkins > Plugins > Available plugins.
5. Search 'HTML Publisher' and Download

### Step 4: Configure a Job (Pipeline)

1. Create a new item in Jenkins and select **Pipeline**.
2. Check the **GitHub project** option and enter:
   ```
   https://github.com/PedroRamirez01/TAQC_T3.git
   ```
3. In the **Pipeline** section:
   - **Definition**: `Pipeline script from SCM`
   - **SCM**: `Git`
   - **Repository URL**:
      ```
      https://github.com/PedroRamirez01/TAQC_T3.git
      ```
   - **Branches to build**:
      ```
      */main
      ```

### Step 5: Run the Job

Click **"Build Now"** to run the pipeline. The pipeline will execute the following stages:
- Checkout from source control
- Activate Python virtual environment
- Update dependencies (if necessary)
- Run end-to-end tests
- Generate HTML reports

### Step 6: View Test Reports

Once the pipeline completes, you can view the generated reports in the Jenkins workspace:
```
ecomus/report/report.html
```

### Docker Image Details

Our custom Docker image (`Dockerfile`) extends the official Jenkins LTS image with:

```dockerfile
# Base image
FROM jenkins/jenkins:lts

# Python environment setup
RUN python3 -m venv venv

# Dependencies pre-installation
COPY requirements.txt /var/jenkins_home/workspace/
RUN venv/bin/pip install -r requirements.txt

# Playwright installation with browsers
RUN venv/bin/playwright install --with-deps chromium
```

This ensures a consistent and reproducible test environment for all team members and CI/CD processes.
