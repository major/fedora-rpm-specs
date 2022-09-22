%{?drupal7_find_provides_and_requires}

%global module entity

Name:          drupal7-%{module}
Version:       1.9
Release:       9%{?dist}
Summary:       Extends the entity API to provide a unified way to deal with entities

License:       GPLv2+
URL:           http://drupal.org/project/%{module}
Source0:       http://ftp.drupal.org/files/projects/%{module}-7.x-%{version}.tar.gz

BuildArch:     noarch
BuildRequires: drupal7-rpmbuild >= 7.70-2

# phpcompatinfo (computed from version 1.9)
Requires:      php-date
Requires:      php-pcre
Requires:      php-spl

%description
This module extends the entity API of Drupal core in order to provide a unified
way to deal with entities and their properties. Additionally, it provides an
entity CRUD controller, which helps simplifying the creation of new entity
types.

This package provides the following Drupal modules:
* %{module}
* %{module}_token


%prep
%setup -q -n %{module}

: Licenses and docs
mkdir -p .rpm/{licenses,docs}
mv LICENSE.txt .rpm/licenses/
mv *.txt .rpm/docs/


%build
# Empty build section, nothing to build


%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{drupal7_modules}/%{module}
cp -pr * %{buildroot}%{drupal7_modules}/%{module}/



%files
%{!?_licensedir:%global license %%doc}
%license .rpm/licenses/*
%doc .rpm/docs/*
%{drupal7_modules}/%{module}


%changelog
* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.9-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.9-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.9-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.9-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.9-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jun 05 2020 Shawn Iwinski <shawn.iwinski@gmail.com> - 1.9-4
- Bump build requires drupal7-rpmbuild to ">= 7.70-2" to fix F32+ auto provides

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.9-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun May 19 2019 Shawn Iwinski <shawn.iwinski@gmail.com> - 1.9-1
- Update to 1.9 (RHBZ #1545456)
- https://www.drupal.org/project/entity/releases/7.x-1.9
- https://www.drupal.org/sa-contrib-2018-013

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.8-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.8-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.8-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun Sep 25 2016 Shawn Iwinski <shawn.iwinski@gmail.com> - 1.8-1
- Updated to 1.8 (RHBZ #1378632)

* Sun Jul 31 2016 Shawn Iwinski <shawn.iwinski@gmail.com> - 1.7-1
- Updated to 1.7 (RHBZ #1318827)

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Feb 27 2015 Shawn Iwinski <shawn.iwinski@gmail.com> - 1.6-1
- Updated to 1.6 (BZ #1196750 / SA-CONTRIB-2015-053)
- Removed RPM README b/c it only explained common Drupal workflow
- %%license usage

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat May 10 2014 Peter Borsa <peter.borsa@gmail.com> - 1.5-1
- Update to upstream 1.5 release for bug fixes
- Upstream changelog for this release is available at https://drupal.org/node/2236077

* Thu Jan 09 2014 Shawn Iwinski <shawn.iwinski@gmail.com> - 1.3-2
- Added provided modules to description

* Thu Jan 09 2014 Shawn Iwinski <shawn.iwinski@gmail.com> - 1.3-1
- Updated to 1.3 (release notes: https://drupal.org/node/2169589) (BZ #1050853)
- CVE-2014-1398, CVE-2014-1399, CVE-2014-1400 (BZ #1050802, 1050803, 1050804)
- SA-CONTRIB-2014-001 (https://drupal.org/node/2169595)
- Spec cleanup

* Fri Aug 16 2013 Peter Borsa <peter.borsa@gmail.com> - 1.2-1
- Update to upstream 1.2 release for security and bug fixes
- Upstream changelog for this release is available at https://drupal.org/node/2065197
- SA-CONTRIB-2013-068 https://drupal.org/node/2065207

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Jun 12 2013 Peter Borsa <peter.borsa@gmail.com> - 1.1-1
- Update to upstream 1.1 release for bug fixes
- Upstream changelog for this release is avalble at https://drupal.org/node/1983440

* Sun Mar 17 2013 Peter Borsa <peter.borsa@gmail.com> - 1.0-1
- Update to 1.0
- Fix BZ 919025

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-0.6.rc3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-0.5.rc3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Jun 19 2012 Scott Dodson <sdodson@redhat.com> - 1.0-0.4.rc3
- Update to 1.0-rc3

* Wed Apr 25 2012 Scott Dodson <sdodson@redhat.com> - 1.0-0.4.rc2
- Update to 1.0-rc2

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-0.4.rc1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Dec 20 2011 Scott Dodson <sdodson@redhat.com> - 1.0-0.3.rc1
- Update to 1.0-rc1

* Fri Oct 28 2011 Scott Dodson <sdodson@redhat.com> - 1.0-0.2.beta11
- Fix description
- Update to beta11

* Wed Aug 31 2011 Scott Dodson <sdodson@redhat.com> - 1.0-0.1.beta10
- Initial Packaging
