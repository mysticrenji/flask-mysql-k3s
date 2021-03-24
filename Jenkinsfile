pipeline {
  environment {
    IMAGE = "ghcr.io/mysticrenji/flask-mysql-k3s"
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
   stage('Build Docker image and Push to Container Registry') {
      steps {
      container('docker') {
        withCredentials([[$class: 'UsernamePasswordMultiBinding', credentialsId:'GitHub',
        usernameVariable: 'USERNAME', passwordVariable: 'PASSWORD']])
        {
        git url: "https://github.com/mysticrenji/flask-mysql-k3s.git",  branch: 'main'
        sh '''
        export CR_PAT=$PASSWORD'
        echo $CR_PAT | docker login $GITHUBCR -u $USERNAME --password-stdin
        docker build -t $IMAGE:latest .
        docker push ${IMAGE}:latest
        '''
        }
      }
   }
 }

 }
 }
