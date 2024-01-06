# Sphinx-generated HTML documentation is not suitable for packaging; see
# https://bugzilla.redhat.com/show_bug.cgi?id=2006555 for discussion.
#
# We generate PDF documentation as a substitute.
%bcond_without doc_pdf

Name:           python-transforms3d
Version:        0.4.1
Release:        %autorelease
Summary:        Functions for 3D coordinate transformations

# The entire source is BSD-2-Clause, except:
#   - transforms3d/_gohlketransforms.py is derived from a BSD-3-Clause original
#     source, so is BSD-3-Clause or possibly (BSD-2-Clause AND BSD-3-Clause)
#   - versioneer.py and original/transformations.py are not installed and do
#     not contribute to the license of the binary RPMs.
License:        BSD-2-Clause AND BSD-3-Clause
URL:            https://matthew-brett.github.io/transforms3d/
%global forgeurl https://github.com/matthew-brett/transforms3d
Source0:        %{forgeurl}/archive/%{version}/transforms3d-%{version}.tar.gz

Patch:          %{forgeurl}/pull/50.patch

BuildArch:      noarch

BuildRequires:  python3-devel

%if %{with doc_pdf}
BuildRequires:  make
BuildRequires:  python3-sphinx-latex
BuildRequires:  latexmk
BuildRequires:  tex(morefloats.sty)
%endif

%global common_description %{expand:
Code to convert between various geometric transformations.

  • Composing rotations / zooms / shears / translations into affine matrix;
  • Decomposing affine matrix into rotations / zooms / shears / translations;
  • Conversions between different representations of rotations, including:
      • 3x3 Rotation matrices;
      • Euler angles;
      • quaternions.}

%description %{common_description}

%package -n python3-transforms3d
Summary:        %{summary}

Recommends:     python3dist(sympy)

%description -n python3-transforms3d %{common_description}

%package doc
Summary:        Documentation and examples for transforms3d

%description doc %{common_description}

%prep
%autosetup -n transforms3d-%{version} -p1

%generate_buildrequires
%{pyproject_buildrequires %{?with_doc_pdf:doc-requirements.txt} \
    test-requirements.txt}

%build
%pyproject_wheel

%if %{with doc_pdf}
# Note that doc/Makefile is customized rather than taken directly from
# sphinx-quickstart output.
PYTHONPATH="${PWD}/build/lib" %make_build -C doc pdf \
    SPHINXOPTS='-j%{?_smp_build_ncpus}' \
    PYTHON='%{python3}' \
    LATEXMKOPTS='-quiet'
%endif

%install
%pyproject_install
%pyproject_save_files -l transforms3d

%check
%pytest

%files -n python3-transforms3d -f %{pyproject_files}

%files doc
%license LICENSE
%doc README.rst
%if %{with doc_pdf}
%doc doc/_build/latex/transforms3d.pdf
%endif

%changelog
%autochangelog
