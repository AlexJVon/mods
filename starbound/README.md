# Starbound: Settlement Overhaul

## Version 0.2.0 — twelve prototype tenants

This build adds role plaques and tenant definitions for all twelve requested
villagers. A plaque is a background decoration that asks a vanilla colony deed
to select its matching tenant. The NPCs inherit **ordinary vanilla villager**
behavior: their roles are labels for now. They do not yet perform jobs, have
custom dialogue or objectives, or use a settlement level system. There are no
quest chains, drone weapons, housing scores, or special rewards in this build.
This is a prototype, not the completed overhaul.

### Install (Windows / Steam)

1. Back up `Starbound\storage` before testing. Use a disposable character and
   world; NPCs and placed objects persist in saves.
2. In Steam, right-click Starbound → **Manage** → **Browse local files**. A
   common location is `C:\Program Files (x86)\Steam\steamapps\common\Starbound`.
3. Copy this repository's `starbound\settlement-overhaul` folder into the
   game's `mods` folder. Replace the older copy, rather than installing both.
4. Confirm the path is `Starbound\mods\settlement-overhaul\_metadata` and that
   `npcs`, `tenants`, and `objects` are inside the same folder. Windows must not
   add `.txt` to any file. Restart Starbound.

### Try a tenant

1. Make a small enclosed room with background walls, a door and a light. Leave
   room for a colony deed and a plaque on the background. Use a fresh room
   with no other deed or existing tenant.
2. In chat, type `/admin`, then `/spawnitem so_farmer_plaque`, then `/admin`
   to switch admin mode back off. If you were already in admin mode, don't
   toggle it twice; leave it as you found it. You also need a vanilla colony
   deed (normally bought at the Outpost; `/spawnitem colonydeed` in admin mode
   is an alternative for testing).
3. Place **one** Farmer Role Plaque on a background wall inside the room, then
   place the colony deed inside the same room. It should summon a human farmer
   tenant. The plaque sprite is the same for every role; check its item name.
4. For another role, use a separate room with one corresponding plaque and its
   own deed. Multiple role plaques in one room can match multiple tenants; the
   result is not deterministic. Other mods that change deeds or tenants may
   change selection. If you change the role in an already occupied room, remove
   the deed and use a fresh room for a reliable test.

Plaques are currently admin-spawn only, not craftable. Item IDs and intended
species:

| Role | Species | Plaque item ID |
| --- | --- | --- |
| Miner | Apex | `so_miner_plaque` |
| Surveyor | Human | `so_surveyor_plaque` |
| Trader | Avian | `so_trader_plaque` |
| Medic | Floran | `so_medic_plaque` |
| Engineer | Glitch | `so_engineer_plaque` |
| Guard | Hylotl | `so_guard_plaque` |
| Farmer | Human | `so_farmer_plaque` |
| Historian | Avian | `so_historian_plaque` |
| Pilot | Human | `so_pilot_plaque` |
| Diplomat | Floran | `so_diplomat_plaque` |
| Tamer | Avian | `so_tamer_plaque` |
| Elder | Glitch | `so_elder_plaque` |

For a quick NPC-only test instead, in admin mode use `/spawnnpc human so_farmer`.
This does not test the deed, housing or plaque. A manually spawned NPC does not
become a tenant automatically. Spawn only in a disposable test world.

### What the files do

- `_metadata` gives Starbound the mod's internal name, display name, version,
  and description.
- `npcs/so_ROLE.npctype` defines each role's NPC ID and inherits the vanilla
  villager type. The species is selected by the deed, not by this file.
- `tenants/so_ROLE.tenant` specifies the unique role tag plus light and door
  requirements, species, NPC type, priority and vanilla rent pool. The high
  priority makes the role win against ordinary tenants when its plaque is
  present; unrelated rooms have no matching role tag and are unaffected.
- `objects/settlement/roleplaques/so_ROLE_plaque.object` defines a placeable
  decoration that contributes that unique tag to a room. `plaque.png` is the
  shared original artwork, and `plaque.frames` defines its single image frame.
- `../tests/test_assets.py` is a repository-side static validation script, not a
  game asset. Run `python -m unittest discover -s starbound/tests -v` from the
  repository root. It checks JSON and role links, not Starbound behavior.

The full copy-ready content is in the individual files in this repository;
copy the folder as a whole so the image and frame file go with the text files.
JSON assets cannot contain comments; the explanations above describe their keys.

### Troubleshooting

- **Item not found:** restart the game, verify the exact mod folder structure
  and spelling, and search `Starbound\storage\starbound.log` for the item ID.
- **Deed complains about housing or no tenant arrives:** check that the room is
  enclosed, background walls have no gaps, and the door, light, plaque and deed
  are inside. Try placing the deed last in a fresh room. Check the log for
  asset errors and test without other colony/deed mods if possible.
- **Wrong tenant:** use exactly one role plaque and a new deed in a fresh room.
  Other mods can introduce competing tenant priorities or alter colony rules.
- **Crash or missing assets:** remove the mod folder, restart, and check the log.
  Restoring a backup is safer than loading a save that contains modded objects
  or NPCs without this mod installed. Avoid opening important saves while
  required mods are disabled.

Static tests pass, but the game itself is not available in this environment;
all in-game steps and compatibility with the user's mod list still need testing.
