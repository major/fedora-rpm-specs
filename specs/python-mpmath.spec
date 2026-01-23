# Docs build is currently broken after the transition to wheels.
# Somebody can figure this out if they care enough.
%bcond docs 0

Name:           python-mpmath
Version:        1.4.0b3
Release:        %autorelease
Summary:        Pure-Python library for multiprecision floating-point arithmetic
License:        BSD-3-Clause
URL:            https://mpmath.org
# Source code
Source0:        https://github.com/fredrik-johansson/mpmath/archive/%{version}/%{name}-%{version}.tar.gz

# Switch to 'traditional' theme in RHEL since 'classic' isn't available
Patch0:         python-mpmath-1.0.0-sphinx.patch

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  xwayland-run
BuildRequires:  mutter
BuildRequires:  mesa-dri-drivers

%if %{with docs}
# For building documentation
BuildRequires:  dvipng
BuildRequires:  latexmk
BuildRequires:  make
BuildRequires:  tex(latex)
BuildRequires:  tex(capt-of.sty)
BuildRequires:  tex(ellipse.sty)
BuildRequires:  tex(fncychap.sty)
BuildRequires:  tex(framed.sty)
BuildRequires:  tex(needspace.sty)
BuildRequires:  tex(pict2e.sty)
BuildRequires:  tex(tabulary.sty)
BuildRequires:  tex(tgtermes.sty)
BuildRequires:  tex(txtt.tfm)
BuildRequires:  tex(upquote.sty)
BuildRequires:  tex(wrapfig.sty)
%endif

BuildArch:      noarch

%global _description %{expand:
Mpmath is a pure-Python library for multiprecision floating-point
arithmetic. It provides an extensive set of transcendental functions,
unlimited exponent sizes, complex numbers, interval arithmetic,
numerical integration and differentiation, root-finding, linear
algebra, and much more. Almost any calculation can be performed just
as well at 10-digit or 1000-digit precision, and in many cases mpmath
implements asymptotically fast algorithms that scale well for
extremely high precision work. If available, mpmath will (optionally)
use gmpy to speed up high precision operations.}

%description %_description

%package -n python3-mpmath
Summary:        A pure Python library for multiprecision floating-point arithmetic
%if 0%{?fedora} || 0%{?rhel} > 7
Recommends:     python3-matplotlib
%endif
%if %{without docs}
Obsoletes:      python-mpmath-doc < %{version}-%{release}
%endif

%description -n python3-mpmath %_description

If you require plotting capabilities in mpmath, install python3-matplotlib.

%if %{with docs}
%package doc
Summary:        HTML documentation for %{name}
Requires:       python3-mpmath = %{version}-%{release}

# BSD-3-Clause: the content
# BSD-2-Clause: files in html/_static and html/searchindex.js, added by Sphinx
License:        BSD-3-Clause AND BSD-2-Clause

%description doc
This package contains the HTML documentation for %{name}.
%endif

%pyproject_extras_subpkg -n python3-mpmath gmpy

%prep
%setup -q -n mpmath-%{version}
%if 0%{?rhel} == 7
%patch -P0 -p1 -b .sphinx
%endif

# Drop the gmpy2 req. We have an older version packaged and we don't
# want to depend on an alpha release.
sed -r -i "/^gmpy2 =/d" pyproject.toml

%generate_buildrequires
export SETUPTOOLS_SCM_PRETEND_VERSION_FOR_MPMATH=%{version}
%pyproject_buildrequires -x %{?with_docs:docs,}gmpy,tests

%build
export SETUPTOOLS_SCM_PRETEND_VERSION_FOR_MPMATH=%{version}
%pyproject_wheel

%if %{with docs}
# Build documentation
export PYTHONPATH=$PWD/build/lib
mkdir -p docs/latex
sphinx-build -b latex %{?_smp_mflags} docs docs/latex
%make_build -C docs/latex
mkdir -p docs/html
sphinx-build -b html %{?_smp_mflags} docs docs/html
rm -rf docs/html/.{buildinfo,doctrees}
%endif

%install
export SETUPTOOLS_SCM_PRETEND_VERSION_FOR_MPMATH=%{version}
%pyproject_install
%pyproject_save_files mpmath

%check
cd mpmath/tests/
OPTIONS=(
    # Some of those tests fail with 'failed to import mpmath'.
    --deselect=mpmath/tests/test_cli.py
)
xwfb-run -c mutter -- pytest-3 -v "${OPTIONS[@]}"

%files -n python3-mpmath -f %{pyproject_files}
%doc CHANGES README.rst

%if %{with docs}
%files doc
%doc docs/latex/mpmath.pdf docs/html
%endif

%changelog
%autochangelog
