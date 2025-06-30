import svg
from textwrap import dedent

STROKE_LEN = 10
GAP = 10
START=25
END = 230
WIDTH = 210
HEIGHT = 297

SHIFT = int(STROKE_LEN / 2)
STEP = 25


def draw() -> svg.SVG:
    elements: list[svg.Element] = []
    path = []
   
    # elements.append(svg.Style(
    #             text=dedent("""
    #                 .small { font: italic 13px sans-serif; }
    #                 .heavy { font: bold 30px sans-serif; }
    #                 .luciole {font: bold 24px luciole;}
    #                 /* Note that the color of the text is set with the    *
    #                 * fill property, the color property is for HTML only */
    #                 .Rrrrr { font: italic 40px serif; fill: red; }
    #             """),
    #         )
    # )
    
    for l in range(START, END, STEP):
        txt = svg.Text(text=str(l), x=50, y=l + SHIFT)
        #elements.append (svg.Text(text=str(l), x=50, y=l + SHIFT, class_='luciole'))
        txt.style = "font: bold 16 Luciole;"
        elements.append(txt)
    testsvg = svg.SVG(
        viewBox=svg.ViewBoxSpec(0, 0, WIDTH, HEIGHT),
        width=svg.mm(WIDTH),
        height=svg.mm(HEIGHT),
        elements=elements,
    )

    with open("test.svg", 'w') as f:
        f.write(str(testsvg))


if __name__ == '__main__':
    print(draw())