# Stage 1: Herw we build the Astro app!
FROM node:lts-alpine AS builder

RUN corepack enable && corepack prepare pnpm@latest --activate

WORKDIR /app

COPY package.json pnpm-lock.yaml ./

RUN pnpm install --frozen-lockfile

COPY . .

# This outputs to /dist
RUN pnpm run build

# Stage 2: Now, we create the server that is going to serve the files.
# In this occasion, we use Caddy for serving static files becuase we do not need
# a config file like nginx. Plus, the user runs as non-root by default which is more 
# secure! Of course, if we want to migrate to nginx we can do it, no problem with that
# :)
FROM caddy:2.10-alpine

COPY --from=builder /app/dist /usr/share/caddy

EXPOSE 8080

HEALTHCHECK --interval=30s --timeout=10s --start-period=5s --retries=3 \
    CMD wget --no-verbose --tries=1 --spider http://localhost:8080/ || exit 1

CMD ["caddy", "file-server", "--root", "/usr/share/caddy", "--listen", ":8080"]
