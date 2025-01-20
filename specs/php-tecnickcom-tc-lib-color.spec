# remirepo/fedora spec file for php-tecnickcom-tc-lib-color
#
# SPDX-FileCopyrightText:  Copyright 2015-2024 Remi Collet
# SPDX-License-Identifier: CECILL-2.1
# http://www.cecill.info/licences/Licence_CeCILL_V2-en.txt
#
# Please, preserve the changelog entries
#
%global gh_commit    5fe3c1771ab577572b3304d11496745aff45db8e
%global gh_short     %(c=%{gh_commit}; echo ${c:0:7})
%global c_vendor     tecnickcom
%global gh_owner     tecnickcom
%global gh_project   tc-lib-color
%global php_project  %{_datadir}/php/Com/Tecnick/Color
%global with_tests   0%{!?_without_tests:1}

Name:           php-%{gh_owner}-%{gh_project}
Version:        2.2.7
Release:        2%{?dist}
Summary:        PHP library to manipulate various color representations

License:        LGPL-3.0-or-later
URL:            https://github.com/%{gh_owner}/%{gh_project}
Source0:        https://github.com/%{gh_owner}/%{gh_project}/archive/%{gh_commit}/%{name}-%{version}-%{?gh_short}.tar.gz

BuildArch:      noarch
%if %{with_tests}
# For tests
%global phpunit %{_bindir}/phpunit10
BuildRequires:  phpunit10 >= 10.5.40
BuildRequires:  php(language) >= 8.1
BuildRequires:  php-pcre
%endif
BuildRequires:  php-fedora-autoloader-devel

# From composer.json, "require": {
#        "php": ">=8.1",
#        "ext-pcre": "*"
Requires:       php(language) >= 8.1
Requires:       php-pcre
# From phpcompatinfo report for version 1.12.4
# none
Requires:       php-composer(fedora/autoloader)

# Composer
Provides:       php-composer(%{c_vendor}/%{gh_project}) = %{version}
# Upstream package name
Provides:       php-%{gh_project} = %{version}


%description
Provides tc-lib-color: PHP library to manipulate various color
representations (GRAY, RGB, HSL, CMYK) and parse Web colors.

The initial source code has been extracted from TCPDF (http://www.tcpdf.org).


%prep
%setup -q -n %{gh_project}-%{gh_commit}

: Sanity check
grep -q '^%{version}$' VERSION

: Fix the examples
sed -e 's:^require:////require:' \
    -e 's:^//require:require:'   \
    -i example/*php


%build
phpab --template fedora --output src/autoload.php src


%install
mkdir -p   $(dirname %{buildroot}%{php_project})
cp -pr src %{buildroot}%{php_project}


%check
%if %{with_tests}
mkdir vendor
cat << 'EOF' | tee vendor/autoload.php
<?php
require '%{buildroot}%{php_project}/autoload.php';
\Fedora\Autoloader\Autoload::addPsr4('Test\\', dirname(__DIR__) . '/test');
EOF

ret=0
# TODO php84 https://github.com/tecnickcom/tc-lib-color/issues/14
for cmdarg in php php81 php82 php83 php84; do
   if which $cmdarg; then
      set $cmdarg
      cp phpunit.xml.dist phpunit.xml
      $1 ${2:-%{phpunit}} --migrate-configuration || :
      $1 ${2:-%{phpunit}} --no-coverage \
        || ret=1
   fi
done
exit $ret
%else
: Test suite disabled
%endif


%files
%license LICENSE
%doc composer.json
%doc *.md example
%dir %{_datadir}/php/Com
%dir %{_datadir}/php/Com/Tecnick
%{php_project}


%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Dec 26 2024 Remi Collet <remi@remirepo.net> - 2.2.7-1
- update to 2.2.7
- raise dependency on PHP 8.1

* Mon Dec 23 2024 Remi Collet <remi@remirepo.net> - 2.2.6-1
- update to 2.2.6 (no change)
- re-license spec file to CECILL-2.1

* Mon Nov 25 2024 Remi Collet <remi@remirepo.net> - 2.2.5-1
- update to 2.2.5 (no change)

* Mon Oct 28 2024 Remi Collet <remi@remirepo.net> - 2.2.4-1
- update to 2.2.4

* Mon Sep  9 2024 Remi Collet <remi@remirepo.net> - 2.2.3-1
- update to 2.2.3 (no change)

* Mon Aug 19 2024 Remi Collet <remi@remirepo.net> - 2.2.2-1
- update to 2.2.2

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Apr 12 2024 Remi Collet <remi@remirepo.net> - 2.0.8-1
- update to 2.0.8 (no change)

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Tue Nov 28 2023 Remi Collet <remi@remirepo.net> - 2.0.5-1
- update to 2.0.5 (no change)

* Wed Nov 22 2023 Remi Collet <remi@remirepo.net> - 2.0.4-1
- update to 2.0.4
- raise dependency on PHP 8

* Mon Oct 23 2023 Remi Collet <remi@remirepo.net> - 1.14.39-1
- update to 1.14.39 (no change)

* Thu Oct 12 2023 Remi Collet <remi@remirepo.net> - 1.14.37-1
- update to 1.14.37

* Tue Oct 10 2023 Remi Collet <remi@remirepo.net> - 1.14.32-1
- update to 1.14.32

* Tue Oct 10 2023 Remi Collet <remi@remirepo.net> - 1.14.29-1
- update to 1.14.29

* Wed Sep  6 2023 Remi Collet <remi@remirepo.net> - 1.14.28-1
- update to 1.14.28 (no change)

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.14.24-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed May 24 2023 Remi Collet <remi@remirepo.net> - 1.14.24-1
- update to 1.14.24 (no change)

* Fri May  5 2023 Remi Collet <remi@remirepo.net> - 1.14.23-1
- update to 1.14.23 (no change)

* Thu May  4 2023 Remi Collet <remi@remirepo.net> - 1.14.21-1
- update to 1.14.21 (no change)

* Wed May  3 2023 Remi Collet <remi@remirepo.net> - 1.14.19-1
- update to 1.14.19 (no change)

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.14.18-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Dec 22 2022 Remi Collet <remi@remirepo.net> - 1.14.18-1
- update to 1.14.18 (no change)

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.14.14-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue Jun 14 2022 Remi Collet <remi@remirepo.net> - 1.14.14-1
- update to 1.14.14 (no change)

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.14.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Mon Jan  3 2022 Remi Collet <remi@remirepo.net> - 1.14.10-1
- update to 1.14.10 (no change)

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.14.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon Feb  8 2021 Remi Collet <remi@remirepo.net> - 1.14.6-1
- update to 1.14.6 (no change)

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.14.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Dec 21 2020 Remi Collet <remi@remirepo.net> - 1.14.1-1
- update to 1.14.1
- switch to classmap autoloader

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.12.15-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.12.15-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jan  3 2020 Remi Collet <remi@remirepo.net> - 1.12.15-1
- update to 1.12.15 (no change)

* Fri Sep 20 2019 Remi Collet <remi@remirepo.net> - 1.12.13-1
- update to 1.12.13

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.12.12-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.12.12-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.12.12-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Jun 25 2018 Remi Collet <remi@remirepo.net> - 1.12.12-1
- update to 1.12.12 (no change)

* Tue May 15 2018 Remi Collet <remi@remirepo.net> - 1.12.11-1
- update to 1.12.11 (no change)

* Mon May 14 2018 Remi Collet <remi@remirepo.net> - 1.12.10-1
- update to 1.12.10 (no change)
- switch to phpunit7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.12.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Jan  2 2018 Remi Collet <remi@remirepo.net> - 1.12.8-1
- Update to 1.12.8 (no change)

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.12.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Feb 12 2017 Remi Collet <remi@fedoraproject.org> - 1.12.6-1
- update to 1.12.6 (no change)
- use phpunit6 on F26+

* Mon Feb  6 2017 Remi Collet <remi@fedoraproject.org> - 1.12.4-1
- update to 1.12.4 (no change)

* Fri Sep  2 2016 Remi Collet <remi@fedoraproject.org> - 1.12.1-1
- update to 1.12.1

* Tue Jun 14 2016 Remi Collet <remi@fedoraproject.org> - 1.11.0-1
- update to 1.11.0
- raise dependency on php >= 5.4
- run test suite with both PHP 5 and 7 when available

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Oct 19 2015 Remi Collet <remi@fedoraproject.org> - 1.6.2-1
- update to 1.6.2

* Sun Sep 13 2015 Remi Collet <remi@fedoraproject.org> - 1.5.2-1
- update to 1.5.2
- provide php-composer(tecnickcom/tc-lib-color)

* Fri Jul 24 2015 Remi Collet <remi@fedoraproject.org> - 1.5.1-1
- update to 1.5.1 (no change)

* Thu Jul  2 2015 Remi Collet <remi@fedoraproject.org> - 1.5.0-1
- update to 1.5.0

* Wed Jul  1 2015 Remi Collet <remi@fedoraproject.org> - 1.4.5-1
- initial package, version 1.4.5
