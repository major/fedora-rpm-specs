%global srcname astroquery
%global sum Python module to access astronomical online data resources

Name:           python-%{srcname}
Version:        0.4.5
Release:        5%{?dist}
Summary:        %{sum}

License:        BSD
URL:            http://pypi.python.org/pypi/%{srcname}
Source0:        https://files.pythonhosted.org/packages/source/a/%{srcname}/%{srcname}-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python3-astropy
BuildRequires:  python3-beautifulsoup4
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-html5lib
BuildRequires:  python3-keyring
BuildRequires:  python3-pyvo
BuildRequires:  python3-requests
# Doc generation not yet working with rawhide 
#BuildRequires:  python3-sphinx

%description
Astroquery is an astropy affiliated package that contains a collection of tools
to access online Astronomical data.

%package -n python3-%{srcname}
Summary:        %{sum}
%{?python_provide:%python_provide python3-%{srcname}}
Requires:       python3-astropy
Requires:       python3-beautifulsoup4
Requires:       python3-html5lib
Requires:       python3-keyring
Requires:       python3-pyvo
Requires:       python3-requests

%description -n python3-%{srcname}
Astroquery is an astropy affiliated package that contains a collection of tools
to access online Astronomical data.

%prep
%autosetup -n %{srcname}-%{version} -p1

%build
%py3_build

%install
%py3_install

%files -n python3-%{srcname}
%doc README.rst
%{python3_sitelib}/*
# Don't ship zero-length files
%exclude %{python3_sitelib}/%{srcname}/alma/tests/data/empty.html
%exclude %{python3_sitelib}/%{srcname}/cosmosim/tests/test_cosmosim.py

%changelog
* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jun 15 2022 Python Maint <python-maint@redhat.com> - 0.4.5-3
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Sun Dec 26 2021 Christian dersch <lupinix@fedoraproject.org> - 0.4.5-1
- new version

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 0.4.1-4
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 20 2020 Christian Dersch <lupinix@fedoraproject.org> - 0.4.1-1
- new version

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.3.10-3
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Oct 20 2019 Christian Dersch <lupinix@fedoraproject.org> - 0.3.10-1
- new version

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.3.9-4
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.3.9-3
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Christian Dersch <lupinix@fedoraproject.org> - 0.3.9-1
- new version
- drop patch applied upstream

* Tue Oct 16 2018 Christian Dersch <lupinix.fedora@gmail.com> - 0.3.8-3
- remove python2 subpackage

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sun Jul 08 2018 Christian Dersch <lupinix@mailbox.org> - 0.3.8-1
- new version

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.3.7-2
- Rebuilt for Python 3.7

* Wed Feb 14 2018 Christian Dersch <lupinix@mailbox.org> - 0.3.7-1
- new version

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Jan 15 2018 Iryna Shcherbina <ishcherb@redhat.com> - 0.3.6-3
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Jul 05 2017 Christian Dersch <lupinix@mailbox.org> - 0.3.6-1
- new version
- temporary no license files (https://github.com/astropy/astroquery/issues/949)

* Mon Apr 03 2017 Christian Dersch <lupinix@mailbox.org> - 0.3.5-1
- new version

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 0.3.4-2
- Rebuild for Python 3.6

* Fri Dec 02 2016 Christian Dersch <lupinix@mailbox.org> - 0.3.4-1
- new version

* Wed Oct 12 2016 Christian Dersch <lupinix@mailbox.org> - 0.3.3-1
- new version

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.2-2
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Mon Jul 11 2016 Christian Dersch <lupinix@mailbox.org> - 0.3.2-1
- new version

* Wed Feb 03 2016 Christian Dersch <lupinix@mailbox.org> - 0.3.1-3
- Don't ship zero-length files
- Disabled -doc subpackage for now (doesn't build on rawhide yet)

* Fri Jan 22 2016 Christian Dersch <lupinix@mailbox.org> - 0.3.1-2
- Added doc subpackage
- Fix permissions

* Thu Jan 21 2016 Christian Dersch <lupinix@mailbox.org> - 0.3.1-1
- new version

* Sun Jan 03 2016 Christian Dersch <lupinix@mailbox.org> - 0.3.0-1
- Initial spec


