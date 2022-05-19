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
