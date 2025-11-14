# Clickjacking Lab (Edge, WSL, Dockerized)

## Setup
1. Use WSL.  
2. `cd` to the repo.  
3. Run `docker-compose up`  

## Access
- Attacker/demo site (decoy): `http://127.0.0.1:4000`  
- Vulnerable/test site: `http://127.0.0.1:5000`

> Note: Use numeric loopback IP (`127.0.0.1`) so origin and session cookie behavior remain consistent.

## Scenario
After signing into the vulnerable app (http://127.0.0.1:5000), the user’s session cookie gets stored in their browser. Later, they visit the attacker’s site (http://127.0.0.1:4000), which silently loads the vulnerable site inside a hidden iframe. The page shows a fake UI and when the user clicks the visible buttons, those clicks reach the hidden app and cause unintended actions.

## Notes
- This lab was developed using **Microsoft Edge** on a **14-inch screen**.  
- For the best demo experience, use the same setup.  
- If you use a different browser or screen size, you may need to adjust the UI or iframe alignment manually.
