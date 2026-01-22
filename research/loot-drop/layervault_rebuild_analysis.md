# LayerVault Rebuild: Business Analysis

**Product Concept:** "GitFig" - Design Version Control Platform  
**Date:** 2026-01-22  
**Status:** Research & Planning

---

## 📊 Business Model Analysis

### Revenue Streams

| Stream | Model | Description |
|--------|-------|-------------|
| **Primary** | SaaS Subscription | Monthly/yearly per-seat pricing |
| **Secondary** | Storage upsell | Additional storage beyond free tier |
| **Tertiary** | Enterprise features | SSO, audit logs, compliance |

---

## 💰 Pricing Strategy

### Option A: "Freemium + Per-Seat" (Recommended)

```
┌──────────────────────────────────────────────────────────┐
│                    PRICING TIERS                          │
├──────────────────────────────────────────────────────────┤
│                                                           │
│  🆓 FREE (Solo)                                           │
│  ├─ 1 user                                                │
│  ├─ 3 projects                                            │
│  ├─ 30-day version history                                │
│  ├─ Figma plugin only                                     │
│  └─ 1 GB storage                                          │
│                                                           │
│  💼 PRO ($12/user/month, billed annually)                 │
│  ├─ Unlimited projects                                    │
│  ├─ Unlimited version history                             │
│  ├─ Branching & merging                                   │
│  ├─ Visual diff (AI-powered)                              │
│  ├─ Figma + Sketch support                                │
│  ├─ 10 GB storage/user                                    │
│  └─ Team commenting & review                              │
│                                                           │
│  🏢 TEAM ($18/user/month, min 5 users)                    │
│  ├─ Everything in Pro                                     │
│  ├─ Design system sync                                    │
│  ├─ Advanced permissions                                  │
│  ├─ Slack/Teams integration                               │
│  ├─ 25 GB storage/user                                    │
│  └─ Priority support                                      │
│                                                           │
│  🏛️ ENTERPRISE (Custom pricing, min 25 users)            │
│  ├─ Everything in Team                                    │
│  ├─ SSO (SAML/OIDC)                                       │
│  ├─ Audit logs & compliance                               │
│  ├─ Custom storage                                        │
│  ├─ Dedicated support                                     │
│  └─ On-premise option                                     │
│                                                           │
└──────────────────────────────────────────────────────────┘
```

### Pricing Rationale

| Decision | Reasoning |
|----------|-----------|
| **$12/user Pro** | Abstract was $9-15, positioned middle-ground |
| **Free tier** | Essential for PLG (Product-Led Growth), designers try before buy |
| **Annual discount** | 2 months free encourages commitment |
| **5-user minimum Team** | Avoids supporting tiny teams at enterprise cost |

---

## 📈 Revenue Projections

### Conservative Scenario (Year 1-3)

```
Year 1:
├─ Free users: 5,000
├─ Pro conversions: 500 (10%)
├─ Avg Pro price: $10/month (discounts)
├─ MRR: $5,000
└─ ARR: $60,000

Year 2:
├─ Free users: 20,000
├─ Pro users: 2,000 (10%)
├─ Team users: 200 (small teams)
├─ MRR: $23,600
└─ ARR: $283,200

Year 3:
├─ Free users: 50,000
├─ Pro users: 5,000
├─ Team users: 1,000
├─ Enterprise: 5 companies (avg 50 users)
├─ MRR: $83,000
└─ ARR: ~$1M
```

### Optimistic Scenario (Captures Abstract Users)

```
Year 1: ARR $150K (500 Abstract refugees)
Year 2: ARR $600K (Product-market fit)
Year 3: ARR $2M+ (Team/Enterprise growth)
```

---

## 🎯 Go-to-Market Strategy

### Phase 1: Launch (Month 1-3)

```
┌─────────────────────────────────────────┐
│           LAUNCH STRATEGY               │
├─────────────────────────────────────────┤
│                                         │
│  1. Target Audience                     │
│     └─ Former Abstract users            │
│     └─ Designers frustrated with Figma  │
│        version history                  │
│                                         │
│  2. Channels                            │
│     └─ Twitter/X design community       │
│     └─ Figma Community forum            │
│     └─ Designer Discord servers         │
│     └─ Product Hunt launch              │
│                                         │
│  3. Initial Offer                       │
│     └─ "Founding Member" discount       │
│        (40% off first year)             │
│     └─ Free migration from Abstract     │
│                                         │
└─────────────────────────────────────────┘
```

### Phase 2: Growth (Month 4-12)

| Channel | Strategy | CAC Target |
|---------|----------|------------|
| **Content** | Blog: "Git for Designers" tutorials | $0 (organic) |
| **SEO** | Target "Abstract alternative", "Figma version control" | $0 (organic) |
| **Referral** | Give 1 month free for referrals | $12 |
| **Partnerships** | Design agencies, bootcamps | $50-100 |

### Phase 3: Scale (Year 2+)

- **Team expansion**: Sales team for Enterprise
- **Platform expansion**: Add Framer, Penpot support
- **Integration**: Jira, Linear, Notion plugins

---

## 💸 Cost Structure

### Fixed Costs (Monthly)

| Item | Cost | Notes |
|------|------|-------|
| Cloud infrastructure (base) | $200 | Scales with users |
| Domain + services | $50 | |
| Figma API fees | $0 | Free for plugins |
| **Total Fixed** | **$250/month** | |

### Variable Costs (Per User)

| Item | Cost/User | Notes |
|------|-----------|-------|
| Storage (S3) | $0.05/GB | Design files large |
| CDN bandwidth | $0.02/GB | |
| Support (at scale) | $1-2/user | |

### Break-even Analysis

```
Fixed costs: $250/month
Avg revenue/user: $10/month
Variable cost/user: $2/month
Contribution margin: $8/user

Break-even: 250 / 8 = ~32 paying users

With 50 Pro users: $150/month profit
With 500 Pro users: $3,750/month profit
With 2,000 Pro users: $15,750/month profit
```

---

## ⚠️ Risk Factors

| Risk | Probability | Impact | Mitigation |
|------|-------------|--------|------------|
| **Figma adds branching** | Medium | High | Focus on multi-platform, AI diff |
| **Low conversion free→paid** | Medium | Medium | Improve onboarding, feature gates |
| **Tech complexity** | Low | Medium | Start Figma-only, expand later |
| **Funding needed** | Low | Low | Bootstrappable to $1M ARR |

---

## 🏁 Key Metrics to Track

### North Star Metric
**Weekly Active Branches Created** - measures core product usage

### Supporting Metrics

| Category | Metric | Target (Y1) |
|----------|--------|-------------|
| Acquisition | Free signups/month | 500+ |
| Activation | Create first branch | 60%+ |
| Retention | Weekly active (Pro) | 70%+ |
| Revenue | Free→Pro conversion | 10%+ |
| Referral | NPS score | 50+ |

---

## 🚀 Bottom Line

| Aspect | Assessment |
|--------|------------|
| **Market opportunity** | ✅ Strong - gap left by Abstract |
| **Business model** | ✅ Proven - SaaS per-seat is standard |
| **Unit economics** | ✅ Healthy - high margin software |
| **Bootstrappable** | ✅ Yes - can reach profitability solo |
| **Scalability** | ✅ High - software scales well |

**Recommendation: GREEN LIGHT to proceed with MVP development** 🟢

---

## Next Steps

1. [ ] Define MVP scope (core features only)
2. [ ] Build Figma plugin prototype
3. [ ] Create landing page + waitlist
4. [ ] Gather 100+ waitlist signups for validation
5. [ ] Build MVP (2-3 months)
6. [ ] Beta launch with founding members
