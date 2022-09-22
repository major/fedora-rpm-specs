# Created by pyp2rpm-3.3.2

%global srcname flask-caching

Name:           python-%{srcname}
Version:        2.0.1
Release:        1%{?dist}
Summary:        Adds caching support to your Flask application

License:        BSD
URL:            https://github.com/sh4nks/flask-caching
Source0:        https://github.com/sh4nks/%{srcname}/archive/v%{version}/%{srcname}-v%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3dist(asgiref)
BuildRequires:  python3dist(cachelib)
BuildRequires:  python3dist(flask)
BuildRequires:  python3dist(pylibmc)
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(pytest-runner)
BuildRequires:  python3dist(pytest-cov)
BuildRequires:  python3dist(pytest-xprocess)
BuildRequires:  python3dist(pytest-asyncio)
BuildRequires:  python3dist(redis)
BuildRequires:  redis
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(sphinx)

%description
Flask-Caching Adds easy cache support to Flask

%package -n     python3-%{srcname}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{srcname}}

Requires:       python3dist(flask)
%description -n python3-%{srcname}
Flask-Caching Adds easy cache support to Flask

%package -n python-%{srcname}-doc
Summary:        Flask-Caching documentation
%description -n python-%{srcname}-doc
Documentation for Flask-Caching

%prep
%autosetup -n %{srcname}-%{version}
# Remove bundled egg-info
rm -rf %{srcname}.egg-info

%build

%py3_build
# generate html docs
PYTHONPATH=${PWD} sphinx-build-3 docs html
# remove the sphinx-build leftovers
rm -rf html/.{doctrees,buildinfo}

%install
%py3_install

%check
redis-server &
%pytest
kill %1

%files -n python3-%{srcname}
%license LICENSE docs/license.rst
%doc README.rst
%{python3_sitelib}/flask_caching
%{python3_sitelib}/Flask_Caching-%{version}-py%{python3_version}.egg-info

%files -n python-%{srcname}-doc
%doc html
%license LICENSE docs/license.rst

%changelog
* Wed Aug 03 2022 Frantisek Zatloukal <fzatlouk@redhat.com> - 2.0.1-1
- Update to 2.0.1 (Closes RHBZ#2112611)

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jul 18 2022 Frantisek Zatloukal <fzatlouk@redhat.com> - 2.0.0-2
- Relax Flask requirements

* Mon Jun 27 2022 Frantisek Zatloukal <fzatlouk@redhat.com> - 2.0.0-1
- Update to 2.0.0

* Tue Jun 14 2022 Python Maint <python-maint@redhat.com> - 1.10.1-5
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 1.10.1-2
- Rebuilt for Python 3.10

* Mon Apr 12 2021 Frantisek Zatloukal <fzatlouk@redhat.com> - 1.10.1-1
- Update to 1.10.1

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jul 24 2020 Frantisek Zatloukal <fzatlouk@redhat.com> - 1.9.0-1
- Update to 1.9.0

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.8.0-3
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Jan 06 2020 Frantisek Zatloukal <fzatlouk@redhat.com> - 1.8.0-1
- Update to 1.8.0
- Drop hack for new pytest-cov

* Mon Jun 17 2019 Lukas Brabec <lbrabec@redhat.com> - 1.7.2-1
- Initial package.