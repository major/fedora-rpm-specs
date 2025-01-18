Name:		dokuwiki
Summary:	Standards compliant simple to use wiki
License:	GPL-2.0-only

%global		releasenum 2023-04-04a
%global		releasetag %(rel="%{releasenum}"; echo "${rel//-/}")
Version:	%{releasetag}
Release:	6%{?dist}

URL:		https://www.dokuwiki.org/dokuwiki
Source0:	https://download.dokuwiki.org/src/%{name}/%{name}-%{releasenum}.tgz

#Fedora specific patches to use Fedora packaged libraries
Patch1:		dokuwiki-rm-bundled-libs.patch

BuildArch:	noarch

Requires:	php-gd
Requires:	php-json
Requires:	php-xml

Requires:	php-composer(aziraphale/email-address-validator) >= 2.0.1
# dokuwiki relies on a certain bugfix backported into geshi/geshi,
# hence the requirement also includes the RPM release number
Requires:	php-composer(geshi/geshi) >= 1.0.9.1-5
Requires:	php-composer(kissifrot/php-ixr) >= 1.8.3
Requires:	php-composer(marcusschwarz/lesserphp) >= 0.5.5
Requires:	php-composer(openpsa/universalfeedcreator) >= 1.8.4.1
Requires:	php-composer(phpseclib/phpseclib) >= 2.0.31
Requires:	php-composer(simplepie/simplepie) >= 1.5.6
Requires:	php-composer(splitbrain/php-archive) >= 1.2.1
Requires:	php-composer(splitbrain/php-cli) >= 1.1.8
Requires:	php-composer(splitbrain/php-jsstrip) >= 1.0.1
Requires:	php-composer(splitbrain/slika) >= 1.0.5


%description
DokuWiki is a standards compliant, simple to use Wiki, mainly aimed at creating
documentation of any kind. It has a simple but powerful syntax which makes sure
the data-files remain readable outside the Wiki and eases the creation of
structured texts.

All data is stored in plain text files no database is required.


%package selinux
Summary:	SELinux support for dokuwiki
Requires:	%name = %version-%release
Requires:	%{_sbindir}/semanage
Requires:	%{_sbindir}/restorecon
BuildArch:	noarch

%description selinux
Configures DokuWiki to run in SELinux enabled environments.


%prep
%setup -q -n %{name}-%{releasenum}

# Remove bundled code that's available as Fedora packages
#  email-address-validator
rm -r vendor/aziraphale/email-address-validator
rmdir vendor/aziraphale || true
#  geshi
rm -r vendor/geshi/geshi
rmdir vendor/geshi || true
#  kissifrot/php-ixr
rm -r vendor/kissifrot/php-ixr
rmdir vendor/kissifrot || true
#  lesserphp
rm -r vendor/marcusschwarz/lesserphp
rmdir vendor/marcusschwarz || true
#  universalfeedcreator
rm -r vendor/openpsa/universalfeedcreator
rmdir vendor/openpsa || true
#  phpseclib
rm -r vendor/phpseclib/phpseclib
rmdir vendor/phpseclib || true
#  simplepie
rm -r vendor/simplepie/simplepie
rmdir vendor/simplepie || true
#  splitbrain/php-archive, splitbrain/php-cli, splitbrain/slika
rm -r vendor/splitbrain/php-archive
rm -r vendor/splitbrain/php-cli
rm -r vendor/splitbrain/slika
# rm -r vendor/splitbrain/php-jsstrip
# rmdir vendor/splitbrain || true

%patch -P1 -p1 -b .bundled

mv -f conf/mysql.conf.php.example .

sed -i "s:'./data':'%{_localstatedir}/lib/%{name}/data':" conf/%{name}.php
sed -i "s:ALL        8:ALL        1:" conf/acl.auth.php.dist

cat <<EOF >%{name}.httpd

Alias /%{name} %{_datadir}/%{name}

<Directory %{_datadir}/%{name}>
	<IfModule mod_authz_core.c>
		# Apache 2.4
		Require local
	</IfModule>
	<IfModule !mod_authz_core.c>
		# Apache 2.2
		Options +FollowSymLinks
		Order Allow,Deny
		Allow from 127.0.0.1 ::1
	</IfModule>
</Directory>

<Directory %{_datadir}/%{name}/bin>
	Order Deny,Allow
	Deny from all
</Directory>

<Directory %{_datadir}/%{name}/conf>
	Order Deny,Allow
	Deny from all
</Directory>

<Directory %{_datadir}/%{name}/inc>
	Order Deny,Allow
	Deny from all
</Directory>

<Directory %{_datadir}/%{name}/vendor>
	Order Deny,Allow
	Deny from all
</Directory>

EOF

cat <<EOF >DOKUWIKI-SELINUX.README
%{name}-selinux
====================

This package configures dokuwiki to run in
SELinux enabled environments

EOF

%build
# nothing to do here

%install
install -d -p %{buildroot}%{_sysconfdir}/%{name}
install -d -p %{buildroot}%{_sysconfdir}/httpd/conf.d
install -d -p %{buildroot}%{_datadir}/%{name}
install -d -p %{buildroot}%{_datadir}/%{name}/bin
install -d -p %{buildroot}%{_localstatedir}/lib/%{name}
mkdir -p %{buildroot}%{_localstatedir}/lib/%{name}/data/{attic,cache,index,locks,log,media,media_attic,media_meta,meta,pages,tmp}
rm -f install.php
rm -f inc/.htaccess
rm -f inc/lang/.htaccess
rm -f vendor/.htaccess
cp -rp data/pages/* %{buildroot}%{_localstatedir}/lib/%{name}/data/pages/
cp -rp conf/* %{buildroot}%{_sysconfdir}/%{name}
cp -rp bin/*  %{buildroot}%{_datadir}/%{name}/bin
cp -rp lib  %{buildroot}%{_datadir}/%{name}/
cp -rp inc  %{buildroot}%{_datadir}/%{name}/
cp -rp vendor  %{buildroot}%{_datadir}/%{name}/
install -p -m0644 *.php %{buildroot}%{_datadir}/%{name}
install -p -m0644 %{name}.httpd %{buildroot}%{_sysconfdir}/httpd/conf.d/%{name}.conf

pushd %{buildroot}%{_sysconfdir}/%{name}
for d in *.dist; do
	d0=`basename $d .dist`
	if [ ! -f "$d0" ]; then
		mv -f $d $d0
	fi
done
popd

pushd %{buildroot}%{_datadir}/%{name}
	ln -sf ../../../etc/%name conf
popd

%post selinux
semanage fcontext -a -t httpd_sys_rw_content_t '%{_sysconfdir}/%{name}(/.*)?' 2>/dev/null || :
semanage fcontext -a -t httpd_sys_content_t '%{_datadir}/%{name}(/.*)?' 2>/dev/null || :
semanage fcontext -a -t httpd_sys_rw_content_t '%{_datadir}/%{name}/lib/plugins(/.*)?' 2>/dev/null || :
restorecon -R '%{_sysconfdir}/%{name}' || :
restorecon -R '%{_datadir}/%{name}' || :

%postun selinux
if [ $1 -eq 0 ] ; then
semanage fcontext -d -t httpd_sys_rw_content_t '%{_sysconfdir}/%{name}(/.*)?' 2>/dev/null || :
semanage fcontext -d -t httpd_sys_content_t '%{_datadir}/%{name}(/.*)?' 2>/dev/null || :
semanage fcontext -d -t httpd_sys_rw_content_t '%{_datadir}/%{name}/lib/plugins(/.*)?' 2>/dev/null || :
fi


%files
%doc COPYING README VERSION mysql.conf.php.example
%config(noreplace) %{_sysconfdir}/httpd/conf.d/%{name}.conf
%config(noreplace) %attr(0644,apache,apache) %{_sysconfdir}/%{name}/*
%dir %attr(0755,apache,apache) %{_sysconfdir}/%{name}
%attr(0755,apache,apache) %{_datadir}/%{name}/bin/*.php
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/conf
%{_datadir}/%{name}/*.php
%dir %{_datadir}/%{name}/lib
%{_datadir}/%{name}/lib/exe
%{_datadir}/%{name}/lib/images
%{_datadir}/%{name}/lib/index.html
%{_datadir}/%{name}/lib/scripts
%{_datadir}/%{name}/lib/styles
%{_datadir}/%{name}/lib/tpl
%attr(0755,apache,apache) %dir %{_datadir}/%{name}/lib/plugins
%{_datadir}/%{name}/lib/plugins/*
%{_datadir}/%{name}/inc
%{_datadir}/%{name}/vendor
%dir %{_localstatedir}/lib/%{name}
%attr(0755,apache,apache) %dir %{_localstatedir}/lib/%{name}/data
%attr(0755,apache,apache) %dir %{_localstatedir}/lib/%{name}/data/attic
%attr(0755,apache,apache) %dir %{_localstatedir}/lib/%{name}/data/cache
%attr(0755,apache,apache) %dir %{_localstatedir}/lib/%{name}/data/index
%attr(0755,apache,apache) %dir %{_localstatedir}/lib/%{name}/data/locks
%attr(0755,apache,apache) %dir %{_localstatedir}/lib/%{name}/data/log
%attr(0755,apache,apache) %dir %{_localstatedir}/lib/%{name}/data/media
%attr(0755,apache,apache) %dir %{_localstatedir}/lib/%{name}/data/media_attic
%attr(0755,apache,apache) %dir %{_localstatedir}/lib/%{name}/data/media_meta
%attr(0755,apache,apache) %dir %{_localstatedir}/lib/%{name}/data/meta
%attr(0755,apache,apache) %dir %{_localstatedir}/lib/%{name}/data/pages
%attr(0755,apache,apache) %dir %{_localstatedir}/lib/%{name}/data/pages/wiki
%attr(0755,apache,apache) %dir %{_localstatedir}/lib/%{name}/data/tmp
%{_localstatedir}/lib/%{name}/data/pages/*/*

%files selinux
%doc DOKUWIKI-SELINUX.README

%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 20230404a-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 20230404a-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 20230404a-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 20230404a-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 20230404a-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Mon May 15 2023 Artur Frenszek-Iwicki <fedora@svgames.pl> - 20230404a-1
- Update to version 2023-04-04a (hotfix update)

* Sat Apr 15 2023 Artur Frenszek-Iwicki <fedora@svgames.pl> - 20230404-2
- Unbundle php-splitbrain-php-jsstrip

* Wed Apr 05 2023 Artur Frenszek-Iwicki <fedora@svgames.pl> - 20230404-1
- Update to latest release (2023-04-04 "Jack Jackrum")
- Fix package not creating the data/log directory
- Migrate license tag to SPDX

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 20220731a-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Mon Oct 10 2022 Artur Frenszek-Iwicki <fedora@svgames.pl> - 20220731a-2
- Unbundle php-splitbrain-php-archive
- Unbundle php-splitbrain-php-cli
- Unbundle php-splitbrain-slika
- Unbundle php-kissifrot-php-ixr

* Thu Sep 15 2022 Artur Frenszek-Iwicki <fedora@svgames.pl> - 20220731a-1
- Update to latest upstream release (2022-07-31a "Igor")
- Add minimum versions for all dependencies
- Add "Provides: bundled()" for not-yet-unbundled libraries

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 20200729-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 20200729-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 20200729-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 20200729-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sun Sep 20 2020 Artur Frenszek-Iwicki <fedora@svgames.pl> - 20200729-2
- Switch to requiring php-email-address-validation via php-composer()
- Add a minimum version requirement on php-email-address-validation

* Wed Aug 26 2020 Artur Iwicki <fedora@svgames.pl> - 20200729-1
- Update to latest upstream release (2020-07-29 "Hogfather")
- Unbundle php-openpsa-universalfeedcreator

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 20180422b-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Mar 23 2020 Artur Iwicki <fedora@svgames.pl> - 20180422b-1
- Use file-level dependencies in -selinux subpackage
- Replace dependency on php-lessphp with php-marcusschwarz-lesserphp
- Switch to naming dependencies using php-composer()

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 20180422b-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 20180422b-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Artur Iwicki <fedora@svgames.pl> - 20180422b-1
- Update to new upstream bugfix release

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 20180422a-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Aug 25 2018 Artur Iwicki <fedora@svgames.pl> - 20180422a-1
- Change the versioning scheme

* Mon Aug 20 2018 Artur Iwicki <fedora@svgames.pl> - 0-0.34.20180422a
- Remove the "Group:" tag (no longer used in Fedora)
- Replace the hand-written %%releasetag with one generated from %%releasenum

* Fri Jul 13 2018 Peter 'Pessoft' Kolínek <fedora@pessoft.com> - 0-0.33.20180422a
- Update to the latest stable upstream 2018-04-22a "Greebo" (#1390291: CVE-2016-7964, CVE-2016-7965, CVE-2017-12583, CVE-2017-12979, CVE-2017-12980, CVE-2017-18123)
- Fix missing vendor directory issue (#1372948)
- Fix Apache config file for access to conf and bin
- Replace more bundled code in vendor directory with Fedora packages (lesserphp, random_compat, phpseclib, simplepie)
- Fix source to HTTPS

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.32.20150810a
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Mar 30 2018 Iryna Shcherbina <ishcherb@redhat.com> - 0-0.31.20150810a
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.30.20150810a
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.29.20150810a
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.28.20150810a
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.27.20150810a
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Sep 30 2015 Adam Tkac <vonsch@gmail.com> - 0.0.26.20150810a
- update to the latest upstream

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.25.20140929c
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Mar 03 2015 Adam Tkac <vonsch@gmail.com> - 0.0.24.20140929c
- update to the latest upstream (CVE-2015-2172)

* Fri Dec 26 2014 Adam Tkac <vonsch@gmail.com> - 0.0.23.20140929b
- update to the latest upstream
- drop requirement of httpd (#1164396)
- fix SELinux file contexts (#1064524)
- require php-xml (#1061477)

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.22.20131208
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu Dec 12 2013 Adam Tkac <vonsch@gmail.com> - 0-0.21.20131208
- fix upstream source link
- use macros for dokuwiki release numbers
- update to the latest upstream

* Tue Sep 03 2013 Adam Tkac <vonsch@gmail.com> - 0-0.20.20130510a
- fix Requires for EL5, #967975 (patch by Charles R. Anderson)

* Tue Sep 03 2013 Adam Tkac <vonsch@gmail.com> - 0-0.19.20121013
- update to the latest upstream

* Tue Sep 03 2013 Adam Tkac <vonsch@gmail.com> - 0-0.18.20121013
- remove bundled code in specfile instead of via patch

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.17.20121013
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.16.20121013
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sun Dec 02 2012 Johan Cwiklinski <johan AT x-tnd DOT be> - 0-0.15.20121013
- Fix apache config file for httpd 2.4, #871388

* Sat Oct 20 2012 Andrew Colin Kissa <andrew@topdog.za.net> - 0-0.14.20121013
- Latest upstream
- Fix Bugzilla bugs #844726, #840255, #795487, #741384, #840686, #835145

* Thu Aug 02 2012 Andrew Colin Kissa <andrew@topdog.za.net> - 0-0.13.20120125.b
- Latest upstream
- Fix Bugzilla bugs #844726, #840255, #795487, #741384, #840686, #835145

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.12.20110525.a
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Apr 24 2012 Andrew Colin Kissa <andrew@topdog.za.net> - 0-0.11.20110525.a
- Fix CVE-2012-2129
- Fix Bugzilla bugs #815123

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.10.20110525.a
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Jun 28 2011 Andrew Colin Kissa <andrew@topdog.za.net> - 0-0.9.20110525.a
- Upgrade to latest upstream
- Fix Bugzilla bugs #717146, #717149, #717148, #715569

* Sun Mar 13 2011 Andrew Colin Kissa <andrew@topdog.za.net> - 0-0.8.20101107.a
- Fix genshi path

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.7.20101107.a
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Jan 17 2011 Andrew Colin Kissa <andrew@topdog.za.net> - 0-0.6.20101107.a
- Fix selinux sub package

* Mon Jan 17 2011 Andrew Colin Kissa <andrew@topdog.za.net> - 0-0.5.20101107.a
- Upgrade to latest upstream
- Split package to create selinux package
- Fix Bugzilla bug #668386

* Tue Jan 19 2010 Andrew Colin Kissa <andrew@topdog.za.net> - 0-0.4.20091225.c
- Fix CSRF bug Secunia advisory SA38205, dokuwiki bug #1853
- Fix Security ACL bypass bug Secunia advisory SA38183, dokuwiki bug #1847
- Upgrade to the latest upstream
- Fix bugzilla bug #556494

* Tue Dec 15 2009 Andrew Colin Kissa <andrew@topdog.za.net> - 0-0.3.20091202.rc
- Fix versioning

* Fri Dec 04 2009 Andrew Colin Kissa <andrew@topdog.za.net> - 0-0.1.20091202.rc
- Upgrade to new upstream
- Fix bugzilla bug #544257

* Fri Aug 07 2009 Andrew Colin Kissa <andrew@topdog.za.net> - 0-0.2.20090214.b
- Fixes requested by reviewer

* Thu Aug 06 2009 Andrew Colin Kissa <andrew@topdog.za.net> - 0-0.1.20090214.b
- Initial package
