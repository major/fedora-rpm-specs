%global srcname mujson
%global common_description %{expand:
mujson lets python libraries make use of the most performant JSON functions
available at import time.  It is small, and does not itself implement any
encoding or decoding functionality.}


Name:           python-%{srcname}
Version:        1.4
Release:        6%{?dist}
Summary:        Use the fastest JSON functions available at import time
License:        MIT
URL:            https://github.com/mattgiles/mujson
# PyPI tarball is missing license
# https://github.com/mattgiles/mujson/issues/8
Source0:        %{url}/archive/%{version}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch


%description %{common_description}


%package -n python3-%{srcname}
Summary:        %{summary}
BuildRequires:  python3-devel
BuildRequires:  %{py3_dist setuptools}


%description -n python3-%{srcname} %{common_description}


%prep
%autosetup -n %{srcname}-%{version}


%build
%py3_build


%install
%py3_install


%files -n python3-%{srcname}
%license LICENSE
%doc README.md
%{python3_sitelib}/%{srcname}
%{python3_sitelib}/%{srcname}-%{version}-py%{python3_version}.egg-info


%changelog
* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 1.4-5
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 1.4-2
- Rebuilt for Python 3.10

* Tue Apr 13 2021 Carl George <carl@george.computer> - 1.4-1
- Initial package rhbz#1948882
