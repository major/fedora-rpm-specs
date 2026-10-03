%global pypi_name pyModbusTCP
%global srcname %{py_dist_name %{pypi_name}}

Name:           python-%{pypi_name}
Version:        0.3.1
Release:        %autorelease
Summary:        A simple Modbus/TCP library for Python

License:        MIT
URL:            https://github.com/sourceperl/pyModbusTCP
Source0:        %{pypi_source %{srcname}}
BuildArch:      noarch
 
BuildRequires:  python3-devel
# For tests
BuildRequires:  python3-pytest


%description
pyModbusTCP A simple Modbus/TCP client library for Python.
Since version 0.1.0, a server is also available for test 
purpose only (don't use in project). pyModbusTCP is pure Python 
code without any extension or external module dependency.


%package -n     python3-%{pypi_name}
Summary:        %{summary}


%description -n python3-%{pypi_name}
pyModbusTCP A simple Modbus/TCP client library for Python.
Since version 0.1.0, a server is also available for test 
purpose only (don't use in project). pyModbusTCP is pure Python 
code without any extension or external module dependency.


%prep
%autosetup -n %{srcname}-%{version}


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files -l %{pypi_name}


%check
%pytest


%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc README.rst

%changelog
%autochangelog
