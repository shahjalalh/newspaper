/* eslint-disable import/prefer-default-export */
/**
 * String utils
 */
export function unquote(str, quoteChar = '"') {
    if (str.startsWith(quoteChar) && str.endsWith(quoteChar)) {
        return str.slice(1, str.length - 1);
    }
    return str;
}
