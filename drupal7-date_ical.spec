%{?drupal7_find_provides_and_requires}

%global module date_ical

Name:          drupal7-%{module}
Version:       3.9
Release:       14%{?dist}
Summary:       Enables import/export of iCal feeds

License:       GPLv2+
URL:           http://drupal.org/project/%{module}
Source0:       http://ftp.drupal.org/files/projects/%{module}-7.x-%{version}.tar.gz

BuildArch:     noarch
BuildRequires: drupal7-rpmbuild >= 7.70-2

# date_ical.info
# Since Drupal 7 itself only requires PHP >= 5.2.4, we must must specify greater PHP min ver
Requires:      php(language) >= 5.3.0
Requires:      drupal7(date_api)
Requires:      drupal7(date_views)
Requires:      drupal7(date)
Requires:      drupal7(entity)
Requires:      drupal7(libraries) >= 2.0
Requires:      drupal7(views) >= 3.5
# date_ical.info: optional
Requires:      drupal7(feeds)
# phpcompatinfo (computed from version 3.5)
Requires:      php-date
Requires:      php-json
Requires:      php-pcre

%description
Date iCal is your one-stop shop for iCal support in Drupal. It provides a
plugin for Views to enable exporting your site's calendar as an iCal feed,
and a plugin for Feeds to enable importing external iCal feeds into your
site's calendar.

Any entity which contains a Date field can be utilized by Date iCal for import
and export of iCal feeds.

This package provides the following Drupal module:
* %{module}


%prep
%setup -qn %{module}

: Licenses and docs
mkdir -p .rpm/{licenses,docs}
mv LICENSE.txt .rpm/licenses/
# Docs used at runtime
#mv *.txt .rpm/docs/


%build
# Empty build section, nothing to build


%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{drupal7_modules}/%{module}
cp -pr * %{buildroot}%{drupal7_modules}/%{module}/



%files
%{!?_licensedir:%global license %%doc}
%license .rpm/licenses/*
# Docs used at runtime
#%%doc .rpm/docs/*
%{drupal7_modules}/%{module}


%changelog
* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.9-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.9-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.9-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.9-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.9-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jun 05 2020 Shawn Iwinski <shawn.iwinski@gmail.com> - 3.9-9
- Bump build requires drupal7-rpmbuild to ">= 7.70-2" to fix F32+ auto provides

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.9-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.9-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.9-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.9-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.9-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.9-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Aug 04 2016 Shawn Iwinski <shawn.iwinski@gmail.com> - 3.9-1
- Updated to 3.9 (RHBZ #1282646)
- Minor spec cleanup

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Dec 04 2015 Jared Smith <jsmith@fedoraproject.org> - 3.8-1
- Update to upstream 3.8 release for Drupal 7.x

* Tue Nov 17 2015 Jared Smith <jsmith@fedoraproject.org> - 3.6-1
- Update to upstream 3.6 release
- Upstream changelog at https://www.drupal.org/node/2616620

* Mon Jul 20 2015 Shawn Iwinski <shawn.iwinski@gmail.com> - 3.5-1
- Update to 3.5 (RHBZ #1244984)

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu May 07 2015 Jared Smith <jsmith@fedoraproject.org> - 3.4-1
- Update to new upstream 3.4 release
- Upstream changelog at https://www.drupal.org/node/2483499

* Sat Oct 18 2014 Shawn Iwinski <shawn.iwinski@gmail.com> - 3.3-1
- Updated to 3.3 (BZ #1150457)
- Removed RPM README b/c it only explained common Drupal workflow
- %%license usage

* Fri Jun 27 2014 Shawn Iwinski <shawn.iwinski@gmail.com> - 3.2-2
- Re-add EPEL-5 bits

* Fri Jun 27 2014 Shawn Iwinski <shawn.iwinski@gmail.com> - 3.2-1
- Updated to 3.2 (BZ #1103436; release notes https://www.drupal.org/node/2277339)
- Spec cleanup

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Feb 14 2014 Peter Borsa <peter.borsa@gmail.com> - 3.1-1
- Update to upstream 3.1 release for bug fixes
- Upstream changelog for this release is available at https://drupal.org/node/2188221

* Thu Nov 28 2013 Peter Borsa <peter.borsa@gmail.com> - 3.0-1
- Update to upstream 3.0 release for bug fixes
- Upstream changelog for this release is available at https://drupal.org/node/2138563

* Sun Sep 22 2013 Peter Borsa <peter.borsa@gmail.com> - 2.12-1
- Update to upstream 2.12 release for bug fixes
- Upstream changelog for this release is available at https://drupal.org/node/2087145

* Tue Sep 03 2013 Jared Smith <jsmith@fedoraproject.org> - 2.10-1
- Update to upstream 2.10 release for bug fixes
- Upstream changelog for this release is available at https://drupal.org/node/2076513

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Jul 24 2013 Peter Borsa <peter.borsa@gmail.com> - 2.9-1
- Update to upstream 2.9 release for bug fixes
- Upstream changelog for this release is avalble at https://drupal.org/node/2047899

* Wed Jun 12 2013 Peter Borsa <peter.borsa@gmail.com> - 2.8-1
- Update to upstream 2.8 release for bug fixes
- Upstream changelog for this release is avalble at http://drupal.org/node/2003618

* Thu Apr 25 2013 Jared Smith <jaredsmith@jaredsmith.net> - 2.7-1
- Update to upstream 2.7 release for bug fixes
- Upstream changelog for this release is avalble at http://drupal.org/node/1978108

* Thu Feb 28 2013 Jared Smith <jaredsmith@jaredsmith.net> - 2.6-1
- Update to upstream 2.6 release
- Upstream changelog for this release is avalble at http://drupal.org/node/1928594

* Wed Feb 13 2013 Jared Smith <jaredsmith@jaredsmith.net> - 2.5-1
- Update to upstream 2.5 release
- Add requires tag on drupal7-views >= 3.5, as this module depends on new
  functionality in views 3.5
- Upstream changelog for this release is available at http://drupal.org/node/1915436

* Tue Feb 05 2013 Jared Smith <jaredsmith@jaredsmith.net> - 2.4-1
- Update to upstream 2.4 release
- Upstream changelog for this release is available at http://drupal.org/node/1908020

* Tue Jan 29 2013 Jared Smith <jaredsmith@jaredsmith.net> - 2.3-1
- Update to upstream 2.3 release
- Upstream changelog for this release is available at http://drupal.org/node/1899324

* Thu Jan 24 2013 Jared Smith <jaredsmith@jaredsmith.net> - 2.2-1
- Update to upstream 2.2 release

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon May 28 2012 Peter Borsa <peter.borsa@gmail.com> - 1.1-1
- Initial Drupal 7 package
