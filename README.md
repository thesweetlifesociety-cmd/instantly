# instantly

Gestione delle campagne cold email su [Instantly](https://instantly.ai) da Claude, tramite l'API v2 di Instantly.

Questo repository accompagna il progetto Claude "Instantly": contiene le regole di lavoro per Claude (`CLAUDE.md`) e piccoli script di supporto in sola lettura.

## Requisiti

- Python 3.9+ (solo libreria standard, nessuna dipendenza)
- Una chiave API Instantly v2 del workspace Fluffy

## Configurazione

1. In Instantly: **Settings → Integrations → API Keys**, crea una chiave API v2 per il workspace Fluffy.
2. Esportala come variabile d'ambiente (in locale, oppure nelle variabili dell'environment Claude Code):

   ```bash
   export INSTANTLY_API_KEY_FLUFFY="..."
   ```

3. Se lavori da un ambiente Claude Code nel cloud, la network policy deve consentire l'host `api.instantly.ai`.

Non salvare mai la chiave in file versionati: `.env` è già in `.gitignore`.

## Script

`scripts/instantly_readonly.py` fa solo richieste GET (non modifica nulla):

```bash
python3 scripts/instantly_readonly.py campaigns   # elenca le campagne con lo stato
python3 scripts/instantly_readonly.py accounts    # elenca gli account di invio
python3 scripts/instantly_readonly.py campaigns --json   # output JSON grezzo
```

## API

- Base URL: `https://api.instantly.ai/api/v2`
- Autenticazione: header `Authorization: Bearer <chiave>`
- Documentazione: https://developer.instantly.ai/
