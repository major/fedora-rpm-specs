%global pypi_name pytest_describe

%global _description %{expand:
Plugin for pytest that allows tests to be written in arbitrary
nested describe-blocks, similar to RSpec (Ruby) and
Jasmine (JavaScript).}


Name:           python-%{pypi_name}
Version:        3.2.0
Release:        %autorelease
Summary:        Pytest plugin adds nested describe blocks

License:        MIT
URL:            https://github.com/pytest-dev/pytest-describe
Source:         %pypi_source

BuildArch:      noarch
BuildRequires:  python3-devel


%description %_description


%package -n     python3-%{pypi_name}
Summary:        %{summary}


%description -n python3-%{pypi_name} %_description


%prep
%autosetup -n %{pypi_name}-%{version}

%pyproject_patch_dependency uv-build:drop_upper


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files -l %pypi_name


%check
%pytest


%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc README.md


%changelog
%autochangelog
