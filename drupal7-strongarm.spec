%global drupaldir %{_datadir}/drupal7

Name:    drupal7-strongarm
Version: 2.0
Release: 18%{?dist}
Summary: Strongarm gives a way to override the default variable values

License: GPLv2+
URL:     http://drupal.org/project/strongarm
Source0: http://ftp.drupal.org/files/projects/strongarm-7.x-%{version}.tar.gz
Source1: %{name}-fedora-README.txt
Source2: LICENSE.txt

BuildArch: noarch
Requires:  drupal7
Requires:  drupal7-ctools >= 1.0-0.1.alpha4

%description
Strongarm gives site builders a way to override the default variable values
that Drupal core and contributed modules ship with. It is not an end user tool,
but a developer and site builder tool which provides an API and a limited UI.

%prep

%setup -qn strongarm

install -p -m 0644 %{SOURCE1} .
install -p -m 0644 %{SOURCE2} .

%build

%install
rm -rf %{buildroot}
install -d %{buildroot}%{drupaldir}/modules/strongarm
cp -pr * %{buildroot}%{drupaldir}/modules/strongarm

# Symlink README.txt for UI help
rm -f %{buildroot}%{drupaldir}/modules/strongarm/README.txt
%if 0%{?fedora} >= 20
# Non-versioned doc dir
ln -s %{_docdir}/%{name}/README.txt \
      %{buildroot}%{drupaldir}/modules/strongarm/README.txt
%else
# Versioned doc dir
ln -s %{_docdir}/%{name}-%{version}/README.txt \
      %{buildroot}%{drupaldir}/modules/strongarm/README.txt
%endif

%files
%doc LICENSE.txt README.txt %{name}-fedora-README.txt
%{drupaldir}/modules/strongarm
%exclude %{drupaldir}/modules/strongarm/LICENSE.txt
%exclude %{drupaldir}/modules/strongarm/drupal7-strongarm-fedora-README.txt

%changelog
* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu Nov 14 2013 Shawn Iwinski <shawn.iwinski@gmail.com> - 2.0-3
- Superfluous commit to make Bodhi happy

* Thu Nov 14 2013 Shawn Iwinski <shawn.iwinski@gmail.com> - 2.0-2
- Fixed non-versioned versus versioned doc dir issue

* Fri Nov 08 2013 Peter Borsa <peter.borsa@gmail.com> - 2.0-1
- Update to upstream 2.0 release for bug fixes
- Upstream changelog for this release: https://drupal.org/node/1632574

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0-0.8.rc1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sat May 25 2013 Shawn Iwinski <shawn.iwinski@gmail.com> - 2.0-0.7.rc1
- README.txt in module directory for UI help (BZ 966933)

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0-0.6.rc1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0-0.5.rc1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed Mar 28 2012 Peter Borsa <peter.borsa@gmail.com> - 2.0-0.4.rc1
- New upstream version.

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0-0.3.beta5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Thu Dec 29 2011 Peter Borsa <peter.borsa@gmail.com> - 2.0-0.2.beta5
- New upstream version.

* Fri Sep 23 2011 Peter Borsa <peter.borsa@gmail.com> - 2.0-0.1.beta3
- Initial packaging

