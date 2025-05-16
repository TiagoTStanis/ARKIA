Bandallon
Tuesday, March 12, 2024
4:42 PM

**<u>Arquitetura</u>**
- IP: 172.31.107.20;
- RAM: 8GB;
- Adaptador de rede: PUBLICA, vlan 107;
- SCSI: Um disco de 100GB.

**<u>Contas de Serviço</u>**

Usuário SGCReset

**<u>Configurações do Ambiente</u>**

n/a

**<u>Configurações Gerais</u>**

IIS e .NET Framework 4.x

Na época, em 2017, um antigo colaborador do desenvolvimento instalou o IIS, o WebDeploy e alguma versão mais antiga do VS. Nisto, o colaborador criou um projeto para uma WEB API em .NET Framework com linguagem em C#. Isto foi feito na versão .NET Framework 4.6.1 usando o runtime 4.0.30319.

O mesmo desenvolveu a WebAPI usando funções nativas do .NET Framework para o reset de senhas e afins. Devido ao mesmo ter o IIS instalado em sua máquina e usar uma versão mais antiga do VS (qual suportava a versão do .NET utilizada), o mesmo conseguia compilar o projeto, resultando em um arquivo .DLL contendo o código compilado do projeto. Essa DLL é referenciada pelo servidor web para executar a lógica da API quando solicitada.

Com isso feito, o colaborador pegou o arquivo .DLL e o migrou para a pasta do IIS em sua máquina. Após, usou o WebDeploy para migrar todo o projeto do IIS que estava em sua máquina e usando o mesmo aplicativo, importou no servidor Bandallon. Assim, atualmente, o servidor possui um webservice que contem API usadas para gerenciamento de usuários no SGC, tudo em um único arquivo .DLL.

Se usarmos uma ferramenta para descompilar a .DLL e verificar seus conteúdos (usei a DotPeek), é possível verificar como estão definidas as funções e as rotas da API:

![image1](../../../../_resources/image1-24.png)

A classe principal tem a rota api/ActiveDirectory e as demais funções tem as rotas finais para a sua finalidade, como por exemplo /reset ou /change. Esse código-fonte usa da classe UserPrincipal do .NET Framework para a alteração de senhas de usuário. Para conexão, usa o usuário SGCReset.

**<u>Últimas atualizações</u>**  

| Editor            | Data       | Motivo                  | Alteração |
|-------------------|------------|-------------------------|-----------|
| André Luiz Fronza | 12/03/2024 | Criação da documentação |          |
|                  |           |                        |           |
|                   |            |                         |           |
|                   |            |                         |           |
|                   |            |                         |           |

