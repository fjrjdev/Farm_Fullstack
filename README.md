# Sobre o projeto

Este projeto consiste na implementação de um sistema de CRUD (Create, Read, Update e Delete) para fazendas utilizando Angular. A aplicação está baseada em um back-end utilzando Django, que é executado por padrão em http://localhost:8000

# Uso

A aplicação permite que você crie, leia, atualize e delete fazendas. As operações de CRUD podem ser realizadas através da interface web.

## Iniciando o projeto frontend

Requerimentos:
Angular 11

- **Etapa 1: clonar o repositório**

```
git@github.com:fjrjdev/Farm_Fullstack.git
```

- **Etapa 2: Abra o diretório do repositório clonado**

```
cd frontend
```

- **Etapa 3: Instalar as dependencias**

```
npm installl
```

- **Etapa 4: Inicie o projeto**

```
ng serve
```

## Iniciando o projeto backend com Docker

Nota: Caso não tenha docker instalado, utilize o README.MD dentro da pasta /backend para iniciar a API

<br>

- **Etapa 1: clonar o repositório**

```
git@github.com:fjrjdev/Farm_Fullstack.git
```

Nota: Caso já tenha clonado pule essa etapa

- **Etapa 2: Abra o diretório do repositório clonado**

```
cd backend
```

- **Etapa 3: Criar o aplicativo**

```
docker compose up --build
```

Esse comando criará as imagens e os contêineres necessários para o aplicativo.

- **Step 4: Start the application**

```
docker compose up
```

- **Etapa 5: Acessar o aplicativo**

```
Visite http://localhost:8000/ no seu navegador da Web.

Nota: Certifique-se de ter o docker em seu sistema antes de executar os comandos acima.
```
