[python example](bestpractice.py):
to illustrate
[best practices](http://cecileane.github.io/computingtools/pages/notes0906-bestpractices.html).  
file extension is not required, but useful to tell the text editor
how to color the file, for example.

---

example for [here](http://cecileane.github.io/computingtools/pages/notes0906-intro-shell.html):
"Unix is like a chainsaw"

1. make absolutely sure that you are in this directory,
   `rm-example`. I'm not kidding. really not.
2. try both of these commands, see how they differ:

```bash
rm -rf tmp-data/aligned-reads*
rm -rf tmp-data/aligned-reads *
```

to revert all these file deletions:

```bash
git checkout -- .
```

---

how these data files were created:

```bash
mkdir tmp-data
mkdir data
for a in $(julia -e 'srand(1); [println(rand(1:1000)) for i in 1:30]')
do
  b=aligned-reads_$a.fa
  touch tmp-data/$b
  touch data/$b
done
```