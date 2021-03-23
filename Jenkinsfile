pipeline {
  environment {
    JENKINS_CRED = "${PROJECT}"
    IMAGE = "ghcr.io/mysticrenji/python-flask"
    TOKEN= 'CRPAT'
    GITHUBCR="ghcr.io"
    OWNER = "mysticrenji"
  }
  agent {
    kubernetes {
      label 'kubernetes'
      defaultContainer 'jnlp'
      yaml """
apiVersion: v1
kind: Pod
spec:
  containers:
  - name: docker
    image: docker:1.11
    command: ['cat']
    tty: true
    volumeMounts:
    - name: dockersock
      mountPath: /var/run/docker.sock
  volumes:
  - name: dockersock
    hostPath:
      path: /var/run/docker.sock
"""
}
  }

 stages {
   stage('Build Docker image') {
      steps {
      container('docker') {
        git url: "https://github.com/mysticrenji/flask-mysql-k3s.git",  branch: 'main'
        sh "docker build -t ${IMAGE}:latest ."
      }
   }
 }
  stage('Push Docker image') {
      steps {
      container('docker') {
        sh "export CR_PAT=${TOKEN}"
        sh "echo $CR_PAT | docker login ghcr.io -u ${OWNER} --password-stdin"
        sh "docker push ${IMAGE}:latest"
        }
      }
   }
 }
 }
