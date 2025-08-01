
Name: phpldapadmin
Summary: Web-based tool for managing LDAP servers
Version: 1.2.6.7
Release: 3%{?dist}
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License: GPL-2.0-or-later
URL: https://www.phpldapadmin.org

Source: https://github.com/leenooks/phpLDAPadmin/refs/tags/%{version}.tar.gz

Patch0: phpldapadmin-1.2.6-config.patch

# From https://sources.debian.org/src/phpldapadmin/1.2.6.7-3/debian/patches/
Patch1: Fix-dynamic-property-PHP-8.2.patch
Patch2: Update-the-VERSION-file.patch
Patch3: 0004-Replace-E_STRICT-by-E_DEPRECATED.patch
Patch4: 0005-Stop-using-xml_set_object-for-PHP-8.4.patch
Patch5: 0006-Fix-deprecation-for-the-Serialization-of-SensitivePa.patch

BuildArch: noarch

Requires: httpd-filesystem, php(httpd), php-ldap
Requires: php-xml, php-gd, php-mbstring

# These ones are normally provided by the main php
Requires: php-date, php-gettext, php-hash, php-iconv
Requires: php-mhash, php-openssl, php-pcre, php-session, php-zlib


%description
PhpLDAPadmin is a web-based LDAP client.
It provides easy, anywhere-accessible, multi-language administration
for your LDAP server. Its hierarchical tree-viewer and advanced search
functionality make it intuitive to browse and administer your LDAP directory.

Since it is a web application, this LDAP browser works on many platforms,
making your LDAP server easily manageable from any location.

PhpLDAPadmin is the perfect LDAP browser for the LDAP professional
and novice alike. Its user base consists mostly of LDAP administration
professionals.

Edit %{_sysconfdir}/%{name}/config.php to change default (localhost) LDAP server
location and other things. Edit %{_sysconfdir}/httpd/conf.d/%{name}.conf to allow
access by remote web-clients.


%prep
%setup -q -n phpLDAPadmin-%{version}

cp config/config.php.example config/config.php

%patch 0 -p1
%patch 1 -p1
%patch 2 -p1
%patch 3 -p1
%patch 4 -p1
%patch 5 -p1


%build

find . \( -name "*.orig" -o -name "*~" -o -name .gitignore \) -print0 | \
								xargs -0 rm -f
find . -type f -print0 | xargs -0 chmod -x


%install
rm -rf $RPM_BUILD_ROOT

install -d -m755 $RPM_BUILD_ROOT%{_datadir}/%{name}
cp -a * $RPM_BUILD_ROOT%{_datadir}/%{name}


pushd $RPM_BUILD_ROOT%{_datadir}/%{name}
rm -rf doc/ INSTALL.md LICENSE README.md config/config.php.example
rm -rf tools/
find locale -name "*.po" -print0 | xargs -0 rm -f
popd


install -d -m755 $RPM_BUILD_ROOT%{_sysconfdir}/%{name}

mv $RPM_BUILD_ROOT%{_datadir}/%{name}/config/* \
	$RPM_BUILD_ROOT%{_sysconfdir}/%{name}
rmdir $RPM_BUILD_ROOT%{_datadir}/%{name}/config

UPS=$(echo %{_datadir}/%{name} | sed -e 's,^/,,' -e 's,[^/]*,..,g')
ln -s $UPS%{_sysconfdir}/%{name} \
	$RPM_BUILD_ROOT%{_datadir}/%{name}/config

cat <<EOF >%{name}.conf
#
#  %{summary}
#

Alias /%{name} %{_datadir}/%{name}/htdocs
Alias /ldapadmin %{_datadir}/%{name}/htdocs

<Directory %{_datadir}/%{name}/htdocs>
  <IfModule mod_authz_core.c>
    # Apache 2.4
    Require local
  </IfModule>
  <IfModule !mod_authz_core.c>
    # Apache 2.2
    Order Deny,Allow
    Deny from all
    Allow from 127.0.0.1
    Allow from ::1
  </IfModule>
</Directory>

EOF

install -d $RPM_BUILD_ROOT%{_sysconfdir}/httpd/conf.d
install -m644 %{name}.conf $RPM_BUILD_ROOT%{_sysconfdir}/httpd/conf.d



%post
if [ $1 -eq 1 ]; then
    set @@@ `dd bs=128 count=1 </dev/urandom 2>/dev/null | md5sum`
    sed -i "/session\['blowfish'\] = null;/ {
	s/^[^\$]*\\\$/\$/
	s/null;/'$2';  # Autogenerated for `uname -n`/
    }"  %{_sysconfdir}/%{name}/config.php
fi


%files
%config %dir %{_sysconfdir}/%{name}
%attr(640,root,apache) %config(noreplace) %{_sysconfdir}/%{name}/*.php
%config(noreplace) %{_sysconfdir}/httpd/conf.d/*.conf
%{_datadir}/%{name}
%doc INSTALL.md LICENSE README.md config/config.php.example


%changelog
* Fri Jul 25 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.6.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_43_Mass_Rebuild

* Fri Mar 28 2025 Dmitry Butskoy <Dmitry@Butskoy.name> - 1.2.6.7-2
- add Debian patches for php-8.x

* Fri Mar 28 2025 Dmitry Butskoy <Dmitry@Butskoy.name> - 1.2.6.7-1
- update to 1.2.6.7

* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.6.6-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 26 2024 Miroslav Suchý <msuchy@redhat.com> - 1.2.6.6-6
- convert license to SPDX

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.6.6-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.6.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.6.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.6.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sun May 14 2023 Dmitry Butskoy <Dmitry@Butskoy.name> - 1.2.6.6-1
- update to 1.2.6.6
- fix #2203293

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.6.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.6.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.6.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Sun Jan 16 2022 Dmitry Butskoy <Dmitry@Butskoy.name> - 1.2.6.3-1
- update to 1.2.6.3
- add fixes for php >= 8.0 (patches from Patrick Monnerat <patrick@monnerat.net>)

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.6.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.6.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Dec 11 2020 Dmitry Butskoy <Dmitry@Butskoy.name> - 1.2.6.2-1
- Update to 1.2.6.2 (#1906752)

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.3-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.3-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.3-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.3-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.3-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Mar 28 2018 Dmitry Butskoy <Dmitry@Butskoy.name> - 1.2.3-13
- Fix spec file (#1560470)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.3-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.3-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Jul 16 2017 Dmitry Butskoy <Dmitry@Butskoy.name> - 1.2.3-10
- Fix CVE-2017-11107 (#1471112)

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.3-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Nov 12 2013 Dmitry Butskoy <Dmitry@Butskoy.name> - 1.2.3-5
- Fix compatibility patch for php >= 5.5 (#974928)

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue Jun 18 2013 Dmitry Butskoy <Dmitry@Butskoy.name> - 1.2.3-3
- Add compatibility patch for php >= 5.5

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Oct 31 2012 Dmitry Butskoy <Dmitry@Butskoy.name> - 1.2.3-1
- update to 1.2.3
- fix apache config file (#871457)

* Tue Sep 18 2012 Dmitry Butskoy <Dmitry@Butskoy.name> - 1.2.2-3.gitbbedf1
- update to latest git source (CVE-2012-1114, CVE-2012-1115, #799873)

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Feb  2 2012 Dmitry Butskoy <Dmitry@Butskoy.name> - 1.2.2-1
- update to 1.2.2
- fix CVE-2012-0834 (#786821, patch from upstream)

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.1.1-3.20111006git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Oct 25 2011 Dmitry Butskoy <Dmitry@Butskoy.name> - 1.2.1.1-2.20111006git
- update to the latest git #cddf783 to fix security issues
  (XSS and code injection vulnerabilities, #748538)

* Fri Jul 22 2011 Dmitry Butskoy <Dmitry@Butskoy.name> - 1.2.1.1-1
- update to 1.2.1.1

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.0.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Sep 23 2010 Dmitry Butskoy <Dmitry@Butskoy.name> - 1.2.0.5-2
- add patches from Patrick Monnerat <pm@datasphere.ch>:
  * fix typo (close comment) in config file (#628067)
  * avoid php-5.3 deprecation errors (#628061)
  * fix add of parent class attributes (#628060)

* Mon Mar 29 2010 Dmitry Butskoy <Dmitry@Butskoy.name> - 1.2.0.5-1
- update to 1.2.0.5

* Fri Nov 20 2009 Dmitry Butskoy <Dmitry@Butskoy.name> - 1.2.0.4-1
- update to 1.2.0.4
- allow local IPv6 address by default as well (#539272)

* Wed Sep 16 2009 Dmitry Butskoy <Dmitry@Butskoy.name> - 1.2.0.3-1
- Upgrade to 1.2.0.3 (#523477)

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.0.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Apr  9 2009 Dmitry Butskoy <Dmitry@Butskoy.name> - 1.1.0.7-1
- update to 1.1.0.7

* Fri Sep 26 2008 Dmitry Butskoy <Dmitry@Butskoy.name> - 1.1.0.5-2
- update config patch

* Wed Feb 13 2008 Dmitry Butskoy <Dmitry@Butskoy.name> - 1.1.0.5-1
- upgrade to 1.1.0.5

* Fri Aug 17 2007 Dmitry Butskoy <Dmitry@Butskoy.name>
- Change License tag to GPLv2+
  (Note: most files do not specify any license information at all,
  which could lead just to "GPL+", but some lib/ files specify
  "GPLv2 or any later" explicitly, hence GPLv2+ wins).

* Tue Sep 19 2006 Dmitry Butskoy <Dmitry@Butskoy.name> - 1.0.1-1
- upgrade to 1.0.1
- drop namingcontexts patch, no more needed for php >= 5.0.6

* Fri Sep  1 2006 Dmitry Butskoy <Dmitry@Butskoy.name> - 0.9.8.3-2
- rebuild for FC6

* Mon May 15 2006 Dmitry Butskoy <Dmitry@Butskoy.name> - 0.9.8.3-1
- update to 0.9.8.3

* Tue Mar 14 2006 Dmitry Butskoy <Dmitry@Butskoy.name> - 0.9.8.2-1
- update to 0.9.8.2

* Thu Mar  2 2006 Dmitry Butskoy <Dmitry@Butskoy.name> - 0.9.8.1-1
- upgrade to 0.9.8.1
- remove unneeded tools dir *.po files in locale dir

* Fri Nov 18 2005 Dmitry Butskoy <Dmitry@Butskoy.name> - 0.9.7.2-2
- update upstream's tarball (was changed without version increment)
- don't treat VERSION as doc file (#173513)

* Tue Nov 15 2005 Dmitry Butskoy <Dmitry@Butskoy.name> - 0.9.7.2-1
- update to 0.9.7.2

* Tue Nov  1 2005 Dmitry Butskoy <Dmitry@Butskoy.name> - 0.9.7.1-1
- upgrade to 0.9.7.1
- adapt patches and spec to new upstream layout.
- don't strip debug anymore -- all seems to work fast enough now.

* Tue Sep 27 2005 Dmitry Butskoy <Dmitry@Butskoy.name> - 0.9.7-2
- patch cleanups.
- accepted for Fedora Extras devel
  (review by Aurelien Bompard <gauret@free.fr>)

* Mon Sep 26 2005 Dmitry Butskoy <Dmitry@Butskoy.name> - 0.9.7-1
- upgrade to final 0.9.7
- strip debug stuff completely. It gives essential speedup of work.
- initial install allow connects from localhost only (security reasons).

* Tue Sep 20 2005 Dmitry Butskoy <Dmitry@Butskoy.name> - 0.9.7-0.3.rc3
- upgrade to 0.9.7-rc3
- add post script to generate blowfish secret on initial installations.

* Thu Sep 15 2005 Dmitry Butskoy <Dmitry@Butskoy.name> - 0.9.7-0.2.rc2
- upgrade to 0.9.7-rc2, cvs snapshot no more needed.

* Tue Sep 13 2005 Dmitry Butskoy <Dmitry@Butskoy.name> - 0.9.7-0.1.20050912
- initial release. CVS snapshot is one week later than 0.9.7-rc1 release.
- add namingcontexts patch and config patch

