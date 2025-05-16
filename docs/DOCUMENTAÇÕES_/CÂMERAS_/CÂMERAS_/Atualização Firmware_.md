AM

**<u>APPLIANCE</u>**

![image1](../../../_resources/image1-39.png)
![image1](../../../_resources/image1-39.png)
Todos os modelos de câmera HikVision DS-\*.

**<u>ARQUITETURA</u>**

Recomenda-se a atualização através do Software BatchConfiguration, ferramenta disponibilizada pela HikVision para o gerenciamento das câmeras.

**<u>Contas de Serviço</u>**

Usuário: admin
Senha: Keepass da Infra

**<u>Configurações</u>**

Para realizar a atualização de uma câmera é necessário acessa-la via web, preferencialmente no Edge, com modo de compatibilidade com o IE, instalar e executar o plugin quando solicitado. Após, vá em Sistema -\> Manutenção -\> Atualizar. Clique em Navegar, selecione o firmware em sua máquina e atualize.
Em caso de erro, verifique qual é e tente outro firmware. Caso aconteça o erro dizendo “Erro em tipo de ficheiro” ou “Versão incompatível”, apesar de ambos estarem corretos, verifique a “Propriedade da Versão do Firmware”, em que esse está localizado em Sistema -\> Definições do sistema. Dependendo do valor da propriedade, apesar de ser o mesmo modelo de câmera, o firmware é diferente. Algumas câmeras são mais recentes e possuem uma propriedade com valor diferente, exigindo outro firmware. Na pasta “Firmwares” possuem diversos firmwares para diversos modelos de câmeras diferentes. Nota-se que a maioria é de 2021. Isso acontece, pois, as câmeras são de modelos mais antigos e não possuem atualizações mais recentes da Hikvision (última verificação 29/12/2022).
Caso queira realizar atualização em lote ou alteração de configuração em lotes, recomendo a utilização do software “Batch Configuration”, disponibilizado pela Hikvision (<https://www.hikvision.com/en/support/tools/hitools/cl25143e034aab161b/><u>).</u>
No software, adicione as câmeras através de um segmento de IP, por exemplo, 172.19.123.0/24, e coloque a senha padrão de acesso as câmeras. Após a conexão de todas as câmeras, o software oferece algumas ferramentas, como a atualização e configuração de câmeras em conjunto. Para atualização, sempre, antes de iniciar pelo software, procure o firmware correto e teste atualizando manualmente na câmera. Após os testes, para atualizar, selecione as câmeras desejadas, clique em “Upgrade” -\> Selecione o arquivo de firmware -\> Finalize. Agora é só esperar que em cerca de 10-15 minutos terminará e reinicializará a câmera automaticamente.
Nota-se que durante todo o processo de atualização a câmera ficará indisponível para acesso e visualização.
Os firmwares estão disponíveis no SharePoint da Infra.

**ÚLTIMAS ATUALIZAÇÕES**
| Editor | Data | Motivo | Alteração |
|----|----|----|----|
| André Luiz Fronza | 21/11/2023 | Novo modelo de documentação | Padronização do texto |
|  |  |  |  |
|  |  |  |  |
|  |  |  |  |
|  |  |  |  |

