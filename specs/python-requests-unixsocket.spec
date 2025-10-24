%global pypi_name requests_unixsocket2
%global package_name requests-unixsocket

# pypi:requests-unixsocket is nolonger maintained upstream
# pypi:requests-unixsocket2 is a for that provides requests-unixsocket
# This package pulls from requests-unixsocket2 and packages as requests-unixsocket
# See change log 0.4.0-1 for details.

Name:           python-%{package_name}
Version:        0.4.1
Release:        %autorelease
Summary:        Use requests to talk HTTP via a UNIX domain socket

# Automatically converted from old format: ASL 2.0 - review is highly recommended.
License:        Apache-2.0
URL:            https://github.com/thelabnyc/requests-unixsocket2
Source0:        %{pypi_source}
BuildArch:      noarch

%description
%{summary}.

%package -n     python3-%{package_name}
Summary:        Use requests to talk HTTP via a UNIX domain socket

BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(waitress)

%description -n python3-%{package_name}
%{summary}.

%prep
%autosetup -n %{pypi_name}-%{version}
# Remove shebangs
sed -i '1d' requests_unixsocket/tests/test_requests_unixsocket.py

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
mv %{buildroot}%{python3_sitelib}/requests_unixsocket2-%{version}.dist-info %{buildroot}%{python3_sitelib}/requests_unixsocket-%{version}.dist-info
sed -i 's/unixsocket2/unixsocket/g' %{buildroot}%{python3_sitelib}/requests_unixsocket-%{version}.dist-info/METADATA

%check
%pytest

%files -n python3-%{package_name}
%doc README.md
%license LICENSE
%{python3_sitelib}/requests_unixsocket
%{python3_sitelib}/requests_unixsocket-%{version}.dist-info

%changelog
%autochangelog
