Name:           python-pytest-cases
Version:        3.10.1
Release:        %autorelease
Summary:        Separate test code from test cases in pytest

License:        BSD-3-Clause
URL:            https://pypi.org/project/pytest-cases/
Source0:        %{pypi_source pytest_cases}

BuildArch:      noarch
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-pkg-resources
BuildRequires:  python3dist(decopatch)
BuildRequires:  python3dist(makefun) > 1.7
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(pytest-asyncio)
BuildRequires:  python3dist(pytest-harvest) > 1.10
BuildRequires:  python3dist(pytest-steps)

%description
%{summary}.

%package -n python3-pytest-cases
Summary: %{summary}

%description -n python3-pytest-cases
%{summary}.

%prep
%autosetup -n pytest_cases-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l pytest_cases

%check
%pyproject_check_import
%pytest

%files -n python3-pytest-cases -f %{pyproject_files}
%doc README.md

%changelog
%autochangelog
