"""
Expert System for Mobile Phone Fault Diagnosis
ITCS-440 Intelligent Systems — Project 4
"""

# ── Knowledge Base: IF-THEN rules ────────────────────────────────────────────
# Each rule: { "conditions": [list of facts], "conclusion": "diagnosis" }

RULES = [
    # ── Battery / Power rules ─────────────────────────────────────────────
    {
        "id": "R1",
        "conditions": ["phone_wont_turn_on", "battery_not_charging"],
        "conclusion": "faulty_battery",
    },
    {
        "id": "R2",
        "conditions": ["phone_wont_turn_on", "battery_charging_ok"],
        "conclusion": "faulty_power_button",
    },
    {
        "id": "R3",
        "conditions": ["battery_drains_fast", "many_apps_running"],
        "conclusion": "close_background_apps",
    },
    {
        "id": "R4",
        "conditions": ["battery_drains_fast", "few_apps_running"],
        "conclusion": "replace_battery",
    },
    {
        "id": "R5",
        "conditions": ["phone_overheating", "battery_drains_fast"],
        "conclusion": "replace_battery",
    },
    # ── Screen rules ──────────────────────────────────────────────────────
    {
        "id": "R6",
        "conditions": ["screen_black", "phone_on"],
        "conclusion": "faulty_display",
    },
    {
        "id": "R7",
        "conditions": ["screen_cracked", "touch_not_responding"],
        "conclusion": "replace_screen",
    },
    {
        "id": "R8",
        "conditions": ["screen_flickering", "phone_on"],
        "conclusion": "loose_display_connector",
    },
    # ── Network / Connectivity rules ──────────────────────────────────────
    {
        "id": "R9",
        "conditions": ["no_signal", "sim_card_present"],
        "conclusion": "faulty_antenna",
    },
    {
        "id": "R10",
        "conditions": ["no_signal", "sim_card_absent"],
        "conclusion": "insert_sim_card",
    },
    {
        "id": "R11",
        "conditions": ["wifi_not_connecting", "other_devices_connect_ok"],
        "conclusion": "faulty_wifi_module",
    },
    {
        "id": "R12",
        "conditions": ["wifi_not_connecting", "other_devices_not_connecting"],
        "conclusion": "router_problem",
    },
    # ── Audio rules ───────────────────────────────────────────────────────
    {
        "id": "R13",
        "conditions": ["no_sound", "headphones_plugged_in"],
        "conclusion": "faulty_speaker",
    },
    {
        "id": "R14",
        "conditions": ["no_sound", "headphones_not_plugged_in"],
        "conclusion": "check_volume_or_mute",
    },
    {
        "id": "R15",
        "conditions": ["microphone_not_working", "calls_silent"],
        "conclusion": "faulty_microphone",
    },
    # ── Storage / Software rules ──────────────────────────────────────────
    {
        "id": "R16",
        "conditions": ["phone_slow", "storage_full"],
        "conclusion": "free_up_storage",
    },
    {
        "id": "R17",
        "conditions": ["phone_slow", "storage_ok"],
        "conclusion": "perform_factory_reset",
    },
    {
        "id": "R18",
        "conditions": ["app_keeps_crashing", "storage_ok"],
        "conclusion": "reinstall_app",
    },
    {
        "id": "R19",
        "conditions": ["app_keeps_crashing", "storage_full"],
        "conclusion": "free_up_storage",
    },
    # ── Camera rules ──────────────────────────────────────────────────────
    {
        "id": "R20",
        "conditions": ["camera_not_working", "app_crash"],
        "conclusion": "reinstall_camera_app",
    },
    {
        "id": "R21",
        "conditions": ["camera_not_working", "hardware_issue"],
        "conclusion": "faulty_camera_module",
    },
]

# ── Diagnosis descriptions ────────────────────────────────────────────────────
DESCRIPTIONS = {
    "faulty_battery":           "The battery is defective and must be replaced by a technician.",
    "faulty_power_button":      "The power button is faulty. Seek hardware repair.",
    "close_background_apps":    "Too many apps are running in the background. Close them to save battery.",
    "replace_battery":          "The battery has degraded and needs replacement.",
    "faulty_display":           "The display hardware is faulty. Professional repair required.",
    "replace_screen":           "The screen assembly (glass + digitizer) needs to be replaced.",
    "loose_display_connector":  "The display cable may be loose internally. A technician can reseat it.",
    "faulty_antenna":           "The cellular antenna is damaged. Hardware repair required.",
    "insert_sim_card":          "No SIM card detected. Insert a valid SIM card.",
    "faulty_wifi_module":       "The Wi-Fi chip is faulty. Hardware repair required.",
    "router_problem":           "The issue is with the router, not the phone. Restart the router.",
    "faulty_speaker":           "The speaker is damaged. Hardware repair required.",
    "check_volume_or_mute":     "Check that the phone is not muted and the volume is turned up.",
    "faulty_microphone":        "The microphone is faulty. Hardware repair required.",
    "free_up_storage":          "Storage is full. Delete unused files, apps, or transfer data.",
    "perform_factory_reset":    "Software corruption likely. Back up data and perform a factory reset.",
    "reinstall_app":            "The app may be corrupted. Uninstall and reinstall it.",
    "reinstall_camera_app":     "The camera app is corrupted. Clear its cache or reinstall.",
    "faulty_camera_module":     "The camera hardware is defective. Seek professional repair.",
    "phone_overheating":        "The phone is overheating. Let it cool down and avoid heavy use.",
}

# ── Symptom display labels ────────────────────────────────────────────────────
SYMPTOM_LABELS = {
    "phone_wont_turn_on":          "Phone won't turn on",
    "battery_not_charging":        "Battery is not charging",
    "battery_charging_ok":         "Battery charges normally",
    "battery_drains_fast":         "Battery drains very fast",
    "many_apps_running":           "Many apps are running in background",
    "few_apps_running":            "Few apps running (battery still drains fast)",
    "phone_overheating":           "Phone is overheating",
    "screen_black":                "Screen is completely black",
    "phone_on":                    "Phone appears to be on (light/sound present)",
    "screen_cracked":              "Screen is physically cracked",
    "touch_not_responding":        "Touchscreen is not responding",
    "screen_flickering":           "Screen is flickering",
    "no_signal":                   "No cellular signal",
    "sim_card_present":            "SIM card is inserted",
    "sim_card_absent":             "No SIM card inserted",
    "wifi_not_connecting":         "Cannot connect to Wi-Fi",
    "other_devices_connect_ok":    "Other devices connect to the same Wi-Fi fine",
    "other_devices_not_connecting":"Other devices also cannot connect to Wi-Fi",
    "no_sound":                    "No audio output from phone",
    "headphones_plugged_in":       "Headphones are plugged in",
    "headphones_not_plugged_in":   "No headphones plugged in",
    "microphone_not_working":      "Microphone is not working",
    "calls_silent":                "The other party cannot hear you during calls",
    "phone_slow":                  "Phone is running very slowly",
    "storage_full":                "Storage is full",
    "storage_ok":                  "Storage has free space",
    "app_keeps_crashing":          "An app keeps crashing",
    "camera_not_working":          "Camera is not working",
    "app_crash":                   "Camera app crashes on open",
    "hardware_issue":              "Camera hardware seems damaged (physically)",
}


# ── Inference Engine (Forward Chaining) ──────────────────────────────────────

def forward_chain(facts: set) -> list[dict]:
    """
    Apply rules until no new conclusions can be drawn.
    Returns a list of fired rules: [{"rule": rule_id, "conclusion": ..., "via": [...conditions]}]
    """
    fired = []
    changed = True

    while changed:
        changed = False
        for rule in RULES:
            conclusion = rule["conclusion"]
            if conclusion not in facts and all(c in facts for c in rule["conditions"]):
                facts.add(conclusion)
                fired.append({
                    "rule":       rule["id"],
                    "conclusion": conclusion,
                    "via":        rule["conditions"],
                })
                changed = True

    return fired


# ── CLI Interface ─────────────────────────────────────────────────────────────

def collect_symptoms() -> set:
    """Interactively ask the user about symptoms."""
    print("\n" + "=" * 60)
    print("  Mobile Phone Fault Diagnosis Expert System")
    print("=" * 60)
    print("Answer each question with  y (yes)  or  n (no).\n")

    facts = set()

    symptom_groups = [
        ("POWER & BATTERY", [
            "phone_wont_turn_on",
            "battery_not_charging",
            "battery_charging_ok",
            "battery_drains_fast",
            "many_apps_running",
            "few_apps_running",
            "phone_overheating",
        ]),
        ("SCREEN", [
            "screen_black",
            "phone_on",
            "screen_cracked",
            "touch_not_responding",
            "screen_flickering",
        ]),
        ("NETWORK", [
            "no_signal",
            "sim_card_present",
            "sim_card_absent",
            "wifi_not_connecting",
            "other_devices_connect_ok",
            "other_devices_not_connecting",
        ]),
        ("AUDIO", [
            "no_sound",
            "headphones_plugged_in",
            "headphones_not_plugged_in",
            "microphone_not_working",
            "calls_silent",
        ]),
        ("STORAGE & SOFTWARE", [
            "phone_slow",
            "storage_full",
            "storage_ok",
            "app_keeps_crashing",
        ]),
        ("CAMERA", [
            "camera_not_working",
            "app_crash",
            "hardware_issue",
        ]),
    ]

    for group_name, symptoms in symptom_groups:
        print(f"\n--- {group_name} ---")
        for symptom in symptoms:
            label = SYMPTOM_LABELS.get(symptom, symptom)
            while True:
                answer = input(f"  {label}? (y/n): ").strip().lower()
                if answer in ("y", "n"):
                    break
                print("  Please enter y or n.")
            if answer == "y":
                facts.add(symptom)

    return facts


def display_results(initial_facts: set, fired_rules: list[dict]) -> None:
    """Print the diagnosis results."""
    print("\n" + "=" * 60)
    print("  DIAGNOSIS RESULTS")
    print("=" * 60)

    diagnoses = [r for r in fired_rules if r["conclusion"] in DESCRIPTIONS]

    if not diagnoses:
        print("\nNo conclusive diagnosis could be made from the given symptoms.")
        print("Please consult a qualified technician.")
        return

    print(f"\n{len(diagnoses)} issue(s) detected:\n")

    for i, entry in enumerate(diagnoses, start=1):
        conclusion = entry["conclusion"]
        rule_id = entry["rule"]
        triggered_by = ", ".join(
            SYMPTOM_LABELS.get(c, c) for c in entry["via"]
        )
        description = DESCRIPTIONS.get(conclusion, "No description available.")
        conclusion_label = conclusion.replace("_", " ").title()

        print(f"  [{i}] {conclusion_label}  (Rule {rule_id})")
        print(f"       Triggered by: {triggered_by}")
        print(f"       Advice: {description}")
        print()

    print("=" * 60)
    print("  End of diagnosis. Consult a technician for hardware repairs.")
    print("=" * 60 + "\n")


def run_demo() -> None:
    """Run a demo with pre-set facts (no user input needed)."""
    print("\n" + "=" * 60)
    print("  DEMO MODE — Pre-set symptom scenario")
    print("=" * 60)

    demo_facts = {
        "phone_slow",
        "storage_full",
        "app_keeps_crashing",
    }

    print("\nSymptoms provided:")
    for f in demo_facts:
        print(f"  - {SYMPTOM_LABELS.get(f, f)}")

    fired = forward_chain(demo_facts.copy())
    display_results(demo_facts, fired)


def main() -> None:
    print("\nSelect mode:")
    print("  1 — Interactive (answer questions about your phone)")
    print("  2 — Demo       (pre-set symptoms, no input needed)")

    while True:
        choice = input("\nEnter 1 or 2: ").strip()
        if choice in ("1", "2"):
            break
        print("Please enter 1 or 2.")

    if choice == "2":
        run_demo()
    else:
        facts = collect_symptoms()
        fired = forward_chain(facts)
        display_results(facts, fired)


if __name__ == "__main__":
    main()
