# Disable automatic requires/provides processing
AutoReqProv: no

# RPM macros dir
%global macrosdir %(d=%{_rpmconfigdir}/macros.d; [ -d $d ] || d=%{_sysconfdir}/rpm; echo $d)

# Drupal 7 directories
%global drupal7      %{_datadir}/%{name}
%global drupal7_var  %{_localstatedir}/lib/%{name}
%global drupal7_conf %{_sysconfdir}/%{name}

%if 0%{?fedora} >= 29 || 0%{?rhel} >= 8
%define python_pkg python3
%define prov_source %SOURCE12
%else
%if 0%{?fedora} || 0%{?rhel} >= 6
%define python_pkg python2
%define prov_source %SOURCE9
%else
%define python_pkg python
%define prov_source %SOURCE7
%endif
%endif

Name:          drupal7
Version:       7.98
Release:       6%{?dist}
Summary:       An open-source content-management platform

# Automatically converted from old format: GPLv2+ and BSD and MIT - review is highly recommended.
License:       GPL-2.0-or-later AND LicenseRef-Callaway-BSD AND LicenseRef-Callaway-MIT
URL:           https://www.drupal.org

Source0:       https://ftp.drupal.org/files/projects/drupal-%{version}.tar.gz
Source1:       %{name}.conf
Source2:       %{name}-README.fedora
Source3:       %{name}-cron
Source4:       %{name}-files-migrator.sh
Source5:       macros.%{name}
Source6:       %{name}.attr
Source7:       %{name}.prov.python
Source8:       macros.%{name}.rpm-lt-4-9-compat
Source9:       %{name}.prov.python2
Source10:      %{name}.req
Source11:      %{name}.req.rpm-lt-4-9-compat
Source12:      %{name}.prov.python3
Source13:      %{name}-prep-licenses-and-docs.sh

Patch0:        %{name}-7.4-scripts-noshebang.patch

BuildArch:     noarch
BuildRequires: %{python_pkg}

Requires:      crontabs
Requires:      wget
%if 0%{?rhel}
Requires:      php
%else
Requires:      php(httpd)
%endif
# phpcompatinfo (computed from version 7.74)
Requires:      php-bcmath
Requires:      php-bz2
Requires:      php-curl
Requires:      php-date
Requires:      php-dom
Requires:      php-fileinfo
Requires:      php-filter
Requires:      php-ftp
Requires:      php-gd
Requires:      php-gmp
Requires:      php-hash
Requires:      php-iconv
Requires:      php-json
Requires:      php-libxml
Requires:      php-mbstring
Requires:      php-openssl
Requires:      php-pcre
Requires:      php-pdo
Requires:      php-pecl(ssh2)
Requires:      php-posix
Requires:      php-reflection
Requires:      php-session
Requires:      php-simplexml
Requires:      php-spl
Requires:      php-xml
Requires:      php-zip
Requires:      php-zlib

# Virtual provides
## Core
Provides:      drupal7(core) = %{version}
## Modules
Provides:      drupal7(aggregator) = %{version}
Provides:      drupal7(block) = %{version}
Provides:      drupal7(blog) = %{version}
Provides:      drupal7(book) = %{version}
Provides:      drupal7(color) = %{version}
Provides:      drupal7(comment) = %{version}
Provides:      drupal7(contact) = %{version}
Provides:      drupal7(contextual) = %{version}
Provides:      drupal7(dashboard) = %{version}
Provides:      drupal7(dblog) = %{version}
Provides:      drupal7(field_sql_storage) = %{version}
Provides:      drupal7(field_ui) = %{version}
Provides:      drupal7(field) = %{version}
Provides:      drupal7(file) = %{version}
Provides:      drupal7(filter) = %{version}
Provides:      drupal7(forum) = %{version}
Provides:      drupal7(help) = %{version}
Provides:      drupal7(image) = %{version}
Provides:      drupal7(list) = %{version}
Provides:      drupal7(locale) = %{version}
Provides:      drupal7(menu) = %{version}
Provides:      drupal7(node) = %{version}
Provides:      drupal7(number) = %{version}
Provides:      drupal7(openid) = %{version}
Provides:      drupal7(options) = %{version}
Provides:      drupal7(overlay) = %{version}
Provides:      drupal7(path) = %{version}
Provides:      drupal7(php) = %{version}
Provides:      drupal7(poll) = %{version}
Provides:      drupal7(rdf) = %{version}
Provides:      drupal7(search) = %{version}
Provides:      drupal7(shortcut) = %{version}
Provides:      drupal7(simpletest) = %{version}
Provides:      drupal7(statistics) = %{version}
Provides:      drupal7(syslog) = %{version}
Provides:      drupal7(system) = %{version}
Provides:      drupal7(taxonomy) = %{version}
Provides:      drupal7(text) = %{version}
Provides:      drupal7(toolbar) = %{version}
Provides:      drupal7(tracker) = %{version}
Provides:      drupal7(translation) = %{version}
Provides:      drupal7(trigger) = %{version}
Provides:      drupal7(update) = %{version}
Provides:      drupal7(user) = %{version}
## Themes
Provides:      drupal7(bartik) = %{version}
Provides:      drupal7(garland) = %{version}
Provides:      drupal7(seven) = %{version}
Provides:      drupal7(stark) = %{version}
## Profiles
Provides:      drupal7(minimal) = %{version}
Provides:      drupal7(standard) = %{version}


%description
Equipped with a powerful blend of features, Drupal is a Content Management
System written in PHP that can support a variety of websites ranging from
personal weblogs to large community-driven websites.  Drupal is highly
configurable, skinnable, and secure.


%package rpmbuild
Summary: Rpmbuild files for %{name}
Requires: %{python_pkg}

%description rpmbuild
%{summary}.


%prep
%setup -q -n drupal-%{version}

%if 0%{?fedora} || 0%{?rhel} >= 9
%patch 0 -p1
%else
%patch -P0 -p1
%endif

: Remove exec bit from all files
find . -type f -executable
find . -type f -executable -print0 | xargs -0 chmod -x

: Remove unneeded files
find . -name '.git*' -delete -print
find . -name '.travis*' -delete -print

: Licenses and docs
sh %{SOURCE13}
cp %{SOURCE2} .rpm/docs/
cp %{SOURCE4} .rpm/docs/


%build
# Empty build section, nothing required


%install
rm -rf %{buildroot}
install -d %{buildroot}%{drupal7}
cp -pr * %{buildroot}%{drupal7}
cp -pr .htaccess %{buildroot}%{drupal7}
mkdir -p %{buildroot}%{_sysconfdir}/httpd
mkdir -p %{buildroot}%{_sysconfdir}/httpd/conf.d
cp -pr %SOURCE1 %{buildroot}%{_sysconfdir}/httpd/conf.d/%{name}.conf
mkdir -p %{buildroot}%{drupal7_conf}
mv %{buildroot}%{drupal7}/sites/* %{buildroot}%{drupal7_conf}
mkdir -p %{buildroot}%{drupal7_conf}/all/libraries
rmdir %{buildroot}%{drupal7}/sites
ln -s ../../..%{drupal7_conf} %{buildroot}%{drupal7}/sites
mkdir -p %{buildroot}%{_docdir}
install -D -p -m 0644 %SOURCE3 %{buildroot}%{_sysconfdir}/cron.hourly/%{name}
mkdir -p %{buildroot}%{drupal7_var}/files/default
ln -s ../../..%{drupal7_var}/files/default %{buildroot}%{drupal7_conf}/default/files
mkdir -p %{buildroot}%{_sysconfdir}/httpd/conf.d
mv %{buildroot}%{drupal7}/.htaccess %{buildroot}%{_sysconfdir}/httpd/conf.d/drupal7-site.htaccess
ln -s ../../../%{_sysconfdir}/httpd/conf.d/drupal7-site.htaccess %{buildroot}%{drupal7}/.htaccess

# rpmbuild
# RPM >= 4.9
%if 0%{?_fileattrsdir:1}
mkdir -p %{buildroot}%{macrosdir}
install -pm0644 %{SOURCE5} %{buildroot}%{macrosdir}/macros.%{name}
mkdir -p %{buildroot}%{_prefix}/lib/rpm/fileattrs
install -pm0644 %{SOURCE6} %{buildroot}%{_prefix}/lib/rpm/fileattrs/%{name}.attr
install -pm0755 %{prov_source} %{buildroot}%{_prefix}/lib/rpm/%{name}.prov
install -pm0755 %{SOURCE10} %{buildroot}%{_prefix}/lib/rpm/%{name}.req
# RPM < 4.9
%else
mkdir -p %{buildroot}%{macrosdir}
install -pm0644 %{SOURCE8} %{buildroot}%{macrosdir}/macros.%{name}
mkdir -p %{buildroot}%{_prefix}/lib/rpm/
install -pm0755 %{prov_source} %{buildroot}%{_prefix}/lib/rpm/%{name}.prov
install -pm0755 %{SOURCE11} %{buildroot}%{_prefix}/lib/rpm/%{name}.req
%endif


%files
%{!?_licensedir:%global license %%doc}
%license .rpm/licenses/*
%doc .rpm/docs/*
%{drupal7}
# Configs
%dir %{drupal7_conf}
%dir %{drupal7_conf}/all
%dir %{drupal7_conf}/all/libraries
%dir %{drupal7_conf}/all/modules
%dir %{drupal7_conf}/all/themes
%dir %{drupal7_conf}/default
     %{drupal7_conf}/default/default.settings.php
     %{drupal7_conf}/default/files
     %{drupal7_conf}/example.sites.php
## HTTPD
%config(noreplace) %{_sysconfdir}/httpd/conf.d/%{name}.conf
%config(noreplace) %{_sysconfdir}/httpd/conf.d/%{name}-site.htaccess
## Files
%dir %attr(775,root,apache) %{drupal7_var}/
%dir %attr(775,root,apache) %{drupal7_var}/files
%dir %attr(775,root,apache) %{drupal7_var}/files/default
# Cron
%attr(755,root,apache) %config(noreplace) %{_sysconfdir}/cron.hourly/%{name}
# RPM
%{macrosdir}/macros.%{name}

%files rpmbuild
%{macrosdir}/macros.%{name}
%{?_fileattrsdir:%{_prefix}/lib/rpm/fileattrs/%{name}.attr}
%{_prefix}/lib/rpm/%{name}.prov
%{_prefix}/lib/rpm/%{name}.req


%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 7.98-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Aug 28 2024 Miroslav Suchý <msuchy@redhat.com> - 7.98-5
- convert license to SPDX

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 7.98-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 7.98-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 7.98-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Tue Sep 26 2023 Shawn Iwinski <shawn.iwinski@gmail.com> - 7.98-1
- Update to 7.98 (RHBZ #2217253)
- SA-CORE-2023-004
- SA-CORE-2023-005 (RHBZ #2188106, 2188107, 2188108)

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 7.92-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 7.92-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Oct 15 2022 Shawn Iwinski <shawn.iwinski@gmail.com> - 7.92-1
- Update to 7.92
- SA-CORE-2022-012 / CVE-2022-25275
- SA-CORE-2022-003 / CVE-2022-25271 (RHBZ #2055472, 2055473)
- SA-CORE-2022-001 / CVE-2021-41184
- SA-CORE-2022-002 / CVE-2021-41182 / CVE-2021-41183 / CVE-2016-7103 / CVE-2010-5312

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 7.82-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 7.82-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Sep 08 2021 Shawn Iwinski <shawn.iwinski@gmail.com> - 7.82-1
- Update to 7.82
- SA-CORE-2020-013 / CVE-2020-28948 / CVE-2020-28949
- SA-CORE-2021-001 / CVE-2020-36193
- SA-CORE-2021-002 / CVE-2020-13672 (RHBZ #1953010, #1953011)
- SA-CORE-2021-004 / CVE-2021-32610

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 7.74-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 7.74-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Nov 18 2020 Shawn Iwinski <shawn.iwinski@gmail.com> - 7.74-1
- Update to 7.74
- SA-CORE-2020-007 / CVE-2020-13666
- SA-CORE-2020-012 / CVE-2020-13671

* Fri Sep 04 2020 Shawn Iwinski <shawn.iwinski@gmail.com> - 7.72-1
- Update to 7.72
- SA-CORE-2020-004/CVE-2020-13663 (RHBZ #1860912, #1860913)

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 7.70-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sun May 31 2020 Shawn Iwinski <shawn.iwinski@gmail.com> - 7.70-2
- rpmbuild sub-pkg: Fix auto-provides for F32+

* Fri May 22 2020 Peter Borsa <peter@asrob.eu> - 7.70-1
- Update to 7.70
- RHBZ #1837516 / SA-CORE-2020-003
- RHBZ #1828416 / SA-CORE-2020-002

* Fri May 22 2020 Peter Borsa <peter@asrob.eu> - 7.69-3
- Remove php-recode as dependency

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 7.69-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Dec 18 2019 Shawn Iwinski <shawn.iwinski@gmail.com> - 7.69-1
- Update to 7.69 (RHBZ #1784967 / SA-CORE-2019-012)
- https://www.drupal.org/sa-core-2019-012

* Mon Dec 16 2019 Shawn Iwinski <shawn.iwinski@gmail.com> - 7.68-2
- Fix ssh2 dependency (`php-ssh2` => `php-pecl(ssh2)`)

* Sat Dec 14 2019 Shawn Iwinski <shawn.iwinski@gmail.com> - 7.68-1
- Update to 7.68 (RHBZ #1779680)
- Use official drupal.org source
- Expand requires to include full phpcompatinfo findings
- Spec, docs, licenses, and %%files revamp

* Sun Sep 15 2019 Shawn Iwinski <shawn.iwinski@gmail.com> - 7.67-3
- Use python3 for Fedora >= 29 and EPEL >= 8

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 7.67-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed May 15 2019 Shawn Iwinski <shawn.iwinski@gmail.com> - 7.67-1
- Update to 7.67 (RHBZ #1707958, #1708649, #1708652, #1708653)
- https://www.drupal.org/SA-CORE-2019-007 (CVE-2019-11831)

* Tue Apr 30 2019 Shawn Iwinski <shawn.iwinski@gmail.com> - 7.66-1
- Update to 7.66 (RHBZ #1701036, #1702424, #1702425, #1702620, #1702619)
- https://www.drupal.org/SA-CORE-2019-006 (CVE-2019-11358)

* Wed Mar 20 2019 Shawn Iwinski <shawn.iwinski@gmail.com> - 7.65-1
- Update to 7.65 (RHBZ #1691035)
- https://www.drupal.org/SA-CORE-2019-004

* Sat Feb 23 2019 Shawn Iwinski <shawn.iwinski@gmail.com> - 7.64-1
- Update to 7.64 (RHBZ #1673206)
- https://www.drupal.org/SA-CORE-2019-001
- https://www.drupal.org/SA-CORE-2019-002

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 7.60-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sun Oct 28 2018 Shawn Iwinski <shawn.iwinski@gmail.com> - 7.60-2
- Explicit python dependencies
- Explicit python2 except el5
- See https://koji.fedoraproject.org/koji/buildinfo?buildID=1156502

* Sat Oct 27 2018 Shawn Iwinski <shawn.iwinski@gmail.com> - 7.60-1
- Update to 7.60 (RHBZ #1643121 / RHBZ #1643122 / RHBZ #1643124 / SA-CORE-2018-006)
- Remove patch drupal-7.14-CVE-2012-2922 (see https://groups.drupal.org/node/230373)

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 7.59-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Apr 25 2018 Shawn Iwinski <shawn.iwinski@gmail.com> - 7.59-1
- Update to 7.59 (RHBZ #1572099 / RHBZ #1572100 / RHBZ #1572102 /
  SA-CORE-2018-004 / CVE-2018-7602)

* Wed Mar 28 2018 Shawn Iwinski <shawn.iwinski@gmail.com> - 7.58-1
- Update to 7.58 (RHBZ #1561801 / SA-CORE-2018-002 / CVE-2018-7600)

* Fri Feb 23 2018 Paul W. Frields <stickster@gmail.com> - 7.57-1
- Update to 7.57 (RHBZ #1548324 / RHBZ #1548326 / SA-CORE-2018-001 /
  CVE-2017-6927 / CVE-2017-6928 / CVE-2017-6929 / CVE-2017-6932)

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 7.56-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 7.56-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Thu Jun 22 2017 Shawn Iwinski <shawn.iwinski@gmail.com> - 7.56-1
- Update to 7.56 (RHBZ #1463856 / SA-CORE-2017-003 / CVE-2017-6922)

* Mon Jun 12 2017 Gwyn Ciesla <limburgher@gmail.com> - 7.55-2
- Requires fix for EPEL.

* Thu Jun 08 2017 Gwyn Ciesla <limburgher@gmail.com> - 7.55-1
- 7.55.

* Wed Mar 15 2017 Jon Ciesla <limburgher@gmail.com> - 7.54-3
- Require php(httpd), not php, BZ 1268937.

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 7.54-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 02 2017 Jon Ciesla <limburgher@gmail.com> - 7.54-1
- 7.54.

* Thu Dec 08 2016 Jon Ciesla <limburgher@gmail.com> - 7.53-1
- 7.53.

* Thu Nov 17 2016 Jon Ciesla <limburgher@gmail.com> - 7.52-1
- 7.52.

* Thu Oct 06 2016 Jon Ciesla <limburgher@gmail.com> - 7.51-1
- 7.51.

* Fri Jul 08 2016 Jon Ciesla <limburgher@gmail.com> - 7.50-1
- 7.50.

* Thu Jun 16 2016 Jon Ciesla <limburgher@gmail.com> - 7.44-1
- 7.44.

* Wed Feb 24 2016 Jared Smith <jsmith@fedoraproject.org> - 7.43-1
- Update to upstream 7.43 release for security issues (SA-CORE-2016-001)
- Upstream changelog at https://www.drupal.org/drupal-7.43-release-notes

* Thu Feb  4 2016 Paul W. Frields <stickster@gmail.com> - 7.42-1
- 7.42.

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 7.41-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Jan 25 2016 Jared Smith <jsmith@fedoraproject.org> - 7.41-2
- Remove calls to %%defattr macro, as they are no longer needed

* Thu Oct 22 2015 Jon Ciesla <limburgher@gmail.com> - 7.41-1
- 7.41.

* Thu Oct 15 2015 Jon Ciesla <limburgher@gmail.com> - 7.40-1
- 7.40.

* Fri Aug 21 2015 Shawn Iwinski <shawn.iwinski@gmail.com> - 7.39-1
- 7.39, SA-CORE-2015-003 (RHBZ #1255662, 1255672, 1255674)

* Thu Jun 18 2015 Peter Borsa <peter.borsa@gmail.com> - 7.38-1
- 7.38, DRUPAL-SA-CORE-2015-002.

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 7.37-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun May 10 2015 Paul W. Frields <stickster@gmail.com> - 7.37-1
- Update to upstream 7.37 maintenance release for bug fixes
- Upstream release notes at https://www.drupal.org/drupal-7.37-release-notes

* Fri Apr 03 2015 Jared Smith <jsmith@fedoraproject.org> - 7.36-1
- Update to upstream 7.36 maintenance release for numerous bug fixes
- Upstream release notes at https://www.drupal.org/drupal-7.36-release-notes

* Thu Mar 19 2015 Peter Borsa <peter.borsa@gmail.com> - 7.35-1
- 7.35, DRUPAL-SA-CORE-2015-001.

* Thu Nov 20 2014 Jon Ciesla <limburgher@gmail.com> - 7.34-1
- 7.34, DRUPAL-SA-CORE-2014-006.

* Tue Nov 11 2014 Peter Borsa <peter.borsa@gmail.com> - 7.33-1
- Update to upstream 7.33 maintenance release with numerous bug fixes

* Wed Oct 15 2014 Jared Smith <jsmith@fedoraproject.org> - 7.32-1
- Update to upstream 7.32 security release for SA-CORE-2014-005

* Thu Aug 07 2014 Jared Smith <jsmith@fedoraproject.org> - 7.31-1
- Update to upstream 7.31 release for SA-CORE-2014-004

* Mon Jul 28 2014 Paul W. Frields <stickster@gmail.com> - 7.30-1
- 7.30

* Wed Jul 16 2014 Paul W. Frields <stickster@gmail.com> - 7.29-1
- 7.29, SA-CORE-2014-003

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 7.28-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu May 08 2014 Jon Ciesla <limburgher@gmail.com> - 7.28-1
- 7.28, BZ 1095618.

* Thu Apr 17 2014 Jon Ciesla <limburgher@gmail.com> - 7.27-1
- 7.27, BZ 1088847.

* Mon Mar 10 2014 Jon Ciesla <limburgher@gmail.com> - 7.26-3
- Revised prior changes.

* Mon Mar 10 2014 Jon Ciesla <limburgher@gmail.com> - 7.26-2
- Update RPM macros location, BZ 1074272.  Should work
- on all branches.

* Wed Jan 15 2014 Jon Ciesla <limburgher@gmail.com> - 7.26-1
- 7.26, SA-CORE-2014-001.

* Fri Jan 03 2014 Jon Ciesla <limburgher@gmail.com> - 7.25-1
- 7.25, BZ 1048114.

* Thu Nov 21 2013 Peter Borsa <peter.borsa@gmail.com> - 7.24-1
- Update to upstream 7.24 release for security fixes
- Upstream changelog for this release is available at https://drupal.org/drupal-7.24-release-notes

* Sat Aug 10 2013 Peter Borsa <peter.borsa@gmail.com> - 7.23-3
- Fix indentation in drupal7.prov.rpm-lt-4-9-compat file.

* Sat Aug 10 2013 Peter Borsa <peter.borsa@gmail.com> - 7.23-2
- EL5 prov Python fix, BZ 995734.

* Thu Aug 08 2013 Peter Borsa <peter.borsa@gmail.com> - 7.23-1
- Update to upstream 7.23 release for bug fixes
- Upstream changelog for this release is available at https://drupal.org/drupal-7.23-release-notes

* Tue Jul 30 2013 Jon Ciesla <limburgher@gmail.com> - 7.22-8
- Add crontabs requires, BZ 989021.

* Wed Jul 10 2013 Jon Ciesla <limburgher@gmail.com> - 7.22-7
-  Typo and EL5 FHS fixes, BZ 979827.

* Tue Jun 18 2013 Jon Ciesla <limburgher@gmail.com> - 7.22-6
- Add AllowOverride All to drupal7.conf, BZ 905912.

* Mon Jun 03 2013 Jon Ciesla <limburgher@gmail.com> - 7.22-5
- Add auto-requires, BZ 969593.

* Tue May 21 2013 Jon Ciesla <limburgher@gmail.com> - 7.22-4
- Allow use of auto-provides <= EL-6.

* Thu May 09 2013 Jon Ciesla <limburgher@gmail.com> - 7.22-3
- Change rpmconfigdir to %%{_prefix}/lib/rpm to support EL-5.

* Thu May 09 2013 Jon Ciesla <limburgher@gmail.com> - 7.22-2
- Add libraries directory and macro, BZ 959687.
- Add auto-provides, BZ 959683.

* Thu Apr 4 2013 Peter Borsa <peter.borsa@gmail.com> - 7.22-1
- 7.22

* Thu Mar 7 2013 Peter Borsa <peter.borsa@gmail.com> - 7.21-1
- 7.21

* Thu Feb 21 2013 Paul W. Frields <stickster@gmail.com> - 7.20-1
- 7.20, SA-CORE-2013-002 (#913403)

* Fri Jan 25 2013 Jon Ciesla <limburgher@gmail.com> - 7.19-2
- README update for cron_key, BZ 902234.

* Thu Jan 17 2013 Jon Ciesla <limburgher@gmail.com> - 7.19-1
- 7.19, SA-CORE-2013-001.

* Thu Dec 20 2012 Jon Ciesla <limburgher@gmail.com> - 7.18-1
- 7.18.

* Thu Nov 8 2012 Peter Borsa <peter.borsa@gmail.com> - 7.17-2
- Fix README.txt location.

* Thu Nov 8 2012 Peter Borsa <peter.borsa@gmail.com> - 7.17-1
- New upstream.

* Wed Oct 31 2012 Jon Ciesla <limburgher@gmail.com> - 7.16-3
- Fix conf.

* Tue Oct 30 2012 Jon Ciesla <limburgher@gmail.com> - 7.16-2
- Fix for httpd 2.4, BZ 871394.

* Wed Oct 17 2012 Orion Poplawski <orion@cora.nwra.com> - 7.16-1
- New upstream - SA-CORE-2012-003 security update

* Wed Aug 1 2012 Peter Borsa <peter.borsa@gmail.com> - 7.15-1
- New upstream.

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 7.14-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu May 24 2012 Jon Ciesla <limburgher@gmail.com> - 7.14-2
- Patch for CVE-2012-2922, BZ 824631, BZ 824632.

* Thu May  3 2012 Paul W. Frields <stickster@gmail.com> - 7.14-1
- New upstream. (#818538)

* Thu Feb 02 2012 Jon Ciesla <limburgher@gmail.com> - 7.12-1
- New upstream.

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 7.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Dec 06 2011 Jon Ciesla <limburgher@gmail.com> - 7.10-1
- New upstream, BZ 760504.

* Thu Oct 27 2011 Paul W. Frields <stickster@gmail.com> - 7.9-1
- New upstream, BZ 749509.

* Sat Sep  3 2011 Paul W. Frields <stickster@gmail.com> - 7.8-1
- New upstream, minor bugfixes and API improvements only.

* Sun Aug  7 2011 Paul W. Frields <stickster@gmail.com> - 7.7-1
- New upstream, fixed version string only.

* Wed Jul 27 2011 Jon Ciesla <limb@jcomserv.net> - 7.6-1
- New upstream, SA-CORE-2011-003, BZ 726243.

* Thu Jun 30 2011 Jon Ciesla <limb@jcomserv.net> - 7.4-1
- New upstream, SA-CORE-2011-002, BZ 717874.
- Dropped unused dirs in /etc/drupal7/, BZ 703736.

* Fri Jun 17 2011 Jon Ciesla <limb@jcomserv.net> - 7.2-2
- Bump and rebuild for BZ 712251.

* Thu May 26 2011 Jon Ciesla <limb@jcomserv.net> - 7.2-1
- New upstream, SA-CORE-2011-001.

* Wed Apr 06 2011 Jon Ciesla <limb@jcomserv.net> - 7.0-4
- Exlcuded README and COPYRIGHT.
- Fixed sites symlink.

* Tue Mar 29 2011 Jon Ciesla <limb@jcomserv.net> - 7.0-3
- Fixed sites symlink.
- Moved example.sites.php to doc.
- Fixed year in changelog.
- Added php-pdo and php-xml requires.
- Corrected license tag.

* Fri Feb 25 2011 Jon Ciesla <limb@jcomserv.net> - 7.0-2
- Corrected license tag.

* Wed Jan 05 2011 Jon Ciesla <limb@jcomserv.net> - 7.0-1
- Initial packaging.
