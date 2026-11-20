Name:           python-PyMySQL
Version:        1.2.4
Release:        1%{?dist}
Summary:        Pure-Python MySQL client library

License:        MIT
URL:            https://pypi.org/project/pymysql/
Source:         %{pypi_source pymysql}

BuildArch:      noarch

%description
This package contains a pure-Python MySQL client library. The goal of PyMySQL is
to be a drop-in replacement for MySQLdb and work on CPython, PyPy, IronPython
and Jython.


%package -n     python3-PyMySQL
Summary:        %{summary}
BuildRequires:  python3-devel


%description -n python3-PyMySQL
This package contains a pure-Python MySQL client library. The goal of PyMySQL is
to be a drop-in replacement for MySQLdb and work on CPython, PyPy, IronPython
and Jython.


%pyproject_extras_subpkg -n python3-PyMySQL rsa %{!?rhel:ed25519}


%prep
%autosetup -n pymysql-%{version}


%generate_buildrequires
%pyproject_buildrequires -x rsa %{!?rhel:-x ed25519}


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files pymysql


%check
# Tests cannot be launch on koji, they require a mysqldb running.
%pyproject_check_import


%files -n python3-PyMySQL -f %{pyproject_files}
%doc README.md


%changelog
%autochangelog
