import { View } from 'backbone';

class AbstractView extends View {

    _ui = {}

    set ui(bindings) {
        Object.entries(bindings).forEach(this._bindElement, this);
        this.trigger('onInitialized');
    }

    get ui() {
        return this._ui;
    }

    _bindElement([key, elem]) {
        this._ui[key] = this.$(elem);
    }

    set events(events) {
        const _events = this.delegateEvents(events);
        return _events;
    }

    destroy() {
        delete this._ui;
        this.stopListening();
        this.undelegateEvents();
    }
}

export default AbstractView;
