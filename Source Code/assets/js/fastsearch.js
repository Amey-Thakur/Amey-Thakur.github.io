/* ==============================================================================
  - File: fastsearch.js (Search Interaction Engine)
  - Author: Amey Thakur
  - Profile: https://github.com/Amey-Thakur
  - Repository: https://github.com/Amey-Thakur/Amey-Thakur.github.io
  - Release Date: December 16, 2025
  - License: MIT License
  - ==============================================================================
  -
  - DESCRIPTION:
  - This script provides a high-performance, fuzzy-search functionality for 
  - Amey's Arc. It indexes site content client-side to enable near-instantaneous 
  - archival retrieval without requiring server-side processing.
  -
  - HOW IT WORKS:
  - The script asynchronously fetches the site's JSON search index and initializes 
  - the Fuse.js engine with optimized weighting for titles and content. It 
  - manages real-time DOM updates and provides advanced keyboard navigation 
  - for an accessible, distraction-free search experience.
  -
  - TECH STACK:
  - - Fuse.js (Fuzzy Search Engine)
  - - Vanilla JavaScript (Asynchronous Operations)
  - - JSON Data Architecture
  -
  - ============================================================================== */

import * as params from '@params';

// Global state management for the search engine and results navigation.
let fuse;
let resList = document.getElementById('searchResults');
let sInput = document.getElementById('searchInput');
let first, last, current_elem = null;
let resultsAvailable = false;

/**
 * Architectural Initialization: Asynchronous retrieval and indexing of the search manifest.
 * Triggered upon document completion to ensure DOM readiness.
 */
window.onload = function () {
    let xhr = new XMLHttpRequest();
    xhr.onreadystatechange = function () {
        if (xhr.readyState === 4) {
            if (xhr.status === 200) {
                let data = JSON.parse(xhr.responseText);
                if (data) {
                    // Configuration of the fuzzy matching algorithm.
                    let options = {
                        distance: 100,
                        threshold: 0.4,
                        ignoreLocation: true,
                        keys: ['title', 'permalink', 'summary', 'content']
                    };

                    // Injection of custom parameters from site configuration if present.
                    if (params.fuseOpts) {
                        options = {
                            isCaseSensitive: params.fuseOpts.iscasesensitive ?? false,
                            includeScore: params.fuseOpts.includescore ?? false,
                            includeMatches: params.fuseOpts.includematches ?? false,
                            minMatchCharLength: params.fuseOpts.minmatchcharlength ?? 1,
                            shouldSort: params.fuseOpts.shouldsort ?? true,
                            findAllMatches: params.fuseOpts.findallmatches ?? false,
                            keys: params.fuseOpts.keys ?? ['title', 'permalink', 'summary', 'content'],
                            location: params.fuseOpts.location ?? 0,
                            threshold: params.fuseOpts.threshold ?? 0.4,
                            distance: params.fuseOpts.distance ?? 100,
                            ignoreLocation: params.fuseOpts.ignorelocation ?? true
                        }
                    }
                    // Construct the search index from the retrieved JSON payload.
                    fuse = new Fuse(data, options);
                }
            } else {
                console.error("Search index retrieval failed:", xhr.responseText);
            }
        }
    };
    xhr.open('GET', "../index.json");
    xhr.send();
}

/**
 * Focus State Orchestrator: Manages the visual highlighting and keyboard capturing 
 * of active search results using class-based temporal states.
 * @param {HTMLElement} ae - The element to target for focus activation.
 */
function activeToggle(ae) {
    document.querySelectorAll('.focus').forEach(function (element) {
        element.classList.remove("focus");
    });
    if (ae) {
        ae.focus();
        document.activeElement = current_elem = ae;
        ae.parentElement.classList.add("focus");
    } else {
        document.activeElement.parentElement.classList.add("focus");
    }
}

/**
 * Restores the search interface to its baseline state.
 */
function reset() {
    resultsAvailable = false;
    resList.innerHTML = sInput.value = '';
    sInput.focus();
}

/**
 * Query Execution Cycle: Executes the fuzzy-matching algorithm upon keyboard input 
 * and triggers the programmatic reconstruction of the results list in the DOM.
 */
sInput.onkeyup = function (e) {
    if (fuse) {
        let results;
        if (params.fuseOpts) {
            results = fuse.search(this.value.trim(), { limit: params.fuseOpts.limit });
        } else {
            results = fuse.search(this.value.trim());
        }

        if (results.length !== 0) {
            // Programmatic construction of the results list in the DOM.
            let resultSet = '';

            for (let item in results) {
                resultSet += `<li class="post-entry"><header class="entry-header">${results[item].item.title}&nbsp;»</header>` +
                    `<a href="${results[item].item.permalink}" aria-label="${results[item].item.title}"></a></li>`
            }

            resList.innerHTML = resultSet;
            resultsAvailable = true;
            first = resList.firstChild;
            last = resList.lastChild;
        } else {
            resultsAvailable = false;
            resList.innerHTML = '';
        }
    }
}

sInput.addEventListener('search', function (e) {
    // Intercept clear interaction (clicking 'x' in input).
    if (!this.value) reset();
});

/**
 * Accessibility Controller: Manages complex keyboard navigation bindings (Arrow keys, Escape) 
 * to provide a high-fidelity, frictionless traversal experience.
 */
document.onkeydown = function (e) {
    let key = e.key;
    let ae = document.activeElement;
    let inbox = document.getElementById("searchbox").contains(ae);

    if (ae === sInput) {
        let elements = document.getElementsByClassName('focus');
        while (elements.length > 0) {
            elements[0].classList.remove('focus');
        }
    } else if (current_elem) {
        ae = current_elem;
    }

    if (key === "Escape") {
        reset();
    } else if (!resultsAvailable || !inbox) {
        return;
    } else if (key === "ArrowDown") {
        e.preventDefault();
        if (ae == sInput) {
            // Traversal from input field to the primary search result.
            activeToggle(resList.firstChild.lastChild);
        } else if (ae.parentElement != last) {
            // Sequential navigation to the subsequent result.
            activeToggle(ae.parentElement.nextSibling.lastChild);
        }
    } else if (key === "ArrowUp") {
        e.preventDefault();
        if (ae.parentElement == first) {
            // Reversion from initial result back to search input.
            activeToggle(sInput);
        } else if (ae != sInput) {
            // Sequential navigation to the preceding result.
            activeToggle(ae.parentElement.previousSibling.lastChild);
        }
    } else if (key === "ArrowRight") {
        // Selection activation via directional keyboard command.
        ae.click();
    }
}