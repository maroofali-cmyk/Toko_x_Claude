# Run Udhaar Twitter Flow

Execute the full Udhaar Book / Rupin Twitter/X community engagement session:

1. **Login to Twitter/X via Playwright MCP**
   - Navigate to x.com
   - Login with credentials from `.env`: `TWITTER_USERNAME` / `TWITTER_PASSWORD`
   - Confirm login is successful before proceeding
   - If login credentials are not set, skip to Step 2 (WebSearch mode still works)

2. **Run the Udhaar Twitter Agent workflow**s
   - Follow all instructions in `.claude/agents/udhaar-twitter-agent.md`

3. **Send output from agent to Sheheryar Izhar on Slack**
   - Use Slack MCP to find Sheheryar Izhar and send the full session report
   - Include: engagement tracker summary, all drafted replies, tweet URLs, and relevance scores

