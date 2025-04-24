# Add a BuildRequires on vtk merely for smoke-testing imports of VTK
# integration modules? This does not enable additional tests.
%bcond vtk_dep 0

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
# While we no longer package a full Sphinx-generated manual, we consider the
# documentation license to apply to files packaged as %%doc, *.md/*.rst.
License:        MIT AND CC-BY-4.0
URL:            https://onurraufbingol.com/NURBS-Python/
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

BuildSystem:            pyproject
BuildOption(install):   -l geomdl
BuildOption(generate_buildrequires): requirements.txt
%if %{without vtk_dep}
# Need python3dist(vtk) for geomdl.visualization.vtk_helpers, but it is not
# worth adding the BuildRequires just for an import check.
BuildOption(check):     %{shrink:
                        -e geomdl.visualization.vtk_helpers
                        -e geomdl.visualization.VisVTK
                        }
%endif

BuildRequires:  gcc

# Upstream uses weird tox environments for testing:
#  https://github.com/orbingol/NURBS-Python/blob/v5.3.1/tox.ini#L5
# The default py3X environment fails with InterpreterNotFound:
#  https://github.com/orbingol/NURBS-Python/pull/145
# And even when everything works, the tox environment builds the extension again.
# It also measures coverage.
# Instead, we BuildRequire the only remaining tests dependency manually:
BuildRequires:  %{py3_dist pytest}
%if %{with vtk_dep}
# Allow smoke-testing importability of VTK integration modules.
BuildRequires:  %{py3_dist vtk}
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

# Removed for Fedora 43; we can drop the Obsoletes after Fedora 46
Obsoletes:      python-geomdl-doc < 5.3.1-34

%description -n python3-geomdl %{common_description}


%prep -a
# Allow newer versions in cases where exact versions are pinned.
sed -r -i 's/==/>=/' requirements.txt


%check -a
%pytest ${ignore-}


%files -n python3-geomdl -f %{pyproject_files}
# The LICENSE file is already handled in .dist-info, but citing.rst contains
# important license information, too.
%license docs/citing.rst
%doc CHANGELOG.md
%doc CONTRIBUTORS.rst
%doc DESCRIPTION.rst
%doc README.rst


%changelog
%autochangelog
