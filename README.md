# Find Latin Nights
A website that shows the latin dance night events around your city.

👉🏻 https://canbolukbas.github.io/findlatinnights/

### Daily Maintenance Steps

```
./manage.py distill-local docs --collectstatic --force
mv ./docs/events/index.html ./docs/index.html
git restore docs/CNAME
find . -name 'index.html' -print0 | xargs -0 sed -i "" "s/\/media/\.\/media/g"

```
