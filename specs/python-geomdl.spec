# Currently unavailable in EPEL
%bcond plotly %{expr:!0%{?rhel}}

# Sphinx-generated HTML documentation is not suitable for packaging; see
# https://bugzilla.redhat.com/show_bug.cgi?id=2006555 for discussion.
#
# We can generate PDF documentation as a substitute.
%bcond doc 1

Name:           python-geomdl
Version:        5.3.1
Release:        %autorelease
Summary:        Object-oriented pure Python B-Spline and NURBS library

# From docs/citing.rst:
#   * Source code is released under the terms of the MIT License
#   * Examples are released under the terms of the MIT License
#   * Documentation is released under the terms of CC BY 4.0
#
# The examples are maintained in a separate repository,
# https://github.com/orbingol/geomdl-examples, which is not packaged here.
#
# Documentation is confined to the -doc subpackage.
#
# SPDX
License:        MIT
%global doc_license CC-BY-4.0
SourceLicense:  %{license} AND %{doc_license}
URL:            https://onurraufbingol.com/NURBS-Python/
# The GitHub tarball has documentation; the PyPI one does not.
%global forgeurl https://github.com/orbingol/NURBS-Python
Source:         %{forgeurl}/archive/v%{version}/NURBS-Python-%{version}.tar.gz

# Upstream uses something like “setup.py bdist_wheel --use-cython” to turn on
# the optional Cython-generated extensions. This doesn’t fit well with the
# pyproject-rpm-macros approach (which uses “pip wheel …”), so we just patch
# setup.py to unconditionally enable Cython.
Patch:          geomdl-5.3.1-unconditional-Cython.patch
# Stop using deprecated/removed np.float/np.int
# https://github.com/orbingol/NURBS-Python/pull/163
Patch:          %{forgeurl}/pull/163.patch

BuildRequires:  python3-devel
BuildRequires:  gcc

# Upstream uses weird tox environments for testing:
#  https://github.com/orbingol/NURBS-Python/blob/v5.3.1/tox.ini#L5
# The default py3X environment fails with InterpreterNotFound:
#  https://github.com/orbingol/NURBS-Python/pull/145
# And even when everything works, the tox environment builds the extension again.
# It also measures coverage.
# Instead, we BuildRequire the only remaining tests dependency manually:
BuildRequires:  python3dist(pytest)


%if %{with doc}
BuildRequires:  make
BuildRequires:  python3dist(sphinx)
# We don’t need python3dist(sphinx-rtd-theme) since we aren’t building HTML.
BuildRequires:  python3-sphinx-latex
BuildRequires:  latexmk
# For sphinx.ext.inheritance_diagram:
BuildRequires:  graphviz
# For index
# BuildRequires:  /usr/bin/xindy
%endif

%global common_description %{expand:
NURBS-Python (geomdl) is a pure Python, self-contained, object-oriented
B-Spline and NURBS spline library for Python versions 2.7.x, 3.4.x and later.

NURBS-Python (geomdl) provides convenient data structures and highly
customizable API for rational and non-rational splines along with the efficient
and extensible implementations of the following algorithms:

  • Spline evaluation
  • Derivative evaluation
  • Knot insertion
  • Knot removal
  • Knot vector refinement
  • Degree elevation
  • Degree reduction
  • Curve and surface fitting via interpolation and least squares approximation

NURBS-Python (geomdl) also provides customizable visualization and animation
options via Matplotlib, Plotly and VTK libraries. Please refer to the
documentation (http://nurbs-python.readthedocs.io/) for more details.}

%description %{common_description}


%package -n     python3-geomdl
Summary:        %{summary}

Suggests:       python3-geomdl-doc = %{version}-%{release}

%description -n python3-geomdl %{common_description}


%if %{with doc}
%package        doc
Summary:        Documentation for geomdl
# See the comment above the base package License field.
License:        %{doc_license}

BuildArch:      noarch

%description    doc %{common_description}
%endif


%prep
%autosetup -n NURBS-Python-%{version} -p1
# Allow newer versions in cases where exact versions are pinned.
sed -r -i 's/==/>=/' requirements.txt
%if %{without plotly}
# Omit plotly; functionality in geomdl.visualization.VisPlotly will be
# unavailable.
sed -r -i 's/^(plotly)\b/# &/' requirements.txt
%endif


%generate_buildrequires
%pyproject_buildrequires requirements.txt


%build
%pyproject_wheel

%if %{with doc}
PYTHONPATH="${PWD}" %make_build -C docs latex \
    SPHINXOPTS='-j%{?_smp_build_ncpus}'
%make_build -C docs/_build/latex LATEXMKOPTS='-quiet'
%endif


%install
%pyproject_install
%pyproject_save_files -l geomdl


%check
%pytest ${ignore-}


%files -n python3-geomdl -f %{pyproject_files}
# pyproject-rpm-macros handles the LICENSE file—verify with “rpm -qL -p …”—but
# we also use an explicit “%%license LICENSE” because we want it in
# %%{_licensedir} alongside citing.rst
%license LICENSE docs/citing.rst
%if %{without doc}
%doc CHANGELOG.md CONTRIBUTORS.rst DESCRIPTION.rst README.rst
%endif


%if %{with doc}
%files doc
%license LICENSE docs/citing.rst
%doc CHANGELOG.md CONTRIBUTORS.rst DESCRIPTION.rst README.rst
%doc docs/_build/latex/NURBS-Python.pdf
%endif


%changelog
%autochangelog
