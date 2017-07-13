import { Model } from 'backbone';

import {
    VIEWPORT_ACTIVE, VIEWPORT_LOADED,
    VIEWPORT_CHANGED, WINDOW_RESIZE,
} from 'constants';

import { Radio } from 'utils/radio';

class StateModel extends Model {
    get defaults() {
        return {
            loaded: false,
            xs: false,
            sm: false,
            md: false,
            lg: false,
            xl: false,
        };
    }

    initialize() {
        this.listenTo(this, 'change', this._onChange);
        this.listenTo(Radio.viewport, WINDOW_RESIZE, this._applyCurrentViewPort);

        Radio.viewport.reply(VIEWPORT_ACTIVE, this._getActiveViewport.bind(this));
    }

    /**
     * The model state changes when the viewport changes.
     * When this happens we send a global Backbone Event.
     */
    _onChange(model) {
        const activeState = this.get('active');
        const initialLoad = this.changed.loaded || false;
        if (initialLoad) Radio.viewport.trigger(VIEWPORT_LOADED);
        Radio.viewport.trigger(VIEWPORT_CHANGED, activeState, model, initialLoad);
    }

    /**
     * On a window resize we apply the viewport response.
     * Depending if the viewport is actually changed it throw a change on props.
     *
     * @param {Event} event - Proxied window event by Backbone Radio
     * @param {string} viewport - Corresponding Bootstrap viewport (xs - xxl)
     */
    _applyCurrentViewPort(event, viewport) {
        const currentState = this.defaults;
        currentState[viewport] = true;
        currentState.active = viewport;
        currentState.loaded = true;
        this.set(currentState);
    }

    _getActiveViewport() {
        return this.get('active');
    }
}

export default StateModel;
