# Upstream tests are broken in multiple ways, disable for now
%bcond tests 0

%global srcname telnetlib3
%global forgeurl https://github.com/jquast/telnetlib3

Name:           python-telnetlib3
Version:        2.0.4
Release:        %autorelease
Summary:        Python 3 asyncio Telnet server and client Protocol library

License:        ISC
URL:            http://telnetlib3.rtfd.org/
Source:         %{forgeurl}/archive/%{version}/%{srcname}-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python3-devel
%if %{with tests}
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(pexpect)
BuildRequires:  python3dist(pytest-asyncio)
%endif

%global _description %{expand:
telnetlib3 is a Telnet Client and Server library for Python.}

%description %_description

%package -n     python3-telnetlib3
Summary:        %{summary}

%description -n python3-telnetlib3 %_description

%prep
%autosetup -p1 -n telnetlib3-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l telnetlib3

%check
%if %{with tests}
PYTHONPATH="telnetlib3:$PYTHONPATH" %pytest
%else
%pyproject_check_import
%endif

%files -n python3-telnetlib3 -f %{pyproject_files}
%doc README.rst
%{_bindir}/telnetlib3-client
%{_bindir}/telnetlib3-server

%changelog
%autochangelog
