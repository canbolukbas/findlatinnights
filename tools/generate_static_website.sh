./manage.py distill-local docs --collectstatic --force
mv ./docs/events/index.html ./docs/index.html
git restore docs/CNAME
find . -name 'index.html' -print0 | xargs -0 sed -i "" "s/\/media/\.\/media/g"
git add --all
git commit -m "Generate static website"
git push
