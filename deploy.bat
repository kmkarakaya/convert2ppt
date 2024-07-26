git add .
git commit -m "deploy"
bump-my-version bump patch --dry-run --verbose
bump-my-version bump patch 
git push --tags
git push
pyinstaller --onefile --add-data "C:\Users\murat.karakaya\CODES\convert2ppt\convert2ppt\config.yaml;." convert2ppt.py