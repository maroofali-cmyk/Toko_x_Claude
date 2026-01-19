# Saddar AI Agents

A comprehensive collection of specialized AI agents designed to accelerate development and growth of **Saddar** (www.saddar.com.pk) - Pakistan's leading wholesale e-commerce platform. Each agent is an expert in their domain, ready to be invoked when their expertise is needed.

## About Saddar

**Saddar** brings Pakistan's famous Saddar Bazaar online, connecting retailers and businesses with verified wholesale suppliers. Our platform offers 10,000+ products across mobile accessories, electronics, fashion, and more—with up to 30% lower prices than retail and nationwide 3-day delivery.

**Tagline:** "Buy bulk, earn more!"

## Quick Start

Agents are automatically available in Claude Code. Simply describe your task and the appropriate agent will be triggered. You can also explicitly request an agent by mentioning their name.

### Example Usage for Saddar Development
- "Create a product listing page for mobile accessories" → `rapid-prototyper` + `frontend-developer`
- "Design the checkout flow with JazzCash integration" → `backend-architect` + `ui-designer`
- "Write product descriptions for wholesale earphones" → `content-creator`
- "Set up WhatsApp order notifications" → `whatsapp-community-salesman`
- "Optimize the homepage for Pakistani retailers" → `ux-researcher` + `performance-benchmarker`

## Directory Structure

All agents are located in `.claude/agents/` directory (flat structure):

```
.claude/agents/
├── ai-engineer.md
├── analytics-reporter.md
├── api-tester.md
├── app-store-optimizer.md
├── aso-competitor-agent.md
├── backend-architect.md
├── brand-guardian.md
├── content-creator.md
├── devops-automator.md
├── email-sender.md
├── feedback-synthesizer.md
├── finance-tracker.md
├── frontend-developer.md
├── growth-hacker.md
├── infrastructure-maintainer.md
├── instagram-curator.md
├── joker.md
├── legal-compliance-checker.md
├── md-to-pdf-converter.md
├── mobile-app-builder.md
├── performance-benchmarker.md
├── rapid-prototyper.md
├── rebrand-strategist.md
├── reddit-community-builder.md
├── seo-specialist.md
├── studio-coach.md
├── support-responder.md
├── test-results-analyzer.md
├── test-writer-fixer.md
├── tiktok-strategist.md
├── tool-evaluator.md
├── trend-researcher.md
├── twitter-engager.md
├── ui-designer.md
├── ux-researcher.md
├── visual-storyteller.md
├── whimsy-injector.md
└── workflow-optimizer.md
```

## Complete Agent List

### Engineering Department
- **rapid-prototyper** - Build Saddar features and MVPs in days, not weeks
- **backend-architect** - Design scalable APIs for wholesale e-commerce
- **frontend-developer** - Build responsive, mobile-first interfaces
- **mobile-app-builder** - Create native iOS/Android apps for Saddar
- **ai-engineer** - Integrate AI features (product recommendations, search)
- **devops-automator** - Deploy and scale Saddar infrastructure
- **test-writer-fixer** - Write tests and fix bugs

### Design Department
- **ui-designer** - Design e-commerce interfaces for Pakistani retailers
- **ux-researcher** - Optimize user experience for wholesale buyers
- **brand-guardian** - Maintain Saddar's visual identity
- **visual-storyteller** - Create product visuals and marketing assets
- **whimsy-injector** - Add delightful micro-interactions

### Marketing Department
- **growth-hacker** - Drive retailer acquisition and viral growth
- **content-creator** - Create B2B content for wholesale market
- **rebrand-strategist** - Complete brand transformation strategy (Udhaar Book → Rupin rebrand specialist)
- **aso-competitor-agent** - ASO competitor analysis, keyword hijacking, Play Store growth (UdhaarBook/Rupin specialist)
- **app-store-optimizer** - General app store optimization and ASO best practices
- **tiktok-strategist** - TikTok marketing for Pakistan market
- **twitter-engager** - Twitter/X engagement and trends
- **instagram-curator** - Instagram content and shopping features
- **reddit-community-builder** - Community engagement on Reddit
- **whatsapp-community-salesman** - WhatsApp marketing and sales (critical for Pakistan)

### Product Department
- **trend-researcher** - Identify trending products and market opportunities
- **feedback-synthesizer** - Transform retailer feedback into features
- **sprint-prioritizer** - Prioritize features for 6-day sprints

### Project Management
- **project-shipper** - Launch coordination and release management
- **studio-producer** - Keep development momentum
- **experiment-tracker** - A/B testing and feature validation

### Studio Operations
- **analytics-reporter** - Sales analytics, user behavior insights
- **finance-tracker** - Revenue tracking, profitability analysis
- **infrastructure-maintainer** - Server scaling, performance optimization
- **legal-compliance-checker** - Pakistan e-commerce regulations, privacy laws
- **support-responder** - Customer support optimization

### Testing & QA
- **api-tester** - Test payment APIs, inventory APIs under load
- **performance-benchmarker** - Page speed, checkout flow optimization
- **test-results-analyzer** - Identify patterns in test failures
- **tool-evaluator** - Evaluate e-commerce tools and integrations
- **workflow-optimizer** - Optimize order fulfillment and operations

### Bonus
- **studio-coach** - Coordinate multi-agent tasks
- **joker** - Lighten the mood

## Proactive Agents

Some agents trigger automatically in specific contexts:
- **studio-coach** - When complex multi-agent tasks begin or agents need guidance
- **test-writer-fixer** - After implementing features, fixing bugs, or modifying code
- **whimsy-injector** - After UI/UX changes
- **experiment-tracker** - When feature flags are added

## Saddar-Specific Considerations

### Pakistan Market Focus
- Support for Pakistani Rupee (PKR) in all pricing
- Local payment gateways (JazzCash, Easypaisa, bank transfers)
- Cash on Delivery (COD) - critical for Pakistan market
- Urdu language support consideration
- WhatsApp integration for customer communication
- Mobile-first design (high mobile usage in Pakistan)

### Key E-commerce Features
- Product catalog and inventory management
- Shopping cart and checkout flow
- Order management system
- Customer accounts and profiles
- Payment gateway integration (JazzCash, Easypaisa, COD)
- Shipping and delivery tracking (TCS, Leopards)
- Reviews and ratings
- Search and filtering
- Wishlist functionality
- Promotional campaigns and discounts

### Target Audience
- Retail shop owners
- Wholesalers looking for suppliers
- Small business owners and entrepreneurs
- Daraz/OLX/Instagram resellers
- Bulk buyers for personal use

### Product Categories
- Mobile Accessories (chargers, earphones, power banks, cases)
- Electronics (smartphones, smartwatches, tablets, speakers)
- Fashion & Clothing
- Home Appliances
- Beauty Products
- Gifts & Essentials
- Vaping Products

## Best Practices

1. **Let agents work together** - Many tasks benefit from multiple agents
2. **Be specific** - Clear task descriptions help agents perform better
3. **Trust the expertise** - Agents are designed for their specific domains
4. **Iterate quickly** - Agents support the 6-day sprint philosophy
5. **Think Pakistan-first** - Always consider local market needs

## Technical Details

### Agent Structure
Each agent includes:
- **name**: Unique identifier
- **description**: When to use the agent with examples
- **color**: Visual identification
- **tools**: Specific tools the agent can access
- **System prompt**: Detailed expertise and instructions

### Recommended Tech Stack for Saddar
- **Frontend**: Next.js with Tailwind CSS (mobile-first)
- **Backend**: Node.js or Python
- **Database**: PostgreSQL / MongoDB
- **Payments**: JazzCash, Easypaisa, COD integration
- **Hosting**: AWS / Vercel
- **Analytics**: Google Analytics 4, Mixpanel

## Status

- ✅ **Active**: Fully functional and tested
- 🚧 **Coming Soon**: In development
- 🧪 **Beta**: Testing with limited functionality

## Contributing

To improve existing agents or suggest new ones:
1. Follow the existing format with YAML frontmatter
2. Include 3-4 detailed usage examples relevant to Saddar
3. Write comprehensive system prompt (500+ words)
4. Test the agent with real Saddar development tasks
