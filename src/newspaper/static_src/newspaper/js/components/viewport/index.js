import { AbstractComponent } from 'abstracts';
import { StateModel } from './models';
import { ViewportView } from './views';

class ViewportComponent extends AbstractComponent {

    get model() {
        return new StateModel();
    }

    get loadViews() {
        return [
            ViewportView,
        ];
    }

}

export default ViewportComponent;
