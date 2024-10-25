# Primeira Etapa:

## Questão 1:

> Diferenciar as camadas 2 e 3 do modelo OSI, e indicar os protocolos utilizados para endereçamento nestas camadas.
> 

A camada 2 (Enlace de Dados) é responsável pela transferência de dados entre dois dispositivos conectados em uma mesma rede local (LAN). Ela utiliza os endereços físicos (MAC) dos dispositivos para fazer essa comunicação, garantindo que a entrega dos frames seja feita corretamente. Os protocolos mais comuns para essa comunicação são o ethernet e o wi-fi, que utilizam esse endereço MAC.

Enquanto isso, a camada 3 (Rede) é responsável pela transferência de dados entre dispositivos em redes diferentes, utilizando os endereçamentos lógicos (IP) das redes para realizar a comunicação. O roteamento dos pacotes é feito pelos roteadores, que utilizam os endereços IP para garantir que eles cheguem à rede correta. Os principais protocolos são o IPv4 e o IPv6. O IPv6 consegue armazenar mais endereços pois suporta 128 bits ao invés de 32.

---

## Questão 2:

> Qual a diferença entre adotar uma solução proprietária como o sistema operacional Windows quando comparado a adoção de uma solução Open source como o sistema operacional Ubuntu? Quais seriam os pontos negativos e positivos de cada abordagem?
> 

### Solução Proprietária: Pontos positivos

Uma solução proprietária (como o windows) é caracterizada por ter seu código-fonte fechado e controlado exclusivamente pela empresa que o desenvolve. Isso torna o sistema mais "amigável" e intuitivo para seu usuário, já que vem pré-configurado e pronto para uso. Resolver problemas técnicos também é mais fácil, pois possui atualizações automáticas, correções de bugs e suporte técnico formal disponível. Esse tipo de solução também têm a vantagem de ser compatível com a grande maioria dos softwares, por ser a alternativa mais popular.

### Solução proprietária: Pontos negativos

Porém, o fato de ser um software fechado também acarreta em alguns pontos negativos, como por exemplo a menor flexibilidade de personalização, já que o código-fonte não pode ser modificado para adaptar o sistema. Além disso, o controle e a privacidade do usuário podem ser uma preocupação, já que a empresa proprietária controla atualizações/funcionalidades que necessitam de coleta de dados. O fator de popularidade também pode ser um ponto negativo, já que existem mais malwares criados para esse tipo de sistema. Também é válido considerar o fator de custo, já que esses sistemas geralmente requerem pagamento de licenças para sua utilização.

### Solução Open source: Pontos positivos

Já os pontos positivos e negativos de soluções Open source são basicamente opostos em relação ás soluções proprietárias. Soluções Open source são gratuitas, oferecem uma maior flexibilidade para personalização e adaptação a tarefas específicas por meio de alterações no código-fonte, e são mais seguras (já que é possivel enxergar e corrigir vulnerabilidades mais facilmente). Outro ponto positivo a se destacar é a interação com a comunidade, que ativamente compartilha maneiras de utilizar/personalizar esses sistemas.

### Solução Open source: Pontos negativos

Por outro lado, são mais difíceis de se utilizar para usuários menos experientes. São menos intuitivas, não têm compatibilidade com certos softwares (e até alguns hardwares como periféricos) e possuem um suporte técnico formal bem mais limitado, muitas vezes dependendo de auxílios da comunidade, o que pode tornar o processo de solucionar um problema mais lento e dependente de conhecimentos próprios do usuário.

---

## Questão 3:

> O que seria um projeto Open source? Como empresas podem adotar tais tecnologias e o que isso acarreta?
> 

Um projeto Open source é um projeto cujo código-fonte está disponível publicamente, permitindo que membros da comunidade possam visualizar, utilizar, e até mesmo altera-lo. Alterações no código podem ser distribuídas, e para que sejam implementadas no código original, devem passar por algum tipo de validação. A ideia por trás do código Open source é promover a colaboração da comunidade para desenvolver a melhor versão possível do software.

Empresas podem adotar tecnologias de Open source de diversas maneiras. Elas podem utilizar um software Open source diretamente como parte de suas operações diárias, aproveitando ferramentas amplamente adotadas, como: linux, mysql, react, django, etc.

Elas também podem personalizar o código-fonte de um software Open source para atender suas necessidades específicas, criando novos recursos ou integrando com soluções internas.

Inclusive, empresas também podem desenvolver algum software próprio e disponibilizar seu código como Open source, tendo em mente as vantagens e desvantagens que essa decisão possui.

Adotar soluções Open source acarreta em:

redução de custos, independência de proprietários para a utilização e personalização do software e segurança/transparência, além de uma cultura de colaboração e inovação. 

---

# Segunda etapa:

Os códigos resolvendo os exercícios da segunda etapa estão nos arquivos deste repositíro. Os nomes dos arquivos são:

- Fibonacci (recursivo): [fib_rec.py](https://github.com/leogttrrs/Desafio-SC-Cloud/blob/main/fib_rec.py)
- Fibonacci (linear): [fib.py](https://github.com/leogttrrs/Desafio-SC-Cloud/blob/main/fib.py)
- Primos (recursivo): primos_ate_rec.py
- Primos (linear): [primos_ate.py](https://github.com/leogttrrs/Desafio-SC-Cloud/blob/main/primos_ate.py)
