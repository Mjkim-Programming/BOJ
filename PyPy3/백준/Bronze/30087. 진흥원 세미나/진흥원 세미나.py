classroom = {}
classroom["Algorithm"] = "204"
classroom["DataAnalysis"] = "207"
classroom["ArtificialIntelligence"] = "302"
classroom["CyberSecurity"] = "B101"
classroom["Network"] = "303"
classroom["Startup"] = "501"
classroom["TestStrategy"] = "105"

n = int(input())

for _ in range(0, n):
    s = input()
    print(classroom[s])