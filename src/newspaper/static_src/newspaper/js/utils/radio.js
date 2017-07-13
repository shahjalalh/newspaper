/* eslint-disable import/prefer-default-export, import/no-named-default */
import { default as BackboneRadio } from 'backbone.radio';
import { DEBUG } from 'constants';

BackboneRadio.DEBUG = DEBUG;

export const Radio = {
    viewport: BackboneRadio.channel('viewport'),
};
