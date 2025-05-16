Assinatura SERPRO - ERRO
Friday, November 24, 2023
2:35 PM

**<u>Arquitetura</u>**

n/a

**<u>Contas de Serviço</u>**

n/a

**<u>Configurações do Ambiente</u>**

n/a

**<u>Configurações Gerais</u>**

**<u>Resolução do Erro:</u>**
"Esta versão do Java não possui a cadeia de confiança do certificado utilizado em nossos servidores. Para transmitir o documento assinado será necessário instalar a versão mais recente do Java."
![image1](../../../_resources/image1-12.png)

**1. Verificação dos certificados da autoridade certificadora**
1.1 Para download dos certificados:
- <https://certificados.serpro.gov.br/arserpro/>
  - Repositório \> Cadeia de certificado
![image2](../../../_resources/image2-6.png)

1.2. Baixar a cadeia de certificados mais recente (baixar os 3 CA's)
![image3](../../../_resources/image3-3.png)

1.3 Abrir as configurações do Java \> Segurança \> Gerenciar Certificados
1.4 Na aba que irá abrir, selecionar no Tipo de certificado: <u>CA de Signatário</u>
![image4](../../../_resources/image4-2.png)
1.5 Importar os 3 certificados baixados no passo 2
**2. Verificar sites confiáveis Java**
2.1 Abrir as configurações do Java \> Segurança \> Editar Lista de Sites
2.2 Validar se a URL qual o assinador será executado, referente a sua autoridade certificadora, está incluso na lista de sites confiáveis
2.3 Em caso negativo, incluir a URL na GPO **Frimesa - Java exception Sites**
**3. Verificação arquivo hosts**
**OBS.: É possível que ao tentar atualizar o software assinador serpro, apareça um aviso "Erro ao escrever no arquivo hosts".**
3.1 Para resolver este erro, verificar no diretório [\\dublinl\informatica\Instaladores_nao_padrao\Serpro](file://dublinl/informatica/Instaladores_nao_padrao/Serpro), terá um arquivo denominado "hosts" com as alterações necessárias
**<u>Importante: NÃO SUBSTITUIR O ARQUIVO HOSTS.</u>**
3.2 Navegar até a pasta C:\Windows\System32\drivers\etc e alterar o atual arquivo **hosts** para **hosts.original**
3.3 Após alteração, criar uma cópia do arquivo e colar o bloco de texto presente no diretório citado no passo 3.1
3.4 Após alteração, salvar e tentar executar novamente o instalador do assinador serpro
3.5 Após instalação, excluir o arquivo hosts criado e renomear novamente o arquivo **hosts.original** para **hosts**
**4. Verificações básicas**
- Java atualizado - [link](https://www.java.com/pt-BR/download/manual.jsp)
- Assinador serpro atualizado - [link](https://www.serpro.gov.br/links-fixos-superiores/assinador-digital/assinador-serpro)
- URL pertence aos sites confiáveis do Java
- Certificados instalados e importados na máquina - [link](https://certificados.serpro.gov.br/arserpro/)

**<u>Últimas atualizações</u>**  

| Editor            | Data       | Motivo                  | Alteração |
|-------------------|------------|-------------------------|-----------|
| Iago Vargas       | ?          | Criação da documentação |          |
| André Luiz Fronza | 24/11/2023 | Padronização            |           |
|                   |            |                         |           |
|                   |            |                         |           |
|                   |            |                         |           |

