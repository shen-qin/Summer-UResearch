import os
from dotenv import load_dotenv

load_dotenv()
with open(os.getenv("ANALYSIS_FILEPATH"), "r") as file:
    lines = file.readlines()

extracted = [line.split(":")[1].strip() for line in lines]

with open("output.txt", "w") as outfile:
    for item in extracted:
        outfile.write("%s\n" % item)