Name:           python-pytest-check
Version:        2.5.3
Release:        %autorelease
Summary:        A pytest plugin that allows multiple failures per test 

License:        MIT
URL:            https://github.com/okken/pytest-check
Source:         %{pypi_source pytest_check}

BuildArch:      noarch
BuildRequires:  python3-devel

%global _description %{expand:
A pytest plugin that allows multiple failures per test.}

%description %_description

%package -n python3-pytest-check
Summary:        %{summary}
%description -n python3-pytest-check %_description


%prep
%autosetup -n pytest_check-%{version}


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files pytest_check


%check
%pytest


%files -n python3-pytest-check -f %{pyproject_files}
%license LICENSE.txt
%doc README.md


%changelog
%autochangelog

