# Fedora spec file for php-pecl-amqp
#
# Copyright (c) 2012-2024 Remi Collet
# License: CC-BY-SA-4.0
# http://creativecommons.org/licenses/by-sa/4.0/
#
# Please, preserve the changelog entries
#

%bcond_with         tests
%global pecl_name   amqp
%global ini_name    40-%{pecl_name}.ini

%global upstream_version 2.1.2
#global upstream_prever  RC1
#global upstream_lower   rc1
%global sources          %{pecl_name}-%{upstream_version}%{?upstream_prever}
%global _configure       ../%{sources}/configure

Summary:       Communicate with any AMQP compliant server
Name:          php-pecl-amqp
Version:       %{upstream_version}%{?upstream_prever:~%{upstream_lower}}
Release:       8%{?dist}
License:       PHP-3.01
URL:           https://pecl.php.net/package/amqp
Source0:       https://pecl.php.net/get/%{pecl_name}-%{upstream_version}%{?upstream_prever}.tgz

ExcludeArch:   %{ix86}

BuildRequires: make
BuildRequires: gcc
BuildRequires: php-devel >= 7.4
BuildRequires: php-pear
BuildRequires: pkgconfig(librabbitmq) >= 0.8.0
%if %{with tests}
BuildRequires: rabbitmq-server
BuildRequires: hostname
%endif

Requires:      php(zend-abi) = %{php_zend_api}
Requires:      php(api) = %{php_core_api}

Provides:      php-%{pecl_name}               = %{version}
Provides:      php-%{pecl_name}%{?_isa}       = %{version}
Provides:      php-pecl(%{pecl_name})         = %{version}
Provides:      php-pecl(%{pecl_name})%{?_isa} = %{version}


%description
This extension can communicate with any AMQP spec 0-9-1 compatible server,
such as RabbitMQ, OpenAMQP and Qpid, giving you the ability to create and
delete exchanges and queues, as well as publish to any exchange and consume
from any queue.


%prep
%setup -q -c

# Don't install/register tests
sed -e 's/role="test"/role="src"/' \
    -e '/LICENSE/s/role="doc"/role="src"/' \
    -i package.xml

cd %{sources}
# Upstream often forget to change this
extver=$(sed -n '/#define PHP_AMQP_VERSION /{s/.* "//;s/".*$//;p}' php_amqp_version.h)
if test "x${extver}" != "x%{upstream_version}%{?upstream_prever}"; then
   : Error: Upstream extension version is ${extver}, expecting %{upstream_version}%{?upstream_prever}.
   exit 1
fi
cd ..

cat > %{ini_name} << 'EOF'
; Enable %{pecl_name} extension module
extension = %{pecl_name}.so

; Whether calls to AMQPQueue::get() and AMQPQueue::consume()
; should require that the client explicitly acknowledge messages.
; Setting this value to 1 will pass in the AMQP_AUTOACK flag to
; the above method calls if the flags field is omitted.
;amqp.auto_ack = 0

; The host to which to connect.
;amqp.host = localhost

; The login to use while connecting to the broker.
;amqp.login = guest

; The password to use while connecting to the broker.
;amqp.password = guest

; The port on which to connect.
;amqp.port = 5672

; The number of messages to prefect from the server during a
; call to AMQPQueue::get() or AMQPQueue::consume() during which
; the AMQP_AUTOACK flag is not set.
;amqp.prefetch_count = 3
;amqp.prefetch_size = 0
;amqp.global_prefetch_count =0
;amqp.global_prefetch_size =0

; The virtual host on the broker to which to connect.
;amqp.vhost = /

; Timeout
;amqp.timeout =
;amqp.read_timeout = 0
;amqp.write_timeout = 0
;amqp.connect_timeout = 0
;amqp.rpc_timeout = 0

;amqp.channel_max = 256
;amqp.frame_max = 131072
;amqp.heartbeat = 0

;amqp.cacert = ''
;amqp.cert = ''
;amqp.key = ''
;amqp.verify = 1
;amqp.sasl_method = 'AMQP_SASL_METHOD_PLAIN'
;amqp.serialization_depth = 128
;amqp.deserialization_depth = 128
EOF


%build
cd %{sources}
%{__phpize}
sed -e 's/INSTALL_ROOT/DESTDIR/' -i build/Makefile.global

%configure --with-php-config=%{__phpconfig}
%make_build


%install
cd %{sources}

: Install the extension
%make_install

: Drop in the bit of configuration
install -Dpm 644 ../%{ini_name} %{buildroot}%{php_inidir}/%{ini_name}

: Install XML package description
install -Dpm 644 ../package.xml %{buildroot}%{pecl_xmldir}/%{name}.xml

: Install the Documentation
for i in $(grep 'role="doc"' ../package.xml | sed -e 's/^.*name="//;s/".*$//')
do install -Dpm 644 $i %{buildroot}%{pecl_docdir}/%{pecl_name}/$i
done


%check
: Minimal load test for the extension
%{__php} --no-php-ini \
    --define extension=%{sources}/modules/%{pecl_name}.so \
    -m | grep '^%{pecl_name}$'

%if %{with tests}
mkdir log run base
: Launch the RabbitMQ service
export LANG=C.UTF-8
export RABBITMQ_PID_FILE=$PWD/run/pid
export RABBITMQ_LOG_BASE=$PWD/log
export RABBITMQ_MNESIA_BASE=$PWD/base
export PHP_AMQP_HOST=localhost
/usr/lib/rabbitmq/bin/rabbitmq-server &>log/output &
/usr/lib/rabbitmq/bin/rabbitmqctl wait $RABBITMQ_PID_FILE

ret=0
pushd %{sources}
: Run the upstream test Suite for the extension
TEST_PHP_ARGS="-n -d extension=$PWD/modules/%{pecl_name}.so" \
%{__php} -n run-tests.php -q --show-diff || ret=1
popd

: Cleanup
if [ -s $RABBITMQ_PID_FILE ]; then
   kill $(cat $RABBITMQ_PID_FILE)
fi
rm -rf log run base

exit $ret
%endif


%files
%license %{sources}/LICENSE
%doc %{pecl_docdir}/%{pecl_name}
%{pecl_xmldir}/%{name}.xml

%config(noreplace) %{php_inidir}/%{ini_name}
%{php_extdir}/%{pecl_name}.so


%changelog
* Fri Jul 25 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_43_Mass_Rebuild

* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Oct 18 2024 Remi Collet <remi@fedoraproject.org> - 2.1.2-6
- modernize the spec file

* Mon Oct 14 2024 Remi Collet <remi@fedoraproject.org> - 2.1.2-5
- rebuild for https://fedoraproject.org/wiki/Changes/php84

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Apr 12 2024 Remi Collet <remi@remirepo.net> - 2.1.2-3
- drop 32-bit support
  https://fedoraproject.org/wiki/Changes/php_no_32_bit

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Remi Collet <remi@remirepo.net> - 2.1.2-1
- update to 2.1.2

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Oct 13 2023 Remi Collet <remi@remirepo.net> - 2.1.1-1
- update to 2.1.1

* Tue Oct 03 2023 Remi Collet <remi@remirepo.net> - 2.1.0-2
- rebuild for https://fedoraproject.org/wiki/Changes/php83

* Thu Sep  7 2023 Remi Collet <remi@remirepo.net> - 2.1.0-1
- update to 2.1.0

* Mon Aug 21 2023 Remi Collet <remi@remirepo.net> - 2.0.0-1
- update to 2.0.0
- build out of sources tree

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.11.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Mar 31 2023 Remi Collet <remi@remirepo.net> - 1.11.0-6
- use SPDX license ID

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.11.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Oct 05 2022 Remi Collet <remi@remirepo.net> - 1.11.0-4
- rebuild for https://fedoraproject.org/wiki/Changes/php82
- add patch for test suite with 8.2 from
  https://github.com/php-amqp/php-amqp/pull/418

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.11.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.11.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Dec  7 2021 Remi Collet <remi@remirepo.net> - 1.11.0-1
- update to 1.11.0

* Tue Nov  2 2021 Remi Collet <remi@remirepo.net> - 1.11.0~rc1-1
- update to 1.11.0RC1

* Thu Oct 28 2021 Remi Collet <remi@remirepo.net> - 1.11.0~beta-3
- rebuild for https://fedoraproject.org/wiki/Changes/php81

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.11.0~beta-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Mar 10 2021 Remi Collet <remi@remirepo.net> - 1.11.0~beta-1
- update to 1.11.0beta
- drop patched merged upstream

* Thu Mar  4 2021 Remi Collet <remi@remirepo.net> - 1.10.2-4
- rebuild for https://fedoraproject.org/wiki/Changes/php80
- add patches for PHP 8 from upstream and
  https://github.com/php-amqp/php-amqp/pull/383

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Apr  6 2020 Remi Collet <remi@remirepo.net> - 1.10.2-1
- update to 1.10.2

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Remi Collet <remi@remirepo.net> - 1.9.4-4
- rebuild for https://fedoraproject.org/wiki/Changes/php74

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Jan  2 2019 Remi Collet <remi@remirepo.net> - 1.9.4-1
- update to 1.9.4
- drop patch merged upstream
- raise minimal PHP version to 5.6
  and open https://github.com/pdezwart/php-amqp/pull/338

* Thu Oct 11 2018 Remi Collet <remi@remirepo.net> - 1.9.3-5
- Rebuild for https://fedoraproject.org/wiki/Changes/php73
- add patch for PHP 7.3 from
  https://github.com/pdezwart/php-amqp/pull/323

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Jan 26 2018 Remi Collet <remi@remirepo.net> - 1.9.3-2
- undefine _strict_symbol_defs_build

* Thu Oct 19 2017 Remi Collet <remi@remirepo.net> - 1.9.3-1
- Update to 1.9.3 (stable)

* Tue Oct 03 2017 Remi Collet <remi@fedoraproject.org> - 1.9.1-4
- rebuild for https://fedoraproject.org/wiki/Changes/php72

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jun 12 2017 Remi Collet <remi@remirepo.net> - 1.9.1-1
- Update to 1.9.1 (stable)

* Tue Mar 21 2017 Remi Collet <remi@remirepo.net> - 1.9.0-1
- update to 1.9.0 (stable)

* Fri Feb 17 2017 Remi Collet <remi@remirepo.net> - 1.8.0-1
- update to 1.8.0 (stable)

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Nov 14 2016 Remi Collet <remi@fedoraproject.org> - 1.7.1-2
- rebuild for https://fedoraproject.org/wiki/Changes/php71

* Mon Jul 11 2016 Remi Collet <remi@fedoraproject.org> - 1.7.1-1
- update to 1.7.1 (php 5 and 7, stable)

* Mon Jun 27 2016 Remi Collet <remi@fedoraproject.org> - 1.7.0-2
- rebuild for https://fedoraproject.org/wiki/Changes/php70

* Tue Apr 26 2016 Remi Collet <remi@fedoraproject.org> - 1.7.0-1
- update to 1.7.0 (php 5 and 7, stable)

* Wed Feb 10 2016 Remi Collet <remi@fedoraproject.org> - 1.6.1-2
- drop scriptlets (replaced file triggers in php-pear)

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Nov 26 2015 Remi Collet <remi@fedoraproject.org> - 1.6.1-1
- update to 1.6.1 (stable)

* Tue Nov  3 2015 Remi Collet <remi@fedoraproject.org> - 1.6.0-1
- update to 1.6.0 (stable)
- fix typo in config file

* Fri Sep 18 2015 Remi Collet <remi@fedoraproject.org> - 1.6.0-0.4.beta4
- update to 1.6.0beta4
- open https://github.com/pdezwart/php-amqp/pull/178 - librabbitmq 0.5
- open https://github.com/pdezwart/php-amqp/pull/179 --with-libdir

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.0-0.2.beta3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Apr 20 2015 Remi Collet <remi@fedoraproject.org> - 1.6.0-0.1.beta3
- update to 1.6.0beta3
* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Thu Jun 19 2014 Remi Collet <rcollet@redhat.com> - 1.4.0-4
- rebuild for https://fedoraproject.org/wiki/Changes/Php56

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed Apr 23 2014 Remi Collet <remi@fedoraproject.org> - 1.4.0-2
- add numerical prefix to extension configuration file

* Tue Apr 15 2014 Remi Collet <remi@fedoraproject.org> - 1.4.0-1
- update to 1.6.0 (stable)
- install doc in pecl doc_dir
- install tests in pecl test_dir (in devel)
- add --with tests option to run upstream tests during build
- build ZTS extension

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu May 30 2013 Remi Collet <remi@fedoraproject.org> - 1.2.0-1
- Update to 1.2.0

* Fri Mar 22 2013 Remi Collet <rcollet@redhat.com> - 1.0.9-4
- rebuild for http://fedoraproject.org/wiki/Features/Php55

* Wed Mar 13 2013 Remi Collet <remi@fedoraproject.org> - 1.0.9-3
- rebuild for new librabbitmq

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Tue Nov 13 2012 Remi Collet <remi@fedoraproject.org> - 1.0.9-1
- update to 1.0.9
- cleanups

* Wed Sep 12 2012 Remi Collet <remi@fedoraproject.org> - 1.0.7-1
- update to 1.0.7

* Mon Aug 27 2012 Remi Collet <remi@fedoraproject.org> - 1.0.5-1
- update to 1.0.5
- LICENSE now provided in upstream tarball

* Wed Aug 01 2012 Remi Collet <remi@fedoraproject.org> - 1.0.4-1
- update to 1.0.4

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat May 19 2012 Remi Collet <remi@fedoraproject.org> - 1.0.3-1
- update to 1.0.3
- add extension version check (and fix)

* Mon Mar 19 2012 Remi Collet <remi@fedoraproject.org> - 1.0.1-3
- clean EL-5 stuff as requires php 5.2.0, https://bugs.php.net/61351

* Sat Mar 10 2012 Remi Collet <remi@fedoraproject.org> - 1.0.1-2
- rebuild for PHP 5.4

* Sat Mar 10 2012 Remi Collet <remi@fedoraproject.org> - 1.0.1-1
- Initial RPM release without ZTS extension
- open request for LICENSE file https://bugs.php.net/61337

