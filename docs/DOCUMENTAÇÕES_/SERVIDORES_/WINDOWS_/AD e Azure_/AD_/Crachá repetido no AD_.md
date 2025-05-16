Crachá repetido no AD
Friday, November 24, 2023
2:33 PM

**<u>Arquitetura</u>**

n/a

**<u>Contas de Serviço</u>**

n/a

**<u>Configurações do Ambiente</u>**

n/a

**<u>Configurações Gerais</u>**

Get-ADUser -Filter {(employeeID -like "\*")} -property employeeID \|Group employeeid \| ? {\$\_.Count -ge 2} \| select -ExpandProperty group \| Select-Object Enabled, ObjectClass, Name, distinguishedName, SamAccountName, employeeID \| Export-Csv C:\Users\afronza-adm\Desktop\employee-id.csv

**<u>Últimas atualizações</u>**  

| Editor            | Data       | Motivo                  | Alteração |
|-------------------|------------|-------------------------|-----------|
| André Luiz Fronza | 24/11/2023 | Criação da documentação |          |
|                   |            |                         |           |
|                   |            |                         |           |
|                   |            |                         |           |
|                   |            |                         |           |

