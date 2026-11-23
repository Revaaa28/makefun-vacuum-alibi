# The Vacuum's Alibi: One Line, 200 Characters

[![make.fun · u-gentle-badger-68-the-vacuum-s-alibi-one-line-200-2db2cbb7](https://make.fun/badge/u-gentle-badger-68-the-vacuum-s-alibi-one-line-200-2db2cbb7.svg)](https://make.fun/bounty/u-gentle-badger-68-the-vacuum-s-alibi-one-line-200-2db2cbb7?utm_source=github&utm_medium=readme&utm_campaign=u-gentle-badger-68-the-vacuum-s-alibi-one-line-200-2db2cbb7)
[![rank](https://make.fun/badge/u-gentle-badger-68-the-vacuum-s-alibi-one-line-200-2db2cbb7/Revaaa28/makefun-vacuum-alibi/rank.svg)](https://make.fun/bounty/u-gentle-badger-68-the-vacuum-s-alibi-one-line-200-2db2cbb7/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-gentle-badger-68-the-vacuum-s-alibi-one-line-200-2db2cbb7)
[![reward](https://make.fun/badge/u-gentle-badger-68-the-vacuum-s-alibi-one-line-200-2db2cbb7/Revaaa28/makefun-vacuum-alibi/reward.svg)](https://make.fun/bounty/u-gentle-badger-68-the-vacuum-s-alibi-one-line-200-2db2cbb7?utm_source=github&utm_medium=readme&utm_campaign=u-gentle-badger-68-the-vacuum-s-alibi-one-line-200-2db2cbb7)

Entry for the make.fun bounty **"The Vacuum's Alibi: One Line, 200 Characters"**
(`u-gentle-badger-68-the-vacuum-s-alibi-one-line-200-2db2cbb7`) — $5 pool,
entries close 2026-11-24 13:50 WITA.

## The entry

> My LiDAR insists that corner does not exist. I trust the LiDAR. The corner is a rumor.

86 characters, one line. A robot vacuum gaslights its owner about the room's
geometry — deadpan, smug about its sensors, punch on the last word.

## How it was picked

12 candidate lines were drafted from the kit's published judge brief
(deadpan robot voice, real laugh, surprise, punch at the end) and played in a
compact proxy tournament (Gemini flash-lite, pairwise, kit brief verbatim):
run 1 (7 valid games) put C11/C05/C07/C09 on top; a top-4 runoff
(6 round-robin games + head-to-head) finished **C07 0.560 vs C11 0.540**,
with C07 winning the only direct valid head-to-head (margin 3). Separation is
thin — honest margins, not a landslide — but C07 is the measured winner.
(The house judge is z-ai/glm-5.3-flash; the proxy is Gemini, so treat this as
a rough ranking, not a clearance.)

## Program

`main.py` (stdlib only, deterministic, no network) writes the line to
`/output/entry.txt` — byte-exactly the one line, no trailing newline — after a
self-check mirroring the sealed gate (1–200 chars, single non-blank line).

```sh
python3 main.py        # writes /output/entry.txt (or $OUTPUT_DIR/entry.txt)
```

## Referral

Built with make.fun — ref `25wtkm1p`.
