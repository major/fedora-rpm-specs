%global pypi_name aiodnsbrute

Name:           %{pypi_name}
Version:        0.3.3
Release:        %autorelease
Summary:        DNS asynchronous brute force utility

License:        GPLv3
URL:            https://github.com/blark/aiodnsbrute
Source0:        https://github.com/blark/aiodnsbrute/archive/v%{version}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools

%description
A Python tool that uses asyncio to brute force domain names asynchronously.

%prep
%autosetup -n %{pypi_name}-%{version}
sed -i -e $'s/ \''asyncio\'',//g' setup.py

%build
%py3_build

%install
%py3_install

%files
%doc CHANGELOG README.md
%license LICENSE.txt
%{_bindir}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}/
%{python3_sitelib}/%{pypi_name}*.egg-info

%changelog
%autochangelog

