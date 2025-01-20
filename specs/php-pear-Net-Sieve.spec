# remirepo/fedora spec file for php-pear-Net-Sieve
#
# Copyright (c) 2008-2024 Remi Collet
# Copyright (c) 2006-2008 Brandon Holbrook
#
# License: MIT
# http://opensource.org/licenses/MIT
#
# Please, preserve the changelog entries
#
%{!?__pear:       %global __pear       %{_bindir}/pear}
%global pear_name Net_Sieve

Name:           php-pear-Net-Sieve
Version:        1.4.7
Release:        3%{?dist}
Summary:        Handles talking to a sieve server

License:        BSD-2-Clause
URL:            http://pear.php.net/package/Net_Sieve
Source0:        http://pear.php.net/get/%{pear_name}-%{version}.tgz

BuildArch:      noarch
BuildRequires:  php-pear

Requires(post): %{__pear}
Requires(postun): %{__pear}
Requires:       php-pear(Net_Socket) >= 1.0
Requires:       php-pear(Auth_SASL) >= 1.0

Provides:       php-pear(%{pear_name}) = %{version}
Provides:       php-composer(pear/net_sieve) = %{version}
# The changes from the fork are merged
Provides:       php-composer(roundcube/net_sieve) = 1.5.0


%description
This package provides an API to talk to servers implementing the 
managesieve protocol. It can be used to install and remove sieve
scripts, mark them active etc.


%prep
%setup -q -c
cd %{pear_name}-%{version}
mv ../package.xml %{name}.xml


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
if [ $1 -eq 0 ]; then
    %{__pear} uninstall --nodeps --ignore-errors --register-only \
        %{pear_name} >/dev/null || :
fi


%files
%doc %{pear_testdir}/%{pear_name}
%{pear_xmldir}/%{name}.xml
%{pear_phpdir}/Net


%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Tue Apr  9 2024 Remi Collet <remi@remirepo.net> - 1.4.7-1
- update to 1.4.7

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.6-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Tue Dec  6 2022 Remi Collet <remi@remirepo.net> - 1.4.6-1
- update to 1.4.6

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Thu Apr 29 2021 Remi Collet <remi@remirepo.net> - 1.4.5-1
- update to 1.4.5

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Sep 10 2018 Remi Collet <remi@remirepo.net> - 1.4.4-1
- update to 1.4.4

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sun Mar  4 2018 Remi Collet <remi@remirepo.net> - 1.4.3-1
- update to 1.4.3

* Wed Feb 14 2018 Remi Collet <remi@remirepo.net> - 1.4.2-1
- update to 1.4.2 (no change)
- install tests as documentation

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat May 27 2017 Remi Collet <remi@remirepo.net> - 1.4.1-1
- update to 1.4.1

* Mon May 22 2017 Remi Collet <remi@fedoraproject.org> - 1.4.0-1
- update to 1.4.0
- drop patches merged upstream

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Dec 28 2015 Remi Collet <remi@fedoraproject.org> - 1.3.4-4
- version of php-composer(roundcube/net_sieve) is 1.5.0

* Sat Dec 19 2015 Remi Collet <remi@fedoraproject.org> - 1.3.4-3
- add patch from https://github.com/roundcube/Net_Sieve
  which fix compatibility with PHP 7 and avoid the fork
- also provide php-composer(roundcube/net_sieve)

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Jan 21 2015 Remi Collet <remi@fedoraproject.org> - 1.3.4-1
- Version 1.3.4 (stable) - API 1.3.0 (stable)
- add provides php-composer(pear/net_sieve)

* Fri Sep 26 2014 Remi Collet <remi@fedoraproject.org> - 1.3.3-1
- Version 1.3.3 (stable) - API 1.3.0 (stable)

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue Feb 19 2013 Remi Collet <remi@fedoraproject.org> - 1.3.2-6
- fix metadata location

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Tue Aug 14 2012 Remi Collet <remi@fedoraproject.org> - 1.3.2-4
- rebuilt for new pear_testdir

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Aug 08 2011 Remi Collet <Fedora@FamilleCollet.com> 1.3.2-1
- Version 1.3.2 (stable) - API 1.3.0 (stable)

* Sat Aug 06 2011 Remi Collet <Fedora@FamilleCollet.com> 1.3.1-1
- Version 1.3.1 (stable) - API 1.3.0 (stable)

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Jun 14 2010 Remi Collet <Fedora@FamilleCollet.com> 1.3.0-1
- Version 1.3.0 (stable) - API 1.3.0 (stable)

* Mon Jun 14 2010 Remi Collet <Fedora@FamilleCollet.com> 1.2.2-1
- update to 1.2.2 - API 1.2.0

* Tue Apr 20 2010 Remi Collet <Fedora@FamilleCollet.com> 1.2.1-1
- update to 1.2.1 - API 1.2.0

* Sat Apr 03 2010 Remi Collet <Fedora@FamilleCollet.com> 1.2.0-1
- update to 1.2.0 - API 1.2.0

* Wed Jul 29 2009 Remi Collet <Fedora@FamilleCollet.com> 1.1.7-1
- update to 1.1.7 (bugfix)
- move Net_Sieve.xml to php-pear-Net-Sieve.xml

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Tue May 27 2008 Remi Collet <Fedora@FamilleCollet.com> 1.1.6-1
- update to 1.1.6
- add generated CHANGELOG

* Sat Dec 30 2006 Brandon Holbrook <fedora at theholbrooks.org> 1.1.5-2
- Cleaned up spec file to latest pear template
- Changed license to BSD

* Fri Dec 29 2006 Brandon Holbrook <fedora at theholbrooks.org> 1.1.5-1
- initial RPM

