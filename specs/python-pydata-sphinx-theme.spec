# Documentation can no longer be built in Fedora due to missing python modules:
# ablog and sphinx-togglebutton
# This also means that doctests cannot be run.
%bcond docs 0

%global giturl  https://github.com/pydata/pydata-sphinx-theme

Name:           python-pydata-sphinx-theme
Version:        0.16.1
Release:        %autorelease
Summary:        Bootstrap-based Sphinx theme from the PyData community

# This project is BSD-3-Clause.
# The bundled bootstrap JavaScript library is MIT.
License:        BSD-3-Clause AND MIT
URL:            https://pydata-sphinx-theme.readthedocs.io/
VCS:            git:%{giturl}.git
Source0:        %{giturl}/archive/v%{version}/pydata-sphinx-theme-%{version}.tar.gz
# Source1 and Source2 created with ./prepare_vendor.sh
Source1:        pydata-sphinx-theme-%{version}-vendor.tar.xz
Source2:        pydata-sphinx-theme-%{version}-vendor-licenses.txt

# Compatibility with Pygments 2.19+
Patch:          https://github.com/pydata/pydata-sphinx-theme/pull/2091.patch

%if %{with docs}
# Generating image files requires network access.  Instead, we scrape these from
# https://pydata-sphinx-theme.readthedocs.io/en/latest/_images.  See
# docs/_static/gallery.yaml for a list of images to download.
Source3:        pydata-gallery.tar.xz
%endif
# Fedora-only patch: unbundle the fontawesome fonts
Patch:          %{name}-fontawesome.patch

BuildArch:      noarch
BuildSystem:    pyproject
BuildOption(install): -L pydata_sphinx_theme
BuildOption(generate_buildrequires): -x test%{?with_docs:,doc}

BuildRequires:  babel
BuildRequires:  fontawesome-fonts-all
BuildRequires:  fontawesome-fonts-web
BuildRequires:  gcc-c++
BuildRequires:  make
BuildRequires:  nodejs-devel
BuildRequires:  nodejs-npm
BuildRequires:  python3-devel
BuildRequires:  yarnpkg

%global _description %{expand:
This package contains a Sphinx extension for creating document components
optimized for HTML+CSS.

- The panels directive creates panels of content in a grid layout,
  utilizing both the Bootstrap 5 grid system, and cards layout.

- The link-button directive creates a clickable button, linking to a URL
  or reference, and can also be used to make an entire panel clickable.

- The dropdown directive creates content that can be toggled.

- The tabbed directive creates tabbed content.

- opticon and fa (fontawesome) roles allow for inline icons to be added.

See https://pydata-sphinx-theme.readthedocs.io/ for documentation.}

%description %_description

%package     -n python3-pydata-sphinx-theme
Summary:        Bootstrap-based Sphinx theme from the PyData community
Requires:       fontawesome-fonts-all
Requires:       fontawesome-fonts-web
Provides:       bundled(js-bootstrap) = 5.3.7

%if %{without docs}
Obsoletes:      %{name}-doc < 0.13.0-1
%endif

%description -n python3-pydata-sphinx-theme %_description

%if %{with docs}
%package        doc
Summary:        Documentation for pydata-sphinx-theme

%description    doc
Documentation for pydata-sphinx-theme.
%endif

%prep
%autosetup -n pydata-sphinx-theme-%{version} -p1 -a1

%conf
cp -p %{SOURCE2} .

%if %{with docs}
%setup -n pydata-sphinx-theme-%{version} -q -T -D -a 3

# Point to the local switcher instead of the inaccessible one on the web
sed -i 's,https://pydata-sphinx-theme\.readthedocs\.io/en/latest/,,' docs/conf.py
%endif

# Substitute the installed nodejs version for the requested version
sed -i 's,^\(node-version = \)".*",\1"%{nodejs_version}",' pyproject.toml

%generate_buildrequires -p
# The Fedora sphinx package does not provide sphinx[test]
sed -i 's/\(sphinx\)\[test\]/\1/' pyproject.toml

%build -p
export YARN_CACHE_FOLDER="$PWD/.package-cache"
yarn install --offline
nodeenv --node=system --prebuilt --clean-src $PWD/.nodeenv

%install -a
%define instdir %{buildroot}%{python3_sitelib}/pydata_sphinx_theme
%define themedir %{instdir}/theme/pydata_sphinx_theme/static
sed -i '/\.gitignore/d' %{pyproject_files}
rm %{themedir}/.gitignore

# More work is required to fully unbundle the fontawesome fonts
sed -i 's,pydata_sphinx_theme/\.\./\.\./\.\./\.\./\.\.,,g' \
    %{themedir}/scripts/fontawesome.js.map \
    %{themedir}/styles/pydata-sphinx-theme.css.map
sed -e 's,url.*fa-solid-900\.woff2.*format("truetype"),local("fontawesome-free-fonts/Font Awesome 6 Free-Solid-900") format("opentype"),g' \
    -e 's,url.*fa-regular-400\.woff2.*format("truetype"),local("fontawesome-free-fonts/Font Awesome 6 Free-Regular-400") format("opentype"),g' \
    -e 's,url.*fa-brands-400\.woff2.*format("truetype"),local("fontawesome-brands-fonts/Font Awesome 6 Brands-Regular-400") format("opentype"),g' \
    -i %{themedir}/styles/pydata-sphinx-theme.css
sed -i '/vendor/d' %{pyproject_files}
rm -fr %{themedir}/vendor

%if %{with docs}
# We need an installed tree before documentation building works properly
cd docs
%{py3_test_envvars} sphinx-build -a . _build
rm _build/.buildinfo
cd -
%endif

%check
%pytest -v

%files -n python3-pydata-sphinx-theme -f %{pyproject_files}
%doc README.md
%license LICENSE

%if %{with docs}
%files doc
%doc docs/_build/*
%license LICENSE
%endif

%changelog
%autochangelog
