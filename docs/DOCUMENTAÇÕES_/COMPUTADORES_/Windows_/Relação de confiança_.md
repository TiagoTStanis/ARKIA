**<u>Arquitetura</u>**

Computador local \<-\> AD

**<u>Contas de Serviço</u>**

Usuário local e usuário \*-adm

**<u>Configurações do Ambiente</u>**

n/a

**<u>Configurações Gerais</u>**

Se ainda houver objeto no AD, é possível restabelecer a relação de confiança. Caso não tenha objeto no AD, pode criar um genérico e realizar o seguinte:
**Testar relação de confiança**
Test-ComputerSecureChannel -verbose
- True = confiável
- False = não confiável
**Restabelecer confiança**
Test-ComputerSecureChannel -Repair -Credential(Get-Credential)

**<u>Últimas atualizações</u>**  

| Editor            | Data       | Motivo                  | Alteração |
|-------------------|------------|-------------------------|-----------|
| Iago Vargas       | 28/09/2023 | Criação da documentação |          |
| André Luiz Fronza | 24/11/2023 | Padronização            |           |
|                   |            |                         |           |
|                   |            |                         |           |
|                   |            |                         |           |

