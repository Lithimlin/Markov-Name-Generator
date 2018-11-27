# Introduction

This is a small Markov Name Generator, inspired by [this generator by SyntaxColoring](http://max.marrone.nyc/Markov-Word-Generator/). It utilizes Markov Chains and a probability tree to build pseudo-random, yet somewhat legible words. It requires the `appJar` package for its GUI.
It is recommended to run it in a virtual environment using the `requirements.txt`.

To start the GUI, call `gui.py` from within the virtual environment.

# Parameters

`n` is the Markov Order. Higher numbers will create words more similar to the corpus given, lower numbers will result in more gibberish.

`maxLength` will clip words at the given length.

# Future Features
* Updating corpora
