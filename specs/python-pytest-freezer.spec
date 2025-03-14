Name:           python-pytest-freezer
Version:        0.4.9
Release:        %autorelease
Summary:        Pytest plugin providing a fixture interface for freezegun

# SPDX
License:        MIT
URL:            https://github.com/pytest-dev/pytest-freezer
Source:         %{pypi_source pytest_freezer}

BuildSystem:            pyproject
BuildOption(install):   -l pytest_freezer

BuildArch:      noarch

BuildRequires:  %{py3_dist pytest}

%global common_description %{expand:
%{summary}.}

%description %{common_description}


%package -n     python3-pytest-freezer
Summary:        %{summary}

%description -n python3-pytest-freezer %{common_description}


%check -a
%pytest -v


%files -n python3-pytest-freezer -f %{pyproject_files}
%doc README.md


%changelog
%autochangelog
