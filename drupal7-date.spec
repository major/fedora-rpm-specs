%{?drupal7_find_provides_and_requires}

%global module date

Name:          drupal7-%{module}
Version:       2.10
Release:       13%{?dist}
Summary:       Makes date/time fields available


# Licenses:
# - GPLv2+
#     - Drupal date module itself
# - MIT
#     - date/date_popup/jquery.timeentry.pack.js
License:       GPLv2+ and MIT

URL:           http://drupal.org/project/%{module}
Source0:       http://ftp.drupal.org/files/projects/%{module}-7.x-%{version}%{?pre_release:-%{pre_release}}.tar.gz

BuildArch:     noarch
BuildRequires: drupal7-rpmbuild >= 7.70-2

# phpcompatinfo (computed from version 2.10)
Requires:      php-date
Requires:      php-pcre

# Bundled
## date_popup/jquery.timeentry.pack.js
###     License: MIT
###     Upstream: https://github.com/kbwood/timeentry
Provides:      bundled(js-jquery-timeentry) = 1.5.2
Provides:      bundled(js-timeentry) = 1.5.2


%description
This package contains both a flexible date/time field type Date field and a
Date API that other modules can use.

The D5 and D6 versions of the Date field require the Content Construction Kit
(CCK) module [1]. The D7 version works with the core Field functionality.
D8 includes Date in core.

The Drupal Handbook pages are at Date/Calendar Documentation [2].

This package provides the following Drupal 7 modules:
* %{module}
* %{module}_all_day
* %{module}_api
* %{module}_context
* %{module}_migrate_example
* %{module}_popup
* %{module}_repeat
* %{module}_repeat_field
* %{module}_tools
* %{module}_views

[1] http://drupal.org/project/cck
[2] http://drupal.org/node/262062


%prep
%setup -qn %{module}

: Licenses and docs
mkdir -p .rpm/{licenses,docs}
mv LICENSE.txt .rpm/licenses/
mv *.txt .rpm/docs/
mkdir .rpm/docs/{date_all_day,date_popup,date_repeat_field,tests}
mv date_all_day/*.txt .rpm/docs/date_all_day/
mv date_popup/*.txt .rpm/docs/date_popup/
mv date_repeat_field/*.txt .rpm/docs/date_repeat_field/
mv tests/*.txt .rpm/docs/tests/


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
* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.10-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.10-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.10-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.10-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.10-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jun 05 2020 Shawn Iwinski <shawn.iwinski@gmail.com> - 2.10-8
- Bump build requires drupal7-rpmbuild to ">= 7.70-2" to fix F32+ auto provides

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.10-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.10-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.10-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.10-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.10-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Apr 08 2017 Shawn Iwinski <shawn.iwinski@gmail.com> - 2.10-1
- Updated to 2.10 (RHBZ #1437043)

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.10-0.2.rc1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Aug 04 2016 Shawn Iwinski <shawn.iwinski@gmail.com> - 2.10-0.1.rc1
- Updated to 2.10-rc1 (RHBZ #1327689)
- License updated from "GPLv2+" to "GPLv2+ and MIT" because of bundled lib
- Spec cleanup

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sun Sep 20 2015 Jared Smith <jsmith@fedoraproject.org> - 2.9-1
- Update to upstream 2.9 release
- Upstream changelog at https://www.drupal.org/node/2565073

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Jul 31 2014 Jared Smith <jsmith@fedoraproject.org> 2.8-1
- Update to upstream 2.8 release
- This release fixes an XSS issue, CVE-2014-5169

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Jan 10 2014 Peter Borsa <peter.borsa@gmail.com> 2.7-1
- Update to upstream 2.7 release for bug fixes
- Upstream changelog for this release is available at https://drupal.org/node/2161141

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.6-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Oct 27 2012 Jared Smith <jsmith@fedoraproject.org> - 2.6-3
- Update to upstream release 2.6
- Upstream changelog at http://drupal.org/node/1727916

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Apr 19 2012 Jared Smith <jsmith@fedoraproject.org> - 2.5-1
- Update to upstream release 2.5

* Mon Apr 02 2012 Jared Smith <jsmith@fedoraproject.org> - 2.3-1
- Update to upstream release 2.3

* Mon Feb 27 2012 Jared Smith <jsmith@fedoraproject.org> - 2.2-1
- Update to upstream release 2.2

* Thu Feb 23 2012 Jared Smith <jsmith@fedoraproject.org> - 2.1-3
- Accidentally removed the %%{dist} from the release number

* Thu Feb 23 2012 Jared Smith <jsmith@fedoraproject.org> - 2.1-2
- Bump release number to fix a small typo

* Wed Feb 22 2012 Jared Smith <jsmith@fedoraproject.org> - 2.1-1
- Update to upstream 2.1 release

* Sat Feb 04 2012 Jared Smith <jsmith@fedoraproject.org> - 2.0-0.1.rc2
- Update to rc2

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0-0.2.rc1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Dec 21 2011 Jared Smith <jsmith@fedoraproject.org> - 2.0-0.1.rc1
- Update to rc1
- Convert CHANGELOG.txt to UTF-8

* Sun Sep 11 2011 Jared Smith <jsmith@fedoraproject.org> - 2.0-0.1.alpha4
- Update to alpha4
- Update FSF address in LICENSE.txt

* Sat Jul 30 2011 Jared Smith <jsmith@fedoraproject.org> - 2.0-0.1.alpha3
- Initial version for Drupal 7
