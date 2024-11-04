import codecs

with open('picmap.csv') as f:
    lines = f.readlines()
    infos = []
    floors = set()

    for line in lines:
        infos.append(line.split('\t'))
        floors.add(infos[-1][0])

colors = {
    'nnz': {'normal': '#923a8d', 'dark': '#491d47'},
    '_nz': {'normal': '#0db3a5', 'dark': '#07665e'},
    'sz': {'normal': '#ff8e3d', 'dark': '#b3632d'}
}

for floor in floors:
    with codecs.open('./schemes/' + floor + '.html', 'w', "utf-8-sig") as f:
        f.write('<!doctype html>'
                '<html>'
                '<head>'
                '   <meta charset="UTF-8">'
                '   <title>Панорамы гимназии 1514</title>'
                """ 
                    <link rel="stylesheet" href="../reset.css" />
                    <link href="https://fonts.googleapis.com/css?family=Philosopher" rel="stylesheet">
                    <link rel="stylesheet" href="../project.css" />
                    <link rel="shortcut icon" href="favicon.ico" type="image/x-icon">
                    <link rel="stylesheet" href="https://cdn.pannellum.org/2.4/pannellum.css"/>
                    <script type="text/javascript" src="https://cdn.pannellum.org/2.4/pannellum.js"></script>
                    <script
                      src="https://code.jquery.com/jquery-1.12.4.min.js"
                      integrity="sha256-ZosEbRLbNQzLpnKIkEdrPv7lOy9C27hHQ+Xp8a4MxAQ="
                      crossorigin="anonymous"></script>"""
                '   <script type="text/javascript" src="../jquery.imagemapster.js"></script>'
                '<script>'
                '$(window).load(function(){'
                """ var image = $("#scheme");
                    image.mapster(
                    {
                        fillOpacity: 0.5,""")
        f.write('''
                        fillColor: "{}",
                        stroke: true,
                        strokeColor: "{}",
                        strokeOpacity: 0.5,
                        strokeWidth: 2,
                        singleSelect: true,
                        mapKey: "name",
                        listKey: "name",
                        '''.format(colors[floor[:-1]]['normal'][1:], colors[floor[:-1]]['dark'][1:]))
        f.write("""     showToolTip: true,
                        toolTipClose: ["tooltip-click", "area-click"],
                        areas: [""")

        for info in infos:
            if info[0] == floor:
                # f.write('{{ key: "{}", toolTip: $("<img class=\'pic-preview\' src=\'../preview/pano{}.jpg\' />")}},'.format(info[1], info[1]))
                f.write("""
                {{ key: "{}", toolTip: $(\'<iframe width="400" height="234" allowfullscreen style="border-style:none;" src="../iframes/{}.html"></iframe>\')}},""".format(
                    info[1], info[1]))

        f.write("""
                            ]
                    });

                });
                """)
        f.write('</script></head><body class="scheme {}">'.format(floor[:-1]))

        f.write('<img id="scheme" src="./img/{}.jpg" usemap="#map_scheme" width="100%"/>'.format(floor))
        f.write('<map id="map_scheme" name="map_scheme">')

        for info in infos:
            if info[0] == floor:
                f.write('<area name={} {} href="#" />'.format(info[1], info[2].strip()[40:-1]))

        f.write('</map>')
        # f.write('<script>')
        # for info in infos:
        #     if info[0] == floor:
        #         f.write("""
        #         pannellum.viewer('pano{}', {{
        #                 "type": "equirectangular",
        #                 "panorama": "../pano/pano{}.jpg",
        #                 "preview": "../preview/pano{}.jpg"
        #         }});
        #         """.format(info[1], info[1], info[1]))
        #
        # f.write('</script>')
        f.write('</body></html>')