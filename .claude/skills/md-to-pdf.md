# MD to PDF Converter Skill

Convert any markdown file to PDF format using automated browser conversion or local tools.

## Usage

```
/md-to-pdf <file.md> [output.pdf]
```

## Examples

```
/md-to-pdf CLAUDE.md
/md-to-pdf docs/README.md output/readme.pdf
/md-to-pdf .claude/agents/marketing/email-sender.md
```

## What it does

This skill will:
1. Verify the markdown file exists
2. Use the md-to-pdf-converter agent to convert it
3. Save the PDF in the same directory (or specified location)
4. Report the conversion results with file size

## Agent

This skill invokes the `md-to-pdf-converter` agent located at:
`.claude/agents/utilities/md-to-pdf-converter.md`

The agent uses browser automation (Playwright/Puppeteer) to convert files via CloudConvert, with fallback to local tools like pandoc or markdown-pdf if needed.

## Requirements

The agent will automatically install dependencies if needed:
- Node.js (for Playwright/Puppeteer approach)
- OR Python with markdown-pdf (fallback approach)
- OR pandoc (alternative fallback)
