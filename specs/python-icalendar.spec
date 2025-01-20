Name:           python-icalendar
Version:        6.1.0
Release:        2%{?dist}
Summary:        Parser/generator of iCalendar files following the RFC 2445

License:        BSD-2-Clause
URL:            http://pypi.python.org/pypi/icalendar
Source0:        https://github.com/collective/icalendar/archive/v%{version}/%{version}.tar.gz

Patch0:         hatch.patch
Patch1:         tzdata.patch

BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-pytz
BuildRequires:  python3-dateutil
BuildRequires:  python3-hypothesis
BuildRequires:  python3-pytest

%global _description\
iCalendar specification (RFC 2445) defines calendaring format used\
by many applications (Zimbra, Thunderbird and others). This\
module is a parser/generator of iCalendar files for use with\
Python. It follows the RFC 2445 (iCalendar) specification.\
The aim is to make a package that is fully compliant with RFC 2445,\
well designed, simple to use and well documented.\


%description %_description

%package -n python3-icalendar
Summary:        Parser/generator of iCalendar files following the RFC 2445 for Python 3
Requires:       python3-pytz
Requires:       python3-dateutil

%description -n python3-icalendar
iCalendar specification (RFC 2445) defines calendaring format used\
by many applications (Zimbra, Thunderbird and others). This\
module is a parser/generator of iCalendar files for use with\
Python. It follows the RFC 2445 (iCalendar) specification.\
The aim is to make a package that is fully compliant with RFC 2445,\
well designed, simple to use and well documented.\

%prep
%setup -q -n icalendar-%{version}%{?veradd}

%patch -P 0 -p0
%patch -P 1 -p0

# we have only 2.7 and 3.3
sed -i 's/py26,//' tox.ini

rm -rf %{py3dir}
cp -a . %{py3dir}

%generate_buildrequires
%pyproject_buildrequires

%build
pushd %{py3dir}
%pyproject_wheel
popd

%install
pushd %{py3dir}
%pyproject_install
popd


%check
pushd %{py3dir}
%{__python3} -m pytest src/icalendar/tests
popd

%files -n python3-icalendar
%doc README.rst CHANGES.rst LICENSE.rst
%{python3_sitelib}/icalendar
%{python3_sitelib}/*.dist-info
%{_bindir}/icalendar

%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 6.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Nov 22 2024 Gwyn Ciesla <gwync@protonmail.com> - 6.1.0-1
- 6.1.0

* Mon Oct 14 2024 Gwyn Ciesla <gwync@protonmail.com> - 6.0.1-1
- 6.0.1

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.13-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 21 2024 Gwyn Ciesla <gwync@protonmail.com> - 5.0.13-1
- 5.0.13

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 5.0.12-2
- Rebuilt for Python 3.13

* Wed Mar 20 2024 Gwyn Ciesla <gwync@protonmail.com> - 5.0.12-1
- 5.0.12

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.11-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Nov 06 2023 Gwyn Ciesla <gwync@protonmail.com> - 5.0.11-1
- 5.0.11

* Thu Sep 28 2023 Gwyn Ciesla <gwync@protonmail.com> - 5.0.10-1
- 5.0.10

* Mon Sep 25 2023 Gwyn Ciesla <gwync@protonmail.com> - 5.0.9-1
- 5.0.9

* Tue Sep 19 2023 Gwyn Ciesla <gwync@protonmail.com> - 5.0.8-1
- 5.0.8

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jun 15 2023 Python Maint <python-maint@redhat.com> - 5.0.7-2
- Rebuilt for Python 3.12

* Tue May 30 2023 Gwyn Ciesla <gwync@protonmail.com> - 5.0.7-1
- 5.0.7

* Fri Apr 14 2023 Gwyn Ciesla <gwync@protonmail.com> - 5.0.5-1
- 5.0.5

* Wed Mar 08 2023 Gwyn Ciesla <gwync@protonmail.com> - 5.0.4-3
- migrated to SPDX license

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Jan 04 2023 Gwyn Ciesla <gwync@protonmail.com> - 5.0.4-1
- 5.0.4

* Mon Nov 28 2022 Gwyn Ciesla <gwync@protonmail.com> - 5.0.3-1
- 5.0.3

* Fri Nov 04 2022 Gwyn Ciesla <gwync@protonmail.com> - 5.0.2-1
- 5.0.2

* Wed Oct 26 2022 Gwyn Ciesla <gwync@protonmail.com> - 5.0.1-1
- 5.0.1

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.9-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 4.0.9-4
- Rebuilt for Python 3.11

* Wed Jan 26 2022 Gwyn Ciesla <gwync@protonmail.com> - 4.0.9-3
- Patch for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Mon Oct 18 2021 Gwyn Ciesla <gwync@protonmail.com> - 4.0.9-1
- 4.0.9

* Fri Oct 08 2021 Gwyn Ciesla <gwync@protonmail.com> - 4.0.8-1
- 4.0.8

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 4.0.7-3
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Sep 08 2020 Gwyn Ciesla <gwync@protonmail.com> - 4.0.7-1
- 4.0.7

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 4.0.6-2
- Rebuilt for Python 3.9

* Thu May 07 2020 Gwyn Ciesla <gwync@protonmail.com> - 4.0.6-1
- 4.0.6

* Sat Mar 21 2020 Gwyn Ciesla <gwync@protonmail.com> - 4.0.5-1
- 4.0.5

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Nov 25 2019 Gwyn Ciesla <gwync@protonmail.com> - 4.0.4-1
- 4.0.4

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 4.0.3-6
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 4.0.3-5
- Rebuilt for Python 3.8

* Tue Aug 13 2019 Gwyn Ciesla <gwync@protonmail.com> - 4.0.3-4
- Drop Python 2.

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Mar 06 2019 Yatin Karel <ykarel@redhat.com> - 4.0.3-2
- Drop unnecessary BR on python-pip
- Enable python3 build on RHEL > 7
- Include icalendar binary in py2 package when py3 disabled

* Thu Jan 31 2019 Gwyn Ciesla <limburgher@gmail.com> 4.0.3-1
- 4.0.3

* Wed Jul 25 2018 Gwyn Ciesla <limburgher@gmail.com> - 3.11.5-9
- Fix FTBFS.

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.11.5-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 3.11.5-7
- Rebuilt for Python 3.7

* Mon May 07 2018 Miro Hrončok <mhroncok@redhat.com> - 3.11.5-6
- Drop tox dependency, use pytest directly
- Use python2 instead of python

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.11.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 25 2018 Iryna Shcherbina <ishcherb@redhat.com> - 3.11.5-4
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Sat Aug 19 2017 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 3.11.5-3
- Python 2 binary package renamed to python2-icalendar
  See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.11.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jul 17 2017 Haïkel Guémar <hguemar@fedoraproject.org> - 3.11.5-1
- Upstream 3.11.5 (multiple bugfixes)

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.11-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 3.11-2
- Rebuild for Python 3.6

* Fri Dec 09 2016 Jon Ciesla <limburgher@gmail.com> - 3.11-1
- 3.11

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.9.0-5
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3.9.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.9.0-3
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.9.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Mar 28 2015 Jon Ciesla <limburgher@gmail.com> - 3.9.0-1
- Latest upstream, BZ 1206758.

* Tue Jan 20 2015 Jon Ciesla <limburgher@gmail.com> - 3.8.4-1
- Latest upstream.

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.6.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed May 14 2014 Bohuslav Kabrda <bkabrda@redhat.com> - 3.6.2-2
- Rebuilt for https://fedoraproject.org/wiki/Changes/Python_3.4

* Thu Apr 24 2014 Jon Ciesla <limburgher@gmail.com> - 3.6.2-1
- Latest upstream.

* Tue Jan 07 2014 Stanislav Ochotnicky <sochotnicky@rdhat.com> - 3.6.1-1
- Update to latest upstream
- Add python3 subpackage

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu May 30 2013 Stanislav Ochotnicky <sochotnicky@redhat.com> - 3.4-2
- Install LICENSE file as well

* Thu May 30 2013 Stanislav Ochotnicky <sochotnicky@redhat.com> - 3.4-1
- Update to latest upstream version (#824323)

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0.1-0.3.b2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0.1-0.2.b2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed May 30 2012 Stanislav Ochotnicky <sochotnicky@redhat.com> - 3.0.1-0.1.b2
- Update to 3.0b2
- Change license to BSD (see https://github.com/collective/icalendar/issues/2)

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Aug  5 2010 Stanislav Ochotnicky <sochotnicky@redhat.com> - 2.1-3
- Install examples
- Fix tests for Python 2.7 and run them
- Add GPLv2 for parser.py to licenses

* Wed Aug  4 2010 Stanislav Ochotnicky <sochotnicky@redhat.com> - 2.1-2
- State correct licenses

* Tue Aug  3 2010 Stanislav Ochotnicky <sochotnicky@redhat.com> - 2.1-1
- Initial package version
