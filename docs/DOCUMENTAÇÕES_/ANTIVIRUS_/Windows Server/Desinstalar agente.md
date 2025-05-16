1\. Desativar auto proteção:  
cd C:\\Program Files\\Trend Micro\\Deep Security Agent  
dsa_control --selfprotect=0 -p &lt;senha&gt; -> desabilita auto proteção  
dsa_control --selfprotect=1 -p &lt;senha&gt; -> habilita auto proteção

2\. Desinstalar utilizando ferramenta ou pelo painel de controle (pode ser necessário reboot)  
2.1 Utilizando ferramenta:  
Copiar DSA_CUT e executar pelo CMD  
https://success.trendmicro.com/en-US/solution/ka-0013399  
2.2 Utilizando painel de controle:  
Necessário que não tenha nenhuma sessão ativa em outro usuário para que seja possível remoção completa

3\. Rodar V1ESUninstall para remover serviços que ficaram