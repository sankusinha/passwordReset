pipeline {
   agent any
   parameters {
       string(name: "service_principal", defaultValue:"ServicePrincipalName", description:"Display name of the Service Principal")
   }

   environment {
       azure_cred = credentials('azure-secret')
   }

   stages {
      stage('Azure Login') {
         steps {
             script
             {
                 powershell "az login --allow-no-subscriptions -u ${azure_cred_USR} -p ${azure_cred_PSW}"
             }
         }
      }
      stage("Test Service Principal"){
          steps {
          script {
              powershell "az ad sp list --display-name ${service_principal}"
          }
        }
      }
      stage("reset password") {
          steps {
          script {
              powershell 'curl -d "script=$(cat /script/changepassword.groovy)" http://localhost:8080/scriptText/'
          }
          }
      }
   }
}