%global srcname sphinx_rtd_theme

# Disables tests and docs
%bcond_with bootstrap

Name:           python-%{srcname}
Version:        3.1.0
Release:        %autorelease
Summary:        Sphinx theme for readthedocs.org

# SPDX
License:        MIT
URL:            https://github.com/readthedocs/%{srcname}/
Source:         %{url}/archive/%{version}/%{srcname}-%{version}.tar.gz
# The koji builders do not have network access, and this file is not included
# in any Fedora package, so we retrieve it for offline use.
Source:         https://docs.readthedocs.io/en/latest/objects.inv

BuildArch:      noarch

BuildRequires:  font(fontawesome)
BuildRequires:  font(lato)
BuildRequires:  font(robotoslab)
BuildRequires:  make
BuildRequires:  python%{python3_pkgversion}-devel
%if %{without bootstrap}
BuildRequires:  %{py3_dist pytest}
BuildRequires:  %{py3_dist sphinx}
BuildRequires:  python-sphinx-doc
%endif

%description
This is a prototype mobile-friendly sphinx theme for readthedocs.org.
It's currently in development and includes some rtd variable checks that
can be ignored if you're just trying to use it on your project outside
of that site.

%package -n python%{python3_pkgversion}-%{srcname}
Summary:        Sphinx theme for readthedocs.org
Requires:       font(fontawesome)
Requires:       font(lato)
Requires:       font(robotoslab)
# Serve the built documentation with working references to the fonts
Recommends:     (web-assets-httpd if httpd)

%description -n python%{python3_pkgversion}-%{srcname}
This is a prototype mobile-friendly sphinx theme for readthedocs.org.
It's currently in development and includes some rtd variable checks that
can be ignored if you're just trying to use it on your project outside
of that site.

%if %{without bootstrap}
%package doc
Summary:        Documentation for the Sphinx theme for readthedocs.org
Requires:       font(fontawesome)
Requires:       font(lato)
Requires:       font(robotoslab)

%description doc
This package contains documentation for the Sphinx theme for
readthedocs.org.
%endif

%prep
%autosetup -p1 -n %{srcname}-%{version}

# Unpin docutils
sed -i "s/docutils >0.18,<0\.22/docutils >0.18/" setup.cfg

# Use local objects.inv for intersphinx
sed -e "s|\('https://docs\.readthedocs\.io/en/stable/', \)None|\1'%{SOURCE1}'|" \
    -e "s|\('https://www\.sphinx-doc\.org/en/master/', \)None|\1'%{_docdir}/python-sphinx-doc/html/objects.inv'|" \
    -i docs/conf.py

# We modify the tests to avoid dependency on readthedocs-sphinx-ext.
# According to upstream, the test dependency is only used to test integration with that dependency.
# See https://github.com/readthedocs/readthedocs-sphinx-ext/pull/105#pullrequestreview-928253285
sed -Ei -e "/extensions\.append\('readthedocs_ext\.readthedocs'\)/d" \
        -e "s/'readthedocs[^']*'(, ?)?//g" \
        tests/util.py

# We patch the theme css files to unbundle fonts (they are required from Fedora)
# Using Web Assets shall support the use case when documentation is
# exported via web server
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Web_Assets/
pushd sphinx_rtd_theme/static/css

rm -r fonts

# Edit the fonts references in theme.css and badge.css
for FONT in lato-normal=lato/Lato-Regular.ttf \
            lato-bold=lato/Lato-Bold.ttf \
            lato-normal-italic=lato/Lato-Italic.ttf \
            lato-bold-italic=lato/Lato-BoldItalic.ttf \
            Roboto-Slab-Regular=google-roboto-slab-fonts/RobotoSlab-Regular.ttf \
            Roboto-Slab-Bold=google-roboto-slab-fonts/RobotoSlab-Bold.ttf;
do
  L="${FONT%=*}"
  R="${FONT#*=}"
  # Get the font basename from the path
  F="${R#*/}"
  F_BASENAME="${F/.ttf}"
  sed \
    -e "s|src:\(url(fonts/$L\.[^)]*) format([^)]*),\?\)\+|src:local('$F_BASENAME'),url('/.sysassets/fonts/$R') format(\"truetype\")|g" \
    -i theme.css
done

sed -e "s|src:url(fonts/fontawesome-webfont\.[^)]*);||" \
    -e "s|src:\(url(fonts/fontawesome-webfont\.[^)]*) format([^)]*),\?\)\+|src:local(\"FontAwesome\"),url('/.sysassets/fonts/fontawesome/fontawesome-webfont.ttf') format(\"truetype\")|" \
    -i badge_only.css theme.css

popd

# We cannot build the Javascript from source at this time, due to many missing
# dependencies.  Convince the build script to skip building the Javascript and
# go on to the python.
mkdir -p build/lib/%{srcname}/static/js
cp -p sphinx_rtd_theme/static/js/badge_only.js build/lib/%{srcname}/static/js
cp -p sphinx_rtd_theme/static/js/theme.js build/lib/%{srcname}/static/js

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%if %{without bootstrap}
# Build the documentation
make -C docs html
%endif

rst2html --no-datestamp README.rst README.html

%install
%pyproject_install

%if %{without bootstrap}
rm docs/build/html/.buildinfo
%endif

%check
%if %{without bootstrap}
%pytest
%endif

# Test that the forbidden fonts were successfully removed from the css files
grep 'format("woff2\?")' \
  %{buildroot}%{python3_sitelib}/%{srcname}/static/css/badge_only.css \
  %{buildroot}%{python3_sitelib}/%{srcname}/static/css/theme.css \
&& exit 1 || true

%files -n python%{python3_pkgversion}-%{srcname}
%doc README.html
%license LICENSE
%{python3_sitelib}/%{srcname}-%{version}.dist-info/
%dir %{python3_sitelib}/%{srcname}/
%{python3_sitelib}/%{srcname}/__pycache__/
%{python3_sitelib}/%{srcname}/static/
%{python3_sitelib}/%{srcname}/*.html
%{python3_sitelib}/%{srcname}/*.py
%{python3_sitelib}/%{srcname}/theme.conf
%dir %{python3_sitelib}/%{srcname}/locale/
%{python3_sitelib}/%{srcname}/locale/sphinx.pot
%lang(da) %{python3_sitelib}/%{srcname}/locale/da/
%lang(de) %{python3_sitelib}/%{srcname}/locale/de/
%lang(en) %{python3_sitelib}/%{srcname}/locale/en/
%lang(es) %{python3_sitelib}/%{srcname}/locale/es/
%lang(et) %{python3_sitelib}/%{srcname}/locale/et/
%lang(fa_IR) %{python3_sitelib}/%{srcname}/locale/fa_IR/
%lang(fr) %{python3_sitelib}/%{srcname}/locale/fr/
%lang(hr) %{python3_sitelib}/%{srcname}/locale/hr/
%lang(hu) %{python3_sitelib}/%{srcname}/locale/hu/
%lang(it) %{python3_sitelib}/%{srcname}/locale/it/
%lang(lt) %{python3_sitelib}/%{srcname}/locale/lt/
%lang(nl) %{python3_sitelib}/%{srcname}/locale/nl/
%lang(pl) %{python3_sitelib}/%{srcname}/locale/pl/
%lang(pt) %{python3_sitelib}/%{srcname}/locale/pt/
%lang(pt_BR) %{python3_sitelib}/%{srcname}/locale/pt_BR/
%lang(ru) %{python3_sitelib}/%{srcname}/locale/ru/
%lang(sv) %{python3_sitelib}/%{srcname}/locale/sv/
%lang(tr) %{python3_sitelib}/%{srcname}/locale/tr/
%lang(zh_CN) %{python3_sitelib}/%{srcname}/locale/zh_CN/
%lang(zh_TW) %{python3_sitelib}/%{srcname}/locale/zh_TW/

%if %{without bootstrap}
%files doc
%doc docs/build/html
%license LICENSE
%endif

%changelog
%autochangelog
