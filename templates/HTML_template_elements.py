"""
Templates and functions for making the results HTML file.

SpiceBucks
"""

HEADER = '''<!DOCTYPE html>
<html>
<head>

  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="generator" content="Mobirise v4.10.6, mobirise.com">
  <meta name="viewport" content="width=device-width, initial-scale=1, minimum-scale=1">
  <link rel="shortcut icon" href="assets/images/mbr-122x86.jpg" type="image/x-icon">
  <meta name="description" content="Lockdown Olympics - Homepage">
  
  <title>Registration</title>
  <link rel="stylesheet" href="assets/web/assets/mobirise-icons/mobirise-icons.css">
  <link rel="stylesheet" href="assets/tether/tether.min.css">
  <link rel="stylesheet" href="assets/bootstrap/css/bootstrap.min.css">
  <link rel="stylesheet" href="assets/bootstrap/css/bootstrap-grid.min.css">
  <link rel="stylesheet" href="assets/bootstrap/css/bootstrap-reboot.min.css">
  <link rel="stylesheet" href="assets/dropdown/css/style.css">
  <link rel="stylesheet" href="assets/animatecss/animate.min.css">
  <link rel="stylesheet" href="assets/theme/css/style.css">
  <link rel="stylesheet" href="assets/mobirise/css/mbr-additional.css" type="text/css">
  <link rel="stylesheet" href="assets/css/all.css">

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
<script src="assets/web/assets/jquery/jquery.min.js"></script>
  <script src="assets/popper/popper.min.js"></script>
  <script src="assets/tether/tether.min.js"></script>
  <script src="assets/bootstrap/js/bootstrap.min.js"></script>
  <script src="assets/smoothscroll/smooth-scroll.js"></script>
  <script src="assets/dropdown/js/nav-dropdown.js"></script>
  <script src="assets/dropdown/js/navbar-dropdown.js"></script>
  <script src="assets/touchswipe/jquery.touch-swipe.min.js"></script>
  <script src="assets/viewportchecker/jquery.viewportchecker.js"></script>
  <script src="assets/theme/js/script.js"></script>
  <script src="assets/formoid/formoid.min.js"></script>

  <div id="scrollToTop" class="scrollToTop mbr-arrow-up"><a style="text-align: center;"><i class="mbr-arrow-up-icon mbr-arrow-up-icon-cm cm-icon cm-icon-smallarrow-up"></i></a></div>
    <input name="animation" type="hidden">
</html>'''

def make_div(result):
    ret = "<table style=width:100%> <tr>"
    ret += "<th><h1>" + result["Name"] + "</h1> <h2> " + "Estimated Winning Profit on a £100 total bet:" + result["Arbitrage Opportunity"] + "</h2></th></tr>"
    ret += '<tr><td><h3> <a href="' + result["Link"] + '"> ' + '<button class="btn btn-primary btn-form display-4">Click to bet now!' + '</button></a></h3> <br/> </td> </tr>'
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
