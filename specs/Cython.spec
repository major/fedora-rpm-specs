%bcond tests 1

# This bcond allows to ship a non-compiled version
# Slower, but sometimes necessary with alpha Python versions
%bcond cython_compile 1

Name:           Cython
Version:        3.0.11
Release:        %autorelease
Summary:        Language for writing Python extension modules

License:        Apache-2.0
URL:            http://www.cython.org
Source:         https://github.com/cython/cython/archive/%{version}/Cython-%{version}.tar.gz

# Backport patch for NumPy 2.x
# https://github.com/cython/cython/issues/6581
Patch:          https://github.com/cython/cython/commit/852286242ee46cc16f0a6efef7eb40a5ab3c57d5.patch

BuildRequires:  python3-devel

%if %{with tests}
BuildRequires:  gcc-c++
BuildRequires:  gdb
# optionally uses Python's test.support for some test
BuildRequires:  python3-test
# the Python tests requirements are curated manually
# the test-requirements*.txt files mix in coverage and optional deps
BuildRequires:  python3-numpy
%if %{undefined rhel}
# We don't want to pull in the following deps to RHEL just to run more tests.
# The tests use IPython.testing.globalipapp:
BuildRequires:  python3-ipython+test
BuildRequires:  python3-pythran
# The tests requiring jedi are optional and skipped when jedi is not installed.
# Note that the jedi tests were forcefully disabled a long time ago,
# in https://github.com/cython/cython/issues/1845 far, far away.
# We keep the dependency here so we don't forget to re-add it once the balance is restored.
BuildRequires:  python3-jedi
%endif
%endif

%if %{with cython_compile}
BuildRequires:  gcc
%else
BuildArch:      noarch
%endif

%global _description %{expand:
The Cython language makes writing C extensions for the Python language as easy
as Python itself. Cython is a source code translator based on Pyrex,
but supports more cutting edge functionality and optimizations.

The Cython language is a superset of the Python language (almost all Python
code is also valid Cython code), but Cython additionally supports optional
static typing to natively call C functions, operate with C++ classes and
declare fast C types on variables and class attributes.
This allows the compiler to generate very efficient C code from Cython code.

This makes Cython the ideal language for writing glue code for external C/C++
libraries, and for fast C modules that speed up the execution of Python code.}

%description %{_description}


%package -n python3-cython
Summary:        %{summary}
Provides:       Cython = %{?epoch:%{epoch}:}%{version}-%{release}
Provides:       Cython%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}
Provides:       cython = %{?epoch:%{epoch}:}%{version}-%{release}
Provides:       cython%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}
%py_provides    python3-Cython
Obsoletes:      python3-Cython < 3~~

# A small templating library is bundled in Cython/Tempita
# Upstream version 0.5.2 is available from https://pypi.org/project/Tempita
# but the bundled copy is patched and reorganized.
# Upstream homepage is inaccessible.
Provides:       bundled(python3dist(tempita))

%description -n python3-cython %{_description}


%prep
%autosetup -n cython-%{version} -p1


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel %{!?with_cython_compile:-C--global-option=--no-cython-compile}


%install
%pyproject_install
%pyproject_save_files Cython cython pyximport


%if %{with tests}
%check
# run.pstats_profile_test* fails on Python 3.12
#   https://github.com/cython/cython/issues/5470
# run.numpy_parallel fails on i686
#   https://github.com/cython/cython/issues/6200
# run.parallel fails on i686
#   https://github.com/cython/cython/issues/2807
%{python3} runtests.py -vv --no-pyregr %{?_smp_mflags} \
  --exclude 'run.pstats_profile_test*' \
  %ifarch %{ix86}
  --exclude run.parallel \
  --exclude run.numpy_parallel \
  %endif

%endif


%files -n python3-cython -f %{pyproject_files}
%doc *.txt Demos Doc Tools
%{_bindir}/cython
%{_bindir}/cygdb
%{_bindir}/cythonize


%changelog
%autochangelog
