Name:           python-pydata-sphinx-theme
Version:        0.9.0
Release:        3%{?dist}
Summary:        Bootstrap-based Sphinx theme from the PyData community

# This project is BSD-3-Clause.
# The bundled bootstrap JavaScript library is MIT.
License:        BSD-3-Clause and MIT
BuildArch:      noarch
URL:            https://github.com/pydata/pydata-sphinx-theme
Source0:        %{url}/archive/v%{version}/pydata-sphinx-theme-%{version}.tar.gz
# Source1 and Source2 created with ./prepare_vendor.sh
Source1:        pydata-sphinx-theme-%{version}-vendor.tar.xz
Source2:        pydata-sphinx-theme-%{version}-vendor-licenses.txt
# Fedora-only patch: unbundle the fontawesome fonts
Patch0:         %{name}-fontawesome.patch

BuildRequires:  fontawesome5-fonts-all
BuildRequires:  gcc-c++
BuildRequires:  make
BuildRequires:  nodejs-devel
BuildRequires:  npm
BuildRequires:  python3-devel
BuildRequires:  %{py3_dist beautifulsoup4}
BuildRequires:  %{py3_dist docutils}
BuildRequires:  %{py3_dist nodeenv}
BuildRequires:  %{py3_dist packaging}
BuildRequires:  %{py3_dist pip}
BuildRequires:  %{py3_dist pytest}
BuildRequires:  %{py3_dist pytest-regressions}
BuildRequires:  %{py3_dist setuptools}
BuildRequires:  %{py3_dist sphinx}
BuildRequires:  %{py3_dist sphinx-theme-builder}
BuildRequires:  %{py3_dist wheel}
BuildRequires:  yarnpkg

# Documentation dependencies
BuildRequires:  %{py3_dist jupyter-sphinx}
BuildRequires:  %{py3_dist myst-parser}
BuildRequires:  %{py3_dist numpydoc}
BuildRequires:  %{py3_dist numpy}
BuildRequires:  %{py3_dist pandas}
BuildRequires:  %{py3_dist plotly}
BuildRequires:  %{py3_dist sphinx-design}
BuildRequires:  %{py3_dist sphinx-sitemap}
BuildRequires:  %{py3_dist sphinxext-rediraffe}
BuildRequires:  %{py3_dist xarray}

%global _description %{expand:
This package contains a Sphinx extension for creating document components
optimized for HTML+CSS.

- The panels directive creates panels of content in a grid layout,
  utilizing both the Bootstrap 4 grid system, and cards layout.

- The link-button directive creates a clickable button, linking to a URL
  or reference, and can also be used to make an entire panel clickable.

- The dropdown directive creates content that can be toggled.

- The tabbed directive creates tabbed content.

- opticon and fa (fontawesome) roles allow for inline icons to be added.}

%description %_description

%package     -n python3-pydata-sphinx-theme
Summary:        Bootstrap-based Sphinx theme from the PyData community
Requires:       fontawesome5-fonts-all

%description -n python3-pydata-sphinx-theme %_description

%package        doc
Summary:        Documentation for pydata-sphinx-theme

%description    doc
Documentation for pydata-sphinx-theme.

%prep
%autosetup -n pydata-sphinx-theme-%{version} -p1 -a1
cp -p %{SOURCE2} .

# Substitute the installed nodejs version for the requested version
sed -i 's,^\(node-version = \)".*",\1"%{nodejs_version}",' pyproject.toml

# Create a node header tarball so we don't try to download it
mkdir -p node-v%{nodejs_version}/include
cp -a %{_includedir}/node node-v%{nodejs_version}/include
tar czf node-v%{nodejs_version}-headers.tar.gz node-v%{nodejs_version}
npm config set tarball $PWD/node-v%{nodejs_version}-headers.tar.gz

# ValueError: invalid mode: 'rU' while trying to load binding.gyp
# https://bugzilla.redhat.com/show_bug.cgi?id=2099065
sed 's/"rU"/"r"/' -i .package-cache/v6/npm-node-gyp-7.1.2-*-integrity/node_modules/node-gyp/gyp/pylib/gyp/input.py

%build
export PUPPETEER_SKIP_CHROMIUM_DOWNLOAD=1
export YARN_CACHE_FOLDER="$PWD/.package-cache"
yarn install --offline

# Workaround deprecated md4 used in webpack
find node_modules/webpack/lib/ -type f -exec sed -i 's/md4/sha256/g' {} +

# Humor nodeenv, which wants a binary named nodejs
nodejs=$(which nodejs 2> /dev/null || :)
if [ -z "$nodejs" ]; then
  if [ -d ~/bin ]; then
    PREEXISTING_BIN=1
  else
    PREEXISTING_BIN=0
    mkdir ~/bin
  fi
  ln -s %{_bindir}/node ~/bin/nodejs
fi
python3 -m nodeenv --node=system --prebuilt --clean-src $PWD/.nodeenv

%pyproject_wheel

if [ -z "$nodejs" ]; then
  if [ "$PREEXISTING_BIN" = 0 ]; then
    rm -fr ~/bin
  else
    rm ~/bin/nodejs
  fi
fi

%install
%pyproject_install
%pyproject_save_files pydata_sphinx_theme
sed -i '/\.gitignore/d' %{pyproject_files}
rm %{buildroot}%{python3_sitelib}/pydata_sphinx_theme/theme/pydata_sphinx_theme/static/.gitignore

# We need an installed tree before documentation building works properly
export PYTHONPATH=%{buildroot}%{python3_sitelib}
cd docs
sphinx-build -a . _build
rm _build/.buildinfo
cd -

%check
%pytest

%files -n python3-pydata-sphinx-theme -f %{pyproject_files}
%doc README.md

%files doc
%doc docs/_build/*
%license LICENSE

%changelog
* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jan  6 2023 Jerry James <loganjerry@gmail.com> - 0.9.0-2
- Fix unexpanded macros in the doc subpackage
- Convert License tag to SPDX

* Tue Aug  2 2022 Jerry James <loganjerry@gmail.com> - 0.9.0-1
- Version 0.9.0 (fixes rhbz#2105307)

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue Jun 21 2022 Python Maint <python-maint@redhat.com> - 0.8.1-3
- Rebuilt for Python 3.11

* Fri May 13 2022 Jerry James <loganjerry@gmail.com> - 0.8.1-2
- Bring back the doc subpackage

* Tue Apr 12 2022 Jerry James <loganjerry@gmail.com> - 0.8.1-1
- Version 0.8.1
- Drop the doc subpackage due to missing dependencies
- Use yarn to install vendored JavaScript

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Nov 11 2021 Jerry James <loganjerry@gmail.com> - 0.7.2-1
- Version 0.7.2

* Sat Oct  2 2021 Jerry James <loganjerry@gmail.com> - 0.7.1-1
- Version 0.7.1
- Drop upstreamed -sphinx4.1 and -docutils patches

* Wed Sep 22 2021 Jerry James <loganjerry@gmail.com> - 0.6.3-2
- Add upstream -docutils patch to fix FTI (bz 2006934)

* Tue Jul 13 2021 Jerry James <loganjerry@gmail.com> - 0.6.3-1
- Initial RPM
