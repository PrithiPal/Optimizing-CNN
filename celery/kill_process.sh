#!/bin/bash
pgrep $1 | xargs -n1 -I {} kill -9 {}
