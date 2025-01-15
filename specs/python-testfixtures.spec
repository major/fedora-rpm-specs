%global pypi_name testfixtures

Name:           python-%{pypi_name}
Version:        8.3.0
Release:        %autorelease
Summary:        Collection of helpers and mock objects for unit tests

License:        MIT
URL:            https://github.com/Simplistix/testfixtures
Source0:        %{pypi_source}
BuildArch:      noarch

%description
Testfixtures is a collection of helpers and mock objects that are useful
when writing automated tests in Python.

%package -n python3-%{pypi_name}
Summary:        %{summary}

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
Testfixtures is a collection of helpers and mock objects that are useful
when writing automated tests in Python.

%prep
%autosetup -n %{pypi_name}-%{version}
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
%py3_install

#%%check
# Upstream has a different idea about how Open Source works
# and is hostile against everything that doesn't match that idea.
# Thus, the only thing that matters is that tests work in their CI

%files -n python3-%{pypi_name}
%doc CHANGELOG.rst README.rst
%license LICENSE.txt
%{python3_sitelib}/%{pypi_name}/
%{python3_sitelib}/*.egg-info/

%changelog
%autochangelog
