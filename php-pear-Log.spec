# remirepo/fedora spec file for php-pear-Log
#
# Copyright (c) 2006-2024 Remi Collet
# License: CC-BY-SA-4.0
# http://creativecommons.org/licenses/by-sa/4.0/
#
# Please, preserve the changelog entries
#
%{!?pear_metadir: %global pear_metadir %{pear_phpdir}}
%{!?__pear:       %global __pear       %{_bindir}/pear}
%global pear_name Log

Summary:        Abstracted logging facility for PHP
Name:           php-pear-Log
Version:        1.14.0
Release:        2%{?dist}
License:        MIT
URL:            http://pear.php.net/package/Log
Source:         http://pear.php.net/get/Log-%{version}.tgz

Patch0:         %{pear_name}-32bit.patch

BuildArch:      noarch
BuildRequires:  php(language) >= 7.4
BuildRequires:  php-pear

Requires:       php(language) >= 7.4
Requires:       php-pear(PEAR) >= 1.4.9
Requires:       php-pear(DB) >= 1.3
Requires:       php-pear(MDB2) >= 2.0.0
Requires:       php-pear(Mail)
Requires(post): %{__pear}
Requires(postun): %{__pear}

Provides:       php-pear(Log) = %{version}
Provides:       php-composer(pear/log) = %{version}


%description
The Log framework provides an abstracted logging system. 
It supports logging to console, file, syslog, SQL, Sqlite, mail, and mcal
targets.  It also provides a subject - observer mechanism.

php-pear-Log can optionally use package "php-pear-DB" (version >= 1.3)
and "php-pear-MDB2" (version >= 2.0.0RC1).


%prep
%setup -c -q

cd %{pear_name}-%{version}
%patch -P0 -p1
sed -e 's/md5sum="[^"]*"//' ../package.xml >%{name}.xml


%build
# Empty build section


%install
rm -rf %{buildroot}

cd %{pear_name}-%{version}
%{__pear} install --nodeps --packagingroot %{buildroot} %{name}.xml

# Clean up unnecessary files
rm -rf %{buildroot}%{pear_metadir}/.??*

# Install XML package description
install -D -p -m 644 %{name}.xml %{buildroot}%{pear_xmldir}/%{name}.xml



%check
cd %{pear_name}-%{version}
%{__pear} \
   run-tests \
   -d -i "-d include_path=%{buildroot}%{pear_phpdir}:%{pear_phpdir}" \
   tests | tee ../tests.log
grep "FAILED TESTS" ../tests.log && exit 1 || exit 0


%post
%{__pear} install --nodeps --soft --force --register-only %{pear_xmldir}/%{name}.xml >/dev/null || :


%postun
if [ "$1" -eq "0" ]; then
    %{__pear} uninstall --nodeps --ignore-errors --register-only %{pear_name} >/dev/null || :
fi


%files
%doc %{pear_docdir}/%{pear_name}
%{pear_phpdir}/Log
%{pear_phpdir}/Log.php
%{pear_testdir}/Log
%{pear_xmldir}/%{name}.xml
# sql script, not used in code, probably should be doc
%{pear_datadir}/Log


%changelog
* Wed Jan 10 2024 Remi Collet <remi@remirepo.net> - 1.14.0-2
- add patch for 32-bit from https://github.com/pear/Log/pull/30

* Wed Jan 10 2024 Remi Collet <remi@remirepo.net> - 1.14.0-1
- version 1.14.0
- raise dependency on PHP 7.4

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.13.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Feb 22 2023 Remi Collet <remi@remirepo.net> - 1.13.3-6
- fix for PHP 8.2 changes in test suite

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.13.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.13.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.13.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.13.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed May  5 2021 Remi Collet <remi@remirepo.net> - 1.13.3-1
- version 1.13.3 (no change)

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.13.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.13.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun  2 2020 Remi Collet <remi@remirepo.net> - 1.13.2-1
- version 1.13.2 (no change)

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.13.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.13.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.13.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.13.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.13.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.13.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.13.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sat Apr 16 2016 Remi Collet <remi@fedoraproject.org> - 1.13.1-1
- version 1.13.1
- provide php-composer(pear/log)

* Sun Apr  3 2016 Remi Collet <remi@fedoraproject.org> - 1.13.0-1
- version 1.13.0

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.12.9-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.12.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Jun 15 2015 Remi Collet <remi@fedoraproject.org> - 1.12.9-1
- version 1.12.9 (no change)

* Tue Jul 15 2014 Remi Collet <remi@fedoraproject.org> - 1.12.8-1
- version 1.12.8

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.12.7-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.12.7-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue Feb 19 2013 Remi Collet <remi@fedoraproject.org> - 1.12.7-7
- fix metadata location

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.12.7-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sun Aug 19 2012 Remi Collet <remi@fedoraproject.org> - 1.12.7-5
- rebuilt for new pear_datadir

* Tue Aug 14 2012 Remi Collet <remi@fedoraproject.org> - 1.12.7-4
- rebuilt for new pear_testdir

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.12.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.12.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Thu Sep 22 2011 Remi Collet <Fedora@FamilleCollet.com> 1.12.7-1
- Version 1.12.7 (stable) - API 1.0.0 (stable)
- minor spec cleanups

* Fri May 27 2011 Remi Collet <Fedora@FamilleCollet.com> 1.12.6-1
- Version 1.12.6 (stable) - API 1.0.0 (stable)

* Sun Apr 17 2011 Remi Collet <Fedora@FamilleCollet.com> 1.12.5-4
- remove temporary link in doc

* Wed Mar 16 2011 Remi Collet <Fedora@FamilleCollet.com> 1.12.5-3
- doc in %%{pear_docdir}

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.12.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Dec 23 2010 Remi Collet <Fedora@FamilleCollet.com> 1.12.5-1
- Version 1.12.5 (stable) - API 1.0.0 (stable)

* Mon Dec  6 2010 Remi Collet <Fedora@FamilleCollet.com> 1.12.4-1.1
- levels.phpt fails, see http://pear.php.net/bugs/18099

* Mon Dec  6 2010 Remi Collet <Fedora@FamilleCollet.com> 1.12.4-1
- Version 1.12.4 (stable) - API 1.0.0 (stable)

* Tue Sep 28 2010 Remi Collet <Fedora@FamilleCollet.com> 1.12.3-1
- Version 1.12.3 (stable) - API 1.0.0 (stable)
- run tests during %%check

* Sun Aug 29 2010 Remi Collet <Fedora@FamilleCollet.com> 1.12.2-1
- Version 1.12.2 (stable) - API 1.0.0 (stable)

* Sat May 29 2010 Remi Collet <Fedora@FamilleCollet.com> 1.12.1-1
- bump release (missing sources)

* Sat May 29 2010 Remi Collet <Fedora@FamilleCollet.com> 1.12.1-1
- update to Version 1.12.1 (stable) - API 1.0.0 (stable)
- type in french description

* Mon Jan 25 2010 Remi Collet <Fedora@FamilleCollet.com> 1.12.0-1
- update to 1.12.0

* Sat Dec 26 2009 Remi Collet <Fedora@FamilleCollet.com> 1.11.6-1
- update to 1.11.6

* Sat Aug 08 2009 Remi Collet <Fedora@FamilleCollet.com> 1.11.5-1
- update to 1.11.5
- rename Log.xml to php-pear-Log.xml

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.11.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon Mar 30 2009 Remi Collet <Fedora@FamilleCollet.com> 1.11.4-1
- update to 1.11.4

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.11.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sat Nov 22 2008 Remi Collet <Fedora@FamilleCollet.com> 1.11.3-1
- update to 1.11.3

* Fri Sep 05 2008 Remi Collet <Fedora@FamilleCollet.com> 1.11.2-1
- update to 1.11.2

* Wed Aug 06 2008 Remi Collet <Fedora@FamilleCollet.com> 1.11.1-1
- update to 1.11.1

* Sat Jun 28 2008 Remi Collet <Fedora@FamilleCollet.com> 1.11.0-1
- update to 1.11.0 : switch from PHP to MIT license

* Thu May 08 2008 Remi Collet <Fedora@FamilleCollet.com> 1.10.1-1
- update to 1.10.1

* Sat Jan 26 2008 Remi Collet <Fedora@FamilleCollet.com> 1.10.0-1
- update to 1.10.0
- add Requires php-pear(Mail) (new handler)
- remove levels.patch (merged upstream)

* Sat Jan 26 2008 Remi Collet <Fedora@FamilleCollet.com> 1.9.16-1
- update to 1.9.16
- add examples in documentation
- add levels.patch http://pear.php.net/bugs/bug.php?id=12933

* Wed Jan 02 2008 Remi Collet <Fedora@FamilleCollet.com> 1.9.14-1
- update to 1.9.14

* Thu Dec 13 2007 Remi Collet <Fedora@FamilleCollet.com> 1.9.13-1
- update to 1.9.13
- add documentation in %%check (post install only)

* Wed Dec 12 2007 Remi Collet <Fedora@FamilleCollet.com> 1.9.12-1
- update to 1.9.12

* Fri Aug 24 2007 Remi Collet <Fedora@FamilleCollet.com> 1.9.11-2
- Fix License

* Wed May 02 2007 Remi Collet <Fedora@FamilleCollet.com> 1.9.11-1
- update to 1.9.11

* Mon Feb 12 2007 Remi Collet <Fedora@FamilleCollet.com> 1.9.10-1
- update to 1.9.10
- All tests succeed with php-5.2.x : http://pear.php.net/bugs/bug.php?id=9023

* Sat Oct 28 2006 Remi Collet <Fedora@FamilleCollet.com> 1.9.9-1
- update to 1.9.9

* Sat Sep 16 2006 Remi Collet <Fedora@FamilleCollet.com> 1.9.8-6
- add CHANGELOG to %%doc

* Thu Sep 07 2006 Remi Collet <Fedora@FamilleCollet.com> 1.9.8-5.fc5.1
- rebuild for FC5

* Thu Sep 07 2006 Remi Collet <Fedora@FamilleCollet.com> 1.9.8-5
- BR php-pear >= 1:1.4.9-1.2

* Thu Sep 07 2006 Remi Collet <Fedora@FamilleCollet.com> 1.9.8-4
- last template.spec

* Mon Sep 04 2006 Remi Collet <Fedora@FamilleCollet.com> 1.9.8-3
- new and simpler %%prep and %%install

* Sat Sep 02 2006 Remi Collet <Fedora@FamilleCollet.com> 1.9.8-2
- failsafe scriplet

* Tue Aug 01 2006 Remi Collet <Fedora@FamilleCollet.com> 1.9.8-1
- update to 1.9.8

* Tue Jul 11 2006 Remi Collet <Fedora@FamilleCollet.com> 1.9.7-1
- update to 1.9.7
- use new macros from /etc/rpm/macros.pear

* Tue May 30 2006 Remi Collet <Fedora@FamilleCollet.com> 1.9.6-1
- install Licence in prep
- update to 1.9.6

* Mon May 15 2006 Remi Collet <Fedora@FamilleCollet.com> 1.9.5-3
- Require pear >= 1.4.9
- Requires(hint): (only comment actually) + description
- bundle the v3.01 PHP LICENSE file (as in php-pear)
- use --packagingroot (instead of -R)
- check from install to check (as in php-pear)

* Sat May 06 2006 Remi Collet <Fedora@FamilleCollet.com> 1.9.5-2
- cleanning (description-line-too-long)

* Sat May 06 2006 Remi Collet <Fedora@FamilleCollet.com> 1.9.5-1
- use %%{_datadir}/pear/.pkgxml for XML (Bug #190252)
- update to 1.9.5
- workaround for buggy pear 1.4.6 installer

* Thu Apr 27 2006 Remi Collet <Fedora@FamilleCollet.com> 1.9.4-1
- spec for extras
- add french summary & description

* Wed Apr 26 2006 Remi Collet <rpms@FamilleCollet.com> 1.9.4-1.fc{3,4,5}.remi
- update to 1.9.4

* Thu Apr 06 2006 Remi Collet <rpms@FamilleCollet.com> 1.9.3-1.fc{3,4,5}.remi
- initial RPM
