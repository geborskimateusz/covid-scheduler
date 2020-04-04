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

            display: flex;
            flex-direction: row;
            justify-content: center;

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
            <h1 class="title">🦠 COVID-19 DAILY</h1>
        </div>
        <div class="main">
            <ul>
                <li>
                    <ul class="inner-ul">
                        <li class="inner-ul-li-ico">🌎 </li>
                        <li>{}</li>
                    </ul>
                </li>
                <li>
                    <ul class="inner-ul">
                        <li class="inner-ul-li-ico">🇵🇱 </li>
                        <li>{}</li>
                    </ul>
                </li>
            </ul>
        </div>
    </div>
</body>

</html>
    """.format(scrapper.get_world_data(), scrapper.get_pl_data())
