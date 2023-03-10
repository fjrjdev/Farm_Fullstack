# Sobre o projeto

Este repositório contém uma aplicação web que permite o gerenciamento de fazendas, com as operações básicas de CRUD (Criar, Ler, Atualizar e Deletar). Ela é desenvolvida utilizando Angular como front-end e Django como back-end, e executada por padrão em http://localhost:8000. O objetivo é oferecer uma solução fácil e eficiente para administrar fazendas.

# Uso

A aplicação permite que você crie, leia, atualize e delete fazendas. As operações de CRUD podem ser realizadas através da interface web.

# Repositorios

- [Front End](https://github.com/fjrjdev/Farm_Front)
- [Backend End](https://github.com/fjrjdev/Farm_Backend)

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
- **Etapa 5: Acessar o aplicativo**
- Visite no seu navegador da Web.
```
 http://localhost:4200/ 

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
- Visite no seu navegador da Web.
```
http://localhost:8000/


```
 
Nota: Certifique-se de ter o docker em seu sistema antes de executar os comandos acima.

# Screenshots

![Create Farm](https://i.imgur.com/5oWG3KX.png)
![List Farm](https://i.imgur.com/gTYpkPD.png)
![Detail, Edit and Exclude Farm](https://i.imgur.com/gQhwmMe.png)
![Edit Farm](https://i.imgur.com/I2oaOsG.png)
