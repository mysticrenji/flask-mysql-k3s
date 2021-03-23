podTemplate(yaml: """
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
  ) {


  node(POD_LABEL) {
    def image = "ghcr.io/mysticrenji/python-flask"
    githubtoken= 'GitHub'
    stage('Build Docker image') {
      container('docker') {
        sh "docker build -t ${image} ."
      }
    }

  }
}
