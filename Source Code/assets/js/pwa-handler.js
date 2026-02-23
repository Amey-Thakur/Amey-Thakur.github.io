/* ==============================================================================
  - File: pwa-handler.js (Progressive Web Application Orchestrator)
  - Author: Amey Thakur
  - Profile: https://github.com/Amey-Thakur
  - Repository: https://github.com/Amey-Thakur/Amey-Thakur.github.io
  - Release Date: December 16, 2025
  - License: MIT License
  - ==============================================================================
  -
  - DESCRIPTION:
  - This component manages the client-side lifecycle of the AmeyArc PWA. 
  - It handles service worker registration, installation event capturing, 
  - and non-intrusive UI suggestions for device-level integration.
  -
  - HOW IT WORKS:
  - The script validates browser capabilities before registering the site-wide 
  - service worker. It intercepts the native 'beforeinstallprompt' event to 
  - deliver a bespoke, high-fidelity installation banner that encourages users 
  - to add the archive to their home screen without disrupting the focal experience.
  -
  - TECH STACK:
  - - Service Worker API
  - - Web App Manifest Specification
  - - Client-side UI Orchestration (Vanilla JS)
  -
  - ============================================================================== */

(function () {
    /* Technical Guard: Validating browser capabilities for service worker support. */
    if ('serviceWorker' in navigator) {
        window.addEventListener('load', () => {
            navigator.serviceWorker.register('/sw.js').then((registration) => {
                // Registration successful: Site is now offline-capable.
            }).catch((err) => {
                console.warn('Service worker orchestration failed:', err);
            });
        });
    }

    let deferredPrompt;
    /* Installation Hook: Capturing the browser's native installation trigger. */
    window.addEventListener('beforeinstallprompt', (e) => {
        // Prevent default browser prompt sequence.
        e.preventDefault();
        deferredPrompt = e;

        // Deployment of the personalized installation suggestion at the top.
        renderInstallSuggestion();
    });

    /**
     * renderInstallSuggestion: Orchestrates a non-intrusive UI suggestion 
     * at the document apex, encouraging the archival of AmeyArc to the device.
     */
    function renderInstallSuggestion() {
        if (localStorage.getItem('pwa-suggestion-dismissed')) return;

        const banner = document.createElement('div');
        banner.id = 'pwa-install-banner';
        banner.style.cssText = `
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            background: var(--entry);
            border-bottom: 1px solid var(--border);
            padding: 10px 24px;
            z-index: 10001;
            display: flex;
            align-items: center;
            justify-content: center;
            cursor: pointer;
            box-shadow: 0 2px 8px rgba(0,0,0,0.1);
            animation: slideDown 0.5s cubic-bezier(0.4, 0, 0.2, 1);
            transition: opacity 0.3s ease;
        `;

        banner.innerHTML = `
            <div style="display: flex; align-items: center; gap: 12px;">
                <span style="font-size: 1.2rem;">💭</span>
                <span style="font-size: 13px; color: var(--primary); font-weight: 500;">
                    Install <strong>AmeyArc</strong> for a focused, offline-ready archival experience.
                </span>
            </div>
            <button id="pwa-dismiss" style="position: absolute; right: 24px; background: none; border: none; color: var(--secondary); cursor: pointer; font-size: 16px;">&times;</button>
        `;

        banner.onclick = (e) => {
            if (e.target.id === 'pwa-dismiss') {
                banner.style.opacity = '0';
                setTimeout(() => banner.remove(), 300);
                localStorage.setItem('pwa-suggestion-dismissed', 'true');
                return;
            }
            banner.remove();
            deferredPrompt.prompt();
            deferredPrompt.userChoice.then((choiceResult) => {
                deferredPrompt = null;
            });
        };

        document.body.prepend(banner);

        // Inject animation keyframes
        const style = document.createElement('style');
        style.textContent = `
            @keyframes slideDown {
                from { transform: translateY(-100%); }
                to { transform: translateY(0); }
            }
        `;
        document.head.appendChild(style);
    }
})();
