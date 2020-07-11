'use strict';
Object.defineProperty(exports, "__esModule", { value: true });
// The module 'vscode' contains the VS Code extensibility API
// Import the module and reference it with the alias vscode in your code below
const vscode = require("vscode");
const dict = require("cspell-dict-es-es");
const local = 'es';
// this method is called when your extension is activated
// your extension is activated the very first time the command is executed
function activate(context) {
    const vscodeSpellCheckerExtension = 'streetsidesoftware.code-spell-checker';
    const extension = vscode.extensions.getExtension(vscodeSpellCheckerExtension);
    if (extension) {
        extension.activate().then(ext => {
            const path = dict.getConfigLocation();
            ext && ext.registerConfig && ext.registerConfig(path);
        });
    }
    function enableSpanish(isGlobal) {
        extension && extension.activate().then(ext => {
            ext && ext.enableLocal && ext.enableLocal(isGlobal, local);
        });
    }
    function disableSpanish(isGlobal) {
        extension && extension.activate().then(ext => {
            ext && ext.disableLocal && ext.disableLocal(isGlobal, local);
        });
    }
    // Push the disposable to the context's subscriptions so that the
    // client can be deactivated on extension deactivation
    context.subscriptions.push(vscode.commands.registerCommand('cSpell.enableSpanish', () => enableSpanish(true)), vscode.commands.registerCommand('cSpell.disableSpanish', () => disableSpanish(true)), vscode.commands.registerCommand('cSpell.enableSpanishWorkspace', () => enableSpanish(false)), vscode.commands.registerCommand('cSpell.disableSpanishWorkspace', () => disableSpanish(false)));
}
exports.activate = activate;
// this method is called when your extension is deactivated
function deactivate() {
}
exports.deactivate = deactivate;
//# sourceMappingURL=extension.js.map