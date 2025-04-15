## 💲[BUY ME](https://stateforge.gumroad.com/l/PackagePortaIngresso?_gl=1*55npor*_ga*NjQxMDYzMS4xNzQ0NzE0NzIw*_ga_6LJN6D94N6*MTc0NDcxNDcxOS4xLjEuMTc0NDcxNTkzNi4wLjAuMA)💲


# 🚪 OneState Packages - Porta d'Ingresso 🚪

Benvenuti in questa guida del nostro primo package, dove avete la possibilità, tramite una sola card, di avere i seguenti servizi:

- Possibilità di sapere se la porta d'ingresso è aperta o chiusa  
- Ultima volta che è stata aperta  
- Possibilità di conoscere lo stato della serratura (se si possiede una serratura smart)  
- Possibilità di impostare un PIN per l'apertura della porta  
- Visualizzare l’ultimo snapshot (dal momento in cui viene aperta la porta, una telecamera scatta una foto)  
- Possibilità di aprire il portone e il cancello  
- Possibilità di ricevere notifiche push e tramite Telegram  

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

4. Una volta fatto, vai nella cartella `packages` appena creata, scarica e inserisci il file: [package_porta.yaml](https://github.com/OneStatePackages/ha-package-porta-ingresso/blob/main/package_porta.yaml)`.

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

### 🐍 Python Scripts

- Configura Python Scripts: [LINK](https://www.home-assistant.io/integrations/python_script/)
- Scarica e inserisci all’interno della cartella `python_scripts` il file [snapshot_porta.py](https://github.com/OneStatePackages/ha-package-porta-ingresso/blob/main/snapshot_porta.py)

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
Configurazione [package_porta.yaml](https://github.com/OneStatePackages/ha-package-porta-ingresso/blob/main/package_porta.yaml)`:
```
# Serratura Smart
Smart Lock: &lock lock.porta                                       # Sostituisci con l'ID della tua smart lock

# Codice di Sblocco
Codice Sblocco porta: &pin !secret pin_sblocco_porta               # Puoi anche direttamente scrivere qui il PIN al posto di `!secret pin_sblocco_porta`                           

# Sensori Porta
Sensore porta: &porta "{{ states('binary_sensor.porta')}}"         # Sostituisci con l'ID del tuo sensore porta
Sensore porta entità: &porta2 binary_sensor.porta                  # Sostituisci con l'ID del tuo sensore porta

# Telecamera
Telecamera: &camera camera.TELECAMERA                              # Sostituisci con l'ID della tua telecamera

# Servizi Notifica
Device per notifica push: &push notify.push_roberto                # Sostituisci con l’ID del tuo dispositivo
Device per notifica telegram: &telegram notify.telegram_lotablet   # Sostituisci con l’ID del tuo bot Telegram
```

## 💳 Card

Aggiungi una **nuova scheda manuale** nella dashboard Lovelace e incolla il codice `package_porta.yaml`.

### Tipi di card disponibili

Abbiamo preferito fare 4 tipi di card in base ad ogni esigenza:

- Card con 2 pulsanti: **Portone + Cancello** apertura via `lock.unlock` → [card](https://github.com/OneStatePackages/ha-package-porta-ingresso/blob/main/cards/package_porta_2_pulsanti_cancello_portone_lock_card.yaml)  
- Card con 2 pulsanti: **Portone + Cancello** apertura via `switch.toggle` → [card](https://github.com/OneStatePackages/ha-package-porta-ingresso/blob/main/cards/package_porta_2_pulsanti_cancello_portone_switch_card.yaml)  
- Card con 1 pulsante: **Portone** apertura via `lock.unlock` → [card](https://github.com/OneStatePackages/ha-package-porta-ingresso/blob/main/cards/package_porta_1_pulsante_portone_lock_card.yaml)  
- Card con 1 pulsante: **Portone** apertura via `switch.toggle` → [card](https://github.com/OneStatePackages/ha-package-porta-ingresso/blob/main/cards/package_porta_2_pulsanti_cancello_portone_switch_card.yaml)

Sostituisci nel codice YAML i nomi, l' entità e il servizio con quelle reali del tuo dispositivo che eseguono l'azione di apertura, come da immagine:

![cancello_lock](https://github.com/OneStatePackages/ha-package-porta-ingresso/blob/main/cards/cancello_lock.gif)

Assicurarsi che `service: lock.unlock` oppure `service: switch.toggle` siano realmente i servizi che aprono il Portone o il Cancello!
---

## 🔄 Riavvio

Ora **riavvia il server** da Impostazioni → Sistema → Controlli del server.

Se tutto è configurato correttamente, dovresti vedere una schermata simile a questa:

![sample](https://github.com/OneStatePackages/ha-package-porta-ingresso/blob/main/cards/sample.gif)

---

## ✅ Fine

Questo è tutto ragazzi, ci vediamo al prossimo package targato **OneState**!
