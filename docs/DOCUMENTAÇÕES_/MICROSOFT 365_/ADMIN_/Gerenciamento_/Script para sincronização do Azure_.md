AM

**<u>Arquitetura</u>**

Computador local e servidor connecticutw

**<u>Contas de Serviço</u>**

Usuário \*-adm.

**<u>Configurações do Ambiente</u>**

n/a

**<u>Configurações Gerais</u>**

Script executado na máquina local. Solicita as credenciais do usuário \*-adm e cria uma sessão no servidor connecticutw para iniciar um novo ciclo de sincronização com o Azure. Script disponível no SharePoint da infra ou executar no ISE:

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

**<u>Últimas atualizações</u>**  

| Editor            | Data       | Motivo                  | Alteração |
|-------------------|------------|-------------------------|-----------|
| André Luiz Fronza | 24/11/2023 | Criação da documentação |          |
| Thiago Leite      | 11/04/2024 | Adicionado script       |           |
|                   |            |                         |           |
|                   |            |                         |           |
|                   |            |                         |           |

