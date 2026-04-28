# EMI Performance & Funnel Analysis Instructions

## Objective
You are required to analyze multiple reports related to EMI onboarding, agent performance, and emi user funnel behavior. The goal is to generate **detailed, data-driven insights**, identify bottlenecks, and provide **actionable recommendations** for improving both agent efficiency and product experience.

---

## Data Sources

# - Access the folder from connected google drive mcp connector. The folder will be named as: `YYYYMMDD` (current date). All the reports are in this folder.

### 1. Agent Performance Report  
**File Name:** Rupin.KYC.Agent Performance  
**Source:** Google Drive (daily files)

#### Context
- Agents call users who are stuck during the EMI application process.
- These users may be:
  - Unable to complete a step
  - Facing NADRA verification issues
- Agents guide users to complete onboarding and verification for the new wallet.

#### Report Contents
- Daily and weekly metrics:
  - Total calls made
  - Successful connects
  - Conversions (verified users)
  - Average call duration (minutes)
- A **Summary section** aggregating all days/weeks

---

## Required Analysis

### A. Overall Performance
- Total calls, connects, and conversions
- Conversion rate = conversions / connects
- Connect rate = connects / total calls
- Average handling time trends

### B. Week-on-Week (WoW) Analysis
- Compare **current week vs last week**
- Metrics to compare:
  - Calls
  - Connects
  - Conversions
  - Conversion rate
  - Connect rate
- Highlight:
  - Growth or decline (% change)
  - Performance shifts

### C. Daily Performance Comparison
- Include **daily breakdown for:**
  - Last week
  - Current week
- Identify:
  - Best-performing days
  - Weak days
  - Any unusual spikes or drops

### D. Agent-Level Analysis
- Identify:
  - Top-performing agents
  - Underperforming agents
- Compare:
  - Call volume vs conversion efficiency
  - Connect rate vs conversion rate
- Highlight consistency vs volatility

### E. Efficiency Analysis
- Are higher call volumes leading to better conversions?
- Is there an optimal call duration linked to higher conversion?
- Identify diminishing returns

### F. Actionable Insights
- Coaching opportunities
- Best practices from top performers
- Suggestions to optimize calling strategy

---

## 2. EMI Funnel Report  
**File Name:** Rupin.KYC-EMI Funnels  

#### Purpose
To analyze user drop-offs across different stages of the EMI application funnel and identify product-level issues.

#### Sheets
- New Users
- Bookkeeping Users
- Existing Wallet Users

#### Important Considerations
- Recent cohorts will naturally have lower conversions due to limited time
- Focus more on **percentages (%) rather than absolute numbers**

---

## Required Analysis

### A. Funnel Drop-off Analysis
- Stage-wise conversion rates
- Identify major drop-off points

### B. Segment Comparison
- Compare performance across:
  - New vs Bookkeeping vs Existing Wallet users

### C. Stage Efficiency
- Identify friction-heavy stages vs smooth stages

### D. Time Bias Consideration
- Adjust insights for recent cohorts

### E. Product Insights
- Identify problematic steps
- Suggest UX/product improvements

---

## 3. EMI Conversion Metrics Report  
**File Name:** EMIConversionMetrics  

#### Funnel Stages
- Not Initiated
- Abandoned
- KYC
- BVS
- Resubmit
- Post Activation

---

## Required Analysis

### A. Flow Analysis
- Track user movement across stages
- Identify loops (e.g., BVS → KYC)

### B. Stage Conversion
- Conversion rate per stage

### C. Bottlenecks
- High drop-offs
- Low forward movement
- High resubmissions

### D. Behavioral Insights
- Identify friction in verification steps

### E. Week-on-Week Trends
- Identify improvements or declines

### F. Recommendations
- Reduce friction
- Improve user guidance
- Optimize verification flow

---

## Final Output Requirements

Generate **ONE consolidated Excel file** containing:

### Sheets to Include
1. Agent Performance Summary
2. Agent WoW Comparison
3. Daily Performance (Last Week vs Current Week)
4. Agent-Level Analysis
5. Funnel Analysis (All Segments)
6. Conversion Metrics Analysis
7. Key Insights & Recommendations

---

## Output Instructions

- Use google drive mcp connector's write_file too save the Excel file in the **same Google Drive folder** from where input files were read
- The folder will be named as: `YYYYMMDD` (current date)
- Ensure the file is clearly named (e.g., `EMI_Analysis_Report.xlsx`)

---

## Additional Expectations

- Be highly analytical, not descriptive
- Focus on insights, not just numbers
- Always include:
  - Absolute numbers
  - Percentages (%)
  - Comparisons (WoW, segment-wise)
- Highlight anomalies and unexpected patterns
- Provide clear, business-focused recommendations
