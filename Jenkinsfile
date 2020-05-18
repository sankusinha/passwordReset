pipeline {
   agent {
       node {
           label "master"
           customWorkspace "c:/jk_workspace"
       }
   }
   parameters {
       string(name: "service_principal", defaultValue:"ServicePrincipalName", description:"Display name of the Service Principal")
   }

   environment {
       azure_cred = credentials('az-secret')
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
                def passChange = load "./script/changepassword.Groovy"
                passChange.changePassword('az-secret', 'G1t@nj@l1')
              }
          }

      }
      stage("Cleanup workspace") {
          deleteDir()
      }
   }
}