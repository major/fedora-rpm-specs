%global srcname aioruckus

# Tests are disabled as they require a live deployment to test against
%bcond_with tests

Name:           python-%{srcname}
Version:        0.37
Release:        %autorelease
Summary:        Interact with Ruckus Unleashed and ZoneDirector devices

License:        0BSD
URL:            https://github.com/ms264556/aioruckus
Source:         %{pypi_source}

BuildArch:      noarch
BuildRequires:  python3-devel
%if %{with tests}
BuildRequires:  python3-pytest
%endif

%global _description %{expand:
This package provides a Python API which interacts with Ruckus Unleashed and
ZoneDirector devices via their AJAX Web Service interface. Configuration
information can also be queried from Ruckus Unleashed and ZoneDirector backup
files.}

%description %_description

%package -n     python3-%{srcname}
Summary:        %{summary}

%description -n python3-%{srcname} %_description

%prep
%autosetup -p1 -n %{srcname}-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files %{srcname}

%check
%if %{with tests}
%pytest
%else
%pyproject_check_import
%endif

%files -n python3-%{srcname} -f %{pyproject_files}
%doc README.md

%changelog
%autochangelog
