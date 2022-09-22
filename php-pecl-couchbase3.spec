# Fedora spec file for php-pecl-couchbase3
# without SCL compatibility from:
#
# remirepo spec file for php-pecl-couchbase3
#
# Copyright (c) 2013-2021 Remi Collet
# License: CC-BY-SA
# http://creativecommons.org/licenses/by-sa/4.0/
#
# Please, preserve the changelog entries
#

# we don't want -z defs linker flag
%undefine _strict_symbol_defs_build

%global pecl_name couchbase
%global with_zts  0%{!?_without_zts:%{?__ztsphp:1}}
# After 20-tokenizer.ini, 40-json
%global ini_name  50-%{pecl_name}.ini

%global libbuildver %(pkg-config --silence-errors --modversion libcouchbase 2>/dev/null || echo 65536)

Summary:       Couchbase Server PHP extension
Name:          php-pecl-couchbase3
Version:       3.2.1
Release:       4%{?dist}
License:       PHP
URL:           https://pecl.php.net/package/couchbase
Source0:       https://pecl.php.net/get/%{pecl_name}-%{version}%{?prever}.tgz

BuildRequires: make
BuildRequires: gcc
BuildRequires: php-devel >= 7.3
BuildRequires: php-pear
BuildRequires: php-json
BuildRequires: php-tokenizer
BuildRequires: pkgconfig(libcouchbase) >= 3.2.2
BuildRequires: fastlz-devel
BuildRequires: zlib-devel

Requires:      php(zend-abi) = %{php_zend_api}
Requires:      php(api) = %{php_core_api}
Requires:      php-json%{?_isa}
Requires:      php-tokenizer%{?_isa}
Requires:      libcouchbase%{?_isa} >= %{libbuildver}

Provides:      php-%{pecl_name}               = %{version}
Provides:      php-%{pecl_name}%{?_isa}       = %{version}
Provides:      php-pecl(%{pecl_name})         = %{version}
Provides:      php-pecl(%{pecl_name})%{?_isa} = %{version}
# Was renamed
Obsoletes:     php-pecl-couchbase             < 3
Provides:      php-pecl-couchbase             = %{version}
Provides:      php-pecl-couchbase%{?_isa}     = %{version}
Obsoletes:     php-pecl-couchbase2            < 3
Provides:      php-pecl-couchbase2            = %{version}
Provides:      php-pecl-couchbase2%{?_isa}    = %{version}


%description
The PHP client library provides fast access to documents stored
in a Couchbase Server.


%prep
%setup -q -c
mv %{pecl_name}-%{version}%{?prever} NTS

%{?_licensedir:sed -e '/LICENSE/s/role="doc"/role="src"/' -i package.xml}

cd NTS
# Drop bundled library
sed -e '/fastlz/d' -i ../package.xml
rm -r fastlz

# Sanity check, really often broken
extver=$(sed -n '/#define PHP_COUCHBASE_VERSION/{s/.* "//;s/".*$//;p}' php_couchbase.h)
if test "x${extver}" != "x%{version}%{?prever}"; then
   : Error: Upstream extension version is ${extver}, expecting %{version}%{?prever}
   exit 1
fi
cd ..

cat << 'EOF' | tee %{ini_name}
; Enable %{pecl_name} extension module
extension=%{pecl_name}.so

; Configuration
;couchbase.log_level = 'WARN'
;couchbase.encoder.format = 'json'
;couchbase.encoder.compression = 'off'
;couchbase.encoder.compression_threshold = 0
;couchbase.encoder.compression_factor = 0.0
;couchbase.decoder.json_arrays = 1
;couchbase.pool.max_idle_time_sec = 60
;couchbase.allow_fallback_to_bucket_connection = 0
EOF

%if 0%{?__ztsphp:1}
# duplicate for ZTS build
cp -pr NTS ZTS
%else
: Only NTS build, no ZTS
%endif


%build
peclconf() {
%configure \
     --with-system-fastlz \
     --with-php-config=$1
}

cd NTS
%{_bindir}/phpize
peclconf %{_bindir}/php-config
make %{?_smp_mflags}

%if %{with_zts}
cd ../ZTS
%{_bindir}/zts-phpize
peclconf %{_bindir}/zts-php-config
make %{?_smp_mflags}
%endif


%install
# Install the NTS stuff
make install -C NTS INSTALL_ROOT=%{buildroot}
install -D -m 644 %{ini_name} %{buildroot}%{php_inidir}/%{ini_name}

# Install the ZTS stuff
%if %{with_zts}
make install -C ZTS INSTALL_ROOT=%{buildroot}
install -D -m 644 %{ini_name} %{buildroot}%{php_ztsinidir}/%{ini_name}
%endif

# Install the package XML file
install -D -m 644 package.xml %{buildroot}%{pecl_xmldir}/%{name}.xml

# Test & Documentation
cd NTS
for i in $(grep 'role="doc"' ../package.xml | sed -e 's/^.*name="//;s/".*$//')
do install -Dpm 644 $i %{buildroot}%{pecl_docdir}/%{pecl_name}/$i
done


%check
: minimal NTS load test
%{__php} -n \
   -d extension=tokenizer.so \
   -d extension=json.so \
   -d extension=%{buildroot}%{php_extdir}/%{pecl_name}.so \
   -m | grep '^%{pecl_name}$'

%if %{with_zts}
: minimal ZTS load test
%{__ztsphp} -n \
   -d extension=tokenizer.so \
   -d extension=json.so \
   -d extension=%{buildroot}%{php_ztsextdir}/%{pecl_name}.so \
   -m | grep '^%{pecl_name}$'
%endif


%files
%license NTS/LICENSE
%doc %{pecl_docdir}/%{pecl_name}
%{pecl_xmldir}/%{name}.xml

%config(noreplace) %{php_inidir}/%{ini_name}
%{php_extdir}/%{pecl_name}.so

%if %{with_zts}
%config(noreplace) %{php_ztsinidir}/%{ini_name}
%{php_ztsextdir}/%{pecl_name}.so
%endif



%changelog
* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Oct 28 2021 Remi Collet <remi@remirepo.net> - 3.2.1-2
- rebuild for https://fedoraproject.org/wiki/Changes/php81

* Thu Oct 14 2021 Remi Collet <remi@remirepo.net> - 3.2.1-1
- update to 3.2.1
- raise dependency on libcouchbase 3.2.2

* Wed Jul 28 2021 Remi Collet <remi@remirepo.net> - 3.2.0-1
- update to 3.2.0
- raise dependency on libcouchbase 3.2

* Thu Jul 22 2021 Remi Collet <remi@remirepo.net> - 3.1.2-2
- rebuild for new libcouchbase soname

* Mon May 17 2021 Remi Collet <remi@remirepo.net> - 3.1.2-1
- update to 3.1.2

* Fri Feb  5 2021 Remi Collet <remi@remirepo.net> - 3.1.1-1
- update to 3.1.1

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Jan 21 2021 Remi Collet <remi@remirepo.net> - 3.1.0-1
- update to 3.1.0

* Mon Dec  7 2020 Remi Collet <remi@remirepo.net> - 3.0.5-1
- update to 3.0.5

* Mon Nov 16 2020 Remi Collet <remi@remirepo.net> - 3.0.4-1
- update to 3.0.4
- rename to php-pecl-couchbase3
- raise dependency on PHP 7.2
- raise dependency on libcouchbase 3.0
- drop dependency on igbinary extension

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Feb  4 2020 Remi Collet <remi@remirepo.net> - 2.6.2-1
- update to 2.6.2

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Remi Collet <remi@remirepo.net> - 2.6.1-3
- rebuild for https://fedoraproject.org/wiki/Changes/php74

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Jun  3 2019 Remi Collet <remi@remirepo.net> - 2.6.1-1
- update to 2.6.1

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Oct 11 2018 Remi Collet <remi@remirepo.net> - 2.6.0-2
- Rebuild for https://fedoraproject.org/wiki/Changes/php73

* Sat Oct  6 2018 Remi Collet <remi@remirepo.net> - 2.6.0-1
- update to 2.6.0
- raise dependency on libcouchbase 2.9.5

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jul  5 2018 Remi Collet <remi@remirepo.net> - 2.5.0-1
- update to 2.5.0
- raise dependency on libcouchbase 2.9.2

* Fri Jun  8 2018 Remi Collet <remi@remirepo.net> - 2.4.7-1
- update to 2.4.7
- raise dependency on libcouchbase 2.9.0

* Mon Apr 16 2018 Remi Collet <remi@remirepo.net> - 2.4.6-1
- update to 2.4.6
- raise dependency on libcouchbase 2.8.6

* Sun Mar 11 2018 Remi Collet <remi@remirepo.net> - 2.4.5-1
- update to 2.4.5

* Tue Feb 13 2018 Remi Collet <remi@remirepo.net> - 2.4.4-1
- Update to 2.4.4

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Jan  5 2018 Remi Collet <remi@remirepo.net> - 2.4.3-2
- cleanup for Fedora review

* Fri Jan  5 2018 Remi Collet <remi@remirepo.net> - 2.4.3-1
- Update to 2.4.3
- raise dependency on libcouchbase 2.8.4

* Tue Nov 14 2017 Remi Collet <remi@remirepo.net> - 2.4.2-1
- Update to 2.4.2

* Thu Oct  5 2017 Remi Collet <remi@remirepo.net> - 2.4.1-1
- Update to 2.4.1
- update provided configuration for couchbase.pool.max_idle_time_sec

* Wed Sep 20 2017 Remi Collet <remi@remirepo.net> - 2.4.0-2
- rebuild with libcouchbase 2.8.1

* Tue Sep  5 2017 Remi Collet <remi@remirepo.net> - 2.4.0-1
- Update to 2.4.0
- raise minimal PHP version to 5.6
- raise dependency on libcouchbase 2.8

* Tue Aug  1 2017 Remi Collet <remi@remirepo.net> - 2.3.4-1
- Update to 2.3.4

* Tue Jul 18 2017 Remi Collet <remi@remirepo.net> - 2.3.3-3
- rebuild for PHP 7.2.0beta1 new API

* Wed Jun 21 2017 Remi Collet <remi@remirepo.net> - 2.3.3-2
- rebuild for 7.2.0alpha2

* Thu Jun  1 2017 Remi Collet <remi@remirepo.net> - 2.3.3-1
- Update to 2.3.3
- raise dependency on libcouchbase 2.7.5

* Tue May  2 2017 Remi Collet <remi@remirepo.net> - 2.3.2-1
- Update to 2.3.2

* Wed Apr  5 2017 Remi Collet <remi@remirepo.net> - 2.3.1-1
- Update to 2.3.1

* Wed Mar  8 2017 Remi Collet <remi@remirepo.net> - 2.3.0-1
- Update to 2.3.0
- drop dependency on pcs extension
- add dependency on igbinary extension
- raise dependency on libcouchbase 2.7.2
- update default configuration with new options

* Tue Dec 27 2016 Remi Collet <remi@fedoraproject.org> - 2.2.4-1
- Update to 2.2.4
- add dependency on pcs extension

* Thu Dec  1 2016 Remi Collet <remi@fedoraproject.org> - 2.2.3-2
- rebuild with PHP 7.1.0 GA

* Wed Oct 05 2016 Remi Collet <remi@fedoraproject.org> - 2.2.3-1
- Update to 2.2.3
- open https://issues.couchbase.com/browse/PCBC-437 - visibility error

* Wed Sep 14 2016 Remi Collet <remi@fedoraproject.org> - 2.2.2-2
- rebuild for PHP 7.1 new API version

* Wed Sep 07 2016 Remi Collet <remi@fedoraproject.org> - 2.2.2-1
- Update to 2.2.2

* Mon Aug 08 2016 Remi Collet <remi@fedoraproject.org> - 2.2.1-1
- Update to 2.2.1

* Thu Jul  7 2016 Remi Collet <remi@fedoraproject.org> - 2.2.0-1
- Update to 2.2.0 (php 5 and 7, stable)

* Wed Jun 29 2016 Remi Collet <remi@fedoraproject.org> - 2.2.0-0.3.beta4
- Update to 2.2.0beta4 (php 5 and 7, beta)

* Thu May 26 2016 Remi Collet <remi@fedoraproject.org> - 2.2.0-0.2.beta3
- Update to 2.2.0beta3 (php 5 and 7, beta)

* Sun Mar 20 2016 Remi Collet <remi@fedoraproject.org> - 2.2.0-0.1.beta1
- Update to 2.2.0beta2 (php 5 and 7, beta)

* Tue Mar  8 2016 Remi Collet <remi@fedoraproject.org> - 2.1.0-2
- adapt for F24

* Thu Nov 05 2015 Remi Collet <remi@fedoraproject.org> - 2.1.0-1
- Update to 2.1.0
- add patch to use system fastlz library
  from https://github.com/couchbase/php-couchbase/pull/10

* Wed Apr 22 2015 Remi Collet <remi@fedoraproject.org> - 2.0.7-1
- Update to 2.0.7

* Wed Apr 08 2015 Remi Collet <remi@fedoraproject.org> - 2.0.6-1
- Update to 2.0.6 (stable)

* Wed Mar 04 2015 Remi Collet <remi@fedoraproject.org> - 2.0.5-1
- Update to 2.0.5 (stable)

* Mon Feb 09 2015 Remi Collet <remi@fedoraproject.org> - 2.0.4-1
- Update to 2.0.4 (stable)
- drop runtime dependency on pear, new scriptlet

* Wed Jan 07 2015 Remi Collet <remi@fedoraproject.org> - 2.0.3-1
- Update to 2.0.3

* Wed Dec 24 2014 Remi Collet <remi@fedoraproject.org> - 2.0.2-1.1
- Fedora 21 SCL mass rebuild

* Wed Dec 03 2014 Remi Collet <remi@fedoraproject.org> - 2.0.2-1
- Update to 2.0.2

* Wed Nov 05 2014 Remi Collet <remi@fedoraproject.org> - 2.0.1-1
- Update to 2.0.1

* Sat Sep 20 2014 Remi Collet <remi@fedoraproject.org> - 2.0.0-1
- rename to php-pecl-couchbase2 for new API
- update to 2.0.0
- open http://www.couchbase.com/issues/browse/PCBC-292 license
- open http://www.couchbase.com/issues/browse/PCBC-293 fastlz
- open http://www.couchbase.com/issues/browse/PCBC-294 xdebug

* Sat Sep  6 2014 Remi Collet <remi@fedoraproject.org> - 1.2.2-3
- test build with system fastlz

* Tue Aug 26 2014 Remi Collet <rcollet@redhat.com> - 1.2.2-2
- improve SCL build

* Mon May 12 2014 Remi Collet <remi@fedoraproject.org> - 1.2.2-1
- Update to 1.2.2

* Wed Apr  9 2014 Remi Collet <remi@fedoraproject.org> - 1.2.1-4
- add numerical prefix to extension configuration file

* Sun Mar 16 2014 Remi Collet <remi@fedoraproject.org> - 1.2.1-2
- install doc in pecl_docdir

* Sat Oct 05 2013 Remi Collet <remi@fedoraproject.org> - 1.2.1-1
- Update to 1.2.1
- add patch to fix ZTS build
  https://github.com/couchbase/php-ext-couchbase/pull/9

* Mon May 13 2013 Remi Collet <remi@fedoraproject.org> - 1.1.15-2
- fix dependency on php-pecl-igbinary

* Thu May  9 2013 Remi Collet <remi@fedoraproject.org> - 1.1.15-1
- update to 1.1.15 (no change)

* Fri Mar 22 2013 Remi Collet <remi@fedoraproject.org> - 1.1.14-1
- initial package

