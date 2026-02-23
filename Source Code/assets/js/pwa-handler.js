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

        // Deployment of the personalized installation notification.
        renderInstallSuggestion();
    });

    /**
     * renderInstallSuggestion: Orchestrates a premium UI notification 
     * at the document apex, encouraging device-level archival of AmeyArc.
     */
    function renderInstallSuggestion() {
        // Suppress if already dismissed or if the banner is already present.
        if (localStorage.getItem('pwa-banner-dismissed-v2') || document.getElementById('pwa-install-banner')) return;

        const banner = document.createElement('div');
        banner.id = 'pwa-install-banner';
        banner.style.cssText = `
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            background: var(--entry);
            border-bottom: 2px solid var(--primary);
            padding: 14px 24px;
            z-index: 10001;
            display: flex;
            align-items: center;
            justify-content: center;
            cursor: pointer;
            box-shadow: 0 4px 20px rgba(0,0,0,0.15);
            animation: slideDown 0.6s cubic-bezier(0.23, 1, 0.32, 1);
            transition: all 0.4s ease;
            backdrop-filter: blur(10px);
        `;

        banner.innerHTML = `
            <div style="display: flex; align-items: center; gap: 20px; max-width: 850px; width: 100%;">
                <span style="font-size: 2rem; filter: drop-shadow(0 2px 4px rgba(0,0,0,0.1));">💭</span>
                <div style="flex-grow: 1;">
                    <div style="font-size: 15px; color: var(--primary); font-weight: 600; line-height: 1.3;">Advancing ideas @ AmeyArc 🧠</div>
                    <div style="font-size: 12px; color: var(--secondary); margin-top: 4px; line-height: 1.5; opacity: 0.9;">
                        A living space for thoughts, sparks, and reflections in motion.<br>
                        Install to stay connected as ideas evolve and grow with you.
                    </div>
                </div>
                <button id="pwa-install-btn" style="background: var(--primary); color: var(--theme); border: none; padding: 8px 24px; border-radius: 20px; font-size: 13px; font-weight: 600; cursor: pointer; transition: transform 0.2s; white-space: nowrap;">Install</button>
            </div>
            <button id="pwa-dismiss" style="margin-left: 20px; background: none; border: none; color: var(--secondary); cursor: pointer; font-size: 24px; line-height: 1; opacity: 0.6;">&times;</button>
        `;

        const installBtn = banner.querySelector('#pwa-install-btn');
        const dismissBtn = banner.querySelector('#pwa-dismiss');

        banner.onclick = (e) => {
            if (e.target.id === 'pwa-dismiss' || e.target.parentElement.id === 'pwa-dismiss') {
                dismissBanner();
                return;
            }
            if (deferredPrompt) {
                deferredPrompt.prompt();
                deferredPrompt.userChoice.then(() => {
                    deferredPrompt = null;
                    dismissBanner();
                });
            }
        };

        function dismissBanner() {
            banner.style.transform = 'translateY(-100%)';
            banner.style.opacity = '0';
            setTimeout(() => banner.remove(), 400);
            localStorage.setItem('pwa-banner-dismissed-v2', 'true');
        }

        document.body.prepend(banner);

        // Inject animation keyframes
        if (!document.getElementById('pwa-styles')) {
            const style = document.createElement('style');
            style.id = 'pwa-styles';
            style.textContent = `
                @keyframes slideDown {
                    from { transform: translateY(-100%); opacity: 0; }
                    to { transform: translateY(0); opacity: 1; }
                }
                #pwa-install-btn:hover { transform: scale(1.05); }
                #pwa-dismiss:hover { color: var(--primary); }
            `;
            document.head.appendChild(style);
        }
    }
})();
