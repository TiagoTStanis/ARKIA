Apagar porta de impressoras no printmanagement
Wednesday, January 24, 2024
2:34 PM

**<u>Arquitetura</u>**

Computador local

**<u>Contas de Serviço</u>**

Administrador local

**<u>Configurações do Ambiente</u>**

n/a

**<u>Configurações Gerais</u>**

Ao tentar apagar uma porta de impressora pode ser que não seja possível pois o recurso está em uso ou algum outro problema. Para resolver isso, primeiramente, pare o spooler de impressão. Este pode ser feito no cmd com o comando "net stop spooler".
Após, abra o regedit como admin e vá até HKEY_LOCAL_MACHINE \\ SYSTEM \\ CurrentControlSet \\ Control \\ Print \\ Monitors \\ Standard TCP/IP Port \\ Ports. Uma vez aqui, procure o tipo de porta, caso por impressora IP ficará em Standard TCP/IP Port e USb em USB Monitor. Faça um backup das chaves por precaução e apague a desejada. Após inicie o spooler de impressão, atualize a página e a porta terá sumido.

**<u>Últimas atualizações</u>**  

| Editor            | Data       | Motivo                  | Alteração |
|-------------------|------------|-------------------------|-----------|
| André Luiz Fronza | 24/01/2024 | Criação da documentação |          |
|                  |           |                        |           |
|                   |            |                         |           |
|                   |            |                         |           |
|                   |            |                         |           |

