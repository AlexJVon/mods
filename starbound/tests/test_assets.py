"""Static checks only; these do not replace testing inside Starbound."""
import json
from pathlib import Path
import unittest

MOD = Path(__file__).resolve().parents[1] / "settlement-overhaul"
ROLES = {
    "miner": "apex", "surveyor": "human", "trader": "avian",
    "medic": "floran", "engineer": "glitch", "guard": "hylotl",
    "farmer": "human", "historian": "avian", "pilot": "human",
    "diplomat": "floran", "tamer": "avian", "elder": "glitch",
}


def load(path):
    return json.loads(path.read_text(encoding="utf-8"))


class AssetsTest(unittest.TestCase):
    def test_all_json_assets_parse(self):
        for path in MOD.rglob("*"):
            if path.is_file() and (path.suffix in {".tenant", ".npctype", ".object", ".frames"} or path.name == "_metadata"):
                with self.subTest(path=path):
                    load(path)

    def test_roles_link_together(self):
        for role, species in ROLES.items():
            with self.subTest(role=role):
                npc = load(MOD / "npcs" / f"so_{role}.npctype")
                tenant = load(MOD / "tenants" / f"so_{role}.tenant")
                plaque = load(MOD / "objects/settlement/roleplaques" / f"so_{role}_plaque.object")
                self.assertEqual(npc["type"], f"so_{role}")
                self.assertEqual(tenant["tenants"][0]["type"], npc["type"])
                self.assertEqual(tenant["tenants"][0]["species"], species)
                self.assertEqual(plaque["colonyTags"], [f"so_role_{role}"])
                self.assertEqual(tenant["colonyTagCriteria"][plaque["colonyTags"][0]], 1)
                self.assertTrue((MOD / "objects/settlement/roleplaques" / plaque["inventoryIcon"]).is_file())


if __name__ == "__main__":
    unittest.main()
