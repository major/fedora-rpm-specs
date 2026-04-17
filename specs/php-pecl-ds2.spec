# Fedora spec file for php-pecl-ds
# without SCL compatibility from:
#
# remirepo spec file for php-pecl-ds2
#
# SPDX-FileCopyrightText:  Copyright 2016-2026 Remi Collet
# SPDX-License-Identifier: CECILL-2.1
# http://www.cecill.info/licences/Licence_CeCILL_V2-en.txt
#
# Please, preserve the changelog entries
#

%bcond_without       tests

%global pecl_name    ds
%global pie_vend     php-ds
%global pie_proj     ext-ds
%global ini_name     40-%{pecl_name}.ini
%global _configure   ../configure

# Github forge
%global gh_vend      %{pie_vend}
%global gh_proj      %{pie_proj}
%global forgeurl     https://github.com/%{gh_vend}/%{gh_proj}
%global tag          v%{version}


Summary:        Data Structures for PHP version 2
Name:           php-pecl-%{pecl_name}2
License:        MIT
Version:        2.0.0
Release:        1%{?dist}
%forgemeta
URL:            %{forgeurl}
Source0:        %{forgesource}

ExcludeArch:    %{ix86}

BuildRequires:  make
BuildRequires:  %{?dtsprefix}gcc
BuildRequires:  php-devel >= 8.2

Requires:       php(zend-abi) = %{php_zend_api}
Requires:       php(api) = %{php_core_api}

%if 0%{?fedora} >= 45 || 0%{?rhel} >= 11 || "%{php_version}" > "8.6"
Obsoletes:     php-pecl-%{pecl_name}            < 2
Provides:      php-pecl-%{pecl_name}            = %{version}-%{release}
Provides:      php-pecl-%{pecl_name}%{?_isa}    = %{version}-%{release}
%else
# A single version can be installed
Conflicts:     php-pecl-%{pecl_name}            < 2
%endif

# Extension
Provides:      php-%{pecl_name}                 = %{version}
Provides:      php-%{pecl_name}%{?_isa}         = %{version}
# PECL
Provides:      php-pecl(%{pecl_name})           = %{version}
Provides:      php-pecl(%{pecl_name})%{?_isa}   = %{version}
# PIE
Provides:      php-pie(%{pie_vend}/%{pie_proj}) = %{version}
Provides:      php-%{pie_vend}-%{pie_proj}      = %{version}


%description
An extension providing specialized data structures as efficient alternatives
to the PHP array.

This package provides API version 2.


%prep
%forgesetup

# Sanity check, really often broken
extver=$(sed -n '/#define PHP_DS_VERSION/{s/.* "//;s/".*$//;p}' php_ds.h)
if test "x${extver}" != "x%{version}%{?prever:-%{prever}}"; then
   : Error: Upstream extension version is ${extver}, expecting %{version}%{?prever:-%{prever}}.
   exit 1
fi

mkdir NTS

# Create configuration file
cat << 'EOF' | tee %{ini_name}
; Enable '%{summary}' extension module
extension=%{pecl_name}.so
EOF


%build
%{?dtsenable}

peclbuild() {
%configure \
    --enable-ds \
    --with-php-config=$1

%make_build
}

%{__phpize}
sed -e 's/INSTALL_ROOT/DESTDIR/' -i build/Makefile.global

cd NTS
peclbuild %{__phpconfig}


%install
%{?dtsenable}

%make_install -C NTS

# install config file
install -D -m 644 %{ini_name} %{buildroot}%{php_inidir}/%{ini_name}


%check
: Minimal load test for NTS extension
%{__php} --no-php-ini \
    --define extension=%{buildroot}%{php_extdir}/%{pecl_name}.so \
    --modules | grep '^%{pecl_name}$'

%if %{with tests}
: Upstream test suite for NTS extension
TEST_PHP_ARGS="-n -d extension=%{buildroot}%{php_extdir}/%{pecl_name}.so" \
%{__php} -n run-tests.php -q --show-diff
%endif


%files
%license LICENSE
%doc composer.json
%doc *.md

%config(noreplace) %{php_inidir}/%{ini_name}
%{php_extdir}/%{pecl_name}.so


%changelog
* Tue Apr 14 2026 Remi Collet <remi@remirepo.net> - 2.0.0-1
- update to 2.0.0
- rename to php-pecl-ds2
- run standard php test suite from extension sources
  instead of separate tests using phpunit
- drop ZTS build

* Fri Mar 13 2026 Remi Collet <remi@remirepo.net> - 1.6.0-4
- drop pear/pecl dependency
- sources from github

* Thu Sep 25 2025 Remi Collet <remi@remirepo.net> - 1.6.0-3
- rebuild for PHP 8.5.0RC1

* Wed Jul 30 2025 Remi Collet <remi@remirepo.net> - 1.6.0-2
- rebuild for 8.5.0alpha3

* Sat May  3 2025 Remi Collet <remi@remirepo.net> - 1.6.0-1
- update to 1.6.0
- re-license spec file to CECILL-2.1

* Wed Dec 20 2023 Remi Collet <remi@remirepo.net> - 1.5.0-1
- update to 1.5.0

* Wed Aug 30 2023 Remi Collet <remi@remirepo.net> - 1.4.0-3
- rebuild for PHP 8.3.0RC1

* Wed Jul 12 2023 Remi Collet <remi@remirepo.net> - 1.4.0-2
- build out of sources tree
- add upstream patch for PHP 8.3

* Tue Dec 14 2021 Remi Collet <remi@remirepo.net> - 1.4.0-1
- update to 1.4.0
- raise dependency on PHP 7.3
- drop all patches merged upstream
- switch to phpunit8

* Wed Nov  3 2021 Remi Collet <remi@remirepo.net> - 1.3.0-6
- add patches for PHP 8.1 from upstream and from
  https://github.com/php-ds/ext-ds/pull/187

* Fri Mar 26 2021 Remi Collet <remi@remirepo.net> - 1.3.0-4
- switch to phpunit7

* Tue Nov  3 2020 Remi Collet <remi@remirepo.net> - 1.3.0-2
- fix segfault using patch from
  https://github.com/php-ds/ext-ds/pull/165

* Wed Oct 14 2020 Remi Collet <remi@remirepo.net> - 1.3.0-1
- update to 1.3.0

* Tue Sep 03 2019 Remi Collet <remi@remirepo.net> - 1.2.9-2
- rebuild for 7.4.0RC1

* Mon May 13 2019 Remi Collet <remi@remirepo.net> - 1.2.9-1
- update to 1.2.9

* Tue Jan 29 2019 Remi Collet <remi@remirepo.net> - 1.2.8-1
- update to 1.2.8

* Mon Nov 19 2018 Remi Collet <remi@remirepo.net> - 1.2.7-1
- update to 1.2.7

* Thu Aug 16 2018 Remi Collet <remi@remirepo.net> - 1.2.6-3
- rebuild for 7.3.0beta2 new ABI

* Wed Jul 18 2018 Remi Collet <remi@remirepo.net> - 1.2.6-2
- rebuld for 7.3.0alpha4 new ABI

* Fri May 25 2018 Remi Collet <remi@remirepo.net> - 1.2.6-1
- update to 1.2.6

* Mon Mar 12 2018 Remi Collet <remi@remirepo.net> - 1.2.5-1
- update to 1.2.5

* Wed Nov 29 2017 Remi Collet <remi@remirepo.net> - 1.2.4-1
- Update to 1.2.4
- switch to phpunit 6

* Wed Aug 16 2017 Remi Collet <remi@remirepo.net> - 1.2.3-2
- Update to 1.2.3
- drop patch merged upstream

* Wed Aug  9 2017 Remi Collet <remi@remirepo.net> - 1.2.2-2
- add patch for bigendian

* Mon Aug  7 2017 Remi Collet <remi@remirepo.net> - 1.2.2-1
- Update to 1.2.2

* Thu Aug  3 2017 Remi Collet <remi@remirepo.net> - 1.2.1-1
- Update to 1.2.1

* Tue Aug  1 2017 Remi Collet <remi@remirepo.net> - 1.2.0-1
- Update to 1.2.0

* Tue Jul 18 2017 Remi Collet <remi@remirepo.net> - 1.1.10-2
- rebuild for PHP 7.2.0beta1 new API

* Thu Jun 22 2017 Remi Collet <remi@remirepo.net> - 1.1.10-1
- Update to 1.1.10

* Fri Mar 24 2017 Remi Collet <remi@remirepo.net> - 1.1.8-1
- Update to 1.1.8

* Mon Feb 13 2017 Remi Collet <remi@fedoraproject.org> - 1.1.7-1
- Update to 1.1.7

* Thu Dec  1 2016 Remi Collet <remi@fedoraproject.org> - 1.1.6-3
- rebuild with PHP 7.1.0 GA

* Wed Sep 14 2016 Remi Collet <remi@fedoraproject.org> - 1.1.6-2
- rebuild for PHP 7.1 new API version

* Sun Sep 04 2016 Remi Collet <remi@fedoraproject.org> - 1.1.6-1
- Update to 1.1.6

* Thu Sep 01 2016 Remi Collet <remi@fedoraproject.org> - 1.1.5-1
- Update to 1.1.5

* Mon Aug 08 2016 Remi Collet <remi@fedoraproject.org> - 1.1.4-1
- Update to 1.1.4

* Mon Aug 08 2016 Remi Collet <remi@fedoraproject.org> - 1.1.3-1
- Update to 1.1.3
- Fix License tag

* Fri Aug 05 2016 Remi Collet <remi@fedoraproject.org> - 1.1.2-1
- Update to 1.1.2 (stable)

* Wed Aug 03 2016 Remi Collet <remi@fedoraproject.org> - 1.1.1-1
- Update to 1.1.1 (stable)

* Wed Aug 03 2016 Remi Collet <remi@fedoraproject.org> - 1.1.0-1
- Update to 1.1.0 (stable)

* Mon Aug 01 2016 Remi Collet <remi@fedoraproject.org> - 1.0.4-1
- Update to 1.0.4 (stable)

* Mon Aug 01 2016 Remi Collet <remi@fedoraproject.org> - 1.0.3-1
- Update to 1.0.3 (stable)

* Sat Jul 30 2016 Remi Collet <remi@fedoraproject.org> - 1.0.2-1
- Update to 1.0.2 (stable)

* Thu Jul 28 2016 Remi Collet <remi@fedoraproject.org> - 1.0.1-1
- Update to 1.0.1

* Thu Jul 28 2016 Remi Collet <remi@fedoraproject.org> - 1.0.0-1
- initial package, version 1.0.0 (devel)
  open tests/tests/Map/sort.php
  open https://github.com/php-ds/extension/pull/26

