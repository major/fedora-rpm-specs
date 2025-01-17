%global giturl  https://github.com/executablebooks/sphinx-design

Name:           python-sphinx-design
Version:        0.6.1
Release:        %autorelease
Summary:        Sphinx extension for responsive web components

# This project is MIT, but bundles JSON glyphs
# - sphinx_design/compiled/material* is Apache-2.0
# - sphinx_design/compiled/octicon* is MIT
License:        MIT AND Apache-2.0
URL:            https://sphinx-design.readthedocs.io/
VCS:            git:%{giturl}.git
Source:         %{giturl}/archive/v%{version}/sphinx-design-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  python3-devel

# The Fedora package does not contain JSON glyphs
Provides:       bundled(material-icons-fonts) = 4.0.0.c9e5528

# Octicons is not available from Fedora
# The upstream release tarball does not contain JSON glyphs
Provides:       bundled(octicons) = 19.8.0

%global _description %{expand:
This package contains a Sphinx extension for designing beautiful, view
size responsive web components.}

%description %_description

%package     -n python3-sphinx-design
Summary:        Sphinx extension for responsive web components

%description -n python3-sphinx-design %_description

%package        doc
Summary:        Documentation for %{name}
# This project is MIT.  The Javascript and CSS bundled with the documentation
# has the following licenses:
# _static/_sphinx_javascript_frameworks_compat.js: BSD-2-Clause
# _static/alabaster.css: BSD-3-Clause
# _static/basic.css: BSD-2-Clause
# _static/custom.css: BSD-3-Clause
# _static/doctools.js: BSD-2-Clause
# _static/documentation_options.js: BSD-2-Clause
# _static/file.png: BSD-2-Clause
# _static/jquery*.js: MIT
# _static/js: MIT
# _static/language_data.js: BSD-2-Clause
# _static/minus.png: BSD-2-Clause
# _static/plus.png: BSD-2-Clause
# _static/searchtools.js: BSD-2-Clause
# _static/underscore*.js: MIT
# genindex.html: BSD-2-Clause
# search.html: BSD-2-Clause
# searchindex.js: BSD-2-Clause
License:        MIT AND BSD-2-Clause AND BSD-3-Clause

%description    doc
Documentation for %{name}.

%prep
%autosetup -n sphinx-design-%{version} -p1

%generate_buildrequires
# Unpin pytest and myst-parser's version
sed -i "/pytest~=/s/~=8\.3//" pyproject.toml
sed -i "/myst-parser>=/s/>=2,<4//" pyproject.toml
%pyproject_buildrequires -t -x testing

%build
%pyproject_wheel

# Build documentation
PYTHONPATH=$PWD sphinx-build -b html docs html
rm -rf html/{.buildinfo,.doctrees}

%install
%pyproject_install
%pyproject_save_files -L sphinx_design

%check
%pytest -v

%files -n python3-sphinx-design -f %{pyproject_files}
%doc CHANGELOG.md README.md
%license LICENSE
%license sphinx_design/compiled/material-icons_LICENSE
%license sphinx_design/compiled/octicon_LICENSE

%files doc
%doc html
%license LICENSE

%changelog
%autochangelog
