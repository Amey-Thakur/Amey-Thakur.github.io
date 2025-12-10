---
title: "Connect"
url: "/connect/"
summary: "Connect with me"
hideMeta: true
ShowBreadCrumbs: false
disableShare: true
---


<div class="contact-form-wrapper">
    <div class="contact-form" id="contact-form-container">
        <div class="form-header">
            <h3>I’m glad you’re here. Leave a note, I read every message.</h3>
        </div>
        <form id="contact-form" action="https://formspree.io/f/mrbnlrbn" method="POST">
            <div class="form-grid">
                <label>
                    <span>Hey! What should I call you?</span>
                    <input type="text" name="name" id="name" required placeholder="Your name">
                </label>
                <label>
                    <span>Where can I write back to you?</span>
                    <input type="email" name="email" required placeholder="Your email">
                </label>
            </div>
            <label>
                <span class="message-label-text">What’s on your mind?</span>
                <textarea name="message" required rows="5" placeholder="Your thoughts…"></textarea>
            </label>
            <div class="form-footer">
                <button type="submit" id="send-btn">Share ✦</button>
            </div>
        </form>
        <div id="form-status" class="form-status" style="display: none;"></div>
    </div>
</div>

<script>
    var form = document.getElementById("contact-form");

    function playSuccessSound() {
        try {
            const AudioContext = window.AudioContext || window.webkitAudioContext;
            if (!AudioContext) return;
            
            const ctx = new AudioContext();
            const osc = ctx.createOscillator();
            const gain = ctx.createGain();

            osc.connect(gain);
            gain.connect(ctx.destination);

            osc.type = 'sine';
            osc.frequency.setValueAtTime(523.25, ctx.currentTime); // C5
            osc.frequency.exponentialRampToValueAtTime(1046.5, ctx.currentTime + 0.1); // Swipe up to C6
            
            gain.gain.setValueAtTime(0.05, ctx.currentTime);
            gain.gain.exponentialRampToValueAtTime(0.001, ctx.currentTime + 0.5);

            osc.start();
            osc.stop(ctx.currentTime + 0.5);
        } catch (e) {
            console.error("Audio play failed", e);
        }
    }
    
    async function handleSubmit(event) {
        event.preventDefault();
        var status = document.getElementById("form-status");
        var btn = document.getElementById("send-btn");
        var data = new FormData(event.target);
        var name = data.get('name');
        var email = data.get('email');
        var message = data.get('message');

        // Simple Validation
        if (!name || !email || !message) {
            status.innerHTML = "Please fill in all mandatory fields.";
            status.style.display = "block";
            status.style.color = "red";
            return;
        }

        // Email Validation
        var emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
        if (!emailRegex.test(email)) {
            status.innerHTML = "Please enter a valid email address (e.g., name@example.com).";
            status.style.display = "block";
            status.style.color = "red";
            return; // Stop submission
        }

        // Disable button during submission
        btn.disabled = true;
        btn.innerHTML = "Sending...";
        status.style.display = "none"; // Clear previous errors

        fetch(event.target.action, {
            method: form.method,
            body: data,
            headers: {
                'Accept': 'application/json'
            }
        }).then(response => {
            if (response.ok) {
                // Play success sound
                playSuccessSound();

                // Hide form elements with fade out effect
                form.style.display = "none";
                document.querySelector('.form-header').style.display = 'none';
                
                status.style.display = "block";
                status.style.color = "var(--primary)";
                
                // Personalized Success Message
                status.innerHTML = `
                    <div class="success-message">
                        <p class="success-title">
                            Thank you, ${name}
                        </p>
                        <p class="success-body">
                           I appreciate you taking a moment to connect. <br> I’ll be in touch soon.
                        </p>
                    </div>`;
            } else {
                response.json().then(data => {
                    btn.disabled = false;
                    btn.innerHTML = "Send it ✦";
                    if (Object.hasOwn(data, 'errors')) {
                        status.innerHTML = data["errors"].map(error => error["message"]).join(", ")
                        status.style.display = "block"; 
                        status.style.color = "red";
                    } else {
                        status.innerHTML = "Oops! There was a problem submitting your form";
                        status.style.display = "block";
                        status.style.color = "red";
                    }
                })
            }
        }).catch(error => {
            btn.disabled = false;
            btn.innerHTML = "Send it ✦";
            status.innerHTML = "Oops! There was a problem submitting your form";
            status.style.display = "block";
            status.style.color = "red";
        });
    }
    form.addEventListener("submit", handleSubmit)
</script>

<style>
/* Container & Animation */
.contact-form-wrapper {
    animation: fadeInUp 0.8s ease-out;
}

@keyframes fadeInUp {
    from { opacity: 0; transform: translateY(20px); }
    to { opacity: 1; transform: translateY(0); }
}

.contact-form {
    background: var(--entry);
    padding: 40px;
    border-radius: 12px;
    border: 1px solid var(--border);
    margin-bottom: 40px;
    max-width: 700px;
    box-shadow: 0 4px 20px rgba(0,0,0,0.1);
}

/* Header */
.contact-form h3 {
    margin-top: 0;
    margin-bottom: 30px;
    font-size: 1.4rem;
}

.welcome-line {
    margin-bottom: 30px;
    opacity: 0.8;
    font-size: 1.05rem;
}

/* Form Layout */
.form-grid {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 20px;
}

@media (max-width: 600px) {
    .form-grid {
        grid-template-columns: 1fr;
    }
}

.contact-form label {
    display: block;
    margin-bottom: 25px;
}

.contact-form span {
    display: block;
    margin-bottom: 10px;
    font-weight: 500;
    font-size: 0.95rem;
    color: var(--primary);
}

/* Inputs & Textarea */
.contact-form input,
.contact-form textarea {
    width: 100%;
    padding: 15px;
    background: var(--code-bg);
    border: 1px solid var(--border);
    border-radius: 8px;
    color: var(--primary);
    font-family: inherit;
    font-size: 1rem;
    transition: all 0.3s ease;
}

.contact-form textarea {
    resize: vertical;
}

/* Focus Glow */
.contact-form input:focus,
.contact-form textarea:focus {
    outline: none;
    border-color: var(--secondary);
    box-shadow: 0 0 0 3px rgba(100, 100, 100, 0.1); /* Subtle glow */
    background: var(--entry);
}



/* Button */
.form-footer {
    display: flex;
    align-items: center;
    gap: 20px;
    margin-top: 10px;
}

.contact-form button {
    background: var(--primary);
    color: var(--theme);
    border: none;
    padding: 14px 30px;
    border-radius: 8px;
    font-size: 1rem;
    font-weight: bold;
    cursor: pointer;
    transition: transform 0.2s ease, opacity 0.2s;
    display: inline-block;
}

.contact-form button:hover {
    opacity: 0.9;
    transform: translateY(-2px);
}

.contact-form button:disabled {
    opacity: 0.6;
    cursor: not-allowed;
    transform: none;
}



/* Success Message */
.success-message {
    text-align: center;
    padding: 40px 0;
    color: var(--primary);
    animation: fadeIn 0.6s ease-in;
}

.checkmark {
    font-size: 1.5em;
    margin-left: 8px;
    vertical-align: middle;
}

.success-title {
    font-size: 1.5rem;
    font-weight: bold;
    margin-bottom: 15px;
}

.success-body {
    font-size: 1.1rem;
    line-height: 1.6;
    opacity: 0.9;
}

@keyframes fadeIn {
    from { opacity: 0; transform: translateY(10px); }
    to { opacity: 1; transform: translateY(0); }
}
</style>

<h2 style="margin-bottom: 0.5rem;">Find me across the spaces where I work, learn, and share.</h2>

{{< social_grid >}}
