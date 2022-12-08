pipeline {
  agent any    
  stages {
    stage('QA Sanity Test') {
      steps {
         sh 'python3 reflect_run.py'
      }
    }
  }
  post {
        always {
          emailext body: "${currentBuild.currentResult}: Job ${env.JOB_NAME} build ${env.BUILD_NUMBER}\n More info at: ${env.BUILD_URL}",
                recipientProviders: [[$class: 'DevelopersRecipientProvider'], [$class: 'RequesterRecipientProvider']],
                mail to: 'vin402@gmail.com, arun.ramesh@mosaicwellness.in, abhay.kaintura@mosaicwellness.in, tejaswini.gowda@mosaicwellness.in',
                subject: "Jenkins Build ${currentBuild.currentResult}: Job ${env.JOB_NAME}"
            }
    }
}
