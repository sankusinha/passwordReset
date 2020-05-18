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
                  withCredentials([usernamePassword(credentialsId: 'admin' , passwordVariable: 'pass', usernameVariable: 'user')]) {
                    def changePassword = { username, new_password ->
                        def creds = com.cloudbees.plugins.credentials.CredentialsProvider.lookupCredentials(
                            com.cloudbees.plugins.credentials.common.StandardUsernameCredentials.class,
                            Jenkins.instance
                        )

                        def c = creds.findResult { it.username == username ? it : null }

                        if ( c ) {
                            println "found credential ${c.id} for username ${c.username}"

                            def credentials_store = Jenkins.instance.getExtensionList(
                                'com.cloudbees.plugins.credentials.SystemCredentialsProvider'
                                )[0].getStore()

                            def result = credentials_store.updateCredentials(
                                com.cloudbees.plugins.credentials.domains.Domain.global(), 
                                c, 
                                new UsernamePasswordCredentialsImpl(c.scope, c.id, c.description, c.username, new_password)
                                )

                            if (result) {
                                println "password changed for ${username}" 
                            } else {
                                println "failed to change password for ${username}"
                            }
                        } else {
                        println "could not find credential for ${username}"
                        }
                }

                changePassword('BillHurt', 's3crEt!')
              }
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