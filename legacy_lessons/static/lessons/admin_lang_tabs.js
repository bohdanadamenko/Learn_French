document.addEventListener('DOMContentLoaded', function() {
    // Prevent double injection
    if (document.querySelector('.admin-lang-tabs')) return;

    const fieldsets = document.querySelectorAll('fieldset');
    const resultList = document.getElementById('result_list');
    const langFieldsets = [];
    
    // Identify language fieldsets (for edit forms and stacked inlines)
    fieldsets.forEach(fs => {
        const h2 = fs.querySelector('h2');
        if (h2 && /\((RU|UA|EN|FR)\)/.test(h2.textContent)) {
            langFieldsets.push(fs);
        }
    });

    const isChangeList = !!resultList;
    const hasLangFieldsets = langFieldsets.length > 0;

    if (hasLangFieldsets || isChangeList) {
        // Use Jazzmin's Bootstrap 4 classes for native look
        // We don't need custom CSS anymore, Jazzmin handles .nav-tabs
        
        // Inject custom styles for "Pill" look as requested:
        // Active: Blue bg, White text
        // Inactive: Transparent bg, Blue text
        const style = document.createElement('style');
        style.textContent = `
            .admin-lang-tabs {
                gap: 5px;
            }
            .admin-lang-tabs .nav-link {
                border: 1px solid transparent;
                color: #007bff; /* Blue text */
                font-weight: 600;
                border-radius: 4px;
                padding: 8px 16px;
            }
            .admin-lang-tabs .nav-link:hover {
                background-color: rgba(0, 123, 255, 0.1);
                color: #0056b3;
            }
            .admin-lang-tabs .nav-link.active {
                background-color: #007bff !important; /* Blue fill */
                color: #ffffff !important; /* White text */
                box-shadow: 0 2px 4px rgba(0, 123, 255, 0.3);
            }
            /* Dark mode adjustments */
            @media (prefers-color-scheme: dark) {
                .admin-lang-tabs .nav-link {
                    color: #60a5fa;
                }
                .admin-lang-tabs .nav-link:hover {
                    background-color: rgba(96, 165, 250, 0.1);
                    color: #93c5fd;
                }
                .admin-lang-tabs .nav-link.active {
                    background-color: #3b82f6 !important;
                    color: #ffffff !important;
                }
            }
        `;
        document.head.appendChild(style);

        // Create tab container (Bootstrap ul.nav.nav-pills)
        const tabContainer = document.createElement('ul');
        tabContainer.className = 'nav nav-pills admin-lang-tabs';
        tabContainer.style.marginBottom = '20px'; // Slight spacing

        // Determine current language from HTML tag
        const currentLang = document.documentElement.lang.split('-')[0];
        
        const allLabelMap = {
            'ru': 'Все',
            'uk': 'Всі',
            'en': 'All',
            'fr': 'Tout'
        };
        const allLabel = allLabelMap[currentLang] || 'All';

        const langs = [
            { id: 'all', label: allLabel, pattern: '', suffix: '' },
            { id: 'ru', label: 'RU', pattern: '(RU)', suffix: '_ru' },
            { id: 'ua', label: 'UA', pattern: '(UA)', suffix: '_ua' },
            { id: 'en', label: 'EN', pattern: '(EN)', suffix: '_en' },
            { id: 'fr', label: 'FR', pattern: '(FR)', suffix: '_fr' }
        ];

        langs.forEach(lang => {
            const li = document.createElement('li');
            li.className = 'nav-item';

            const btn = document.createElement('a');
            btn.href = '#';
            btn.className = 'nav-link admin-lang-btn';
            btn.textContent = lang.label;
            
            // Prevent default link behavior
            btn.addEventListener('click', (e) => {
                e.preventDefault();
                
                // Save selection
                localStorage.setItem('admin_lang_pref', lang.id);

                // Update active state
                tabContainer.querySelectorAll('.nav-link').forEach(b => b.classList.remove('active'));
                btn.classList.add('active');

                // 1. Handle Fieldsets (Edit Forms & Stacked Inlines)
                langFieldsets.forEach(fs => {
                    const h2 = fs.querySelector('h2');
                    if (lang.id === 'all' || h2.textContent.includes(lang.pattern)) {
                        fs.style.display = '';
                        if (lang.id !== 'all') fs.classList.remove('collapsed');
                    } else {
                        fs.style.display = 'none';
                    }
                });

                // 2. Handle Tables (ChangeList & TabularInlines)
                // 3. Handle ChangeList (List View)
                // Jazzmin might use #result_list or just a table class
                const mainTable = document.getElementById('result_list') || document.querySelector('#content-main table.table');
                
                if (mainTable) {
                    const headers = mainTable.querySelectorAll('thead th');
                    const rows = mainTable.querySelectorAll('tbody tr');

                    headers.forEach((th, index) => {
                        // Robust detection: Check text content for language patterns (RU), (UA), etc.
                        const text = th.textContent.trim();
                        const langMatch = text.match(/\((RU|UA|EN|FR)\)/);
                        
                        if (langMatch) {
                            // Found a language column!
                            const columnLang = langMatch[1]; // "RU", "UA", "EN", "FR"
                            
                            // Determine if this column matches the selected language
                            // If 'all', show everything.
                            // If 'ru', show columns containing (RU).
                            const isMatch = lang.id === 'all' || columnLang === lang.label; // lang.label is "RU", "UA"...
                            
                            th.style.display = isMatch ? '' : 'none';
                            rows.forEach(row => {
                                const cell = row.cells[index];
                                if (cell) cell.style.display = isMatch ? '' : 'none';
                            });
                        }
                    });
                }

                    // 4. Handle Filters (Sidebar)
                    // Jazzmin uses a different structure: #changelist-filter is inside a card
                    const filterSidebar = document.getElementById('changelist-filter');
                    const translationsData = document.getElementById('lesson-translations-data');
                    
                    if (filterSidebar && translationsData) {
                        try {
                            const translations = JSON.parse(translationsData.textContent);
                            
                            // Localize filter headers
                            // Jazzmin: h5.card-title or similar, standard: h3
                            const filterTitles = filterSidebar.querySelectorAll('h3, h5, .card-title');
                            const headerTranslations = {
                                'ru': 'Урок',
                                'ua': 'Урок',
                                'en': 'Lesson',
                                'fr': 'Leçon'
                            };
                            filterTitles.forEach(title => {
                                const text = title.textContent.toLowerCase();
                                if (text.includes('lesson') || text.includes('урок') || text.includes('leçon') || text.includes('lecon')) {
                                    title.textContent = (lang.id === 'all') ? headerTranslations['ru'] : (headerTranslations[lang.id] || headerTranslations['ru']);
                                }
                            });

                            // Localize filter links
                            // Jazzmin: .list-group-item, standard: ul li a
                            const filterLinks = filterSidebar.querySelectorAll('ul li a, .list-group-item');
                            filterLinks.forEach(link => {
                                const href = link.getAttribute('href');
                                if (!href) return;

                                // Robustly extract lesson ID from URL parameters
                                const match = href.match(/[?&]lesson(?:__id__exact)?=([^&]+)/);
                                const lessonId = match ? decodeURIComponent(match[1]) : null;
                                
                                if (lessonId && translations[lessonId]) {
                                    const trans = translations[lessonId];
                                    let newText = (lang.id === 'all') ? trans['ru'] : (trans[lang.id] || trans['ru']);
                                    
                                    // Preserve count if it exists (e.g. "Lesson 1 (5)" or badge in Jazzmin)
                                    // Jazzmin often puts count in a span.badge
                                    const badge = link.querySelector('.badge');
                                    if (badge) {
                                        // If badge exists, we only replace the text node
                                        const textNode = Array.from(link.childNodes).find(node => node.nodeType === 3 && node.textContent.trim().length > 0);
                                        if (textNode) {
                                            textNode.textContent = newText + ' ';
                                        }
                                    } else {
                                        // Standard Django admin behavior
                                        const currentText = link.textContent.trim();
                                        const countMatch = currentText.match(/ \(\d+\)$/);
                                        if (countMatch) {
                                            newText += countMatch[0];
                                        }
                                        if (link.textContent.trim() !== newText) {
                                            link.textContent = newText;
                                        }
                                    }
                                }
                            });
                        } catch (e) {
                            console.error('Error localizing admin filters:', e);
                        }
                    }
                const tables = document.querySelectorAll('.tabular.inline-related table'); // Only target tabular inlines now
                tables.forEach(table => {
                    const headers = table.querySelectorAll('thead th');
                    const langSuffixes = ['_ru', '_ua', '_en', '_fr'];

                    headers.forEach((th, index) => {
                        const classes = Array.from(th.classList);
                        // Find if this column is a language field
                        const fieldClass = classes.find(c => langSuffixes.some(s => c.endsWith(s) || c.includes(s + ' ')));
                        
                        if (fieldClass) {
                            const isMatch = lang.id === 'all' || fieldClass.endsWith(lang.suffix) || fieldClass.includes(lang.suffix + ' ');
                            th.style.display = isMatch ? '' : 'none';
                            
                            // Hide cells in this column
                            const rows = table.querySelectorAll('tbody tr');
                            rows.forEach(row => {
                                const cell = row.cells[index];
                                if (cell) cell.style.display = isMatch ? '' : 'none';
                            });
                        }
                    });
                });
            });

            li.appendChild(btn);
            tabContainer.appendChild(li);
        });

        // Insert tabs at the top of the content area
        const target = document.getElementById('changelist') || document.querySelector('#content-main form');
        if (target) {
            if (target.id === 'changelist') {
                target.parentNode.insertBefore(tabContainer, target);
            } else {
                target.prepend(tabContainer);
            }
        }

        // Restore selection or default to RU
        const savedLang = localStorage.getItem('admin_lang_pref');
        let btnToClick = tabContainer.querySelectorAll('.admin-lang-btn')[1]; // Default RU

        if (savedLang) {
            const savedBtn = Array.from(tabContainer.querySelectorAll('.admin-lang-btn')).find(b => 
                langs.find(l => l.id === savedLang && b.textContent === l.label)
            );
            if (savedBtn) btnToClick = savedBtn;
        }
        
        if (btnToClick) btnToClick.click();
    }
});
