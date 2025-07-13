# EPEL is missing dependencies required for docs
%if 0%{?rhel}
%bcond_with docs
%else
%bcond_without docs
%endif
%bcond_without tests

%global modname testslide
%global pypi_name TestSlide
%global obs_verrel 2.6.4-99

Name:           python-%{pypi_name}
Version:        2.7.1
Release:        %autorelease
Summary:        A Python test framework

License:        MIT
URL:            https://github.com/facebook/TestSlide
# The PyPI tarball doesn't include tests, so use the original source instead
Source0:        %{url}/archive/%{version}/%{pypi_name}-%{version}.tar.gz

# Fedora-only patches (100-199)
# Updating Testslide to typeguard 3.02
# https://github.com/facebook/TestSlide/pull/352
#
# Rebased to 2.7.1; version bound loosened to allow 4.x as well as 3.x
Patch100:       TestSlide-2.7.1-typeguard-4.patch
#     for name in klass.__dict__:
# E   RuntimeError: dictionary changed size during iteration
Patch101:       TestSlide-strictmock-fix-dictionary-changed-size.diff

BuildArch:      noarch

BuildRequires:  python3-devel

%if %{with docs}
# Docs requirements
BuildRequires:  make
BuildRequires:  /usr/bin/tput
BuildRequires:  python3-ipython-sphinx
%endif

%if %{with tests}
# Test requirements
BuildRequires:  python3dist(pytest)
%endif

%global _description %{expand:
A test framework for Python that enable unit testing / TDD / BDD to be
productive and enjoyable.

Its well behaved mocks with thorough API validations catches bugs both
when code is first written or long in the future when it is changed.

The flexibility of using them with existing unittest.TestCase or TestSlide's
own test runner let users get its benefits without requiring refactoring
existing code.}

%description %{_description}


%package -n     python3-%{modname}
Summary:        %{summary}
Provides:       python3-%{pypi_name} = %{version}-%{release}
Obsoletes:      python3-%{pypi_name} < %{obs_verrel}

%description -n python3-%{modname} %{_description}


%if %{with docs}
%package -n     python3-%{modname}-docs
Summary:        Documentation for python3-%{pypi_name}
Provides:       python3-%{pypi_name}-docs = %{version}-%{release}
Obsoletes:      python3-%{pypi_name} < %{obs_verrel}

%description -n python3-%{modname}-docs %{_description}

The python3-%{modname}-docs package contains documentation for
python3-%{modname}.
%endif


%prep
%autosetup -n %{pypi_name}-%{version} -N
%autopatch -p1 -M 99
%if 0%{?fedora} || 0%{?rhel} >= 10
%autopatch -p1 -m 100 -M 199
%endif
# remove unnecessary test BRs
sed -r -i '/^(black|coverage|coveralls|flake8|isort|mypy|twine)/d' \
    requirements-dev.txt
sed -r -i 's/^([[:blank:]]*)("COVERAGE_PROCESS_START")/\1# \2/' \
    tests/cli_unittest.py
sed -i '/^sphinx-autobuild/d' requirements-dev.txt

%generate_buildrequires
%pyproject_buildrequires -r requirements-dev.txt


%build
%pyproject_wheel
%if %{with docs}
make docs V=1
%endif

%install
%pyproject_install
%pyproject_save_files %{modname}


%if %{with tests}
%check
# deselect tests sensitive to version of pygments
# see e.g. rhbz#2350306
%pytest tests/*_unittest.py tests/*_testslide.py \
%if 0%{?el9} || 0%{?python3_version_nodots} >= 314
  --deselect tests/cli_unittest.py::TestCliDocumentFormatter::test_prints_exceptions_with_cause \
  --deselect tests/cli_unittest.py::TestCliProgressFormatter::test_prints_exceptions_with_cause \
  --deselect tests/cli_unittest.py::TestCliLongFormatter::test_prints_exceptions_with_cause \
%endif
;
%endif


%files -n python3-%{modname} -f %{pyproject_files}
%license LICENSE
%doc README.md
%{_bindir}/testslide

%if %{with docs}
%files -n python3-%{modname}-docs
%doc docs/_build/html
%endif


%changelog
%autochangelog
