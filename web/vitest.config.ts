import { defineConfig } from 'vitest/config';
import { resolve } from 'path';

export default defineConfig({
  test: {
    environment: 'node',
    include: ['src/**/*.test.ts'],
  },
  resolve: {
    alias: {
      '@components': resolve(__dirname, 'src/components'),
      '@layouts': resolve(__dirname, 'src/layouts'),
      '@utils': resolve(__dirname, 'src/utils'),
    },
  },
});
