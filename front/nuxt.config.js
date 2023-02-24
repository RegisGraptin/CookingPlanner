export default {
  // Global page headers: https://go.nuxtjs.dev/config-head
  head: {
    titleTemplate: '%s - front',
    title: 'front',
    htmlAttrs: {
      lang: 'en'
    },
    meta: [
      { charset: 'utf-8' },
      { name: 'viewport', content: 'width=device-width, initial-scale=1' },
      { hid: 'description', name: 'description', content: '' },
      { name: 'format-detection', content: 'telephone=no' }
    ],
    link: [
      { rel: 'icon', type: 'image/x-icon', href: '/favicon.ico' }
    ]
  },

  // Global CSS: https://go.nuxtjs.dev/config-css
  css: [
    '@/assets/css/main.css',
  ],

  // Plugins to run before rendering page: https://go.nuxtjs.dev/config-plugins
  plugins: [
  ],

  // Auto import components: https://go.nuxtjs.dev/config-components
  components: true,

  // Modules for dev and build (recommended): https://go.nuxtjs.dev/config-modules
  buildModules: [
    // https://go.nuxtjs.dev/typescript
    '@nuxt/typescript-build',

    '@nuxt/postcss8',
  ],

  // Modules: https://go.nuxtjs.dev/config-modules
  modules: [
    '@nuxtjs/axios',
    '@nuxtjs/auth-next',             // https://auth.nuxtjs.org/
    '@nuxtjs/i18n',
    'nuxt-logger',
    ['nuxt-tailvue', {all: true}],   // https://github.com/acidjazz/nuxt-tailvue
  ],

  // Axios module configuration (https://go.nuxtjs.dev/config-axios)
  axios: {
    proxy: true,
  },

  proxy: {
    '/cookingplanner': {
      target:
        process.env.NODE_ENV === 'production'
          ? 'http://0.0.0.0:8000/' // TODO :: https://backend/ Can be use for docker configuration later on
          : 'http://0.0.0.0:8000/',
      pathRewrite: {
        '^/cookingplanner': '',
      },
      changeOrigin: false,
    },
  },

  auth: {
    strategies: {
      local: {
        token: {
          property: 'token',
          global: true,
        },
        user: {
          property: 'user',
          autoFetch: false,
        },
        endpoints: {
          login:  {url: '/cookingplanner/auth/login', method: 'POST' },
          logout: {url: '/cookingplanner/auth/logout', method: 'POST' },
          user:   {url: '/cookingplanner/auth/user', method: 'GET' },
        }
      }
    }
  },


  i18n: {
    locales: [
      {
        name: 'English',
        code: 'en',
        iso: 'en-US',
        file: 'en-US.js',
      },
      {
        name: 'Français',
        code: 'fr',
        iso: 'fr-FR',
        file: 'fr-FR.js',
      },
    ],
    lazy: true,
    langDir: 'lang/',
    defaultLocale: 'fr',
  },

  logger: {
      isEnabled: process.env.NODE_ENV === 'production' ? false : true,
      logLevel: 'debug', // debug, info, warn or error, defaults to debug
  },

  // Build Configuration: https://go.nuxtjs.dev/config-build
  build: {
    postcss: {
      plugins: {
        tailwindcss: {},
        autoprefixer: {},
      },
    },
  }
}
