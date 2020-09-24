# example of running a "long" analysis

illustration for [here](http://cecileane.github.io/computingtools/pages/notes0915.html)
to show how to
- redirect the output and/or errors, and
- pause or kill or process.

This folder contain the sequence [data](alignedDNA.nex) and the
[option](mrBayes-run.nex) file to reproduce the analysis.
To run the analysis, the [MrBayes](http://mrbayes.sourceforge.net/index.php)
program also needs to be installed, and its executable `md` needs to be located in a
directory in the PATH variable.
Run the analysis from the command line like this:

```shell
mb mrBayes-run.nex
```

## things to try

```
mb mrBayes-run.nex
^z (sleep)
fg
^c (cancels / interrupts the process)
mb mrBayes-run.nex > alignedDNA.nex.screenlog
(error messages, if any, still go to the screen)
(forgot & : can't work)
^z (sleep)
ps
kill -9 ...
less alignedDNA.nex.screenlog
mb mrBayes-run.nex > alignedDNA.nex.screenlog &
ps (check the match in process ID)
top (q to quit)
tail -n 5 alignedDNA.nex.screenlog
kill -9 ...
mb mrBayes-run.nex > /dev/null 2> alignedDNA.nex.err
^z
ps
bg
```

## running analyses on a remote machine

in statistics or CS machines: AFS (Andrew file system)
has a very strong authentication system

do this below, to run something for as much as 1 month.
keep this list of commands in your readme file.
yes: `ssh` twice.

```bash
ssh darwin00.stat.wisc.edu
stashticket
tmux new-session -s mb-analysis
ssh darwin00
cd private/st679/classroom-repos/lecture-examples/mrbayes-example/
mb mrBayes-run.nex > alignedDNA.nex.screenlog &
```

^a d to detach, `tmux attach` to attach, `tmux list` to list sessions
