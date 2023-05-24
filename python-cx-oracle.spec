%global pypi_name cx_Oracle
%global local_name cx-oracle
# Tests requires the Oracle Client libraries
%bcond_with check

Name:           python-%{local_name}
Version:        8.3.0
Release:        %autorelease
Summary:        Python interface to Oracle

License:        BSD
URL:            https://oracle.github.io/python-cx_Oracle
Source0:        %{pypi_source}

BuildRequires:  gcc

%description
Python interface to Oracle Database conforming to the Python DB API 2.0
specification.

%package -n     python3-%{local_name}
Summary:        %{summary}

BuildRequires:  python3-devel

%description -n python3-%{local_name}
Python interface to Oracle Database conforming to the Python DB API 2.0
specification.

%prep
%autosetup -n %{pypi_name}-%{version}

%generate_buildrequires
%pyproject_buildrequires -r

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files cx_Oracle
rm -rf %{buildroot}%{_prefix}/cx_Oracle-doc

%if %{with check}
%check
%python3 setup.py test
%endif

%files -n python3-%{local_name} -f %{pyproject_files}
%license LICENSE.txt
%doc README.txt

%changelog
%autochangelog
