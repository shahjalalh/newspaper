class AbstractComponent {

    get loadViews() {
        throw new Error('[Component::loadViews] Not implemented by subclass');
    }

    constructor(el) {
        this.el = el;
        this.activeViews = [];

        this.loadViews.forEach((ViewClass) => {
            const instance = new ViewClass({
                el: this.el,
                component: this,
                model: this.model,
            });
            this.activeViews.push(instance);
        });
    }

    destroy() {
        this.activeViews.forEach((view) => {
            if ('destroy' in view) {
                view.destroy();
            }
        });
    }

}

export default AbstractComponent;
