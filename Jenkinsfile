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
       booleanParam(name: "RESET_ADUSER", defaultValue: false, description: "Tochange the ADUSER Password")
       //choice choices: ['yes','no'], description: "Need to change AD user password?", name: 'RESET_ADUSER'
   }

   environment {
       azure_cred = credentials('az-secret')
       CH_ADUSER = "${params.RESET_ADUSER}"
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
                    \$oldPassword = "Sanku#1Nupur"
                    if ("${env:CH_ADUSER}" -eq "false") {
                        Write-Output "false"
                    }
                    else {
                        Install-Module MSOnline -Force -Confirm:\$false
                        Import-Module 'C:/Program Files/WindowsPowerShell/Modules/MSOnline/1.1.183.57/MSOnline.psd1'
                        add-type -AssemblyName System.Web
                        \$secret=[System.Web.Security.Membership]::GeneratePassword(20,5)
                        Write-Output \$secret
                        Update-AzureADSignedInUserPassword -CurrentPassword \$oldPassword -NewPassword \$secret
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