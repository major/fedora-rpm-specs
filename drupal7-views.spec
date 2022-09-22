%{?drupal7_find_provides_and_requires}

%global module views

Name:          drupal7-%{module}
Version:       3.24
Release:       7%{?pre_release:.%{pre_release}}%{?dist}
Summary:       Create customized lists and queries from your database

License:       GPLv2+
URL:           https://drupal.org/project/%{module}
Source0:       https://ftp.drupal.org/files/projects/%{module}-7.x-%{version}%{?pre_release:-%{pre_release}}.tar.gz

BuildArch:     noarch
BuildRequires: drupal7-rpmbuild >= 7.70-2

# views.info
Requires:      drupal7(ctools)
# phpcompatinfo (computed from version 3.24)
Requires:      php-date
Requires:      php-hash
Requires:      php-mbstring
Requires:      php-pcre

%description
You need Views if:
* You like the default front page view, but you find you want to sort it
  differently.
* You like the default taxonomy/term view, but you find you want to sort it
  differently; for example, alphabetically.
* You use /tracker, but you want to restrict it to posts of a certain type.
* You like the idea of the 'article' module, but it doesn't display articles
  the way you like.
* You want a way to display a block with the 5 most recent posts of some
  particular type.
* You want to provide 'unread forum posts'.
* You want a monthly archive similar to the typical Movable Type/Wordpress
  archives that displays a link to the in the form of "Month, YYYY (X)" where
  X is the number of posts that month, and displays them in a block. The links
  lead to a simple list of posts for that month.

Views can do a lot more than that, but those are some of the obvious uses of
Views.

This package provides the following Drupal 7 modules:
* %{module}
* %{module}_ui


%prep
%setup -qn %{module}

: Licenses and docs
mkdir -p .rpm/{licenses,docs}
mv LICENSE.txt .rpm/licenses/
mv *.txt .rpm/docs/
mkdir .rpm/docs/test_templates
mv test_templates/README.txt .rpm/docs/test_templates/


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
* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.24-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.24-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.24-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.24-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.24-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jun 05 2020 Shawn Iwinski <shawn@iwin.ski> - 3.24-2
- Bump build requires drupal7-rpmbuild to ">= 7.70-2" to fix F32+ auto provides

* Sun Apr 05 2020 Shawn Iwinski <shawn@iwin.ski> - 3.24-1
- Updated to 3.24 (RHBZ #1794211)

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.23-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.23-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 24 2019 Shawn Iwinski <shawn@iwin.ski> - 3.23-1
- Updated to 3.23 (RHBZ #1566277 / SA-CONTRIB-2019-034 / SA-CONTRIB-2019-034 / SA-CONTRIB-2019-036)
- https://www.drupal.org/sa-contrib-2019-036
- https://www.drupal.org/sa-contrib-2019-035
- https://www.drupal.org/sa-contrib-2019-034

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.18-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.18-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.18-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sun Sep 10 2017 Shawn Iwinski <shawn@iwin.ski> - 3.18-1
- Updated to 3.18 (RHBZ #1482276)

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.16-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Apr 08 2017 Shawn Iwinski <shawn@iwin.ski> - 3.16-1
- Updated to 3.16 (RHBZ #1433539)

* Mon Feb 27 2017 Shawn Iwinski <shawn@iwin.ski> - 3.15-1
- Updated to 3.15 (RHBZ #1425991)

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.14-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Jul 19 2016 Shawn Iwinski <shawn@iwin.ski> - 3.14-1
- Updated to 3.14 (RHBZ #1347061 / SA-CONTRIB-2016-036)
- Remove call to %%defattr as it is no longer needed

* Tue Apr 12 2016 Shawn Iwinski <shawn@iwin.ski> - 3.13-1
- Updated to 3.13 (RHBZ #1279841)
- Spec cleanup

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3.11-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Apr 30 2015 Peter Borsa <peter.borsa@gmail.com> - 3.11-1
- Release 3.11 is a security fix release
- Upstream changelog is at https://www.drupal.org/node/2480259

* Sat Feb 14 2015 Peter Borsa <peter.borsa@gmail.com> - 3.10-1
- Release 3.10 is a security fix release
- Upstream changelog is at https://drupal.org/node/2424103

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed May 21 2014 Peter Borsa <peter.borsa@gmail.com> - 3.8-1
- Release 3.8 is a security fix release
- Upstream changelog is at https://drupal.org/node/2271305

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Apr 10 2013 Jared Smith <jsmith@fedoraproject.org> - 3.7-1
- Release 3.7 is a bug-fix release
- Upstream changelog is at http://drupal.org/node/1965242

* Wed Mar 20 2013 Jared Smith <jsmith@fedoraproject.org> - 3.6-1
- Release 3.6 fixes a cross-site scripting vulnerability SA-CONTRIB-2013-035 (CVE-2013-1887)
- More details at http://drupal.org/node/1948358

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Aug 24 2012 Jared Smith <jsmith@fedoraproject.org> - 3.5-1
- Update to upstream 3.5 release
- Upstream changelog available at http://drupal.org/node/1751522

* Fri Aug 24 2012 Jared Smith <jsmith@fedoraproject.org> - 3.4-3
- Update to upstream 3.4 release

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Feb 23 2012 Jared Smith <jsmith@fedoraproject.org> - 3.3-1
- Update to upstream 3.3 release

* Mon Jan 23 2012 Jared Smith <jsmith@fedoraproject.org> - 3.1-1
- Update to 3.1 release version

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Fri Dec 23 2011 Jared Smith <jsmith@fedoraproject.org> - 3.0-1
- Update to 3.0 release version

* Thu Nov 17 2011 Jared Smith <jsmith@fedoraproject.org> - 3.0-0.1.rc3
- Update to RC3 version, including the security patch

* Sat Aug 06 2011 Jared Smith <jsmith@fedoraproject.org> - 3.0-0.1.rc1
- Initial version for Drupal 7
