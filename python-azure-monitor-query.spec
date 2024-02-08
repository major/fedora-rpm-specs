Name:           python-azure-monitor-query
Version:        1.2.0
Release:        %autorelease
Summary:        Microsoft Azure Monitor Query Client Library for Python

License:        MIT
URL:            https://github.com/Azure/azure-sdk-for-python
Source:         %{pypi_source azure-monitor-query %{version} zip}

BuildArch:      noarch
BuildRequires:  python3-devel


%global _description %{expand:
Microsoft Azure Monitor Query Client Library for Python.}

%description %_description

%package -n     python3-azure-monitor-query
Summary:        %{summary}

%description -n python3-azure-monitor-query %_description


%prep
%autosetup -p1 -n azure-monitor-query-%{version}


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files azure


%check
%pyproject_check_import


%files -n python3-azure-monitor-query -f %{pyproject_files}


%changelog
%autochangelog
