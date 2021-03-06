EXACT_TO_GENERIC = {'CAM': 'midfield',
                    'CB': 'defence',
                    'CDM': 'midfield',
                    'CF': 'attack',
                    'CM': 'midfield',
                    'GK': 'goalkeeper',
                    'LAM': 'midfield',
                    'LB': 'defence',
                    'LCB': 'defence',
                    'LCM': 'midfield',
                    'LDM': 'midfield',
                    'LF': 'attack',
                    'LM': 'midfield',
                    'LS': 'attack',
                    'LW': 'attack',
                    'RAM': 'attack',
                    'RB': 'defence',
                    'RCB': 'defence',
                    'RCM': 'midfield',
                    'RDM': 'midfield',
                    'RF': 'attack',
                    'RM': 'midfield',
                    'RS': 'attack',
                    'RW': 'attack',
                    'RWB': 'defence',
                    'LWB': 'defence',
                    'Res': 'nan',
                    'ST': 'attack',
                    'Sub': 'nan'}

LINEUP_TO_PLAYER_TEAM_MAPPINGS = {'2017-2018': {'afc-bournemouth': 'bournemouth',
                                                'arsenal': 'arsenal',
                                                'brighton-hove-albion': 'brighton',
                                                'burnley': 'burnley',
                                                'chelsea': 'chelsea',
                                                'crystal-palace': 'crystal-palace',
                                                'everton': 'everton',
                                                'huddersfield-town': 'huddersfield',
                                                'leicester-city': 'leicester-city',
                                                'liverpool': 'liverpool',
                                                'manchester-city': 'manchester-city',
                                                'manchester-united': 'manchester-utd',
                                                'newcastle-united': 'newcastle-utd',
                                                'southampton': 'southampton',
                                                'stoke-city': 'stoke-city',
                                                'swansea-city': 'swansea-city',
                                                'tottenham-hotspur': 'spurs',
                                                'watford': 'watford',
                                                'west-bromwich-albion': 'west-brom',
                                                'west-ham-united': 'west-ham'},
                                  'ALL': {'afc-bournemouth': 'bournemouth',
                                          'arsenal': 'arsenal',
                                          'aston-villa': 'aston-villa',
                                          'brighton-hove-albion': 'brighton',
                                          'burnley': 'burnley',
                                          'cardiff-city': 'cardiff-city',
                                          'chelsea': 'chelsea',
                                          'crystal-palace': 'crystal-palace',
                                          'everton': 'everton',
                                          'fulham': 'fulham',
                                          'huddersfield-town': 'huddersfield',
                                          'hull-city': 'hull-city',
                                          'leicester-city': 'leicester-city',
                                          'liverpool': 'liverpool',
                                          'manchester-city': 'manchester-city',
                                          'manchester-united': 'manchester-utd',
                                          'middlesbrough': 'middlesbrough',
                                          'newcastle-united': 'newcastle-utd',
                                          'norwich-city': 'norwich-city',
                                          'queens-park-rangers': 'qpr',
                                          'southampton': 'southampton',
                                          'stoke-city': 'stoke-city',
                                          'sunderland': 'sunderland',
                                          'swansea-city': 'swansea-city',
                                          'tottenham-hotspur': 'spurs',
                                          'watford': 'watford',
                                          'west-bromwich-albion': 'west-brom',
                                          'west-ham-united': 'west-ham'}

                                  }

FOOTBALL_DATA_TEAM_MAPPINGS = {'2017-2018': {'afc-bournemouth': 'bournemouth',
                                             'arsenal': 'arsenal',
                                             'brighton-hove-albion': 'brighton',
                                             'burnley': 'burnley',
                                             'chelsea': 'chelsea',
                                             'crystal-palace': 'crystal-palace',
                                             'everton': 'everton',
                                             'huddersfield-town': 'huddersfield',
                                             'leicester-city': 'leicester',
                                             'liverpool': 'liverpool',
                                             'manchester-city': 'man-city',
                                             'manchester-united': 'man-united',
                                             'newcastle-united': 'newcastle',
                                             'southampton': 'southampton',
                                             'stoke-city': 'stoke',
                                             'swansea-city': 'swansea',
                                             'tottenham-hotspur': 'tottenham',
                                             'watford': 'watford',
                                             'west-bromwich-albion': 'west-brom',
                                             'west-ham-united': 'west-ham'},
                               '2016-2017': {'afc-bournemouth': 'bournemouth',
                                             'arsenal': 'arsenal',
                                             'burnley': 'burnley',
                                             'chelsea': 'chelsea',
                                             'crystal-palace': 'crystal-palace',
                                             'everton': 'everton',
                                             'hull-city': 'hull',
                                             'leicester-city': 'leicester',
                                             'liverpool': 'liverpool',
                                             'manchester-city': 'man-city',
                                             'manchester-united': 'man-united',
                                             'middlesbrough': 'middlesbrough',
                                             'southampton': 'southampton',
                                             'stoke-city': 'stoke',
                                             'sunderland': 'sunderland',
                                             'swansea-city': 'swansea',
                                             'tottenham-hotspur': 'tottenham',
                                             'watford': 'watford',
                                             'west-bromwich-albion': 'west-brom',
                                             'west-ham-united': 'west-ham'},
                               '2015-2016': {'afc-bournemouth': 'bournemouth',
                                             'arsenal': 'arsenal',
                                             'aston-villa': 'aston-villa',
                                             'chelsea': 'chelsea',
                                             'crystal-palace': 'crystal-palace',
                                             'everton': 'everton',
                                             'leicester-city': 'leicester',
                                             'liverpool': 'liverpool',
                                             'manchester-city': 'man-city',
                                             'manchester-united': 'man-united',
                                             'newcastle-united': 'newcastle',
                                             'norwich-city': 'norwich',
                                             'southampton': 'southampton',
                                             'stoke-city': 'stoke',
                                             'sunderland': 'sunderland',
                                             'swansea-city': 'swansea',
                                             'tottenham-hotspur': 'tottenham',
                                             'watford': 'watford',
                                             'west-bromwich-albion': 'west-brom',
                                             'west-ham-united': 'west-ham'},
                               '2014-2015': {'arsenal': 'arsenal',
                                             'aston-villa': 'aston-villa',
                                             'burnley': 'burnley',
                                             'chelsea': 'chelsea',
                                             'crystal-palace': 'crystal-palace',
                                             'everton': 'everton',
                                             'hull-city': 'hull',
                                             'leicester-city': 'leicester',
                                             'liverpool': 'liverpool',
                                             'manchester-city': 'man-city',
                                             'manchester-united': 'man-united',
                                             'newcastle-united': 'newcastle',
                                             'queens-park-rangers': 'qpr',
                                             'southampton': 'southampton',
                                             'stoke-city': 'stoke',
                                             'sunderland': 'sunderland',
                                             'swansea-city': 'swansea',
                                             'tottenham-hotspur': 'tottenham',
                                             'watford': 'watford',
                                             'west-bromwich-albion': 'west-brom',
                                             'west-ham-united': 'west-ham'},
                               '2013-2014': {'arsenal': 'arsenal',
                                             'aston-villa': 'aston-villa',
                                             'cardiff-city': 'cardiff',
                                             'chelsea': 'chelsea',
                                             'crystal-palace': 'crystal-palace',
                                             'everton': 'everton',
                                             'fulham': 'fulham',
                                             'hull-city': 'hull',
                                             'liverpool': 'liverpool',
                                             'manchester-city': 'man-city',
                                             'manchester-united': 'man-united',
                                             'newcastle-united': 'newcastle',
                                             'norwich-city': 'norwich',
                                             'southampton': 'southampton',
                                             'stoke-city': 'stoke',
                                             'sunderland': 'sunderland',
                                             'swansea-city': 'swansea',
                                             'tottenham-hotspur': 'tottenham',
                                             'west-bromwich-albion': 'west-brom',
                                             'west-ham-united': 'west-ham'}
                               }

PLAYER_URL_TO_SEASON = {'fifa13_10': '2012-2013',
                        'fifa14_13': '2013-2014',
                        'fifa15_14': '2014-2015',
                        'fifa16_73': '2015-2016',
                        'fifa17_173': '2016-2017'
                        }

NATIONALITIES = {'afghanistan',
                 'albania',
                 'algeria',
                 'angola',
                 'antigua-barbuda',
                 'argentina',
                 'armenia',
                 'aruba',
                 'australia',
                 'austria',
                 'azerbaijan',
                 'bahrain',
                 'barbados',
                 'belarus',
                 'belgium',
                 'belize',
                 'benin',
                 'bermuda',
                 'bolivia',
                 'bosnia-herzegovina',
                 'brazil',
                 'bulgaria',
                 'burkina-faso',
                 'burundi',
                 'cambodia',
                 'cameroon',
                 'canada',
                 'cape-verde',
                 'central-african-rep',
                 'chad',
                 'chile',
                 'china-pr',
                 'chinese-taipei',
                 'colombia',
                 'comoros',
                 'congo',
                 'costa-rica',
                 'croatia',
                 'cuba',
                 'curacao',
                 'cyprus',
                 'czech-republic',
                 'denmark',
                 'dominican-republic',
                 'dr-congo',
                 'ecuador',
                 'egypt',
                 'el-salvador',
                 'england',
                 'equatorial-guinea',
                 'eritrea',
                 'estonia',
                 'ethiopia',
                 'faroe-islands',
                 'fiji',
                 'finland',
                 'france',
                 'fyr-macedonia',
                 'gabon',
                 'gambia',
                 'georgia',
                 'germany',
                 'ghana',
                 'gibraltar',
                 'greece',
                 'grenada',
                 'guam',
                 'guatemala',
                 'guinea',
                 'guinea-bissau',
                 'guyana',
                 'haiti',
                 'honduras',
                 'hungary',
                 'iceland',
                 'india',
                 'indonesia',
                 'iran',
                 'iraq',
                 'israel',
                 'italy',
                 'ivory-coast',
                 'jamaica',
                 'japan',
                 'jordan',
                 'kazakhstan',
                 'kenya',
                 'korea-dpr',
                 'korea-republic',
                 'kosovo',
                 'kuwait',
                 'kyrgyzstan',
                 'laos',
                 'latvia',
                 'lebanon',
                 'liberia',
                 'libya',
                 'liechtenstein',
                 'lithuania',
                 'luxembourg',
                 'madagascar',
                 'mali',
                 'malta',
                 'mauritania',
                 'mauritius',
                 'mexico',
                 'moldova',
                 'montenegro',
                 'montserrat',
                 'morocco',
                 'mozambique',
                 'namibia',
                 'netherlands',
                 'new-caledonia',
                 'new-zealand',
                 'niger',
                 'nigeria',
                 'northern-ireland',
                 'norway',
                 'oman',
                 'pakistan',
                 'palestine',
                 'panama',
                 'papua-new-guinea',
                 'paraguay',
                 'peru',
                 'philippines',
                 'poland',
                 'portugal',
                 'puerto-rico',
                 'qatar',
                 'republic-of-ireland',
                 'romania',
                 'russia',
                 'rwanda',
                 'san-marino',
                 'sao-tome-principe',
                 'saudi-arabia',
                 'scotland',
                 'senegal',
                 'serbia',
                 'sierra-leone',
                 'slovakia',
                 'slovenia',
                 'solomon-islands',
                 'somalia',
                 'south-africa',
                 'spain',
                 'st-kitts-nevis',
                 'st-lucia',
                 'st-vincent-grenadine',
                 'suriname',
                 'sweden',
                 'switzerland',
                 'syria',
                 'tajikistan',
                 'tanzania',
                 'timor-leste',
                 'togo',
                 'trinidad-tobago',
                 'tunisia',
                 'turkey',
                 'turkmenistan',
                 'uganda',
                 'ukraine',
                 'united-states',
                 'uruguay',
                 'uzbekistan',
                 'venezuela',
                 'wales',
                 'zambia',
                 'zimbabwe'}

TEAM_PROBABILITY = 0.15
NUMBER_PROBABILITY = 0.2
NATIONALITY_PROBABILITY = 0.15
NAME_PROBABILITY = 0.4
SEASON_PROBABILITY = 0.1
