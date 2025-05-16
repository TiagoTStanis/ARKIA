**<u>Arquitetura</u>**

Powershell; Agendador de Tarefas

**<u>Contas de Serviço</u>**

Usuário \*-adm

**<u>Configurações do Ambiente</u>**

N/A

**<u>Configurações Gerais</u>**

**Powershell**
==\# Obtém o nome de usuário atualmente logado na máquina==
==\$currentUserID = ((quser \| Where-Object { \$\_ -match 'Ativo' }) -split '\s+')\[2\]==

==\# Obtém todas as sessões de usuário==
==\$sessions = query session==

==\# Itera sobre as sessões==
==foreach (\$session in \$sessions) {==
==\# Divide as informações da sessão em espaços==
==\$sessionInfo = \$session -split '\s+'==

==\# Obtém o ID da sessão==
==\$sessionId = \$sessionInfo\[2\]==
==\# Verifica se o ID da sessão é igual ao ID da sessão atual==
==if (\$sessionId -ne '0' -and \$sessionId -ne \$currentUserId -and \$sessionId -ne 'USERNAME') {==
==\# Desconecta a sessão usando o ID==
==logoff \$sessionId==
==Write-Host "Sessão desconectada: \$sessionId"==
==}==
==}==

**Agendador de Tarefas**
Geral \>
Executar estando o usuário conectado ou não

Não armazenar a senha.

Executar com privilégios mais altos

Disparadores \>
Uma vez. Depois de disparado, repetir a cada 1 hora indefinidamente.

Ações \>
Program/script: C:\Windows\System32\WindowsPowerShell\v1.0\powershell.exe

Add arguments: -ExecutionPolicy Bypass -File "C:\Windows\Scripts\kill_session.ps1"

Start in: C:\Windows\Scripts\\

**<u>Últimas atualizações</u>**  

| Editor      | Data       | Motivo                  | Alteração |
|-------------|------------|-------------------------|-----------|
| Iago Vargas | 13/03/2024 | Criação da documentação |          |
|            |           |                        |           |
|             |            |                         |           |
|             |            |                         |           |
|             |            |                         |           |
