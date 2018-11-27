from appJar import gui
import parser, markov

gen = markov.Markov("")

def generate(buttonName):
    global gen
    app.label("gen_output", value=gen.generate().capitalize())

def update_corpora(value):
    if value is "add_corpus":
        name = app.entry("corpus_name")
        try:
            parser.save_corpus(name, app.text("corpus"))
            app.changeOptionBox("corpora", parser.list_corpora())
            app.option("corpora", name)
        except FileExistsError as e:
            app.popUp("File exists", e, kind="error")
        except ValueError as e:
            app.popUp("Invalid name", e, kind="error")

    elif value is "remove_corpus":
        parser.remove_corpus(app.option("corpora"))
        app.changeOptionBox("corpora", parser.list_corpora(), 0)

    if value is not "corpora":
        app.entry("corpus_name", value="")

    app.clearTextArea("corpus", callFunction=False)
    app.text("corpus", value=get_corpus())
    update_gen("corpus")

def get_corpus():
    return parser.read_corpus(app.option("corpora"))

def update_gen(value):
    global gen
    gen = markov.Markov(app.text("corpus"), n=int(app.spin("order")), maxLength=int(app.spin("maxLength")))

with gui("Markov Word Generator", bg="lightblue") as app:
    app.label("title1", value="Your word is:", sticky="e", font=25)
    app.label("gen_output", value="", row=0, column=1, sticky="", font=25)
    app.button("generate", generate, label="Generate new Word",
                colspan=2, stretch="column", sticky="news", font=15)
    app.spin("order", label="n=", value=0, endValue=5, pos=2, change=update_gen)
    app.spin("maxLength", label="Maximum Length:", value=2, endValue=20,
                pos=7, row=2, column=1, change=update_gen)
    app.separator(colspan=2, stretch="both")
    app.option("corpora", value=parser.list_corpora(), label="Corpora",
                colspan=2, change=update_corpora, stretch="column", font=14)
    app.text("corpus", value=get_corpus(), scroll=True,
                colspan=2, change=update_gen)
    app.entry("corpus_name", label="Corpus Name:", colspan=2)
    app.button("add_corpus", update_corpora, label="Add Corpus", sticky="news",
                stretch="column")
    app.button("remove_corpus", update_corpora, label="Remove Corpus", row=7,
                column=1, sticky="news", stretch="column")
    update_gen("initial")
