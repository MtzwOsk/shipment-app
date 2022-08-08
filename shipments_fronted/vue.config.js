const path = require('path');

module.exports = {
    // Should be STATIC_URL + path/to/build
   publicPath: '/static/src/vue/dist/', // Should be STATIC_URL + path/to/build
    outputDir: path.resolve(__dirname, '../static/src/vue/dist/'), // Output to a directory in STATICFILES_DIRS
    filenameHashing: false, // Django will hash file names, not webpack
    runtimeCompiler: true, // See: https://vuejs.org/v2/guide/installation.html#Runtime-Compiler-vs-Runtime-only

    devServer: {
        devMiddleware: {
            writeToDisk: true,
        },
    },

    pluginOptions: {
        vuetify: {
            // https://github.com/vuetifyjs/vuetify-loader/tree/next/packages/vuetify-loader
        }
    },
    configureWebpack: {
        optimization: {
            splitChunks: {
                chunks: 'async',
                minSize: 200000,
            }
        }
    }
};
