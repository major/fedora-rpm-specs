# There is a bootstrap loop between libpysal and networkx when tests/docs are
# enabled
%bcond bootstrap 0

# Whether to create the extras package
%bcond extras  %[%{without bootstrap} && !0%{?rhel}]

# Whether to build documentation and run tests
# scikit-learn is no longer available on 32-bit x86
%bcond doctest  %[%{with extras} && "%(uname -m)" != "i686"]

%global giturl  https://github.com/networkx/networkx

Name:           python-networkx
Version:        3.5
Release:        %autorelease
Summary:        Creates and Manipulates Graphs and Networks
License:        BSD-3-Clause
URL:            https://networkx.org/
VCS:            git:%{giturl}.git
Source0:        %{giturl}/archive/networkx-%{version}.tar.gz
# For intersphinx
Source1:        https://numpy.org/neps/objects.inv#/objects-neps.inv
Source2:        https://matplotlib.org/stable/objects.inv#/objects-matplotlib.inv
Source3:        https://docs.scipy.org/doc/scipy/objects.inv#/objects-scipy.inv
Source4:        https://pandas.pydata.org/pandas-docs/stable/objects.inv#/objects-pandas.inv
Source5:        https://geopandas.org/en/stable/objects.inv#/objects-geopandas.inv
Source6:        https://sphinx-gallery.github.io/stable/objects.inv#/objects-sphinx-gallery.inv
Source7:        https://networkx.org/nx-guides/objects.inv#/objects-nx-guides.inv

# Some examples cannot be executed, so expect them to fail.
# Examples that require network access:
# - football
# Examples that require packages not available from Fedora:
# - osmnx requires osmnx
# - plot_lines requires momepy
Patch:          %{name}-doc.patch
# Undo upstream change to use intersphinx_registry.  Fedora does not have it,
# and it does not let us use local documentation in the build.
Patch:          %{name}-intersphinx.patch

BuildArch:      noarch

BuildRequires:  make
BuildRequires:  python3-devel

%if %{with doctest}
# Tests
BuildRequires:  %{py3_dist pytest-mpl}

# Documentation
BuildRequires:  python-pygraphviz-doc
BuildRequires:  python3-docs
BuildRequires:  python3-numpy-doc
BuildRequires:  %{py3_dist geopandas}
BuildRequires:  %{py3_dist libpysal}
BuildRequires:  sympy-doc
BuildRequires:  tex(latex)
BuildRequires:  tex-preview
%endif

%description
NetworkX is a Python package for the creation, manipulation, and
study of the structure, dynamics, and functions of complex networks.

%package -n python3-networkx
Summary:        Creates and Manipulates Graphs and Networks
Recommends:     xdg-utils

%description -n python3-networkx
NetworkX is a Python 3 package for the creation, manipulation, and
study of the structure, dynamics, and functions of complex networks.

%if %{with doctest}
%package doc
# The content is BSD-3-Clause.  Other licenses are due to files copied in by
# Sphinx.
# _static/basic.css: BSD-2-Clause
# _static/binder_badge_logo.svg: BSD-3-Clause
# _static/broken_example.png: BSD-3-Clause
# _static/copybutton.js: MIT
# _static/custom.css: BSD-3-Clause
# _static/doctools.js: BSD-2-Clause
# _static/documentation_options.js: BSD-2-Clause
# _static/file.png: BSD-2-Clause
# _static/jupyterlite_badge_logo.svg: BSD-3-Clause
# _static/language_data.js: BSD-2-Clause
# _static/minus.png: BSD-2-Clause
# _static/mystnb.*.css: BSD-3-Clause
# _static/no_image.png: BSD-3-Clause
# _static/opensearch.xml: BSD-2-Clause
# _static/plot_directive.css: PSF-2.0
# _static/plus.png: BSD-2-Clause
# _static/scripts/bootstrap.*: MIT
# _static/scripts/pydata-sphinx-theme.*: BSD-3-Clause
# _static/searchtools.js: BSD-2-Clause
# _static/sg_gallery.css: BSD-3-Clause
# _static/sg_gallery-binder.css: BSD-3-Clause
# _static/sg_gallery-dataframe.css: BSD-3-Clause
# _static/sg_gallery-rendered-html.css: BSD-3-Clause
# _static/sphinx_highlight.js: BSD-2-Clause
# _static/styles/bootstrap.*: MIT
# _static/styles/pydata-sphinx-theme.*: BSD-3-Clause
# _static/styles/theme.css: BSD-3-Clause
# genindex.html: BSD-2-Clause
# search.html: BSD-2-Clause
# searchindex.js: BSD-2-Clause
License:        BSD-3-Clause AND BSD-2-Clause AND MIT AND PSF-2.0
Summary:        Documentation for networkx
Requires:       fontawesome-fonts-all
Provides:       bundled(js-bootstrap)

%description doc
Documentation for networkx
%endif

%if %{with extras}
%pyproject_extras_subpkg -n python3-networkx extra
%endif

%prep
%autosetup -p1 -n networkx-networkx-%{version}

# Use local objects.inv for intersphinx
sed -e 's|\("https://numpy.org/neps/", \)None|\1"%{SOURCE1}"|' \
    -e 's|\("https://matplotlib.org/stable/", \)None|\1"%{SOURCE2}"|' \
    -e 's|\("https://docs.scipy.org/doc/scipy/", \)None|\1"%{SOURCE3}"|' \
    -e 's|\("https://pandas.pydata.org/pandas-docs/stable/", \)None|\1"%{SOURCE4}"|' \
    -e 's|\("https://geopandas.org/en/stable/", \)None|\1"%{SOURCE5}"|' \
    -e 's|\("https://sphinx-gallery.github.io/stable/", \)None|\1"%{SOURCE6}"|' \
    -e 's|\("https://networkx.org/nx-guides/", \)None|\1"%{SOURCE7}"|' \
    -i doc/conf.py

# Point to the local switcher instead of the inaccessible one on the web
sed -i 's,https://networkx.org/documentation/latest/,,' doc/conf.py

# Use a free font instead of a proprietary font
sed -i 's/Helvetica/sans-serif/' examples/drawing/plot_chess_masters.py

%generate_buildrequires
%pyproject_buildrequires %{?with_doctest:-x doc,example,extra,test}

%build
%pyproject_wheel

%if %{with doctest}
# Build the documentation
PYTHONPATH=$PWD/build/lib make -C doc html
rst2html --no-datestamp README.rst README.html
%endif

%install
%pyproject_install
%pyproject_save_files -l networkx

%if %{with doctest}
# Repack uncompressed zip archives
for fil in $(find doc/build -name \*.zip); do
  mkdir zip
  cd zip
  unzip ../$fil
  zip -9r ../$fil .
  cd ..
  rm -fr zip
done
%endif

%check
export FLEXIBLAS=NETLIB
%if %{with doctest}
%pytest -v
%else
%pyproject_check_import -e '*.tests.*' -e '*.conftest'
%endif

%files -n python3-networkx -f %{pyproject_files}
%if %{with doctest}
%doc README.html
%endif

%if %{with doctest}
%files doc
%doc doc/build/html/*
%endif

%changelog
%autochangelog
