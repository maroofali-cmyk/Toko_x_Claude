# store_strategies_locally

Analyze the current conversation, extract strategic insights, categorize them automatically, and store in organized markdown files.

## Instructions

When this command is invoked:

1. **Analyze the conversation** - Review the entire conversation history for strategic discussions
2. **Extract strategies** - Identify all strategic insights, recommendations, plans, approaches, and ideas
3. **Auto-categorize** - Classify each strategy into one of these categories:
   - **business/** - Revenue models, partnerships, market expansion, growth tactics
   - **marketing/** - Campaigns, content plans, social media, customer acquisition
   - **technical/** - Architecture, tech stack, implementation approaches, performance
   - **seo/** - Keywords, content optimization, technical SEO, rankings
   - **product/** - Features, roadmaps, positioning, UX improvements
   - **operations/** - Logistics, support, processes, vendor management

4. **Format each strategy** as a markdown file with this structure:
```markdown
# [Strategy Title]

**Date:** YYYY-MM-DD HH:MM:SS
**Category:** [Category]
**Status:** Proposed
**Priority:** [High/Medium/Low]

## Summary
[2-3 sentence concise summary]

## Key Initiatives
1. [Action item 1]
2. [Action item 2]
3. [Action item 3]

## Expected Impact
- [Outcome 1]
- [Outcome 2]

## Implementation Steps
- [ ] Step 1
- [ ] Step 2
- [ ] Step 3

## Context
**Trigger:** [What prompted this strategy]
**Discussion:** [Brief conversation reference]

## Success Metrics
- [How to measure success]
```

5. **File naming**: Use format `YYYY-MM-DD_descriptive-slug.md`
   - Example: `2026-01-07_whatsapp-automation-strategy.md`

6. **Store files** in `.strategies/[category]/` directories
   - Create directory structure if it doesn't exist
   - Example path: `.strategies/marketing/2026-01-07_tiktok-campaign.md`

7. **Update master index** at `.strategies/index.md`:
   - Add new strategies to category sections
   - Update statistics (total count per category)
   - Add to "Recent Additions" section

8. **Provide summary** to user:
```
✓ Strategy Storage Complete

Stored X strategies:

Business (1):
  • Strategy title here

Marketing (2):
  • Strategy title 1
  • Strategy title 2

All strategies saved to: .strategies/
Master index: .strategies/index.md
```

## Output Directory Structure

```
.strategies/
├── index.md                    # Master index (auto-updated)
├── business/
├── marketing/
├── technical/
├── seo/
├── product/
└── operations/
```

## Tips for AI Processing

- Be thorough - extract ALL strategies, not just major ones
- Be concise - each strategy file should be scannable in 30 seconds
- Be actionable - focus on WHAT to do and WHY
- Avoid duplicates - check existing files before creating new ones
- Context matters - this is for saddar.com.pk (Pakistani wholesale e-commerce)
- If conversation has no clear strategies, still create a "conversation-insights" file

---

**Project:** saddar.com.pk
**Created:** 2026-01-07
