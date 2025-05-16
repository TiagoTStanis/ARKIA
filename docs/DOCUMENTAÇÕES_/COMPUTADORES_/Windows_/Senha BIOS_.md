Senha BIOS
Friday, March 1, 2024
9:01 AM

**<u>Arquitetura</u>**

n/a

**<u>Contas de Serviço</u>**

Usuário administrador local

**<u>Configurações do Ambiente</u>**

n/a

**<u>Configurações Gerais</u>**

A DELL fornece um cmdlet que permite a alteração da senha da BIOS. O cmdlet é DellBIOSProvider:

Install-Module -Name DellBIOSProvider
Import-Module DellBIOSProvider
Se der erro
Set-ExecutionPolicy Unrestricted
Import-Module DellBIOSProvider
\#Verificar se o PC tem senha:
Get-Item -Path DellSmbios:\Security\IsAdminPasswordSet
Get-Item -Path DellSmbios:\Security\IsSystemPasswordSet

\#Configurar nova senha:
Set-Item -Path DellSmbios:\Security\AdminPassword "\$AdminPwd"
Set-Item -Path DellSmbios:\Security\SystemPassword "\$SystemPwd"

\#Nova senha:
Set-Item -Path DellSmbios:\Security\AdminPassword "\$NewAdminPwd" -Password "\$OldAdminPwd"
Set-Item -Path DellSmbios:\Security\SystemPassword "\$NewSystemPwd" -Password "\$OldSystemPwd"

\#Remover senha
\$OldAdminPwd = "kaioshin"
Set-Item -Path DellSmbios:\Security\AdminPassword "" -Password "\$OldAdminPwd"

Maiores informações: <https://www.dell.com/support/kbdoc/en-us/000146358/dell-command-powershell-provider-bios-passwords-feature>

**<u>Últimas atualizações</u>**  

| Editor            | Data       | Motivo                  | Alteração |
|-------------------|------------|-------------------------|-----------|
| André Luiz Fronza | 01/03/2024 | Criação da documentação |          |
|                  |           |                        |           |
|                   |            |                         |           |
|                   |            |                         |           |
|                   |            |                         |           |

