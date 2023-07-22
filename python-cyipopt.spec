# Sphinx-generated HTML documentation is not suitable for packaging; see
# https://bugzilla.redhat.com/show_bug.cgi?id=2006555 for discussion.
#
# We generate PDF documentation as a substitute.
%bcond doc_pdf 1

Name:           python-cyipopt
Version:        1.1.0
Release:        %autorelease
Summary:        Cython interface for the interior point optimizer IPOPT

# SPDX
License:        EPL-1.0
URL:            https://github.com/mechmotum/cyipopt
# We prefer the GitHub source archive to the PyPI one because it contains
# the examples.
Source:         %{url}/archive/v%{version}/cyipopt-%{version}.tar.gz

# A little consistency in shebangs and execute bits
# https://github.com/mechmotum/cyipopt/pull/136
Patch:          %{url}/pull/136.patch
# Fix a couple of small documentation typos
# https://github.com/mechmotum/cyipopt/pull/137
Patch:          %{url}/pull/137.patch
# Don’t use deprecated/removed np.float alias
# https://github.com/mechmotum/cyipopt/pull/191
Patch:          %{url}/pull/191.patch
# Pin Cython<3 until compatibility can be fixed
# https://github.com/mechmotum/cyipopt/pull/212
#
# Works around, but does not fix:
#
# Does not build with Cython 3
# https://github.com/mechmotum/cyipopt/issues/211
#
# “In addition to upper-bounding the version of Cython, this also drops Cython
# from install_requires, since it doesn’t appear to be a real runtime
# dependency.”
Patch:          %{url}/pull/212.patch

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}

BuildRequires:  python3-devel

# setup_requires:
# Does not build with Cython 3
# https://github.com/mechmotum/cyipopt/issues/211
BuildRequires:  ((python3dist(cython) >= 0.26) with (python3dist(cython) < 3~~))
BuildRequires:  python3dist(numpy) >= 1.15

BuildRequires:  pkgconfig(ipopt)
# Called from setup.py:
BuildRequires:  /usr/bin/pkg-config

BuildRequires:  python3dist(pytest)
# Scipy is an optional dependency. Installing it allows testing the scipy
# integration.
BuildRequires:  python3dist(scipy)

BuildRequires:  gcc

%if %{with doc_pdf}
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


%package doc
Summary:        Documentation and examples for cyipopt
BuildArch:      noarch

%description doc %{common_description}


%prep
%autosetup -n cyipopt-%{version} -p1

# Replace zero-length files in the tests with proper empty text files, i.e.,
# just a newline. It makes sense for __init__.py files to be empty, but the
# empty test files look like a mistake, so an upstream issue was filed:
# https://github.com/mechmotum/cyipopt/issues/135
echo '' | tee $(find cyipopt/tests -type f -name '*.py' -size 0 | tr '\n' ' ')

%py3_shebang_fix examples

%if %{with doc_pdf}
# Avoid:
#   ! LaTeX Error: Too deeply nested.
echo 'latex_elements["preamble"] = r"\usepackage{enumitem}\setlistdepth{99}"' \
    >> docs/source/conf.py
%endif


%generate_buildrequires
%pyproject_buildrequires %{?with_doc_pdf:docs/requirements.txt}


%build
%pyproject_wheel

%if %{with doc_pdf}
BLIB="${PWD}/build/lib.%{python3_platform}-cpython-%{python3_version_nodots}"
PYTHONPATH="${BLIB}" %make_build -C docs latex \
    SPHINXOPTS='-j%{?_smp_build_ncpus}'
%make_build -C docs/build/latex LATEXMKOPTS='-quiet'
%endif


%install
%pyproject_install
%pyproject_save_files cyipopt ipopt ipopt_wrapper


%check
%pytest
# Run the examples for additional confidence.
while read -r example
do
  PYTHONPATH='%{buildroot}%{python3_sitearch}' '%{python3}' "${example}"
done < <(
  # Skip hs071_scipy_jax.py, since it requires https://pypi.org/project/jax/,
  # which is not packaged.
  find examples -type f -name '*.py' ! -name hs071_scipy_jax.py
)

%files -n python3-cyipopt -f %{pyproject_files}
# pyproject-rpm-macros handles LICENSE; verify with “rpm -qL -p …”


%files doc
%license LICENSE
%doc CHANGELOG.rst
%doc README.rst
%doc examples/
%if %{with doc_pdf}
%doc docs/build/latex/cyipopt.pdf
%endif


%changelog
%autochangelog
