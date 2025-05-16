AM

**<u>Arquitetura</u>**

n/a

**<u>Contas de Serviço</u>**

n/a

**<u>Configurações do Ambiente</u>**

Executar como administrador

**<u>Configurações Gerais</u>**

Para verificar se não há mais de um registro com o mesmo nome de máquina e pode estar ocasionando conflito

**Alterar variável PC e a variável DHCPServer caso necessário:**

\$PC = 'ufm-infti-c14.frimesa.local'
\$DHCPServer = 'fouroceans01.frimesa.local'
\$scopes = Get-DhcpServerv4Scope -ComputerName \$DHCPServer
foreach (\$scope in \$scopes){
Get-DhcpServerv4Lease -ScopeId \$scope.ScopeID -ComputerName \$DHCPServer \| Where-Object Hostname -eq \$PC
}

**<u>Últimas atualizações</u>**  

| Editor       | Data       | Motivo                  | Alteração |
|--------------|------------|-------------------------|-----------|
| Thiago Leite | 11/12/2023 | Criação da documentação |          |
|              |            |                         |           |
|              |            |                         |           |
|              |            |                         |           |
|              |            |                         |           |

