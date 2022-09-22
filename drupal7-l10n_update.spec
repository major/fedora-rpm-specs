%{?drupal7_find_provides_and_requires}

%global module l10n_update

Name:          drupal7-%{module}
Version:       2.3
Release:       8%{?pre_release:.%{pre_release}}%{?dist}
Summary:       Provides automatic downloads and updates for translations

License:       GPLv2+
URL:           https://drupal.org/project/%{module}
Source0:       https://ftp.drupal.org/files/projects/%{module}-7.x-%{version}%{?pre_release:-%{pre_release}}.tar.gz

BuildArch:     noarch
BuildRequires: drupal7-rpmbuild >= 7.70-2

# l10n_update.info
Requires:      drupal7(locale)
# phpcompatinfo (computed from version 2.3)
Requires:      php-date
Requires:      php-pcre

%description
Automatically download and update your translations fetching them from
localize.drupal.org [1] or any other localization server [2].

This package provides the following Drupal module:
* %{module}

[1] http://localize.drupal.org/
[2] http://drupal.org/project/l10n_server


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
* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jun 05 2020 Shawn Iwinski <shawn.iwinski@gmail.com> - 2.3-3
- Bump build requires drupal7-rpmbuild to ">= 7.70-2" to fix F32+ auto provides

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Dec 15 2019 Shawn Iwinski <shawn.iwinski@gmail.com> - 2.3-1
- Updated to 2.3 (RHBZ #1757939, SA-CONTRIB-2019-072)
- https://www.drupal.org/sa-contrib-2019-072
- Add .info file to repo

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Sep 18 2017 Shawn Iwinski <shawn.iwinski@gmail.com> - 2.2-1
- Updated to 2.2 (RHBZ #1492654)

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Dec 15 2016 Shawn Iwinski <shawn.iwinski@gmail.com> - 2.1-1
- Updated to 2.1 (RHBZ #1401189)
- Removed unneeded %%defattr(-,root,root,-)

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Apr 04 2015 Shawn Iwinski <shawn.iwinski@gmail.com> - 2.0-1
- Updated to 2.0 (BZ #1198580)

* Wed Nov 12 2014 Shawn Iwinski <shawn.iwinski@gmail.com> - 1.1-1
- Updated to 1.1 (BZ #1163121)
- Removed RPM README b/c it only explained common Drupal workflow
- %%license usage

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun May 11 2014 Peter Borsa <peter.borsa@gmail.com> - 1.0-1
- Update to upstream 1.0 release for bug fixes
- Upstream changelog for this release is available at https://drupal.org/node/2239135

* Thu Mar 06 2014 Shawn Iwinski <shawn.iwinski@gmail.com> - 1.0-0.4.rc1
- Updated to 1.0-rc1 (BZ #1070105; release notes https://drupal.org/node/2204871)

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-0.3.beta3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sun Jun 16 2013 Shawn Iwinski <shawn.iwinski@gmail.com> - 1.0-0.2.beta3
- Updated for drupal7-rpmbuild 7.22-5

* Fri May 03 2013 Shawn Iwinski <shawn.iwinski@gmail.com> - 1.0-0.1.beta3
- Initial package
