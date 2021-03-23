pipeline {
  environment {
    IMAGE = "ghcr.io/mysticrenji/flask-mysql-k3s"
    TOKEN= credentials('GitHub')
    GITHUBCR="ghcr.io"
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
        sh "docker build -t ${IMAGE}:v1 ."
      }
   }
 }
  stage('Push Docker image') {
      steps {
      container('docker') {
        //sh('export CR_PAT=$TOKEN_PSW')
        //sh('echo $CR_PAT | docker login ghcr.io -u $TOKEN_USR --password-stdin')
        sh "docker login -u $TOKEN_USR -p $TOKEN_PSW $GITHUBCR"
        sh "docker push ${IMAGE}:latest"
        }
      }
   }
 }
 }
