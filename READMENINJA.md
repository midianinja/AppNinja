# APP Ninja

_“Lançando o maior movimento Ninja do universo!”._

**Nós somos Ninjas e acreditamos que podemos transformar o nosso país por meio da lógica de organização social coletiva.
. Junte-se a nós!**

## Conteúdo

1. [Sobre o APP Ninja]
2. [Comunicação](#comunicação)
3. [Roadmap de tecnologia](#roadmap-de-tecnologia)
4. [Como contribuir](#como-contribuir)
5. [Instalação](#instalação)
6. [FAQ](#perguntas-frequentes-(FAQ))

## Sobre o APP Ninja


## Comunicação

Acreditamos que o sucesso do projeto depende diretamente da interação clara e
objetiva entre os membros. Por isso, estamos definindo algumas
políticas para que estas interações nos ajudem a crescer juntos! Você pode
consultar algumas destas boas práticas em nosso [código de
conduta](https://github.com/portabilis/i-educar/blob/master/CODE_OF_CONDUCT.md).

Além disso, gostamos de meios de comunicação assíncrona, onde não há necessidade de
respostas em tempo real. Isso facilita a produtividade individual dos
colaboradores do projeto.

| Canal de comunicação | Objetivos |
|----------------------|-----------|
| [Issues do Github](https://github.com/midianinja/AppNinja/issues) | - Sugestão de novas funcionalidades<br> - Reportar bugs<br> - Discussões técnicas |
| [Telegram](https:// ) | - Comunicar novidades sobre o projeto<br> - Movimentar a comunidade<br>  - Falar tópicos que **não** demandem discussões profundas |

## Roadmap de tecnologia

### Passos iniciais

- Adoção do [PSR1](https://)
- Adoção do [PSR2](https://)
- Adoção do [PSR4](https://)

### Planejamento Técnico

Em nossa wiki você encontra um planejamento mais técnico de como devemos
prosseguir com as melhorias e evoluções do nosso projeto.
[Clique aqui](https://github.com/)
para ler mais a respeito.

## Como contribuir

Contribuições são **super bem vindas**! Se você tem vontade de construir o
APP Ninja junto conosco, veja o nosso [guia de contribuição](./CONTRIBUTING.md)
onde explicamos detalhadamente como trabalhamos e de que formas você pode nos
ajudar a alcançar nossos objetivos.

## Instalação

> ATENÇÃO: Essa forma de instação tem o objetivo de facilitar demonstrações e desenvolvimento. Não é recomendado para ambientes de produção!

Antes de começar você vai precisar instalar o Docker e o Docker Compose em sua
máquina. Para mais informações veja estes links:

- [Docker](https://docs.docker.com/install/) (> 18.03.1-ce)
- [Docker Compose](https://docs.docker.com/compose/install/) (> 1.21.2)

Você também vai precisar do [Git](https://git-scm.com/downloads) caso ainda não
o tenha instalado.

Depois de ter o Docker e git instalados faça o clone deste repositório e execute
o Docker Compose para criar os containers da aplicação:

```terminal
git clone https://github.com/portabilis/i-educar.git i-educar
cd i-educar
cp .env.example .env
cp ieducar/configuration/ieducar.ini.sample ieducar/configuration/ieducar.ini
cp phinx.php.sample phinx.php
docker-compose up -d
```

Depois disto faça as alterações necessárias nos arquivos de configuração:

### Inicializando o banco de dados

**Atenção:**

## Perguntas frequentes (FAQ)

Algumas perguntas aparecem recorrentemente. Olhe primeiro por aqui: [FAQ](docs/faq.md)

---

Powered by [Frente Hacker]
