# fedora/remirepo spec file for php-pear-Net-Socket
#
# Copyright (c) 2006-2023 Remi Collet
# License: CC-BY-SA-4.0
# http://creativecommons.org/licenses/by-sa/4.0/
#
# Please, preserve the changelog entries
#
%{!?__pear: %global __pear %{_bindir}/pear}
%global pear_name Net_Socket

Name:           php-pear-Net-Socket
Version:        1.2.2
Release:        19%{?dist}
Summary:        Network Socket Interface

License:        BSD-2-Clause
URL:            http://pear.php.net/package/Net_Socket
Source0:        http://pear.php.net/get/%{pear_name}-%{version}.tgz

BuildArch:      noarch
BuildRequires:  php(language) >= 5.4
BuildRequires:  php-pear >= 1:1.10.1

Requires(post): %{__pear}
Requires(postun): %{__pear}
Requires:       php(language) >= 5.4
Requires:       php-pear(PEAR) >= 1.10.1
Requires:       php-date

Provides:       php-pear(%{pear_name}) = %{version}
Provides:       php-composer(pear/net_socket) = %{version}


%description
Net_Socket is a class interface to TCP sockets.  It provides blocking
and non-blocking operation, with different reading and writing modes
(byte-wise, block-wise, line-wise and special formats like network
byte-order ip addresses).



%prep
%setup -q -c
cd %{pear_name}-%{version}
# package.xml is V2
mv ../package.xml %{name}.xml


%build
cd %{pear_name}-%{version}
# Empty build section, most likely nothing required.


%install
cd Net_Socket-%{version}
%{__pear} install --nodeps --packagingroot %{buildroot} %{name}.xml

# Clean up unnecessary files
rm -rf %{buildroot}%{pear_metadir}/.??*

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
%{pear_phpdir}/Net
%{pear_xmldir}/%{name}.xml
%{pear_docdir}/%{pear_name}


%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.2-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.2-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.2-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.2-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.2-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Apr 26 2023 Remi Collet <remi@remirepo.net> 1.2.2-14
- use SPDX license ID

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.2-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.2-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.2-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Apr 14 2017 Remi Collet <remi@remirepo.net> 1.2.2-1
- update to 1.2.2

* Thu Apr  6 2017 Remi Collet <remi@remirepo.net> 1.2.1-1
- update to 1.2.1 (no change)
- add documentation

* Thu Apr  6 2017 Remi Collet <remi@remirepo.net> 1.2.0-1
- update to 1.2.0 (no change)
- license changed to BSD

* Thu Mar  9 2017 Remi Collet <remi@remirepo.net> 1.1.0-2
- update to 1.1.0
- raise dependency on PHP 5.4
- raise dependency on PEAR 1.10.1
- add spec file license header
- add composer virtual provides

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.14-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.14-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.14-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.14-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.14-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sat May 25 2013 Remi Collet <remi@fedoraproject.org> 1.0.14-1
- Version 1.0.14 (stable) - API 1.0.10 (stable)

* Thu May 23 2013 Remi Collet <Fedora@FamilleCollet.com> 1.0.13-1
- Version 1.0.13 (stable) - API 1.0.10 (stable)

* Fri May 17 2013 Remi Collet <Fedora@FamilleCollet.com> 1.0.12-1
- Version 1.0.12 (stable) - API 1.0.10 (stable)

* Thu May 16 2013 Remi Collet <Fedora@FamilleCollet.com> 1.0.11-1
- Version 1.0.11 (stable) - API 1.0.10 (stable)

* Tue Feb 19 2013 Remi Collet <remi@fedoraproject.org> - 1.0.10-6
- fix metadata location

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.10-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.10-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.10-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sat Oct 16 2010 Remi Collet <Fedora@FamilleCollet.com> 1.0.10-1
- Version 1.0.10 (stable) - API 1.0.9 (stable) - QA release
- set timezone during build

* Sat May 22 2010 Remi Collet <Fedora@FamilleCollet.com> 1.0.9-4
- spec cleanup
- rename Net_Socket.xml to php-pear-Net-Socket.xml

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.9-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sat Jul 12 2008 Remi Collet <Fedora@FamilleCollet.com> 1.0.9-1
- update to 1.0.9

* Fri Jun 13 2008 Jon Stanley <jonstanley@gmail.com> - 1.0.8-2
- Rebuild

* Tue May 08 2007 Remi Collet <Fedora@FamilleCollet.com> 1.0.8-1
- update to 1.0.8

* Sat Mar 31 2007 Remi Collet <Fedora@FamilleCollet.com> 1.0.7-1
- remove PEAR from sumnary
- update to 1.0.7
- spec cleanup
- add generated CHANGELOG

* Fri Sep 08 2006 Remi Collet <Fedora@FamilleCollet.com> 1.0.6-5
- last template.spec

* Sun Sep 03 2006 Remi Collet <Fedora@FamilleCollet.com> 1.0.6-4
- new and simpler %%prep and %%install

* Sat Sep 02 2006 Remi Collet <Fedora@FamilleCollet.com> 1.0.6-3
- install Licence in prep
- use new macros from /etc/rpm/macros.pear
- own /usr/share/pear/Net
- require php >= 4.3.0 (info from PHP_CompatInfo)

* Sat May 20 2006 Remi Collet <Fedora@FamilleCollet.com> 1.0.6-2
- Require pear >= 1.4.9
- bundle the v3.01 PHP LICENSE file
- use --packagingroot (instead of -R)
- check from install to check (as in php-pear)

* Sat May 06 2006 Remi Collet <Fedora@FamilleCollet.com> 1.0.6-1
- spec for extras
- use %%{_datadir}/pear/.pkgxml for XML (Bug #190252)

* Thu Apr 06 2006 Remi Collet <rpms@FamilleCollet.com> 1.0.6-2.fc{3,4,5}.remi
- change /var/lib/pear to %%{_libdir}/php/pear for XML (as in extras for FC5)
- spec cleanning

* Sat Jan  7 2006 Remi Collet <remi.collet@univ-reims.fr> 1.0.6-1.fc{3,4}.remi
- initial RPM
