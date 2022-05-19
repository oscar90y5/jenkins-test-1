
def remote = [:]
remote.name = 'test'
remote.host = 'pro-server'
remote.user = 'test'
remote.password = 'test'

pipeline {
  agent any
  stages {
    stage('Test') {
      steps {
        sh 'python3 test.py'
      }
    }
    stage('Deploy') {
      when {
        branch 'main'
      }
      steps {
        sshScript remote: remote, script: "deploy.sh"
      }
    }
  }
}
