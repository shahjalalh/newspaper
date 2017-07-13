import webpack from 'webpack';
import base from './config.base';

const config = base('production');

// production overrides go here
config.plugins = config.plugins.concat([
    new webpack.optimize.UglifyJsPlugin({
        compress: {
            screw_ie8: true,
            warnings: false
        },
        mangle: {
            screw_ie8: true,
        },
        output: {
            comments: false,
            screw_ie8: true,
        },
    }),
]);

export default config;
