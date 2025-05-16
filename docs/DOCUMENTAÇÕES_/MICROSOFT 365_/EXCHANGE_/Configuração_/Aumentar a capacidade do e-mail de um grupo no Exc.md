Aumentar a capacidade do e-mail de um grupo no Exchange
Thursday, February 29, 2024
5:14 PM

Isso vale também para e-mails de sites de Sharepoint:

**<u>Arquitetura</u>**

M365 Online via PowerShell

**<u>Contas de Serviço</u>**

n/a

**<u>Configurações do Ambiente</u>**

n/a

**<u>Configurações Gerais</u>**

Get-Mailbox -GroupMailbox <cq@frimesacombr.onmicrosoft.com>

Set-Mailbox -GroupMailbox cq@frimesacombr.onmicrosoft.com -ProhibitSendQuota 98GB -ProhibitSendReceiveQuota 99GB -IssueWarningQuota 98GB

Start-sleep -Seconds 60

Get-Mailbox -GroupMailbox cq@frimesacombr.onmicrosoft.com

**<u>Últimas atualizações</u>**  

| Editor            | Data       | Motivo                  | Alteração |
|-------------------|------------|-------------------------|-----------|
| André Luiz Fronza | 24/11/2023 | Criação da documentação |          |
|                   |            |                         |           |
|                   |            |                         |           |
|                   |            |                         |           |
|                   |            |                         |           |

