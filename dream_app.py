import tkinter as tk, random

F=[("Velvet Night","A blindfold, slow music, and complete surrender to touch."),("The Garden","Outdoors fantasy — warm breeze, soft grass, freedom."),("Silk & Lace","You dress each other slowly. Anticipation is everything."),("Mirror Game","Face each other. Eye contact. No looking away."),("The Tease","One leads, one follows. Patience is the rule."),("Candlelight Ritual","Warm oil, candles, whispered words, no rush."),("Power Play","Gentle dominance — one commands softly, one obeys lovingly."),("The Unwrapping","Clothes come off one piece at a time, slowly."),("Midnight Rain","Shower together first. Then the bedroom. Then everything."),("Sweet Surrender","Wrists loosely tied with a silk scarf. Full trust.")]

P=[("Lotus","Face to face, legs intertwined, hearts close — slow and deep.","tender"),("Spooning","From behind, side by side — warm, safe, deeply intimate.","tender"),("The Arch","She arches her back, he supports her — beautiful and passionate.","passionate"),("Lap Dance","She sits on his lap, face to face — she controls the rhythm.","playful"),("The Throne","He sits, she straddles — eye contact, total connection.","passionate"),("Doggy (Gentle)","From behind, he holds her hips softly — deep and loving.","passionate"),("The Bridge","She arches up like a bridge — he worships every curve.","sensory"),("Blindfolded Touch","Eyes covered, one explores the other slowly with hands only.","sensory"),("Wrist Hold","He pins her wrists above her — gently, with her smile of approval.","gentle dominance"),("The Tease Kneel","She kneels, he stands — she decides when and how, fully in charge.","playful"),("Reversed Throne","She faces away on his lap — she controls depth and pace.","playful"),("Side Kiss","Both on sides, facing — kissing, touching, no rush, no goal.","tender"),("The Lift","He lifts her against a wall — brief, passionate, breathless.","passionate"),("Silk Scarf Bind","Wrists tied loosely with silk — she's free anytime, but chooses to stay.","gentle dominance"),("Feather Trail","One uses a feather (or fingertips) to trace the other — no skipping ahead.","sensory"),("The Melt","Missionary, ultra slow — forehead to forehead, breathing together.","tender"),("Guided Hands","Blindfolded partner, guided hand by hand across the other's body.","sensory"),("The Command","She whispers exactly what she wants. He listens and obeys completely.","gentle dominance")]

C={"bg":"#1a0a12","mid":"#2d1020","card":"#3d1530","pink":"#f472b6","violet":"#c084fc","red":"#fb7185","gold":"#fcd34d","text":"#fdf2f8","dim":"#e879a0"}

def dream():
    ft,fm=random.choice(F)
    positions=random.sample(P,random.randint(4,6))
    out.config(state="normal"); out.delete("1.0","end")
    out.insert("end",f"❧  {ft}  ❧\n","ft")
    out.insert("end",f"{fm}\n","fm")
    out.insert("end","─"*40+"\n","sep")
    for i,(n,d,t) in enumerate(positions,1):
        out.insert("end",f"{i}. ","num")
        out.insert("end",f"{n}\n","pn")
        out.insert("end",f"{d}\n","pd")
        out.insert("end",f"✦ {t}\n\n","pt")
    out.insert("end","✦  Enjoy your evening  ✦","fm")
    out.config(state="disabled")

r=tk.Tk(); r.title("Dream ✦"); r.geometry("720x620"); r.configure(bg=C["bg"])
tk.Label(r,text="✦  Dream  ✦",font=("Georgia",32,"bold","italic"),fg=C["pink"],bg=C["bg"]).pack(pady=(14,2))
tk.Label(r,text="A private sanctuary for two",font=("Georgia",11,"italic"),fg=C["dim"],bg=C["bg"]).pack(pady=(0,12))
btn=tk.Button(r,text="✦  Dream  ✦",font=("Georgia",14,"bold"),bg=C["card"],fg=C["pink"],activebackground=C["red"],activeforeground="white",relief="flat",bd=0,padx=28,pady=10,cursor="hand2",command=dream)
btn.pack(pady=(0,14))
f=tk.Frame(r,bg=C["mid"]); f.pack(fill="both",expand=True,padx=18,pady=(0,12))
sb=tk.Scrollbar(f,bg=C["mid"],troughcolor=C["bg"]); sb.pack(side="right",fill="y")
out=tk.Text(f,wrap="word",bg=C["mid"],fg=C["text"],font=("Georgia",12),relief="flat",bd=0,padx=18,pady=14,state="disabled",yscrollcommand=sb.set,spacing2=3,spacing3=5,cursor="arrow")
out.pack(side="left",fill="both",expand=True); sb.config(command=out.yview)
for tag,kw in [("ft",{"font":("Georgia",16,"bold"),"foreground":C["gold"]}),("fm",{"font":("Georgia",11,"italic"),"foreground":C["pink"]}),("sep",{"foreground":"#6d2060"}),("num",{"font":("Georgia",18,"bold"),"foreground":C["violet"]}),("pn",{"font":("Georgia",13,"bold"),"foreground":C["pink"]}),("pd",{"font":("Georgia",11),"foreground":C["text"]}),("pt",{"font":("Georgia",10,"italic"),"foreground":C["red"]})]:
    out.tag_configure(tag,**kw)
r.mainloop()
