import scrapper


def get_mail_template():
    return """
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>COVID Email</title>
    <link href="https://fonts.googleapis.com/css2?family=Rubik:wght@500&display=swap" rel="stylesheet">
    <link href="https://fonts.googleapis.com/css2?family=Source+Sans+Pro:wght@200&display=swap" rel="stylesheet">

    <style type="text/css">
        ul {
            list-style-type: none;
            padding: 0;
        }

        li {
            margin-top: 5%;
        }

        .container {
            margin: auto;
            width: 50%;
            padding: 10px;
        }

        .header {
            font-family: 'Rubik', sans-serif;
        }

        .main {
            font-family: 'Source Sans Pro', sans-serif;
            font-size: 150%;
        }

        .main-poland p {
            margin-top: 1%;
            margin-bottom: 1%;
        }

        .inner-ul {
            display: flex;
        }

        .inner-ul-li-ico {
            margin-right: 5%;
        }



        @media only screen and (max-width: 414px) {
            .main {
                font-size: 78%;
            }
        }

        @media only screen and (max-width: 411px) {
            .main {
                font-size: 70%;
            }
        }

        @media only screen and (max-width: 360px) {
            .main {
                font-size: 60%;
            }

            .title {
                font-size: 70%;
            }
        }
    </style>
</head>

<body>
    <div class="container">
        <div class="header">
            <h1 class="title">🦠 COVID-19 DAILY SUMMARY</h1>
        </div>
        <div class="main">
            <div class="main-worldwide">
                <h4>🌎 WORLDWIDE </h4>
                <p>""" + scrapper.get_world_data() + """
                </p>
            </div>
            <hr>
            <div class="main-poland">
                <h4>🇵🇱 POLAND </h4>
                <p>""" + scrapper.get_pl_data() + """
                </p>
                <br>
                <p>""" + scrapper.get_pl_deaths() + """
                </p>
                <br>
                <p>""" + scrapper.get_difference() + """
                </p>
            </div>
        </div>
    </div>
</body>

</html>
    """
