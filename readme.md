# 🚪 OneState Packages - Porta Ingresso - Front Door 🚪

Welcome to our first Home Assistant package!

With this package, you can control everything from a single Lovelace card:

- Check if the front door is open or closed  
- View the last time it was opened  
- Check smart lock status (if available)  
- Unlock the door  
- Open the gate and building entrance  
- Receive push and Telegram notifications

> ⚠️ Here on Github is included the **free version**.  
> The following features and configurations are available in the **PRO version**:
> - Integrated numeric keypad
> - Automatic snapshot when door opens
> - Snapshot sent to Telegram
> - Visual feedback for correct/incorrect PIN

👉 Want to support us and get the full experience?  
[💖 Get the PRO version on Gumroad](https://stateforge.gumroad.com/l/PackagePortaIngresso?wanted=true)


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

4. Go to the new `packages` folder, download and add the file `package_door.yaml`.

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
- Download and add `snapshot_door.py` into the `python_scripts` folder <---- INCLUDED IN THE PACKAGE

---

### 🐚 Shell Command

Add this shell command in `configuration.yaml`:

```yaml
shell_command:
  clean_snapshots: "find /config/www/snapshot_door/ -type f -name '*.jpg' -delete"
```

---

## 📁 `snapshot_door` and `photo-pkg` Folders

Create the folders `snapshot_door` and `photo-pkg` inside `/config/www` (use File Editor or Samba).

Once created, upload the images from the package folder `photo-pkg` (`door-opened.png` and `door-closed.png`), which will be used in the card.

---

## 🧠 Configuration

Store your PIN in `secrets.yaml`:

```
pin_unlock_door: 1234
```

Config inside `package_front_door.yaml`:
```
# Smart Lock
Smart Lock: &lock lock.door                                         # Replace with your smart lock entity ID

# Unlock PIN
Door Unlock Code: &pin !secret pin_unlock_door                      # You can also insert the PIN directly here instead
                                                                    # of using `!secret` - DEFAULT INCLUDED DIRECTLY

# Door Sensors
Door Sensor: &door "{{ states('binary_sensor.door')}}"              # Replace with your door sensor entity
Door Sensor Entity: &door2 binary_sensor.door                       # Replace with your door sensor entity

# Camera
Camera: &camera camera.door_camera                                  # Replace with your camera entity ID

# Notification Services
Push Notification Service: &push notify.push_roberto                # Replace with your device ID
Telegram Notification Service: &telegram notify.telegram_lotablet   # Replace with your Telegram bot ID
```

## 💳 Card

Add a **manual card** to your Lovelace dashboard and paste the `package_door.yaml` code.

### Available Card Types

We’ve created 4 card variations based on different needs:

- Card with 2 buttons: **Gate + Building Entrance** via `lock.unlock`
- Card with 2 buttons: **Gate + Building Entrance** via `switch.toggle` 
- Card with 1 button: **Building Entrance** via `lock.unlock` 
- Card with 1 button: **Building Entrance** via `switch.toggle`

Replace entity names and services in the YAML code with your actual devices used to open doors/gates.

![cancello_lock](https://github.com/OneStatePackages/ha-package-door-ingresso/blob/main/samples/cancello_lock.gif) 
![cancello_switch](https://github.com/OneStatePackages/ha-package-door-ingresso/blob/main/samples/cancello_switch.gif)

Make sure `service: lock.unlock` or `service: switch.toggle` are actually what opens your door or gate!

---

## 🔄 Restart

Now **restart the server** from Settings → System → Server Controls.

If everything is configured properly, you should see a screen like this:

![sample](https://github.com/OneStatePackages/ha-package-door-ingresso/blob/main/samples/sample.gif)

---

## ✅ Done

That’s it guys! See you in the next OneState package!
