#!/usr/bin/env python3
"""Numbering consistency linter: fails on non-sequential captions, duplicates,
or dangling Table/Figure references. Run before every build."""
import re, sys
from collections import defaultdict
FILES = {1:"Chapter1_Full_v30.md",2:"Chapter2_Full_v29.md",3:"Chapter3_Full_v4.md",
         4:"Chapter4_Full_v9.md",5:"Chapter5_Full_v8.md",6:"Chapter6_Full_v3.md"}
cap_re = re.compile(r'^\s*\*{0,2}(Table|Figure)\s+(\d+)\.(\d+)[.:]')
ref_re = re.compile(r'(?<![\*\d])(Table|Figure)[~ ]+(\d+)\.(\d+)')
captions = defaultdict(int); refs = []
for ch,fn in FILES.items():
    try: text=open(fn,encoding="utf-8").read()
    except FileNotFoundError: continue
    for ln in text.split("\n"):
        m=cap_re.match(ln)
        if m: captions[(m.group(1),int(m.group(2)),int(m.group(3)))]+=1; continue
        for r in ref_re.finditer(ln): refs.append((r.group(1),int(r.group(2)),int(r.group(3)),fn))
issues=[]
for k,c in captions.items():
    if c>1: issues.append(f"DUP caption {k[0]} {k[1]}.{k[2]} ({c}x)")
bych=defaultdict(list)
for (kind,c,m) in captions: bych[(kind,c)].append(m)
for (kind,c),nums in sorted(bych.items()):
    if sorted(nums)!=list(range(1,len(nums)+1)): issues.append(f"NON-SEQUENTIAL {kind} ch{c}: {sorted(nums)}")
valid=set(captions)
for kind,c,m,fn in refs:
    if (kind,c,m) not in valid: issues.append(f"DANGLING ref {kind} {c}.{m} in {fn}")
if issues:
    print("NUMBERING ISSUES:"); [print("  -",i) for i in issues]; sys.exit(1)
print(f"numbering OK: {len(captions)} captions, {len(refs)} references all consistent")
