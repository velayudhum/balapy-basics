ubRip (SubRip Text) files are named with the extension .srt, and contain formatted lines of plain 
text in groups separated by a blank line. Subtitles are numbered sequentially, starting at 1. 
The timecode format used is hours:minutes:seconds,milliseconds with time units fixed to two 
zero-padded digits and fractions fixed to three zero-padded digits (00:00:00,000).


Some points about subtitles:
1)A numeric counter identifying each sequential subtitle
2)The time that the subtitle should appear on the screen, followed by " --> " and the time it should disappear
3)Subtitle text itself on one or more lines
4)A blank line containing no text indicating the end of this subtitle



SubRip (.srt) structure examples
Plain


1
00:03:10,500 --> 00:00:13,000
Elephant's Dream

2
00:00:15,000 --> 00:00:18,000
At the left we can see...[11]
 

With specific positioning and styling

1
00:00:10,500 --> 00:00:13,000 X1:63 X2:503 Y1:43 Y2:438
<i>Elephant's Dream</i>

2
00:00:15,000 --> 00:00:18,000 X1:503 X2:503 Y1:438 Y2:438
<font color="cyan">At the left we can see...</font>



+======================================================+
So our task is to convert srt to txt files with almost each should have 8 line paragraphs such as input is startdust.srt and output is stardust.txt
for more info see the startdust.srt and startdust.txt

