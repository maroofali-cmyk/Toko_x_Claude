# Run Udhaar Quora Flow

Execute the full Udhaar Book / Rupin Quora community engagement session:

1. **Login to Quora via Playwright MCP**
   - Navigate to quora.com
   - Login with credentials from `.env`: `QUORA_EMAIL` / `QUORA_PASSWORD`
   - Confirm login is successful before proceeding

2. **Run the Udhaar Quora Agent workflow**
   - Follow all instructions in `.claude/agents/udhaar-quora-agent.md`
   - Run all search queries from the agent's workflow (Step 1)
   - Use Playwright to fetch each Quora question page (bypasses 403 for logged-in users)
   - Score each question using the agent's rubric (Step 2)
   - Draft answers only for questions scoring 50+ (Step 3)
   - Include 2–3 goodwill answers with no brand mention

3. **Send output to Sheheryar Izhar on Slack**
   - Use Slack MCP to find Sheheryar Izhar and send the full session report
   - Include: karma tracker summary, all drafts, thread URLs, and relevance scores
