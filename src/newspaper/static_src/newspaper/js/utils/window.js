import { debounce } from 'throttle-debounce';

import { WINDOW_RESIZE } from 'constants';
import { Radio } from 'utils/radio';
import { unquote } from 'utils/helpers';


class Window {

    get previousScrollTop() {
        return this._previousScrollTop || 0;
    }

    set previousScrollTop(val) {
        this._previousScrollTop = val;
    }

    constructor() {
        window.addEventListener('load', this._onResize.bind(this));
        window.addEventListener('resize', debounce(100, this._onResize.bind(this)));
    }

    _onResize(event) {
        Radio.viewport.trigger(WINDOW_RESIZE, event, this._getBreakpoint());
    }

    _getBreakpoint() {
        const after = window.getComputedStyle(window.document.documentElement, ':after');
        const content = unquote(after.getPropertyValue('content'));
        return content;
    }
}

export default Window;
