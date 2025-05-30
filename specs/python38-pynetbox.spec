%global srcname pynetbox
%global __python3 /usr/bin/python3.8
%global python3_pkgversion 38

Name:           python%{python3_pkgversion}-%{srcname}
Version:        6.6.2
Release:        %autorelease
Summary:        Python API client library for Netbox

License:        ASL 2.0
URL:            https://github.com/digitalocean/pynetbox
Source:         %{pypi_source}

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-rpm-macros
BuildRequires:  python%{python3_pkgversion}-setuptools

BuildArch:      noarch

%global _description \
%{summary}.

%description %{_description}

%prep
%autosetup -n %{srcname}-%{version} -p1
rm -vr *.egg-info
sed -i -e "s/six==1\.\*/six>=1.0,<2.0/" setup.py
sed -i -e '/scm/d' setup.py

%build
%py3_build

%install
%py3_install

%files
%license LICENSE
%doc README.md CHANGELOG.md
%{python3_sitelib}/%{srcname}/
%{python3_sitelib}/%{srcname}-*.egg-info/

%changelog
%autochangelog
