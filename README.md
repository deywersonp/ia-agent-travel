# IA TRAVEL AGENT

## LLM

O LLM utilizado foi o da OpenAI, portanto foi necessário criar uma conta na plataforma deles para ter acesso as chaves de API que vamos utilizar;

## MOTIVAÇÃO

O objetivo de criar nosso próprio agente de IA é para que o mesmo tenha acesso a recursos extras, recursos estes que não estão disponíveis no Chat GPT por padrão.
Um bom exemplo está relacionado com o prompt que estamos utilizando para efeito de teste. O prompt `Vou viajar em Agosto de 2024 para Londres e quero um roteiro de viagens`, quando enviado no frontend do Chat GPT retorna um roteiro de eventos com informações genéricas, não levando em consideração, por exemplo, os eventos que vão ocorrer em Londres nesta data.
Com a nossa própria IA, utilizando o LLM da OpenAI, poderemos fazer a busca pelos valores de passagens atualizados além de conseguir criar um roteiro que leva em consideração os eventos que estão para ocorrer no futuro.

## OBJETIVO

Gerar Texto a partir do Input do Usuário
https://platform.openai.com/docs/guides/text-generation

## MODELO UTILIZADO

Estamos utilizando o modelo `gpt-3.5-turbo-16k` ao invés de utilizar o modelo `gpt-4o` por conta da tabela de preços. O modelo 3.5 é, em média, 10x mais barato do que o modelo mais atual disponível da OpenAI.

## SET UP VIRTUAL ENVIRONMENT

https://platform.openai.com/docs/quickstart?context=python

Once you have Python installed, it is a good practice to create a virtual python environment to install the OpenAI Python library. Virtual environments provide a clean working space for your Python packages to be installed so that you do not have conflicts with other libraries you install for other projects. You are not required to use a virtual environment, so skip to step 3 if you do not want to set one up.

To create a virtual environment, Python supplies a built in `venv module` which provides the basic functionality needed for the virtual environment. Running the command below will create a virtual environment named `"openai-env"` inside the current folder you have selected in your terminal / command line:

`python -m venv openai-env`

Once you’ve created the virtual environment, you need to activate it. On
Windows, run:

`openai-env/Scripts/activate`

On Unix or MacOS, run:

`source openai-env/bin/activate`

You should see the terminal / command line interface change slightly after you active the virtual environment, it should now show `"openai-env"` to the left of the cursor input section. For more details on working wit virtual environments, please refer to the official Python documentation.

## INSTALL OPEN AI DEPENDENCY

Once you have Python 3.7.1 or newer installed and (optionally) set up a virtual environment, the OpenAI Python library can be installed. From the terminal / command line, run:

`pip install --upgrade openai`

Once this completes, running `pip list` will show you the Python libraries you have installed in your current environment, which should confirm that the OpenAI Python library was successfully installed.

## SET UP API KEY FOR A SINGLE PROJECT

If you only want your API key to be accessible to a single project, you can create a local .env file which contains the API key and then explicitly use that API key with the Python code shown in the steps to come.

Start by going to the project folder you want to create the .env file in.

In order for your `.env` file to be ignored by version control, create a `.gitignore` file in the root of your project directory. Add a line with `.env` on it which will make sure your API key or other secrets are not accidentally shared via version control.
Once you create the `.gitignore` and `.env` files using the terminal or an integrated development environment (IDE), copy your secret API key and set it as the `OPENAI_API_KEY` in your `.env` file. If you haven't created a secret key yet, you can do so on the API key page.

The `.env` file should look like the following:

```jsx
  # Once you add your API key below, make sure to not share it with anyone! The API key should remain private.

  OPENAI_API_KEY=abc123
```

The API key can be imported by running the code below:

```jsx
  from openai import OpenAI

  client = OpenAI()
  # defaults to getting the key using os.environ.get("OPENAI_API_KEY")
  # if you saved the key under a different environment variable name, you can do something like:
  # client = OpenAI(
  #   api_key=os.environ.get("CUSTOM_ENV_NAME"),
  # )
```

## INSTALANDO DEPENDÊNCIAS

- Adicionar

`pip install {dependency-name}`

- Remover

`pip install {dependency-name}`

## EXECUTANDO ARQUIVOS

`python {filename}.py`

> # AULA 1

## AULA 01.1

Foi adicionada a configuração inicial e testamos o output para entendimento de como podemos fazer uso do LLM;

## AULA 01.2

Alteramos a mensagem enviada pelo usuário para verificar que a resposta que obtivemos da IA é similar a resposta que obtivemos utilizando o frontend do ChatGPT.

![Aula 01.2](github/images/image.png)

## AULA 01.3

### AGENTES DE IA

Para contextualizar o LLM, utilizamos os `Agentes de IA`. Os agentes de IA são estruturas mais complexas que fornecem um conjunto de ferramentas junto ao LLM, permitindo adicionar contexto e permitir uma melhor interação. Essa interação melhorada se da pelo fato de que com os agentes conseguimos passar informações novas, que complementam o contexto. Entre elas, podemos passar, por exemplo, o hotel no qual vamos nos hospedar e pedir referências de locais para um jantar que estejam localizados próxima a nossa estadia.

#### AGENTES DE IA - FERRAMENTAS

Utilizamos o `LangChain` para adicionar agentes que nos permitem fazer buscas na internet, consultar bancos de dados, etc.
https://www.langchain.com/

A inicialização do `llm` não será mais feita utilizando a lib da OpenAI, mas sim a lib do LangChain.

![Aula 01.3](github/images/image-4.png)

As ferramentas (`tools`) contém as informações que vamos passar para o nosso `llm` no formato de instruções. Na imagem abaixo podemos notar no print que é exibido o nome da ferramenta e a descrição. Essa descrição auxilia a o modelo a saber quando essa ferramenta pode ser útil.
![Aula 01.3](github/images/image-1.png)

Ao inicializar o `agent` podemos visualizar no terminal que o resultado é um prompt. Esse prompt é um conjunto de informações (instruções) que será aplicado a nossa IA para que ela entenda o passo a passo do que deve ser feito antes de responder ao input do usuário.

- Instruções passadas de forma padrão
  ![Aula 01.3](github/images/image-2.png)

- Instruções passadas através do `agent`
  ![Aula 01.3](github/images/image-3.png)

Adicionamos a propriedade `verbose` no `agent` para conseguir visualizar a cadeia de pensamentos da IA ocorrendo em tempo real:
![Aula 01.3](github/images/image-5.png)

| Fim da AULA 01

#######################################################################################################

> # AULA 02

## AULA 02.1

### ReAct - Re => Reason / Act => Act

https://react-lm.github.io/

O `prompt` que importamos pronto é no formato `ReAct`. O `Langchain` é no formato `Reason Only` enquanto os ChatGPT é no formato `Act Only`.
![Aula 02.1](/github/images/image-6.png)

### Correção do Warning

Começamos a aula 2 fazendo a correção do alerta que é exibido no terminal sobre o fim do suporte da função `initialize_agent`.

```jsx
The function `initialize_agent` was deprecated in LangChain 0.1.0 and will be removed in 0.3.0. Use Use new agent constructor methods like create_react_agent, create_json_agent, create_structured_chat_agent, etc. instead.
```

## AULA 02.2

### Refactor função de busca

Movemos tudo que diz respeito ao envio do input do usuário para o LLM para a função `researchAgent`

## AULA 02.3

### Evoluções no Modelo

Atualmente temos esta estrutura pronta
![Aula 02.3](/github/images/image-7.png)

Nosso objetivo foi evoluir nosso modelo para está estrutura abaixo, com isso conseguiremos trazer uma resposta pro usuário mais completa e com mais detalhes.
![Aula 02.3](/github/images/image-8.png)

Além disso, adicionamos também um `Supervisor`. Esse Supervisor tem como tarefa conferir/revisar a informação que o Agente trouxe e melhorar o resultado final entregue ao usuário, dessa forma teremos duas LLM's separadas que vão trabalhar em conjunto.

O Supervisor também pode ser um intermediário de vários Agentes, compilando a informação que esses agentes enviam e encaminhando o resultado final como resposta para o usuário. Essa é uma outra forma de usar o Supervisor.
![Aula 02.3](/github/images/image-9.png)
![Aula 02.3](/github/images/image-10.png)

### RAG => Retrieval-Augmented Generation

Ao invés de fazer a conexão com o site `dicasdeviagem.com` utilizando a internet, fizemos a busca da informação utilizando o método RAG.

Passo a passo:

- Pegamos o conteúdo que está dentro do site `dicasdeviagens`;
- Transformamos a informação em um embedding;

  | Embeddings => um Embedding é quando pegamos qualquer tipo de informação e a transformamos em uma informação numérica,para que o modelo de IA possa fazer uso dele de forma mais efetiva.

- Salvamos a informação dentro de banco vetorial.

Essa abordagem pode ser feita com qualquer documento estático. Utilizamos o banco vetorial `Chroma`.

| Fim da AULA 02

#######################################################################################################

# AULA 03

## AULA 03.1

### Sobre o Deploy

O deploy da aplicação será feito na AWS. Antes disso, fizemos a atualização do código para que seja compatível com as chamadas da lambda.
Inicialmente convertemos nossa aplicação em uma imagem docker. Essa imagem será enviada para o `ECR Registry` da AWS, serviço responsável por fazer todo o versionamento de versões e gestão, e a partir do `ECR` vamos utilizar essa imagem para fazer o deploy de uma `Lambda Function`, uma função serverless para fazer o código rodar.

![Aula 03.1](/github/images/image-11.png)

## AULA 03.2

### Requirements.txt

O arquivo `requirements.txt`é o arquivo no qual declaramos todas as dependências que o projeto utiliza. Esse arquivo será utilizado no `Dockerfile` para informar a lista de dependências que precisam ser instaladas antes de executar a aplicação.

| Nota Importante sobre instalação de dependências: Quando fazemos o import de uma lib no Python, fazemos utilizando o `underline` como separador, porém, para fazer a instalação, precisamos substituir o `underline` por `hífen`. Na dúvida, sempre faça a busca pelo nome da dependência no google seguido por `pip install` para confirmar a forma correta de salvar o nome da dependência no arquivo `.txt`.

## AULA 03.3

### Imagem no Docker

O arquivo `Dockerfile` é aonde colocamos as informações sobre a imagem que será criada para uso no docker.
`LAMBDA_TASK_ROOT` -> Funções que devem ser executadas antes das coisas estarem funcionando.

`docker build --platform linux/x86_64 -t travelagent .`

### Conta na AWS

Para seguir para as próximas etapas de deploy, criamos uma conta na AWS.

### ECR

Após buscar por `ECR` na AWS, clicar em `Criar Repositório` e informar o nome desse novo repositório.

![Aula 03.3](/github/images/image-12.png)

### AWS Command Line Interface

Fizemos uso da AWS CLI para fazer o upload da nossa imagem do docker para a AWS.
https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html

#### IAM - Usuário não criado

Caso você acesso o IAM e não tenha um usuário criado, vamos ensinar rapidamente como criar um com a permissão necessário

1. Acesse o IAM
2. Clique na opção `Usuários` no menu lateral esquerdo
3. Clique no botão `Criar usuário`

   ![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/f1cc6d84-3852-4ba0-a14f-aed47f1d62ea/2e9ef969-1519-499a-90fb-65c75f22753f/Untitled.png)

4. Dê o nome que quiser ao usuário e clique em `Próximo`

   ![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/f1cc6d84-3852-4ba0-a14f-aed47f1d62ea/79c6d947-3cda-4fcc-9282-0ea3017d9b3d/Untitled.png)

5. Selecione a opção `Anexar políticas diretamente` e selecione `AdministratorAccess`. Clique em `Próximo`

   ![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/f1cc6d84-3852-4ba0-a14f-aed47f1d62ea/bebd59c3-48b6-494c-9bb9-e0fe15a6dcb9/Untitled.png)

6. Revise as informações. Se tudo estiver certo, clique em `Criar usuário`

   ![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/f1cc6d84-3852-4ba0-a14f-aed47f1d62ea/8659682b-d653-4b06-b18e-ccf633d20818/Untitled.png)

7. Acesse o usuário criado

8. Clique em `Security Credentials`

9. Navegue até `Access Keys` e clique em `Create access key`

10. Em `Use Case` selecione a opção `CLI`, confirme a box no canto inferior da página

11. Defina uma tag. No nosso caso colocamos: `cli-deywerson`

### AWS Configure

1 - Execute o comando `aws configure --profile {profile_name}`

2 - Informe as credenciais do `IAM` da AWS (Access Key, Secret Access Key e Region. Output pode deixar vazio).

### Enviando Imagem do Docker para AWS

1 - Em ECR, clique no repositório criado

2 - Clique em `View Push Commands`
![Aula 03.3](/github/images/image-13.png)

3 - Execute as linhas de comando para `macOS/Linux`. No primeiro passo, que refere-se a conseguir o token de autenticação fizemos uma pequena modificação na linha de comando para que o login fosse efetuado utilizando o profile `deywersontest`, criado anteriormente durante a configuração do profile aws.
`aws ecr get-login-password --region eu-central-1  --profile deywersontest | docker login --username AWS --password-stdin 008971639242.dkr.ecr.eu-central-1.amazonaws.com`

4 - O segundo passo pulamos, pois já haviamos feito build do nosso projeto

5 - Execute as linha de código do passo 3 e 4 mostrados nas instruções de `Push commands`.

### Criando função Lambda

1 - Vá em Lambdas

2 - `Create a function`

3 - Defina o nome da função e faça a busca pelo repositório, digitando o nome atribuído ao repositório anteriormente

![Aula 03.3](/github/images/image-14.png)

4 - Confirme a criação da função

5 - Vamos editar algumas configurações dessa função. A primeira delas será a `memória`, que vai para `512`, `timeout` para `15min`. Salve.

6 - O próximo passo é configurar a variável de ambiente utilizando a chave da OPENAI, portanto clique em `Configuration` e no canto esquerdo clique em `Environment variables`. Clique em `Edit`, `Add Environment Variable` e informe o nome e o valor da nova chave. Salve essas alterações.

### Rebuild do Projeto

Sempre que alguma alteração for feita no código, precisamos fazer uma nova build, adicionar nova tag e fazer o push para o repositório.
Por fim, precisamos acessar a lambda que criamos e atualizar o ponteiro de referência do código.

1 - `docker build --platform linux/x86_64 -t travelagent .`

2 - `docker tag travelagent:latest 008971639242.dkr.ecr.eu-central-1.amazonaws.com/travelagent:latest`

3 - `docker push 008971639242.dkr.ecr.eu-central-1.amazonaws.com/travelagent:latest`

4 - Busque por `Lambdas`

5 - Clique na aba `Image`

6 - `Deploy new image`

7 - Informe o nome do repositório

8 - Selecione a imagem que contém a tag `latest`

9 - Salve as alterações

### Testando a LAMBDA

1 - Clique na aba `Test`

2 - Defina o nome do Teste

3 - Atualize o corpo do teste baseado no que o código espera receber. No nosso caso, esperamos receber um `JSON` com a query `question` que tem como valor uma string.

![Aula 03.3](/github/images/image-15.png)

4 - Salve o teste

5 - Para executar basta clicar em `Test`

![Aula 03.3](/github/images/image-16.png)

## AULA 03.4

### ALB

Utilizamos o `ALB` - Application Load Balance conectado a Lambda para disponibilizar o nosso servido para uso externo

![Aula 03.4](/github/images/image-17.png)

Para fazer uso do Load Balancers utilizamos o `EC2` da AWS.

1 - Após procurar por `EC2`, clique em `Load Balancing` no menu esquerdo

2 - Clique em `Create load balancer`

3 - Selecione o Load Balancer que mais se enquadra a finalidade do projeto. No nosso caso foi o `Application Load Balancer`

4 - Em `Basic Configuration` defina o nome da aplicação. Como nosso serviço ficará disponível na internet, selecionamos o schema `Internet facing`. Mantenha o `IPV4` selecionado

![Aula 03.4](/github/images/image-18.png)

5 -Em `Network Mapping` deixe o `VPC` que vem por padrão. Marque todos os `subnets` disponíveis

![Aula 03.4](/github/images/image-19.png)

6 - Em `Security groups` mantenha o valor default

![Aula 03.4](/github/images/image-20.png)

7 - Em `Listeners and routing` vamos utilizar o protocolo `HTTP` apenas para remover a necessidade de configurar um certificado SSL. Utilizamos a porta `80`.

7.1 - Criamos um novo `target group` para indicar a lambda que vamos utilizar nesse ALB

7.2 - Selecione `Lambda function`, e defina o target group name, clique em `Next`

7.3 - Informe qual lambda function e qual versão deverá ser utilizada e confirme a criação em `Create target group`

![Aula 03.4](/github/images/image-21.png)

8 - Defina a `Default action` para ser o novo target group criado

![Aula 03.4](/github/images/image-22.png)

9 - Confirme a criação do `Load Balance`

Dessa forma já temos uma API exposta que pode ser utilizada.

### Ajustes no ALB - Segurança

1 - Com o load balance criado, vamos acessar a aba de `Security`

2 - Clique no `Security Group` listado

3 - Na nova página, vamos editar as `Inbound Rules`

4 - Altere as informações conforme a imagem abaixo. Essas configurações vão permitir que qualquer endereço IP tenha acesso a nossa aplicação.

![Aula 03.4](/github/images/image-23.png)

5 - Atualizamos o `lambda_handler` para ser compatível com a chamada de API

6 - Utilizamos o postman para executar a chamada para a API, para efeito de testes. o `DNS` da API está disponível nos detalhes do nosso Load Balance.
