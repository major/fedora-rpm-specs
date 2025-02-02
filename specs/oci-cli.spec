# 22 of the 23 provided unit tests require a valid configuration file and certificate.
# The remaining dependency fails due to the dependency adjustments in %%prep
%bcond_with     tests

Name:           oci-cli
Version:        3.51.5
Release:        %autorelease
Summary:        Command Line Interface for Oracle Cloud Infrastructure 

License:        UPL-1.0
URL:            https://github.com/oracle/oci-cli
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  python3-devel

%if %{with tests}
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(vcrpy)
%endif

%global _description %{expand:
This is the command line interface for Oracle Cloud Infrastructure.}

%description %{_description}

# Awaiting a fix for python-cx-oracle
# https://src.fedoraproject.org/rpms/python-cx-oracle/pull-request/1
# %%pyproject_extras_subpkg -n %%{name} db


%prep
%autosetup -n %{name}-%{version}

# Remove upper limits and pinned dependencies.
sed -i -e 's/,[<=]\+[0-9\.]\+//' -e 's/==/>=/' setup.py

# Work around a versioning bug when trying to find terminaltables.
sed -i 's/terminaltables>=[0-9\.]\+/terminaltables/' setup.py

%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install

# Remove extra script that isn't needed.
rm -f %{buildroot}/%{_bindir}/create_backup_from_onprem

%pyproject_save_files alloy common_util interactive oci_cli services


%check
%pyproject_check_import -e 'oci_cli.scripts.database.dbaas' -e 'services.*'

%if %{with tests}
%pytest
%endif


%files -n %{name} -f %{pyproject_files}
%license LICENSE.txt THIRD_PARTY_LICENSES.txt
%doc CHANGELOG.rst COMMON_ISSUES.rst README.rst
%{_bindir}/oci


%changelog
%autochangelog
