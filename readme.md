# 🚪 OneState Packages – Porta d’Ingresso 🚪

Benvenuto nel nostro primo package per Home Assistant!
Check out our guide in English -> [ENGLISH GUIDE]
Con questo pacchetto puoi gestire tutto da un’unica card Lovelace:

- ✅ Verificare se la porta d’ingresso è aperta o chiusa  
- ⏱️ Vedere l’ultima volta che è stata aperta  
- 🔐 Controllare lo stato della serratura smart (se disponibile)  
- 🧩 Sbloccare la porta  
- 🚪 Aprire cancello e portone  
- 📩 Ricevere notifiche push e su Telegram

---

> ⚠️ **Attenzione:** questo repository contiene la **versione gratuita**.  
> Le seguenti funzionalità avanzate sono incluse solo nella **versione PRO**:
> 
> - 🔢 Tastierino numerico integrato  
> - 📸 Snapshot automatico all’apertura porta  
> - 🤖 Invio snapshot su Telegram  
> - 🔁 Feedback visivo per PIN corretto o errato  

👉 Vuoi supportarci e ottenere l’esperienza completa?  
[💖 Acquista la versione PRO su Gumroad](https://stateforge.gumroad.com/l/PackagePortaIngresso?wanted=true)



Ora mettetevi comodi e cominciamo!

---

## 🔧 Configurazione del Package

### Requisiti iniziali

1. Apri File Editor o Samba – se non li hai, li puoi trovare in “Impostazioni → Componenti Aggiuntivi”.
2. Crea una cartella chiamata `packages` nella cartella principale `/config`.
3. Apri il file `configuration.yaml` e aggiungi questa riga:

```
homeassistant:
  packages: !include_dir_named packages
```

4. Una volta fatto, vai nella cartella `packages` appena creata, scarica e inserisci il file: `package_porta.yaml`.

---

## 📦 Componenti da installare via HACS

- [Button Card](https://github.com/custom-cards/button-card)
- [Card Mod](https://github.com/thomasloven/lovelace-card-mod) 
- [Paper Buttons Row](https://github.com/jcwillox/lovelace-paper-buttons-row)
- [Multiple-entity-row](https://github.com/benct/lovelace-multiple-entity-row)
- [Hui-element](https://github.com/thomasloven/lovelace-hui-element)
- [Config Template Card](https://github.com/iantrich/config-template-card)

---

## ⚙️ Configurazione del Package

Segui alla lettera tutti i passaggi indicati qui sotto (che comunque trovi anche dentro il package):

---
## 📲 Configurazione Telegram

Per ricevere le notifiche su Telegram, è necessario configurare un **bot** e recuperare l’ID della chat.

### 🔧 Passaggi:

1. **Crea un bot**
   - Cerca su Telegram `@BotFather`
   - Scrivi `/newbot` e segui le istruzioni per creare un nuovo bot
   - Copia il **Token** che ti viene fornito (es. `123456:ABC-DEF1234ghIkl-zyx57W2v1u123ew11`)

2. **Aggiungi il bot su Home Assistant**
   - Vai in `configuration.yaml` e aggiungi:

   ```yaml
   telegram_bot:
     - platform: polling
       api_key: "TUO_TOKEN"
       allowed_chat_ids:
         - 123456789  # <-- Inserisci il tuo chat_id qui

   notify:
     - name: telegram_mio
       platform: telegram
       chat_id: 123456789

Trova il tuo Chat ID

Scrivi a @MyIDIMBot e ti darà il tuo chatID

Dopo aver modificato configuration.yaml, riavvia Home Assistant per applicare le modifiche

✅ Ora puoi usare il servizio notify.telegram_mio all'interno del package per inviare notifiche, anche con immagini o snapshot.

### 🐍 Python Scripts

- Configura Python Scripts: [LINK](https://www.home-assistant.io/integrations/python_script/)
- Scarica e inserisci all’interno della cartella `python_scripts` il file `snapshot_porta.py` <---- INCLUSO NEL PACCHETTO

---

### 🐚 Shell Command

Aggiungi questo comando shell in `configuration.yaml`:

```yaml
shell_command:
  pulisci_snapshot: "find /config/www/snapshot_porta/ -type f -name '*.jpg' -delete"
```

---

## 📁 Cartella `snapshot_porta` e `foto-pkg`

Crea la cartella `snapshot_porta` e `foto-pkg` dentro `/config/www` (usando File Editor o Samba).

Una volta create, carica le immagini nella cartella `foto-pkg` nella cartella che trovi qui su github, ci serviranno dopo per la card (`porta-aperta.png` e `porta-chiusa.png`).

---

## 🧠 Configurazione

Inserire il PIN in `secrets.yaml`:

```
pin_sblocco_porta: 1234
```
Configurazione `package_porta.yaml`: 
```
# Serratura Smart
Smart Lock: &lock lock.porta                                       # Sostituisci con l'ID della tua smart lock

# Codice di Sblocco
Codice Sblocco porta: &pin !secret pin_sblocco_porta               # Puoi anche direttamente scrivere qui il PIN al posto di `!secret pin_sblocco_porta`                           

# Sensori Porta
Sensore porta: &porta "{{ states('binary_sensor.porta')}}"         # Sostituisci con l'ID del tuo sensore porta
Sensore porta entità: &porta2 binary_sensor.porta                  # Sostituisci con l'ID del tuo sensore porta

# Telecamera
Telecamera: &camera camera.telecamera                              # Sostituisci con l'ID della tua telecamera

# Servizi Notifica
Device per notifica push: &push notify.push_roberto                # Sostituisci con l’ID del tuo dispositivo
Device per notifica telegram: &telegram notify.telegram_lotablet   # Sostituisci con l’ID del tuo bot Telegram
```

## 💳 Card

Aggiungi una **nuova scheda manuale** nella dashboard Lovelace e incolla il codice `package_porta.yaml`.

### Tipi di card disponibili

Abbiamo preferito fare 4 tipi di card in base ad ogni esigenza:

- Card con 2 pulsanti: **Portone + Cancello** apertura via `lock.unlock`
- Card con 2 pulsanti: **Portone + Cancello** apertura via `switch.toggle` 
- Card con 1 pulsante: **Portone** apertura via `lock.unlock` 
- Card con 1 pulsante: **Portone** apertura via `switch.toggle`

Sostituisci nel codice YAML i nomi, l'entità e il servizio con quelli reali del tuo dispositivo che eseguono l'azione di apertura, come da immagine:

![cancello_lock](https://github.com/OneStatePackages/ha-package-porta-ingresso/blob/main/samples/cancello_lock.gif) 
![cancello_switch](https://github.com/OneStatePackages/ha-package-porta-ingresso/blob/main/samples/cancello_switch.gif)

Assicurati che `service: lock.unlock` oppure `service: switch.toggle` siano realmente i servizi che aprono il Portone o il Cancello!

---

## 🔄 Riavvio

Ora **riavvia il server** da Impostazioni → Sistema → Controlli del server.

Se tutto è configurato correttamente, dovresti vedere una schermata simile a questa:

![sample](https://github.com/OneStatePackages/ha-package-porta-ingresso/blob/main/samples/sample.gif)

---

## ✅ Fine

Questo è tutto ragazzi, ci vediamo al prossimo package targato **OneState**!
