%global srcname pyrad

Name:           python-pyrad
Version:        2.4
Release:        3%{?dist}
Summary:        Python RADIUS client
License:        BSD
URL:            https://github.com/wichert/pyrad
Source0:        %{url}/archive/%{version}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch

%description
pyrad is an implementation of a RADIUS client as described in RFC2865. It takes
care of all the details like building RADIUS packets, sending them and decoding
responses.

%package -n python3-%{srcname}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{srcname}}
BuildRequires:  python3-devel
BuildRequires:  python3-netaddr
BuildRequires:  python3-setuptools
BuildRequires:  python3-six
BuildRequires:  python3-sphinx
Requires:       python3-netaddr
Requires:       python3-six
Requires:       python3-twisted

%description -n python3-%{srcname}
pyrad is an implementation of a RADIUS client as described in RFC2865. It takes
care of all the details like building RADIUS packets, sending them and decoding
responses.

%prep
%autosetup -n %{srcname}-%{version} -p1
# Fedora-specific - to avoid picking up dependencies from these files
chmod 644 example/acct.py example/auth.py example/server.py

%build
%py3_build

sphinx-build-3 -b html docs/source docs/_build/html/ -d docs/_build/doctrees/

%install
%py3_install
rm -f docs/_build/html/.buildinfo

%check
%{__python3} -m unittest -v

%files -n python3-%{srcname}
%license LICENSE.txt
%doc CHANGES.rst README.rst example/ docs/_build/html/
%{python3_sitelib}/%{srcname}-*.egg-info/
%{python3_sitelib}/%{srcname}/

%changelog
* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 2.4-2
- Rebuilt for Python 3.11

* Wed May 18 2022 Antonio Torres <antorres@redhat.com> - 2.4-1
- Update to upstream release 2.4

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 2.1-10
- Rebuilt for Python 3.10

* Wed Feb 10 2021 Charalampos Stratakis <cstratak@redhat.com> - 2.1-9
- Switch the test run from nose to stdlib unittest

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 2.1-6
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 2.1-4
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 2.1-3
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Mar 29 2019 Peter Lemenkov <lemenkov@gmail.com> - 2.1-1
- Ver. 2.1

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-18.git1ca2da3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Oct 02 2018 Peter Lemenkov <lemenkov@gmail.com> - 2.0-17.git1ca2da3
- Remove python2 subpackage

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-16.git1ca2da3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Jul 11 2018 Peter Lemenkov <lemenkov@gmail.com> - 2.0-15.git1ca2da3
- Fix FTBFS on F-28 and higher

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 2.0-14.git1ca2da3
- Rebuilt for Python 3.7

* Mon Mar 26 2018 Iryna Shcherbina <ishcherb@redhat.com> - 2.0-13.git1ca2da3
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-12.git1ca2da3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-11.git1ca2da3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-10.git1ca2da3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 2.0-9.git1ca2da3
- Rebuild for Python 3.6

* Wed Aug 31 2016 Peter Lemenkov <lemenkov@gmail.com> - 2.0-8.git1ca2da3
- Rebase to the latest git commit

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0-7
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu Sep 05 2013 Peter Lemenkov <lemenkov@gmail.com> - 2.0-3
- Better random number generator

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Jul 11 2013 Christopher Meng <rpm@cicku.me> - 2.0-1
- Update to 2.0 version.

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Sep  6 2010 Peter Lemenkov <lemenkov@gmail.com> - 1.1-5
- Cleaned up spec-file
- Added %%check section
- Dropped support for fedora > 9

* Thu Jul 22 2010 David Malcolm <dmalcolm@redhat.com> - 1.1-4
- Rebuilt for https://fedoraproject.org/wiki/Features/Python_2.7/MassRebuild

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Sat Apr 11 2009 Peter Lemenkov <lemenkov@gmail.com> - 1.1-2
- Fixed rpmling warning
- Changed 'files' section
- Added missing requires python-twisted-core

* Sat Apr 11 2009 Peter Lemenkov <lemenkov@gmail.com> - 1.1-1
- Initial build

