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
pytest --html=login/report/report.html --self-contained-html
```

---

## Jenkins + Docker Setup

This project uses Jenkins inside a Docker container to automate integrations and deployments.

### Step 1: Launch Jenkins

```bash
sudo docker-compose build
sudo docker-compose up -d
```

### Step 2: Create a 'TOKEN' Credential

In the Jenkins web interface (http://localhost:8080):

1. Go to Manage Jenkins > Credentials.
2. Select the credential store.
3. Create a new credential:
   - Type: Secret text
   - ID: TOKEN
   - Secret: ****************

### Paso 3: Configurar un Job (Pipeline)

1. Crea un nuevo ítem en Jenkins y selecciona **"Pipeline"**.
2. Marca la opción **GitHub project** y coloca:
   ```
   https://github.com/PedroRamirez01/TAQC_T3.git
   ```
3. En la sección **Pipeline**:
   - **Definition**: `Pipeline script from SCM`
   - **SCM**: `Git`
   - **Repository URL**:
     ```
     https://github.com/tu-usuario/TAQC_T3.git
     ```
   - **Branches to build**:
     ```
     */main
     ```

### Step 3: Configure a Job (Pipeline)

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

### Step 4: Run the Job

Click **"Build Now"** to run the pipeline.
