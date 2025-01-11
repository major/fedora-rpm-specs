Name:           python-oracledb
Version:        2.5.1
Release:        %{autorelease}
Summary:        OracleDB Driver

License:        Apache-2.0 OR UPL-1.0
URL:            https://oracle.github.io/python-oracledb/
Source:         %{pypi_source oracledb}

BuildRequires:  python3-devel
BuildRequires:  gcc

%global _description %{expand:
The python-oracledb driver is a Python programming language extension module
allowing Python programs to connect to Oracle Database. Python-oracledb 
is the new name for Oracle's popular cx_Oracle driver.}

%description %_description

%package -n python3-oracledb
Summary:        %{summary}

%description -n python3-oracledb %_description


%prep
%autosetup -p1 -n oracledb-%{version}


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files oracledb


# Tests require an Oracle database to connect to.
%check
%pyproject_check_import


%files -n python3-oracledb -f %{pyproject_files}


%changelog
%autochangelog
