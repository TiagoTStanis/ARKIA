Apagar usuário - Regedit
Friday, November 24, 2023
2:23 PM

**<u>Arquitetura</u>**

n/a

**<u>Contas de Serviço</u>**

Usuário administrador local

**<u>Configurações do Ambiente</u>**

n/a

**<u>Configurações Gerais</u>**

Primeiramente, validar os usuários que serão apagados. Esteja ciente que tais dados não podem ser recuperados.
Após, apagar as pastas dos mesmos em C:\Users. (Sempre pare a sincronização do OneDrive antes).
Por fim, apague o registro do usuário no regedit, no seguinte caminho:
HKEY_LOCAL_MACHINE\Software\Microsoft\Windows NT\CurrentVersion\ProfileList

**<u>Últimas atualizações</u>**  

| Editor            | Data       | Motivo                  | Alteração |
|-------------------|------------|-------------------------|-----------|
| André Luiz Fronza | 01/11/2023 | Criação da documentação |          |
| André Luiz Fronza | 24/11/2023 | Padronização            |           |
|                   |            |                         |           |
|                   |            |                         |           |
|                   |            |                         |           |

