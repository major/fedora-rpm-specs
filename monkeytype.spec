%global srcname MonkeyType

Name:           monkeytype
Version:        21.5.0
Release:        %autorelease
Summary:        Generating Python type annotations from sampled production types
License:        BSD
URL:            https://github.com/instagram/%{srcname}
# PyPI source has no tests
# Source0:        %%{pypi_source %%{srcname}}
Source0:        %{url}/archive/v%{version}/%{srcname}-%{version}.tar.gz

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
