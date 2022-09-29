%global srcname MonkeyType

Name:           monkeytype
Version:        22.2.0
Release:        %autorelease
Summary:        Generating Python type annotations from sampled production types
License:        BSD
URL:            https://github.com/instagram/%{srcname}
# PyPI source has no tests
# Source:        %%{pypi_source %%{srcname}}
Source:         %{url}/archive/v%{version}/%{srcname}-%{version}.tar.gz
# Fix for Python 3.11's changes to handling of Tuple[()]
# based on https://github.com/Instagram/MonkeyType/pull/273.patch
Patch:          fix-py311-emptytuple.diff
# skip test_generator_trace
# see https://github.com/Instagram/MonkeyType/issues/274
Patch:          skip-test-generator-trace-py311.diff

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
# we don't care about coverage checks
rm pytest.ini


%generate_buildrequires
%pyproject_buildrequires -r


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files %{name}


%check
%pytest


%files -f %{pyproject_files}
%license LICENSE
%doc CHANGES.rst CODE_OF_CONDUCT.md CONTRIBUTING.rst README.rst
%{_bindir}/%{name}


%changelog
%autochangelog
