AM
**<u>Arquitetura</u>**

Messinaw e microsoft 365 admin center

**<u>Contas de Serviço</u>**

n/a

**<u>Configurações do Ambiente</u>**

n/a

**<u>Configurações Gerais</u>**

Foi criado uma caixa de e-mail compartilhada no Office 365 e não no exchange interno. Em troca de mensagens na nuvem, funciona, porém quando tenta enviar um e-mail usando o SMTP interno (Oracle, Senior e afins) não funciona, pois não há um objeto no SMTP interno para referenciar esse endereço de e-mail. Para resolver este problema, basta criar uma caixa interna e criar um endereço remoto apontando para a nuvem.

New-Remotemailbox -Name "\<Shared mailbox\>" -Alias \<sharedmailbox\> -UserPrincipalName [\<sharedmailbox@contoso.com](mailto:%3csharedmailbox@contoso.com)\> -Remoteroutingaddress [\<sharedmailbox@contoso.mail.onmicrosoft.com](mailto:%3csharedmailbox@contoso.mail.onmicrosoft.com)\> -Shared
Exemplo:
New-Remotemailbox -Name "<supterceiros@frimesa.com.br>" -Alias supterceiros -UserPrincipalName <supterceiros@frimesa.com.br> -Remoteroutingaddress <supterceiros@frimesacombr.mail.onmicrosoft.com> -Shared
Link para referência:
<https://learn.microsoft.com/en-US/exchange/troubleshoot/user-and-shared-mailboxes/cannot-access-mailbox>

**<u>Últimas atualizações</u>**  

| Editor            | Data       | Motivo                  | Alteração |
|-------------------|------------|-------------------------|-----------|
| André Luiz Fronza | 24/11/2023 | Criação da documentação |          |
|                   |            |                         |           |
|                   |            |                         |           |
|                   |            |                         |           |
|                   |            |                         |           |

