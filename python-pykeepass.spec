# Created by pyp2rpm-3.3.2
%global pypi_name pykeepass

Name:           python-%{pypi_name}
Version:        4.0.3
Release:        %autorelease
Summary:        Python library to interact with keepass databases

License:        GPLv3
URL:            https://github.com/libkeepass/pykeepass
Source0:        %{pypi_source}
BuildArch:      noarch
 
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)

%description
This library allows you to write entries to a KeePass database.


%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}
 
%description -n python3-%{pypi_name}
This library allows you to write entries to a KeePass database.


%prep
%autosetup -n %{pypi_name}-%{version}

# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

sed -i 's|pycryptodomex==|pycryptodomex>=|' requirements.txt
sed -i 's|construct==|construct>=|' requirements.txt
sed -i 's|construct==|construct>=|' setup.py


%build
%py3_build


%install
%py3_install


%files -n python3-%{pypi_name}
%license LICENSE
%doc README.rst
%{python3_sitelib}/%{pypi_name}/
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info/


%changelog
%autochangelog
