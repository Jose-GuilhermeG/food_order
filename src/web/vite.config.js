import { defineConfig } from 'vite'
import tailwindcss from '@tailwindcss/vite'
import react from '@vitejs/plugin-react'
import { qrcode } from 'vite-plugin-qrcode'

export default defineConfig({
  root : "./src/web",
  plugins: [
    react(),
    tailwindcss(),
    qrcode(),
  ],
  server : {
    port : 5000,
  },
})
