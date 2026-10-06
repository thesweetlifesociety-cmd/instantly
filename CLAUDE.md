# Regole del progetto Instantly

Questo progetto serve a gestire le campagne cold email di Instantly da Claude, tramite l'API v2 (`https://api.instantly.ai/api/v2`, autenticazione Bearer).

## Regole fisse

- Lavora **solo** sul workspace Instantly di Fluffy.
- Non mostrare, elencare, analizzare né modificare **mai** campagne, lead o account di qualsiasi altro workspace.
- Usa solo la chiave nella variabile `INSTANTLY_API_KEY_FLUFFY`. **Non usare** `INSTANTLY_API_KEY`: punta a un altro workspace.
- Se `INSTANTLY_API_KEY_FLUFFY` non è disponibile, dillo all'utente invece di ripiegare su un'altra chiave.
- Non creare, modificare, avviare, mettere in pausa o inviare campagne (né aggiungere/rimuovere lead) senza una richiesta esplicita dell'utente.
- Non scrivere mai chiavi API in file, commit, log o memoria. Il repository è pubblico.
- Rispondi in italiano.

## Note tecniche

- Paginazione v2: parametri `limit` e `starting_after`; la risposta contiene `items` e `next_starting_after`.
- Stati campagna: `0` bozza, `1` attiva, `2` in pausa, `3` completata, `4` subsequence in corso, `-1` account non sani, `-2` bounce protection, `-99` sospesa.
- Per letture veloci usa `scripts/instantly_readonly.py`.
