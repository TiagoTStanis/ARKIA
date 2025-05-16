Softwares DEV
Friday, March 1, 2024
9:24 AM

**<u>Arquitetura</u>**

n/a

**<u>Contas de Serviço</u>**

Usuário administrador local

**<u>Configurações do Ambiente</u>**

n/a

**<u>Configurações Gerais</u>**

**JAVA 8 UPDATE 144**
1.  Instalar ambos os java’s JDK e JRE. Começar pelo JDK;
2.  Durante a instalação do JDK, solicitará para instalar o JRE, pode confirmar e prosseguir com a instalação.
3.  Após instalar ambos os JDK, desinstalar a versão JRE que foi instala junto, pois está é instalada na versão mais atual e é necessário a versão 144.
4.  Após desinstalar, prosseguir e instalar ambas as versões do Java JRE.
**BI PUBLISHER (XML PUBLISHER)**

Requisitos: Word 2010, .NET Framework 2.0 (para este, refere-se ao documento de instalação do .NET Framework, qual se encontra no SharePoint), JRE 8u144 x32 e administrador local.

Observação: A instalação do BI Publisher deve ser realizada no usuário que for utilizar a aplicação, para isto, é necessário colocar o usuário da pessoa em questão como administrador local para realizar a instalação.
1.  Com os requisitos preenchidos, basta apenas executar o instalador;
2.  Após, ir até a pasta do Java no Program Files (x86) e atribuir permissão de modificação total aos usuários (ação deve ser realizada como usuário administrador);
3.  Após, entrar no Word, ativar edição, ir na aba suplementos, ir em opções e verificar se o caminho do executável do Java está preenchido, e caso não estiver, selecionar o caminho do Java no Program Files (x86);
4.  Caso não apareça a aba suplementos, reinstalar o software;
5.  Caso seja necessário configurar para dois usuários usarem a mesma máquina (e.g. estagiários), seguir o passo a passo abaixo:
    1.  Atribuir permissão total para usuário das pastas Oracle e Java no Program Files (x86);
    2.  Atribuir administrador local para os dois usuários;
    3.  Considerarei os dois usuários como usuário 1 e usuário 2;
    4.  Instalar o BIPublisherDesktop_10g no usuário 1;
    5.  Testar no usuário 1, deverá funcionar corretamente;
    6.  Testar no usuário 2, é necessário configurar o Java Home nesse usuário 2;
    7.  Possivelmente Não irá funcionar a propriedade do campo no BI Publisher após carregar os dados (apenas usuário 2);
    8.  Voltar para o usuário administrador;
    9.  Remover administrador local dos dois usuários;
    10. Testar nos dois usuários;
    11. Caso antes tenha funcionado, agora irá parar definitivamente a propriedade do campo no BI Publisher após carregar os dados (apenas usuário 2);
    12. Executar o instalador 2 SEM PERMISSÃO DE ADMINISTRADOR, COMO USUÁRIO LOCAL MESMO.
    13. Irá apresentar o erro: Template Builder Installer did not complete! Return code is: -1. Apenas ignorar, não tem problema.
    14. Após terminar o instalador, testar novamente e todas as funções devem estar funcionando de acordo.
1.  Depois de instalado, valide se está funcional, vefique as opções na aba "Ferramentas", lá deve conter o caminho do java x86 144 conforme na imagem a seguir:
2.  ![image1](../../../_resources/image1-8.png)

8.  O caminho do Home Java só estará populado caso o instalador tenha sido executado no usuário do colaborador em questão (se pedir adm, irá instalar como se fosse usuário adm, portanto nesse caso, o colaborador teria que ter adm local no ad dele). Se o Home Java não estiver populado, não será possível pois não há permissões para a pasta x86 do Java. Nesse caso, é necessário ir até a pasta Java no Program Files (x86) e dar permissão de controle total a todos os usuários da máquina, a partir dai será possível popular o Home Java.

9.  **TROUBLESHOOTING ERRORS**
10. Antes de começar nos erros, realize alguns troubleshootings básicos, como:
11. Verificação da variável JAVA_HOME, apontando para o JRE da máquina do colaborador;
12. No word, na guia suplementos, abra as opções do Bi Publisher e verifique, se no 2º campo, está configurado corretamente o caminho do java JRE;
    1.  Para esse passo II, é necessário que o usuário tenha permissão a pasta do Java;
1.  Verifique se os suplementos estão ativos:
    1.  Este pode ser verificado nas configurações do Word -\> Suplementos -\> Gerenciar (inferior da tela) -\> Suplementos de COM -\> IR -\> Selecionar o Template Word Builder -\> ok.
**ERRO 1:** A macro não pode ser localizada ou foi desativada pelas configurações de segurança de macro.
14. Primeiramente, verifique nas configurações de Word se está habilitado a utilização de macros. Caso esteja tudo certo, siga os seguintes passos:
15. Abra o CMD como administrador:
    1.  No CMD, vá para a pasta Users do usuário e execute o seguinte comando:
        1.  cd C:\Users\\usuário”
        2.  DEL /S /A:H /A:-H \*.EXD
    1.  Esse comando tem por objetivo apagar todos os arquivos .EXD.
    2.  Caso ainda não resolve, execute esses comandos também no CMD:
        1.  32 bits: Regsvr32 "C:\Windows\System32\MSCOMCTL.OCX"
        2.  64 bits: Regsvr32 "C:\Windows\SysWOW64\MSCOMCTL.OCX"
    1.  Reiniciar o PC e testar.

**ERRO 2:** O componente ActiveX não pode criar objeto
16. Esse é um erro um pouco complicado, pois envolve o VBA. Foi testado algumas soluções, porém a única que apresentou sucesso foi a reinstalação completa do Bi Publisher, sendo para esta necessário:
    1.  Desinstalação local do PC;
    2.  Remoção de registros no Regedit;
    3.  Remoção das pastas existentes do BI Publisher;
    4.  Reiniciar o PC;
    5.  Instalar novamente o Bi Publisher;
**ERRO 3:** Nr. do erro: 53. Descrição: O arquivo não foi localizado. Confirme se: “...”
17. A solução deste erro se encontra nos passos básicos de troubleshooting, especificadamente passos I, II e II.a.

**JDeveloper Suíte**
1.  Necessário extrair os arquivos do arquivo zipado jdev_suite_122140_win64-2;
2.  Após a extração, basta apenas executar o instalador.
**ODAC12**
1.  Para este, tem um tutorial PDF separado, qual deixarei junto ao instalador;
2.  O arquivo tnsnames.ora está em posse do André ou com o pessoal do Desenvolvimento, conversar com algum destes para obtê-lo.
**Forms and Reports (Forms Builder)**
1.  Alterar as propriedades de swap do Windows:
    1.  Ir em configurações Avançadas do Sistema;
    2.  Desempenho (Configurações);
    3.  Avançado;
    4.  Memória Virtual (Alterar);
    5.  Configurar o tamanho personalizado para inicial 2048 e final 10000, clicar em Definir;
    6.  Reiniciar o sistema.
1.  Descompactar Disco 1 e Disco 2 em diretórios diferentes;
2.  Alterar o modo de compatibilidade do executável setup.exe do disco 1 para compatibilidade com Windows XP SP3;
3.  Quando solicitado sobre o servidor SMTP, pode pular;
4.  Quando solicitado, selecionar o caminho do disco 2;
5.  Esperar terminar, se solicitar algo do Oracle Net, pode cancelar;
6.  Caso falhe, abra o Instalador do Oracle, desinstale os produtos, pastas apagadas inclusas, limpar as pastas temporárias, reiniciar o computador e tentar novamente.
7.  Após instalar tudo com sucesso, passar a FORMS_LIBRARIES_V10 para o disco e coloca-la como variável de ambiente, conforme mostrado na imagem abaixo:
**Oracle Workflow Builder**
1.  Executar o instalador em modo de compatibilidade Windows XP SP3. Nome da pasta p6970344_R12_WINNT.
2.  Cuidado, o instalador do Oracle não suporta espaços, ou seja, o caminho do arquivo não pode contem espaços e nem ser um caminho muito grande.
3.  Caso de o erro de registro de um arquivo .OCX, é o caminho de instalação inválido, coloque outro, como por exemplo C:\Workflow.
**Spoon (PDI-CE)**
1.  Não possui executável, apenas um .bat que abre a aplicação.
2.  Criar uma variavel com o nome JDK_HOME onde foi instalado o jdk, sem o \bin;
3.  Na variável path crie uma nova variável local do arquivo instalado do Java mas com o \bin no final, ex %JDK_HOME%\bin.
4.  Criar mais uma variável de sistema com o nome PENTAHO_JAVA_HOME com o caminho do JRE sem o \bin.
5.  Caso de erro crie uma variável com o nome PENTAHO_DI_JAVA_OPTIONS e valor -Xmx1g.
**SQL Developer 21-2.0**
1.  Apenas extrair e pronto
**Apache ANT**
1.  Extrair em uma pasta, preferencialmente no disco C:\\
2.  Criar uma variável com o nome ANT_HOME e colocar o caminho de onde foi extraído o apache;
3.  Após vá na variavel Path, em system variables e adicione uma nova linha com o conteúdo %ANT_HOME%\bin.
**Apache Mavem**
1.  Extrair em uma pasta, preferencialmente no disco C:\\
2.  Criar uma variável com o nome M2_HOME e colocar o caminho de onde foi extraído o apache;
3.  Após vá na variavel Path, em system variables e adicione uma nova linha com o conteúdo %M2_HOME%\bin.
**Eclipse**
1.  Extrair o arquivo zip .m2 para dentro da pasta do usuário atual, C:\Users\username\\
2.  Extrair o arquivo zip apache-maven-3.2.2 para o disco C:\\
3.  Extrair o arquivo zip eclipse-java-neon-3-win32-x86_64 para o disco C:\\
4.  Configuração das variáveis de ambiente:
    1.  Necessário ter todas as variáveis de ambiente apontando para C:\Dev_SuiteHome1;
    2.  Necessário ter uma variável de ambiente para o JDK 8u144 x64;
Exceções:
1.  Caso apareça o erro: “Failed to load the JNI shared library "C:/JDK/bin/client/jvm.dll"
    1.  Verifique se tudo é x64 bits;
        1.  64-bit OS;
        2.  64-bit Java;
        3.  64-bit Eclipse.
    1.  Após, caso o problema persista, edite o arquivo eclipse.ini, e adicione as seguintes linhas após “org.eclipse.platform”
-vm

C:\SEU CAMINHO DO JAVA(JDK) X64 AQUI\bin\javaw.exe

**Oracle Forms Builder**

1.  Fazer download o Oracle Forms and Reports do site da Oracle;
    1.  Ao fazer o download, irá baixar o gerenciador de downloads do Oracle, que irá baixar o Oracle Fusion Middleware (OFM);
    1.  Executar o gerenciador de downloads e baixar o arquivo zipado do OFM;
    1.  Descompactar o arquivo e instalar o OFM;
    1.  Na tela para escolher o caminho do JDK instalado, selecione o caminho no qual foi instalado o JDK, geralmente “C:\Program Files\Java\versãodoJDK\bin”;
    1.  Prosseguir com a instalação até finalizar.
1.  Procurar no menu do Windows por “Editar as variáveis de ambiente do sistema” -\> “Variáveis de Ambiente”, em variáveis do sistema clique em novo e preencha conforme imagens a seguir. Obs: O caminho não existe, este será criado e populado pelo pessoal do desenvolvimento depois.
2.  ![image2](../../../_resources/image2-3.png)

4.  Caso apareça o erro que faltou a dll MSVCR100.DLL, basta instalar o Microsoft Visual C++ 2010 SP1 Redistributable Package.

**Diversos**
1.  Para o restante, basta apenas executar o instalador

**<u>Últimas atualizações</u>**  

| Editor            | Data       | Motivo                  | Alteração |
|-------------------|------------|-------------------------|-----------|
| André Luiz Fronza | 01/03/2024 | Criação da documentação |          |
|                  |           |                        |           |
|                   |            |                         |           |
|                   |            |                         |           |
|                   |            |                         |           |

