%{?drupal7_find_provides_and_requires}

%global module addressfield

Name:          drupal7-%{module}
Version:       1.2
Release:       16%{?dist}
Summary:       Manage a flexible address field, implementing the xNAL standard

License:       GPLv2+
URL:           http://drupal.org/project/%{module}
Source0:       http://ftp.drupal.org/files/projects/%{module}-7.x-%{version}.tar.gz

BuildArch:     noarch
BuildRequires: drupal7-rpmbuild >= 7.70-2

# addressfield.info
Requires:      drupal7(ctools)
# phpcompatinfo (computed from version 1.2)
# <none>

%description
Address Field defines a new field type to store international postal
addresses, implementing a subset of the top-level address elements
defined in the xNAL standard [1].

The field configuration lets you determine which elements of an address
should be present in the field widget form and which ones should be
rendered for display.

This package provides the following Drupal module:
* %{module}

[1] http://xml.coverpages.org/xnal.html


%prep
%setup -qn %{module}


%build
# Emtpy build section, nothing to build


%install
mkdir -p %{buildroot}%{drupal7_modules}/%{module}
cp -pr * %{buildroot}%{drupal7_modules}/%{module}/


%files
%{?_licensedir:%license LICENSE.txt}
%{drupal7_modules}/%{module}


%changelog
* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jun 05 2020 Shawn Iwinski <shawn.iwinski@gmail.com> - 1.2-11
- Bump build requires drupal7-rpmbuild to ">= 7.70-2" to fix F32+ auto provides

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sat Oct 10 2015 Shawn Iwinski <shawn.iwinski@gmail.com> - 1.2-2
- Add drupal7(ctools) dependency

* Sat Oct 10 2015 Shawn Iwinski <shawn.iwinski@gmail.com> - 1.2-1
- Updated to 1.2 (RHBZ #1270071)

* Mon Jul 06 2015 Shawn Iwinski <shawn.iwinski@gmail.com> - 1.1-1
- Updated to 1.1 (RHBZ #1219735)

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-0.4.rc1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Dec 22 2014 Shawn Iwinski <shawn.iwinski@gmail.com> - 1.0-0.3.rc1
- Updated to 1.0-rc1 (BZ #1175145)
- Removed RPM README b/c it only explained common Drupal workflow
- %%license usage

* Fri Jun 27 2014 Sam Wilson <sam.wilson@nextdc.com> - 1.0-0.2.beta5
- Updated to incorporate packaging guidance

* Tue May 20 2014 Sam Wilson <sam.wilson@nextdc.com> - 1.0-0.1.beta5
- Initial Package (release notes https://drupal.org/node/2151159)
