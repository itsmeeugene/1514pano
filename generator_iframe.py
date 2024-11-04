import codecs

with open('picmap.csv') as f:
    lines = f.readlines()
    infos = []
    floors = set()

    for line in lines:
        infos.append(line.split('\t'))
        floors.add(infos[-1][0])

with open('titles.csv') as f:
    lines = f.readlines()
    titles = dict()
    for line in lines:
        no, title = line.split('\t')
        titles[no] = title.rstrip('\n')

print(titles)

for info in infos:
    with codecs.open("./iframes/" + info[1] + '.html', 'w', "utf-8-sig") as f:
        code = """
        <!DOCTYPE HTML>
        <html>
        <head>
            <meta charset="utf-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title></title>
            <link rel="stylesheet" href="https://cdn.pannellum.org/2.4/pannellum.css"/>
            <script type="text/javascript" src="https://cdn.pannellum.org/2.4/pannellum.js"></script>
			<script
                      src="https://code.jquery.com/jquery-1.12.4.min.js"
                      integrity="sha256-ZosEbRLbNQzLpnKIkEdrPv7lOy9C27hHQ+Xp8a4MxAQ="
                      crossorigin="anonymous"></script>
			<link rel="stylesheet" href="../reset.css" />
            <style>
			html, body, #panorama{{
				width: 100%;
                height: 100%;
			}}
            </style>
        </head>
        <body>

        <div id="panorama"></div>
        <script>
        pannellum.viewer('panorama', {{
            "type": "equirectangular",
            "panorama": "../pano/pano{}.jpg",
            "preview": "../preview/pano{}.jpg"
        }});
        $('.pnlm-load-button').html('<p>{}<p>');
        </script>

        </body>
        </html>
        """.format(info[1], info[1], titles[info[1]])

        f.write(code)
