# spec file for php-pear-Mail-Mime
#
# Copyright (c) 2009-2024 Remi Collet
# Copyright (c) 2006-2008 Brandon Holbrook
#
# License: MIT
# http://opensource.org/licenses/MIT
#
# Please, preserve the changelog entries
#
%{!?__pear:       %global __pear       %{_bindir}/pear}
%global pear_name Mail_Mime

Name:           php-pear-Mail-Mime
Version:        1.10.12
Release:        3%{?dist}
Summary:        Classes to create MIME messages

License:        BSD-3-Clause
URL:            http://pear.php.net/package/Mail_Mime
Source0:        http://pear.php.net/get/Mail_Mime-%{version}.tgz

BuildArch:      noarch
BuildRequires:  php-pear(PEAR) >= 1.6.0
BuildRequires:  php-mbstring

Requires:       php-pear(PEAR) >= 1.6.0
Requires:       php-date
Requires:       php-mbstring
Requires:       php-pcre
Requires(post): %{__pear}
Requires(postun): %{__pear}

Provides:       php-pear(%{pear_name}) = %{version}
Provides:       php-composer(pear/mail_mime) = %{version}


%description
Mail_Mime provides classes to deal with the creation and manipulation 
of MIME messages. It allows people to create e-mail messages consisting of:
* Text Parts
* HTML Parts
* Inline HTML Images
* Attachments
* Attached messages

It supports big messages, base64 and quoted-printable encoding and
non-ASCII characters in file names, subjects, recipients, etc. encoded
using RFC2047 and/or RFC2231.


%prep
%setup -q -c 
cd %{pear_name}-%{version}
mv ../package.xml %{name}.xml


%build
# Empty build section, nothing required


%install
cd %{pear_name}-%{version}
%{__pear} install --nodeps --packagingroot %{buildroot} %{name}.xml

# Clean up unnecessary files
rm -rf %{buildroot}%{pear_metadir}/.??*

# Install XML package description
mkdir -p %{buildroot}%{pear_xmldir}
install -pm 644 %{name}.xml %{buildroot}%{pear_xmldir}


%check
cd %{pear_name}-%{version}
%{__pear} \
   run-tests \
   -i "-d include_path=%{buildroot}%{pear_phpdir}:%{pear_phpdir}" \
   tests | tee ../tests.log
grep "FAILED TESTS" ../tests.log && exit 1
exit 0


%post
%{__pear} install --nodeps --soft --force --register-only %{pear_xmldir}/%{name}.xml >/dev/null ||:


%postun
# if refcount = 0 then package has been removed (not upgraded)
if [ "$1" -eq "0" ]; then
   %{__pear} uninstall --nodeps --ignore-errors --register-only %{pear_name} >/dev/null ||:
fi


%files
%doc %{pear_testdir}/%{pear_name}
%{pear_xmldir}/%{name}.xml
%{pear_phpdir}/Mail


%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.12-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.12-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Tue Mar 12 2024 Remi Collet <remi@remirepo.net> - 1.10.12-1
- update to 1.10.12

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.11-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.11-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.11-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Apr 26 2023 Remi Collet <remi@remirepo.net> - 1.10.11-5
- use SPDX license ID

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.11-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.11-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Sep  8 2021 Remi Collet <remi@remirepo.net> - 1.10.11-1
- update to 1.10.11

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.10-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jan 18 2021 Remi Collet <remi@remirepo.net> - 1.10.10-1
- update to 1.10.10

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jun 29 2020 Remi Collet <remi@remirepo.net> - 1.10.9-1
- update to 1.10.9

* Mon Jun 15 2020 Remi Collet <remi@remirepo.net> - 1.10.8-1
- update to 1.10.8

* Mon Mar  2 2020 Remi Collet <remi@remirepo.net> - 1.10.7-1
- update to 1.10.7

* Thu Jan 30 2020 Remi Collet <remi@remirepo.net> - 1.10.6-1
- update to 1.10.6

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Jan 27 2020 Remi Collet <remi@remirepo.net> - 1.10.5-1
- update to 1.10.5

* Mon Oct 14 2019 Remi Collet <remi@remirepo.net> - 1.10.4-1
- update to 1.10.4

* Wed Sep 25 2019 Remi Collet <remi@remirepo.net> - 1.10.3-1
- update to 1.10.3

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Nov 17 2017 Remi Collet <remi@fedoraproject.org> - 1.10.2-1
- update to 1.10.2

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon May 22 2017 Remi Collet <remi@fedoraproject.org> - 1.10.1-1
- update to 1.10.1
- provide php-composer(pear/mail_mime)

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Sep 14 2015 Remi Collet <remi@fedoraproject.org> - 1.10.0-1
- update to 1.10.0

* Thu Aug  6 2015 Remi Collet <remi@fedoraproject.org> - 1.9.0-1
- update to 1.9.0

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.8.9-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.8.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed May 14 2014 Remi Collet <remi@fedoraproject.org> - 1.8.9-1
- update to 1.8.9

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.8.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Jul  5 2013 Remi Collet <remi@fedoraproject.org> - 1.8.8-1
- Version 1.8.8 (stable) - API 1.4.3 (stable)

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.8.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Dec 27 2012 Remi Collet <remi@fedoraproject.org> - 1.8.7-1
- Version 1.8.7 (stable) - API 1.4.3 (stable)

* Tue Oct 23 2012 Remi Collet <remi@fedoraproject.org> - 1.8.6-1
- Version 1.8.6 (stable) - API 1.4.3 (stable)

* Tue Aug 14 2012 Remi Collet <remi@fedoraproject.org> - 1.8.5-3
- rebuilt for new pear_testdir

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.8.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sun Jun 10 2012 Remi Collet <remi@fedoraproject.org> - 1.8.5-1
- Version 1.8.5 (stable) - API 1.4.3 (stable)

* Fri May 18 2012 Remi Collet <remi@fedoraproject.org> - 1.8.4-1
- Version 1.8.4 (stable) - API 1.4.2 (stable)

* Mon Mar 12 2012 Remi Collet <Fedora@FamilleCollet.com> 1.8.3-1
- Version 1.8.3 (stable) - API 1.4.1 (stable)

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.8.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Thu Aug 11 2011 Remi Collet <Fedora@FamilleCollet.com> 1.8.2-1
- Version 1.8.2 (stable) - API 1.4.1 (stable)

* Sun Apr 17 2011 Remi Collet <Fedora@FamilleCollet.com> 1.8.1-3
- doc in /usr/share/doc/pear

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.8.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Dec  1 2010 Remi Collet <Fedora@FamilleCollet.com> - 1.8.1-1
- Version 1.8.1 (stable) - API 1.4.1 (stable)
- use %%{pear_name} macro
- define timezone during build
- run tests suite in %%check
- requires php-mbstring

* Thu Jul 29 2010 Remi Collet <Fedora@FamilleCollet.com> - 1.8.0-1
- update to new upstream version (Version 1.8.0 - API 1.4.1)
- review summary and description (from upstream)

* Sat Apr 17 2010 Remi Collet <Fedora@FamilleCollet.com> - 1.7.0-1
- update to new upstream version (Version 1.7.0 - API 1.4.0)

* Tue Mar 23 2010 Remi Collet <Fedora@FamilleCollet.com> - 1.6.2-1
- update to new upstream version (Version 1.6.2 - API 1.4.0)

* Tue Mar 09 2010 Remi Collet <Fedora@FamilleCollet.com> - 1.6.1-1
- update to new upstream version (Version 1.6.1 - API 1.4.0)

* Sat Jan 30 2010 Remi Collet <Fedora@FamilleCollet.com> - 1.6.0-1
- update to new upstream version (Version 1.6.0 - API 1.4.0)
- generate CHANGELOG from package.xml

* Wed Dec 30 2009 Remi Collet <Fedora@FamilleCollet.com> - 1.5.3-1
- update to new upstream version
- remove circular dependency on Mail_mimeDecode
- rename Mail_Mime.xml to php-pear-Mail-Mime.xml
- fix License (BSD, not PHP, since 1.4.0)
- fix missing URL

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Aug 28 2008 Tom "spot" Callaway <tcallawa@redhat.com> 1.5.2-4
- fix license tag

* Thu Apr  3 2008 Brandon Holbrook <fedora at theholbrooks.org> 1.5.2-3
- Add Requirement for Mail_mimeDecode

* Wed May 16 2007 Brandon Holbrook <fedora at theholbrooks.org> 1.5.2-2
- Add Requirement for pear-1.6.0

* Wed May 16 2007 Brandon Holbrook <fedora at theholbrooks.org> 1.5.2-1
- Upgraded to 1.5.2

* Wed May 16 2007 Brandon Holbrook <fedora at theholbrooks.org> 1.4.0-1
- Upgraded to 1.4.0

* Wed Sep  6 2006 Brandon Holbrook <fedora at theholbrooks.org> 1.3.1-8
- Remove quotes from 'install' in %%post section (rpmlint has been fixed)
- More specific BR: php-pear EVR

* Tue Sep  5 2006 Brandon Holbrook <fedora at theholbrooks.org> 1.3.1-7
- New PEAR packaging standards

* Wed Jun 28 2006 Brandon Holbrook <fedora at theholbrooks.org> 1.3.1-6
- Replaced version dependency for BuildRequires: php-pear :)

* Wed Jun 28 2006 Brandon Holbrook <fedora at theholbrooks.org> 1.3.1-5
- Added Requires: php
- Removed version dependencies for php-pear(PEAR)
- Fixed incorrect URL line

* Tue Jun 27 2006 Brandon Holbrook <fedora at theholbrooks.org> 1.3.1-4
- Added comment about 'install' in %%post

* Tue Jun 27 2006 Brandon Holbrook <fedora at theholbrooks.org> 1.3.1-3
- Added php-pear version dependencies for (post) and (postun)
- Updated defattr
- Renamed from php-pear-Mail_Mime to php-pear-Mail-Mime
- Took ownership of /usr/share/pear/Mail/

* Mon Jun 26 2006 Brandon Holbrook <fedora at theholbrooks.org> 1.3.1-2
- inserted newlines into description

* Mon Jun 26 2006 Brandon Holbrook <fedora at theholbrooks.org> 1.3.1-1
- initial RPM borrowed HEAVILY from php-pear-Mail
