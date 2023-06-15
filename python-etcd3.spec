%global srcname etcd3

Name:           python-%{srcname}
Version:        0.12.0
Release:        9%{?dist}
Summary:        Python client for the etcd API v3
License:        ASL 2.0
URL:            https://github.com/kragniz/python-etcd3
Source0:        %{url}/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  %{py3_dist setuptools}

%global _description %{summary}, supported under python 2.7, 3.4 and 3.5.

%description
%{_description}

%package -n python3-%{srcname}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{srcname}}

%description -n python%{python3_pkgversion}-%{srcname}
%{_description}


%prep
%autosetup -p1 -n %{name}-%{version}
sed -e 's|grpcio==.*|grpcio==1.26.0|' \
    -e 's|tenacity==.*|tenacity==6.0.0|' -i requirements/base.txt


%build
%py3_build


%install
%py3_install


%files -n python3-%{srcname}
%license LICENSE
%doc AUTHORS.rst CONTRIBUTING.rst HISTORY.rst README.rst
%{python3_sitelib}/%{srcname}/
%{python3_sitelib}/%{srcname}-*.egg-info/


%changelog
* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 0.12.0-9
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 0.12.0-6
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Sun Aug 15 2021 Vasiliy Glazov <vascom2@gmail.com> - 0.12.0-4
- Correct dependency version

* Tue Jul 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.0-3
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jun 29 2021 Vasiliy Glazov <vascom2@gmail.com> - 0.12.0-2
- Fix python macro

* Mon Jun 28 2021 Vasiliy Glazov <vascom2@gmail.com> - 0.12.0-1
- Initial packaging
