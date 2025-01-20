# remirepo/fedora spec file for php-pear-Net-SMTP
#
# Copyright (c) 2006-2024 Remi Collet
# License: CC-BY-SA-4.0
# http://creativecommons.org/licenses/by-sa/4.0/
#
# Please, preserve the changelog entries
#
%{!?__pear:       %global __pear       %{_bindir}/pear}
%global pear_name Mail

Name:           php-pear-Mail
Version:        2.0.0
Release:        5%{?dist}
Summary:        Class that provides multiple interfaces for sending emails

License:        BSD-3-Clause
URL:            http://pear.php.net/package/Mail
Source0:        http://pear.php.net/get/%{pear_name}-%{version}.tgz

BuildArch:      noarch
BuildRequires:  php-pear(PEAR) >= 1.5.6

Requires:       php(language) >= 5.2.1
Requires:       php-pear(PEAR) >= 1.5.6 
Requires:       php-pear(Net_SMTP) >= 1.4.1
Requires(post): %{__pear}
Requires(postun): %{__pear}

Provides:       php-pear(%{pear_name}) = %{version}
Provides:       php-composer(pear/mail) = %{version}


%description
PEAR's Mail package defines an interface for implementing mailers under the
PEAR hierarchy.  It also provides supporting functions useful to multiple
mailer backends.  Currently supported backends include: PHP's native
mail() function, sendmail, and SMTP.  This package also provides a RFC822
email address list validation utility class.
 

%prep
%setup -q -c
mv package.xml %{pear_name}-%{version}/%{name}.xml


%build
cd %{pear_name}-%{version}
# Empty build section, most likely nothing required.


%install
cd %{pear_name}-%{version}
%{__pear} install --nodeps --packagingroot %{buildroot} %{name}.xml

# Clean up unnecessary files
rm -rf %{buildroot}%{pear_metadir}/.??*

# Install XML package description
mkdir -p %{buildroot}%{pear_xmldir}
install -pm 644 %{name}.xml %{buildroot}%{pear_xmldir}


%post
%{__pear} install --nodeps --soft --force --register-only \
    %{pear_xmldir}/%{name}.xml >/dev/null || :

%postun
if [ $1 -eq 0 ] ; then
    %{__pear} uninstall --nodeps --ignore-errors --register-only \
        %{pear_name} >/dev/null || :
fi


%files
%{pear_phpdir}/Mail.php
%{pear_phpdir}/Mail
%{pear_testdir}/Mail
%{pear_xmldir}/%{name}.xml
%{pear_docdir}/%{pear_name}


%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Tue Jan 16 2024 Remi Collet <remi@remirepo.net> - 2.0.0-1
- update to 2.0.0

* Mon Nov  6 2023 Remi Collet <remi@remirepo.net> - 1.6.0-1
- update to 1.6.0

* Fri Aug 25 2023 Remi Collet <remi@remirepo.net> - 1.5.1-1
- update to 1.5.1

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Apr 26 2023 Remi Collet <remi@remirepo.net> - 1.5.0-3
- use SPDX license ID

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Dec  2 2022 Remi Collet <remi@remirepo.net> - 1.5.0-1
- update to 1.5.0

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Apr 12 2017 Remi Collet <remi@remirepo.net> - 1.4.1-1
- update to 1.4.1

* Mon Apr 10 2017 Remi Collet <remi@remirepo.net> - 1.4.0-1
- update to 1.4.0
- add LICENSE file now provided by upstream
- add composer virtual provides

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Feb  1 2016 Remi Collet <remi@fedoraproject.org> - 1.3.0-1
- update to 1.3.0

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon Aug  5 2013 Remi Collet <remi@fedoraproject.org> - 1.2.0-9
- xml2changelog need simplexml

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue Feb 19 2013 Remi Collet <remi@fedoraproject.org> - 1.2.0-7
- fix metadata location

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Tue Aug 14 2012 Remi Collet <remi@fedoraproject.org> - 1.2.0-5
- rebuilt for new pear_testdir

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Mar  1 2010 Remi Collet <Fedora@FamilleCollet.com> 1.2.0-1
- update to 1.2.0
- license is now BSD

* Fri Nov 27 2009 Remi Collet <Fedora@FamilleCollet.com> 1.1.14-5
- Fix CVE-2009-4023 (#540842)
- rename Mail.xml to php-pear-Mail.xml

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.14-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.14-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Fri Aug 24 2007 Remi Collet <Fedora@FamilleCollet.com> 1.1.14-2
- Fix License

* Thu Oct 12 2006 Remi Collet <Fedora@FamilleCollet.com> 1.1.14-1
- update to 1.1.14

* Sat Sep 16 2006 Remi Collet <Fedora@FamilleCollet.com> 1.1.13-1
- regenerate SPEC with pear make-rpm-spec
- remove PEAR from sumnary
- update to 1.1.13
- add generated CHANGELOG %%doc

* Fri Sep 08 2006 Remi Collet <Fedora@FamilleCollet.com> 1.1.10-8
- last template.spec

* Mon Sep 04 2006 Remi Collet <Fedora@FamilleCollet.com> 1.1.10-7
- new and simpler %%prep and %%install

* Mon Aug 28 2006 Remi Collet <Fedora@FamilleCollet.com> 1.1.10-6
- FE6 rebuild

* Sat Jul 22 2006 Remi Collet <Fedora@FamilleCollet.com> 1.1.10-5
- remove "rm pearrc"
- secure scriplet with || :
- install Licence in prep
- use new macros from /etc/rpm/macros.pear

* Mon May 15 2006 Remi Collet <Fedora@FamilleCollet.com> 1.1.10-4
- Require pear >= 1:1.4.9
- Requires(hint): php-pear(Net_SMTP) >= 1.1.0 (only comment actually)
- bundle the v3.01 PHP LICENSE file
- use --packagingroot (instead of -R)
- check from install to check (as in php-pear)

* Sun May 14 2006 Remi Collet <Fedora@FamilleCollet.com> 1.1.10-3
- License : PHP -> PHP License

* Sat May 06 2006 Remi Collet <Fedora@FamilleCollet.com> 1.1.10-2
- new spec for extras
- use %%{_datadir}/pear/.pkgxml for XML (Bug #190252)

* Thu Apr 27 2006 Remi Collet <Fedora@FamilleCollet.com> 1.1.10-1
- spec for extras

* Wed Apr 26 2006 Remi Collet <rpms@FamilleCollet.com> 1.1.10-1.fc{3,4,5}.remi
- update to 1.1.10

* Thu Apr 06 2006 Remi Collet <rpms@FamilleCollet.com> 1.1.9-2.fc{3,4,5}.remi
- change /var/lib/pear to %%{_libdir}/php/pear for XML (as in extras for FC5)
- spec cleanning

* Sat Jan  7 2006 Remi Collet <remi.collet@univ-reims.fr> 1.1.9-1.fc{3,4}.remi
- initial RPM
