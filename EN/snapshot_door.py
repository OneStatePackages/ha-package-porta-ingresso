snapshot_time = hass.states.get("input_datetime.ora_snapshot").state
snapshot_time = snapshot_time.replace("-", "").replace(":", "").replace(" ", "_")

filename = "/config/www/snapshot_door/snapshot_" + snapshot_time + ".jpg"
web_path = "/local/snapshot_door/snapshot_" + snapshot_time + ".jpg"

entity_id = data.get("entity_id")

if entity_id is not None:
    hass.services.call("camera", "snapshot", {
        "entity_id": entity_id,
        "filename": filename
    })

    hass.services.call("input_text", "set_value", {
        "entity_id": "input_text.snapshot_path_telegram",
        "value": filename
    })

    hass.services.call("input_text", "set_value", {
        "entity_id": "input_text.snapshot_path_frontend",
        "value": web_path
    })
