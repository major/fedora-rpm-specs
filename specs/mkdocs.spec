# Docs and integration tests are disabled to avoid circular dependencies for now
%bcond docs 0
%bcond tests 1
%bcond integration 0

%global forgeurl https://github.com/%{name}/%{name}

Name:           mkdocs
Version:        1.6.1
Release:        %autorelease
Summary:        Python tool to create HTML documentation from markdown sources

# mkdocs itself is BSD-2-Clause, the rest comes from bundled dependencies
License:        BSD-2-Clause AND OFL-1.1-RFN AND Apache-2.0 AND OFL-1.1 AND MIT AND (MIT OR GPL-2.0-only) AND MPL-1.1
URL:            https://www.mkdocs.org
Source0:        %{forgeurl}/archive/%{version}/%{name}-%{version}.tar.gz

# Fix compatibility with click 8.3.0+
Patch: https://github.com/mkdocs/mkdocs/pull/4065.patch

BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  sed

%if %{with docs}
BuildRequires:  python3dist(mdx-gh-links)
BuildRequires:  python3dist(mkdocs-redirects)
%endif
%if %{with integration}
BuildRequires:  python3dist(pymdown-extensions)
BuildRequires:  python3dist(markdown-callouts)
%endif

BuildRequires:  fontawesome4-fonts
BuildRequires:  fontawesome-fonts-web
BuildRequires:  js-jquery

# These need to be unretired
# Recommends:     mkdocs-bootstrap
# Recommends:     mkdocs-bootswatch

Requires:       fontawesome4-fonts
Requires:       fontawesome-fonts-web
Requires:       js-jquery

# These fonts are vendored under mkdocs/themes/readthedocs/css/fonts/ in
# formats that are not available in Fedora (eot/svg/woff/woff2)
# License: OFL-1.1-RFN
Provides:       bundled(fontawesome4-fonts)
# License: Apache-2.0
Provides:       bundled(google-roboto-slab-fonts)
# Licence: OFL-1.1
Provides:       bundled(lato-fonts)

# Vendored under mkdocs/themes/mkdocs/js/bootstrap.bundle.min.js
# License: MIT
Provides:       bundled(js-bootstrap) = 5.3.2
# Vendored under mkdocs/themes/readthedocs/js/html5shiv.min.js
# License: MIT OR GPL-2.0-only
Provides:       bundled(js-html5shiv) = 3.7.3
# Vendored under mkdocs/contrib/search/templates/search/lunr.js
# License: MIT
Provides:       bundled(js-lunr) = 2.3.9
# Vendored under mkdocs/contrib/search/lunr-language/
# License: MPL-1.1
Provides:       bundled(js-lunr-languages)

%description
MkDocs is a fast and simple way to create a website from source files written 
in Markdown, and configured with a YAML configuration file, the documentation 
can be hosted anywhere, even in free hosting services like Read the Docs and 
GitHub Pages.

%if %{with docs}
%package docs
Summary:        Documentation for %{name}
Requires:       %{name} = %{version}-%{release}

%description docs
Documentation for %{name}.
%endif

%prep
%autosetup -p1

# Drop unnecessary shebangs
sed -i '1{\@^#!/usr/bin/env python@d}' mkdocs/{__init__,__main__}.py

# Replace bundled fonts
ln -sf %{_fontbasedir}/fontawesome/fontawesome-webfont.ttf \
  mkdocs/themes/readthedocs/css/fonts/
rm mkdocs/themes/mkdocs/webfonts/*
for f in %{_datadir}/fontawesome/webfonts/*; do
  ln -s "$f" mkdocs/themes/mkdocs/webfonts/
done

# Replace bundled js
ln -sf %{_datadir}/javascript/jquery/3/jquery.min.js \
  mkdocs/themes/readthedocs/js/jquery-3.6.0.min.js

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%if %{with docs}
LC_ALL=C.UTF-8 LANG=C.UTF-8 PYTHONPATH=$PWD %{__python3} -m mkdocs build
%endif

%install
%pyproject_install
%pyproject_save_files mkdocs

%check
%pyproject_check_import
%if %{with tests}
%{py3_test_envvars} %{python3} -m unittest discover -s mkdocs -p "*tests.py" -v
%endif
%if %{with integration}
%{py3_test_envvars} %{python3} -m mkdocs.tests.integration
%endif

%files -f %{pyproject_files}
%doc README.md
%license LICENSE
%{_bindir}/%{name}

%if %{with docs}
%files docs
%doc site/*
%endif

%changelog
%autochangelog
