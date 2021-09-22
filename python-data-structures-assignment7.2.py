''' 7.2 Write a program that prompts for a file name, then opens that file and reads through the file, 
looking for lines of the form: X-DSPAM-Confidence:    0.8475
Count these lines and extract the floating point values from each of the lines and 
compute the average of those values and produce an output as shown below. 
Do not use the sum() function or a variable named sum in your solution.
You can download the sample data at https://www.py4e.com/code3/mbox-short.txt?PHPSESSID=b2b920494c49f2f429f394a19a92874c
when you are testing below enter mbox-short.txt as the file name '''

# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
count = 0
aggregate = 0.0
for line in fh:
    line = line.rstrip()
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    if line.startswith("X-DSPAM-Confidence:"):
        #count = count + 1
        #floaters = line.find("0")
        #floaters = floaters[20]
        line = line[20:]
        #count = count + 1
        line = float(line)
        aggregate = aggregate + line
        count = count + 1

#print (aggregate/count)

        #print(line)

print("Average spam confidence:", aggregate/count)
