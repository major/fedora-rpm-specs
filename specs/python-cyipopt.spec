# Sphinx-generated HTML documentation is not suitable for packaging; see
# https://bugzilla.redhat.com/show_bug.cgi?id=2006555 for discussion.
#
# We generate PDF documentation as a substitute.
%bcond doc_pdf 1

Name:           python-cyipopt
Version:        1.5.0
Release:        %autorelease
Summary:        Cython interface for the interior point optimizer IPOPT

# The entire source is EPL-2.0.
#
# The GitHub project contains one file that is BSD-3-Clause:
#   - cyipopt/tests/unit/test_scipy_ipopt_from_scipy.py
# but this is excluded from the PyPI sdist.
License:        EPL-2.0
URL:            https://github.com/mechmotum/cyipopt
Source:         %{pypi_source cyipopt}

BuildSystem:            pyproject
BuildOption(install):   -l cyipopt ipopt ipopt_wrapper

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}

BuildRequires:  tomcli

BuildRequires:  pkgconfig(ipopt) >= 3.12
# Called from setup.py:
BuildRequires:  /usr/bin/pkg-config

BuildRequires:  %{py3_dist pytest}
# Scipy is an optional dependency. Installing it allows testing the scipy
# integration.
BuildRequires:  %{py3_dist scipy} >= 1.8

BuildRequires:  gcc

%if %{with doc_pdf}
# Add examples/ and docs/requirements.txt to source distribution
# https://github.com/mechmotum/cyipopt/pull/242
# numpydoc>=1.2
BuildRequires:  %{py3_dist numpydoc} >= 1.2
# sphinx>=4.3.2
BuildRequires:  %{py3_dist sphinx} >= 4.3.2

BuildRequires:  make
BuildRequires:  python3-sphinx-latex
BuildRequires:  latexmk
BuildRequires:  tex(morefloats.sty)
%endif

%global common_description %{expand:
Ipopt (Interior Point OPTimizer, pronounced eye-pea-opt) is a software package
for large-scale nonlinear optimization. Ipopt is available from the COIN-OR
initiative, under the Eclipse Public License (EPL).

cyipopt is a Python wrapper around Ipopt. It enables using Ipopt from the
comfort of the Python programming language.}

%description %{common_description}


%package -n python3-cyipopt
Summary:        %{summary}

# From README.rst:
#
#   As of version 1.1.0 (2021-09-07), the distribution is released under the
#   name "cyipopt" on PyPi (https://pypi.org/project/cyipopt). Before version
#   1.1.0, it was released under the name "ipopt"
#   (https://pypi.org/project/ipopt).
#
# A compatibility shim is provided for the old package name.
%py_provides python3-ipopt
# Furthermore, the extension module is installed at the top level as
# “ipopt_wrapper”.
%py_provides python3-ipopt_wrapper

%description -n python3-cyipopt %{common_description}


%package -n python3-cyipopt-tests
Summary:        Tests for cyipopt

Requires:       python3-cyipopt = %{version}-%{release}
Requires:       %{py3_dist pytest}
Recommends:     %{py3_dist scipy} >= 1.8

%description -n python3-cyipopt-tests
This provides the “cyipopt.tests” subpackage.


%package doc
Summary:        Documentation for cyipopt

BuildArch:      noarch

%description doc %{common_description}


%prep -a
# Replace zero-length files in the tests with proper empty text files, i.e.,
# just a newline. It makes sense for __init__.py files to be empty, but the
# empty test files look like a mistake, so an upstream issue was filed:
# https://github.com/mechmotum/cyipopt/issues/135
echo '' | tee $(find cyipopt/tests -type f -name '*.py' -size 0 | tr '\n' ' ')

%if %{with doc_pdf}
# Avoid:
#   ! LaTeX Error: Too deeply nested.
echo 'latex_elements["preamble"] = r"\usepackage{enumitem}\setlistdepth{99}"' \
    >> docs/source/conf.py
%endif


%build -a
%if %{with doc_pdf}
BLIB="${PWD}/build/lib.%{python3_platform}-cpython-%{python3_version_nodots}"
PYTHONPATH="${BLIB}" %make_build -C docs latex \
    SPHINXOPTS='-j%{?_smp_build_ncpus}'
%make_build -C docs/build/latex LATEXMKOPTS='-quiet'
%endif


%check -a
%ifarch %{power64} s390x
# Arch-dependent failures of test_minimize_ipopt_jac_with_scipy_methods[cobyla]
# https://github.com/mechmotum/cyipopt/issues/237
k="${k-}${k+ and }not test_minimize_ipopt_jac_with_scipy_methods[cobyla]"
%endif

%pytest -v -rsx -k "${k-}"


%files -n python3-cyipopt -f %{pyproject_files}
%exclude %{python3_sitearch}/cyipopt/tests/


%files -n python3-cyipopt-tests
%{python3_sitearch}/cyipopt/tests/


%files doc
%license LICENSE
%doc CHANGELOG.rst
%doc README.rst
%if %{with doc_pdf}
%doc docs/build/latex/cyipopt.pdf
%endif


%changelog
%autochangelog
