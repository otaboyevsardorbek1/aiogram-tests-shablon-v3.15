def http_status_message(code):
    match code:
        case 100:
            return "Continue"
        case 101:
            return "Switching protocols"
        case 102:
            return "Processing"
        case 103:
            return "Early Hints"
        
        # 2xx Successful
        case 200:
            return "OK"
        case 201:
            return "Created"
        case 202:
            return "Accepted"
        case 203:
            return "Non-Authoritative Information"
        case 204:
            return "No Content"
        case 205:
            return "Reset Content"
        case 206:
            return "Partial Content"
        case 207:
            return "Multi-Status"
        case 208:
            return "Already Reported"
        case 226:
            return "IM Used"
        
        # 3xx Redirection
        case 300:
            return "Multiple Choices"
        case 301:
            return "Moved Permanently"
        case 302:
            return "Found (Previously 'Moved Temporarily')"
        case 303:
            return "See Other"
        case 304:
            return "Not Modified"
        case 305:
            return "Use Proxy"
        case 306:
            return "Switch Proxy"
        case 307:
            return "Temporary Redirect"
        case 308:
            return "Permanent Redirect"
        
        # 4xx Client Error
        case 400:
            return "Bad Request"
        case 401:
            return "Unauthorized"
        case 402:
            return "Payment Required"
        case 403:
            return "Forbidden"
        case 404:
            return "Not Found"
        case 405:
            return "Method Not Allowed"
        case 406:
            return "Not Acceptable"
        case 407:
            return "Proxy Authentication Required"
        case 408:
            return "Request Timeout"
        case 409:
            return "Conflict"
        case 410:
            return "Gone"
        case 411:
            return "Length Required"
        case 412:
            return "Precondition Failed"
        case 413:
            return "Payload Too Large"
        case 414:
            return "URI Too Long"
        case 415:
            return "Unsupported Media Type"
        case 416:
            return "Range Not Satisfiable"
        case 417:
            return "Expectation Failed"
        case 418:
            return "I'm a Teapot"
        case 421:
            return "Misdirected Request"
        case 422:
            return "Unprocessable Entity"
        case 423:
            return "Locked"
        case 424:
            return "Failed Dependency"
        case 425:
            return "Too Early"
        case 426:
            return "Upgrade Required"
        case 428:
            return "Precondition Required"
        case 429:
            return "Too Many Requests"
        case 431:
            return "Request Header Fields Too Large"
        case 451:
            return "Unavailable For Legal Reasons"
        
        # 5xx Server Error
        case 500:
            return "Internal Server Error"
        case 501:
            return "Not Implemented"
        case 502:
            return "Bad Gateway"
        case 503:
            return "Service Unavailable"
        case 504:
            return "Gateway Timeout"
        case 505:
            return "HTTP Version Not Supported"
        case 506:
            return "Variant Also Negotiates"
        case 507:
            return "Insufficient Storage"
        case 508:
            return "Loop Detected"
        case 510:
            return "Not Extended"
        case 511:
            return "Network Authentication Required"
        
        case _:
            return "Unknown HTTP Status Code"


def countries_info(langs: str):
    langs=langs.upper()
    if len(langs) == int(2):
        match langs:
                case 'AF':
                    return 'AFGHANISTAN'
                case 'AL':
                    return 'ALBANIA'
                case 'DZ':
                    return 'ALGERIA'
                case 'AS':
                    return 'AMERICAN SAMOA'
                case 'AD':
                    return 'ANDORRA'
                case 'AO':
                    return 'ANGOLA'
                case 'AQ':
                    return 'ANTARCTICA'
                case 'AG':
                    return 'ANTIGUA AND BARBUDA'
                case 'AR':
                    return 'ARGENTINA'
                case 'AM':
                    return 'ARMENIA'
                case 'AW':
                    return 'ARUBA'
                case 'AU':
                    return 'AUSTRALIA'
                case 'AT':
                    return 'AUSTRIA'
                case 'AZ':
                    return 'AZERBAIJAN'
                case 'BS':
                    return 'BAHAMAS'
                case 'BH':
                    return 'BAHRAIN'
                case 'BD':
                    return 'BANGLADESH'
                case 'BB':
                    return 'BARBADOS'
                case 'BY':
                    return 'BELARUS'
                case 'BE':
                    return 'BELGIUM'
                case 'BZ':
                    return 'BELIZE'
                case 'BJ':
                    return 'BENIN'
                case 'BM':
                    return 'BERMUDA'
                case 'BT':
                    return 'BHUTAN'
                case 'BO':
                    return 'BOLIVIA'
                case 'BA':
                    return 'BOSNIA AND HERZEGOVINA'
                case 'BW':
                    return 'BOTSWANA'
                case 'BV':
                    return 'BOUVET ISLAND'
                case 'BR':
                    return 'BRAZIL'
                case 'IO':
                    return 'BRITISH INDIAN OCEAN TERRITORY'
                case 'BN':
                    return 'BRUNEI DARUSSALAM'
                case 'BG':
                    return 'BULGARIA'
                case 'BF':
                    return 'BURKINA FASO'
                case 'BI':
                    return 'BURUNDI'
                case 'KH':
                    return 'CAMBODIA'
                case 'CM':
                    return 'CAMEROON'
                case 'CA':
                    return 'CANADA'
                case 'CV':
                    return 'CAPE VERDE'
                case 'KY':
                    return 'CAYMAN ISLANDS'
                case 'CF':
                    return 'CENTRAL AFRICAN REPUBLIC'
                case 'TD':
                    return 'CHAD'
                case 'CL':
                    return 'CHILE'
                case 'CN':
                    return 'CHINA'
                case 'CX':
                    return 'CHRISTMAS ISLAND'
                case 'CC':
                    return 'COCOS (KEELING) ISLANDS'
                case 'CO':
                    return 'COLOMBIA'
                case 'KM':
                    return 'COMOROS'
                case 'CG':
                    return 'CONGO'
                case 'CD':
                    return 'CONGO, THE DEMOCRATIC REPUBLIC OF THE'
                case 'CK':
                    return 'COOK ISLANDS'
                case 'CR':
                    return 'COSTA RICA'
                case 'CI':
                    return "CÔTE D'IVOIRE"
                case 'HR':
                    return 'CROATIA'
                case 'CU':
                    return 'CUBA'
                case 'CY':
                    return 'CYPRUS'
                case 'CZ':
                    return 'CZECH REPUBLIC'
                case 'DK':
                    return 'DENMARK'
                case 'DJ':
                    return 'DJIBOUTI'
                case 'DM':
                    return 'DOMINICA'
                case 'DO':
                    return 'DOMINICAN REPUBLIC'
                case 'EC':
                    return 'ECUADOR'
                case 'EG':
                    return 'EGYPT'
                case 'SV':
                    return 'EL SALVADOR'
                case 'GQ':
                    return 'EQUATORIAL GUINEA'
                case 'ER':
                    return 'ERITREA'
                case 'EE':
                    return 'ESTONIA'
                case 'ET':
                    return 'ETHIOPIA'
                case 'FK':
                    return 'FALKLAND ISLANDS (MALVINAS)'
                case 'FO':
                    return 'FAROE ISLANDS'
                case 'FJ':
                    return 'FIJI'
                case 'FI':
                    return 'FINLAND'
                case 'FR':
                    return 'FRANCE'
                case 'GF':
                    return 'FRENCH GUIANA'
                case 'PF':
                    return 'FRENCH POLYNESIA'
                case 'TF':
                    return 'FRENCH SOUTHERN TERRITORIES'
                case 'GA':
                    return 'GABON'
                case 'GM':
                    return 'GAMBIA'
                case 'GE':
                    return 'GEORGIA'
                case 'DE':
                    return 'GERMANY'
                case 'GH':
                    return 'GHANA'
                case 'GI':
                    return 'GIBRALTAR'
                case 'GR':
                    return 'GREECE'
                case 'GL':
                    return 'GREENLAND'
                case 'GD':
                    return 'GRENADA'
                case 'GP':
                    return 'GUADELOUPE'
                case 'GU':
                    return 'GUAM'
                case 'GT':
                    return 'GUATEMALA'
                case 'GN':
                    return 'GUINEA'
                case 'GW':
                    return 'GUINEA-BISSAU'
                case 'GY':
                    return 'GUYANA'
                case 'HT':
                    return 'HAITI'
                case 'HM':
                    return 'HEARD ISLAND AND MCDONALD ISLANDS'
                case 'HN':
                    return 'HONDURAS'
                case 'HK':
                    return 'HONG KONG'
                case 'HU':
                    return 'HUNGARY'
                case 'IS':
                    return 'ICELAND'
                case 'IN':
                    return 'INDIA'
                case 'ID':
                    return 'INDONESIA'
                case 'IR':
                    return 'IRAN, ISLAMIC REPUBLIC OF'
                case 'IQ':
                    return 'IRAQ'
                case 'IE':
                    return 'IRELAND'
                case 'IL':
                    return 'ISRAEL'
                case 'IT':
                    return 'ITALY'
                case 'JM':
                    return 'JAMAICA'
                case 'JP':
                    return 'JAPAN'
                case 'JO':
                    return 'JORDAN'
                case 'KZ':
                    return 'KAZAKHSTAN'
                case 'KE':
                    return 'KENYA'
                case 'KI':
                    return 'KIRIBATI'
                case 'KP':
                    return "KOREA, DEMOCRATIC PEOPLE'S REPUBLIC OF"
                case 'KR':
                    return 'KOREA, REPUBLIC OF'
                case 'KW':
                    return 'KUWAIT'
                case 'KG':
                    return 'KYRGYZSTAN'
                case 'LA':
                    return "LAO PEOPLE'S DEMOCRATIC REPUBLIC (LAOS)"
                case 'LV':
                    return 'LATVIA'
                case 'LB':
                    return 'LEBANON'
                case 'LS':
                    return 'LESOTHO'
                case 'LR':
                    return 'LIBERIA'
                case 'LY':
                    return 'LIBYA, STATE OF'
                case 'LI':
                    return 'LIECHTENSTEIN'
                case 'LT':
                    return 'LITHUANIA'
                case 'LU':
                    return 'LUXEMBOURG'
                case 'MO':
                    return 'MACAO'
                case 'MG':
                    return 'MADAGASCAR'
                case 'MW':
                    return 'MALAWI'
                case 'MY':
                    return 'MALAYSIA'
                case 'MV':
                    return 'MALDIVES'
                case 'ML':
                    return 'MALI'
                case 'MT':
                    return 'MALTA'
                case 'MH':
                    return 'MARSHALL ISLANDS'
                case 'MQ':
                    return 'MARTINIQUE'
                case 'MR':
                    return 'MAURITANIA'
                case 'MU':
                    return 'MAURITIUS'
                case 'YT':
                    return 'MAYOTTE'
                case 'MX':
                    return 'MEXICO'
                case 'FM':
                    return 'MICRONESIA (FEDERATED STATES OF)'
                case 'MD':
                    return 'MOLDOVA (REPUBLIC OF)'
                case 'MC':
                    return 'MONACO'
                case 'MN':
                    return 'MONGOLIA'
                case 'ME':
                    return 'MONTENEGRO'
                case 'MS':
                    return 'MONTSERRAT'
                case 'MA':
                    return 'MOROCCO'
                case 'MZ':
                    return 'MOZAMBIQUE'
                case 'MM':
                    return 'MYANMAR'
                case 'NA':
                    return 'NAMIBIA'
                case 'NR':
                    return 'NAURU'
                case 'NP':
                    return 'NEPAL'
                case 'NL':
                    return 'NETHERLANDS'
                case 'NC':
                    return 'NEW CALEDONIA'
                case 'NZ':
                    return 'NEW ZEALAND'
                case 'NI':
                    return 'NICARAGUA'
                case 'NE':
                    return 'NIGER'
                case 'NG':
                    return 'NIGERIA'
                case 'NU':
                    return 'NIUE'
                case 'NF':
                    return 'NORFOLK ISLAND'
                case 'MP':
                    return 'NORTHERN MARIANA ISLANDS'
                case 'NO':
                    return 'NORWAY'
                case 'OM':
                    return 'OMAN'
                case 'PK':
                    return 'PAKISTAN'
                case 'PW':
                    return 'PALAU'
                case 'PA':
                    return 'PANAMA'
                case 'PG':
                    return 'PAPUA NEW GUINEA'
                case 'PY':
                    return 'PARAGUAY'
                case 'PE':
                    return 'PERU'
                case 'PH':
                    return 'PHILIPPINES'
                case 'PN':
                    return 'PITCAIRN'
                case 'PL':
                    return 'POLAND'
                case 'PT':
                    return 'PORTUGAL'
                case 'PR':
                    return 'PUERTO RICO'
                case 'QA':
                    return 'QATAR'
                case 'RE':
                    return 'REUNION'
                case 'RO':
                    return 'ROMANIA'
                case 'RU':
                    return 'RUSSIAN FEDERATION'
                case 'RW':
                    return 'RWANDA'
                case 'BL':
                    return 'SAINT BARTHÉLEMY'
                case 'SH':
                    return 'SAINT HELENA, ASCENSION AND TRISTAN DA CUNHA'
                case 'KN':
                    return 'SAINT KITTS AND NEVIS'
                case 'LC':
                    return 'SAINT LUCIA'
                case 'MF':
                    return 'SAINT MARTIN (FRENCH PART)'
                case 'PM':
                    return 'SAINT PIERRE AND MIQUELON'
                case 'VC':
                    return 'SAINT VINCENT AND THE GRENADINES'
                case 'WS':
                    return 'SAMOA'
                case 'SM':
                    return 'SAN MARINO'
                case 'ST':
                    return 'SAO TOME AND PRINCIPE'
                case 'SA':
                    return 'SAUDI ARABIA'
                case 'SN':
                    return 'SENEGAL'
                case 'RS':
                    return 'SERBIA'
                case 'SC':
                    return 'SEYCHELLES'
                case 'SL':
                    return 'SIERRA LEONE'
                case 'SG':
                    return 'SINGAPORE'
                case 'SX':
                    return 'SINT MAARTEN (DUTCH PART)'
                case 'SO':
                    return 'SOMALIA'
                case 'ZA':
                    return 'SOUTH AFRICA'
                case 'GS':
                    return 'SOUTH GEORGIA AND THE SOUTH SANDWICH ISLANDS'
                case 'SS':
                    return 'SOUTH SUDAN'
                case 'ES':
                    return 'SPAIN'
                case 'LK':
                    return 'SRI LANKA'
                case 'SD':
                    return 'SUDAN'
                case 'SR':
                    return 'SURINAME'
                case 'SJ':
                    return 'SVALBARD AND JAN MAYEN'
                case 'SZ':
                    return 'SWAZILAND'
                case 'SE':
                    return 'SWEDEN'
                case 'CH':
                    return 'SWITZERLAND'
                case 'SY':
                    return 'SYRIAN ARAB REPUBLIC'
                case 'TW':
                    return 'TAIWAN'
                case 'TJ':
                    return 'TAJIKISTAN'
                case 'TZ':
                    return 'TANZANIA (UNITED REPUBLIC OF)'
                case 'TH':
                    return 'THAILAND'
                case 'TL':
                    return 'TIMOR-LESTE'
                case 'TG':
                    return 'TOGO'
                case 'TK':
                    return 'TOKELAU'
                case 'TO':
                    return 'TONGA'
                case 'TT':
                    return 'TRINIDAD AND TOBAGO'
                case 'TN':
                    return 'TUNISIA'
                case 'TM':
                    return 'TURKMENISTAN'
                case 'TC':
                    return 'TURKS AND CAICOS ISLANDS'
                case 'TV':
                    return 'TUVALU'
                case 'UG':
                    return 'UGANDA'
                case 'UA':
                    return 'UKRAINE'
                case 'AE':
                    return 'UNITED ARAB EMIRATES'
                case 'GB':
                    return 'UNITED KINGDOM OF GREAT BRITAIN AND NORTHERN IRELAND'
                case 'US':
                    return 'UNITED STATES OF AMERICA'
                case 'UY':
                    return 'URUGUAY'
                case 'UZ':
                    return 'UZBEKISTAN'
                case 'VU':
                    return 'VANUATU'
                case 'VE':
                    return 'VENEZUELA (BOLIVARIAN REPUBLIC OF)'
                case 'VN':
                    return 'VIET NAM'
                case 'VG':
                    return 'VIRGIN ISLANDS (BRITISH)'
                case 'VI':
                    return 'VIRGIN ISLANDS (U.S.)'
                case 'WF':
                    return 'WALLIS AND FUTUNA'
                case 'EH':
                    return 'WESTERN SAHARA'
                case 'YE':
                    return 'YEMEN'
                case 'ZM':
                    return 'ZAMBIA'
                case 'ZW':
                    return 'ZIMBABWE'
    else:
        return "Ma`lumot xato kiritildi.!"




# print(http_status_message(code=200))
# print(countries_info(langs='ar'))

