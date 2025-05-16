AM

**<u>APPLIANCE</u>**

![image1](../../../_resources/image1-40.png)
![image1](../../../_resources/image1-40.png)
Servidor ESSOVIUS

**<u>ARQUITETURA</u>**

Software Symphony

**<u>Contas de Serviço</u>**

n/a

**<u>Configurações</u>**

**Recuperar imagem de objeto que não existe mais no Symphony:**
Existem duas opções, uma é realizar o backup do servidor para antes de o objeto ser excluído e a outra é converter o vídeo armazenado em .dat.
O caminho do histórico de vídeos é F:\data_path_tmp\\footagearchive e é separado por pastas nomeadas pelo ID da câmera.
Ao identificar qual câmera deseja recuperar, existem alguns comandos no CMD que manipulam utilitários que fazem a conversão do vídeo .dat.
Abra o CMD como administrador, navegue até a pasta E:\Senstar\Symphony Server v7\\Tools, nessa contém os utilitários responsáveis pela conversão. Existem mais de um. Aqui, usarei o foot2aira como exemplo:
foot2aira e o nome do arquivo .dat
foot2aira F:\data_path_tmp\\footagearchive\cam6\hist_cam6.16737218131353534.dat

**Backup do Banco de dados:**
Abra o CMD como administrador, crie uma pasta no disco C:\\ navegue até ela e execute o seguinte comando para fazer o backup do banco de dados (AIRA):
Dbupdater "BACKUP DATABASE aira TO DISK = 'C:\Temp\aira.bak'"

**Coleta de logs avançadas para câmeras (executar no cmd como administrador):**
dbupdater "insert into settings (Type,ID,Section,K,V) values ('Camera',126(ID_DA_CAMERA),'Camera','LogLevel','BasicInfo\|LogError\|MoreInfo\|Verbose')"
Após, reinicie o serviço AI Tracker da câmera em questão.

**Exportar logs do servidor:**
Na barra de pesquisa do Windows, pesquise por logpackage, execute como administrador e selecione a data qual deseja exportar os logs. Selecione a opção “Exclude data paths from dir.txt”. Irá criar um .zip na área de trabalho com os logs.
![image2](../../../_resources/image2-20.png)

**ÚLTIMAS ATUALIZAÇÕES**
| Editor | Data | Motivo | Alteração |
|----|----|----|----|
| André Luiz Fronza | 21/11/2023 | Novo modelo de documentação | Padronização do texto |
|  |  |  |  |
|  |  |  |  |
|  |  |  |  |
|  |  |  |  |

