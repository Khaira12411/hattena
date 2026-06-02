from constants.straydex import SD_EMOJIS

class SD_TR_DESC:
    tref = f"""# TRAINERS: EV FAQs
    **What are EVs?**
    > When battling, pokemon gain effort values (EVs).
    > These stats help increase your pokemon stats (HP, ATTACK, DEFENSE, SPECIAL ATTACK, SPECIAL DEFENSE, SPEED).

    **What is the maximum amount of EVs I can obtain?**
    > Total EVs across all stats max out at 510.
    > Individual EV stats max out at 252. At level 100, every 4 EVs obtained in a stat translates to 1 point for that stat, meaning you can increase a level 100 Pokemon's stat by a maximum 63 points (252 EV)

    **How do I increase my EV training rate over 3 per mon?**
    > Power items are from `;factions shop`.
    > Per change log, if held by a Pokemon, it grants that Pokemon 8 extra EVs in the respective stat regardless of any condition
    - {SD_EMOJIS.powerweight} Power Weight - Gives HP bonus by 8
    - {SD_EMOJIS.powerbracer} Power Bracer - Gives ATTACK bonus by 8
    - {SD_EMOJIS.powerbelt} Power Belt - Gives DEFENSE bonus by 8
    - {SD_EMOJIS.powerlens} Power Lens - Gives SPECIAL ATTACK bonus by 8
    - {SD_EMOJIS.powerband} Power Band - Gives SPECIAL DEFENSE bonus by 8
    - {SD_EMOJIS.poweranklet} Power Anklet - Gives SPEED EV bonus by 8

    **How do I decrease my EVs?**
    > Berry items are from the `;factions shop`.
    > Per the change log, each berry reduces the EV by 10.
    > If your EV is above 100, the first berry will reduce the EV to 100, and then by 10 thereafter.
    > Overall, you'd need to use at most 11 of a berry to set the respective EV to 0.
    > Command to use them is `;bud eat name_berry amount`
    - {SD_EMOJIS.pomegberry} Pomeg Berry - Reduces HP EV by 10
    - {SD_EMOJIS.kelpsyberry} Kelpsy Berry - Reduces ATTACK EV by 10
    - {SD_EMOJIS.qualotberry} Qualot Berry - Reduces DEFENSE EV by 10
    - {SD_EMOJIS.hondewberry} Hondew Berry - Reduces  SPECIAL ATTACK EV by 10
    - {SD_EMOJIS.grepaberry} Grepa Berry - Reduces SPECIAL DEFENSE EV by 10
    - {SD_EMOJIS.tamatoberry} Tamato Berry - Reduces SPEED EV by 10"""
