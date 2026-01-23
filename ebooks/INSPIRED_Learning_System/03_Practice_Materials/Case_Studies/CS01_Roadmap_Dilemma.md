# Case Study 01 - Thoát Khỏi "Feature Factory"

## Thông Tin Case Study

**Tiêu đề**: Từ Feature-Driven đến Outcome-Based: Chuyển Đổi Roadmap tại VietPay
**Chủ đề INSPIRED**: Part II (JTBD, PM Role) + Part III (Vision, Strategy, OKRs)
**Độ khó**: ⭐⭐⭐ (3/5 sao)
**Thời gian ước tính**: 60-90 phút

---

## PART 1: SITUATION (Tình Huống) - 10 phút đọc

### Company Context (Bối cảnh công ty)

**Tên công ty**: VietPay
**Ngành**: Fintech - Digital Wallet & Payment
**Giai đoạn**: Series A (vừa gọi được $8M từ quỹ đầu tư Singapore)
**Quy mô**:
- 45 nhân viên (15 tech, 12 sales/marketing, 8 ops, 10 admin/support)
- 250,000 active users (MAU)
- GMV: $12M/tháng
- Launched: 18 tháng trước

**Về VietPay**:
VietPay là ví điện tử cho phép người dùng thanh toán QR, chuyển tiền miễn phí, và nạp tiền điện thoại. Ra mắt tại TP.HCM, công ty đang mở rộng sang Hà Nội và các tỉnh thành lớn. Sau khi gọi vốn Series A thành công, Board đặt mục tiêu tăng trưởng 5x users trong 12 tháng tới.

### Market Conditions (Điều kiện thị trường)

**Competitive Landscape**:
- **MoMo**: Market leader, 30M users, ví điện tử đa tiện ích với mini-apps
- **ZaloPay**: 15M users, tích hợp mạnh với Zalo ecosystem
- **ShopeePay**: 10M users, lợi thế từ e-commerce Shopee
- **VietPay**: 250K users, nhỏ nhưng tốc độ tăng trưởng 15%/tháng

**Market trend**:
- Thanh toán không tiền mặt tăng 35% năm 2025 ở Việt Nam
- Gen Z (18-25 tuổi) chiếm 40% users của digital wallets
- Competition gay gắt: MoMo và ZaloPay đều có chương trình cashback khủng
- Regulation mới: NHNN yêu cầu eKYC chặt chẽ hơn từ Q2/2026

**User Base**:
- **Target users**: Gen Z và Millennials (18-35 tuổi) tại thành phố lớn
- **Current pain points**:
  1. Số lượng điểm chấp nhận thanh toán QR còn ít (10,000 merchants vs 200,000+ của MoMo)
  2. Không có tính năng đầu tư/tiết kiệm như ví khác
  3. Chương trình khuyến mãi không hấp dẫn bằng competitors
  4. App còn chậm, nhiều bugs (App Store rating: 3.8/5)
  5. Customer support phản hồi chậm (average 6 giờ)

### Problem Statement (Vấn đề cốt lõi)

**Bạn là Minh**, Product Manager duy nhất của VietPay, vừa được hire 2 tuần trước. Bạn có 5 năm kinh nghiệm làm PM tại một startup e-commerce nhỏ, nhưng đây là lần đầu bạn làm trong fintech.

Trong first week, bạn phát hiện ra một vấn đề nghiêm trọng:

**Q1 2026 Roadmap (đã được approve bởi CEO và Sales Director) bao gồm:**

1. **Tính năng "Lucky Wheel"** (gamification để tăng engagement)
   - Sales Director yêu cầu: "MoMo có vòng quay may mắn, mình cũng phải có!"
   - Timeline: Ship trước Tết (3 tuần nữa)
   - Estimated effort: 120 man-hours

2. **Tích hợp thanh toán hóa đơn điện, nước, internet**
   - CEO yêu cầu: "Đối tác mới (EVN, VNPT) đã ký MOU, cần ship Q1"
   - Timeline: End of Q1
   - Estimated effort: 200 man-hours

3. **Chức năng "Chia bill" với bạn bè**
   - Sales Director: "Khách hàng VIP request feature này 5 lần rồi!"
   - Timeline: Mid Q1
   - Estimated effort: 80 man-hours

4. **Theme Tết (giao diện đỏ đào, hoa mai)**
   - Marketing Director: "App phải có theme Tết, như Shopee ấy!"
   - Timeline: Trước Tết (2 tuần nữa)
   - Estimated effort: 40 man-hours

5. **Tính năng "Refer a Friend" với thưởng 50K/bạn**
   - Growth lead: "Đây là cách nhanh nhất để tăng users!"
   - Timeline: Q1
   - Estimated effort: 100 man-hours

**Total Q1 commitment**: 540 man-hours
**Team capacity**: 2 mobile developers + 1 backend dev = ~480 man-hours/quarter (đã trừ bugs, meetings, etc.)

**VƯỢT CAPACITY 12.5%** - và đây chưa tính technical debt, bugs, và maintenance!

### Challenges (Thách thức)

**Challenge 1: Feature Factory Mindset**
- Roadmap là một "feature list" không có prioritization rõ ràng
- Không có outcome metrics - chỉ có "ship by date"
- Không ai biết features này sẽ impact business metrics như thế nào
- PM role hiện tại = "Project manager" nhận requirements từ Sales/CEO

**Challenge 2: Lack of Discovery**
- Không có user research nào được conduct
- "Khách hàng VIP request" = 5 người trong tổng số 250K users (0.002%)
- Không validate assumptions: "Lucky Wheel sẽ tăng engagement" - có evidence gì?
- Không biết users thực sự cần gì (Jobs to Be Done chưa được xác định)

**Challenge 3: Technical Debt Crisis**
- Backlog có 127 bugs (32 critical, 95 minor)
- App performance issues: Average load time 4.5 giây (industry standard: <2 giây)
- Crash rate: 2.3% (acceptable là <1%)
- Engineers frustrated vì không có time fix technical debt

**Challenge 4: No Clear Strategy**
- Product vision không rõ ràng: "Trở thành ví điện tử #1 Việt Nam" (quá generic)
- Không có OKRs - chỉ có "tăng users 5x" (input metric, không phải outcome)
- Không biết competitive advantage là gì
- Strategy = "copy MoMo"

### Stakeholder Constraints (Ràng buộc từ stakeholders)

**CEO (Anh Tuấn, 38 tuổi, founder):**
- Pressure từ investors: "Phải đạt 1.2M MAU end of year để raise Series B"
- Mindset: "Ship fast, iterate later"
- Expectation: "PM phải deliver theo roadmap đã commit với board"
- Quote: "Minh ơi, anh biết em vừa join, nhưng roadmap này đã approve rồi. Mình cần execute thôi!"

**Sales Director (Chị Lan, 35 tuổi):**
- Bonus tied to: Số lượng merchants onboard
- Pain point: "Merchants hỏi: Sao VietPay không có feature X như MoMo?"
- Expectation: "Features phải ship đúng deadline để close deals"
- Quote: "Em không hiểu, features này merchants đang đòi đấy. Không ship là mất deals!"

**Engineering Lead (Anh Khoa, 32 tuổi):**
- Team morale thấp: 2 senior devs đang consider resign
- Technical debt crisis: "Codebase như núi rác rồi"
- Constraint: Only 480 man-hours/quarter thực tế (sau khi trừ bugs, meetings)
- Quote: "Roadmap này không realistic. Anh cần time fix tech debt, nếu không app sẽ collapse."

**Timeline:**
- **Tết Nguyên Đán**: 2 tuần nữa (hard deadline cho Lucky Wheel + Theme Tết)
- **End of Q1**: 10 tuần nữa
- **Series B fundraising**: Target Q4 2026 (9 tháng nữa)
- **Board meeting**: 3 tuần nữa - CEO sẽ present progress

**Budget:**
- Engineering budget: Fixed (2 mobile + 1 backend + 1 QA)
- Marketing budget: $50K/quarter cho user acquisition
- No budget for user research, design, or additional hires trong Q1

---

## PART 2: YOUR MISSION (Nhiệm Vụ Của Bạn)

Bạn là Minh - Product Manager của VietPay. Đây là tuần thứ 3 của bạn. Sáng nay, anh Khoa (Engineering Lead) pull bạn vào 1-on-1 và nói:

> "Minh, anh nói thẳng nhé. Roadmap này không khả thi. Team anh đang burnout với bugs. 2 senior dev đang có offer từ ngoài. Nếu ship tiếp feature mà không fix tech debt, app sẽ crash. Anh cần em là PM thật sự, không phải project coordinator. Em phải pushback với CEO và Sales."

Chiều nay, bạn có 1-on-1 với CEO. Đây là cơ hội để influence roadmap.

### Deliverables (Kết quả cần nộp)

Bạn cần chuẩn bị cho 1-on-1 meeting với CEO:

- [ ] **Analysis Document**: Phân tích current situation (4 risks, root causes)
- [ ] **Strategic Recommendation**: Đề xuất approach mới (outcome-based)
- [ ] **Revised Q1 Plan**: Re-prioritize roadmap dựa trên JTBD và OKRs
- [ ] **Success Metrics**: Define OKRs cho Q1 (outcome, not output)
- [ ] **Stakeholder Communication Plan**: Làm sao convince CEO và Sales

### Choose Your Approach (Chọn cách tiếp cận)

Dựa trên kiến thức từ INSPIRED, bạn sẽ áp dụng approach nào?

- [ ] **Option A**: Discovery-focused approach
  - Focus: Pause roadmap, run discovery sprints to validate assumptions
  - Tools: User interviews, JTBD research, prototype testing
  - Risk: CEO sẽ reject vì "mất time", investors đang chờ progress

- [ ] **Option B**: Strategy-focused approach
  - Focus: Define product vision, create OKRs, transform to outcome roadmap
  - Tools: Product vision framework, OKR setting, prioritization
  - Risk: Quá "big picture", CEO muốn thấy concrete actions ngay

- [ ] **Option C**: Hybrid approach (RECOMMENDED)
  - Focus: Quick wins + Strategic foundation
  - Phase 1: Re-prioritize current roadmap (outcome-based)
  - Phase 2: Introduce lightweight discovery practices
  - Phase 3: Build strategic foundation (vision, OKRs)
  - Tools: JTBD, OKRs, rapid prototyping, stakeholder management

**Your chosen approach**: ____________
**Lý do**: _________________________

---

## PART 3: STAR ANALYSIS (Phân Tích Theo STAR)

### S - SITUATION (Phân tích tình huống)

**Câu hỏi hướng dẫn**:

1. **Root cause analysis**: Vấn đề gốc rễ của VietPay là gì? (Hint: Review Chapter 6 - Root Causes of Failed Product Efforts)

2. **INSPIRED concepts**: Concepts nào từ INSPIRED apply cho case này?
   - Part I: Root causes of failure?
   - Part II: PM role vs PO role?
   - Part III: Roadmap problems? Vision/Strategy/OKRs?

3. **The 4 Risks Assessment**:
   - **Value risk**: Có evidence nào rằng features này valuable cho users không?
   - **Usability risk**: Users có dùng được features này không?
   - **Feasibility risk**: Team có capacity ship không?
   - **Viability risk**: Features này support business model không?

4. **Jobs to Be Done**: Users "hire" VietPay để làm gì?
   - Functional jobs?
   - Emotional jobs?
   - Social jobs?

**Your analysis** (minimum 300 từ):

```
[VIẾT PHÂN TÍCH CỦA BẠN Ở ĐÂY]

Gợi ý structure:
- Đoạn 1: Root causes (2-3 causes từ Ch 6)
- Đoạn 2: 4 Risks analysis (high/medium/low cho mỗi risk)
- Đoạn 3: JTBD analysis (users "hire" VietPay để làm gì?)
- Đoạn 4: PM role issue (hiện tại là PO hay PM?)
```

---

### T - TASK (Xác định nhiệm vụ)

**Câu hỏi hướng dẫn**:

1. Objective chính của bạn là gì? (Hint: Không phải "ship 5 features")
2. Bạn cần convince stakeholders điều gì?
3. Success criteria cho Q1 nên là gì? (Outcome metrics, not output)
4. Priorities: Cái gì MUST do, cái gì SHOULD do, cái gì CAN WAIT?

**Your task definition**:

**Primary Objective**:
```
[VD: "Transform VietPay from feature factory to outcome-driven product organization"]
```

**Secondary Objectives**:
1. ___________________________
2. ___________________________
3. ___________________________

**Success Criteria** (Q1 2026):

**Business Outcomes**:
- [ ] [VD: Tăng retention rate từ X% lên Y%]
- [ ] [VD: Reduce churn từ X% xuống Y%]
- [ ] [VD: Increase transaction frequency từ X lên Y lần/user/tháng]

**Team Health**:
- [ ] [VD: Reduce critical bugs từ 32 xuống <10]
- [ ] [VD: Improve app performance: load time <2.5s]
- [ ] [VD: Engineering satisfaction score >7/10]

**Strategic Foundation**:
- [ ] [VD: Có product vision rõ ràng, được align với team]
- [ ] [VD: Q2 roadmap là outcome-based, không phải feature list]

---

### A - ACTION (Kế hoạch hành động)

**Câu hỏi hướng dẫn**:

1. Concrete steps bạn sẽ làm trong 3 tuần tới?
2. Frameworks nào từ INSPIRED bạn sẽ apply?
3. Làm sao handle stakeholders (CEO, Sales, Engineering)?
4. Quick wins để build credibility?

**Your action plan**:

#### Week 1 (Tuần này): Foundation & Quick Wins

**Days 1-2: Data Gathering & Analysis**
- [ ] Action 1: ___________________________
- [ ] Action 2: ___________________________
- [ ] Deliverable: ___________________________

**Days 3-4: Stakeholder Alignment**
- [ ] Action 1: ___________________________
- [ ] Action 2: ___________________________
- [ ] Deliverable: ___________________________

**Day 5: CEO 1-on-1 Presentation**
- [ ] Action 1: ___________________________
- [ ] Deliverable: ___________________________

---

#### Week 2-3: Re-prioritization & Discovery

**Week 2: JTBD Research & Prioritization**
- [ ] ___________________________
- [ ] ___________________________
- [ ] Deliverable: ___________________________

**Week 3: Execute Revised Q1 Plan**
- [ ] ___________________________
- [ ] ___________________________
- [ ] Deliverable: ___________________________

---

#### Week 4-10: Q1 Execution với Outcome Focus

**Monthly Milestones**:
- **End of Month 1**: ___________________________
- **End of Month 2**: ___________________________
- **End of Q1**: ___________________________

---

**INSPIRED Frameworks Applied**:

Tick (✓) frameworks bạn sẽ dùng và ghi cụ thể apply như thế nào:

- [ ] **Jobs to Be Done**: ___________________________
- [ ] **Product Discovery**: ___________________________
- [ ] **OKRs**: ___________________________
- [ ] **Outcome-based roadmap**: ___________________________
- [ ] **4 Risks mitigation**: ___________________________
- [ ] **Product vision**: ___________________________
- [ ] **Product strategy**: ___________________________
- [ ] **Stakeholder management**: ___________________________

---

### R - RESULT (Kết quả đo lường)

**Câu hỏi hướng dẫn**:

1. OKRs cho Q1 nên là gì?
2. Leading indicators (early signals) để track?
3. Lagging indicators (long-term metrics)?
4. Làm sao biết approach của bạn success?

**Your success metrics**:

#### OKR Structure cho Q1 2026

**Objective 1**: [Outcome-based objective, VD: "Biến VietPay thành payment method ưa thích cho Gen Z"]

- **KR1**: ___________________________ (Measurable)
- **KR2**: ___________________________ (Measurable)
- **KR3**: ___________________________ (Measurable)

**Objective 2**: [VD: "Xây dựng foundation vững chắc cho scale"]

- **KR1**: ___________________________
- **KR2**: ___________________________
- **KR3**: ___________________________

---

#### Metrics Dashboard

**Leading Indicators** (Track weekly):
| Metric | Baseline | Target Q1 | Week 1 | Week 4 | Week 10 |
|--------|----------|-----------|--------|--------|---------|
| [VD: DAU/MAU ratio] | 25% | 35% | | | |
| [VD: Transaction frequency] | 2.3/month | 4/month | | | |
| [VD: Feature adoption rate] | - | >40% | | | |
| [Your metric 1] | | | | | |
| [Your metric 2] | | | | | |

**Lagging Indicators** (Track monthly):
| Metric | Baseline | Target EOQ |
|--------|----------|------------|
| [VD: Retention (D30)] | 18% | 28% |
| [VD: Churn rate] | 12%/month | <8%/month |
| [VD: NPS] | 32 | 45+ |
| [VD: App Store rating] | 3.8 | 4.2+ |
| [Your metric] | | |

**Team Health Metrics**:
| Metric | Baseline | Target |
|--------|----------|--------|
| Critical bugs | 32 | <10 |
| App crash rate | 2.3% | <1% |
| Load time (avg) | 4.5s | <2.5s |
| Engineering NPS | Unknown | 7+/10 |

---

## PART 4: REFLECTION (Phản Chiếu)

### INSPIRED Concepts Applied

**Liệt kê concepts từ INSPIRED bạn đã áp dụng**:

1. _____________________________ từ [Part X, Chapter Y]
   - Applied như thế nào: _____________________________

2. _____________________________ từ [Part X, Chapter Y]
   - Applied như thế nào: _____________________________

3. _____________________________ từ [Part X, Chapter Y]
   - Applied như thế nào: _____________________________

(Minimum 5 concepts)

---

### What Would Marty Cagan Recommend?

**Dựa trên sách INSPIRED, trong tình huống này Marty Cagan sẽ:**

```
[Viết 150-200 từ về những gì Marty sẽ recommend]

Gợi ý:
- Chapter 6 nói gì về root causes?
- Chapter 22-23 nói gì về roadmap problems?
- Chapter 28 nói gì về OKRs?
- Part II nói gì về PM role?
```

**Key quotes từ INSPIRED relevant cho case này**:

1. "_____________________________" (Chapter ___)
2. "_____________________________" (Chapter ___)
3. "_____________________________" (Chapter ___)

---

### Trade-offs & Risks

**Trade-offs bạn đã make**:

1. **Trade-off 1**: Chose _________ over _________
   - **Reason**: _____________________________
   - **Risk**: _____________________________
   - **Mitigation**: _____________________________

2. **Trade-off 2**: Chose _________ over _________
   - **Reason**: _____________________________
   - **Risk**: _____________________________
   - **Mitigation**: _____________________________

3. **Trade-off 3**: Chose _________ over _________
   - **Reason**: _____________________________
   - **Risk**: _____________________________
   - **Mitigation**: _____________________________

---

**Risks Remaining & Mitigation**:

| Risk Type | Risk Description | Probability | Impact | Mitigation Plan |
|-----------|------------------|-------------|--------|-----------------|
| **Value** | | High/Med/Low | High/Med/Low | |
| **Usability** | | High/Med/Low | High/Med/Low | |
| **Feasibility** | | High/Med/Low | High/Med/Low | |
| **Viability** | | High/Med/Low | High/Med/Low | |

---

### Personal Learning

**What did you learn about yourself as a PM?**:

**Strengths I demonstrated**:
- _____________________________
- _____________________________

**Growth areas I discovered**:
- _____________________________
- _____________________________

**Specific actions for improvement**:
1. _____________________________
2. _____________________________

**Next learning goal**:
- _____________________________

---

## PART 5: SELF-EVALUATION

### Scorecard (Rate yourself 1-10)

| Criteria | Score | Evidence/Notes |
|----------|-------|----------------|
| **Applied JTBD correctly** | __/10 | Did you identify real jobs users are trying to accomplish? |
| **Strategic thinking** | __/10 | Did you focus on vision, strategy, OKRs (not just tactics)? |
| **Outcome-focused approach** | __/10 | Are metrics outcomes (user behavior) not outputs (features shipped)? |
| **Considered all 4 risks** | __/10 | Did you assess Value, Usability, Feasibility, Viability? |
| **Stakeholder management** | __/10 | Did you balance CEO, Sales, and Engineering concerns? |
| **Actionable plan** | __/10 | Is plan concrete with clear timeline and owners? |
| **Measurable results** | __/10 | Are OKRs and KRs measurable and time-bound? |

**Total Score**: ___/70

---

### Detailed Rubric

#### Excellent (60-70 points):
- ✅ Clear JTBD analysis với evidence
- ✅ Well-defined OKRs (Objective = outcome, KRs = measurable)
- ✅ Outcome-based roadmap, không phải feature list
- ✅ Realistic plan với clear trade-offs
- ✅ Strong stakeholder management strategy
- ✅ Applied 5+ INSPIRED concepts correctly
- ✅ Deep understanding of root causes

#### Good (50-59 points):
- ✅ JTBD analysis present nhưng thiếu depth
- ✅ OKRs có nhưng một số KRs còn là outputs
- ✅ Roadmap có outcome thinking nhưng chưa consistent
- ✅ Plan khả thi nhưng thiếu details
- ✅ Applied 3-4 INSPIRED concepts
- ✅ Identified 2-3 root causes

#### Developing (40-49 points):
- ⚠️ JTBD analysis surface-level
- ⚠️ OKRs confused với goals/outputs
- ⚠️ Roadmap vẫn feature-focused
- ⚠️ Plan vague, thiếu concrete actions
- ⚠️ Applied 1-2 INSPIRED concepts
- ⚠️ Chưa rõ root causes

#### Needs Work (<40 points):
- ❌ Không apply JTBD
- ❌ Không có OKRs hoặc metrics
- ❌ Vẫn là feature roadmap
- ❌ Không có clear action plan
- ❌ Không reference INSPIRED concepts
- ❌ Không hiểu root causes

---

## BONUS: SOLUTION HINTS & PARTIAL ANSWER KEY

### Hint 1: Root Causes Analysis

**VietPay đang mắc các root causes sau (theo Chapter 6):**

1. **Root Cause #1**: ___________________________
   - Evidence trong case: _____________________________
   - Impact: _____________________________

2. **Root Cause #2**: ___________________________
   - Evidence trong case: _____________________________
   - Impact: _____________________________

3. **Root Cause #3**: ___________________________
   - Evidence trong case: _____________________________
   - Impact: _____________________________

<details>
<summary>Click để xem suggested answer</summary>

**Root Cause #1: Roadmap-Driven (not outcome-driven)**
- Evidence: Q1 roadmap là feature list với deadlines, không có success metrics
- Impact: Team ship features but don't know if they create value

**Root Cause #2: Role of PM (acting as PO/Project Manager, not PM)**
- Evidence: Minh nhận requirements từ Sales/CEO, không challenge assumptions
- Impact: No discovery, no strategy, just execution

**Root Cause #3: No Product Vision/Strategy**
- Evidence: Vision = "Trở thành #1" (generic), strategy = "copy MoMo"
- Impact: Features không aligned, scattered efforts

</details>

---

### Hint 2: JTBD Analysis

**Users "hire" VietPay để làm việc gì?**

**Functional Jobs**:
- Job 1: _____________________________
- Job 2: _____________________________

**Emotional Jobs**:
- Job 1: _____________________________

**Social Jobs**:
- Job 1: _____________________________

<details>
<summary>Click để xem suggested answer</summary>

**Functional Jobs**:
- "Send money to friends/family instantly without going to bank"
- "Pay at merchants quickly without cash"
- "Top up phone credit conveniently"

**Emotional Jobs**:
- "Feel smart/modern when using digital payment"
- "Feel secure that my money is safe"

**Social Jobs**:
- "Be seen as tech-savvy among friends"

**Key insight**: Current roadmap features (Lucky Wheel, Bill Payment) không directly address core JTBD. "Chia bill" có thể support JTBD "send money to friends" nhưng need validation.

</details>

---

### Hint 3: Sample OKR

**Bad OKR (Output-focused)**:
- Objective: Ship 5 features in Q1
- KR1: Launch Lucky Wheel by Tết
- KR2: Integrate bill payment by end Q1
- KR3: Get 10,000 new users

**Good OKR (Outcome-focused)**:
- Objective: _____________________________
- KR1: _____________________________
- KR2: _____________________________
- KR3: _____________________________

<details>
<summary>Click để xem suggested answer</summary>

**Good OKR Example**:

**Objective**: "Make VietPay the most reliable and frequently-used wallet for Gen Z"

**KR1**: Increase transaction frequency from 2.3 to 4 transactions/user/month
**KR2**: Improve D30 retention from 18% to 28%
**KR3**: Reduce critical bugs from 32 to <10 (reliability)

**Rationale**:
- Objective = outcome (user behavior change)
- KRs = measurable, ambitious, time-bound
- Focus on retention & usage (not acquisition)

</details>

---

### Hint 4: Revised Q1 Priorities

**Current roadmap có 5 features. Dựa trên JTBD và 4 Risks, prioritize lại:**

| Feature | Value Risk | Feasibility Risk | Priority | Decision |
|---------|------------|------------------|----------|----------|
| Lucky Wheel | High (no validation) | Low (easy) | Low | DEFER |
| Bill Payment | Med (có demand) | Med (partner dependency) | Med | DESCOPE → lightweight version |
| Chia Bill | ? | Low | ? | VALIDATE first |
| Theme Tết | Low (cosmetic) | Low | Low | DEFER hoặc làm minimal |
| Refer a Friend | ? | Med | ? | VALIDATE economics |

**Your revised roadmap**:
1. _____________________________
2. _____________________________
3. _____________________________

<details>
<summary>Click để xem suggested answer</summary>

**Revised Q1 Roadmap (Outcome-based)**:

**Must Do (Support OKRs)**:
1. **Fix critical bugs + performance** (32 bugs → <10, load time <2.5s)
   - Why: Reliability là foundation cho retention
   - Effort: 150 hours
   - Impact: Reduce churn, improve rating

2. **Lightweight discovery**: User interviews (20 users) về payment habits
   - Why: Validate assumptions, identify real JTBD
   - Effort: 40 hours (PM + 1 designer)
   - Impact: Inform Q2 roadmap

3. **ONE bet based on JTBD**: "Quick split bill" (if validated)
   - Why: Support core JTBD "send money to friends"
   - Effort: 80 hours
   - Impact: KR1 (transaction frequency)

**Should Do (if capacity)**:
4. **Bill payment MVP**: Chỉ điện + nước (không phải internet)
   - Why: Merchant commitment, but descoped
   - Effort: 120 hours

**Defer to Q2**:
- Lucky Wheel: No evidence of value
- Theme Tết: Cosmetic, low ROI
- Refer a Friend: Need to design economics properly

**Total: ~390 hours vs 480 capacity** → Healthy buffer

</details>

---

### Hint 5: CEO Conversation Framework

**Làm sao convince CEO trong 1-on-1?**

**DON'T**:
- ❌ "Roadmap này sai, em muốn làm lại"
- ❌ "Em đọc sách INSPIRED, họ nói phải làm khác"
- ❌ "Anh không hiểu PM, để em handle"

**DO**:
- ✅ Start with shared goal: "Anh muốn 1.2M MAU để raise Series B đúng không?"
- ✅ Present data: "Current retention 18% → nếu không fix, churn rate sẽ kill growth"
- ✅ Show math: "Acquire 1M users nhưng retain 18% = waste marketing budget"
- ✅ Propose alternative: "Nếu improve retention 18%→28%, cần acquire ít hơn 30%"
- ✅ Quick wins: "Em sẽ ship 1-2 features, nhưng focus vào những cái impact retention"

**Your conversation outline**:

_____________________________
_____________________________
_____________________________

---

## Notes & Additional Thoughts

**Space for brainstorming, questions, or additional ideas**:

```
[Ghi notes của bạn ở đây]

- Questions cần research thêm:
- Assumptions cần validate:
- Stakeholder concerns cần address:
```

---

## Completion Checklist

- [ ] Đã phân tích situation thoroughly (4 risks, JTBD, root causes)
- [ ] Đã define clear tasks và objectives (outcome-based)
- [ ] Đã tạo action plan với timeline cụ thể
- [ ] Đã set OKRs và metrics (leading + lagging indicators)
- [ ] Đã apply ít nhất 5 INSPIRED concepts
- [ ] Đã xác định trade-offs và risks
- [ ] Đã reflect về personal learning
- [ ] Đã self-evaluate với rubric

---

**Completed Date**: __/__/____
**Time Spent**: ___ minutes
**Overall Confidence**: ⭐⭐⭐⭐⭐ (1-5 sao)
**Would I recommend this case to other PMs**: ⭐⭐⭐⭐⭐

---

## Feedback & Discussion

**Muốn discuss case study này?**
- Join INSPIRED Learning System community
- Share your solution và nhận feedback từ other PMs
- Xem sample solutions từ experienced PMs

**Next Steps**:
- Sau khi hoàn thành case study này, move to **Case Study 02: Discovery vs Delivery Balance**
- Practice more JTBD exercises trong Exercise Set Week 2
- Read Part III (Vision, Strategy, OKRs) để deepen understanding

---

**Case Study Version**: 1.0
**Created for**: INSPIRED Learning System - Week 2
**Difficulty**: ⭐⭐⭐ (Intermediate)
**Learning Objectives**: JTBD, PM Role, Outcome thinking, OKRs, Stakeholder management
