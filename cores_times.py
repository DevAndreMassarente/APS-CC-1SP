cores_times = {
    # 50 clubes mais famosos do Brasil
    "Corinthians": ["#000000", "#FFFFFF"],  # Preto, Branco
    "Flamengo": ["#C3271D", "#000000"],  # Vermelho, Preto
    "Palmeiras": ["#006437", "#FFFFFF"],  # Verde, Branco
    "São Paulo": ["#FE0000", "#000000", "#FFFFFF"],  # Vermelho, Preto, Branco
    "Santos": ["#000000", "#FFFFFF"],  # Preto, Branco
    "Grêmio": ["#0D80BF", "#1F1A17", "#FFFFFF"],  # Azul, Preto, Branco
    "Internacional": ["#E5050F", "#FFFFFF"],  # Vermelho, Branco
    "Cruzeiro": ["#2F529E", "#FFFFFF"],  # Azul, Branco
    "Atlético Mineiro": ["#000000", "#FFFFFF"],  # Preto, Branco
    "Botafogo": ["#000000", "#FFFFFF"],  # Preto, Branco
    "Vasco da Gama": ["#000000", "#FFFFFF"],  # Preto, Branco
    "Fluminense": ["#008000", "#8B0000", "#FFFFFF"],  # Verde, Grená, Branco
    "Bahia": ["#0033A0", "#FF0000", "#FFFFFF"],  # Azul, Vermelho, Branco
    "Sport Recife": ["#FF0000", "#000000"],  # Vermelho, Preto
    "Ceará": ["#000000", "#FFFFFF"],  # Preto, Branco
    "Fortaleza": ["#0033A0", "#FF0000", "#FFFFFF"],  # Azul, Vermelho, Branco
    "Atlético Paranaense": ["#FF0000", "#000000"],  # Vermelho, Preto
    "Coritiba": ["#008000", "#FFFFFF"],  # Verde, Branco
    "Goiás": ["#008000", "#FFFFFF"],  # Verde, Branco
    "Vitória": ["#FF0000", "#000000"],  # Vermelho, Preto
    "Chapecoense": ["#008000", "#FFFFFF"],  # Verde, Branco
    "Avaí": ["#0033A0", "#FFFFFF"],  # Azul, Branco
    "Figueirense": ["#000000", "#FFFFFF"],  # Preto, Branco
    "Juventude": ["#008000", "#FFFFFF"],  # Verde, Branco
    "Náutico": ["#FF0000", "#FFFFFF"],  # Vermelho, Branco
    "Santa Cruz": ["#000000", "#FFFFFF", "#FF0000"],  # Preto, Branco, Vermelho
    "Paysandu": ["#0033A0", "#FFFFFF"],  # Azul, Branco
    "Remo": ["#0033A0", "#FFFFFF"],  # Azul, Branco
    "ABC": ["#000000", "#FFFFFF"],  # Preto, Branco
    "América Mineiro": ["#008000", "#000000"],  # Verde, Preto
    "Botafogo-SP": ["#000000", "#FFFFFF", "#FF0000"],  # Preto, Branco, Vermelho
    "Bragantino": ["#000000", "#FFFFFF"],  # Preto, Branco
    "Criciúma": ["#FFD700", "#000000"],  # Amarelo, Preto
    "Guarani": ["#008000", "#FFFFFF"],  # Verde, Branco
    "Londrina": ["#0033A0", "#FFFFFF"],  # Azul, Branco
    "Paraná Clube": ["#0033A0", "#FF0000", "#FFFFFF"],  # Azul, Vermelho, Branco
    "Ponte Preta": ["#000000", "#FFFFFF"],  # Preto, Branco
    "Sampaio Corrêa": ["#008000", "#FFD700", "#FF0000"],  # Verde, Amarelo, Vermelho
    "São Caetano": ["#0033A0", "#FFFFFF"],  # Azul, Branco
    "Vila Nova": ["#FF0000", "#FFFFFF"],  # Vermelho, Branco
    "Atlético Goianiense": ["#FF0000", "#000000"],  # Vermelho, Preto
    "CSA": ["#0033A0", "#FFFFFF"],  # Azul, Branco
    "CRB": ["#FF0000", "#FFFFFF"],  # Vermelho, Branco

    # 50 clubes mais famosos do mundo
    "Barcelona": ["#004D98", "#A50044"],  # Azul, Grená
    "Real Madrid": ["#FFFFFF"],  # Branco
    "Manchester United": ["#DA291C", "#000000"],  # Vermelho, Preto
    "Liverpool": ["#C8102E"],  # Vermelho
    "Bayern de Munique": ["#DC052D", "#FFFFFF"],  # Vermelho, Branco
    "Paris Saint-Germain": ["#004170", "#DA291C"],  # Azul, Vermelho
    "Juventus": ["#000000", "#FFFFFF"],  # Preto, Branco
    "Chelsea": ["#034694", "#FFFFFF"],  # Azul, Branco
    "Manchester City": ["#6CABDD", "#FFFFFF"],  # Azul Claro, Branco
    "Arsenal": ["#EF0107", "#FFFFFF"],  # Vermelho, Branco
    "Milan": ["#FB090B", "#000000"],  # Vermelho, Preto
    "Inter de Milão": ["#003366", "#000000"],  # Azul, Preto
    "Ajax": ["#D42029", "#FFFFFF"],  # Vermelho, Branco
    "Benfica": ["#FF0000", "#FFFFFF"],  # Vermelho, Branco
    "Porto": ["#0033A0", "#FFFFFF"],  # Azul, Branco
    "Boca Juniors": ["#0033A0", "#FFD700"],  # Azul, Amarelo
    "River Plate": ["#FFFFFF", "#FF0000"],  # Branco, Vermelho
    "Peñarol": ["#FFD700", "#000000"],  # Amarelo, Preto
    "Nacional": ["#0033A0", "#FF0000", "#FFFFFF"],  # Azul, Vermelho, Branco
    "Independiente": ["#FF0000", "#FFFFFF"],  # Vermelho, Branco
    "Al Ahly": ["#FF0000", "#FFFFFF"],  # Vermelho, Branco
    "Tottenham Hotspur": ["#FFFFFF", "#132257"],  # Branco, Azul
    "Borussia Dortmund": ["#FDE100", "#000000"],  # Amarelo, Preto
    "Atletico Madrid": ["#D7141A", "#FFFFFF"],  # Vermelho, Branco
    "Sevilla": ["#FFFFFF", "#D7141A"],  # Branco, Vermelho
    "Roma": ["#8E1B1B", "#FFD700"],  # Vermelho, Amarelo
    "Lazio": ["#B2DFF4", "#FFFFFF"],  # Azul Claro, Branco
    "Napoli": ["#0064A8", "#FFFFFF"],  # Azul Claro, Branco
    "Galatasaray": ["#A32638", "#FFD700"],  # Vermelho, Amarelo
    "Olympique de Marseille": ["#0080FF", "#FFFFFF"],  # Azul Claro, Branco
    "Lyon": ["#004494", "#FFFFFF", "#D7141A"],  # Azul, Branco, Vermelho
    "PSV Eindhoven": ["#DA291C", "#FFFFFF"],  # Vermelho, Branco
    "Red Bull Salzburg": ["#FF0000", "#FFFFFF"],  # Vermelho, Branco
    "Shakhtar Donetsk": ["#F36F21", "#000000"],  # Laranja, Preto
    "Al Hilal": ["#005BAC", "#FFFFFF"],  # Azul, Branco

    # Times da NBA
    "Atlanta Hawks": ["#E03A3E", "#C1D32F"],  # Vermelho, Verde
    "Boston Celtics": ["#007A33", "#BA9653"],  # Verde, Dourado
    "Brooklyn Nets": ["#000000", "#FFFFFF"],  # Preto, Branco
    "Charlotte Hornets": ["#1D1160", "#00788C"],  # Roxo, Azul Claro
    "Chicago Bulls": ["#CE1141", "#000000"],  # Vermelho, Preto
    "Cleveland Cavaliers": ["#860038", "#FDBB30"],  # Vermelho, Dourado
    "Dallas Mavericks": ["#00538C", "#002B5E"],  # Azul, Azul Escuro
    "Denver Nuggets": ["#0E2240", "#FEC524"],  # Azul, Amarelo
    "Detroit Pistons": ["#C8102E", "#1D42BA"],  # Vermelho, Azul
    "Golden State Warriors": ["#1D428A", "#FFC72C"],  # Azul, Amarelo
    "Houston Rockets": ["#CE1141", "#C4CED4"],  # Vermelho, Cinza
    "Indiana Pacers": ["#002D62", "#FDBB30"],  # Azul, Amarelo
    "LA Clippers": ["#C8102E", "#1D428A"],  # Vermelho, Azul
    "Los Angeles Lakers": ["#552583", "#FDB927"],  # Roxo, Amarelo
    "Memphis Grizzlies": ["#5D76A9", "#12173F"],  # Azul, Azul Escuro
    "Miami Heat": ["#98002E", "#F9A01B"],  # Vermelho, Amarelo
    "Milwaukee Bucks": ["#00471B", "#EEE1C6"],  # Verde, Creme
    "Minnesota Timberwolves": ["#0C2340", "#236192"],  # Azul, Azul Claro
    "New Orleans Pelicans": ["#0C2340", "#C8102E"],  # Azul, Vermelho
    "New York Knicks": ["#006BB6", "#F58426"],  # Azul, Laranja
    "Oklahoma City Thunder": ["#007AC1", "#EF3B24"],  # Azul, Laranja
    "Orlando Magic": ["#0077C0", "#C4CED4"],  # Azul, Cinza
    "Philadelphia 76ers": ["#006BB6", "#ED174C"],  # Azul, Vermelho
    "Phoenix Suns": ["#1D1160", "#E56020"],  # Roxo, Laranja
    "Portland Trail Blazers": ["#E03A3E", "#000000"],  # Vermelho, Preto
    "Sacramento Kings": ["#5A2D81", "#63727A"],  # Roxo, Cinza
    "San Antonio Spurs": ["#C4CED4", "#000000"],  # Cinza, Preto
    "Toronto Raptors": ["#CE1141", "#000000"],  # Vermelho, Preto
    "Utah Jazz": ["#002B5C", "#F9A01B"],  # Azul, Amarelo
    "Washington Wizards": ["#002B5C", "#E31837"],  # Azul, Vermelho
}
