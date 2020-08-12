"""
Templates and functions for making the results HTML file.

SpiceBucks
"""

HEADER = '''<!DOCTYPE html>
<html>
<head>
<style>
table, th, tr, td {
  border: 1px solid black;
  border-collapse: collapse;
  text-align: center;
}
.center {
  display: block;
  margin-left: auto;
  margin-right: auto;
  width: 50%;
}
</style>
<meta charset="UTF-8">
<title>Arbitrage Finder</title>
</head>
<body>
<img src="templates/logo.jpg" alt="Arbitrage Finder" class="center">'''

FOOTER = '''</body>
</html>'''

def make_div(result):
    ret = "<table style=width:100%> <tr>"
    ret += "<th><h1>" + result["Name"] + "</h1> <h2> " + "Estimated Winning Profit on a £100 total bet:" + result["Arbitrage Opportunity"] + "</h2></th></tr>"
    ret += '<tr><td><h3> <a href="' + result["Link"] + '"> ' + '<button>Click to bet now!' + '</button></a></h3> <br/> </td> </tr>'
    for r in result["Instructions"]:
        ret += "<tr><td><span> " + r + "<br /> </span></td></tr>"
    ret += "</table>"
    return ret

def make_html(res_list):
    ret = HEADER
    for r in res_list:
        ret += make_div(r)
    ret += FOOTER
    return ret
