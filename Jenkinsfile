pipeline {
  agent any
  stages {
    stage('Test') {
      steps {
        sh 'python3 test.py'
      }
    }
    script {
      def remote = [:]
      remote.name = 'test'
      remote.host = 'pro-server'
      remote.user = 'test'
      remote.password = 'test'
      sshScript remote: remote, script: "deploy.sh"
    }
    #stage('Deploy') {
    #  when {
    #    branch 'main'
    #  }
    #  steps {
    #    sshScript remote: remote, script: "deploy.sh"
    #  }
    #}
  }
}
