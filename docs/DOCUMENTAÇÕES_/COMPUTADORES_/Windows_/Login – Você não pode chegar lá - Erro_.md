Login – Você não pode chegar lá - Erro
Monday, January 15, 2024
9:17 AM

**<u>Arquitetura</u>**

n/a

**<u>Contas de Serviço</u>**

n/a

**<u>Configurações do Ambiente</u>**

n/a

**<u>Configurações Gerais</u>**

**Resolução do erro:**
-Entre com sua conta corporativa
-Você não pode chegar lá a partir daqui

![image1](../../../_resources/image1-7.png)

- Acessar cmd como adm e execute:

dsregcmd /debug /leave

- Aguardar máquina sair da lista no Azure

- Forçar sincronização com Azure:

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

- Em seguida aguardar máquina voltar para a lista no Azure

- Acessar cmd como adm novamente e executar:
dsregcmd /debug /join

**<u>Últimas atualizações</u>**  

| Editor       | Data       | Motivo                  | Alteração |
|--------------|------------|-------------------------|-----------|
| Thiago Leite | 15/01/2024 | Criação da documentação |          |
|              |            |                         |           |
|              |            |                         |           |
|              |            |                         |           |
|              |            |                         |           |

