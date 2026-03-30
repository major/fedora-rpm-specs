%global pypi_name requestsexceptions

%global common_desc %{expand:
This is a simple library to find the correct path to exceptions in the
requests library regardless of whether they are bundled.}

Name:           python-%{pypi_name}
Version:        1.4.0
%forgemeta
Release:        %autorelease
Summary:        Import exceptions from potentially bundled packages in requests
License:        Apache-2.0
URL:            http://www.openstack.org/
Source0:        %{pypi_source %pypi_name}
# to here
BuildArch:      noarch
BuildRequires:  python3-devel


%description
%{common_desc}


%package -n python3-%{pypi_name}
Summary:        %summary


%description -n python3-%{pypi_name}
%{common_desc}


%prep
%autosetup -n %{pypi_name}-%{version}

sed -i \
    -e "/^hacking[[:space:]]*[!><=]/d" \
    test-requirements.txt


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install

%pyproject_save_files -l %{pypi_name}


%check
%pyproject_check_import %{pypi_name}


%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc README.rst
%license LICENSE


%changelog
%autochangelog
