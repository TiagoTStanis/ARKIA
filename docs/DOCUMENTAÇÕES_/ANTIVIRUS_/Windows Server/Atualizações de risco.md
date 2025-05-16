Algumas versões de sistema operacional e aplicativos possuem vulnerabilidades conhecidas que podem ser exploradas, para isso são lançados patches ou novas versões com a intenção de corrigir este problema.

Foi aberto o chamado 316337 para registrar essas atualizações. 

**Passo a passo para identificar as atualizações necessárias:**

1\. Abrir a console Trend > Attack Surface Risk Management > Attack Surface Discovery  
2\. Na aba Devices é possível verificar os dispositivos com maior risco de segurança  
3\. Abrir o device e verificar o RISK INDICATORS com o parâmetro -> **Risk factor: All**  
4\. Para cada registro, deve-se validar a atualização necessária

**Atualizações de sistema operacional:**  
1\. Abrir o link que consta no parâmetro **cveId** 2\. Na nova página que se abrir, abrir o link que consta no parâmetro **Published**  
3\. Nesta página, abrir o link que esta identificado na aba **Hyperlink  
**4\. Com esta aba aberta, não é mais necessário abrir os links de cada evento como informado nos passos anteriores, pois é possível copiar a CVE e substituir na URL.  
https://msrc.microsoft.com/update-guide/vulnerability/CVE-2024-43572  
[https://msrc.microsoft.com/update-guide/vulnerability/CVE-&lt;ano-número&gt;](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2024-43572)  
5\. No evento do Trend é possível verificar o sistema operacional (Windows Server 2019 ou 2022), isso é necessário para verificar o KB necessário para corrigir a vulnerabilidade  
6\. No documento da CVE consta **Atualizações de segurança**, neste campo você deverá buscar pelo sistema operacional (Windows Server 2019 ou 2022).  
7\. O KB será o número do Artigo

**Atualizações de software:  
**1\. Identificar o software e copiar a versão  
2\. Registrar no chamado o nome do aplicativo, sua versão e as CVEs exploráveis