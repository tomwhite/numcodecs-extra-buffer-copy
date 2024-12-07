```
memray run -f -o output.bin repro.py
memray flamegraph -f output.bin
open memray-flamegraph-output.html
```