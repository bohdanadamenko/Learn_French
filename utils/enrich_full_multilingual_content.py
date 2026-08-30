"""
Script to fully populate and synchronize EN (English) and FR (Français) content
across all lessons that had brief stubs, ensuring 100% complete 4-language support.
"""
import os
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'learn_french.settings')
django.setup()

from apps.lessons.models import Lesson

def enrich_multilingual():
    # 1. Lesson 4: Gender & Plural
    l4 = Lesson.objects.filter(data_lesson_id="lesson4").first()
    if l4:
        l4.content_html_en = """
        <h2>How Masculine, Feminine, and Plural are Formed in French</h2>
        <p>In French, <strong>there is no neuter gender</strong> — all nouns and adjectives are either <strong>Masculine</strong> or <strong>Feminine</strong>.</p>
        
        <h3>1. ♀️ Forming the Feminine:</h3>
        <div class="callout-box callout-rule">
            <div class="callout-title">📐 General Rule: Add « -e » at the end</div>
            <div class="callout-content">
                <p>When adding <strong>-e</strong>, the previously silent final consonant becomes pronounced:</p>
                <ul>
                    <li><em>Un étudiant</em> ➔ <em>Une étudiante</em> (Student)</li>
                    <li><em>Un ami</em> ➔ <em>Une amie</em> (Friend)</li>
                    <li><em>Français</em> ➔ <em>Française</em> (French)</li>
                </ul>
            </div>
        </div>
        
        <h4>Key Suffix Changes:</h4>
        <div class="conjugation-grid" style="grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 14px;">
            <div><strong>-ER ➔ -ÈRE</strong><br><em>Un boulanger ➔ Une boulangère</em></div>
            <div><strong>-IEN ➔ -IENNE</strong><br><em>Un musicien ➔ Une musicienne</em></div>
            <div><strong>-EUR ➔ -EUSE</strong><br><em>Un serveur ➔ Une serveuse</em></div>
            <div><strong>-TEUR ➔ -TRICE</strong><br><em>Un directeur ➔ Une directrice</em></div>
        </div>

        <h3>2. 👥 Forming the Plural:</h3>
        <div class="callout-box callout-rule">
            <div class="callout-title">📐 General Rule: Add « -s » at the end (silent)</div>
            <div class="callout-content">
                <ul>
                    <li><em>Un croissant</em> ➔ <strong>Des croissants</strong></li>
                    <li><em>Une table</em> ➔ <strong>Des tables</strong></li>
                </ul>
            </div>
        </div>

        <h3>🃏 Practice Cards</h3>
        <div class="flip-grid">
            <div class="flip-card">
                <div class="flip-card-inner">
                    <div class="flip-card-front">
                        <strong style="font-size:1.25rem; color:var(--accent-blue);">Female Student</strong>
                        <span class="flip-hint">Click to flip</span>
                    </div>
                    <div class="flip-card-back">
                        <strong style="font-size:1.05rem;">Une étudiante</strong>
                    </div>
                </div>
            </div>
            <div class="flip-card">
                <div class="flip-card-inner">
                    <div class="flip-card-front">
                        <strong style="font-size:1.25rem; color:var(--accent-purple);">Newspapers (Plural)</strong>
                        <span class="flip-hint">Click to flip</span>
                    </div>
                    <div class="flip-card-back">
                        <strong style="font-size:1.05rem;">Des journaux</strong>
                    </div>
                </div>
            </div>
        </div>
        """
        l4.content_html_fr = """
        <h2>Le masculin, le féminin et le pluriel en français</h2>
        <p>En français, tous les noms et adjectifs ont un genre : <strong>masculin</strong> ou <strong>féminin</strong>.</p>
        
        <h3>1. ♀️ La formation du féminin :</h3>
        <div class="callout-box callout-rule">
            <div class="callout-title">📐 Règle générale : On ajoute un « -e »</div>
            <div class="callout-content">
                <ul>
                    <li><em>Un étudiant ➔ Une étudiante</em></li>
                    <li><em>Un ami ➔ Une amie</em></li>
                </ul>
            </div>
        </div>

        <h3>2. 👥 La formation du pluriel :</h3>
        <div class="callout-box callout-rule">
            <div class="callout-title">📐 Règle générale : On ajoute un « -s »</div>
            <div class="callout-content">
                <ul>
                    <li><em>Un livre ➔ Des livres</em></li>
                    <li><em>Un journal ➔ Des journaux</em></li>
                </ul>
            </div>
        </div>

        <h3>🃏 Cartes mémoire</h3>
        <div class="flip-grid">
            <div class="flip-card">
                <div class="flip-card-inner">
                    <div class="flip-card-front">
                        <strong style="font-size:1.25rem; color:var(--accent-blue);">Une étudiante</strong>
                        <span class="flip-hint">Cliquez pour retourner</span>
                    </div>
                    <div class="flip-card-back">
                        <strong style="font-size:1.05rem;">Féminin de étudiant</strong>
                    </div>
                </div>
            </div>
        </div>
        """
        l4.save()

    # 2. Lesson Partitive
    lp = Lesson.objects.filter(data_lesson_id="lesson-partitive").first()
    if lp:
        lp.content_html_en = """
        <h2>Partitive Articles: DU, DE LA, DE L', DES</h2>
        <p>Used to express an <strong>unspecified quantity</strong> of uncountable items (food, drinks, money, time).</p>
        <div class="conjugation-grid" style="grid-template-columns: repeat(auto-fit, minmax(180px, 1fr)); gap: 12px;">
            <div><strong>DU</strong> (Masculine)<br><em>Du pain, du fromage, du café</em></div>
            <div><strong>DE LA</strong> (Feminine)<br><em>De la bière, de la viande</em></div>
            <div><strong>DE L'</strong> (Vowel / silent H)<br><em>De l'eau, de l'argent</em></div>
            <div><strong>DES</strong> (Plural)<br><em>Des frites, des pâtes</em></div>
        </div>
        <div class="callout-box callout-warning">
            <div class="callout-title">⚠️ In negation, partitive articles become DE / D'</div>
            <div class="callout-content">
                <p><em>Je bois <strong>du</strong> café</em> ➔ <em>Je ne bois pas <strong>de</strong> café</em>.</p>
            </div>
        </div>
        <h3>🃏 Practice Cards</h3>
        <div class="flip-grid">
            <div class="flip-card">
                <div class="flip-card-inner">
                    <div class="flip-card-front">
                        <strong style="font-size:1.25rem; color:var(--accent-blue);">I drink water</strong>
                        <span class="flip-hint">Click to flip</span>
                    </div>
                    <div class="flip-card-back">
                        <strong style="font-size:1.05rem;">Je bois de l'eau</strong>
                    </div>
                </div>
            </div>
        </div>
        """
        lp.content_html_fr = """
        <h2>Les articles partitifs : DU, DE LA, DE L', DES</h2>
        <p>Ils expriment une quantité indéterminée d'un ensemble non comptable.</p>
        <div class="conjugation-grid" style="grid-template-columns: repeat(auto-fit, minmax(180px, 1fr)); gap: 12px;">
            <div><strong>DU</strong> : <em>Du pain, du café</em></div>
            <div><strong>DE LA</strong> : <em>De la viande, de la salade</em></div>
            <div><strong>DE L'</strong> : <em>De l'eau, de l'argent</em></div>
            <div><strong>DES</strong> : <em>Des frites</em></div>
        </div>
        <h3>🃏 Cartes mémoire</h3>
        <div class="flip-grid">
            <div class="flip-card">
                <div class="flip-card-inner">
                    <div class="flip-card-front">
                        <strong style="font-size:1.25rem; color:var(--accent-blue);">De l'eau</strong>
                        <span class="flip-hint">Cliquez pour retourner</span>
                    </div>
                    <div class="flip-card-back">
                        <strong style="font-size:1.05rem;">Article partitif singulier</strong>
                    </div>
                </div>
            </div>
        </div>
        """
        lp.save()

    # 3. Lesson Passé Composé
    l_pc = Lesson.objects.filter(data_lesson_id="lesson-passe-compose").first()
    if l_pc:
        l_pc.content_html_en = """
        <h2>Past Tense: Passé Composé (Avoir & Être)</h2>
        <p>Used for completed past actions.</p>
        <p><strong>Formula:</strong> Avoir / Être in present + Past Participle (Participe passé).</p>
        <div class="callout-box callout-warning">
            <div class="callout-title">⚠️ Movement and reflexive verbs use ÊTRE:</div>
            <div class="callout-content">
                <p><em>Il est allé</em> vs <em>Elle est allée</em> (Agreement with subject).</p>
            </div>
        </div>
        <h3>🃏 Practice Cards</h3>
        <div class="flip-grid">
            <div class="flip-card">
                <div class="flip-card-inner">
                    <div class="flip-card-front">
                        <strong style="font-size:1.25rem; color:var(--accent-blue);">I finished the work</strong>
                        <span class="flip-hint">Click to flip</span>
                    </div>
                    <div class="flip-card-back">
                        <strong style="font-size:1.05rem;">J'ai fini le travail</strong>
                    </div>
                </div>
            </div>
        </div>
        """
        l_pc.content_html_fr = """
        <h2>Le Passé Composé avec Avoir et Être</h2>
        <p>Le passé composé exprime une action ponctuelle et achevée dans le passé.</p>
        <div class="callout-box callout-warning">
            <div class="callout-title">⚠️ Accord avec l'auxiliaire ÊTRE :</div>
            <div class="callout-content">
                <p><em>Elle est partie, ils sont arrivés.</em></p>
            </div>
        </div>
        <h3>🃏 Cartes mémoire</h3>
        <div class="flip-grid">
            <div class="flip-card">
                <div class="flip-card-inner">
                    <div class="flip-card-front">
                        <strong style="font-size:1.25rem; color:var(--accent-blue);">J'ai fini</strong>
                        <span class="flip-hint">Cliquez pour retourner</span>
                    </div>
                    <div class="flip-card-back">
                        <strong style="font-size:1.05rem;">Passé composé du verbe finir</strong>
                    </div>
                </div>
            </div>
        </div>
        """
        l_pc.save()

    # 4. Lesson Conditionnel
    l_cond = Lesson.objects.filter(data_lesson_id="lesson-conditionnel").first()
    if l_cond:
        l_cond.content_html_en = """
        <h2>Conditional Mood: Le Conditionnel Présent</h2>
        <p>The essential tool for polite requests, advice, and wishes.</p>
        <ul>
            <li><strong>Je voudrais...</strong> = I would like...</li>
            <li><strong>Pourriez-vous m'aider ?</strong> = Could you help me?</li>
            <li><strong>Vous devriez...</strong> = You should...</li>
        </ul>
        <h3>🃏 Practice Cards</h3>
        <div class="flip-grid">
            <div class="flip-card">
                <div class="flip-card-inner">
                    <div class="flip-card-front">
                        <strong style="font-size:1.25rem; color:var(--accent-blue);">I would like a coffee</strong>
                        <span class="flip-hint">Click to flip</span>
                    </div>
                    <div class="flip-card-back">
                        <strong style="font-size:1.05rem;">Je voudrais un café</strong>
                    </div>
                </div>
            </div>
        </div>
        """
        l_cond.content_html_fr = """
        <h2>Le Conditionnel Présent de politesse</h2>
        <p>Indispensable pour exprimer un souhait ou une demande polie.</p>
        <ul>
            <li><strong>Je voudrais un café, s'il vous plaît.</strong></li>
            <li><strong>Pourriez-vous m'indiquer le chemin ?</strong></li>
        </ul>
        <h3>🃏 Cartes mémoire</h3>
        <div class="flip-grid">
            <div class="flip-card">
                <div class="flip-card-inner">
                    <div class="flip-card-front">
                        <strong style="font-size:1.25rem; color:var(--accent-blue);">Je voudrais...</strong>
                        <span class="flip-hint">Cliquez pour retourner</span>
                    </div>
                    <div class="flip-card-back">
                        <strong style="font-size:1.05rem;">Formule de politesse</strong>
                    </div>
                </div>
            </div>
        </div>
        """
        l_cond.save()

    # 5. Lesson Banking BE
    l_bank = Lesson.objects.filter(data_lesson_id="lesson-banking-be").first()
    if l_bank:
        l_bank.content_html_en = """
        <h2>Banking in Belgium: Accounts, Bancontact & Payconiq</h2>
        <p>In Belgium, cashless payments are standard across all services.</p>
        <ul>
            <li><strong>Un compte à vue</strong> = Current checking account.</li>
            <li><strong>Un compte d'épargne</strong> = Savings account.</li>
            <li><strong>Bancontact & Payconiq</strong> = National debit card and QR-code mobile payment system.</li>
        </ul>
        <h3>🃏 Practice Cards</h3>
        <div class="flip-grid">
            <div class="flip-card">
                <div class="flip-card-inner">
                    <div class="flip-card-front">
                        <strong style="font-size:1.25rem; color:var(--accent-blue);">I'd like to open an account</strong>
                        <span class="flip-hint">Click to flip</span>
                    </div>
                    <div class="flip-card-back">
                        <strong style="font-size:1.05rem;">Je voudrais ouvrir un compte à vue</strong>
                    </div>
                </div>
            </div>
        </div>
        """
        l_bank.content_html_fr = """
        <h2>Ouvrir un compte bancaire en Belgique</h2>
        <p>Le système bancaire et les paiements électroniques en Belgique.</p>
        <ul>
            <li><strong>Un compte à vue</strong> et <strong>un compte d'épargne</strong>.</li>
            <li><strong>Bancontact</strong> et <strong>Payconiq</strong> pour les paiements quotidiens.</li>
        </ul>
        <h3>🃏 Cartes mémoire</h3>
        <div class="flip-grid">
            <div class="flip-card">
                <div class="flip-card-inner">
                    <div class="flip-card-front">
                        <strong style="font-size:1.25rem; color:var(--accent-blue);">Un compte à vue</strong>
                        <span class="flip-hint">Cliquez pour retourner</span>
                    </div>
                    <div class="flip-card-back">
                        <strong style="font-size:1.05rem;">Compte courant</strong>
                    </div>
                </div>
            </div>
        </div>
        """
        l_bank.save()

    print("All multilingual lessons successfully populated with comprehensive EN and FR contents!")

if __name__ == '__main__':
    enrich_multilingual()
