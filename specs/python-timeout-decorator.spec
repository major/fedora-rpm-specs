%bcond_without tests
%global srcname timeout-decorator

Name:           python-%{srcname}
Version:        0.5.0
Release:        %autorelease
Summary:        Timeout decorator for Python

License:        MIT
URL:            https://github.com/pnpnpn/timeout-decorator
Source0:        %{pypi_source}

BuildArch:      noarch

%description
A python module which provides a timeout decorator.

%package -n python3-%{srcname}
Summary:        %{summary}
BuildRequires:  python3-devel

%description -n python3-%{srcname}
A python module which provides a timeout decorator.

%prep
%autosetup -n %{srcname}-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files timeout_decorator

%if %{with tests}
%check
%pyproject_check_import timeout_decorator
%endif

%files -n python3-%{srcname} -f %{pyproject_files}
%doc README.rst

%changelog
%autochangelog
