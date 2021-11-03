module.exports = {
  env: {
    browser: true,
  },
  extends: [
    'plugin:vue/essential',
    'airbnb-base',
  ],
  parserOptions: {
    ecmaVersion: 13,
    parser: '@typescript-eslint/parser',
    sourceType: 'module',
  },
  plugins: [
    'vue',
    '@typescript-eslint',
  ],
  rules: {
    "no-console":"off",
    "no-alert":"off",
    "no-plusplus":"off",
    "import/no-unresolved":"off",
    "vue/valid-v-slot":"off",
    "vue/multi-word-component-names":"off"
  },
};
