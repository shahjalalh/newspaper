/* eslint-disable import/prefer-default-export */
/*
 * Site-wide application constants
 * Mostly relevant for triggering global DOM Events.
 */
export const VIEWPORT_STATES = ['xs', 'sm', 'md', 'lg', 'xl'];
export const VIEWPORT_ACTIVE = 'viewport:active';
export const VIEWPORT_LOADED = 'viewport:loaded';
export const VIEWPORT_CHANGED = 'viewport:changed';

export const WINDOW_RESIZE = 'window:resize';

export const DEV = 'development';
export const PRD = 'production';
export const DEBUG = process.env.NODE_ENV === DEV;
