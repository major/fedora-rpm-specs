%global drupaldir %{_datadir}/drupal7

Name:    drupal7-calendar
Version: 3.5
Release: 16%{?dist}
Summary: This module will display any Views date field in calendar formats

License: GPLv2+
URL:     http://drupal.org/project/calendar
Source0: http://ftp.drupal.org/files/projects/calendar-7.x-%{version}.tar.gz
Source1: %{name}-fedora-README.txt
Source2: LICENSE.txt

BuildArch: noarch
Requires:  drupal7
Requires:  drupal7-date >= 2.0-0.1.alpha4
Requires:  drupal7-views >= 3.0-0.1.rc1

%description
This module will display any Views date field in calendar formats,
including CCK date fields, Event module event fields, node created or
updated dates, etc. Switch between year, month, and day views. Back and
next navigation is provided for all views.

%prep

%setup -qn calendar

install -p -m 0644 %{SOURCE1} .
install -p -m 0644 %{SOURCE2} .

%build

%install
rm -rf %{buildroot}
install -d %{buildroot}%{drupaldir}/modules/calendar
cp -pr * %{buildroot}%{drupaldir}/modules/calendar

%files
%doc CHANGELOG.txt LICENSE.txt README.txt %{name}-fedora-README.txt
%{drupaldir}/modules/calendar
%exclude %{drupaldir}/modules/calendar/*.txt

%changelog
* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.5-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.5-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.5-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.5-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.5-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.5-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.5-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.5-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.5-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.5-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.5-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Jan 26 2016 Jared Smith <jsmith@fedoraproject.org> - 3.5-3
- Remove call to %%defattr macro, as it is no longer needed

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Oct 17 2014 Jared Smith <jsmith@fedoraproject.org> - 3.5-1
- New upstream release.  See release notes at https://www.drupal.org/node/2356415

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat May 19 2012 Peter Borsa <peter.borsa@gmail.com> - 3.4-1
- New upstream version.

* Mon Apr 30 2012 Peter Borsa <peter.borsa@gmail.com> - 3.3-1
- New upstream version.

* Sat Apr 21 2012 Peter Borsa <peter.borsa@gmail.com> - 3.2-1
- New upstream version.

* Wed Feb 29 2012 Peter Borsa <peter.borsa@gmail.com> - 3.0-1
- New upstream version.

* Thu Feb 16 2012 Peter Borsa <peter.borsa@gmail.com> - 3.0-0.4.rc1
- Fixed release number

* Thu Feb 16 2012 Peter Borsa <peter.borsa@gmail.com> - 3.0-0.1.rc1
- New upstream version.

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0-0.3.alpha2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Jan  3 2012 Peter Borsa <peter.borsa@gmail.com> - 3.0-0.2.alpha2
- New upstream version.

* Tue Oct 18 2011 Peter Borsa <peter.borsa@gmail.com> - 3.0-0.1.alpha1
- Initial packaging.
