# Run Udhaar Reddit Flow

Execute the full Udhaar Book / Rupin Reddit community engagement session:

1. **Login to Reddit via Playwright MCP**
   - Navigate to reddit.com
   - Login with credentials from `.env`: `REDDIT_USERNAME` / `REDDIT_PASSWORD`
   - Confirm login is successful before proceeding

2. **Run the Udhaar Reddit Agent workflow**s
   - Follow all instructions in `.claude/agents/udhaar-reddit-agent.md`

3. **Send output from agent to Sheheryar Izhar on Slack**
   - Use Slack MCP to find Sheheryar Izhar and send the full session agent output report/

