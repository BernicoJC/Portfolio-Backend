import { defineConfig } from 'vite';
import react from '@vitejs/plugin-react';

export default defineConfig({
  plugins: [react()],
  build: {
    rollupOptions: {
      external: ['react-router-dom']
    }
  },
  server: {
    port: process.env.PORT || 4173,
    host: '0.0.0.0',
    proxy: {
      '/api': 'http://127.0.0.1:5000'
    }
  }
});
