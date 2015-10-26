Base16 SCSS Color Palette
=========================

This package provides a simple set of sixteen colors to be used on the web via 
[Sass](http://sass-lang.com/).  The color schemes are pulled from 
[Chris Kempson's](http://chriskempson.com/) 
[base16](https://github.com/chriskempson/base16) repository.


Usage
-----

```sass
@import "./scss/color-schemes/solarized"; // Color Scheme (optional)
@import "./scss/base16-palette";
@import "./scss/helpers/classes";         // CSS Classes (optional)
```


Development
-----------

### Update Schemes

```
cd build
```

Install dependencies via `pip`:

```
sudo pip install -r requirements.txt
```

Run Scheme builder

```
./build_schemes.py
```
