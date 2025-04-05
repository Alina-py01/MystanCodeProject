"""
File: 
Name:Alina
----------------------
TODO:
"""

from campy.graphics.gobjects import GOval, GRect, GPolygon, GLabel, GLine, GArc
from campy.graphics.gwindow import GWindow


def main():
    """
    Title: lucky cat

    This cat can bring blessings and good luck to people.
    I hope that everyone will be blessed in the new year, have their dreams come true, and
    move forward with a positive outlook.
    """
    window = GWindow(width=800, height=600, title='招財貓')

    # body
    body = GOval(270, 280, x=265, y=220)
    body.filled = True
    body.fill_color = 'white'
    window.add(body)

    # head
    head = GOval(200, 200, x=300, y=100)
    head.filled = True
    head.fill_color = 'white'
    window.add(head)

    # little bell
    bell = GOval(30, 30, x=385, y=280)
    bell.filled = True
    bell.fill_color = 'gold'
    window.add(bell)

    bell_strap = GLine(400, 295, 400, 310)
    bell_strap.color = 'black'
    window.add(bell_strap)
    # left eye
    left_eye = GArc(45, 40, 0, 160)
    left_eye.filled = False
    left_eye.color = 'black'
    window.add(left_eye, x=330, y=180)

    # right eye
    right_eye = GArc(45, 40, 0, 160)
    right_eye.filled = False
    right_eye.color = 'black'
    window.add(right_eye, x=415, y=180)

    # left ear
    left_ear = GPolygon()
    left_ear.add_vertex((330, 140))
    left_ear.add_vertex((350, 60))
    left_ear.add_vertex((370, 140))
    left_ear.filled = True
    left_ear.fill_color = 'white'
    window.add(left_ear)

    # inside left ear
    left_inner_ear = GPolygon()
    left_inner_ear.add_vertex((340, 130))
    left_inner_ear.add_vertex((350, 90))
    left_inner_ear.add_vertex((360, 130))
    left_inner_ear.filled = True
    left_inner_ear.fill_color = 'pink'
    window.add(left_inner_ear)

    # right ear
    right_ear = GPolygon()
    right_ear.add_vertex((420, 140))
    right_ear.add_vertex((440, 60))
    right_ear.add_vertex((460, 140))
    right_ear.filled = True
    right_ear.fill_color = 'white'
    window.add(right_ear)

    # inside right ear
    right_inner_ear = GPolygon()
    right_inner_ear.add_vertex((430, 130))
    right_inner_ear.add_vertex((440, 90))
    right_inner_ear.add_vertex((450, 130))
    right_inner_ear.filled = True
    right_inner_ear.fill_color = 'pink'
    window.add(right_inner_ear)

    # nose
    nose = GOval(15, 10, x=385, y=200)
    nose.filled = True
    nose.fill_color = 'pink'
    window.add(nose)

    # mouth
    mouth_left = GArc(40, 40, 200, 165)
    mouth_left.color = 'black'
    window.add(mouth_left, x=355, y=200)

    mouth_right = GArc(40, 40, 200, 165)
    mouth_right.color = 'black'
    window.add(mouth_right, x=395, y=200)

    # the whiskers on the left
    left_whisker_top = GLine(350, 220, 320, 210)  # left upper whisker
    left_whisker_middle = GLine(350, 230, 310, 230)  # left middle whisker
    left_whisker_bottom = GLine(350, 240, 320, 250)  # left lower whisker
    left_whisker_top.color = 'red'
    left_whisker_middle.color = 'red'
    left_whisker_bottom.color = 'red'
    window.add(left_whisker_top)
    window.add(left_whisker_middle)
    window.add(left_whisker_bottom)

    # the whiskers on the right
    right_whisker_top = GLine(450, 220, 480, 210)  # right upper whisker
    right_whisker_middle = GLine(450, 230, 490, 230)  # right middle whisker
    right_whisker_bottom = GLine(450, 240, 480, 250)  # right lower whisker
    right_whisker_top.color = 'red'
    right_whisker_middle.color = 'red'
    right_whisker_bottom.color = 'red'
    window.add(right_whisker_top)
    window.add(right_whisker_middle)
    window.add(right_whisker_bottom)

    # sign
    plaque = GRect(60, 120, x=370, y=310)
    plaque.filled = True
    plaque.fill_color = 'gold'
    window.add(plaque)
    plaque_label = GLabel('招財', x=380, y=370)
    plaque_label.font = 'Courier-20-bold'
    plaque_label.color = 'black'
    window.add(plaque_label)

    # foot
    left_leg = GOval(80, 50, x=310, y=480)
    left_leg.filled = True
    left_leg.fill_color = 'white'
    window.add(left_leg)

    right_leg = GOval(80, 50, x=410, y=480)
    right_leg.filled = True
    right_leg.fill_color = 'white'
    window.add(right_leg)

    # left arm
    left_arm = GOval(40, 90, x=250, y=300)
    left_arm.filled = True
    left_arm.fill_color = 'white'
    window.add(left_arm)

    # left palm
    left_hand = GOval(50, 50, x=245, y=375)
    left_hand.filled = True
    left_hand.fill_color = 'white'
    window.add(left_hand)

    # right arm
    right_arm = GOval(40, 90, x=505, y=230)
    right_arm.filled = True
    right_arm.fill_color = 'white'
    window.add(right_arm)

    # right palm
    right_hand = GOval(50, 50, x=502, y=190)
    right_hand.filled = True
    right_hand.fill_color = 'white'
    window.add(right_hand)

    # left foot paw
    left_toe1 = GOval(10, 10, x=325, y=505)
    left_toe1.filled = True
    left_toe1.fill_color = 'pink'
    window.add(left_toe1)

    left_toe2 = GOval(10, 10, x=345, y=510)
    left_toe2.filled = True
    left_toe2.fill_color = 'pink'
    window.add(left_toe2)

    left_toe3 = GOval(10, 10, x=365, y=505)
    left_toe3.filled = True
    left_toe3.fill_color = 'pink'
    window.add(left_toe3)

    # right foot paw
    right_toe1 = GOval(10, 10, x=425, y=505)
    right_toe1.filled = True
    right_toe1.fill_color = 'pink'
    window.add(right_toe1)

    right_toe2 = GOval(10, 10, x=445, y=510)
    right_toe2.filled = True
    right_toe2.fill_color = 'pink'
    window.add(right_toe2)

    right_toe3 = GOval(10, 10, x=465, y=505)
    right_toe3.filled = True
    right_toe3.fill_color = 'pink'
    window.add(right_toe3)

    # left foot meat ball
    left_paw1 = GOval(35, 15, x=330, y=490)
    left_paw1.filled = True
    left_paw1.fill_color = 'pink'
    window.add(left_paw1)

    # right foot meat ball
    right_paw1 = GOval(35, 15, x=430, y=490)
    right_paw1.filled = True
    right_paw1.fill_color = 'pink'
    window.add(right_paw1)

    label = GLabel('大吉大利')
    label.color = 'green'
    label.font = '-80'
    window.add(label, x=0, y=100)

    # orange
    orange = GOval(50, 50, x=650, y=400)
    orange.filled = True
    orange.fill_color = 'orange'
    window.add(orange)

    # stem
    stem = GLine(673, 385, 675, 400)
    stem.color = 'brown'
    window.add(stem)

    # leaf
    leaf = GOval(15, 10, x=675, y=390)
    leaf.filled = True
    leaf.fill_color = 'green'
    window.add(leaf)

    # spring couplet
    spring_couplet = GPolygon()
    spring_couplet.add_vertex((100, 400))
    spring_couplet.add_vertex((150, 350))
    spring_couplet.add_vertex((200, 400))
    spring_couplet.add_vertex((150, 450))
    spring_couplet.filled = True
    spring_couplet.fill_color = 'red'
    window.add(spring_couplet)

    couplet_text = GLabel('福', x=135, y=415)
    couplet_text.font = 'Courier-30-bold'
    couplet_text.color = 'gold'
    window.add(couplet_text)


if __name__ == '__main__':
    main()
