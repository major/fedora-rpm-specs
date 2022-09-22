%global srcname prometheus_client

Name:           python-%{srcname}
Version:        0.13.1
Release:        3%{?dist}
Summary:        Python client for Prometheus

License:        ASL 2.0
URL:            https://github.com/prometheus/client_python
Source:         %{url}/archive/v%{version}/%{srcname}-%{version}.tar.gz
Patch0001:      0001-Remove-the-bundled-decorator-package.patch

BuildArch:      noarch

%description
%{summary}.

%package -n python3-%{srcname}
Summary:        %{summary}
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3dist(decorator)
BuildRequires:  python3dist(pytest)
%{?python_provide:%python_provide python3-%{srcname}}

%description -n python3-%{srcname}
%{summary}.

%package -n python3-%{srcname}+twisted
Summary:        %{summary}
Requires:       python3-%{srcname} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       python%{python3_version}dist(twisted)
BuildRequires:  python3dist(twisted)
%{?python_provide:%python_provide python3-%{srcname}+twisted}

%description -n python3-%{srcname}+twisted
%{summary}.

"twisted" extras.

%prep
%autosetup -p1 -n client_python-%{version}
sed -i -e '1{/^#!/d}' prometheus_client/__init__.py

%build
%py3_build

%install
%py3_install

%check
%{__python3} -m pytest -v

%files -n python3-%{srcname}
%license LICENSE
%doc README.md MAINTAINERS.md
%{python3_sitelib}/%{srcname}/
%{python3_sitelib}/%{srcname}-*.egg-info/

%files -n python3-%{srcname}+twisted
%{?python_extras_subpkg:%ghost %{python3_sitelib}/%{srcname}-*.egg-info/}

%changelog
* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.13.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue Jun 14 2022 Python Maint <python-maint@redhat.com> - 0.13.1-2
- Rebuilt for Python 3.11

* Tue Feb 01 2022 Matt Prahl <mprahl@redhat.com> - 0.13.1-1
- Update to 0.13.1

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 0.9.0-3
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Dec 12 2020 Igor Raits <ignatenkobrain@fedoraproject.org> - 0.9.0-1
- Update to 0.9.0

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.1-6
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jul 10 2020 Miro Hrončok <mhroncok@redhat.com> - 0.7.1-4
- Add metadata for Python extras subpackages

* Sun May 24 2020 Miro Hrončok <mhroncok@redhat.com> - 0.7.1-3
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Oct 23 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.7.1-1
- Update to 0.7.1
- Split twisted extras into a separate subpackage

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.6.0-4
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Sun Aug 18 2019 Miro Hrončok <mhroncok@redhat.com> - 0.6.0-3
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Feb 21 2019 mprahl <mprahl@redhat.com> - 0.6.0-1
- Update to 0.6.0

* Wed Feb 20 2019 mprahl <mprahl@redhat.com> - 0.5.0-2
- Remove #!/usr/bin/python line from prometheus_client/openmetrics/*.py

* Thu Feb 07 2019 mprahl <mprahl@redhat.com> - 0.5.0-1
- Update to 0.5.0

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Jan 14 2019 Miro Hrončok <mhroncok@redhat.com> - 0.2.0-4
- Subpackage python2-prometheus_client has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.2.0-2
- Rebuilt for Python 3.7

* Sat Jun 09 2018 Jeremy Cline <jeremy@jcline.org> - 0.2.0-1
- Initial package
