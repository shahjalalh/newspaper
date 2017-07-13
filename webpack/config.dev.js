import BrowserSyncPlugin from 'browser-sync-webpack-plugin';
import StyleLintPlugin from 'stylelint-webpack-plugin';
import base, { source } from './config.base';

const config = base('development');

// development overrides go here
config.watch = true;
config.devtool = 'inline-source-map'; // See http://webpack.github.io/docs/configuration.html#devtool

config.module.rules = config.module.rules.concat([
    {
        test: /\.js$/,
        include: [source],
        loader: 'eslint-loader',
        enforce: 'pre',
    }
]);

config.plugins = config.plugins.concat([
    new StyleLintPlugin({
        context: source,
        syntax: 'scss',
    }),
    new BrowserSyncPlugin({
        host: 'localhost',
        port: 3000,
        proxy: 'http://localhost:8000/',
    }),
]);

export default config;
