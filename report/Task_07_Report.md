# Task 07 – Ethical Decision Making  
Author: Pavithra Ramasamy Pattuselvam  
Dataset: Syracuse Women’s Lacrosse – 2023 Season Stats

---

## 🎯 Purpose
Prepared for the Syracuse Women’s Lacrosse coaching staff / athletic director.  
Goal: turn my Task 5 LLM work into actionable recommendations with explicit ethics, reliability, and transparency.

---

## 📌 Executive Summary (≤300 words)
LLM answers on this dataset were mixed: good on simple facts, weaker on judgment calls.  
**Key actions**
- **Low risk:** Use LLM for exploratory Q&A; always validate with stats.
- **Medium risk:** Pilot LLM in assistant workflows; collect more context (injury, minutes, splits).
- **High risk:** Don’t use LLM alone for roster/recruitment/HR/legal decisions; human review required.

**Uncertainty**: Factual Qs ~70% accurate; prompt clarity and small data scope improved results.

---

## 🗂 Stakeholder & Decision Context
- **Stakeholders:** Head Coach, Athletic Director  
- **Decision:** Where to focus next season: offense, defense, or possession  
- **Risk level:** Medium (impacts game outcomes but coach-controlled)

---

## 🧾 Data & Methods
- **Source:** Official SU Women’s Lacrosse 2023 stats (PDF) → cleaned to CSV (1 row/player).  
- **Columns:** Player, GP, G, A, Pts, Sh, Gw, GB, DC, TO, CT.  
- **Validation:** Python/Excel to recompute leaders (see `code/validate_stats.py`).  
- **LLM testing:** Asked factual → intermediate → judgment questions; compared to validated answers.

---

## 💬 Prompts & Results (sample)
| Question | Correct (Dataset) | LLM | Correct? |
|---|---|---|---|
| Top scorer | Megan Carney – 59 | Meaghan Tyrrell | ❌ |
| Most assists | Emma Ward – 56 | Emma Ward | ✅ |
| Most points | Meaghan Tyrrell – 107 | Meaghan Tyrrell | ✅ |
| Most CT | Katie Goodale – 27 | Emma Tyrrell | ❌ |
| Possession (GB+DC) | Olivia Adamson – 114 | Olivia Adamson – 114 | ✅ |
| Shooting eff. | Katelyn Mashewsk – 1.00 | Katelyn Mashewsk – 1.00 | ✅ |

---

## 📊 Findings
- Great on straightforward facts; weaker when categories are similar (goals vs. points).
- Tendency to favor star offensive players on judgment calls.
- Prompt clarity (e.g., “compute GB+DC”) improved accuracy.
- Small, visible tables inside the chat helped the LLM answer correctly.

---

## ✅ Recommendations (Tiered)
**Operational (Low):**  
- Use LLM for brainstorming/explanations only; verify with validated stats.

**Investigatory (Medium):**  
- Pilot LLM in non-critical coaching workflows; add minutes, injury logs, time splits for context.

**High-stakes (High):**  
- Don’t rely on LLM alone for roster/recruitment/discipline; human/HR/legal review is mandatory.

---

## ⚖️ Ethical / Legal Notes
- **Bias:** Model over-weights offensive stars → risk of undervaluing role players.  
- **Fairness:** Ensure defensive/possession impact is represented (CT, GB+DC).  
- **Transparency:** Prompts + raw outputs are archived; edited text is labeled.  
- **Liability:** Misuse of AI advice without validation could misguide strategy.

---

## 🔬 Robustness & Uncertainty
- Try re-running with minor data perturbations (remove top N rows, change normalization).  
- Report confidence concisely (e.g., “Confidence: moderate; see Methods & validation script”).

---

## 🔁 Reproducibility & Archive
- **Repo:** Task_07_Decision_Making  
- **Prompts:** `prompts/` (raw .txt)  
- **Outputs:** `outputs/` (raw .txt)  
- **Validation code:** `code/validate_stats.py`  
- **Data lineage:** `docs/data_lineage.md`  
- **Note:** CSV not committed (per instructions).

---

## 🔮 Next Steps
1) Share with staff, collect feedback; 2) add multi-season trends; 3) expand features (minutes, injury); 4) keep testing LLM accuracy and log failure cases.

*Process > outcome:* this report emphasizes clarity, verification, and ethics.
