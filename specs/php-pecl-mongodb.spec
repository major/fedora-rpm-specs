# Fedora spec file for php-pecl-mongodb
# without SCL compatibility, from
#
# remirepo spec file for php-pecl-mongodb
#
# Copyright (c) 2015-2024 Remi Collet
# License: CC-BY-SA-4.0
# http://creativecommons.org/licenses/by-sa/4.0/
#
# Please, preserve the changelog entries
#

%global pecl_name         mongodb
# After 40-smbclient.ini, see https://jira.mongodb.org/browse/PHPC-658
%global ini_name          50-%{pecl_name}.ini

%global upstream_version  1.20.1
#global upstream_prever   RC1
#global upstream_lower    ~rc1
%global sources           %{pecl_name}-%{upstream_version}%{?upstream_prever}

# Required versions from config.m4
%global minimal_libmongo  1.28.1
%global minimal_libcrypt  1.11.0

# Build dependencies
%global system_libmongo   1.28.1
%global system_libcrypt   1.11.0

Summary:        MongoDB driver for PHP
Name:           php-pecl-%{pecl_name}
Version:        %{upstream_version}%{?upstream_lower}
Release:        2%{?dist}
License:        Apache-2.0
URL:            https://pecl.php.net/package/%{pecl_name}
Source0:        https://pecl.php.net/get/%{pecl_name}-%{upstream_version}%{?upstream_prever}.tgz

ExcludeArch:    %{ix86}

BuildRequires:  gcc
BuildRequires:  php-devel >= 7.4
BuildRequires:  php-pear
BuildRequires:  php-json
BuildRequires:  pkgconfig(libbson-1.0)    >= %{system_libmongo}
BuildRequires:  pkgconfig(libmongoc-1.0)  >= %{system_libmongo}
BuildRequires:  pkgconfig(libmongocrypt)  >= %{system_libcrypt}

Requires:       php(zend-abi) = %{php_zend_api}
Requires:       php(api) = %{php_core_api}
Requires:       php-json%{?_isa}

# Don't provide php-mongodb which is the pure PHP library
Provides:       php-pecl(%{pecl_name})         = %{version}
Provides:       php-pecl(%{pecl_name})%{?_isa} = %{version}


%description
The purpose of this driver is to provide exceptionally thin glue between
MongoDB and PHP, implementing only fundemental and performance-critical
components necessary to build a fully-functional MongoDB driver.


%prep
%setup -q -c

# Don't install/register tests and License
sed -e 's/role="test"/role="src"/' \
    -e '/LICENSE/s/role="doc"/role="src"/' \
    -i package.xml

pushd %{sources}

# Check our macro values
grep CHECK_MODULES config.m4
grep -q %{minimal_libmongo} config.m4
grep -q %{minimal_libcrypt} config.m4

# temporary: lower minimal required versions
sed -e 's/%{minimal_libmongo}/%{system_libmongo}/;s/%{minimal_libcrypt}/%{system_libcrypt}/' -i config.m4

# Sanity check, really often broken
extver=$(sed -n '/#define PHP_MONGODB_VERSION /{s/.* "//;s/".*$//;p}' phongo_version.h)
if test "x${extver}" != "x%{upstream_version}%{?upstream_prever}"; then
   : Error: Upstream extension version is ${extver}, expecting %{upstream_version}%{?upstream_prever}.
   exit 1
fi

popd

# Create configuration file
cat << 'EOF' | tee %{ini_name}
; Enable %{summary} extension module
extension=%{pecl_name}.so

; Configuration
;mongodb.debug=''
EOF


%build
cd %{sources}
%{__phpize}
sed -e 's/INSTALL_ROOT/DESTDIR/' -i build/Makefile.global

# Ensure we use system library
# Need to be removed only after phpize because of m4_include
rm -r src/libmongoc*

%configure \
    --with-php-config=%{__phpconfig} \
    --with-mongodb-system-libs \
    --with-mongodb-client-side-encryption \
    --enable-mongodb

%make_build


%install
cd %{sources}

: Install the extension
%make_install

: Install config file
install -D -m 644 ../%{ini_name} %{buildroot}%{php_inidir}/%{ini_name}

: Install XML package description
install -D -m 644 ../package.xml %{buildroot}%{pecl_xmldir}/%{name}.xml

: Install the Documentation
for i in $(grep 'role="doc"' ../package.xml | sed -e 's/^.*name="//;s/".*$//')
do install -Dpm 644 $i %{buildroot}%{pecl_docdir}/%{pecl_name}/$i
done


%check
cd %{sources}
OPT="-n"

: Minimal load test for the extension
%{__php} $OPT \
    --define extension=%{buildroot}%{php_extdir}/%{pecl_name}.so \
    --modules | grep '^%{pecl_name}$'


%files
%license %{sources}/LICENSE
%doc %{pecl_docdir}/%{pecl_name}
%{pecl_xmldir}/%{name}.xml

%config(noreplace) %{php_inidir}/%{ini_name}
%{php_extdir}/%{pecl_name}.so


%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.20.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Nov 28 2024 Remi Collet <remi@remirepo.net> - 1.20.1-1
- update to 1.20.1

* Mon Oct 28 2024 Remi Collet <remi@fedoraproject.org> - 1.20.0-3
- modernize the spec file

* Mon Oct 14 2024 Remi Collet <remi@fedoraproject.org> - 1.20.0-2
- rebuild for https://fedoraproject.org/wiki/Changes/php84

* Wed Sep 25 2024 Remi Collet <remi@remirepo.net> - 1.20.0-1
- update to 1.20.0
- raise dependency on libbson and libmongc 1.28.0
- raise dependency on libmongocrypt 1.11.0

* Mon Sep  9 2024 Remi Collet <remi@remirepo.net> - 1.19.4-1
- update to 1.19.4
- raise dependency on libbson and libmongc 1.27.6
- raise dependency on libmongocrypt 1.10.1

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.19.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jun  6 2024 Remi Collet <remi@remirepo.net> - 1.19.2-1
- update to 1.19.2 (no change)

* Wed May 29 2024 Remi Collet <remi@remirepo.net> - 1.19.1-1
- update to 1.19.1

* Tue May 14 2024 Remi Collet <remi@remirepo.net> - 1.19.0-1
- update to 1.19.0
- raise dependency on libbson and libmongc 1.27.0
- raise dependency on libmongocrypt 1.10.0

* Fri Apr 12 2024 Remi Collet <remi@remirepo.net> - 1.18.1-1
- update to 1.18.1 (no change)

* Thu Mar 28 2024 Remi Collet <remi@remirepo.net> - 1.18.0-1
- update to 1.18.0

* Tue Mar 19 2024 Remi Collet <remi@remirepo.net> - 1.17.3-1
- update to 1.17.3 (no change)
- drop 32-bit support

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.17.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.17.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Dec 21 2023 Remi Collet <remi@remirepo.net> - 1.17.2-1
- update to 1.17.2

* Wed Dec  6 2023 Remi Collet <remi@remirepo.net> - 1.17.1-1
- update to 1.17.1

* Wed Nov 15 2023 Remi Collet <remi@remirepo.net> - 1.17.0-1
- update to 1.17.0
- raise dependency on PHP 7.4
- raise dependency on libmongoc 1.25.1
- raise dependency on libmongocrypt 1.8.2
- open https://github.com/mongodb/mongo-php-driver/pull/1490 drop ICU information

* Tue Oct 03 2023 Remi Collet <remi@remirepo.net> - 1.16.2-2
- rebuild for https://fedoraproject.org/wiki/Changes/php83

* Mon Aug 21 2023 Remi Collet <remi@remirepo.net> - 1.16.2-1
- update to 1.16.2

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.16.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Mon Jun 26 2023 Remi Collet <remi@remirepo.net> - 1.16.1-1
- update to 1.16.1 (no change)

* Thu Jun 22 2023 Remi Collet <remi@remirepo.net> - 1.16.0-1
- update to 1.16.0

* Tue May 16 2023 Remi Collet <remi@remirepo.net> - 1.15.3-1
- update to 1.15.3

* Tue Apr 25 2023 Remi Collet <remi@remirepo.net> - 1.15.2-2
- build out of sources tree

* Tue Apr 25 2023 Remi Collet <remi@remirepo.net> - 1.15.2-1
- update to 1.15.2 (no change)

* Thu Feb  9 2023 Remi Collet <remi@remirepo.net> - 1.15.1-1
- update to 1.15.1
- cleanup spec macros
- use spdx license id

* Wed Nov 23 2022 Remi Collet <remi@remirepo.net> - 1.15.0-1
- update to 1.15.0
- raise dependency on libbson and libmongoc 1.23.1

* Fri Oct 21 2022 Remi Collet <remi@remirepo.net> - 1.14.2-1
- update to 1.14.2

* Wed Oct 05 2022 Remi Collet <remi@remirepo.net> - 1.14.1-2
- rebuild for https://fedoraproject.org/wiki/Changes/php82

* Fri Sep 16 2022 Remi Collet <remi@remirepo.net> - 1.14.1-1
- update to 1.14.1

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.14.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jul 18 2022 Remi Collet <remi@remirepo.net> - 1.14.0-1
- update to 1.14.0
- raise dependency on libbson and libmongoc 1.22.0
- raise dependency on libmongocrypt 1.5.0

* Thu Mar 24 2022 Remi Collet <remi@remirepo.net> - 1.13.0-1
- update to 1.12.0
- raise dependency on libbson and libmongoc 1.21

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.12.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Dec 15 2021 Remi Collet <remi@remirepo.net> - 1.12.0-1
- update to 1.12.0
- raise dependency on libbson and libmongoc 1.20.0
- raise dependency on libmongocrypt 1.3.0
- raise dependency on PHP 7.2

* Wed Nov  3 2021 Remi Collet <remi@remirepo.net> - 1.11.1-1
- update to 1.11.1 (no change)

* Tue Nov  2 2021 Remi Collet <remi@remirepo.net> - 1.11.0-1
- update to 1.11.0
- raise dependency on libbson and libmongoc 1.19.1

* Thu Oct 28 2021 Remi Collet <remi@remirepo.net> - 1.10.0-3
- rebuild for https://fedoraproject.org/wiki/Changes/php81
- add patch for PHP 8.1.0beta1 from
  https://github.com/mongodb/mongo-php-driver/pull/1240

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon Jul 19 2021 Remi Collet <remi@remirepo.net> - 1.10.0-1
- update to 1.10.0

* Tue Jul 13 2021 Remi Collet <remi@remirepo.net> - 1.9.2-1
- update to 1.9.2

* Thu Apr  8 2021 Remi Collet <remi@remirepo.net> - 1.9.1-1
- update to 1.9.1

* Thu Mar  4 2021 Remi Collet <remi@remirepo.net> - 1.9.0-3
- rebuild for https://fedoraproject.org/wiki/Changes/php80

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Nov 25 2020 Remi Collet <remi@remirepo.net> - 1.9.0-1
- update to 1.9.0

* Thu Nov  5 2020 Remi Collet <remi@remirepo.net> - 1.8.2-1
- update to 1.8.2 (no change)

* Tue Oct  6 2020 Remi Collet <remi@remirepo.net> - 1.8.1-1
- update to 1.8.1

* Mon Aug 10 2020 Remi Collet <remi@remirepo.net> - 1.8.0-1
- update to 1.8.0

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.0~rc1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jul 17 2020 Remi Collet <remi@remirepo.net> - 1.8.0~rc1-1
- update to 1.8.0RC1

* Thu Jun 11 2020 Remi Collet <remi@remirepo.net> - 1.8.0~beta2-1
- update to 1.8.0beta2

* Wed Apr 15 2020 Remi Collet <remi@remirepo.net> - 1.8.0~beta1-1
- update to 1.8.0beta1
- raise dependency on libbson and libmongoc 1.17
- raise dependency on PHP 7

* Tue Mar 24 2020 Remi Collet <remi@remirepo.net> - 1.7.4-1
- update to 1.7.4 (no change)

* Tue Feb 25 2020 Remi Collet <remi@remirepo.net> - 1.7.3-1
- update to 1.7.3 (no change)
- raise dependency on libbson and libmongoc 1.16.2

* Thu Feb 13 2020 Remi Collet <remi@remirepo.net> - 1.7.2-1
- update to 1.7.2 (no change)
- raise dependency on libmongocrypt 1.0.3

* Wed Feb  5 2020 Remi Collet <remi@remirepo.net> - 1.7.1-1
- update to 1.7.1
- raise dependency on libbson and libmongoc 1.16.1
- add dependency on libmongocrypt

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Dec  6 2019 Remi Collet <remi@remirepo.net> - 1.6.1-1
- update to 1.6.1 (no change)
- raise dependency on libbson and libmongoc 1.15.2

* Thu Oct 03 2019 Remi Collet <remi@remirepo.net> - 1.6.0-2
- rebuild for https://fedoraproject.org/wiki/Changes/php74

* Mon Sep  9 2019 Remi Collet <remi@remirepo.net> - 1.6.0-1
- update to 1.6.0

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Jun 11 2019 Remi Collet <remi@remirepo.net> - 1.5.5-1
- update to 1.5.5

* Tue Jun  4 2019 Remi Collet <remi@remirepo.net> - 1.5.4-1
- update to 1.5.4

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Oct 11 2018 Remi Collet <remi@remirepo.net> - 1.5.3-2
- Rebuild for https://fedoraproject.org/wiki/Changes/php73

* Fri Sep 21 2018 Remi Collet <remi@remirepo.net> - 1.5.3-1
- update to 1.5.3
- raise dependency on libbson and libmongoc 1.13.0

* Fri Aug 17 2018 Remi Collet <remi@remirepo.net> - 1.5.2-1
- update to 1.5.2
- raise dependency on libbson and libmongoc 1.12.0

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Jul  9 2018 Remi Collet <remi@remirepo.net> - 1.5.1-1
- update to 1.5.1

* Wed Jun 27 2018 Remi Collet <remi@remirepo.net> - 1.5.0-1
- update to 1.5.0
- raise dependency on libbson and libmongoc 1.11.0

* Fri Jun  8 2018 Remi Collet <remi@remirepo.net> - 1.4.4-2
- rebuild with libbson and libmongc 1.10.2 (soname back to 0)

* Thu Jun  7 2018 Remi Collet <remi@remirepo.net> - 1.4.4-1
- update to 1.4.4

* Mon May 28 2018 Remi Collet <remi@remirepo.net> - 1.4.3-2
- rebuild with libbson and libmongc 1.10.0

* Thu Apr 19 2018 Remi Collet <remi@remirepo.net> - 1.4.3-1
- update to 1.4.3

* Wed Mar  7 2018 Remi Collet <remi@remirepo.net> - 1.4.2-1
- Update to 1.4.2 (no change)

* Wed Feb 21 2018 Remi Collet <remi@remirepo.net> - 1.4.1-1
- Update to 1.4.1 (stable, no change)

* Fri Feb  9 2018 Remi Collet <remi@remirepo.net> - 1.4.0-1
- Update to 1.4.0 (stable)

* Wed Feb  7 2018 Remi Collet <remi@remirepo.net> - 1.4.0~rc2-1
- Update to 1.4.0RC2

* Fri Dec 22 2017 Remi Collet <remi@remirepo.net> - 1.4.0~rc1-1
- Update to 1.4.0RC1

* Fri Dec 22 2017 Remi Collet <remi@remirepo.net> - 1.4.0~beta1-1
- Update to 1.4.0beta1
- raise dependency on libbson and libmongoc 1.9.0

* Sun Dec  3 2017 Remi Collet <remi@remirepo.net> - 1.3.4-1
- Update to 1.3.4

* Wed Nov 22 2017 Remi Collet <remi@remirepo.net> - 1.3.3-1
- Update to 1.3.3

* Tue Oct 31 2017 Remi Collet <remi@remirepo.net> - 1.3.2-1
- Update to 1.3.2

* Tue Oct 17 2017 Remi Collet <remi@remirepo.net> - 1.3.1-1
- update to 1.3.1 (stable)

* Tue Oct 03 2017 Remi Collet <remi@fedoraproject.org> - 1.3.0-2
- rebuild for https://fedoraproject.org/wiki/Changes/php72

* Wed Sep 20 2017 Remi Collet <remi@remirepo.net> - 1.3.0-1
- update to 1.3.0 (stable)

* Fri Sep 15 2017 Remi Collet <remi@remirepo.net> - 1.3.0~RC1-1
- update to 1.3.0RC1
- raise dependency on libbson and mongo-c-driver 1.8.0
- raise dependency on PHP 5.5

* Fri Aug 11 2017 Remi Collet <remi@remirepo.net> - 1.3.0~beta1-1
- update to 1.3.0beta1
- raise dependency on libbson and mongo-c-driver 1.7.0

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.9-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Thu May  4 2017 Remi Collet <remi@remirepo.net> - 1.2.9-1
- Update to 1.2.9

* Mon Mar 20 2017 Remi Collet <remi@remirepo.net> - 1.2.8-1
- Update to 1.2.8 (no change)

* Wed Mar 15 2017 Remi Collet <remi@remirepo.net> - 1.2.7-1
- Update to 1.2.7

* Wed Mar  8 2017 Remi Collet <remi@remirepo.net> - 1.2.6-1
- Update to 1.2.6

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb  1 2017 Remi Collet <remi@fedoraproject.org> - 1.2.5-1
- update to 1.2.5

* Wed Dec 14 2016 Remi Collet <remi@fedoraproject.org> - 1.2.2-1
- update to 1.2.2

* Thu Dec  8 2016 Remi Collet <remi@fedoraproject.org> - 1.2.1-1
- update to 1.2.1

* Tue Nov 29 2016 Remi Collet <remi@fedoraproject.org> - 1.2.0-1
- update to 1.2.0
- internal dependency on date, json, spl and standard

* Wed Nov 23 2016 Remi Collet <remi@fedoraproject.org> - 1.2.0-0.4.alpha3
- add upstream patch for libbson and mongo-c-driver 1.5.0RC6
- fix FTBFS detected by Koschei

* Mon Nov 14 2016 Remi Collet <remi@fedoraproject.org> - 1.2.0-0.3.alpha3
- rebuild for https://fedoraproject.org/wiki/Changes/php71

* Fri Oct 21 2016 Remi Collet <remi@fedoraproject.org> - 1.2.0-0.2.alpha3
- add upstream patch for libbson and mongo-c-driver 1.5.0RC3
- fix FTBFS detected by Koschei

* Fri Oct 14 2016 Remi Collet <remi@fedoraproject.org> - 1.2.0-0.1.alpha3
- update to 1.2.0alpha3 for libbson and mongo-c-driver 1.5

* Mon Aug 29 2016 Petr Pisar <ppisar@redhat.com> - 1.1.8-4
- Rebuild against libbson-1.4.0 (bug #1361166)

* Tue Jul 19 2016 Remi Collet <remi@fedoraproject.org> - 1.1.8-2
- License is ASL 2.0, from review #1269056

* Wed Jul 06 2016 Remi Collet <remi@fedoraproject.org> - 1.1.8-1
- Update to 1.1.8

* Thu Jun  2 2016 Remi Collet <remi@fedoraproject.org> - 1.1.7-1
- Update to 1.1.7

* Thu Apr  7 2016 Remi Collet <remi@fedoraproject.org> - 1.1.6-1
- Update to 1.1.6

* Thu Mar 31 2016 Remi Collet <remi@fedoraproject.org> - 1.1.5-3
- load after smbclient to workaround
  https://jira.mongodb.org/browse/PHPC-658

* Fri Mar 18 2016 Remi Collet <remi@fedoraproject.org> - 1.1.5-1
- Update to 1.1.5 (stable)

* Thu Mar 10 2016 Remi Collet <remi@fedoraproject.org> - 1.1.4-1
- Update to 1.1.4 (stable)

* Sat Mar  5 2016 Remi Collet <remi@fedoraproject.org> - 1.1.3-1
- Update to 1.1.3 (stable)

* Thu Jan 07 2016 Remi Collet <remi@fedoraproject.org> - 1.1.2-1
- Update to 1.1.2 (stable)

* Thu Dec 31 2015 Remi Collet <remi@fedoraproject.org> - 1.1.1-3
- fix patch for 32bits build
  open https://github.com/mongodb/mongo-php-driver/pull/191

* Sat Dec 26 2015 Remi Collet <remi@fedoraproject.org> - 1.1.1-1
- Update to 1.1.1 (stable)
- add patch for 32bits build,
  open https://github.com/mongodb/mongo-php-driver/pull/185

* Wed Dec 16 2015 Remi Collet <remi@fedoraproject.org> - 1.1.0-1
- Update to 1.1.0 (stable)
- raise dependency on libmongoc >= 1.3.0

* Tue Dec  8 2015 Remi Collet <remi@fedoraproject.org> - 1.0.1-1
- update to 1.0.1 (stable)
- ensure libmongoc >= 1.2.0 and < 1.3 is used

* Fri Oct 30 2015 Remi Collet <remi@fedoraproject.org> - 1.0.0-1
- update to 1.0.0 (stable)

* Tue Oct 27 2015 Remi Collet <remi@fedoraproject.org> - 1.0.0-0.6.RC0
- Update to 1.0.0RC0 (beta)

* Tue Oct  6 2015 Remi Collet <remi@fedoraproject.org> - 1.0.0-0.4-beta2
- drop SCL compatibility for Fedora

* Tue Oct  6 2015 Remi Collet <remi@fedoraproject.org> - 1.0.0-0.3-beta2
- Update to 1.0.0beta2 (beta)

* Fri Sep 11 2015 Remi Collet <remi@fedoraproject.org> - 1.0.0-0.2-beta1
- Update to 1.0.0beta1 (beta)

* Mon Aug 31 2015 Remi Collet <remi@fedoraproject.org> - 1.0.0-0.1.alpha2
- Update to 1.0.0alpha2 (alpha)
- buid with system libmongoc

* Thu May 07 2015 Remi Collet <remi@fedoraproject.org> - 0.6.3-1
- Update to 0.6.3 (alpha)

* Wed May 06 2015 Remi Collet <remi@fedoraproject.org> - 0.6.2-1
- Update to 0.6.2 (alpha)

* Wed May 06 2015 Remi Collet <remi@fedoraproject.org> - 0.6.0-1
- Update to 0.6.0 (alpha)

* Sat Apr 25 2015 Remi Collet <remi@fedoraproject.org> - 0.5.1-1
- Update to 0.5.1 (alpha)

* Thu Apr 23 2015 Remi Collet <remi@fedoraproject.org> - 0.5.0-2
- build with system libbson
- open https://jira.mongodb.org/browse/PHPC-259

* Wed Apr 22 2015 Remi Collet <remi@fedoraproject.org> - 0.5.0-1
- initial package, version 0.5.0 (alpha)

