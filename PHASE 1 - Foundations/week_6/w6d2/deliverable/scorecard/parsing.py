def parse_results(line):
    parts = line.split(":")
    player = parts[0].strip().title()
    score = parts[1].strip()
    return {
        "player": player,
        "score": int(score)
    }


#at this point i have a dict with {player: "...", score:int}
def filter_above(results, threshold=50):
    scores_above = []
    for result in results:
        if result["score"] > threshold:
            scores_above.append(result)
    return scores_above


def get_score(result):
    return result["score"]

def rank_results(results):
     return sorted(results, key=get_score, reverse=True)



if __name__ == "__main__":
    print("whatever dude")