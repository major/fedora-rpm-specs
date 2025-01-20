%{!?php_inidir:  %global php_inidir  %{_sysconfdir}/php.d}
%{!?__php:       %global __php       %{_bindir}/php}
%{!?_pkgdocdir:  %global _pkgdocdir  %{_docdir}/%{name}-%{version}}

# The change to redhat-rpm-config to force symbols to be defined breaks all PHP extensions
# c.f.: https://src.fedoraproject.org/rpms/redhat-rpm-config/c/078af192613e1beec34824a94dc5f6feeeea1568
# c.f.: https://lists.fedoraproject.org/archives/list/devel@lists.fedoraproject.org/message/7EHQUO6JIFRE4KIQQMFVQCAQ72NLKARO/
%undefine _strict_symbol_defs_build

# The change to gcc10 to default to -fno-common breaks libvirt-php
# c.f.: https://src.fedoraproject.org/rpms/redhat-rpm-config/c/3e759e70ac919595f45c1dc80c19fc8d3499b459
# c.f.: https://lists.fedoraproject.org/archives/list/devel@lists.fedoraproject.org/message/MXKIKAV4GMS22TGAO5Y6ROQ76EG4GKW2/
%define _legacy_common_support 1

%global  req_libvirt_version 1.2.13
%global  extname             libvirt-php
%global  ini_name            40-%{extname}.ini

Name:		php-libvirt
Version:	0.5.8
Release:	2%{?dist}
Summary:	PHP language bindings for Libvirt

# libvirt-php is under the same terms as libvirt
# Automatically converted from old format: LGPLv2+ - review is highly recommended.
License:	LicenseRef-Callaway-LGPLv2+
URL:		http://libvirt.org/php
Source0:	http://libvirt.org/sources/php/libvirt-php-%{version}.tar.xz

ExcludeArch:    %{ix86}

BuildRequires:	make
BuildRequires:	php-devel >= 7.0
BuildRequires:	libvirt-devel >= %{req_libvirt_version}
BuildRequires:	libxml2-devel
BuildRequires:	libxslt
BuildRequires:	xhtml1-dtds

Requires:	libvirt >= %{req_libvirt_version}
Requires:	php(zend-abi) = %{php_zend_api}
Requires:	php(api) = %{php_core_api}

# Filter shared private - always as libvirt-php.so is a private extension
%global __provides_exclude_from ^%{_libdir}/.*\\.so$


%description
PHP language bindings for Libvirt API.
For more details see: http://www.libvirt.org/php/


%package doc
Summary:	Documentation for %{name}
BuildArch:	noarch
Requires:	%{name} = %{version}-%{release}

%description doc
PHP language bindings for Libvirt API.
For more details see: http://www.libvirt.org/php/ http://www.php.net/

This package contains the documentation for php-libvirt.


%prep
%autosetup -n %{extname}-%{version} -p1


%build
%configure \
  --with-html-dir=%{_docdir} \
  --with-html-subdir=$(echo %{_pkgdocdir} | sed -e 's|^%{_docdir}/||')/html \
  --libdir=%{php_extdir}
%make_build


%install
%make_install
chmod +x %{buildroot}%{php_extdir}/%{extname}.so

if [ -f %{buildroot}%{php_inidir}/%{extname}.ini ]; then
    mv %{buildroot}%{php_inidir}/%{extname}.ini \
       %{buildroot}%{php_inidir}/%{ini_name}
else
  install -Dpm 644 src/libvirt-php.ini %{buildroot}%{php_inidir}/%{ini_name}
fi

# Erase unnecessary libtool archive file
rm %{buildroot}%{php_extdir}/%{extname}.la


%check
: simple module load test
%{__php} --no-php-ini \
    --define extension=%{buildroot}%{php_extdir}/%{extname}.so \
    --modules | grep libvirt


%files
%license COPYING
%dir %{_pkgdocdir}
%{php_extdir}/%{extname}.so
%config(noreplace) %{php_inidir}/%{ini_name}


%files doc
%{_pkgdocdir}/html


%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Oct 14 2024 Remi Collet <remi@fedoraproject.org> - 0.5.8-1
- update to 0.5.8
- rebuild for https://fedoraproject.org/wiki/Changes/php84

* Wed Sep 04 2024 Miroslav Suchý <msuchy@redhat.com> - 0.5.7-6
- convert license to SPDX

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.7-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Apr 12 2024 Remi Collet <remi@remirepo.net> - 0.5.7-4
- drop 32-bit support
  https://fedoraproject.org/wiki/Changes/php_no_32_bit

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Tue Oct 03 2023 Remi Collet <remi@remirepo.net> - 0.5.7-1
- update to 0.5.7
- rebuild for https://fedoraproject.org/wiki/Changes/php83
- raise dependency on PHP 7.0

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.6-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Oct 05 2022 Remi Collet <remi@remirepo.net> - 0.5.6-3
- rebuild for https://fedoraproject.org/wiki/Changes/php82

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jun 15 2022 Neal Gompa <ngompa@fedoraproject.org> - 0.5.6-1
- Upgrade to 0.5.6

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.5-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Oct 28 2021 Remi Collet <remi@remirepo.net> - 0.5.5-6
- rebuild for https://fedoraproject.org/wiki/Changes/php81

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Thu Mar  4 2021 Remi Collet <remi@remirepo.net> - 0.5.5-4
- rebuild for https://fedoraproject.org/wiki/Changes/php80

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sat Feb 08 2020 Neal Gompa <ngompa13@gmail.com> - 0.5.5-1
- Upgrade to 0.5.5

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.4-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Oct 04 2019 Remi Collet <remi@remirepo.net> - 0.5.4-9
- rebuild for https://fedoraproject.org/wiki/Changes/php74

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.4-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.4-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Oct 11 2018 Remi Collet <remi@remirepo.net> - 0.5.4-6
- Rebuild for https://fedoraproject.org/wiki/Changes/php73

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 25 2018 Neal Gompa <ngompa13@gmail.com> - 0.5.4-3
- Disable forcing symbols to be defined at link time to fix build

* Tue Oct 03 2017 Remi Collet <remi@fedoraproject.org> - 0.5.4-2
- rebuild for https://fedoraproject.org/wiki/Changes/php72

* Sat Aug 05 2017 Neal Gompa <ngompa13@gmail.com> - 0.5.4-1
- Upgrade to 0.5.4

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Thu May 11 2017 Neal Gompa <ngompa13@gmail.com> - 0.5.3-2
- Fix license tag to match actual source license

* Thu May 11 2017 Neal Gompa <ngompa13@gmail.com> - 0.5.3-1
- Upgrade to 0.5.3

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Nov 14 2016 Remi Collet <remi@fedoraproject.org> - 0.5.2-3
- rebuild for https://fedoraproject.org/wiki/Changes/php71

* Mon Jun 27 2016 Remi Collet <remi@fedoraproject.org> - 0.5.2-2
- rebuild for https://fedoraproject.org/wiki/Changes/php70

* Sat Jun 11 2016 Neal Gompa <ngompa13@gmail.com> - 0.5.2-1
- Upgrade to 0.5.2

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.8-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.8-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.8-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Thu Jun 19 2014 Remi Collet <rcollet@redhat.com> - 0.4.8-3
- rebuild for https://fedoraproject.org/wiki/Changes/Php56
- add numerical prefix to extension configuration file

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon Jan  6 2014 Remi Collet <remi@fedoraproject.org> - 0.4.8-1
- update to 0.4.8
- spec cleanups

* Thu Dec 12 2013 Ville Skyttä <ville.skytta@iki.fi> - 0.4.5-6
- Install docs to %%{_pkgdocdir} where available (#994035).
- Include COPYING in main package.
- Disable parallel build.

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Mar 22 2013 Remi Collet <rcollet@redhat.com> - 0.4.5-4
- rebuild for http://fedoraproject.org/wiki/Features/Php55

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jan 19 2012 Remi Collet <remi@fedoraproject.org> - 0.4.5-1
- update to 0.4.5 (upstream is libvirt-php)
- build against php 5.4.0, with patch
- add filter to fix private-shared-object-provides
- add %%check for php extension
- use macro from latest php (php_inidir, php_extdir)
- requires php ABI

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Aug 22 2011 Michal Novotny <minovotn@redhat.com> - 0.4.4
- Several bugfixes for VNC and updated SPEC file

* Thu Aug 11 2011 Michal Novotny <minovotn@redhat.com> - 0.4.3
- Rebase to 0.4.3 from master branch

* Tue Apr 19 2011 Michal Novotny <minovotn@redhat.com> - 0.4.1-5
- Minor memory leak fixes
- Several bug fixes

* Mon Apr 11 2011 Michal Novotny <minovotn@redhat.com> - 0.4.1-4
- Add new storagepool API functions
- Add optional xPath argument for *_get_xml_desc() functions
- Add new network API functions
- Add new API functions to add/remove disks

* Wed Mar 23 2011 Michal Novotny <minovotn@redhat.com> - 0.4.1-3
- Add connection information function
- Add coredump support
- Add snapshots support
- Improve error reporting for destructors

* Thu Mar 10 2011 Michal Novotny <minovotn@redhat.com> - 0.4.1-2
- Changes done to comply with Fedora package policy

* Tue Feb  8 2011 Michal Novotny <minovotn@redhat.com> - 0.4.1
- Initial commit (from github)
