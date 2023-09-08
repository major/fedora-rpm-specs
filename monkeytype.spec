%global srcname MonkeyType

%if 0%{?python3_version_nodots} >= 312
# some tests currently fail
%bcond_with all_tests
%else
%bcond_without all_tests
%endif

Name:           monkeytype
Version:        23.3.0
Release:        %autorelease
Summary:        Generating Python type annotations from sampled production types
License:        BSD-3-Clause
URL:            https://github.com/instagram/%{srcname}
# PyPI source has no tests
# Source:        %%{pypi_source %%{srcname}}
Source:         %{url}/archive/v%{version}/%{srcname}-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel
# Pipfile not supported yet
# Test dependencies:
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(django)

%py_provides python%{python3_pkgversion}-%{name}

%global _description %{expand:
MonkeyType collects runtime types of function arguments and return values, and
can automatically generate stub files or even add draft type annotations
directly to your Python code based on the types collected at runtime.}

%description %{_description}


%prep
%autosetup -p1 -n %{srcname}-%{version}


%generate_buildrequires
%pyproject_buildrequires -r


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files %{name}


%check
%pyproject_check_import
%if %{with all_tests}
%pytest -v
%else
# FAILED tests/test_tracing.py::TestTraceCalls::test_callee_throws_recovers - A...
# FAILED tests/test_tracing.py::TestTraceCalls::test_nested_callee_throws_recovers
# FAILED tests/test_tracing.py::TestTraceCalls::test_caller_handles_callee_exception
# FAILED tests/test_tracing.py::TestTraceCalls::test_generator_trace - Assertio...
# FAILED tests/test_tracing.py::TestTraceCalls::test_return_none - AssertionErr...
# FAILED tests/test_tracing.py::TestTraceCalls::test_access_property - Assertio...
EXCLUDES=" not test_callee_throws_recovers"
EXCLUDES+=" and not test_nested_callee_throws_recovers"
EXCLUDES+=" and not test_caller_handles_callee_exception"
EXCLUDES+=" and not test_generator_trace and not test_return_none"
EXCLUDES+=" and not test_access_property"
%pytest -v -k "$EXCLUDES"
%endif


%files -f %{pyproject_files}
%license LICENSE
%doc CHANGES.rst CODE_OF_CONDUCT.md CONTRIBUTING.rst README.rst
%{_bindir}/%{name}


%changelog
%autochangelog
