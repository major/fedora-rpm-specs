%{?drupal7_find_provides_and_requires}

%global module backup_migrate

Name:          drupal7-%{module}
Version:       3.7
Release:       7%{?dist}
Summary:       Backup the Drupal database and files or migrate them to another environment

License:       GPLv2+
URL:           https://drupal.org/project/%{module}
Source0:       https://ftp.drupal.org/files/projects/%{module}-7.x-%{version}.tar.gz

BuildArch:     noarch
BuildRequires: drupal7-rpmbuild >= 7.70-2

# backup_migrate.info
Requires:      php(language) >= 5.4
# phpcompatinfo (computed from version 3.7)
Requires:      php-bz2
Requires:      php-date
Requires:      php-ftp
Requires:      php-pcre
Requires:      php-zip
Requires:      php-zlib

%description
Back up and restore your Drupal MySQL database, code, and files or migrate
a site between environments. Backup and Migrate supports gzip, bzip and zip
compression as well as automatic scheduled backups.

With Backup and Migrate you can dump some or all of your database tables to a
file download or save to a file on the server or offsite, and to restore from
an uploaded or previously saved database dump. You can choose which tables and
what data to backup and cache data is excluded by default.

Features:
* Backup/Restore multiple MySQL databases and code
* Backup of files directory is built into this version
* Add a note to backup files
* Smart delete options make it easier to manage backup files
* Backup to FTP/S3/Email or NodeSquirrel.com
* Drush integration
* Multiple backup schedules
* AES encryption for backups

This package provides the following Drupal module:
* %{module}


%prep
%setup -qn %{module}

: Licenses and docs
mkdir -p .rpm/{licenses,docs}
mv LICENSE.txt .rpm/licenses/
mv *.txt .rpm/docs/


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
* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.7-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.7-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.7-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jun 05 2020 Shawn Iwinski <shawn.iwinski@gmail.com> - 3.7-2
- Bump build requires drupal7-rpmbuild to ">= 7.70-2" to fix F32+ auto provides

* Sun Apr 05 2020 Shawn Iwinski <shawn@iwin.ski> - 3.7-1
- Update to 3.7 (RHBZ #1808584)

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sun Jun 24 2018 Shawn Iwinski <shawn.iwinski@gmail.com> - 3.5-1
- Update to 3.5 (RHBZ #1503867)

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sun Oct 08 2017 Shawn Iwinski <shawn.iwinski@gmail.com> - 3.2-1
- Updated to 3.2 (RHBZ #1496611)

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Jul 06 2015 Shawn Iwinski <shawn.iwinski@gmail.com> - 3.1-1
- Updated to 3.1 (RHBZ #1220584)
- Removed RPM README b/c it only explained common Drupal workflow
- Keep documentation where end-users expect it
- %%license usage

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Jun 29 2014 Shawn Iwinski <shawn.iwinski@gmail.com> - 3.0-3
- Require "php-zip" instead of "php-pecl(zip)"

* Fri Jun 27 2014 Shawn Iwinski <shawn.iwinski@gmail.com> - 3.0-2
- Re-add EPEL-5 bits

* Fri Jun 27 2014 Shawn Iwinski <shawn.iwinski@gmail.com> - 3.0-1
- Updated to 3.0 (BZ #1101926; release notes https://www.drupal.org/node/2275063)
- Spec cleanup

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed Nov 06 2013 Peter Borsa <peter.borsa@gmail.com> - 2.8-1
- Update to upstream 2.8 release for bug fixes
- Upstream changelog for this release is available at https://drupal.org/node/2128465

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Jun 13 2013 Peter Borsa <peter.borsa@gmail.com> - 2.7-1
- Update to upstream 2.7 release for bug fixes
- Upstream changelog for this release is available at https://drupal.org/node/1996614

* Mon Apr 15 2013 Peter Borsa <peter.borsa@gmail.com> - 2.5-1
- Update to 2.5

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Jun 19 2012 Scott Dodson <sdodson@redhat.com> - 2.4-1
- Update to 2.4

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Sep 13 2011 Scott Dodson <sdodson@redhat.com> - 2.2-2
- Fix FSF Address in LICENSE.txt

* Wed Aug 31 2011 Scott Dodson <sdodson@redhat.com> - 2.2-1
- Initial Drupal 7 version
