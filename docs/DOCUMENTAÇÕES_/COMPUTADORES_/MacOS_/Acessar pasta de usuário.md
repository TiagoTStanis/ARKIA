O administrador local não tem privilégios para acessar algumas pastas de usuários

Caso queira que o adm local (ou outro usuário) tenha acesso a uma pasta de usuário específico, seguir o procedimento:  
<br/>1 - Acessar máquina via SSH  
2 - Logar com administrador local  
3 - Rodar o seguinte comando:  
<br/>        sudo chown -R usuario_para_acesso:staff /Users/usuario_alvo  
<br/>Substituir "usuario_para_acesso" com o usuário que quer acessar a pasta (pode ser do solicitante ou só 'administrador' mesmo, o ideal é colocar o do usuário solicitante do acesso, pois ele ja vai poder transferir os arquivos direto para o usuário dele, facilitando)  
<br/>Substituir: "usuario_alvo" com o usuário que tem a pasta que quer ser acessada (provavelmente algum que saiu da empresa)

Após roda o comando já pode testar.