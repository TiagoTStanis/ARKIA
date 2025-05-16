Instalação .NET 3.5  
Friday, March 1, 2024  
9:05 AM

**<u>Arquitetura</u>**

n/a

**<u>Contas de Serviço</u>**

Usuário administrador local

**<u>Configurações do Ambiente</u>**

n/a

**<u>Configurações Gerais</u>**

Existem dois métodos para fazer o download do .NET Framework, sendo um online e outro Offline via Pen Drive;  
1\. Online:

Abra o regedit e vá em:

- HKEY_LOCAL_MACHINE\\SOFTWARE\\Policies\\Microsoft\\Windows\\WindowsUpdate\\AU  
    Altere o valor da chave 'UseWUServer' de 1 para 0;  
    Após, abra o CMD como administrador e execute o seguinte:
- net stop bits
- net stop wuauserv
- net stop cryptsvc
- ren C:\\Windows\\SoftwareDistribution SoftwareDistribution.old
- net start bits
- net start wuauserv
- net start cryptsvc  
    Abra o snap-in "Ativar ou desativar recursos do Windows", selecione o .NET Framework 3.5, espere carregar e selecione baixar do Windows Update.  
    Após terminar a ativação do recurso, volte o valor da chave no regedit para 1.

2\. Offline:  
Vá para a seguinte pasta na dublinl:  
[\\dublinl\\informatica\\Instaladores_nao_padrao\\DotNET 3.5](file://dublinl/informatica/Instaladores_nao_padrao/DotNET%203.5)  
Nesta pasta, terá mais duas pastas, uma para cada versão sistema operacional Windows utilizado na Frimesa, 10 ou 11. Selecione a desejada e envie para uma pasta no computador.  
Neste computador, abra o CMD como administrador e execute o seguinte comando:  
DISM /Online /Enable-Feature /FeatureName:NetFx3 /All /LimitAccess /Source:C:\\sxs  
Claro, mude o caminho de Source para onde foi movido a pasta contendo os arquivos do .NET

**<u>Últimas atualizações</u>**

| Editor | Data | Motivo | Alteração |
| --- | --- | --- | --- |
| André Luiz Fronza | 01/03/2024 | Criação da documentação |     |
|     |     |     |     |
|     |     |     |     |
|     |     |     |     |
|     |     |     |     |