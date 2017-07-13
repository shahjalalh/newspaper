import Backbone from 'backbone';

import { DefaultRouter } from 'routers';
import Window from 'utils/window';

class Application {

    constructor() {
        this.window = new Window();
        this.setupRouter();
    }

    setupRouter() {
        this.router = new DefaultRouter();
        Backbone.history.start({
            hashChange: false,
            pushState: true,
            root: '/',
        });
    }

}

(function boot() {
    return new Application();
}());
