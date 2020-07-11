"use strict";
var __createBinding = (this && this.__createBinding) || (Object.create ? (function(o, m, k, k2) {
    if (k2 === undefined) k2 = k;
    Object.defineProperty(o, k2, { enumerable: true, get: function() { return m[k]; } });
}) : (function(o, m, k, k2) {
    if (k2 === undefined) k2 = k;
    o[k2] = m[k];
}));
var __setModuleDefault = (this && this.__setModuleDefault) || (Object.create ? (function(o, v) {
    Object.defineProperty(o, "default", { enumerable: true, value: v });
}) : function(o, v) {
    o["default"] = v;
});
var __importStar = (this && this.__importStar) || function (mod) {
    if (mod && mod.__esModule) return mod;
    var result = {};
    if (mod != null) for (var k in mod) if (k !== "default" && Object.hasOwnProperty.call(mod, k)) __createBinding(result, mod, k);
    __setModuleDefault(result, mod);
    return result;
};
Object.defineProperty(exports, "__esModule", { value: true });
exports.replaceWebviewPlaceholders = void 0;
const vscode = __importStar(require("vscode"));
const path = __importStar(require("path"));
function replaceWebviewPlaceholders(content, extension, webview) {
    const resourcesFolder = path.join(extension.extensionRoot, 'resources');
    const filePath = vscode.Uri.file(resourcesFolder);
    const link = webview.asWebviewUri(filePath).toString();
    return content.replace(/%VSCODE_RES%/g, link)
        .replace(/%VSCODE_CSP%/g, webview.cspSource);
}
exports.replaceWebviewPlaceholders = replaceWebviewPlaceholders;
//# sourceMappingURL=webview.js.map