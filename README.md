# Relinns Test Task 

## Overview

This project leverages **LangChain** and **Hugging Face** to build a question-answering system from web-scraped content and documents (PDFs, web pages, etc.). The system uses **FAISS** for vector storage and retrieval, and **Hugging Face's LLM** for generating answers based on the extracted context.

## Prerequisites

- Docker
- Docker Compose
- Python (for testing outside of Docker)

## Setup Instructions

Follow these steps to get the project up and running using Docker.

### 1. Extract the Project

First, you need to extract or clone the repository to your local machine.

If you have the project as a compressed file, extract it to a directory.

```bash
unzip filename.zip -d /path/to/destination/
```

If you are cloning the repository via Git:

```bash
git clone git@github.com:w7Ali/relinns-test-task.git
cd relinns-test-task.git
```

### 2. Navigate to the Project Directory

Once the project is extracted or cloned, navigate into the project folder:

```bash
cd relinns-testtask
```

### 3. Set Up Environment Variables

You will need to create a `.env` file to store sensitive information, such as your Hugging Face API key.

- **Create a `.env` file** in the root of your project.
- Add your Hugging Face API key to the `.env` file.

Example:

```text
HUGGINGFACE_API_KEY=your_huggingface_api_key_here
```

Replace `your_huggingface_api_key_here` with your actual Hugging Face API key.

### 4. Build and Run the Docker Containers

Now that you have your environment set up, you can use Docker to build and run the application.

Run the following command to build and start the container:

```bash
docker-compose up --build
```

This will:

1. **Build the Docker image** from the `Dockerfile`.
2. **Install dependencies** (as listed in `requirements.txt`).
3. **Start the application** inside a container.

Once the process is complete, your application will be running inside the container.

### 5. Access the Running Container

To interact with the container and run Python scripts, use the following command to open a **bash shell** inside the running container:

```bash
docker exec -it <container_id> bash
```

To get the container ID, run:

```bash
docker ps
```

This will show you a list of running containers. Copy the container ID associated with your project container.

### 6. Run the Python Script (`main.py`)

Inside the container, you can now run your Python test script to check if the application is working as expected.

```bash
python main.py
```

This script will ask you to provide a **URL** and ask **questions** related to it. Once you enter the URL, you will be able to ask questions based on the extracted context.

- **Provide the URL**: Enter the URL of the website you want to scrape.
- **Ask a Question**: Ask questions related to the content scraped from the website.
- **Exit**: Type `exit` to stop the application.

### 7. Stopping the Application

When you're done, you can stop the application by pressing `Ctrl + C` in the terminal where the Docker container is running, or by running the following command to stop and remove the containers:

```bash
docker-compose down
```

This will stop the running containers and remove them, but the Docker images will remain on your system.

---

## Troubleshooting

### Common Issues

- **Hugging Face API Key Missing**: If you didn't set the `HUGGINGFACE_API_KEY` in the `.env` file, the program will fail to connect to Hugging Face. Make sure the `.env` file is present and properly configured.
  
- **Dependencies Not Installing**: If the `docker-compose up --build` fails due to missing dependencies, ensure that `requirements.txt` is installed and includes all the necessary libraries.

- **Docker Not Installed**: Make sure Docker and Docker Compose are installed on your machine. You can check the installation by running:

  ```bash
  docker --version
  docker-compose --version
  ```

---

## Project Structure

The project folder structure should look something like this:

```
/project-name
  ├── images
  ├── Dockerfile
  ├── docker-compose.yml
  ├── requirements.txt
  ├── .env
  ├── main.py
  └── README.md
```

---


## Conclusion

With this setup, you can easily build, run, and query a question-answering system that leverages web scraping and Hugging Face's models—all within Docker containers. This approach provides portability and ease of deployment, making it a versatile solution for any project.

### Screenshots and Test Usage
I have attached screenshots that demonstrate how to test and use the system, along with the source of the data, which is the following website URL:

[Install and Configure Apache Airflow – A Step-by-Step Guide](https://medium.com/orchestras-data-release-pipeline-blog/installing-and-configuring-apache-airflow-a-step-by-step-guide-5ff602c47a36)

### Support
If you encounter any errors or difficulties during setup or installation, feel free to reach out to me for assistance.

**Contact Information:**
- Wahid Ali
- Email: [mr.wahidali7c@gmail.com](mailto:mr.wahidali7c@gmail.com)
- Phone: +91 62392 84784

---

Have a great day
