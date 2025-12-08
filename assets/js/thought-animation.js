
document.addEventListener('DOMContentLoaded', () => {
    const thoughtBalloon = document.querySelector('.thought-balloon');
    const logoLink = document.querySelector('.logo a');

    if (!thoughtBalloon || !logoLink) {
        return;
    }

    thoughtBalloon.style.cursor = 'pointer';

    thoughtBalloon.addEventListener('click', (e) => {
        e.preventDefault();

        // Enter Distraction-Free Mode
        document.body.classList.add('distraction-free');

        const startRect = thoughtBalloon.getBoundingClientRect();
        const endRect = logoLink.getBoundingClientRect();

        const startX = startRect.left + startRect.width / 2;
        const startY = startRect.top + startRect.height / 2;

        const endX = endRect.left + endRect.width / 2;
        const endY = endRect.top + endRect.height / 2;

        const particleCount = 12;

        // Remove the single sound timeout.
        // Sound is now triggered by individual particles finishing.

        for (let i = 0; i < particleCount; i++) {
            // Stagger creation much more slowly for "plop... plop" effect
            setTimeout(() => {
                createParticle(startX, startY, endX, endY);
            }, i * 200); // 200ms delay = distinct pops
        }

        // Trigger Ambient Balloons (Extra decoration)
        createAmbientParticles();
    });

    function createAmbientParticles() {
        const infoSection = document.querySelector('.home-info');
        if (!infoSection) return;

        const rectification = infoSection.getBoundingClientRect();
        // Spawn 3-5 random ambient bubbles
        const count = 3 + Math.floor(Math.random() * 3);

        for (let i = 0; i < count; i++) {
            const bubble = document.createElement('div');
            bubble.classList.add('thought-particle');
            bubble.textContent = '💭';
            document.body.appendChild(bubble);

            // Random position WITHIN the text area
            const startX = rectification.left + Math.random() * rectification.width;
            const startY = rectification.top + Math.random() * rectification.height;

            // Random gentle drift
            const driftX = (Math.random() * 60 - 30);
            const driftY = -(40 + Math.random() * 60); // Upward float

            const duration = 3000 + Math.random() * 2000;

            const anim = bubble.animate([
                {
                    top: 0, left: 0, // Reset for transform
                    transform: `translate(${startX}px, ${startY}px) scale(0)`,
                    opacity: 0,
                    offset: 0
                },
                {
                    transform: `translate(${startX}px, ${startY}px) scale(0.6)`, // Smaller size
                    opacity: 0.5, // Subtle opacity
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

        // Exit Distraction-Free Mode after slight delay
        setTimeout(() => {
            document.body.classList.remove('distraction-free');
        }, 4500); // Sync with particles fading
    }

    function createParticle(x, y, targetX, targetY) {
        const particle = document.createElement('div');
        particle.classList.add('thought-particle');
        particle.textContent = '💭';
        document.body.appendChild(particle);

        // Stage 1: The Pop (Initial Burst)
        const angle = Math.random() * Math.PI * 2;
        const popDistance = 60 + Math.random() * 40;
        const popX = Math.cos(angle) * popDistance;
        const popY = Math.sin(angle) * popDistance;

        // Stage 2: The Float (Antigravity Drift)
        const floatX = popX + (Math.random() * 40 - 20);
        const floatY = popY - (30 + Math.random() * 50);

        const duration = 3500 + Math.random() * 1000;

        const animation = particle.animate([
            // 0% - Start
            {
                transform: `translate(${x}px, ${y}px) scale(0) rotate(0deg)`,
                opacity: 0,
                offset: 0
            },
            // 15% - POP!
            {
                transform: `translate(${x + popX}px, ${y + popY}px) scale(1) rotate(${Math.random() * 20 - 10}deg)`,
                opacity: 1,
                offset: 0.15,
                easing: 'cubic-bezier(0.175, 0.885, 0.32, 1.275)'
            },
            // 60% - FLOAT
            {
                transform: `translate(${x + floatX}px, ${y + floatY}px) scale(1) rotate(${Math.random() * 40 - 20}deg)`,
                opacity: 0.9,
                offset: 0.6,
                easing: 'ease-in-out'
            },
            // 90% - CONVERGE
            {
                transform: `translate(${targetX}px, ${targetY}px) scale(0.3) rotate(360deg)`,
                opacity: 0.6,
                offset: 0.9,
                easing: 'ease-in'
            },
            // 100% - ARCHIVE
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
            triggerTextBloom(logoLink); // Trigger bloom for EACH particle
            playMagicalChime();        // Trigger chime for EACH particle
        };
    }

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
    function triggerTextBloom(element) {
        // Since this triggers rapidly, we remove the class immediately to allow re-trigger
        element.classList.remove('logo-bloom');
        // Force reflow
        void element.offsetWidth;
        element.classList.add('logo-bloom');

        clearTimeout(bloomTimeout);
        bloomTimeout = setTimeout(() => {
            element.classList.remove('logo-bloom');
        }, 300); // Shorter bloom to handle rapid fire
    }

    function playMagicalChime() {
        try {
            const AudioContext = window.AudioContext || window.webkitAudioContext;
            if (!AudioContext) return;
            const ctx = new AudioContext();

            const osc = ctx.createOscillator();
            const gain = ctx.createGain();

            osc.connect(gain);
            gain.connect(ctx.destination);

            // Magical Chime Synthesis
            // High pitch, sine wave, random variation for "sparkling" sound
            // Pentatonic-ish random notes: 880, 987, 1174, 1318, 1567 (A5, B5, D6, E6, G6)
            const baseFreqs = [880, 987, 1174, 1318, 1567];
            const freq = baseFreqs[Math.floor(Math.random() * baseFreqs.length)];

            osc.type = 'sine';
            const t = ctx.currentTime;

            osc.frequency.setValueAtTime(freq, t);

            // Envelope: Fast attack, slow smooth decay (Bell-like)
            gain.gain.setValueAtTime(0, t);
            gain.gain.linearRampToValueAtTime(0.05, t + 0.01); // Low volume to avoid ear-piercing
            gain.gain.exponentialRampToValueAtTime(0.001, t + 0.8);

            osc.start(t);
            osc.stop(t + 0.8);

        } catch (e) { }
    }
});
