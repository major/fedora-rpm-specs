%{?drupal7_find_provides_and_requires}

%global module webform

Name:          drupal7-%{module}
Version:       4.22
Release:       7%{?pre_release:.%{pre_release}}%{?dist}
Summary:       Enables the creation of forms and questionnaires

License:       GPLv2+
URL:           https://drupal.org/project/%{module}
Source0:       https://ftp.drupal.org/files/projects/%{module}-7.x-%{version}%{?pre_release:-%{pre_release}}.tar.gz

BuildArch:     noarch
BuildRequires: drupal7-rpmbuild >= 7.70-2

# webform.info
Requires:      drupal7(ctools)
Requires:      drupal7(views)
# phpcompatinfo (computed from version 4.22)
Requires:      php-date
Requires:      php-filter
Requires:      php-mbstring
Requires:      php-pcre
Requires:      php-session
Requires:      php-zip


%description
Webform is the module for making forms and surveys in Drupal. After a
submission, users may be sent an e-mail "receipt" as well as sending a
notification to administrators. Results can be exported into Excel or
other spreadsheet applications. Webform also provides some basic statistical
review and has an extensive API for expanding its features.

Some good examples could be contests, personalized contact forms, or petitions.
Each of these could have a customized form for end-users to fill out. If you
need to build a lot of customized, one-off forms, Webform is a more suitable
solution than creating content types and using CCK or Field module. Explanation
of Webform vs. CCK (or Fields) [1].

This package provides the following Drupal 7 module:
* %{module}

[1] http://drupal.org/documentation/modules/webform#webform-vs-cck


%prep
%setup -qn %{module}

: Licenses and docs
mkdir -p .rpm/{licenses,docs}
mv LICENSE.txt .rpm/licenses/
mv *.md .rpm/docs/


%build
# Empty build section, nothing to build


%install
mkdir -p %{buildroot}%{drupal7_modules}/%{module}
cp -pr * %{buildroot}%{drupal7_modules}/%{module}/


%files
%{!?_licensedir:%global license %%doc}
%license .rpm/licenses/*
%doc .rpm/docs/*
%{drupal7_modules}/%{module}


%changelog
* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.22-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.22-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.22-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.22-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.22-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jun 05 2020 Shawn Iwinski <shawn.iwinski@gmail.com> - 4.22-2
- Bump build requires drupal7-rpmbuild to ">= 7.70-2" to fix F32+ auto provides

* Sun Apr 05 2020 Shawn Iwinski <shawn.iwinski@gmail.com> - 4.22-1
- Update to 4.22 (RHBZ #1796964)

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.21-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Dec 15 2019 Shawn Iwinski <shawn.iwinski@gmail.com> - 4.21-1
- Update to 4.21 (RHBZ #1742293, SA-CONTRIB-2019-096)
- https://www.drupal.org/sa-contrib-2019-096
- Add .info file to repo

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.19-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 24 2019 Shawn Iwinski <shawn.iwinski@gmail.com> - 4.19-1
- Updated to 4.19 (RHBZ #1503365)

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.16-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.16-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sun Apr 01 2018 Shawn Iwinski <shawn.iwinski@gmail.com> - 4.16-1
- Update to 4.16 (RHBZ #1503365)

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.16-0.2.rc1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Sep 18 2017 Shawn Iwinski <shawn.iwinski@gmail.com> - 4.16-0.1.rc1
- Updated to 4.16-rc1 (RHBZ #1492251)

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.15-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Apr 14 2017 Shawn Iwinski <shawn.iwinski@gmail.com> - 4.15-1
- Updated to 4.15 (RHBZ #1442289)

* Sat Apr 08 2017 Shawn Iwinski <shawn.iwinski@gmail.com> - 4.15-0.1.rc1
- Updated to 4.15-rc1 (RHBZ #1437695)

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.14-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun Sep 11 2016 Shawn Iwinski <shawn.iwinski@gmail.com> - 4.14-1
- Updated to 4.14 (RHBZ #1371127)

* Sun Aug 07 2016 Shawn Iwinski <shawn.iwinski@gmail.com> - 4.13-1
- Updated to 4.13 (RHBZ #1359428)

* Wed Jul 20 2016 Shawn Iwinski <shawn.iwinski@gmail.com> - 4.12-2
- Spec cleanup
- %%license usage

* Fri May 06 2016 Peter Borsa <peter.borsa@gmail.com> 4.12-1
- Update to 4.12
- Release notes can be found at https://www.drupal.org/node/2599998

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 4.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sun Jul 19 2015 Peter Borsa <peter.borsa@gmail.com> 4.10-1
- Update to 4.10
- Release notes can be found at https://www.drupal.org/node/2534752

* Wed Jul 01 2015 Peter Borsa <peter.borsa@gmail.com> 4.9-1
- Update to 4.9
- Release notes can be found at https://www.drupal.org/node/2495339

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Apr 30 2015 Peter Borsa <peter.borsa@gmail.com> 4.8-1
- Update to 4.8
- Release notes can be found at https://www.drupal.org/node/2480415

* Sun Mar 29 2015 Peter Borsa <peter.borsa@gmail.com> 4.7-1
- Update to 4.7
- Release notes can be found at https://www.drupal.org/node/2460229

* Mon Mar 23 2015 Peter Borsa <peter.borsa@gmail.com> 4.6-1
- Update to 4.6
- Release notes can be found at https://www.drupal.org/node/2457219

* Fri Mar 20 2015 Peter Borsa <peter.borsa@gmail.com> 4.5-1
- Update to 4.5
- Release notes can be found at https://www.drupal.org/node/2454063

* Fri Feb 20 2015 Peter Borsa <peter.borsa@gmail.com> 4.3-1
- Update to 4.3
- Release notes can be found at https://www.drupal.org/node/2427257

* Tue Dec 23 2014 Peter Borsa <peter.borsa@gmail.com> 4.2-1
- Update to 4.2
- Release notes can be found at https://www.drupal.org/node/2381793

* Tue Nov 25 2014 Peter Borsa <peter.borsa@gmail.com> 4.1-1
- Update to 4.1
- Release notes can be found at https://www.drupal.org/node/2351973

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.0-0.3.beta3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Mar 14 2014 Peter Borsa <peter.borsa@gmail.com> 4.0-0.2.beta3
- Update to 4.0-beta3
- Release notes can be found at https://drupal.org/node/2196069

* Fri Feb 28 2014 Peter Borsa <peter.borsa@gmail.com> 4.0-0.2.beta1
- Remove php-pecl(zip) dependency

* Sat Jan 11 2014 Peter Borsa <peter.borsa@gmail.com> 4.0-0.1.beta1
- Initial package
