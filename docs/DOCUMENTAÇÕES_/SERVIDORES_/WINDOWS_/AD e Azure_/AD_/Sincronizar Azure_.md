Sincronizar Azure
Wednesday, December 6, 2023
4:51 PM

**<u>Arquitetura</u>**

n/a

**<u>Contas de Serviço</u>**

n/a

**<u>Configurações do Ambiente</u>**

n/a

**<u>Configurações Gerais</u>**

Forçar sincronização com Azure:

\$user = \$env:username
if (!(\$user -match "-adm")){
\$user += "-adm"
}
\$cred = Get-Credential -Username \$user -Message "Credencial sincronização do Azure AD"
\$AzureADConnectserver="connecticutw.frimesa.local"
Invoke-Command -ComputerName \$AzureADConnectserver -Credential \$cred -ScriptBlock {
Import-Module ADSync
Start-ADSyncSyncCycle -PolicyType Delta
}
\$date = Get-Date
Write-Host "\$date"

**<u>Últimas atualizações</u>**  

