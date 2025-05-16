  
Verificar se o certificado digital que está no token é da Certisign ou da Safeweb.

- **CASO CERTISIGN**  
    <br/>Verificar como é o modelo do token físico e baixar o driver correspondente a foto da própria página de drivers da Certisign  
    <br/>Página de drivers da Certisign:  
    https://suporte.certisign.com.br/duvidas-suporte/downloads/tokens  
    <br/><br/><br/>
- **CASO SAFEWEB  
    <br/>** Acessar a página de drivers da Safeweb e ir até o final para baixar o seguinte arquivo:

&nbsp;       ![4d3c10322c7a49e094bc89527581cc76.png](../../../_resources/4d3c10322c7a49e094bc89527581cc76.png)  
        Após baixar, executar o arquivo .pfx baixado e ir avançando até chegar na seguinte tela:  
        - Senha: safeweb  
        - Marcar a opção identificada na imagem abaixo, então clicar em avançar.  
        <img src="../../../_resources/ca1fe43dd1ef88e4094bae05afd70352.png" alt="ca1fe43dd1ef88e4094bae05afd70352.png" width="355" height="345">  
         
        Na próxima tela selecionar as opções identificadas na imagem abaixo e clicar em avançar  
        **OBS.:** **Após avançar ele irá começar a pedir uma confirmação para cada certificado, ir aceitando até concluir**

&nbsp;       ![2357f4c2e5c94c3fcedfbf039eec0125.png](../../../_resources/2357f4c2e5c94c3fcedfbf039eec0125.png)             

  
        Após a importação terminar com êxito, também verificar como é o modelo do token físico e baixar o driver correspondente as seguintes fotos  
   
        **Modelo:**  
        <img src="../../../_resources/b65ace98835c8854c21ad60fa7d8bd10.png" alt="b65ace98835c8854c21ad60fa7d8bd10.png" width="164" height="136">  
        **Driver é o Safenet** - Começar pelo mais antigo, caso não funcione, desinstalar pelo painel de controle e instalar uma versão mais recente:  
        <img src="../../../_resources/3eacde1f4b6a13d871777ce05632f8df.png" alt="3eacde1f4b6a13d871777ce05632f8df.png" width="625" height="136">  
<br/><br/>        **Modelo (GD):**  
        ![659811fdd423216d23ba815b99b955ad.png](../../../_resources/659811fdd423216d23ba815b99b955ad.png)  
        **Driver é o Safesign** - Começar pelo mais antigo, caso não funcione, desinstalar pelo painel de controle e instalar uma versão mais recente:  
        <img src="../../../_resources/a138b046a62b3c55cc1610036028bece.png" alt="a138b046a62b3c55cc1610036028bece.png" width="645" height="178">

&nbsp;       Página de drivers da Safeweb:  
        https://safeweb.com.br/suporte/centraldedownloads/token  
<br/><br/>        **PARA CERTISIGN E SAFEWEB:**  
<br/>        Após instalar o driver, **reiniciar** dois serviços do windows (abrir app serviços como adm):  
<br/>        ![fce0025430c81c7ec00504987852f7b9.png](../../../_resources/fce0025430c81c7ec00504987852f7b9.png)  
          
        Antes de reiniciar o serviço 'Propagação de Certificado', dar 2 cliques nele para abrir as propriedades e em seguida selecionar 'Automático' conforme imagem abaixo, caso já não esteja automático:        
        ![ce494844f5b069f68de9da6780dd4cdd.png](../../../_resources/ce494844f5b069f68de9da6780dd4cdd.png)  
        ![7dfc49fd27501b0b8498c5bd60705062.png](../../../_resources/7dfc49fd27501b0b8498c5bd60705062.png)  
<br/>Após aplicar, pode reiniciar esse serviço, então verificar se o certificado do token aparece no 'Opções de Internet'. Caso não apareça, reiniciar a máquina uma vez. Se ainda assim não aparecer, seguir a instrução de deinstalar o driver pelo painel de controle e instalar outra versão (mais recente)  
<br/>