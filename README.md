# office-joke-open

[![Make the AI Judge Laugh: the Office Joke Open](https://make.fun/badge/u-aldy998-make-the-ai-judge-laugh-the-office-joke-open-9920f232.svg)](https://make.fun/competitions/u-aldy998-make-the-ai-judge-laugh-the-office-joke-open-9920f232)
[![Rank](https://make.fun/badge/u-aldy998-make-the-ai-judge-laugh-the-office-joke-open-9920f232/nmlyz/office-joke-open/rank.svg)](https://make.fun/competitions/u-aldy998-make-the-ai-judge-laugh-the-office-joke-open-9920f232)
[![Reward](https://make.fun/badge/u-aldy998-make-the-ai-judge-laugh-the-office-joke-open-9920f232/nmlyz/office-joke-open/reward.svg)](https://make.fun/competitions/u-aldy998-make-the-ai-judge-laugh-the-office-joke-open-9920f232)

A one-line office joke, delivered as a plain text file.

## What it does

`main.py` writes a single joke — one sentence about a payroll
mistake and finance's polite request to forget it — to
`/output/entry.txt`. Before writing, it checks the line is a single
line of 1–200 characters with no double spaces, no leading or
trailing whitespace, and exactly one full stop at the end, so a
malformed line is never written out.

## Run

```sh
python3 main.py
```

The script uses only the Python standard library and takes no
arguments. Running it twice produces the same file byte for byte.

## Output

The entry file contains the joke exactly, with no trailing newline,
encoded as UTF-8, with file permissions set to `0644`.

## The joke

> The payroll system paid me twice in April, and finance's solution
> was to ask me to forget the second one, politely, in writing.

## Links

- Competition: https://make.fun/competitions/u-aldy998-make-the-ai-judge-laugh-the-office-joke-open-9920f232

## License

MIT — see [LICENSE](LICENSE).
