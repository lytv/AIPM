# Flashcard Format Guide - Anki Deck

## Giới Thiệu

Hệ thống flashcard này sử dụng **Anki format** với **spaced repetition algorithm** để tối ưu hóa việc ghi nhớ dài hạn.

### Tại Sao Anki?
- **Spaced repetition**: 95% improvement trong long-term memory
- **Adaptive**: Algorithm điều chỉnh theo performance của bạn
- **Cross-platform**: Desktop, mobile, web
- **Free và open-source**

---

## Card Types (4 Loại Thẻ)

### Type 1: Concept Definition (Định nghĩa khái niệm)

**Format**:
```
Front: [Khái niệm] là gì?
Back: [Định nghĩa ngắn gọn] + [Visual cue nếu có] + [Example]
```

**Example**:
```
Front: Product Discovery là gì?

Back:
Product Discovery là quá trình xác định sản phẩm đúng cần xây dựng thông qua:
- Nghiên cứu người dùng
- Thử nghiệm nhanh (rapid prototyping)
- Validation với chi phí thấp

🔑 Key: "Discover the product" vs "Deliver the product"

📝 Example: Before building LinkedIn's newsfeed, they tested 5 prototype variations with users to discover which approach solved the job best.

[Part V - Chapter 33: Principles of Product Discovery]
```

---

### Type 2: Framework Application (Áp dụng framework)

**Format**:
```
Front: Khi nào sử dụng [Framework/Tool]?
Back: [Tình huống] + [Steps to apply] + [Expected outcome]
```

**Example**:
```
Front: Khi nào sử dụng Jobs to Be Done framework?

Back:
Sử dụng JTBD khi:
✅ Cần hiểu động lực thật sự của khách hàng
✅ Users yêu cầu features nhưng bạn muốn hiểu "why"
✅ Muốn discover opportunities chưa được serve

Steps:
1. Identify the "job" user is trying to accomplish
2. Understand context và constraints
3. Map emotional + functional + social dimensions
4. Find gaps in current solutions

Expected Outcome:
→ Insight về jobs, không phải features
→ Better product-market fit
→ Innovation opportunities

❌ Don't use JTBD for: Quick feature prioritization, tactical decisions

[Part II - Chapter 5: Jobs to Be Done]
```

---

### Type 3: Visual Recognition (Nhận diện hình ảnh)

**Format**:
```
Front: [Image của framework/diagram]
Back: [Tên framework] + [Key components] + [When to use]
```

**Example**:
```
Front: [Image: Company OKR → Team OKR → Individual Contribution cascade diagram]

Back:
Framework: OKR Cascade (Objectives & Key Results)

Structure:
1. Company Objective (outcome-based, qualitative)
   └─ KR1, KR2, KR3 (measurable, quantitative)
2. Team Objective (supports company OKR)
   └─ KR1, KR2, KR3
3. Individual Contribution (how I contribute)

Key Principle: Alignment + Autonomy
- Objectives cascade down (alignment)
- Teams choose HOW to achieve (autonomy)

[Part III - Chapter 28: OKR Technique]
```

---

### Type 4: Case Judgment (Đánh giá tình huống)

**Format**:
```
Front: [Scenario mô tả] → Đây là dấu hiệu của gì?
Back: [Diagnosis] + [INSPIRED concept] + [What to do]
```

**Example**:
```
Front:
Scenario: Product team của bạn nhận roadmap từ Sales với 20 feature requests từ top customers. Team build theo list without user research. Engineers frustrated, churning high.

→ Đây là dấu hiệu của gì?

Back:
🚩 Diagnosis: **Feature Factory**

INSPIRED Concepts Violated:
❌ Feature teams, not empowered teams
❌ Output-driven (features) thay vì outcome-driven
❌ No discovery before delivery
❌ Mercenaries, not missionaries

Red Flags:
- Roadmap = feature list từ stakeholders
- No user research/validation
- Engineering frustration (no ownership)
- High churn (no empowerment)

What To Do (Theo Marty Cagan):
1. Transform roadmap: Features → Outcomes
2. Empower team to discover solutions
3. Establish product discovery process
4. Build missionary culture
5. Set outcome-based OKRs

✅ Good Team Alternative:
- Team owns outcomes, not features
- Discovery before delivery
- Engineers engaged in problem-solving
- User research informs decisions

[Part VI - Ch 64: Good Product Team vs Bad Product Team]
```

---

## Deck Structure (200+ Cards)

### Deck 1: Part I-II Fundamentals (60 cards)

**Part I - Lessons from Top Tech Companies (30 cards)**
- Ch 1-3: PM role, tech products, company stages (10 cards)
- Ch 6: Root causes of failure (10 cards)
- Ch 7: Beyond Lean & Agile (10 cards)

**Part II - Product Leadership (30 cards)**
- Ch 5: Jobs to Be Done (15 cards)
- Ch 6-9: PM/PO roles, leadership, culture (15 cards)

---

### Deck 2: Part III Strategy (50 cards)

**Strategic Frameworks (50 cards)**
- Ch 22-23: Roadmap problems (10 cards)
- Ch 24: Product Vision (10 cards)
- Ch 25-26: Vision & Strategy principles (10 cards)
- Ch 27: Product Principles (5 cards)
- Ch 28: OKRs (15 cards)

---

### Deck 3: Part IV-V Discovery & Process (60 cards)

**Part IV - Process (20 cards)**
- Team structure (10 cards)
- Collaboration models (10 cards)

**Part V - Discovery (40 cards)**
- Discovery principles (10 cards)
- Research techniques (10 cards)
- Prototyping (10 cards)
- Testing & validation (10 cards)

---

### Deck 4: Part VI Culture (30 cards)

**Culture & Mindset (30 cards)**
- Ch 64: Good vs Bad teams (10 cards)
- Ch 65-66: Loss of innovation/velocity (10 cards)
- Ch 67: Strong product culture (10 cards)

---

## Anki Text File Format

Each deck is a `.txt` file with this format:

```
Front text	Back text	Tags

Product Discovery là gì?	Product Discovery là quá trình xác định sản phẩm đúng cần xây dựng thông qua:<br>- Nghiên cứu người dùng<br>- Thử nghiệm nhanh (rapid prototyping)<br>- Validation với chi phí thấp<br><br>🔑 Key: "Discover the product" vs "Deliver the product"<br><br>📝 Example: Before building LinkedIn's newsfeed, they tested 5 prototype variations with users to discover which approach solved the job best.<br><br>[Part V - Chapter 33: Principles of Product Discovery]	INSPIRED::PartV::Discovery::Concept

Khi nào sử dụng JTBD framework?	Sử dụng JTBD khi:<br>✅ Cần hiểu động lực thật sự của khách hàng<br>✅ Users yêu cầu features nhưng bạn muốn hiểu "why"<br>✅ Muốn discover opportunities chưa được serve<br><br>Steps:<br>1. Identify the "job" user is trying to accomplish<br>2. Understand context và constraints<br>3. Map emotional + functional + social dimensions<br>4. Find gaps in current solutions<br><br>Expected Outcome:<br>→ Insight về jobs, không phải features<br>→ Better product-market fit<br>→ Innovation opportunities<br><br>❌ Don't use JTBD for: Quick feature prioritization, tactical decisions<br><br>[Part II - Chapter 5: Jobs to Be Done]	INSPIRED::PartII::JTBD::Framework
```

**Format Rules**:
- Tabs separate Front, Back, Tags
- `<br>` for line breaks
- Tags use `::` hierarchy: `INSPIRED::PartX::Topic::Type`

---

## Spaced Repetition Schedule

### Anki Default Algorithm
- **Again**: Card reset, show in <10 minutes
- **Hard**: Show in 1.2x previous interval
- **Good**: Show in 2.5x previous interval
- **Easy**: Show in 4x previous interval

### Recommended Settings
- New cards per day: 20 cards
- Maximum reviews per day: 100 cards
- Graduating interval: 1 day
- Easy interval: 4 days
- Starting ease: 250%

### Daily Routine
1. **Morning (10 min)**: Review due cards
2. **Evening (10 min)**: Learn new cards (20/day)
3. **Total**: ~20 minutes/day

---

## Best Practices

### Creating Good Cards

**✅ DO**:
- One concept per card
- Use Vietnamese for easier recall
- Include examples
- Add visual cues (emoji, symbols)
- Reference source chapter
- Test understanding, not memorization

**❌ DON'T**:
- Multiple concepts on one card
- Too long answers (>150 words)
- Vague questions ("What is PM?")
- No context or examples
- No source attribution

### Using Anki Effectively

1. **Consistency**: Daily practice > Binge studying
2. **Honest ratings**: Rate difficulty honestly
3. **Edit cards**: Improve cards that confuse you
4. **Add cards**: Create cards from mistakes
5. **Suspend cards**: Temporarily suspend mastered cards

---

## Sample Cards by Difficulty

### Easy (Beginner)
```
Front: Product Manager vs Product Owner - sự khác biệt chính?
Back:
PM: Strategic, customer-focused, owns outcomes
PO: Tactical, team-focused, owns backlog

PM > PO in scope và responsibilities
[Part II - Chapter 7: Product Owner]
```

### Medium (Intermediate)
```
Front: 4 loại risks trong Product Discovery là gì?
Back:
1. Value Risk: Will customers buy it?
2. Usability Risk: Can users figure out how to use it?
3. Feasibility Risk: Can we build it?
4. Viability Risk: Does it work for our business?

Discovery process phải address ALL 4 risks
[Part V - Chapter 33: Discovery Principles]
```

### Hard (Advanced)
```
Front: Company có strong product culture có đặc điểm gì? (Marty Cagan's definition)
Back:
Strong Product Culture characteristics:
1. Customer-centric: All decisions start with customer
2. Empowered teams: Teams own outcomes, not just output
3. Missionaries, not mercenaries: Believe in mission
4. Innovation culture: Safe to fail, learn fast
5. Data-informed: Use data to inform, not dictate
6. Discovery before delivery: Validate before building
7. Leadership: Product leaders coach và remove obstacles

Test: Can engineers directly talk to customers? Do teams set their own OKRs?
[Part VI - Chapter 67: Strong Product Culture]
```

---

## Import to Anki

### Steps
1. Install Anki from https://apps.ankiweb.net/
2. Create new deck: "INSPIRED - Part I-II Fundamentals"
3. File → Import → Select `.txt` file
4. Configure import settings:
   - Field 1: Front
   - Field 2: Back
   - Field 3: Tags
   - Field separator: Tab
5. Click Import

### Syncing
- Create AnkiWeb account (free)
- Sync across devices
- Study anywhere: Desktop, mobile, web

---

## Progress Tracking in Anki

### Stats to Monitor
- **Again rate**: Should be <20% (if higher, cards too hard)
- **Mature cards**: Goal is 80%+ mature after 3 weeks
- **Review time**: Average 30-45 seconds per card
- **Daily streak**: Aim for 60+ day streak

### Monthly Review
- Export stats
- Identify difficult cards
- Update/improve problematic cards
- Celebrate milestones (100, 200 cards mature!)

---

## Conclusion

**200+ flashcards** covering toàn bộ INSPIRED = **Comprehensive retention system**

**Commit**: 20 minutes/day for 60 days
**Result**: Master 200+ PM concepts with 95% retention

Ready to build the decks! 🚀
