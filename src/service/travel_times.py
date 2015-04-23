import bisect

from pprint import pprint as pp

walking_times = [(((tup[0] * 60) + tup[1]) * 60, tup[2]) for tup in [
    (0, 0, "the door to the meeting room"),

    (0, 1, "The Hammersmith Ram"),
    (0, 2, "Hammersmith Broadway"),
    (0, 24, "Franco Manca Chiswick"),
    (0, 27, "Westfield Shepherds Bush"),
    (0, 40, "Putney Bridge"),
    (0, 45, "HMP Wormwood Scrubs"),
    (0, 50, "The Natural History Museum"),
    (1, 19, "Buckingham Palace"),
    (1, 29, "Oxford Circus"),
    (1, 37, "The Houses of Parliament"),
    (2, 7, "Wembley Stadium"),
    (2, 58, "Hampton Court"),
    (3, 14, "Canary Wharf"),
    (3, 28, "Feltham Young Offenders Institute"),
    (3, 40, "Heathrow"),
    (4, 32, "Staines[-upon-Thames]"),
    (17, 13, "Brighton Pier"),
    (24, 0, "The Magic Roundabout, Swindon"),
    (30, 0, "Coventry"),
    (18, 11, "Bicester (pronounced Bister)"),

    (999999999, 0, "THE MOOOOOOOOOOOOOON")
]]

driving_times = [(((tup[0] * 60) + tup[1]) * 60, tup[2]) for tup in [
    (0, 0, "the Hammersmith Gyratory"),

    (0, 44, "St Paul's Cathedral"),
    (1, 28, "Oxford"),
    (1, 41, "Silverstone Circuit"),
    (1, 45, "Brighton"),
    (2, 18, "Bristol"),
    (5, 49, "Paris"),

    (999999999, 0, "THE MOOOOOOOOOOOOOON")
]]

flying_times = [(((tup[0] * 60) + tup[1]) * 60, tup[2]) for tup in [
    (0, 0, 'nowhere'),

    (0, 29, 'Belgium - Brussels'),
    (0, 31, 'Netherlands - Amsterdam'),
    (0, 32, 'France - Paris'),
    (0, 43, 'Ireland - Dublin'),
    (0, 45, 'Luxembourg - Luxembourg'),
    (1, 9, 'Switzerland - Bern'),
    (1, 16, 'Liechtenstein - Vaduz'),
    (1, 22, 'Germany - Berlin - Berlin'),
    (1, 24, 'Denmark - Copenhagen'),
    (1, 30, 'Andorra - Andorra La Vella'),
    (1, 31, 'Czech Republic - Prague'),
    (1, 33, 'Monaco - Monaco'),
    (1, 41, 'Norway - Oslo'),
    (1, 48, 'Slovenia - Ljubljana'),
    (1, 49, 'Austria - Vienna'),
    (1, 50, 'Croatia - Zagreb'),
    (1, 52, 'Faroe Islands - Faroe Islands - Torshavn'),
    (1, 52, 'Spain - Madrid'),
    (1, 53, 'San Marino - San Marino'),
    (1, 55, 'Slovakia - Bratislava'),
    (1, 60, 'Sweden - Stockholm'),
    (1, 60, 'Vatican City State - Vatican City'),
    (2, 0, 'Italy - Rome'),
    (2, 1, 'Poland - Warsaw'),
    (2, 2, 'Hungary - Budapest'),
    (2, 13, 'Portugal - Lisbon'),
    (2, 15, 'Bosnia Herzegovina - Sarajevo'),
    (2, 19, 'Algeria - Algiers'),
    (2, 19, 'Latvia - Riga'),
    (2, 21, 'Serbia - Belgrade'),
    (2, 23, 'Lithuania - Vilnius'),
    (2, 25, 'Gibraltar - Gibraltar'),
    (2, 28, 'Estonia - Tallinn'),
    (2, 28, 'Montenegro - Podgorica'),
    (2, 31, 'Finland - Helsinki'),
    (2, 33, 'Tunisia - Tunis'),
    (2, 35, 'Belarus - Minsk'),
    (2, 36, 'Albania - Tirane'),
    (2, 36, 'Bulgaria - Sofia'),
    (2, 37, 'Kosovo - Pristina'),
    (2, 38, 'Iceland - Reykjavik'),
    (2, 42, 'Malta - Valletta'),
    (2, 42, 'Romania - Bucharest'),
    (2, 44, 'Macedonia - Skopje'),
    (2, 44, 'Moldova - Kishinev'),
    (2, 44, 'Ukraine - Kiev'),
    (2, 46, 'Morocco - Rabat'),
    (3, 1, 'Libya - Tripoli'),
    (3, 2, 'Greece - Athens'),
    (3, 13, 'Russia - Moscow'),
    (3, 36, 'Turkey - Ankara'),
    (3, 45, 'Western Sahara - El Aaiun'),
    (4, 8, 'Cyprus - Nicosia'),
    (4, 12, 'Greenland - Nuuk'),
    (4, 28, 'Lebanon - Beirut'),
    (4, 31, 'Egypt - Cairo'),
    (4, 33, 'Georgia - Tbilisi'),
    (4, 34, 'Syria - Damascus'),
    (4, 37, 'Gaza Strip - Gaza'),
    (4, 39, 'Armenia - Yerevan'),
    (4, 40, 'Israel - Jerusalem'),
    (4, 40, 'West Bank - Bethlehem'),
    (4, 41, 'Jordan - Amman'),
    (5, 5, 'Mauritania - Nouakchott'),
    (5, 6, 'Azerbaijan - Baku'),
    (5, 10, 'Saint Pierre and Miquelon - Saint-Pierre'),
    (5, 16, 'Iraq - Baghdad'),
    (5, 27, 'Niger - Niamey'),
    (5, 36, 'Burkina Faso - Ouagadougou'),
    (5, 39, 'Mali - Bamako'),
    (5, 39, 'Senegal - Dakar'),
    (5, 41, 'Iran - Tehran'),
    (5, 46, 'Gambia - Banjul'),
    (5, 53, 'Chad - Ndjamena'),
    (5, 55, 'Cape Verde - Praia'),
    (5, 59, 'Guinea Bissau - Bissau'),
    (5, 60, 'Kuwait - Kuwait City'),
    (6, 7, 'Nigeria - Abuja'),
    (6, 7, 'Turkmenistan - Ashgabat'),
    (6, 9, 'Kazakhstan - Astana'),
    (6, 14, 'Guinea - Conakry'),
    (6, 22, 'Saudi Arabia - Riyadh'),
    (6, 22, 'Sierra Leone - Freetown'),
    (6, 22, 'Sudan - Khartoum'),
    (6, 27, 'Cote dIvoire - Yamoussoukro'),
    (6, 28, 'Benin - Porto Novo'),
    (6, 29, 'Togo - Lome'),
    (6, 31, 'Bahrain - Manama'),
    (6, 35, 'Liberia - Monrovia'),
    (6, 36, 'Ghana - Accra'),
    (6, 43, 'Qatar - Doha'),
    (6, 45, 'Uzbekistan - Tashkent'),
    (6, 49, 'Eritrea - Asmara'),
    (6, 56, 'Canada - Ontario - Ottawa'),
    (6, 56, 'Equatorial Guinea - Malabo'),
    (6, 57, 'Tajikistan - Dushanbe'),
    (6, 59, 'Cameroon - Yaounde'),
    (7, 3, 'UAE - Abu Dhabi - Abu Dhabi'),
    (7, 5, 'Kyrgyzstan - Bishkek'),
    (7, 6, 'Central African Republic - Bangui'),
    (7, 9, 'Bermuda - Hamilton (Bermuda)'),
    (7, 14, 'Yemen - Sana'),
    (7, 22, 'Sao Tome and Principe - Sao Tome'),
    (7, 23, 'Afghanistan - Kabul'),
    (7, 24, 'Gabon - Libreville'),
    (7, 29, 'Djibouti - Djibouti'),
    (7, 31, 'Oman - Muscat'),
    (7, 34, 'Ethiopia - Addis Ababa'),
    (7, 39, 'USA - District of Columbia - Washington DC'),
    (7, 41, 'South Sudan - Juba'),
    (7, 49, 'Pakistan - Islamabad'),
    (8, 10, 'Congo - Brazzaville'),
    (8, 11, 'Congo Dem. Rep. - Kinshasa'),
    (8, 19, 'Uganda - Kampala'),
    (8, 26, 'Rwanda - Kigali'),
    (8, 28, 'Antigua and Barbuda - Saint Johns'),
    (8, 29, 'Anguilla - The Valley'),
    (8, 32, 'Saint Kitts and Nevis - Basseterre'),
    (8, 33, 'Guadeloupe - Basse-Terre'),
    (8, 35, 'British Virgin Islands - Tortola - Road Town'),
    (8, 35, 'Montserrat - Brades'),
    (8, 36, 'Burundi - Bujumbura'),
    (8, 39, 'Dominica - Roseau'),
    (8, 41, 'India - Delhi - New Delhi'),
    (8, 44, 'Angola - Luanda'),
    (8, 44, 'Barbados - Bridgetown'),
    (8, 44, 'Kenya - Nairobi'),
    (8, 44, 'Martinique - Fort-de-France'),
    (8, 44, 'Puerto Rico - San Juan'),
    (8, 44, 'Saint Lucia - Castries'),
    (8, 52, 'Saint Vincent Grenadines - Kingstown'),
    (8, 55, 'Somalia - Mogadishu'),
    (9, 1, 'Bahamas - Nassau'),
    (9, 1, 'Grenada - Saint Georges'),
    (9, 2, 'Mongolia - Ulaanbaatar'),
    (9, 3, 'Dominican Republic - Santo Domingo'),
    (9, 7, 'French Guiana - Cayenne'),
    (9, 12, 'Trinidad and Tobago - Port of Spain'),
    (9, 15, 'Suriname - Paramaribo'),
    (9, 17, 'Haiti - Port-au-Prince'),
    (9, 19, 'Tanzania - Dodoma'),
    (9, 23, 'Guyana - Georgetown'),
    (9, 29, 'Nepal - Kathmandu'),
    (9, 39, 'Curacao - Willemstad'),
    (9, 40, 'Cuba - Havana'),
    (9, 40, 'Venezuela - Caracas'),
    (9, 42, 'Aruba - Oranjestad'),
    (9, 45, 'Jamaica - Kingston (Jamaica)'),
    (9, 51, 'Bhutan - Thimphu'),
    (9, 60, 'Cayman Islands - George Town(Cayman Islands)'),
    (10, 10, 'Zambia - Lusaka'),
    (10, 12, 'Malawi - Lilongwe'),
    (10, 20, 'Bangladesh - Dhaka'),
    (10, 27, 'Seychelles - Victoria (Seychelles)'),
    (10, 28, 'Comoros - Moroni'),
    (10, 33, 'China - Beijing'),
    (10, 37, 'Zimbabwe - Harare'),
    (10, 42, 'Maldives - Male'),
    (10, 44, 'Mayotte - Mamoutzou'),
    (10, 47, 'Namibia - Windhoek'),
    (10, 51, 'Belize - Belmopan'),
    (10, 59, 'Colombia - Bogota'),
    (10, 59, 'Panama - Panama'),
    (11, 5, 'Honduras - Tegucigalpa'),
    (11, 11, 'North Korea - Pyongyang'),
    (11, 13, 'Nicaragua - Managua'),
    (11, 15, 'Sri Lanka - Colombo'),
    (11, 16, 'Brazil - Distrito Federal - Brasilia'),
    (11, 17, 'Myanmar - Naypyidaw'),
    (11, 18, 'Costa Rica - San Jose (Costa Rica)'),
    (11, 19, 'Guatemala - Guatemala'),
    (11, 20, 'Botswana - Gaborone'),
    (11, 20, 'El Salvador - San Salvador'),
    (11, 29, 'South Korea - Seoul'),
    (11, 33, 'Mexico - Federal District - Mexico City'),
    (11, 34, 'South Africa - Pretoria'),
    (11, 39, 'Madagascar - Antananarivo'),
    (11, 46, 'Mozambique - Maputo'),
    (11, 48, 'Swaziland - Mbabane'),
    (11, 53, 'Ecuador - Quito'),
    (11, 54, 'Vietnam - Hanoi'),
    (11, 59, 'Laos - Vientiane'),
    (12, 3, 'Lesotho - Maseru'),
    (12, 19, 'Thailand - Bangkok'),
    (12, 23, 'Japan - Tokyo'),
    (12, 25, 'Reunion (French) - Saint-Denis'),
    (12, 26, 'Hong Kong - Hong Kong'),
    (12, 31, 'Mauritius - Port Louis'),
    (12, 38, 'Taiwan - Taipei'),
    (12, 52, 'Bolivia - La Paz'),
    (12, 55, 'Cambodia - Phnom Penh'),
    (13, 5, 'Peru - Lima - Lima'),
    (13, 8, 'Paraguay - Asuncion'),
    (13, 35, 'Malaysia - Kuala Lumpur'),
    (13, 53, 'Philippines - Manila'),
    (13, 59, 'Singapore - Singapore'),
    (14, 11, 'Uruguay - Montevideo'),
    (14, 17, 'Argentina - Buenos Aires'),
    (14, 33, 'Brunei - Bandar Seri Begawan'),
    (15, 0, 'Chile - Santiago'),
    (15, 4, 'Indonesia - Java - Jakarta'),
    (15, 43, 'Palau - Melekeok'),
    (16, 18, 'Falkland Islands - Stanley'),
    (16, 57, 'Timor Leste - Dili'),
    (17, 6, 'Micronesia - Ponape - Palikir'),
    (17, 23, 'Marshall Islands - Majuro'),
    (18, 14, 'Kiribati - Tarawa'),
    (18, 20, 'Nauru - Yaren'),
    (18, 40, 'Papua New Guinea - Port Moresby'),
    (19, 13, 'Pitcairn Islands - Adamstown'),
    (19, 22, 'Solomon Islands - Honiara'),
    (19, 39, 'Tuvalu - Funafuti'),
    (19, 42, 'Tokelau - Tokelau - Fakaofo'),
    (19, 50, 'French Polynesia - Tahiti - Papeete'),
    (20, 18, 'Samoa - Apia'),
    (20, 23, 'American Samoa - Pago Pago'),
    (20, 47, 'Vanuatu - Port Vila'),
    (20, 58, 'Cook Islands - Rarotonga'),
    (21, 3, 'Fiji - Suva'),
    (21, 3, 'Niue - Alofi'),
    (21, 22, 'New Caledonia - New Caledonia - Noumea'),
    (21, 27, 'Tonga - Nukualofa'),
    (21, 54, 'Australia - ACT - Canberra'),
    (22, 22, 'Norfolk Island - Kingston'),
    (24, 16, 'New Zealand - Wellington'),

    (999999999, 0, "THE MOOOOOOOOOOOOOON")
]]


def how_far_could_i_have_walked(headcount, num_secs):
    mansecs = headcount * num_secs
    index = bisect.bisect([x[0] for x in walking_times], mansecs)
    dist_to_prev = mansecs - walking_times[index-1][0]
    dist_to_next = walking_times[index][0] - mansecs

    if dist_to_prev >= dist_to_next:
        return "With this many man-days you could have almost walked to " + walking_times[index][1] + " by now!"
    else:
        return "With this many man-days you could have walked to " + walking_times[index-1][1] + " by now!"

def how_far_could_i_have_driven(headcount, num_secs):
    mansecs = headcount * num_secs
    index = bisect.bisect([x[0] for x in driving_times], mansecs)
    dist_to_prev = mansecs - driving_times[index-1][0]
    dist_to_next = driving_times[index][0] - mansecs

    if dist_to_prev >= dist_to_next:
        return "With this many man-days you could have almost driven to " + driving_times[index][1] + " by now!"
    else:
        return "With this many man-days you could have driven to " + driving_times[index-1][1] + " by now!"

def how_far_could_i_have_flown(headcount, num_secs):
    mansecs = headcount * num_secs
    index = bisect.bisect([x[0] for x in flying_times], mansecs)
    dist_to_prev = mansecs - flying_times[index-1][0]
    dist_to_next = flying_times[index][0] - mansecs

    if dist_to_prev >= dist_to_next:
        return "With this many man-days you could have almost flown to " + flying_times[index][1] + " by now!"
    else:
        return "With this many man-days you could have flown to " + flying_times[index-1][1] + " by now!"

def how_far_could_i_have_travelled(headcount, num_secs):
    return [
        how_far_could_i_have_walked(headcount, num_secs),
        how_far_could_i_have_driven(headcount, num_secs),
        how_far_could_i_have_flown(headcount, num_secs)
    ]