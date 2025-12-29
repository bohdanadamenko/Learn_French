/* =========================================
   UNIFIED SCRIPT - Theme System + All Features
   ========================================= */

// Global variable for next lesson ID
let pendingNextLessonId = null;

// ========================================
// THEME SYSTEM
// ========================================

function toggleTheme() {
    const body = document.body;
    const themeToggle = document.getElementById('themeToggle');
    const isDark = body.getAttribute('data-theme') === 'dark';
    
    if (isDark) {
        body.setAttribute('data-theme', 'light');
        if (themeToggle) themeToggle.checked = false;
        localStorage.setItem('preferredTheme', 'light');
    } else {
        body.setAttribute('data-theme', 'dark');
        if (themeToggle) themeToggle.checked = true;
        localStorage.setItem('preferredTheme', 'dark');
    }
}

function applyStoredTheme() {
    const savedTheme = localStorage.getItem('preferredTheme') || 'light';
    document.body.setAttribute('data-theme', savedTheme);
    
    const themeToggle = document.getElementById('themeToggle');
    if (themeToggle) {
        themeToggle.checked = savedTheme === 'dark';
    }
}

function applyStoredLang() {
    const savedLang = localStorage.getItem('preferredLang') || 'ru';
    document.body.setAttribute('data-lang', savedLang);
    
    document.querySelectorAll('.option-btn[data-lang]').forEach(btn => {
        btn.classList.toggle('active', btn.dataset.lang === savedLang);
    });
    
    updateSearchPlaceholders(savedLang);
}

function updateSearchPlaceholders(lang) {
    const placeholders = {
        'ru': 'Поиск...',
        'ua': 'Пошук...',
        'en': 'Search...',
        'fr': 'Rechercher...'
    };
    
    const text = placeholders[lang] || placeholders['ru'];
    document.querySelectorAll('.search-input').forEach(input => {
        input.placeholder = text;
    });
}

// ========================================
// INITIALIZATION
// ========================================

document.addEventListener('DOMContentLoaded', () => {
    // Apply saved theme and language FIRST
    applyStoredTheme();
    applyStoredLang();
    
    // 1. Wrap videos
    document.querySelectorAll('.video-container').forEach(div => {
        if (!div.closest('.video-wrapper')) {
            const wrapper = document.createElement('div');
            wrapper.className = 'video-wrapper';
            div.parentNode.insertBefore(wrapper, div);
            wrapper.appendChild(div);
        }
    });
    
    // 2. Style conjugation grids
    document.querySelectorAll('.conjugation-grid > div').forEach(div => {
        div.classList.add('conjugation-item');
    });
    
    // 3. Setup event listeners
    document.getElementById('sidebarOverlay')?.addEventListener('click', closeSidebar);
    
    // Search handlers
    document.querySelectorAll('.search-input').forEach(input => {
        input.addEventListener('input', (e) => handleSearch(e.target.value.trim()));
    });
    
    // 4. Progress tracking
    loadProgress();
    document.querySelectorAll('.progress-indicator').forEach(indicator => {
        indicator.addEventListener('click', (e) => {
            e.stopPropagation();
            toggleProgress(indicator.closest('.nav-item'));
        });
    });
    
    // 5. Keyboard shortcuts
    document.addEventListener('keydown', handleKeydown);
    
    // 6. Handle window resize
    window.addEventListener('resize', () => {
        if (window.innerWidth > 900) {
            closeSidebar();
        }
    });

    // 7. Load last viewed lesson
    loadLastLesson();

    // 8. Update Nav Buttons
    updateNavButtonsState();
    
    // 9. Theme switcher listener
    const themeToggle = document.getElementById('themeToggle');
    if (themeToggle) {
        themeToggle.addEventListener('change', () => {
            toggleTheme();
        });
    }
    
    // 10. Language selection
    document.querySelectorAll('.option-btn[data-lang]').forEach(btn => {
        btn.addEventListener('click', () => {
            const lang = btn.dataset.lang;
            document.body.setAttribute('data-lang', lang);
            
            btn.parentElement.querySelectorAll('.option-btn').forEach(b => b.classList.remove('active'));
            btn.classList.add('active');
            localStorage.setItem('preferredLang', lang);
            
            updateSearchPlaceholders(lang);
        });
    });
});

// ========================================
// NAVIGATION & MOBILE MENU
// ========================================

function switchLesson(lessonId, element) {
    // 1. Update Navigation Active State
    document.querySelectorAll('.nav-item').forEach(el => el.classList.remove('active'));
    
    let navItem = element;
    if (!navItem) {
        navItem = document.querySelector(`.nav-item[data-lesson-id="${lessonId}"]`);
    }

    if (navItem) {
        navItem.classList.add('active');
        navItem.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
    }

    // 2. Handle Content Transition
    document.querySelectorAll('.lesson-view').forEach(el => {
        el.classList.remove('active');
        el.style.display = ''; // Clear inline display
        el.style.opacity = '';
        el.style.transform = '';
    });
    
    const target = document.getElementById(lessonId);
    if (target) {
        // Reset quiz visibility if switching lessons
        const quizContainer = target.querySelector('.quiz-container');
        const lessonBody = target.querySelectorAll('.lesson-body');
        const lessonTitles = target.querySelectorAll('.lesson-title');
        const navButtons = target.querySelector('.lesson-footer-nav');
        const quizQuestions = target.querySelector('.quiz-questions');
        const quizResults = target.querySelector('.quiz-results');

        if (quizContainer) quizContainer.style.display = 'none';
        if (quizQuestions) quizQuestions.style.display = 'block';
        if (quizResults) quizResults.style.display = 'none';
        lessonBody.forEach(el => el.style.display = '');
        lessonTitles.forEach(el => el.style.display = '');
        if (navButtons) navButtons.style.display = '';

        // 1. Scroll to the very top of the page
        window.scrollTo({ top: 0, behavior: 'smooth' });

        // 2. Smooth reveal animation
        target.style.display = 'block';
        target.style.opacity = '0';
        target.style.transform = 'translateY(20px) scale(0.98)';

        setTimeout(() => {
            target.classList.add('active');
            target.style.opacity = ''; 
            target.style.transform = '';
        }, 50);
    }

    // 3. Stop all videos
    document.querySelectorAll('iframe').forEach(iframe => {
        const src = iframe.src;
        iframe.src = '';
        iframe.src = src;
    });

    // 4. Save current lesson
    saveLastLesson(lessonId);

    // 5. Close mobile sidebar
    closeSidebar();

    // 6. Update Buttons
    setTimeout(updateNavButtonsState, 50);
}

function toggleSidebar() {
    const sidebar = document.getElementById('sidebar');
    const overlay = document.getElementById('sidebarOverlay');
    const hamburger = document.getElementById('hamburger');
    
    const isOpening = !sidebar.classList.contains('active');
    
    sidebar.classList.toggle('active');
    overlay.classList.toggle('active');
    
    if (hamburger) {
        if (isOpening) {
            hamburger.classList.remove('is-closed');
            hamburger.classList.add('is-open');
            document.body.style.overflow = 'hidden';
        } else {
            hamburger.classList.remove('is-open');
            hamburger.classList.add('is-closed');
            document.body.style.overflow = '';
        }
    }
}

function closeSidebar() {
    const sidebar = document.getElementById('sidebar');
    const overlay = document.getElementById('sidebarOverlay');
    const hamburger = document.getElementById('hamburger');
    
    if (sidebar && sidebar.classList.contains('active')) {
        sidebar.classList.remove('active');
        overlay?.classList.remove('active');
        if (hamburger) {
            hamburger.classList.remove('is-open');
            hamburger.classList.add('is-closed');
        }
        document.body.style.overflow = '';
    }
}

// ========================================
// SEARCH FUNCTIONALITY
// ========================================

function escapeRegExp(string) {
    return string.replace(/[.*+?^${}()|[\]\\]/g, '\\$&');
}

function clearHighlights() {
    document.querySelectorAll('mark').forEach(mark => {
        mark.replaceWith(document.createTextNode(mark.textContent));
    });
    document.querySelector('.main-content')?.normalize();
}

function highlightText(root, regex) {
    if (!root) return;
    
    const walker = document.createTreeWalker(root, NodeFilter.SHOW_TEXT, null, false);
    const textNodes = [];
    
    while (walker.nextNode()) {
        textNodes.push(walker.currentNode);
    }

    textNodes.forEach(node => {
        if (!node.nodeValue.trim()) return;
        if (['MARK', 'SCRIPT', 'STYLE'].includes(node.parentNode.tagName)) return;

        const globalRegex = new RegExp(regex.source, regex.flags + 'g');
        
        if (globalRegex.test(node.nodeValue)) {
            globalRegex.lastIndex = 0;
            const fragment = document.createDocumentFragment();
            let lastIdx = 0;
            let match;
            
            while ((match = globalRegex.exec(node.nodeValue)) !== null) {
                const fullMatch = match[0];
                const prefix = match[1] || '';
                const target = match[2] || fullMatch;
                const matchIndex = match.index;

                fragment.appendChild(document.createTextNode(
                    node.nodeValue.substring(lastIdx, matchIndex)
                ));
                
                if (prefix) {
                    fragment.appendChild(document.createTextNode(prefix));
                }
                
                const mark = document.createElement('mark');
                mark.textContent = target;
                fragment.appendChild(mark);
                
                lastIdx = matchIndex + fullMatch.length;
            }
            
            fragment.appendChild(document.createTextNode(
                node.nodeValue.substring(lastIdx)
            ));
            
            node.parentNode.replaceChild(fragment, node);
        }
    });
}

function handleSearch(query) {
    clearHighlights();

    if (!query) {
        document.querySelectorAll('.nav-item').forEach(item => {
            item.style.display = 'flex';
        });
        updateNavButtonsState();
        return;
    }

    const escapedQuery = escapeRegExp(query);
    const searchRegex = new RegExp(
        '(^|[^a-zA-Z0-9\\u0400-\\u04FF_])(' + escapedQuery + ')',
        'i'
    );
    
    document.querySelectorAll('.nav-item').forEach(item => {
        const lessonId = item.getAttribute('data-lesson-id');
        const titleText = item.textContent;
        const contentEl = document.getElementById(lessonId);
        const contentText = contentEl ? contentEl.textContent : '';
        
        const matchTitle = searchRegex.test(titleText);
        const matchContent = searchRegex.test(contentText);

        if (matchTitle || matchContent) {
            item.style.display = 'flex';
            if (matchContent && contentEl) {
                highlightText(contentEl, searchRegex);
            }
        } else {
            item.style.display = 'none';
        }
    });
    updateNavButtonsState();
}

// ========================================
// PROGRESS TRACKING
// ========================================

function loadProgress() {
    const savedProgress = JSON.parse(localStorage.getItem('lessonProgress') || '{}');
    
    document.querySelectorAll('.nav-item').forEach(item => {
        const lessonId = item.getAttribute('data-lesson-id');
        const indicator = item.querySelector('.progress-indicator');
        
        if (savedProgress[lessonId]) {
            item.classList.add('completed');
            indicator?.setAttribute('aria-checked', 'true');
        }
    });
}

function toggleProgress(navItem) {
    const lessonId = navItem.getAttribute('data-lesson-id');
    const indicator = navItem.querySelector('.progress-indicator');
    
    navItem.classList.toggle('completed');
    const isCompleted = navItem.classList.contains('completed');
    indicator?.setAttribute('aria-checked', isCompleted ? 'true' : 'false');
    
    const currentProgress = JSON.parse(localStorage.getItem('lessonProgress') || '{}');
    
    if (isCompleted) {
        currentProgress[lessonId] = true;
    } else {
        delete currentProgress[lessonId];
    }
    
    localStorage.setItem('lessonProgress', JSON.stringify(currentProgress));
}

// ========================================
// KEYBOARD NAVIGATION
// ========================================

function navigateLesson(direction) {
    const activeItem = document.querySelector('.nav-item.active');
    if (!activeItem) return;

    let targetItem = direction === 'next' 
        ? activeItem.nextElementSibling 
        : activeItem.previousElementSibling;

    while (targetItem && targetItem.classList.contains('nav-item')) {
        if (targetItem.style.display !== 'none') {
            targetItem.click();
            targetItem.scrollIntoView({ behavior: 'smooth', block: 'center' });
            return;
        }
        targetItem = direction === 'next'
            ? targetItem.nextElementSibling
            : targetItem.previousElementSibling;
    }
}

function handleKeydown(e) {
    if (['INPUT', 'TEXTAREA'].includes(e.target.tagName)) {
        if (e.key === 'Escape') e.target.blur();
        return;
    }

    switch (e.key) {
        case '/':
            e.preventDefault();
            document.querySelector('.search-input')?.focus();
            break;
        case 'Escape':
            closeSidebar();
            break;
        case 'ArrowRight':
            navigateLesson('next');
            break;
        case 'ArrowLeft':
            navigateLesson('prev');
            break;
    }
}

// ========================================
// LAST VIEWED LESSON
// ========================================

function saveLastLesson(lessonId) {
    localStorage.setItem('lastViewedLesson', lessonId);
}

function loadLastLesson() {
    const lastLessonId = localStorage.getItem('lastViewedLesson');
    
    if (lastLessonId) {
        const lessonElement = document.querySelector(`[data-lesson-id="${lastLessonId}"]`);
        if (lessonElement) {
            switchLesson(lastLessonId, lessonElement);
            return;
        }
    }
    
    const firstLesson = document.querySelector('.nav-item');
    if (firstLesson) {
        const firstLessonId = firstLesson.getAttribute('data-lesson-id');
        switchLesson(firstLessonId, firstLesson);
    }
}

// ========================================
// NAV BUTTONS & MODAL
// ========================================

function getSiblingLessonId(offset) {
    const allItems = Array.from(document.querySelectorAll('.nav-item'));
    const visibleItems = allItems.filter(item => item.style.display !== 'none');
    
    const activeIndex = visibleItems.findIndex(item => item.classList.contains('active'));
    
    if (activeIndex === -1) return null;
    
    const targetIndex = activeIndex + offset;
    
    if (targetIndex >= 0 && targetIndex < visibleItems.length) {
        return visibleItems[targetIndex].getAttribute('data-lesson-id');
    }
    return null;
}

function updateNavButtonsState() {
    const currentLessonView = document.querySelector('.lesson-view.active');
    if (!currentLessonView) return;

    const prevBtn = currentLessonView.querySelector('.nav-btn.prev');
    const nextBtn = currentLessonView.querySelector('.nav-btn.next');

    const prevId = getSiblingLessonId(-1);
    const nextId = getSiblingLessonId(1);

    if (prevBtn) {
        if (prevId) {
            prevBtn.classList.remove('hidden');
            prevBtn.onclick = () => switchLesson(prevId);
        } else {
            prevBtn.classList.add('hidden');
        }
    }

    if (nextBtn) {
        if (nextId) {
            nextBtn.classList.remove('hidden');
        } else {
            nextBtn.classList.add('hidden');
        }
    }
}

function openNextModal() {
    const nextId = getSiblingLessonId(1);
    
    if (nextId) {
        pendingNextLessonId = nextId;
        const modal = document.getElementById('nextLessonModal');
        if (modal) {
            modal.style.display = 'flex';
            setTimeout(() => modal.classList.add('open'), 10);
        }
    }
}

function closeModal(event) {
    if (event && event.target.id !== 'nextLessonModal') return;
    
    const modal = document.getElementById('nextLessonModal');
    modal.classList.remove('open');
    setTimeout(() => modal.style.display = 'none', 300);
}

function confirmNextLesson() {
    const modal = document.getElementById('nextLessonModal');
    modal.classList.remove('open');
    setTimeout(() => modal.style.display = 'none', 300);

    if (pendingNextLessonId) {
        switchLesson(pendingNextLessonId);
    }
}

let quizState = {
    currentQuestion: 0,
    score: 0,
    totalQuestions: 0,
    activeLessonId: null
};

function startQuiz() {
    const currentLessonView = document.querySelector('.lesson-view.active');
    if (!currentLessonView) return;

    const lessonId = currentLessonView.id;
    const quizContainer = document.getElementById(`quiz-${lessonId}`);
    const lessonBody = currentLessonView.querySelectorAll('.lesson-body');
    const lessonTitles = currentLessonView.querySelectorAll('.lesson-title');
    const navButtons = currentLessonView.querySelector('.lesson-footer-nav');

    if (!quizContainer) return;

    // Close modal first
    const modal = document.getElementById('nextLessonModal');
    if (modal) {
        modal.classList.remove('open');
        setTimeout(() => modal.style.display = 'none', 300);
    }

    // Hide lesson content and nav
    lessonBody.forEach(el => el.style.display = 'none');
    lessonTitles.forEach(el => el.style.display = 'none');
    if (navButtons) navButtons.style.display = 'none';

    // Reset and show quiz
    quizState = {
        currentQuestion: 0,
        score: 0,
        totalQuestions: quizContainer.querySelectorAll('.quiz-question-card').length,
        activeLessonId: lessonId
    };

    // Initialize segments
    const segmentsContainer = quizContainer.querySelector('.quiz-progress-segments');
    if (segmentsContainer) {
        segmentsContainer.innerHTML = '';
        for (let i = 0; i < quizState.totalQuestions; i++) {
            const segment = document.createElement('div');
            segment.className = 'quiz-segment';
            segmentsContainer.appendChild(segment);
        }
    }

    quizContainer.style.display = 'block';
    updateQuizProgress();
    window.scrollTo({ top: 0, behavior: 'smooth' });
}

function checkAnswer(btn) {
    const isCorrect = btn.dataset.isCorrect === 'true';
    if (btn.parentNode.classList.contains('answered')) return;
    
    btn.parentNode.classList.add('answered');
    const allBtns = btn.parentNode.querySelectorAll('.quiz-choice-btn');
    const quizContainer = document.getElementById(`quiz-${quizState.activeLessonId}`);
    const segments = quizContainer?.querySelectorAll('.quiz-segment');
    const currentSegment = segments ? segments[quizState.currentQuestion] : null;
    
    if (isCorrect) {
        btn.classList.add('correct');
        quizState.score++;
        if (currentSegment) {
            currentSegment.classList.remove('active');
            currentSegment.classList.add('correct');
        }
    } else {
        btn.classList.add('incorrect');
        if (currentSegment) {
            currentSegment.classList.remove('active');
            currentSegment.classList.add('incorrect');
        }
        // Show correct answer
        allBtns.forEach(b => {
            if (b.dataset.isCorrect === 'true') b.classList.add('correct');
        });
    }

    // Disable all buttons in this card
    allBtns.forEach(b => b.disabled = true);

    // Move to next question after delay
    setTimeout(() => {
        const currentCard = btn.closest('.quiz-question-card');
        const nextCard = currentCard.nextElementSibling;

        if (nextCard && nextCard.classList.contains('quiz-question-card')) {
            currentCard.classList.remove('active');
            nextCard.classList.add('active');
            quizState.currentQuestion++;
            updateQuizProgress();
        } else {
            showQuizResults();
        }
    }, 1500);
}

function updateQuizProgress() {
    const quizContainer = document.getElementById(`quiz-${quizState.activeLessonId}`);
    if (!quizContainer) return;

    const counter = quizContainer.querySelector('.quiz-counter');
    const segments = quizContainer.querySelectorAll('.quiz-segment');
    
    // Update counter
    if (counter) {
        counter.textContent = `${quizState.currentQuestion + 1} / ${quizState.totalQuestions}`;
    }

    // Update segments active state
    segments.forEach((segment, idx) => {
        if (idx === quizState.currentQuestion) {
            segment.classList.add('active');
        } else if (idx > quizState.currentQuestion) {
            segment.classList.remove('active', 'correct', 'incorrect');
        }
    });
}

function showQuizResults() {
    const quizContainer = document.getElementById(`quiz-${quizState.activeLessonId}`);
    if (!quizContainer) return;

    const questionsContainer = quizContainer.querySelector('.quiz-questions');
    const resultsContainer = quizContainer.querySelector('.quiz-results');
    const scoreText = quizContainer.querySelector('.results-score');
    const progressBar = quizContainer.querySelector('.quiz-progress-bar');

    questionsContainer.style.display = 'none';
    resultsContainer.style.display = 'block';
    scoreText.textContent = `${quizState.score} / ${quizState.totalQuestions}`;
    progressBar.style.width = '100%';
}

// ========================================
// SETTINGS DROPDOWN
// ========================================

function toggleSettings() {
    const dropdown = document.getElementById('settingsDropdown');
    dropdown.classList.toggle('open');
}

document.addEventListener('click', (e) => {
    const wrapper = document.querySelector('.settings-wrapper');
    const dropdown = document.getElementById('settingsDropdown');
    
    if (wrapper && dropdown && !wrapper.contains(e.target)) {
        dropdown.classList.remove('open');
    }
});
