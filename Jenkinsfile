pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                // Checkout the repository
                git 'https://github.com/Kobe24ever/WorldOfGames.git'
            }
        }
        stage('Build') {
            steps {
                // Build your Docker image
                sh 'docker build -t games_img .'
            }
        }
        stage('Run') {
            steps {
                // Run your Dockerized application
                sh 'docker run -d -p 8777:8777 -v Scores.txt:/app/Scores.txt --name games_cont games_img'
            }
        }
        stage('Test') {
            steps {
                // Run your Selenium tests
                sh 'python e2e.py'
            }
        }
        stage('Finalize') {
            steps {
                // Stop and remove the Docker container
                sh 'docker stop games_cont'
                sh 'docker rm games_cont'

                // Push the Docker image to DockerHub
                sh 'docker push games_img'
            }
        }
    }
}
