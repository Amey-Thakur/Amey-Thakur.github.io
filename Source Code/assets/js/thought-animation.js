/* ==============================================================================
 * File: thought-animation.js
  * Profile: https://github.com/Amey-Thakur
 * Repository: https://github.com/Amey-Thakur/Amey-Thakur.github.io
 * Release Date: December 16, 2025
 * License: MIT License
 * ==============================================================================
 *
 * DESCRIPTION:
 * This script orchestrates the signature "thought balloon" interaction for 
 * Amey's Arc. It manages spatial particle systems, auditory synthesis, and 
 * state-driven UI transitions that symbolize the archival of ideas.
 *
 * HOW IT WORKS:
 * Upon interaction with a trigger element, the script enters a "distraction-free" 
 * state, executes a multi-stage coordinate translation for animated particles, 
 * and synthesizes real-time audio chimes using the Web Audio API. Each 
 * particle represents a discrete intellectual "spark" being archived.
 *
 * TECH STACK:
 * - Vanilla JavaScript (ES6+)
 * - Web Animations API (WAAPI)
 * - Web Audio API (Oscillator Synthesis)
 *
 * ============================================================================== */

document.addEventListener('DOMContentLoaded', () => {
    // Selection of primary interactive anchors.
    const thoughtBalloon = document.querySelector('.thought-balloon');
    const logoLink = document.querySelector('.logo a');

    // Structural guard to prevent execution on pages without these components.
    if (!thoughtBalloon || !logoLink) {
        return;
    }

    // Indicate interactivity via cursor mutation.
    thoughtBalloon.style.cursor = 'pointer';

    // Core Interaction: The Archival Sequence
    thoughtBalloon.addEventListener('click', (e) => {
        e.preventDefault();

        // Initiation of the distraction-free modal state to focus user attention.
        document.body.classList.add('distraction-free');

        // Capture spatial coordinates for trajectory calculation.
        const startRect = thoughtBalloon.getBoundingClientRect();
        const endRect = logoLink.getBoundingClientRect();

        const startX = startRect.left + startRect.width / 2;
        const startY = startRect.top + startRect.height / 2;

        const endX = endRect.left + endRect.width / 2;
        const endY = endRect.top + endRect.height / 2;

        // Configuration of the particle burst density.
        const particleCount = 12;

        // Incremental dispatch of particles to simulate a fluid, organic dispersion.
        for (let i = 0; i < particleCount; i++) {
            setTimeout(() => {
                createParticle(startX, startY, endX, endY);
            }, i * 200); // 200ms stagger for distinct rhythmic arrival.
        }

        // Deployment of decorative ambient elements within the visual field.
        createAmbientParticles();
    });

    /**
     * Spawns localized ambient particles to enrich the focal section's density.
     */
    function createAmbientParticles() {
        const infoSection = document.querySelector('.home-info');
        if (!infoSection) return;

        const rectification = infoSection.getBoundingClientRect();
        const count = 3 + Math.floor(Math.random() * 3);

        for (let i = 0; i < count; i++) {
            const bubble = document.createElement('div');
            bubble.classList.add('thought-particle');
            bubble.textContent = '💭';
            document.body.appendChild(bubble);

            // Randomization of spatial origin within host boundaries.
            const startX = rectification.left + Math.random() * rectification.width;
            const startY = rectification.top + Math.random() * rectification.height;

            // Definition of gentle upward drift vectors.
            const driftX = (Math.random() * 60 - 30);
            const driftY = -(40 + Math.random() * 60);

            const duration = 3000 + Math.random() * 2000;

            const anim = bubble.animate([
                {
                    transform: `translate(${startX}px, ${startY}px) scale(0)`,
                    opacity: 0,
                    offset: 0
                },
                {
                    transform: `translate(${startX}px, ${startY}px) scale(0.6)`,
                    opacity: 0.5,
                    offset: 0.2
                },
                {
                    transform: `translate(${startX + driftX}px, ${startY + driftY}px) scale(0.6) rotate(${Math.random() * 20 - 10}deg)`,
                    opacity: 0,
                    offset: 1
                }
            ], {
                duration: duration,
                easing: 'ease-out',
                fill: 'forwards'
            });

            anim.onfinish = () => bubble.remove();
        }

        // Restoration of standard UI state after interaction sequence completes.
        setTimeout(() => {
            document.body.classList.remove('distraction-free');
        }, 4500);
    }

    /**
     * Executes the lifecycle of a high-fidelity trajectory particle.
     * Includes: Initialization -> Burst -> Antigravity Drift -> Convergence -> Archive.
     */
    function createParticle(x, y, targetX, targetY) {
        const particle = document.createElement('div');
        particle.classList.add('thought-particle');
        particle.textContent = '💭';
        document.body.appendChild(particle);

        // Parametric definition of the initial "Pop" burst.
        const angle = Math.random() * Math.PI * 2;
        const popDistance = 60 + Math.random() * 40;
        const popX = Math.cos(angle) * popDistance;
        const popY = Math.sin(angle) * popDistance;

        // Definition of the secondary "Antigravity" drift phase.
        const floatX = popX + (Math.random() * 40 - 20);
        const floatY = popY - (30 + Math.random() * 50);

        const duration = 3500 + Math.random() * 1000;

        const animation = particle.animate([
            {
                transform: `translate(${x}px, ${y}px) scale(0) rotate(0deg)`,
                opacity: 0,
                offset: 0
            },
            {
                transform: `translate(${x + popX}px, ${y + popY}px) scale(1) rotate(${Math.random() * 20 - 10}deg)`,
                opacity: 1,
                offset: 0.15,
                easing: 'cubic-bezier(0.175, 0.885, 0.32, 1.275)'
            },
            {
                transform: `translate(${x + floatX}px, ${y + floatY}px) scale(1) rotate(${Math.random() * 40 - 20}deg)`,
                opacity: 0.9,
                offset: 0.6,
                easing: 'ease-in-out'
            },
            {
                transform: `translate(${targetX}px, ${targetY}px) scale(0.3) rotate(360deg)`,
                opacity: 0.6,
                offset: 0.9,
                easing: 'ease-in'
            },
            {
                transform: `translate(${targetX}px, ${targetY}px) scale(0)`,
                opacity: 0,
                offset: 1
            }
        ], {
            duration: duration,
            fill: 'forwards'
        });

        animation.onfinish = () => {
            particle.remove();
            createSparkle(targetX, targetY);
            triggerTextBloom(logoLink);
            playMagicalChime();
        };
    }

    /**
     * Visual confirmation of successful convergence.
     */
    function createSparkle(x, y) {
        const sparkle = document.createElement('div');
        sparkle.classList.add('archive-sparkle');
        sparkle.style.left = `${x}px`;
        sparkle.style.top = `${y}px`;
        document.body.appendChild(sparkle);

        const anim = sparkle.animate([
            { transform: 'translate(-50%, -50%) scale(0) rotate(0deg)', opacity: 1 },
            { transform: 'translate(-50%, -50%) scale(2) rotate(180deg)', opacity: 0 }
        ], {
            duration: 500,
            easing: 'ease-out'
        });

        anim.onfinish = () => sparkle.remove();
    }

    let bloomTimeout;
    /**
     * Orchestrates the typography-based "Bloom" effect upon successful archival.
     */
    function triggerTextBloom(element) {
        element.classList.remove('logo-bloom');
        void element.offsetWidth; // Enforcement of reflow for animation reset.
        element.classList.add('logo-bloom');

        clearTimeout(bloomTimeout);
        bloomTimeout = setTimeout(() => {
            element.classList.remove('logo-bloom');
        }, 300);
    }

    /**
     * Synthesizes transient audio frequencies to provide haptic-like feedback.
     * Utilizes a randomized pentatonic scale for a harmoniously archival sound.
     */
    function playMagicalChime() {
        try {
            const AudioContext = window.AudioContext || window.webkitAudioContext;
            if (!AudioContext) return;
            const ctx = new AudioContext();

            const osc = ctx.createOscillator();
            const gain = ctx.createGain();

            osc.connect(gain);
            gain.connect(ctx.destination);

            // Frequency selection from a predefined harmonious set.
            const baseFreqs = [880, 987, 1174, 1318, 1567]; // A5, B5, D6, E6, G6
            const freq = baseFreqs[Math.floor(Math.random() * baseFreqs.length)];

            osc.type = 'sine';
            const t = ctx.currentTime;

            osc.frequency.setValueAtTime(freq, t);

            // ADSR-like envelope optimized for transient "bell" characteristics.
            gain.gain.setValueAtTime(0, t);
            gain.gain.linearRampToValueAtTime(0.05, t + 0.01);
            gain.gain.exponentialRampToValueAtTime(0.001, t + 0.8);

            osc.start(t);
            osc.stop(t + 0.8);

        } catch (e) {
            // Silent catch to ensure visual experience continues if audio fails.
        }
    }
});