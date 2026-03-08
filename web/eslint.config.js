import js from '@eslint/js';
import tseslint from 'typescript-eslint';
import eslintPluginAstro from 'eslint-plugin-astro';
import eslintPluginSvelte from 'eslint-plugin-svelte';
import svelteParser from 'svelte-eslint-parser';
import eslintConfigPrettier from 'eslint-config-prettier';
import globals from 'globals';

export default [
  // Global ignores
  { ignores: ['dist/', '.astro/', 'node_modules/', '.vercel/'] },

  // Base JS config
  js.configs.recommended,

  // TypeScript
  ...tseslint.configs.recommended,

  // Astro
  ...eslintPluginAstro.configs.recommended,

  // Svelte — with TypeScript parser for <script lang="ts">
  ...eslintPluginSvelte.configs['flat/recommended'].map((config) =>
    config.files
      ? {
          ...config,
          languageOptions: {
            ...config.languageOptions,
            parser: svelteParser,
            parserOptions: {
              ...config.languageOptions?.parserOptions,
              parser: tseslint.parser,
            },
          },
        }
      : config,
  ),

  // Global settings
  {
    languageOptions: {
      globals: {
        ...globals.browser,
        ...globals.node,
      },
    },
    rules: {
      '@typescript-eslint/no-explicit-any': 'warn',
      '@typescript-eslint/no-unused-vars': [
        'warn',
        { argsIgnorePattern: '^_', varsIgnorePattern: '^_' },
      ],
      '@typescript-eslint/no-unused-expressions': 'off',
      'no-console': 'off',
      'no-case-declarations': 'off',
      'no-useless-assignment': 'warn',
    },
  },

  // Allow triple-slash references in env.d.ts (Astro convention)
  {
    files: ['src/env.d.ts'],
    rules: {
      '@typescript-eslint/triple-slash-reference': 'off',
    },
  },

  // Lenient Svelte rules — existing code uses these patterns intentionally
  {
    files: ['**/*.svelte'],
    rules: {
      'svelte/no-at-html-tags': 'warn',
      'svelte/require-each-key': 'warn',
      'svelte/no-dom-manipulating': 'warn',
    },
  },

  // Prettier must be last to override conflicting rules
  eslintConfigPrettier,
];
