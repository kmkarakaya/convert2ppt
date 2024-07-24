git add .
git commit -m "deploy"
bump-my-version bump patch --dry-run --verbose
bump-my-version bump patch 
git push --tags
git push
pyinstaller --onefile --add-data "config.yaml;." convert2ppt.py