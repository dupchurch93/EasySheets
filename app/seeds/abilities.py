from app.models import db, Ability


def seed_abilities():

    rage = Ability(
        name="Rage",
        description='''In battle, you fight with primal ferocity. On your turn, you can enter a rage as a bonus action.

While raging, you gain the following benefits if you aren’t wearing heavy armor:

    You have advantage on Strength checks and Strength saving throws.
    When you make a melee weapon attack using Strength, you gain a bonus to the damage roll that increases as you gain levels as a barbarian, as shown in the Rage Damage column of the Barbarian table.
    You have resistance to bludgeoning, piercing, and slashing damage.

If you are able to cast spells, you can’t cast them or concentrate on them while raging.

Your rage lasts for 1 minute. It ends early if you are knocked unconscious or if your turn ends and you haven’t attacked a hostile creature since your last turn or taken damage since then. You can also end your rage on your turn as a bonus action.

Once you have raged the number of times shown for your barbarian level in the Rages column of the Barbarian table, you must finish a long rest before you can rage again.''',
    source="1:Barbarian:any"
    )

    race_count = Ability(
        name="Rage Count: 2",
        description="Amount of times you can rage per long rest. Increases with level.",
        source="1:Barbarian:any"
    )
    rage_damage = Ability(
        name="Bonus Rage Damage: 2",
        description="Extra damage gained on melee attack while raging. Increases with level.",
        source="1:Barbarian:any"
    )

    reckless_attack = Ability(
        name="Reckless Attack",
        description="Starting at 2nd level, you can throw aside all concern for defense to attack with fierce desperation. When you make your first attack on your turn, you can decide to attack recklessly. Doing so gives you advantage on melee weapon attack rolls using Strength during this turn, but attack rolls against you have advantage until your next turn.",
        source="2:Barbarian:any"
    )

    danger_sense = Ability(
        name="Danger Sense",
        description="At 2nd level, you gain an uncanny sense of when things nearby aren't as they should be, giving you an edge when you dodge away from danger. You have advantage on Dexterity saving throws against effects that you can see, such as traps and spells. To gain this benefit, you can't be blinded, deafened, or incapacitated.",
        source="2:Barbarian:any"
    )

    frenzy = Ability(
        name="Frenzy",
        description="Starting when you choose this path at 3rd level, you can go into a frenzy when you rage. If you do so, for the duration of your rage you can make a single melee weapon attack as a bonus action on each of your turns after this one. When your rage ends, you suffer one level of exhaustion.",
        source="3:Barbarian:Path of the Berserker"
    )

    totem_spirit = Ability(
        name="Totem Spirit",
        description="At 3rd level, when you adopt this path, you choose a totem spirit and gain its feature. You must make or acquire a physical totem object – an amulet or similar adornment – that incorporates fur or feathers, claws, teeth, or bones of the totem animal. At your option, you also gain minor physical attributes that are reminiscent of your totem spirit. For example, if you have a bear totem spirit, you might be unusually hairy and thick-skinned, or if your totem is the eagle, your eyes turn bright yellow.",
        source="3:Barbarian:Path of the Totem Warrior:option:Totem Spirit"
    )

    totem_spirit_bear = Ability(
        name="Totem Spirit - Bear",
        description="Bear. While raging, you have resistance to all damage except psychic damage. The spirit of the bear makes you tough enough to stand up to any punishment.",
        source="3:Barbarian:Path of the Totem Warrior:choice:Totem Spirit"
    )

    totem_spirit_eagle = Ability(
        name="Totem Spirit - Eagle",
        description="Eagle. While you're raging and aren't wearing heavy armor, other creatures have disadvantage on opportunity attack rolls against you, and you can use the Dash action as a bonus action on your turn. The spirit of the eagle makes you into a predator who can weave through the fray with ease.",
        source="3:Barbarian:Path of the Totem Warrior:choice:Totem Spirit"
    )

    totem_spirit_elk = Ability(
        name="Totem Spirit - Elk",
        description="Elk. While you're raging and aren't wearing heavy armor, your walking speed increases by 15 feet. The spirit of the elk makes you extraordinarily swift.",
        source="3:Barbarian:Path of the Totem Warrior:choice:Totem Spirit"
    )

    totem_spirit_tiger = Ability(
        name="Totem Spirit - Tiger",
        description="Tiger. While raging, you can add 10 feet to your long jump distance and 3 feet to your high jump distance. The spirit of the tiger empowers your leaps.",
        source="3:Barbarian:Path of the Totem Warrior:choice:Totem Spirit"
    )

    totem_spirit_wolf = Ability(
        name="Totem Spirit - Wolf",
        description="Wolf. While you're raging, your friends have advantage on melee attack rolls against any creature within 5 feet of you that is hostile to you. The spirit of the wolf makes you a leader of hunters.",
        source="3:Barbarian:Path of the Totem Warrior:choice:Totem Spirit"
    )

    fighting_style = Ability(
        name="Fighting Style",
        description="You adopt a particular style of fighting as your specialty. Choose one of the following options. You can't take a Fighting Style option more than once, even if you later get to choose again.",
        source="1:Fighter:Any:option:Fighting Style"
    )

    fighting_style_archery = Ability(
        name="Fighting Style Archery",
        description="You gain a +2 bonus to attack rolls you make with ranged weapons.",
        source="1:Fighter:Any:choice:Fighting Style"
    )

    fighting_style_blind_fighting = Ability(
        name="Fighting Style Blind Fighting",
        description="Blind Fighting. You have blindsight with a range of 10 feet. Within that range, you can effectively see anything that isn't behind total cover, even if you're blinded or in darkness. Moreover, you can see an invisible creature within that range, unless the creature successfully hides from you.",
        source="1:Fighter:Any:choice:Fighting Style"
    )

    fighting_style_defense = Ability(
        name="Fighting Style Defense",
        description="While you are wearing armor, you gain a +1 bonus to AC.",
        source="1:Fighter:Any:choice:Fighting Style"
    )

    fighting_style_dueling = Ability(
        name="Fighting Style Dueling",
        description="When you are wielding a melee weapon in one hand and no other weapons, you gain a +2 bonus to damage rolls with that weapon.",
        source="1:Fighter:Any:choice:Fighting Style"
    )

    fighting_style_great_weapon_fighting = Ability(
        name="Fighting Style Great Weapon Fighting",
        description="When you roll a 1 or 2 on a damage die for an attack you make with a melee weapon that you are wielding with two hands, you can reroll the die and must use the new roll, even if the new roll is a 1 or a 2. The weapon must have the two-handed or versatile property for you to gain this benefit.",
        source="1:Fighter:Any:choice:Fighting Style"
    )

    fighting_style_interception = Ability(
        name="Fighting Style Interception",
        description="When a creature you can see hits a target, other than you, within 5 feet of you with an attack, you can use your reaction to reduce the damage the target takes by 1d10 + your proficiency bonus (to a minimum of 0 damage). You must be wielding a shield or a simple or martial weapon to use this reaction.",
        source="1:Fighter:Any:choice:Fighting Style"
    )

    fighting_style_protection = Ability(
        name="Fighting Style Protection",
        description="When a creature you can see attacks a target other than you that is within 5 feet of you, you can use your reaction to impose disadvantage on the attack roll. You must be wielding a shield.",
        source="1:Fighter:Any:choice:Fighting Style"
    )

    fighting_style_superior_technique = Ability(
        name="Fighting Style Superior Technique",
        description="You learn one maneuver of your choice from among those available to the Battle Master archetype. If a maneuver you use requires your target to make a saving throw to resist the maneuver's effects, the saving throw DC equals 8 + your proficiency bonus + your Strength or Dexterity modifier (your choice.) You gain one superiority die, which is a d6 (this die is added to any superiority dice you have from another source). This die is used to fuel your maneuvers. A superiority die is expended when you use it. You regain your expended superiority dice when you finish a short or long rest. Thrown Weapon Fighting. You can draw a weapon that has the thrown property as part of the attack you make with the weapon. In addition, when you hit with a ranged attack using a thrown weapon, you gain a +2 bonus to the damage roll.",
        source="1:Fighter:Any:choice:Fighting Style"
    )

    fighting_style_two_weapon_fighting = Ability(
        name="Fighting Style Two Weapon Fighting",
        description="When you engage in two-weapon fighting, you can add your ability modifier to the damage of the second attack.",
        source="1:Fighter:Any:choice:Fighting Style"
    )

    fighting_style_unarmed_fighting = Ability(
        name="Fighting Style Unarmed Fighting",
        description="Your unarmed strikes can deal bludgeoning damage equal to 1d6 + your Strength modifier on a hit. If you aren't wielding any weapons or a shield when you make the attack roll, the d6 becomes a d8. At the start of each of your turns, you can deal 1d4 bludgeoning damage to one creature grappled by you.",
        source="1:Fighter:Any:choice:Fighting Style"
    )

    unarmored_defense = Ability(
      name="Unarmored Defense",
      description="Beginning at 1st level, while you are wearing no armor and not wielding a shield, your AC equals 10 + your Dexterity modifier + your Wisdom modifier.",
      source="1:Monk:Any"
    )

    martial_arts = Ability(
      name="Martial Arts",
      description=''' At 1st level, your practice of martial arts gives you mastery of combat styles that use unarmed strikes and monk weapons, which are shortswords and any simple melee weapons that don’t have the two-handed or heavy property.

        You gain the following benefits while you are unarmed or wielding only monk weapons and you aren’t wearing armor or wielding a shield:

            You can use Dexterity instead of Strength for the attack and damage rolls of your unarmed strikes and monk weapons.
            You can roll a d4 in place of the normal damage of your unarmed strike or monk weapon. This die changes as you gain monk levels, as shown in the Martial Arts column of the Monk table.
            When you use the Attack action with an unarmed strike or a monk weapon on your turn, you can make one unarmed strike as a bonus action. For example, if you take the Attack action and attack with a quarterstaff, you can also make an unarmed strike as a bonus action, assuming you haven’t already taken a bonus action this turn.

        Certain monasteries use specialized forms of the monk weapons. For example, you might use a club that is two lengths of wood connected by a short chain (called a nunchaku) or a sickle with a shorter, straighter blade (called a kama). Whatever name you use for a monk weapon, you can use the game statistics provided for the weapon in the Weapons section.''',
      source="1:Monk:Any"
    )

    expertise = Ability(
        name="Expertise",
        description='''At 1st level, choose two of your skill proficiencies, or one of your skill proficiencies and your proficiency with thieves’ tools. Your proficiency bonus is doubled for any ability check you make that uses either of the chosen proficiencies.

    At 6th level, you can choose two more of your proficiencies (in skills or with thieves’ tools) to gain this benefit.''',
        source="1:Rogue:Any"
    )

    sneak_attack = Ability(
        name="Sneak Attack",
        description='''Beginning at 1st level, you know how to strike subtly and exploit a foe’s distraction. Once per turn, you can deal an extra 1d6 damage to one creature you hit with an attack if you have advantage on the attack roll. The attack must use a finesse or a ranged weapon.

        You don’t need advantage on the attack roll if another enemy of the target is within 5 feet of it, that enemy isn’t incapacitated, and you don’t have disadvantage on the attack roll. Increases with level.''',
        source="1:Rogue:Any"
    )

    thieves_cant = Ability(
        name="Thieves Cant",
        description='''During your rogue training you learned thieves’ cant, a secret mix of dialect, jargon, and code that allows you to hide messages in seemingly normal conversation. Only another creature that knows thieves’ cant understands such messages. It takes four times longer to convey such a message than it does to speak the same idea plainly.

        In addition, you understand a set of secret signs and symbols used to convey short, simple messages, such as whether an area is dangerous or the territory of a thieves’ guild, whether loot is nearby, or whether the people in an area are easy marks or will provide a safe house for thieves on the run.''',
        source="1:Rogue:Any"
    )

    db.session.add_all([rage, race_count, rage_damage, danger_sense, frenzy,
                        reckless_attack, totem_spirit, totem_spirit_bear,
                        totem_spirit_tiger, totem_spirit_wolf,
                        totem_spirit_eagle, totem_spirit_elk,
                        fighting_style, fighting_style_archery,
                        fighting_style_blind_fighting, fighting_style_defense,
                        fighting_style_dueling,
                        fighting_style_great_weapon_fighting,
                        fighting_style_interception, fighting_style_protection,
                        fighting_style_superior_technique,
                        fighting_style_unarmed_fighting,
                        fighting_style_two_weapon_fighting, unarmored_defense,
                        martial_arts, expertise, sneak_attack, thieves_cant])
    db.session.commit()


def undo_abilities():
    db.session.execute('TRUNCATE abilities;')
    db.session.commit()
