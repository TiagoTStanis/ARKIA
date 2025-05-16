AM

1.  Para realizar a instalação do programa de apontamento do DIF será necessário baixar da URL <http://172.31.106.43:8080/automacao/apontamento-dif-seg/ListagemSegregadoDIF.jar>.
2.  Utilize o comando:
**wget** <http://172.31.106.43:8080/automacao/apontamento-dif-seg/ListagemSegregadoDIF.jar>

O arquivo será instalado na pasta /root
3.  Mova o arquivo para /home/frimesa/Downloads utilizando o seguintes comando:
**mv ListagemSegregadoDIF.jar /home/frimesa/Downloads**
4.  Ao mover o arquivo será necessário mudar o executável que está localizado na área de trabalho para que execute o programa que foi instalado, este programa é um executado em .JAR então o comando para ser executado será diferente.
5.  Ao acessa a área de trabalho com o comando **cd /home/frimesa/Desktop** será observado 2 executáveis:
6.  ![image1](../../../_resources/image1-16.png)
7.  Será necessário verificar qual o conteúdo de cada executável para trocar o executável da automação para o apontamento
8.  Execute o comando **vim jws_app_shortcut_1703246570958.desktop** e verifique qual o conteúdo do mesmo
9.  Neste caso, este é o executável da automação vamos mudar só a linha **Exec=** que executa os comandos quando clicado
![image2](../../../_resources/image2-8.png)

10. A linha ficará da seguinte forma:
**Exec= java -jar /home/frimesa/Downloads/ListagemSegregadoDIF.jar**

![image3](../../../_resources/image3-5.png)

OBS: Deve mudar o nome e comentário do aplicativo.
11. Desta forma o aplicativo será aberto automaticamente.
![image4](../../../_resources/image4-4.png)


