# PCEngine_eng_patch
English translation patch to PC Engine CD version of Might &amp; Magic Book One: The Secret of the Inner Sanctum

## Create Syscard image
Translation use **David Shadoff** PC Engine Translate font patched SYSCARD, you found here: [SYSCARD_Translatefont](https://github.com/dshadoff/SYSCARD_Translatefont)
I used with Japanse version 3.0 patched rom, never tested with USA version. Be sure Davids IPS patches should be applied on headerless SYSCARD rom image.

## Create Patched Game image
Game translation released as PPF-O-Matic .ppf path file. Work primaly with TOSEC "trurip" .img version. md5 hash: **6050d7260923a5671e1191d8bcea64ce** .
Also work with Redump version (with 11 separate .bin and .cue file) just needed merge back to one .bin file (size needed to be 285728016 bytes, same as TOSEC version)
You can use **Chris Putnam** binmerge on Redump version [binmerge](https://github.com/putnam/binmerge).

## Know issues
- ~~needed some alignment and fix on a profile screen.~~
- text input screen cleanup just with roman letters.
- ~~battle screen text in draft, spell names come from different area then main menu.~~
- ~~cleanup my 4x8 font hack leftovers what is ruining some text output now (amount of Gold and battle texts).~~
- blacksmith inspection text output need to better aligned.

## Further possible improvement
- Lots of free 8x8 tile space now, character names could be redesigned as fixed tiles.
- Status symbol icons.
