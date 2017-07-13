import { AbstractView } from 'abstracts';

class ViewportView extends AbstractView {

    ui = {
        body: 'body',
        content: '[data-content]',
    }

    initialize() {
        this.listenTo(this, 'onInitialized', this._updateBodyClass);
    }

    _updateBodyClass() {
        this.ui.body.removeClass('preload');
    }

}

export default ViewportView;
