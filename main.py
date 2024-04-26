from flask import Flask, request, render_template_string

app = Flask(__name__)

# Your data, assuming it's already converted from the Excel sheet into a list of dictionaries
data = [
    {'Rank': 1, 'Team Name': 'DU_UNSATISFIEDSOULS', 'University': 'UNIVERSITY OF DHAKA', 'Score': 90.5, 'Status': 'Qualified'},
    {'Rank': 2, 'Team Name': 'YOUR WORST NIGHTMARE', 'University': 'SHAHJALAL UNIVERSITY OF SCIENCE & TECHNOLOGY', 'Score': 89.0, 'Status': 'Qualified'},
    {'Rank': 2, 'Team Name': 'DU_TRIPLEHASH', 'University': 'UNIVERSITY OF DHAKA', 'Score': 89.0, 'Status': 'Qualified'},
    {'Rank': 2, 'Team Name': 'RU LEGION', 'University': 'UNIVERSITY OF RAJSHAHI', 'Score': 89.0, 'Status': 'Qualified'},
    {'Rank': 5, 'Team Name': 'QUANTUM GUYS', 'University': 'JAGANNATH UNIVERSITY', 'Score': 88.5, 'Status': 'Qualified'},
    {'Rank': 5, 'Team Name': 'DU_KKHO', 'University': 'UNIVERSITY OF DHAKA', 'Score': 88.5, 'Status': 'Qualified'},
    {'Rank': 7, 'Team Name': 'BUET STORMS END', 'University': 'BANGLADESH UNIVERSITY OF ENGINEERING AND TECHNOLOGY', 'Score': 88.0, 'Status': 'Qualified'},
    {'Rank': 8, 'Team Name': 'TEAM NANDE', 'University': 'SHAHJALAL UNIVERSITY OF SCIENCE & TECHNOLOGY', 'Score': 87.0, 'Status': 'Qualified'},
    {'Rank': 9, 'Team Name': 'JUST_POWER_RANGERS', 'University': 'JASHORE UNIVERSITY OF SCIENCE AND TECHNOLOGY', 'Score': 85.0, 'Status': 'Qualified'},
    {'Rank': 10, 'Team Name': 'সাস্ট_জিপিটিযোদ্ধা', 'University': 'SHAHJALAL UNIVERSITY OF SCIENCE & TECHNOLOGY', 'Score': 84.5, 'Status': 'Qualified'},
    {'Rank': 11, 'Team Name': 'SAMURAI SQUAD', 'University': 'SHAHJALAL UNIVERSITY OF SCIENCE & TECHNOLOGY', 'Score': 84.0, 'Status': 'Qualified'},
    {'Rank': 12, 'Team Name': 'DU_RAEMON', 'University': 'UNIVERSITY OF DHAKA', 'Score': 83.0, 'Status': 'Qualified'},
    {'Rank': 13, 'Team Name': 'CU_CODECONQUEST', 'University': 'UNIVERSITY OF CHITTAGONG', 'Score': 82.5, 'Status': 'Qualified'},
    {'Rank': 14, 'Team Name': 'DU_PROMETHEUS', 'University': 'UNIVERSITY OF DHAKA', 'Score': 82.0, 'Status': 'Qualified'},
    {'Rank': 14, 'Team Name': 'ONTORPONTHIK', 'University': 'SHAHJALAL UNIVERSITY OF SCIENCE & TECHNOLOGY', 'Score': 82.0, 'Status': 'Qualified'},
    {'Rank': 16, 'Team Name': 'RUET_UNKNOWNS', 'University': 'RAJSHAHI UNIVERISTY OF ENGINEERING AND TECHNOLOGY', 'Score': 81.0, 'Status': 'Qualified'},
    {'Rank': 16, 'Team Name': 'DEFINE CODERS', 'University': 'SHAHJALAL UNIVERSITY OF SCIENCE & TECHNOLOGY', 'Score': 81.0, 'Status': 'Qualified'},
    {'Rank': 16, 'Team Name': 'Homo_sapiens', 'University': 'SHAHJALAL UNIVERSITY OF SCIENCE & TECHNOLOGY', 'Score': 81.0, 'Status': 'Qualified'},
    {'Rank': 19, 'Team Name': 'DU_STRONG_ENOUGH', 'University': 'UNIVERSITY OF DHAKA', 'Score': 80.5, 'Status': 'Qualified'},
    {'Rank': 19, 'Team Name': 'DU_DILIGENCE', 'University': 'UNIVERSITY OF DHAKA', 'Score': 80.5, 'Status': 'Qualified'},
    {'Rank': 21, 'Team Name': 'UNTITLED', 'University': 'DAFFODIL INTERNATIONAL UNIVERSITY', 'Score': 80.0, 'Status': 'Qualified'},
    {'Rank': 22, 'Team Name': 'JUST_NINJAS', 'University': 'JASHORE UNIVERSITY OF SCIENCE AND TECHNOLOGY', 'Score': 79.0, 'Status': 'Qualified'},
    {'Rank': 23, 'Team Name': 'HERE_WE_GO_AGAIN', 'University': 'INTERNATIONAL ISLAMIC UNIVERSITY CHITTAGONG', 'Score': 78.0, 'Status': 'Qualified'},
    {'Rank': 24, 'Team Name': 'JU-METRONOME', 'University': 'JAHANGIRNAGAR UNIVERSITY', 'Score': 76.5, 'Status': 'Qualified'},
    {'Rank': 24, 'Team Name': 'NOWAYHOME', 'University': 'SHAHJALAL UNIVERSITY OF SCIENCE & TECHNOLOGY', 'Score': 76.5, 'Status': 'Not Qualified'},
    {'Rank': 26, 'Team Name': 'IUT ALT_F4', 'University': 'ISLAMIC UNIVERSITY OF TECHNOLOGY', 'Score': 76.0, 'Status': 'Qualified'},
    {'Rank': 26, 'Team Name': 'LAZY_CODERS', 'University': 'UNIVERSITY OF RAJSHAHI', 'Score': 76.0, 'Status': 'Qualified'},
    {'Rank': 28, 'Team Name': 'JU_AMADEUS', 'University': 'JAHANGIRNAGAR UNIVERSITY', 'Score': 75.0, 'Status': 'Qualified'},
    {'Rank': 29, 'Team Name': 'JUST_Paraffin', 'University': 'JASHORE UNIVERSITY OF SCIENCE AND TECHNOLOGY', 'Score': 74.5, 'Status': 'Qualified'},
    {'Rank': 30, 'Team Name': 'BOLBONA', 'University': 'PABNA UNIVERSITY OF SCIENCE AND TECHNOLOGY', 'Score': 74.0, 'Status': 'Qualified'},
    {'Rank': 30, 'Team Name': 'CUET_OFF_WE_GO', 'University': 'CHITTAGONG UNIVERSITY OF ENGINEERING AND TECHNOLOGY', 'Score': 74.0, 'Status': 'Qualified'},
    {'Rank': 30, 'Team Name': 'TEAM SUPPLY', 'University': 'INTERNATIONAL ISLAMIC UNIVERSITY CHITTAGONG', 'Score': 74.0, 'Status': 'Qualified'},
    {'Rank': 33, 'Team Name': 'MIST_MZM', 'University': 'MILITARY INSTITUTE OF SCIENCE AND TECHNOLOGY', 'Score': 73.5, 'Status': 'Qualified'},
    {'Rank': 34, 'Team Name': 'UNIT 7', 'University': 'BANGABANDHU SHEIKH MUJIBUR RAHMAN SCIENCE AND TECHNOLOGY UNIVERSITY', 'Score': 73.0, 'Status': 'Qualified'},
    {'Rank': 35, 'Team Name': 'Randomthree', 'University': 'INTERNATIONAL ISLAMIC UNIVERSITY CHITTAGONG', 'Score': 71.5, 'Status': 'Qualified'},
    {'Rank': 36, 'Team Name': 'BSMRSTU_Prefect_Number', 'University': 'BANGABANDHU SHEIKH MUJIBUR RAHMAN SCIENCE AND TECHNOLOGY UNIVERSITY', 'Score': 70.0, 'Status': 'Qualified'},
    {'Rank': 37, 'Team Name': 'TEAM_MATRIX', 'University': 'BRAC UNIVERSITY', 'Score': 69.0, 'Status': 'Qualified'},
    {'Rank': 38, 'Team Name': 'DU_ALGORHYTHMS', 'University': 'UNIVERSITY OF DHAKA', 'Score': 68.0, 'Status': 'Not Qualified'},
    {'Rank': 39, 'Team Name': 'OPTIMISTS', 'University': 'UNIVERSITY OF DHAKA', 'Score': 67.0, 'Status': 'Not Qualified'},
    {'Rank': 40, 'Team Name': 'VANGA BOYZ', 'University': 'CHITTAGONG UNIVERSITY OF ENGINEERING AND TECHNOLOGY', 'Score': 66.5, 'Status': 'Qualified'},
    {'Rank': 41, 'Team Name': 'DU_NO_FEAR', 'University': 'UNIVERSITY OF DHAKA', 'Score': 66.0, 'Status': 'Not Qualified'},
    {'Rank': 42, 'Team Name': 'TEAM ENDEAVOR', 'University': 'SHAHJALAL UNIVERSITY OF SCIENCE & TECHNOLOGY', 'Score': 65.0, 'Status': 'Not Qualified'},
    {'Rank': 43, 'Team Name': 'TEAM_OMNITRIX', 'University': 'UNITED INTERNATIONAL UNIVERSITY', 'Score': 64.5, 'Status': 'Qualified'},
    {'Rank': 44, 'Team Name': 'TEAM_DATE_EXPIRED', 'University': 'UNIVERSITY OF BARISHAL', 'Score': 64.0, 'Status': 'Qualified'},
    {'Rank': 45, 'Team Name': 'THE_CHIEFS', 'University': 'UNIVERSITY OF BARISHAL', 'Score': 63.0, 'Status': 'Qualified'},
    {'Rank': 45, 'Team Name': 'DOMAIN_EXPANSION', 'University': 'CHITTAGONG UNIVERSITY OF ENGINEERING AND TECHNOLOGY', 'Score': 63.0, 'Status': 'Qualified'},
    {'Rank': 45, 'Team Name': 'GREEN THUNDER', 'University': 'GREEN UNIVERSITY OF BANGLADESH', 'Score': 63.0, 'Status': 'Qualified'},
    {'Rank': 45, 'Team Name': 'Team Codex', 'University': 'SHANTO MARIAM UNIVERSITY OF CREATIVE TECHNOLOGY', 'Score': 63.0, 'Status': 'Qualified'},
    {'Rank': 49, 'Team Name': 'BUET_SYNTAXERROR', 'University': 'BANGLADESH UNIVERSITY OF ENGINEERING AND TECHNOLOGY', 'Score': 62.0, 'Status': 'Qualified'},
    {'Rank': 50, 'Team Name': 'LIQUIDATORS', 'University': 'SHAHJALAL UNIVERSITY OF SCIENCE & TECHNOLOGY', 'Score': 61.0, 'Status': 'Not Qualified'},
    {'Rank': 50, 'Team Name': 'AUST_THE_FINAL_FRONTIER', 'University': 'AHSANULLAH UNIVERSITY OF SCIENCE AND TECHNOLOGY', 'Score': 61.0, 'Status': 'Qualified'},
    {'Rank': 50, 'Team Name': 'DIIT_RUNTIME_TERROR', 'University': 'DAFFODIL INSTITUTE OF IT', 'Score': 61.0, 'Status': 'Qualified'},
    {'Rank': 53, 'Team Name': 'ZIMA BLUE', 'University': 'UNIVERSITY OF DHAKA', 'Score': 60.0, 'Status': 'Not Qualified'},
    {'Rank': 54, 'Team Name': 'DJANGO', 'University': 'INTERNATIONAL UNIVERSITY OF BUSINESS AGRICULTURE AND TECHNOLOGY', 'Score': 59.0, 'Status': 'Not Qualified'},
    {'Rank': 54, 'Team Name': 'MURIRTEAM', 'University': 'BANGLADESH UNIVERSITY OF ENGINEERING AND TECHNOLOGY', 'Score': 59.0, 'Status': 'Not Qualified'},
    {'Rank': 56, 'Team Name': 'BSMRSTU_FUSINGBRILLIANCE', 'University': 'BANGABANDHU SHEIKH MUJIBUR RAHMAN SCIENCE AND TECHNOLOGY UNIVERSITY', 'Score': 57.0, 'Status': 'Not Qualified'},
    {'Rank': 57, 'Team Name': 'DU_ROUNDRONIN', 'University': 'UNIVERSITY OF DHAKA', 'Score': 54.5, 'Status': 'Not Qualified'},
    {'Rank': 58, 'Team Name': 'TEAM_DEADBEEF', 'University': 'ISLAMIC UNIVERSITY OF TECHNOLOGY', 'Score': 53.0, 'Status': 'Not Qualified'},
    {'Rank': 59, 'Team Name': 'Straw Hats', 'University': 'BANGLADESH UNIVERSITY OF ENGINEERING AND TECHNOLOGY', 'Score': 52.0, 'Status': 'Not Qualified'},
    {'Rank': 60, 'Team Name': 'BYTE_FUSION', 'University': 'Compact Polytechnic Institute', 'Score': 49.0, 'Status': 'Not Qualified'},
    {'Rank': 61, 'Team Name': 'ALPHA CENTAURI', 'University': 'RANGAMATI SCIENCE & TECHNOLOGY UNIVERSITY', 'Score': 47.0, 'Status': 'Not Qualified'},
    {'Rank': 62, 'Team Name': 'BLOCKBUSTER', 'University': 'INTERNATIONAL UNIVERSITY OF BUSINESS AGRICULTURE AND TECHNOLOGY', 'Score': 42.0, 'Status': 'Not Qualified'}
]

# HTML template as a string
template = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>University Team Search</title>
    <style>
        body {
            font-family: 'Arial', sans-serif;
            background-color: #f4f4f4;
            margin: 0;
            padding: 20px;
            color: #333;
        }
        h1 {
            color: #444;
        }
        form {
            background: #fff;
            padding: 20px;
            border-radius: 5px;
            box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
            margin-bottom: 20px;
        }
        label {
            display: block;
            margin-top: 10px;
            color: #666;
        }
        select, input[type="text"] {
            width: 100%;
            padding: 10px;
            margin-top: 5px;
            border-radius: 5px;
            border: 1px solid #ddd;
            box-sizing: border-box; /* Added to fix width issues */
        }
        input[type="submit"] {
            background: #5cb85c;
            color: white;
            padding: 10px 20px;
            border: none;
            border-radius: 5px;
            cursor: pointer;
            margin-top: 10px;
        }
        input[type="submit"]:hover {
            background: #4cae4c;
        }
        ul {
            list-style: none;
            padding: 0;
        }
        ul li {
            background: #fff;
            padding: 10px;
            border-radius: 5px;
            margin-bottom: 5px;
            box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
        }
        ul li:nth-child(even) {
            background: #f8f8f8;
        }
    </style>
</head>
<body>
    <h1>Search for Teams</h1>
    <form action="/" method="post">
        <label for="university">Choose a university:</label>
        <select name="university" id="university">
            <option value="">All Universities</option>
            {% for uni in universities %}
            <option value="{{ uni }}">{{ uni }}</option>
            {% endfor %}
        </select>
        
        <label for="team_name">Team Name:</label>
        <input type="text" id="team_name" name="team_name">
        
        <input type="submit" value="Search">
    </form>
    
    {% if teams %}
        <h2>Search Results:</h2>
        <ul>
            {% for team in teams %}
                <li>
                    <strong>{{ team['Rank'] }}</strong>: {{ team['Team Name'] }} - 
                    {{ team['University'] }} - Score: {{ team['Score'] }} - 
                    Status: <b> {{ team['Status'] }} </b>
                </li>
            {% endfor %}
        </ul>
    {% endif %}
</body>
</html>
"""

@app.route('/', methods=['GET', 'POST'])
def index():
    universities = sorted(set(team['University'] for team in data))
    teams = []
    if request.method == 'POST':
        university = request.form.get('university')
        team_name = request.form.get('team_name', '').upper()
        teams = [team for team in data if team['University'] == university and team_name in team['Team Name'].upper()]
    return render_template_string(template, universities=universities, teams=teams)

if __name__ == "__main__":
    app.run(debug=True)
