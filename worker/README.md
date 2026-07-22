# Anderson chat Worker — deploy guide

This is the tiny backend that holds the Anthropic API key and answers the chat widget.
The static site (GitHub Pages) can't hold a secret, so this runs on Cloudflare's free tier.
One-time setup, ~10 minutes.

## What you need
- A free **Cloudflare** account (dash.cloudflare.com).
- An **Anthropic API key** with credits (console.anthropic.com → API Keys). Make a *separate* key just for this bot so it can be rotated on its own.
- Node.js (already installed on this machine).

## Steps

```bash
# 1. from this folder
cd worker
npx wrangler login            # opens a browser, approve

# 2. store the API key as a secret (paste the key when prompted; it never goes in any file)
npx wrangler secret put ANTHROPIC_API_KEY

# 3. deploy
npx wrangler deploy
```

`deploy` prints a URL like `https://anderson-chat.<your-subdomain>.workers.dev`. Copy it.

## Wire it to the site
1. Open `../chat.js`, set `WORKER_URL` to that URL (no trailing slash).
2. In `../build.py`, bump the chat.js cache-bust: `chat.js?v=1` → `chat.js?v=2`.
3. `py build.py` then `git push origin master`. The bubble goes live once `WORKER_URL` is real (until then it stays hidden).

## Recommended safety (do these)
- **Anthropic Console → set a monthly spend limit + billing alert.** This is the hard backstop: even if the endpoint is abused, the bill can't exceed the number you pick. With the dedicated key, this only caps the bot.
- **Optional per-IP rate limiting:** `npx wrangler kv namespace create RATE_KV`, paste the returned id into `wrangler.toml` (uncomment the block), `npx wrangler deploy`. Without it, the spend cap above is still your backstop.

## Notes
- Model is `claude-haiku-4-5` (cheapest, right tier for FAQ). Change `MODEL` in `worker.js` to switch.
- `ALLOWED` in `worker.js` lists the origins allowed to call it — update if the domain changes.
- The quote wizard's `/lead` endpoint posts to the same FormSubmit `info@` inbox the contact form uses (already activated). No new inbox.
- No secrets live in `worker.js`, so it's safe in the public repo.
- Cost: Cloudflare free tier covers this traffic ($0); Claude API is ~2 cents per conversation (see `../docs/AI_CHATBOT_SCOPING.md`).
