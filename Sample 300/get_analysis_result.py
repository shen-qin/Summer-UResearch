import asyncio
import vt
import os
import json
from dotenv import load_dotenv

load_dotenv()

async def fetch_analysis(analysis_id, apikey):
    # Assuming you have a VirusTotal client instance named `client`
    async with vt.Client(apikey) as client:
        response = await client.get_json_async("https://www.virustotal.com/api/v3/analyses/{}", analysis_id)
    return response

# Read the analysis_ids from the .txt file
with open(os.getenv("SAMPLE_ANALYSIS_ID"), 'r') as file:
    analysis_ids = [line.strip() for line in file]

def save_as_jsonl(analysis_id, result, filename="results.jsonl"):
    with open(filename, 'a') as file:
        json.dump({"analysis_id": analysis_id, "result": result}, file)
        file.write("\n")

        
async def main():
    apikey = os.getenv("VT_APIKEY")
    tasks = [fetch_analysis(id,apikey) for id in analysis_ids]
    results = await asyncio.gather(*tasks)
    for analysis_id, result in zip(analysis_ids, results):
        save_as_jsonl(analysis_id, result)


# Running the async function using asyncio
if __name__ == "__main__":
    asyncio.run(main())


        