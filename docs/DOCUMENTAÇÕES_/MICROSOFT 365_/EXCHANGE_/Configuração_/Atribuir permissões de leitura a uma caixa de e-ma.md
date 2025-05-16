Atribuir permissões de leitura a uma caixa de e-mail
Friday, March 1, 2024
9:16 AM

**<u>Arquitetura</u>**

n/a

**<u>Contas de Serviço</u>**

Usuário administrador local

**<u>Configurações do Ambiente</u>**

n/a

**<u>Configurações Gerais</u>**

As configurações serão realizadas através do PowerShell.
1\. Acesso ao Office 365 via Powershell.
Como é utilizado MFA para acesso aos serviços do Office 365, para acessar o Exchange via PowerShell é necessário baixar uma aplicação que fornece este meio. As etapas citados abaixo devem ser, obrigatoriamente, realizados no Edge ou IE.
1.1 Vá para o EAC (Exchange Admin Center);
1.2 Clique em Other Features e clique no link do Hybrid Setup.
1.3 Clique no segundo botão configurar, este realizará o download do executável do módulo do PowerShell do Exchange Online que dá suporte a MFA.
1.4 Instale a aplicação.
1.5 Abra o PowerShell e digite o seguinte comando:

Import-Module ExchangeOnlineManagement
Connect-ExchangeOnline -UserPrincipalName [\<UPN\>@frimesa.com.br](mailto:%3cUPN%3e@frimesa.com.br)
Connect-ExchangeOnline -UserPrincipalName ivargas@frimesa.com.br -ShowBanner:\$false -ShowProgress:\$false

2\. Atribuir permissão de leitura a uma caixa de e-mail.
Nas etapas abaixo, será usado como exemplo o usuário testeinfra e a caixa shared-mailbox-test.
2.1. Atribuir permissão de leitura a caixa. É realizada pelo seguinte comando:

Add-MailboxPermission -Identity <shared-mailbox-test@frimesa.com.br> -user <testeinfra@frimesa.com.br> -AccessRights ReadPermission -InheritanceType all

2.2. Com o comando acima, a caixa permitimos que o usuário tenha acesso de leitura a caixa, mas ainda não pode ler nenhum e-mail, isso se dá pois, dessa forma, é necessário atribuir acesso a pasta por pasta, separadamente. Os comandos abaixo mostram como se faz:

\#Atribui acesso a pasta ROOT
Add-MailboxFolderPermission -Identity [shared-mailbox-test@frimesa.com.br:\\](mailto:shared-mailbox-test@frimesa.com.br:\) -User <testeinfra@frimesa.com.br> -AccessRights Reviewer
\#Atribui acesso a pasta Caixa de Entrada
Add-MailboxFolderPermission -Identity [shared-mailbox-test@frimesa.com.br:\Inbox](mailto:shared-mailbox-test@frimesa.com.br:\Inbox) -User <testeinfra@frimesa.com.br> -AccessRights FolderVisible,ReadItems
\#Atribui acesso a pasta Arquivo Morto
Add-MailboxFolderPermission -Identity [shared-mailbox-test@frimesa.com.br:\Archive](mailto:shared-mailbox-test@frimesa.com.br:\Archive) -User <testeinfra@frimesa.com.br> -AccessRights FolderVisible,ReadItems
2.3. É possível, também, atribuir acesso a pastas novas, criados por outros usuários. Caso, algum usuário com acesso full crie uma nova pasta, será necessário atribuir o acesso manualmente através dos comandos citados anteriormente. Abaixo, segue um comando de uma pasta que contenha espaço em seu nome.

Add-MailboxFolderPermission -Identity [shared-mailbox-test@frimesa.com.br:\\Pasta](mailto:shared-mailbox-test@frimesa.com.br:\) com espaco no Nome" -User <testeinfra@frimesa.com.br> -AccessRights FolderVisible,ReadItems

2.4. Por fim, desconecte-se do Exchange Online.

Disconnect-ExchangeOnline

3\. Acesso as pastas:
Ao utilizar esse método, o acesso as pastas é de forma não convencional. Se tentar acessar a caixa compartilhada diretamente pelo e-mail, ocorrerá um erro de acesso negado devido a falta de permissão. Ao invés, para acessar as pastas quais anteriormente atribuímos acesso, segue-se os passos:
3.1. Clique com o botão direito nas Pastas e vá em Adicionar pasta compartilhada;
3.2. Insira o email da caixa compartilhada e clique em adicionar.
3.3. Expanda e aparecerão as pastas quais foram atribuídas acesso na etapa 2.2.
3.4. Desta forma, o usuário consegue visualizar os e-mails, porém não pode excluir, move-los ou responder em nome da caixa.

**<u>Últimas atualizações</u>**  

<table>
<colgroup>
<col style="width: 23%" />
<col style="width: 17%" />
<col style="width: 32%" />
<col style="width: 26%" />
</colgroup>
<thead>
<tr class="header">
<th>Editor</th>
<th>Data</th>
<th>Motivo</th>
<th>Alteração</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>André Luiz Fronza</td>
<td>01/03/2024</td>
<td>Criação da documentação</td>
<td></td>
</tr>
<tr class="even">
<td>Iago Vargas</td>
<td>10/04/2024</td>
<td>Incluído parâmetro</td>
<td><p>-ShowBanner:$false</p>
<p>-ShowProgress:$false</p></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>

