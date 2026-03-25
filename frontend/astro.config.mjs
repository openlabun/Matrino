import { defineConfig } from 'astro/config';
import tailwind from "@astrojs/tailwind";
import fs from "node:fs";
import path from "node:path";

import react from "@astrojs/react";

function getGlobalEnvValue(key) {
  const globalEnvPath = path.resolve(process.cwd(), "..", ".env");
  if (!fs.existsSync(globalEnvPath)) return undefined;

  const envContent = fs.readFileSync(globalEnvPath, "utf-8");
  const lines = envContent.split(/\r?\n/);

  for (const line of lines) {
    const trimmedLine = line.trim();
    if (!trimmedLine || trimmedLine.startsWith("#")) continue;

    const separatorIndex = trimmedLine.indexOf("=");
    if (separatorIndex === -1) continue;

    const envKey = trimmedLine.slice(0, separatorIndex).trim();
    if (envKey !== key) continue;

    const envValue = trimmedLine.slice(separatorIndex + 1).trim();
    return envValue.replace(/^['\"]|['\"]$/g, "");
  }

  return undefined;
}

const apiPort = process.env.API_PORT ?? getGlobalEnvValue("API_PORT") ?? "3000";
const apiUrl = process.env.API_URL ?? getGlobalEnvValue("API_URL") ?? `http://localhost:${apiPort}`;

// https://astro.build/config
export default defineConfig({
  integrations: [
    tailwind({
      applyBaseStyles: false,
    }), 
    react()
  ],
  vite: {
    server: {
      proxy: {
        '/api': {
          target: apiUrl,
          changeOrigin: true,
          rewrite: (requestPath) => requestPath.replace(/^\/api/, ''),
        },
      },
    },
    preview: {
      proxy: {
        '/api': {
          target: apiUrl,
          changeOrigin: true,
          rewrite: (requestPath) => requestPath.replace(/^\/api/, ''),
        },
      },
    },
  },
});