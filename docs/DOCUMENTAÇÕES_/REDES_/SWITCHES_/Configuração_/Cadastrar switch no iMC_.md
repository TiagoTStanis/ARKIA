Cadastrar switch no iMC
Thursday, August 15, 2024
2:25 PM

Vá em Resource -\> Add Device:

![image1](../../../../_resources/image1.png)

Essa será a tela para adição de novos switches no iMC:
- Host/IP: IP do dispositivo
- Device Label: Nome do Switch
- Mask: Máscara de rede
- Device Group: Pode deixar em branco, tem uma regra que os move automaticamente para o device group correto
- Login Type: SSH
- Selecione:
  - Automatically register...
  - Support Ping Operation
- Expanda as configurações SNMP, clique em configure, selecione usar um template existente, selecione o template de nome SNMPv3 e clique em OK.
- Expanda as configurações Telnet, clique em configure, selecione usar um template existente, selecione o template de nome IMC e clique em OK.
- Expanda as configurações SSH, clique em configure, selecione usar um template existente, selecione o template de nome IMC e clique em OK.
![image2](../../../../_resources/image2.png)

