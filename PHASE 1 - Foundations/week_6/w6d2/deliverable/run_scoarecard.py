from scorecard.parsing import parse_results

import scorecard.parsing as sp

from scorecard.display import format_header, format_result, format_summary

#Adding instantly parsed results - no data before this

results = []
results.append(parse_results("  Mihai:51"))
results.append((parse_results("Gigi :  38")))
results.append((parse_results("gigicu:  61")))
results.append((parse_results("Alex   :78")))
results.append((parse_results("chris :83"    )))
results.append((parse_results("collin:80")))
results.append((parse_results("    Adrian:   48    ")))

#Honestly I lost it from here...i need to come back and re-read and see what i did here
#Filter and ranking
passing = sp.filter_above(results)
ranked = sp.rank_results(passing)

#Display
print(format_header("LEADERBOARD"))
print()


for i in range(len(ranked)):
    print(format_result(ranked[i], i + 1))
print()
print(format_summary(results))