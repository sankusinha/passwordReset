import com.cloudbees.plugins.credentials.impl.UsernamePasswordCredentialsImpl
pipeline {
   agent {
       node {
           label "master"
           customWorkspace "c:/jk_workspace"
       }
   }
   parameters {
       string(name: "service_principal", defaultValue:"ServicePrincipalName", description:"Display name of the Service Principal")
       booleanParam(name: 'RESET_ADUSER', defaultValue: false, description: "Tochange the ADUSER Password")
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
      stage("Test Powershell condition") {
          steps {
              script {
                  powershell '''
                    \$t="abc"
                    if($t -eq "xyz") {
                        Write-Output \$t
                    }
                    else {
                        Write-Output "Not match"
                    }

                  '''
              }
          }
      }
      stage("reset password") {
          steps {
              script {
                  powershell """
                    if (${RESET_ADUSER} -eq "false") {
                        Write-Output "false"
                    }
                    else {
                        Write-Output "If condition not checked"
                    }
                  """
              }
          }
      }
   }
   post {
       always {
           echo "Cleaning Workspace"
           deleteDir()
       }
   }
}