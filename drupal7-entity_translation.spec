%{?drupal7_find_provides_and_requires}

%global module entity_translation

Name:          drupal7-%{module}
Version:       1.1
Release:       8%{?pre_release:.%{pre_release}}%{?dist}
Summary:       Allows entities to be translated into different languages

License:       GPLv2+
URL:           https://drupal.org/project/%{module}
Source0:       https://ftp.drupal.org/files/projects/%{module}-7.x-%{version}%{?pre_release:-%{pre_release}}.tar.gz

BuildArch:     noarch
BuildRequires: drupal7-rpmbuild >= 7.70-2

# entity_translation.info
Requires:      drupal7(locale) > 7.14
# phpcompatinfo (computed from version 1.0)
Requires:      php-date
Requires:      php-pcre

%description
Allows (fieldable) entities to be translated into different languages,
by introducing entity/field translation for the new translatable fields
capability in Drupal 7. Maintained by the Drupal core i18n team.

This project does not replace the Internationalization
(http://drupal.org/project/i18n) project, which focuses on enabling a full
multilingual workflow for site admins/builders. Some features, e.g. content
language negotiation or taxonomy translation, might overlap but most of them
are unrelated.

This package provides the following Drupal modules:
* %{module}
* %{module}_i18n_menu (requires install of drupal7-i18n)
* %{module}_upgrade


%prep
%setup -qn %{module}

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
* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jun 05 2020 Shawn Iwinski <shawn.iwinski@gmail.com> - 1.1-3
- Bump build requires drupal7-rpmbuild to ">= 7.70-2" to fix F32+ auto provides

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Dec 15 2019 Shawn Iwinski <shawn.iwinski@gmail.com> - 1.1-1
- Update to 1.1 (RHBZ #1776035)
- Add .info files to repo

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu May 23 2019 Shawn Iwinski <shawn.iwinski@gmail.com> - 1.0-1
- Update to 1.0 (RHBZ #1558957)

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-0.16.beta7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-0.15.beta7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-0.14.beta7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sun Sep 10 2017 Shawn Iwinski <shawn.iwinski@gmail.com> - 1.0-0.13.beta7
- Updated to 1.0-beta7 (RHBZ #1483772)

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-0.12.beta6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Mar 10 2017 Shawn Iwinski <shawn.iwinski@gmail.com> - 1.0-0.11.beta6
- Updated to 1.0-beta6 (RHBZ #1428809)

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-0.10.beta5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Aug 04 2016 Shawn Iwinski <shawn.iwinski@gmail.com> - 1.0-0.9.beta5
- Updated to 1.0-beta5 (RHBZ #1335331)
- Minor spec cleanup

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-0.8.beta4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-0.7.beta4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Jan 27 2015 Shawn Iwinski <shawn.iwinski@gmail.com> - 1.0-0.6.beta4
- Updated to 1.0-beta4 (BZ #1185294)
- Moved RPM README inside spec
- %%license usage

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-0.5.beta3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu Aug 08 2013 Peter Borsa <peter.borsa@gmail.com> - 1.0-0.4.beta3
- Update to upstream 1.0-beta3 release for bug fixes
- Upstream changelog for this release is available at https://drupal.org/node/2048665

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-0.3.beta2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sun Jun 16 2013 Shawn Iwinski <shawn.iwinski@gmail.com> - 1.0-0.2.beta2
- Updated for drupal7-rpmbuild 7.22-5

* Fri May 03 2013 Shawn Iwinski <shawn.iwinski@gmail.com> - 1.0-0.1.beta2
- Initial package
