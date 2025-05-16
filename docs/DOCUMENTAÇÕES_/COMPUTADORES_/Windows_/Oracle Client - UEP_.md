Oracle Client - UEP
Friday, March 1, 2024
9:29 AM

**<u>Arquitetura</u>**

n/a

**<u>Contas de Serviço</u>**

Usuário administrador local

**<u>Configurações do Ambiente</u>**

n/a

**<u>Configurações Gerais</u>**

**Instalação Oracle Client**
- Copiar o instalador do Oracle Client que esta na pasta: "[\\felwood\informatica\Instaladores\Instaladores_nao_padrao\Tecnosul](file://felwood/informatica/Instaladores/Instaladores_nao_padrao/Tecnosul)" para a máquina do colaborador;
- Abrir o instalador o Oracle Client: "setup.exe";
- Na primeira tela marcar a opção: "Runtime" e clicar em "Próximo";
- Nas próximas telas, manter as configurações padrão e clicar em "Próximo";
- Clicar em "Instalar";
- Após a instalação terminar, clicar em "Fechar";
**Configurações Painel de Controle**
- Abrir o "Painel de controle" e ir nas opções "Ferramentas administrativas";
- Executar como Administrador a opção "Política de Segurança Local";
- Abrir a opção "Políticas Locais"; Abrir a opção "Atribuição de direitos de usuários" e abrir a opção "Criar objetos globais";
- Ir na opção "Adicionar um usuário ou grupo";
- Na tela que abrir, terá um campo: "Digite os nomes de objeto a serem selecionados: ": Neste campo informar o nome do grupo a ser adicionado: "S-UFM-Custos--M";
- Clicar em "Ok";
- Clicar em "Aplicar" e depois em "Ok";
- Adicionar permissões de controle total para o grupo: "S-UFM-Custos--M" nas pastas: "C:\app" e "C:\app\client\administrator\product\12.1.0\client_1";
**Configurações Net Manager**
- Ir no menu Iniciar e pesquisar por "Net Manager", após abri-lo, expandir a opção "Local" e ir na opção "Nomeação de Serviço";
- Clicar no ícone "Criar" (sinal de adição na lateral esquerda da tela) e informar o "Nome do Serviço de rede": "PRDSAT";
- Na próxima tela manter as configurações padrões e clicar em "Próximo";
- Informar o nome de host "longsisterscan.frimesa.local", porta 1521 e clicar em "Próximo";
- Na próxima tela identifique o "Nome do Serviço": "PRDSAT";
- Pressione Finalizar;
- Clicar no menu "Arquivo" e clicar na opção: "Salvar Configurações de Rede";

**<u>Últimas atualizações</u>**  

| Editor            | Data       | Motivo                  | Alteração |
|-------------------|------------|-------------------------|-----------|
| André Luiz Fronza | 01/03/2024 | Criação da documentação |          |
|                  |           |                        |           |
|                   |            |                         |           |
|                   |            |                         |           |
|                   |            |                         |           |

