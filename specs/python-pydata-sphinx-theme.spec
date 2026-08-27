# Documentation can no longer be built in Fedora due to missing python modules:
# ablog and sphinx-togglebutton
# This also means that doctests cannot be run.
%bcond docs 0

%global giturl  https://github.com/pydata/pydata-sphinx-theme

Name:           python-pydata-sphinx-theme
Version:        0.21.0
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

%if %{with docs}
# Generating image files requires network access.  Instead, we scrape these from
# https://pydata-sphinx-theme.readthedocs.io/en/latest/_images.  See
# docs/_static/gallery.yaml for a list of images to download.
Source3:        pydata-gallery.tar.xz
%endif

BuildArch:      noarch
BuildSystem:    pyproject
BuildOption(install): -L pydata_sphinx_theme
BuildOption(generate_buildrequires): -x test%{?with_docs:,doc}

BuildRequires:  babel
BuildRequires:  gcc-c++
BuildRequires:  make
BuildRequires:  nodejs-devel
BuildRequires:  /usr/bin/node
BuildRequires:  /usr/bin/npm

%if %{without docs}
Obsoletes:      %{name}-doc < 0.13.0-1
%endif

%global _description %{expand:This package contains a Sphinx extension for creating document components
optimized for HTML+CSS.

- The panels directive creates panels of content in a grid layout, utilizing
  both the Bootstrap 5 grid system, and cards layout.

- The link-button directive creates a clickable button, linking to a URL or
  reference, and can also be used to make an entire panel clickable.

- The dropdown directive creates content that can be toggled.

- The tabbed directive creates tabbed content.

- opticon and fa (fontawesome) roles allow for inline icons to be added.

See https://pydata-sphinx-theme.readthedocs.io/ for documentation.}

%description
%_description

%package     -n python3-pydata-sphinx-theme
Summary:        Bootstrap-based Sphinx theme from the PyData community
Requires:       fontawesome-fonts-all
Requires:       fontawesome-fonts-web

Provides:       bundled(npm(bootstrap)) = 5.3.8

%if %{without docs}
Obsoletes:      %{name}-doc < 0.13.0-1
%endif

%description -n python3-pydata-sphinx-theme
%_description

%if %{with docs}
%package        doc
Summary:        Documentation for pydata-sphinx-theme

%description    doc
Documentation for pydata-sphinx-theme.
%endif

%prep
%autosetup -n pydata-sphinx-theme-%{version} -p1 -a1
cp -p %{SOURCE2} .

%if %{with docs}
%setup -n pydata-sphinx-theme-%{version} -q -T -D -a 3

# Point to the local switcher instead of the inaccessible one on the web
sed -i 's,https://pydata-sphinx-theme\.readthedocs\.io/en/latest/,,' docs/conf.py
%endif

# Substitute the installed nodejs version for the requested version
%global nodejs_version %(%{_bindir}/node -v | sed s/v//)
sed -i 's,^\(node-version = \)".*",\1"%{nodejs_version}",' pyproject.toml

# Skip the playwright tests, since playwright is not available in Fedora
%pyproject_patch_dependency pytest-playwright:ignore

# Do not run coverage tools in an RPM build
%pyproject_patch_dependency pytest-cov:ignore

# The Fedora sphinx package does not provide sphinx[test]
sed -i 's/\(sphinx\)\[test\]/\1/' pyproject.toml

%build -p
export npm_config_cache="$PWD/.package-cache"
nodeenv --node=system --prebuilt --clean-src $PWD/.nodeenv

%install -a
%define instdir %{buildroot}%{python3_sitelib}/pydata_sphinx_theme
%define themedir %{instdir}/theme/pydata_sphinx_theme/static
sed -i '/\.gitignore/d' %{pyproject_files}
rm %{themedir}/.gitignore

# Clean up build-host paths leaking into the source maps
sed -i 's|pydata_sphinx_theme/\.\.||g' %{themedir}/scripts/fontawesome.js.map
sed -i 's|pydata_sphinx_theme/\.\./\.\./\.\./\.\./\.\.||g' \
    %{themedir}/styles/pydata-sphinx-theme.css.map

# Unbundle the FontAwesome fonts: webpack already vendors the woff2 files
# referenced by the (Fedora-patched) SCSS/JS imports into
# vendor/fontawesome/webfonts/, copying them from the system
# fontawesome-fonts-web package.  Replace those copies with symlinks back to
# that package instead of shipping duplicate binaries.  The CSS/JS keep
# referencing them with the same relative url()/path, so nothing else needs to
# change; Sphinx dereferences the symlinks (real files, real bytes) when it
# copies the static assets into a project's own build output, so the generated
# documentation stays fully self-contained.
for font in fa-brands-400.woff2 fa-regular-400.woff2 fa-solid-900.woff2; do
    rm -f %{themedir}/vendor/fontawesome/webfonts/$font
    ln -s %{_datadir}/fontawesome/webfonts/$font \
        %{themedir}/vendor/fontawesome/webfonts/$font
done

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
