# If docs should point to local python3-docs rather than website.
# python3-docs is not shipped in RHEL 9+
%bcond py3docs %{undefined rhel}
# tests require hypothesis, which is not included in RHEL
%bcond tests %{undefined rhel}

Name:           python-gmpy2
Version:        2.2.1
Release:        %autorelease
Summary:        Python interface to GMP, MPFR, and MPC

License:        LGPL-3.0-or-later
URL:            https://gmpy2.readthedocs.io/
VCS:            git:https://github.com/aleaxit/gmpy.git
Source:         %pypi_source gmpy2

BuildRequires:  gcc
BuildRequires:  gmp-devel
BuildRequires:  libmpc-devel
BuildRequires:  make
BuildRequires:  pkgconfig(mpfr)
BuildRequires:  python3-devel
%if %{with py3docs}
BuildRequires:  python3-docs
%endif
BuildRequires:  %{py3_dist sphinx}

%global _docdir_fmt %{name}

%global common_desc %{expand:
This package contains a C-coded Python extension module that supports
multiple-precision arithmetic.  It is the successor to the original
gmpy module.  The gmpy module only supported the GMP multiple-precision
library.  Gmpy2 adds support for the MPFR (correctly rounded real
floating-point arithmetic) and MPC (correctly rounded complex
floating-point arithmetic) libraries.  It also updates the API and
naming conventions to be more consistent and support the additional
functionality.}

%description %common_desc

%package -n python3-gmpy2
Summary:        Python 3 interface to GMP, MPFR, and MPC

%description -n python3-gmpy2 %common_desc

%package doc
# The content is LGPL-3.0-or-later.  Files added by Sphinx have the following
# licences:
# _static/*: BSD-2-Clause, except for the following:
# _static/css/*: MIT
# _static/jquery.js: MIT
# _static/js/*: MIT
# _static/pygments.css: LGPL-3.0-or-later
# genindex.html: BSD-2-Clause
# search.html: BSD-2-Clause
# searchindex.js: BSD-2-Clause
License:        LGPL-3.0-or-later AND BSD-2-Clause AND MIT
Summary:        Documentation for gmpy2
BuildArch:      noarch
Provides:       bundled(js-jquery)

%description doc
This package contains API documentation for gmpy2.

%prep
%autosetup -n gmpy2-%{version} -p1

%conf
%if %{with py3docs}
# Use local objects.inv for intersphinx
sed -e "s|\('https://docs\.python\.org/3/', \)None|\1'%{_docdir}/python3-docs/html/objects.inv'|" \
    -i docs/conf.py
%endif

%generate_buildrequires
%pyproject_buildrequires -x docs%{?with_tests:,tests}

%build
# Do not pass -pthread to the compiler or linker
export LDSHARED="gcc -shared"

%pyproject_wheel
PYTHONPATH=$PWD/$(ls -1d build/lib.linux*) make -C docs html

%install
%pyproject_install
%pyproject_save_files -l gmpy2

%check
%if %{with tests}
%pytest -v
%else
%pyproject_check_import
%endif

%files -n python3-gmpy2 -f %{pyproject_files}

%files doc
%doc docs/_build/html/*

%changelog
%autochangelog
