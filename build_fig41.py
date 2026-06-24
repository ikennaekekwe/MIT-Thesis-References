import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D

# ============================================================================
# Figure 4.1 data, RECOVERED from the figure we built together (uploads __1_/__2_)
# and cross-verified against the NEITI extraction log and the 4.5 traceability table.
# Modeled = Wood Mackenzie 2026 (sales basis, after estimated theft).
# Audited = NEITI fiscalized / NUPRC annual (governing in disrupted years).
# Aiteo and Eroton modeled lines end 2023 (WoodMac 2024-25 recovery omitted as a
# modeling artifact above the audited record). Bases are never spliced.
# ============================================================================
modeled = {
 "Aiteo":  {2016:29.5,2017:36.0,2018:40.3,2019:36.0,2020:41.0,2021:34.0,2022:10.0,2023:11.7},
 "Eroton": {2016:28.5,2017:27.0,2018:30.0,2019:32.0,2020:21.0,2021:4.4,2022:4.4,2023:5.5},
 "Seplat": {2016:16.5,2017:35.0,2018:52.5,2019:46.5,2020:47.0,2021:40.3,2022:34.3,2023:33.0,2024:33.3,2025:38.7},
 "OML30":  {2016:3.8,2017:13.0,2018:22.5,2019:29.0,2020:29.5,2021:35.0,2022:33.3,2023:33.0,2024:33.3,2025:35.0},
 "FHN":    {2016:2.1,2017:3.1,2018:6.4,2019:7.9,2020:8.6,2021:9.2,2022:9.9,2023:10.3,2024:10.8,2025:14.8},
}
audited = {"Aiteo":[(2022,0.7),(2024,7.4)], "Eroton":[(2024,13.6)]}
C   = {"Aiteo":"#c0392b","Eroton":"#e08214","Seplat":"#1b7837","OML30":"#2166ac","FHN":"#8a8d8f"}
MK  = {"Aiteo":"o","Eroton":"s","Seplat":"^","OML30":"D","FHN":"v"}
LAB = {"Aiteo":"Aiteo (OML 29)","Eroton":"Eroton (OML 18)","Seplat":"Seplat (OMLs 4, 38, 41)",
       "OML30":"Heritage / HEOSL (OML 30)","FHN":"First Hydrocarbon (OML 26)"}

fig, ax = plt.subplots(figsize=(11,6.3))
for k in ["Aiteo","Eroton","Seplat","OML30","FHN"]:
    xs=sorted(modeled[k]); ys=[modeled[k][x] for x in xs]
    ax.plot(xs,ys,'-',marker=MK[k],color=C[k],lw=2.4,ms=7,mec="white",mew=0.6,zorder=3,solid_capstyle="round")
# dotted gap line at the Aiteo blowout (modeled 2022 down to audited 2022)
ax.plot([2022,2022],[modeled["Aiteo"][2022],0.7],ls=":",color=C["Aiteo"],lw=1.3,zorder=2)
# audited stars
for k in audited:
    for (x,y) in audited[k]:
        ax.plot(x,y,marker="*",color=C[k],ms=20,mec="black",mew=0.7,ls="None",zorder=6)
        ax.annotate(f"{y}", (x,y), textcoords="offset points", xytext=(13,-3),
                    fontsize=10, fontweight="bold", color="#222")

ax.annotate("Seplat and Heritage:\ngrowth sustained", (2016.5,51.5), fontsize=10,
            color=C["Seplat"], ha="left", va="top")
ax.annotate("Stars mark audited actuals, which replace\nthe modeled recovery in disrupted years", (2023.3,27),
            fontsize=9, color=C["Aiteo"], ha="center", va="center")

ax.set_xlim(2015.7,2025.3); ax.set_ylim(0,55)
ax.set_xticks(range(2016,2026))
ax.set_xlabel("Year", fontsize=11.5)
ax.set_ylabel("Liquids production (thousand barrels per day, sales basis)", fontsize=11)
ax.grid(True, ls=":", lw=0.6, color="#d5d5d5", zorder=0)
ax.spines[["top","right"]].set_visible(False)

mod_h=[Line2D([0],[0],color=C[k],lw=2.5,marker=MK[k],ms=7,mec="white",mew=0.6,label=LAB[k]) for k in ["Aiteo","Eroton","Seplat","OML30","FHN"]]
leg1=ax.legend(handles=mod_h, loc="upper right", fontsize=9.2, framealpha=0.96,
               title="Modeled (Wood Mackenzie 2026)", title_fontsize=9.6, borderpad=0.7)
ax.add_artist(leg1)

plt.tight_layout()
plt.savefig("Figure_4_1_production_trajectories.png", dpi=200, bbox_inches="tight", facecolor="white")
print("saved Figure_4_1_production_trajectories.png")
