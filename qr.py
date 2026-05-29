import qrcode

data = "CONTROL YOU BRAIN BEFORE IT START TO CONTROL YOU"

F = qrcode.make(data)

F.save("qrcode.png")