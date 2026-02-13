#!/bin/bash
echo "=== GitHub Pages Deploy Check ==="
echo ""
echo "Repository: toru-taaaaan/internal-dx-portal"
echo "Expected URL: https://toru-taaaaan.github.io/internal-dx-portal/"
echo ""
echo "Recent commits:"
git log --oneline -5
echo ""
echo "Current branch:"
git branch --show-current
echo ""
echo "Remote status:"
git status
