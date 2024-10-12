
# :card_index_dividers: Spam Mail Detection using NLP and MLOps

Hello there. This mini project takes an email content as input and predicts whether it is spam or not. It uses NLP to convert text into numericals. It is powered by MLOps facilitated by Github CI/CD and Docker. 


![image](https://github.com/user-attachments/assets/70ee1b37-c97d-47ac-8aa5-b160b949d058)

NOTE: As the purpose of this project was to dive into MLOps , I did not stress much on the UI of the app.

## :sparkles: Features of project

- Uses NLP and ML (Multinomial Naive Bayes) to convert and classify text as spam or not spam.

- Flask used to provide UI and server functionalities.

- Docker used to containerize the Flask app.

- Used Github Actions to facilitate CI/CD pipelining.

- Pytest used to run unit tests on the app. 


## :computer: Installation

You must have Docker pre-installed in your computer.

For installing Docker, click [here](https://www.docker.com/get-started/).


After you have docker installed, follow the given steps:


1. Pull this project's image into your machine

     `docker pull bhuv2003/flask-app`

2. Now run the container using the following command 

    `docker run -d -p 5000:5000 bhuv2003/flask-app:latest`

3. Enter `http://localhost:5000/` on your web browser to see the app running.


4. To stop the container , first find the container id using `docker ps` and then stop the container using `docker stop <container_id>`





