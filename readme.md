## 💲[BUY ME](https://stateforge.gumroad.com/l/PackagePortaIngresso?_gl=1*55npor*_ga*NjQxMDYzMS4xNzQ0NzE0NzIw*_ga_6LJN6D94N6*MTc0NDcxNDcxOS4xLjEuMTc0NDcxNTkzNi4wLjAuMA)💲 Support us with a small donation for our work and get access to the full package 🩷

# 🚪 OneState Packages - Front Door 🚪

Welcome to the guide for our first package, where you can manage everything through a single card with the following features:

- Know if the front door is open or closed  
- See the last time it was opened  
- Get the status of the smart lock (if available)  
- Set a PIN to unlock the door  
- View the latest snapshot (a camera takes a picture when the door opens)  
- Open the gate and main door  
- Receive push and Telegram notifications  

Now sit back and let's get started!

---

## 🔧 Package Setup

### Initial Requirements

1. Open File Editor or Samba – if you don’t have them, install from “Settings → Add-ons”.
2. Create a folder named `packages` in the `/config` directory.
3. Open `configuration.yaml` and add this line:

```
homeassistant:
  packages: !include_dir_named packages
```

4. Go to the new `packages` folder, download and add the file `package_porta.yaml`.

---

## 📦 Components to install via HACS

- [Button Card](https://github.com/custom-cards/button-card)
- [Card Mod](https://github.com/thomasloven/lovelace-card-mod) 
- [Paper Buttons Row](https://github.com/jcwillox/lovelace-paper-buttons-row)
- [Multiple-entity-row](https://github.com/benct/lovelace-multiple-entity-row)
- [Hui-element](https://github.com/thomasloven/lovelace-hui-element)
- [Config Template Card](https://github.com/iantrich/config-template-card)

---

## ⚙️ Package Configuration

Follow all the steps below (they are also included in the package):

---

### 🐍 Python Scripts

- Setup Python Scripts: [LINK](https://www.home-assistant.io/integrations/python_script/)
- Download and add `snapshot_porta.py` into the `python_scripts` folder <---- INCLUDED IN THE PACKAGE

---

### 🐚 Shell Command

Add this shell command in `configuration.yaml`:

```yaml
shell_command:
  pulisci_snapshot: "find /config/www/snapshot_porta/ -type f -name '*.jpg' -delete"
```

---

## 📁 `snapshot_porta` and `foto-pkg` Folders

Create the folders `snapshot_porta` and `foto-pkg` inside `/config/www` (use File Editor or Samba).

Once created, upload the images from the GitHub folder into `foto-pkg` (`porta-aperta.png` and `porta-chiusa.png`), which will be used in the card.

---

## 🧠 Configuration

Insert your PIN in `secrets.yaml`:

```
pin_sblocco_porta: 1234
```

Config inside `package_porta.yaml`:
```
# Smart Lock
Smart Lock: &lock lock.porta                                       # Replace with your smart lock entity ID

# Unlock PIN
Door Unlock Code: &pin !secret pin_sblocco_porta                   # You can also insert the PIN directly here instead of using `!secret`

# Door Sensors
Door Sensor: &porta "{{ states('binary_sensor.porta')}}"           # Replace with your door sensor entity
Door Sensor Entity: &porta2 binary_sensor.porta                    # Replace with your door sensor entity

# Camera
Camera: &camera camera.TELECAMERA                                  # Replace with your camera entity ID

# Notification Services
Push Notification Device: &push notify.push_roberto                # Replace with your device ID
Telegram Notification Device: &telegram notify.telegram_lotablet   # Replace with your Telegram bot ID
```

## 💳 Card

Add a **manual card** to your Lovelace dashboard and paste the `package_porta.yaml` code.

### Available Card Types

We’ve created 4 card variations based on different needs:

- Card with 2 buttons: **Main Door + Gate** via `lock.unlock`
- Card with 2 buttons: **Main Door + Gate** via `switch.toggle` 
- Card with 1 button: **Main Door** via `lock.unlock` 
- Card with 1 button: **Main Door** via `switch.toggle`

Replace entity names and services in the YAML code with your actual devices used to open doors/gates.

![cancello_lock](https://github.com/OneStatePackages/ha-package-porta-ingresso/blob/main/samples/cancello_lock.gif) 
![cancello_switch](https://github.com/OneStatePackages/ha-package-porta-ingresso/blob/main/samples/cancello_switch.gif)

Make sure `service: lock.unlock` or `service: switch.toggle` are actually what opens your door or gate!

---

## 🔄 Restart

Now **restart the server** from Settings → System → Server Controls.

If everything is configured properly, you should see a screen like this:

![sample](https://github.com/OneStatePackages/ha-package-porta-ingresso/blob/main/samples/sample.gif)

---

## ✅ Done

That’s it guys! See you in the next OneState package!
