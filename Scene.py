scene_list: list[str] = [
'Deku Tree',
'Dodongos Cavern',
'Jabu Jabus Belly',
'Forest Temple',
'Fire Temple',
'Water Temple',
'Spirit Temple',
'Shadow Temple',
'Bottom of the Well',
'Ice Cavern',
'Ganons Tower',
'Gerudo Training Ground',
'Thieves Hideout',
'Ganons Castle',
'',
'',
'Market Treasure Chest Game',
'Deku Tree Boss',
'Dodongos Cavern Boss',
'Jabu Jabus Belly Boss',
'Forest Temple Boss',
'Fire Temple Boss',
'Water Temple Boss',
'Spirit Temple Boss',
'Shadow Temple Boss',
'Ganondorf Boss Room',
'',
'Market Entrance (Child Day)',
'Market Entrance (Child Night)',
'Market Entrance (Adult)',
'Back Alley (Child Day)',
'Back Alley (Child Night)',
'Market (Child Day)',
'Market (Child Night)',
'Market (Adult)',
'ToT Entrance (Child Day)',
'ToT Entrance (Child Night)',
'ToT Entrance (Adult)',
'KF Know it All House',
'KF House of Twins',
'KF Midos House',
'KF Sarias House',
'Kak Carpenter Boss House',
'Market Man in Green House',
'Kak Bazaar',
'KF Kokiri Shop',
'GC Shop',
'ZD Shop',
'Kak Potion Shop',
'Market Potion Shop',
'Market Bombchu Shop',
'Market Mask Shop',
'KF Links House',
'Market Dog Lady House',
'LLR Stables',
'Kak Impas House',
'LH Lab',
'GV Carpenter Tent',
'Graveyard Dampes House',
'',
'',
'',
'Grottos',
'Graveyard Heart Piece Grave',
'',
'Graveyard Royal Familys Tomb',
'',
'Temple of Time',
'',
'',
'',
'',
'Windmill and Dampes Grave',
'LH Fishing Hole',
'Castle Courtyard',
'Market Bombchu Bowling',
'LLR Tower',
'Market Guard House',
'',
'',
'',
'Hyrule Field',
'Kakariko Village',
'Graveyard',
'Zoras River',
'Kokiri Forest',
'Sacred Forest Meadow',
'Lake Hylia',
'Zoras Domain',
'Zoras Fountain',
'Gerudo Valley',
'Lost Woods',
'Desert Colossus',
'Gerudo Fortress',
'Haunted Wasteland',
'Hyrule Castle',
'Death Mountain',
'Death Mountain Crater',
'Goron City',
'Lon Lon Ranch',
'',
]

grotto_scenes: dict[str,str] = {
     'SFM Wolfos Grotto': 'Sacred Forest Meadow',
     'HF Cow Grotto': 'Hyrule Field',
     'HF Near Kak Grotto': 'Hyrule Field',
     'HF Tektite Grotto': 'Hyrule Field',
     'HC Storms Grotto': 'Hyrule Castle',
     'Kak Redead Grotto': 'Kakariko Village'
}

scene_groups: dict[str, list[str]] = {
    'Deku Tree': ['Deku Tree', 'Deku Tree Boss'],
    'Dodongos Cavern': ['Dodongos Cavern', 'Dodongos Cavern Boss'],
    'Jabu Jabus Belly': ['Jabu Jabus Belly', 'Jabu Jabus Belly Boss'],
    'Forest Temple': ['Forst Temple', 'Forest Temple Boss'],
    'Fire Temple': ['Fire Temple', 'Fire Temple Boss'],
    'Water Temple': ['Water Temple', 'Water Temple Boss'],
    'Spirit Temple': ['Spirit Temple', 'Spirit Temple Boss'],
    'Shadow Temple': ['Shadow Temple', 'Shadow Temple Boss'],
    'Ganons Castle': ['Ganons Castle', 'Ganons Tower'],
    'Market Area': [
        'Market Treasure Chest Game',
        'Market Entrance (Child Day)',
        'Market Entrance (Child Night)',
        'Market Entrance (Adult)',
        'Back Alley (Child Day)',
        'Back Alley (Child Night)',
        'Market (Child Day)',
        'Market (Child Night)',
        'Market (Adult)',
        'ToT Entrance (Child Day)',
        'ToT Entrance (Child Night)',
        'ToT Entrance (Adult)',
        'Market Man in Green House',
        'Market Potion Shop',
        'Market Bombchu Shop',
        'Market Mask Shop',
        'Market Dog Lady House',
        'Market Guard House',
        'Market Bombchu Bowling',
        'Temple of Time',
        'Castle Courtyard',
        'Hyrule Castle',
    ],
    'Forest Area': [
        'KF Know it All House',
        'KF House of Twins',
        'KF Midos House',
        'KF Sarias House',
        'KF Kokiri Shop',
        'KF Links House',
        'Kokiri Forest',
        'Sacred Forest Meadow',
        'Lost Woods',
    ],
    'Gerudo Area': [
        'GV Carpenter Tent',
        'Gerudo Valley',
        'Desert Colossus',
        'Gerudo Fortress',
        'Haunted Wasteland',
    ],
    'Goron Area': [
        'GC Shop',
        'Goron City',
        'Death Mountain',
        'Death Mountain Crater',
    ],
    'Zora Area': [
        'ZD Shop',
        'Zoras River',
        'Zoras Domain',
        'Zoras Fountain',
    ],
    'Kakariko Area': [
        'Kak Carpenter Boss House',
        'Kak Potion Shop',
        'Graveyard Dampes House',
        'Graveyard Royal Familys Tomb',
        'Graveyard Heart Piece Grave',
        'Windmill and Dampes Grave',
        'Kakariko Village',
        'Graveyard',
    ],
    'Lon Lon Ranch': [
        'LLR Stables',
        'Kak Impas House',
        'LLR Tower',
        'Lon Lon Ranch',
    ],
    'Lake Hylia': [
        'LH Lab',
        'Lake Hylia',
        'LH Fishing Hole',
    ]
}

def get_scene_group(scene: str):
    #if scene in grotto_scenes:
    #     scene = grotto_scenes[scene]
    for group in scene_groups:
        if scene in scene_groups[group]:
            return group
    if scene in scene_list:
         return scene
    return None

# Maps boss rooms to their dungeons
boss_room_map: dict[str,str] = {
    'Deku Tree Boss': 'Deku Tree',
    'Dodongos Cavern Boss': 'Dodongos Cavern',
    'Jabu Jabus Belly Boss': 'Jabu Jabus Belly',
    'Forest Temple Boss': 'Forest Temple',
    'Fire Temple Boss': 'Fire Temple',
    'Spirit Temple Boss': 'Spirit Temple',
    'Shadow Temple Boss': 'Shadow Temple'
}