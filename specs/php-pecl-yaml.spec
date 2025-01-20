# Fedora spec file for php-pecl-yaml
#
# License: MIT
# http://opensource.org/licenses/MIT
#
# Please, preserve the changelog entries
#
%bcond_without           tests

%global with_zts         0%{!?_without_zts:%{?__ztsphp:1}}
%global pecl_name        yaml
%global ini_name         40-%{pecl_name}.ini

%global upstream_version 2.2.4
#global upstream_prever  b2
%global sources          %{pecl_name}-%{upstream_version}%{?upstream_prever}

Summary:       PHP Bindings for libyaml
Name:          php-pecl-%{pecl_name}
Version:       %{upstream_version}%{?upstream_prever:~%{upstream_prever}}
Release:       2%{?dist}
License:       MIT
URL:           https://pecl.php.net/package/%{pecl_name}

Source0:       https://pecl.php.net/get/%{sources}.tgz

ExcludeArch:   %{ix86}

BuildRequires: make
BuildRequires: gcc
BuildRequires: php-devel
BuildRequires: php-pear
BuildRequires: libyaml-devel

Requires:      php(zend-abi) = %{php_zend_api}
Requires:      php(api) = %{php_core_api}

Provides:      php-%{pecl_name}               = %{version}
Provides:      php-%{pecl_name}%{?_isa}       = %{version}
Provides:      php-pecl(%{pecl_name})         = %{version}
Provides:      php-pecl(%{pecl_name})%{?_isa} = %{version}


%description
Support for YAML 1.1 (YAML Ain't Markup Language) serialization using the
LibYAML library.

Documentation: https://php.net/yaml

Package built for PHP %(%{__php} -r 'echo PHP_MAJOR_VERSION.".".PHP_MINOR_VERSION;')%{?scl: as Software Collection (%{scl} by %{?scl_vendor}%{!?scl_vendor:rh})}.


%prep
%setup -c -q

# Remove test file to avoid regsitration
sed -e 's/role="test"/role="src"/' \
    -e '/LICENSE/s/role="doc"/role="src"/' \
    -i package.xml

cd %{sources}
# Check upstream version (often broken)
extver=$(sed -n '/#define PHP_YAML_VERSION/{s/.* "//;s/".*$//;p}' php_yaml.h)
if test "x${extver}" != "x%{upstream_version}%{?upstream_prever}"; then
   : Error: Upstream extension version is ${extver}, expecting %{upstream_version}%{?upstream_prever}.
   exit 1
fi
cd ..

cat << 'EOF' | tee %{ini_name}
; Enable %{summary} extension module
extension=%{pecl_name}.so

; %{pecl_name} extension configuration
; see http://www.php.net/manual/en/yaml.configuration.php

; Decode entities which have the explicit tag "tag:yaml.org,2002:binary"
;yaml.decode_binary = 0

; Controls the decoding of "tag:yaml.org,2002:timestamp"
; 0 will not apply any decoding, 1 will use strtotime() 2 will use date_create().
;yaml.decode_timestamp = 0

; Cause canonical form output.
;yaml.output_canonical = 0

; Number of spaces to indent sections. Value should be between 1 and 10.
;yaml.output_indent = 2

; Set the preferred line width. -1 means unlimited.
;yaml.output_width = 80

; Enable/disable serialized php object processing.
;yaml.decode_php = 0
EOF


%build
cd %{sources}
%{__phpize}
sed -e 's/INSTALL_ROOT/DESTDIR/' -i build/Makefile.global

%configure \
    --with-libdir=%{_lib} \
    --with-php-config=%{__phpconfig}

%make_build


%install
: Install the XML package description
install -Dpm 644 package.xml %{buildroot}%{pecl_xmldir}/%{name}.xml

: install the config file
install -Dpm644 %{ini_name} %{buildroot}%{php_inidir}/%{ini_name}

: Install the extension
cd %{sources}
%make_install

: Install the Documentation
for i in $(grep 'role="doc"' ../package.xml | sed -e 's/^.*name="//;s/".*$//')
do install -Dpm 644 $i %{buildroot}%{pecl_docdir}/%{pecl_name}/$i
done


%check
cd %{sources}

: Minimal load test for NTS extension
%{__php} --no-php-ini \
    --define extension=%{buildroot}%{php_extdir}/%{pecl_name}.so \
    --modules | grep '^%{pecl_name}$'

%if %{with tests}
: Upstream test suite for NTS extension
TEST_PHP_ARGS="-n -d extension=%{buildroot}%{php_extdir}/%{pecl_name}.so" \
%{__php} -n run-tests.php -q -P --show-diff %{?_smp_mflags}
%endif


%files
%license %{sources}/LICENSE
%doc %{pecl_docdir}/%{pecl_name}
%{pecl_xmldir}/%{name}.xml
%config(noreplace) %{php_inidir}/%{ini_name}
%{php_extdir}/%{pecl_name}.so


%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Oct  7 2024 Remi Collet <remi@remirepo.net> - 2.2.4-1
- update to 2.2.4
- drop patches merged upstream
- cleanup for Fedora review

* Mon Sep 30 2024 Remi Collet <remi@remirepo.net> - 2.2.3-5
- fix test suite with 8.4 using patch from
  https://github.com/php/pecl-file_formats-yaml/pull/86

* Mon Feb 19 2024 Remi Collet <remi@remirepo.net> - 2.2.3-4
- fix incompatible-pointer-types using patch from
  https://github.com/php/pecl-file_formats-yaml/pull/74

* Wed Aug 30 2023 Remi Collet <remi@remirepo.net> - 2.2.3-3
- rebuild for PHP 8.3.0RC1

* Tue Jul 18 2023 Remi Collet <remi@remirepo.net> - 2.2.3-2
- build out of sources tree

* Mon Mar  6 2023 Remi Collet <remi@remirepo.net> - 2.2.3-1
- update to 2.2.3
- drop patch merged upstream

* Fri Sep  9 2022 Remi Collet <remi@remirepo.net> - 2.2.2-3
- add upstream patch for test suite with PHP 8.2

* Tue Feb 22 2022 Remi Collet <remi@remirepo.net> - 2.2.2-2
- fix gh#65 yaml_parse_url method not working using patch from
  https://github.com/php/pecl-file_formats-yaml/pull/66

* Mon Oct 25 2021 Remi Collet <remi@remirepo.net> - 2.2.2-1
- update to 2.2.2
- drop patch merged upstream

* Wed Sep 01 2021 Remi Collet <remi@remirepo.net> - 2.2.1-8
- rebuild for 8.1.0RC1

* Tue Aug  3 2021 Remi Collet <remi@remirepo.net> - 2.2.1-7
- rebuild for PHP 8.1.0beta2

* Fri Jul 23 2021 Remi Collet <remi@remirepo.net> - 2.2.1-6
- add fix for PHP 8.1.0beta1 from
  https://github.com/php/pecl-file_formats-yaml/pull/59

* Wed Jun  9 2021 Remi Collet <remi@remirepo.net> - 2.2.1-5
- add fix for test suite with PHP 8.1 from
  https://github.com/php/pecl-file_formats-yaml/pull/59

* Thu Apr 29 2021 Remi Collet <remi@remirepo.net> - 2.2.1-4
- F34 rebuild for https://github.com/remicollet/remirepo/issues/174

* Mon Dec 21 2020 Remi Collet <remi@remirepo.net> - 2.2.1-1
- update to 2.2.1

* Sun Nov 29 2020 Remi Collet <remi@remirepo.net> - 2.2.0-1
- update to 2.2.0 (stable)

* Wed Sep 30 2020 Remi Collet <remi@remirepo.net> - 2.2.0~b2-2
- rebuild for PHP 8.0.0RC1

* Mon Sep 14 2020 Remi Collet <remi@remirepo.net> - 2.2.0~b2-1
- update to 2.2.0b2 (no change)

* Wed Sep  2 2020 Remi Collet <remi@remirepo.net> - 2.2.0~b1-2
- rebuild for PHP 8.0.0beta3

* Sun Aug 16 2020 Remi Collet <remi@remirepo.net> - 2.2.0~b1-1
- update to 2.2.0b1
- drop patches merged upstream

* Wed Aug  5 2020 Remi Collet <remi@remirepo.net> - 2.1.0-3
- rebuild for 8.0.0beta1

* Wed Jul 22 2020 Remi Collet <remi@remirepo.net> - 2.1.0-2
- rebuild for 8.0.0alpha3 using patch from
  https://github.com/php/pecl-file_formats-yaml/pull/53

* Thu Apr 23 2020 Remi Collet <remi@remirepo.net> - 2.1.0-1
- update to 2.1.0
- raise dependency on PHP 7.1
- fix 32-bit build using patch from
  https://github.com/php/pecl-file_formats-yaml/pull/45

* Tue Sep 03 2019 Remi Collet <remi@remirepo.net> - 2.0.4-4
- rebuild for 7.4.0RC1

* Tue Jul 23 2019 Remi Collet <remi@remirepo.net> - 2.0.4-3
- rebuild for 7.4.0beta1

* Fri Mar  1 2019 Remi Collet <remi@remirepo.net> - 2.0.4-1
- rebuild

* Sat Nov 24 2018 Remi Collet <remi@remirepo.net> - 2.0.4-1
- update to 2.0.4

* Tue Nov 13 2018 Remi Collet <remi@remirepo.net> - 2.0.3-1
- update to 2.0.3
- drop patch merged upstream

* Thu Aug 16 2018 Remi Collet <remi@remirepo.net> - 2.0.2-5
- rebuild for 7.3.0beta2 new ABI

* Wed Jul 18 2018 Remi Collet <remi@remirepo.net> - 2.0.2-4
- rebuild for 7.3.0alpha4 new ABI

* Wed Jul  4 2018 Remi Collet <remi@remirepo.net> - 2.0.2-3
- add better patch for PHP 7.3 from
  https://github.com/php/pecl-file_formats-yaml/pull/33

* Tue Jul  3 2018 Remi Collet <remi@remirepo.net> - 2.0.2-2
- add patch for PHP 7.3 from
  https://github.com/php/pecl-file_formats-yaml/pull/32
- ignore 1 failed test with PHP 7.3

* Tue Aug  1 2017 Remi Collet <remi@remirepo.net> - 2.0.2-1
- Update to 2.0.2

* Tue Jul 18 2017 Remi Collet <remi@remirepo.net> - 2.0.0-4
- rebuild for PHP 7.2.0beta1 new API

* Wed Mar 29 2017 Remi Collet <remi@fedoraproject.org> - 2.0.0-3
- add upstream patch to fix FTBFS with 7.1.4RC1, reported by Koschei

* Thu Dec  1 2016 Remi Collet <remi@fedoraproject.org> - 2.0.0-2
- rebuild with PHP 7.1.0 GA

* Mon Sep 26 2016 Remi Collet <remi@fedoraproject.org> - 2.0.0-1
- update to 2.0.0 (php 7)

* Wed Sep 14 2016 Remi Collet <remi@fedoraproject.org> - 2.0.0-0.10.RC8
- rebuild for PHP 7.1 new API version

* Mon Jun  6 2016 Remi Collet <remi@fedoraproject.org> - 2.0.0-0.9.RC8
- update to 2.0.0RC8

* Sun Mar  6 2016 Remi Collet <remi@fedoraproject.org> - 2.0.0-0.8.RC7
- adapt for F24

* Tue Mar  1 2016 Remi Collet <remi@fedoraproject.org> - 2.0.0-0.7.RC7
- skip yaml_002.phpt, see https://bugs.php.net/71696

* Thu Dec 31 2015 Remi Collet <remi@fedoraproject.org> - 2.0.0-0.6.RC7
- update to 2.0.0RC7

* Tue Dec  8 2015 Remi Collet <remi@fedoraproject.org> - 2.0.0-0.5.RC6
- update to 2.0.0RC6

* Sun Oct 18 2015 Remi Collet <remi@fedoraproject.org> - 2.0.0-0.4.RC5
- update to 2.0.0RC5

* Sat Oct 17 2015 Remi Collet <remi@fedoraproject.org> - 2.0.0-0.3.RC4
- update to 2.0.0RC4

* Sat Oct 17 2015 Remi Collet <remi@fedoraproject.org> - 2.0.0-0.2.RC2
- add uptream patches, fix segfault and test suite

* Sat Oct 17 2015 Remi Collet <remi@fedoraproject.org> - 2.0.0-0.1.RC2
- update to 2.0.0RC2 for PHP 7
- 2 failed tests, so ignore test suite results for now

* Sat Oct 17 2015 Remi Collet <remi@fedoraproject.org> - 2.0.0-0.1.RC1
- update to 2.0.0RC1 for PHP 7

* Tue Jun 23 2015 Remi Collet <remi@fedoraproject.org> - 1.2.0-2
- allow build against rh-php56 (as more-php56)

* Mon May 18 2015 Remi Collet <remi@fedoraproject.org> - 1.2.0-1
- Update to 1.2.0 (stable)

* Mon May  4 2015 Remi Collet <remi@fedoraproject.org> - 1.1.1-6
- drop runtime dependency on pear, new scriptlets

* Wed Dec 24 2014 Remi Collet <remi@fedoraproject.org> - 1.1.1-5.1
- Fedora 21 SCL mass rebuild

* Fri Aug 29 2014 Remi Collet <rcollet@redhat.com> - 1.1.1-5
- don't install tests

* Mon Aug 25 2014 Remi Collet <rcollet@redhat.com> - 1.1.1-4
- improve SCL build

* Thu Apr 17 2014 Remi Collet <remi@fedoraproject.org> - 1.1.1-3
- add numerical prefix to extension configuration file (php 5.6)

* Wed Mar 19 2014 Remi Collet <rcollet@redhat.com> - 1.1.1-2
- allow SCL build

* Tue Nov 19 2013 Remi Collet <remi@fedoraproject.org> - 1.1.1-1
- Update to 1.1.1 (stable)
- install doc in pecl doc_dir
- install tests in pecl test_dir

* Fri Nov 30 2012 Remi Collet <RPMS@FamilleCollet.com> - 1.1.0-2.1
- also provides php-yaml

* Fri Apr 20 2012 Remi Collet <RPMS@FamilleCollet.com> - 1.1.0-2
- update to 1.0.1 for php 5.4

* Fri Apr 20 2012 Remi Collet <RPMS@FamilleCollet.com> - 1.1.0-1
- update to 1.0.1 for php 5.3

* Fri Apr 20 2012 Theodore Lee <theo148@gmail.com> - 1.1.0-1
- Update to upstream 1.1.0 release
- Drop upstreamed cflags patch

* Sun Nov 13 2011 Remi Collet <remi@fedoraproject.org> - 1.0.1-5
- build against php 5.4

* Wed Oct 05 2011 Remi Collet <Fedora@FamilleCollet.com> - 1.0.1-4
- ZTS extension
- spec cleanups

* Fri May 06 2011 Remi Collet <RPMS@FamilleCollet.com> - 1.0.1-2
- clean spec
- fix requirment, license, tests...

* Thu May 05 2011 Thomas Morse <tmorse@empowercampaigns.com> 1.0.1-1
- Version 1.0.1
- initial RPM

