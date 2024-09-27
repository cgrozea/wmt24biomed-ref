# Reference system for the WMT 2024 biomedical translation task
https://www2.statmt.org/wmt24/biomedical-translation-task.html 

## Instructions

### Requirements 

Preferably on a Linux machine with a 48 GB VRAM Nvidia GPU, although it might work on Windows under WSL and it does work but much slower with smaller VRAM Nvidia GPUs.

- download and install ollama https://ollama.com/download

- install python 3, pip and then ollama python module with either "pip install ollama" or "pip3 install ollama"

### How to run it

- put the test files into the folder "wmtbiomed24testdata"

- start ollama with "ollama serve"

- use "ollama pull llama-3.1:70b" in a terminal to get the model we used 

- execute the script "runall.sh"


## Runnning times

In about 3 hours (or 36 hours for a 24 GB card) you will have the translated
texts into the folder "results".

Tested on Ubuntu 22.04 Linux with a 48 GB GPU (Nvidia A6000 ADA, see the times below) and with a 24 GB GPU (Nvidia A5000, 12x slower in this task, as a result of the insufficent VRAM size)

    de2en_de.txt:took: 728.68479347229 s
    en2de_en.txt:took: 1213.0289468765259 s
    en2es_en.txt:took: 1066.3779108524323 s
    en2fr_en.txt:took: 1142.28484249115 s
    en2it_en.txt:took: 1318.7238502502441 s
    en2pt_en.txt:took: 1091.4702382087708 s
    en2ru_en.txt:took: 1110.1685411930084 s
    es2en_es.txt:took: 933.2781286239624 s
    fr2en_fr.txt:took: 807.0216953754425 s
    it2en_it.txt:took: 805.7838594913483 s
    pt2en_pt.txt:took: 749.8489987850189 s
    ru2en_ru.txt:took: 640.5795819759369 s
