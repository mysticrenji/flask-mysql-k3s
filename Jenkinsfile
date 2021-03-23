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
   stage('Cleanup'){
    steps{
      container('docker') {
        sh '''
        docker rmi $(docker images -f 'dangling=true' -q) || true
        docker rmi $(docker images | sed 1,2d | awk '{print $3}') || true
        '''
      }
    }
   }
   stage('Build Docker image and Push to Container Registry') {
      steps {
      container('docker') {
        git url: "https://github.com/mysticrenji/flask-mysql-k3s.git",  branch: 'main'
        sh ('docker login -u $TOKEN_USR -p $TOKEN_PSW $GITHUBCR')
        sh ('docker build -t $IMAGE:latest .')
        sh ('docker push ${IMAGE}:latest')
      }
   }
 }

 }
 }
