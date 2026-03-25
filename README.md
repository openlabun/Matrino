<div align="center">

<strong><h1>Matrino - Teoría de Códigos y Matemática Discreta</h1></strong>

<a name="readme-top"></a>

[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]

</div>

## 📎 Descripción

**Matrino** es una aplicación web para trabajar algoritmos de **Teoría de Códigos** (códigos lineales, matrices generadoras, matrices de control y códigos duales), construida por estudiantes de la **Universidad del Norte**.

El proyecto tiene dos partes:
- **Frontend** en Astro + React
- **Backend** en FastAPI, ejecutado sobre **SageMath** para los cálculos matemáticos

## 🗂️ Índice

- [📎 Descripción](#-descripción)
- [🚀 Tech Stack](#-tech-stack)
- [🏗️ Arquitectura del Proyecto](#️-arquitectura-del-proyecto)
- [⚙️ Variables de Entorno](#️-variables-de-entorno)
- [🧑‍💻 Ejecución Local](#-ejecución-local)
- [📡 Endpoints](#-endpoints)
- [🤝 Contribuir](#-contribuir)

## 🚀 Tech Stack

### Frontend
- [![Astro][astro-badge]][astro-url]
- [![React][react-badge]][react-url]
- [![TypeScript][typescript-badge]][typescript-url]
- [![Tailwind CSS][tailwind-badge]][tailwind-url]
- [![pnpm][pnpm-badge]][pnpm-url]

### Backend
- [![FastAPI][fastapi-badge]][fastapi-url]
- [![Uvicorn][uvicorn-badge]][uvicorn-url]
- [![SageMath][sagemath-badge]][sagemath-url]

### Infraestructura
- [![Docker][docker-badge]][docker-url]
- [![Docker Compose][compose-badge]][compose-url]
- [![Caddy][caddy-badge]][caddy-url]

## 🏗️ Arquitectura del Proyecto

```text
Matrino/
├── docker-compose.yaml
├── .env.example
├── backend/
│   ├── Dockerfile
│   ├── requirements.txt
│   └── src/
│       ├── main.py
│       ├── api/v1/
│       │   ├── router.py
│       │   └── routes/code/endpoints.py
│       └── schemas/v1/
└── frontend/
    ├── Dockerfile
    ├── Caddyfile
    ├── astro.config.mjs
    ├── package.json
    └── src/
        ├── components/
        └── pages/
```

## ⚙️ Variables de Entorno

Crea un archivo `.env` en la raíz (puedes copiar desde `.env.example`):

```bash
cp .env.example .env
```

Variables necesarias:

```env
API_PORT=3000
FRONTEND_PORT=1234
API_URL=http://matrino-api:3000
```

Notas:
- `API_URL` debe apuntar al servicio backend accesible desde el contenedor frontend.
- En Docker Compose, el valor recomendado es `http://matrino-api:3000`.

## 🧑‍💻 Ejecución Local

### Opción recomendada: Docker Compose (raíz del proyecto)

```bash
docker compose up --build -d
```

Servicios:
- Frontend: `http://localhost:${FRONTEND_PORT}`
- API: `http://localhost:${API_PORT}`
- Healthcheck API: `http://localhost:${API_PORT}/health`

Detener servicios:

```bash
docker compose down
```

### Desarrollo del frontend (sin Docker)

```bash
cd frontend
pnpm install
pnpm dev
```

## 📡 Endpoints

Base URL API: `http://localhost:${API_PORT}`

Versión: `/v1`

### Health
- `GET /health`

### Teoría de códigos
- `POST /v1/code-theory/code-to-generator`
- `POST /v1/code-theory/lineal-code`
- `POST /v1/code-theory/generator-to-control`
- `POST /v1/code-theory/dual`

Ejemplo de respuesta exitosa:

```json
{
  "success": true,
  "message": "Control matrix obtained",
  "matrix": [[0,0,1,0],[0,0,0,1]]
}
```

Ejemplo de respuesta de error:

```json
{
  "success": false,
  "message": "Error message"
}
```

## 🤝 Contribuir

1. Crea una rama desde `main`
2. Realiza tus cambios
3. Verifica que el proyecto levante con `docker compose up --build`
4. Abre un Pull Request

---

<div align="center">

Hecho con ❤️ por estudiantes de Ingeniería de Sistemas - Universidad del Norte.

</div>

<!-- Repository Links -->

[contributors-shield]: https://img.shields.io/github/contributors/openlabun/Matrino.svg?style=for-the-badge
[contributors-url]: https://github.com/openlabun/Matrino/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/openlabun/Matrino.svg?style=for-the-badge
[forks-url]: https://github.com/openlabun/Matrino/network/members
[stars-shield]: https://img.shields.io/github/stars/openlabun/Matrino.svg?style=for-the-badge
[stars-url]: https://github.com/openlabun/Matrino/stargazers
[issues-shield]: https://img.shields.io/github/issues/openlabun/Matrino.svg?style=for-the-badge
[issues-url]: https://github.com/openlabun/Matrino/issues

<!-- Tech Links -->

[astro-url]: https://astro.build/
[react-url]: https://react.dev/
[typescript-url]: https://www.typescriptlang.org/
[tailwind-url]: https://tailwindcss.com/
[pnpm-url]: https://pnpm.io/
[fastapi-url]: https://fastapi.tiangolo.com/
[uvicorn-url]: https://www.uvicorn.org/
[sagemath-url]: https://www.sagemath.org/
[docker-url]: https://www.docker.com/
[compose-url]: https://docs.docker.com/compose/
[caddy-url]: https://caddyserver.com/

<!-- Tech Badges -->

[astro-badge]: https://img.shields.io/badge/Astro-000000?style=for-the-badge&logo=astro&logoColor=white
[react-badge]: https://img.shields.io/badge/React-61DAFB?style=for-the-badge&logo=react&logoColor=black
[typescript-badge]: https://img.shields.io/badge/TypeScript-3178C6?style=for-the-badge&logo=typescript&logoColor=white
[tailwind-badge]: https://img.shields.io/badge/Tailwind_CSS-06B6D4?style=for-the-badge&logo=tailwindcss&logoColor=white
[pnpm-badge]: https://img.shields.io/badge/pnpm-F69220?style=for-the-badge&logo=pnpm&logoColor=white
[fastapi-badge]: https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white
[uvicorn-badge]: https://img.shields.io/badge/Uvicorn-499848?style=for-the-badge&logo=python&logoColor=white
[sagemath-badge]: https://img.shields.io/badge/SageMath-0F4C81?style=for-the-badge&logo=python&logoColor=white
[docker-badge]: https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white
[compose-badge]: https://img.shields.io/badge/Docker_Compose-1D63ED?style=for-the-badge&logo=docker&logoColor=white
[caddy-badge]: https://img.shields.io/badge/Caddy-1F88C0?style=for-the-badge&logo=caddy&logoColor=white
