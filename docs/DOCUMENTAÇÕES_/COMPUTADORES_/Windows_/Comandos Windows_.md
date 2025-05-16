Comandos Windows
Friday, November 24, 2023
2:24 PM

**<u>Arquitetura</u>**

n/a

**<u>Contas de Serviço</u>**

Usuário administrador local

**<u>Configurações do Ambiente</u>**

n/a

**<u>Configurações Gerais</u>**

Chave de ativação: Wmic path SoftwareLicensingService get OA3xOriginalProductKey
cd: Acessa o diretório especificado
cd..: Volta o diretório
Cls: Limpa a tela
Copy: Copia o conteúdo especificado
xcopy: Copia o conteúdo recursivamnente
Dir: Lista o conteúdo do diretório
Md: Cria um diretório
Move: Move arquivos de um diretório
Chdir: Exibe o diretório atual
Del: Deleta um arquivo
deltree: Deleta recursivamente
rd: Deleta um diretório
Desligar PC remotamente pelo CMD
Shutdown -s -t 00 -f (desligar, 00 tempo em segundos, -f forçar finalização de aplicativos abertos)
Shutdown -r -t 00 -f (reiniciar, 00 tempo em segundos, -f forçar finalização de aplicativos abertos)
Shutdown -r ou -s -t 00 -f -m \NomedoPCouIP (desligar ou reiniciar máquina remotamente)
Mostrar servidor de logon do user: echo %logonserver%
Habilitar modo de performance máxima: powercfg -duplicatescheme e9a42b02-d5df-448d-aa00-03f14749eb61
Verificar qual dc a máquina autenticou: nltest /server:FISC-COML-C17 /sc_query:frimesa.local
Verificar informações sobre um processo: Sc queryex NOMEDOPROCESSO
Encerrar o processo: Taskkill /PID 123 /F (FORCE) /T (T FINALIZA OS PROCESSOS FILHOS TBM)

**<u>Últimas atualizações</u>**  

| Editor            | Data       | Motivo                  | Alteração |
|-------------------|------------|-------------------------|-----------|
| André Luiz Fronza | 21/07/2023 | Criação da documentação |          |
| André Luiz Fronza | 24/11/2023 | Padronização            |           |
|                   |            |                         |           |
|                   |            |                         |           |
|                   |            |                         |           |

