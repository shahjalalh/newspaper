import { Router as BackboneRouter } from 'backbone';
import { ViewportComponent } from 'components';


class Router extends BackboneRouter {

    get componentMap() {
        return {
            viewport: ViewportComponent,
        };
    }

    initialize() {
        this._loadComponents();
    }

    _loadComponents() {
        this.activeComponents = [];
        const elementlist = document.querySelectorAll('[data-component]');

        [].slice.call(elementlist).forEach((el) => {
            const indexes = JSON.parse(el.getAttribute('data-component'));
            indexes.map(this._loadComponent.bind(this, el));
        });
    }

    _loadComponent(el, component) {
        if (component in this.componentMap) {
            const instance = new this.componentMap[component](el);
            this.activeComponents.push(instance);
        }
    }

}

export default Router;
