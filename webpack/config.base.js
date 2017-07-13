import path from 'path';
import autoprefixer from 'autoprefixer';
import mqpacker from 'css-mqpacker';
import flexbugs from 'postcss-flexbugs-fixes';
import webpack from 'webpack';

import CopyWebpackPlugin from 'copy-webpack-plugin';
import ExtractTextPlugin from 'extract-text-webpack-plugin';

import { config } from '../package.json';
import autoprefixerConfig from '../node-config/autoprefixer.json';

export const source = path.resolve(path.join(config.static.src, config.app));
export const destination = path.resolve(path.join(config.static.dest, config.app));

export default function(env) {
    return {
        entry: [
            'babel-polyfill',
            path.join(source, 'scss', 'main.scss'),
            path.join(source, 'js', 'main.js'),
        ],

        module: {
            rules: [
                {
                    test:  /\.scss$/,
                    use: ExtractTextPlugin.extract({
                        fallback: 'style-loader',
                        use: [{
                            loader: 'raw-loader',
                        }, {
                            loader: 'postcss-loader',
                            options: {
                                plugins: () => {
                                    flexbugs,
                                    autoprefixer(autoprefixerConfig),
                                    mqpacker
                                }
                            }
                        }, {
                            loader: 'sass-loader'
                        }],
                    }),
                },
                {
                    test: /\.js$/,
                    exclude: [/node_modules/],
                    use: [{
                        loader: 'babel-loader',
                        options: {
                            'presets': [
                                ['es2015', { 'modules': false }],
                                'stage-1'
                            ]
                        }
                    }],
                },
            ],
        },

        output: {
            filename: 'js/[name].js',
            path: destination,
        },

        plugins: [
            new webpack.DefinePlugin({
                'process.env': {
                    NODE_ENV: JSON.stringify(env),
                }
            }),
            new ExtractTextPlugin({
                filename: 'css/[name].css',
                disable: false,
                allChunks: true,
            }),
            new CopyWebpackPlugin([
                {
                    from: path.join(source, 'assets'),
                    to: path.join(destination, 'assets')
                },
            ]),
            new webpack.NoEmitOnErrorsPlugin(),
        ]
    }
};
