Name:           python-oracledb
Version:        3.4.0
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


%pyproject_extras_subpkg -n python3-oracledb oci_config oci_auth azure_config azure_auth


%package -n python3-oracledb
Summary:        %{summary}

%description -n python3-oracledb %_description


%prep
%autosetup -p1 -n oracledb-%{version}


%generate_buildrequires
%pyproject_buildrequires -x oci_config,oci_auth,azure_config,azure_auth


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
