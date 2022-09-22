# remirepo/fedora spec file for php-phpmyadmin-sql-parser5
#
# Copyright (c) 2015-2021 Remi Collet
# License: CC-BY-SA
# http://creativecommons.org/licenses/by-sa/4.0/
#
# Please, preserve the changelog entries
#

%bcond_without       tests

%global gh_commit    8ab99cd0007d880f49f5aa1807033dbfa21b1cb5
%global gh_short     %(c=%{gh_commit}; echo ${c:0:7})
%global gh_owner     phpmyadmin
#global gh_date      20150820
%global gh_project   sql-parser
%global ns_vendor    PhpMyAdmin
%global ns_project   SqlParser
%global major        5

Name:           php-%{gh_owner}-%{gh_project}%{major}
Version:        5.5.0
Release:        3%{?gh_date?%{gh_date}git%{gh_short}}%{?dist}
Summary:        A validating SQL lexer and parser with a focus on MySQL dialect

License:        GPLv2+
URL:            https://github.com/%{gh_owner}/%{gh_project}
Source0:        https://github.com/%{gh_owner}/%{gh_project}/archive/%{gh_commit}/%{name}-%{version}-%{?gh_short}.tar.gz

# Use our autoloader and locale relocation
Patch0:         %{name}-autoload.patch

BuildArch:      noarch
BuildRequires:  gettext
%if %{with tests}
BuildRequires:  php(language) >= 7.1
BuildRequires:  php-composer(phpmyadmin/motranslator) >= 3.0
BuildRequires:  php-mbstring
BuildRequires:  php-spl
# For tests, from composer.json "require-dev": {
#        "phpmyadmin/coding-standard": "^3.0",
#        "phpmyadmin/motranslator": "^4.0 || ^5.0",
#        "phpstan/extension-installer": "^1.1",
#        "phpstan/phpstan": "^1.2",
#        "phpstan/phpstan-phpunit": "^1.0",
#        "phpunit/php-code-coverage": "*",
#        "phpunit/phpunit": "^7.5 || ^8.5 || ^9.5",
#        "psalm/plugin-phpunit": "^0.16.1",
#        "vimeo/psalm": "^4.11",
#        "zumba/json-serializer": "^3.0"
BuildRequires:  phpunit9 >= 9.5
%global phpunit %{_bindir}/phpunit9
BuildRequires:  php-composer(zumba/json-serializer) >= 3.0
%endif
# For autoloader
BuildRequires:  php-composer(fedora/autoloader)

# From composer.json, "require": {
#        "php": "^7.1 || ^8.0",
#        "symfony/polyfill-mbstring": "^1.3"
# From composer.json, "conflict": {
#        "phpmyadmin/motranslator": "<3.0"
# From composer.json, "suggest": {
#        "ext-mbstring": "For best performance",
#        "phpmyadmin/motranslator": "Translate messages to your favorite locale"
Requires:       php(language) >= 7.1
Requires:       php-composer(phpmyadmin/motranslator) >= 3.0
# Mandatory to avoid symfony/polyfill-mbstring
Requires:       php-mbstring
# From phpcompatinfo report for 5.0.0
Requires:       php-spl
# For generated autoloader
Requires:       php-composer(fedora/autoloader)
# For commands
Requires:       php-cli

# Composer
Provides:       php-composer(%{gh_owner}/%{gh_project}) = %{version}


%description
A validating SQL lexer and parser with a focus on MySQL dialect.

This library was originally developed for phpMyAdmin during
the Google Summer of Code 2015.

Autoloader: %{_datadir}/php/%{ns_vendor}/%{ns_project}%{major}/autoload.php


%prep
%setup -q -n %{gh_project}-%{gh_commit}

%patch0 -p0 -b .rpm
find src -name \*rpm -exec rm {} \;

: Create autoloader
cat <<'AUTOLOAD' | tee src/autoload.php
<?php
/* Autoloader for %{name} and its dependencies */
require_once '%{_datadir}/php/Fedora/Autoloader/autoload.php';

\Fedora\Autoloader\Autoload::addPsr4('%{ns_vendor}\\%{ns_project}\\', __DIR__);
\Fedora\Autoloader\Dependencies::required([
    [
        '%{_datadir}/php/PhpMyAdmin/MoTranslator5/autoload.php',
        '%{_datadir}/php/PhpMyAdmin/MoTranslator/autoload.php',
    ]
]);
AUTOLOAD


%build
: Generate the locales
for loc in $(find locale -name \*.po)
do
   msgfmt --statistics --check -o ${loc%.po}.mo $loc
   rm $loc
done
rm locale/sqlparser.pot


%install
: Library
mkdir -p      %{buildroot}%{_datadir}/php/%{ns_vendor}
cp -pr src    %{buildroot}%{_datadir}/php/%{ns_vendor}/%{ns_project}%{major}
# keep locale in project dir as name seems too generic
cp -pr locale %{buildroot}%{_datadir}/php/%{ns_vendor}/%{ns_project}%{major}/locale

: Commands
install -Dpm 0755 bin/highlight-query %{buildroot}%{_bindir}/%{name}-highlight-query
install -Dpm 0755 bin/lint-query      %{buildroot}%{_bindir}/%{name}-lint-query
install -Dpm 0755 bin/tokenize-query  %{buildroot}%{_bindir}/%{name}-tokenize-query

%if 0%{?fedora} >= 12 || 0%{?rhel} >= 7
%find_lang sqlparser
%endif


%check
%if %{with tests}
mkdir vendor
cat << 'EOF' | tee vendor/autoload.php
<?php
require '%{buildroot}%{_datadir}/php/%{ns_vendor}/%{ns_project}%{major}/autoload.php';
\Fedora\Autoloader\Autoload::addPsr4('%{ns_vendor}\\%{ns_project}\\Tests\\', dirname(__DIR__).'/tests');
\Fedora\Autoloader\Dependencies::required([
    '%{_datadir}/php/Zumba/JsonSerializer/autoload.php',
]);
EOF

: fix commands
sed -e 's:%{_datadir}/php:%{buildroot}%{_datadir}/php:' -i bin/*query

ret=0
for cmdarg in "php %{phpunit}" php74 php80 php81; do
   if which $cmdarg; then
      set $cmdarg
      $1 ${2:-%{_bindir}/phpunit9} --no-coverage --verbose || ret=1
   fi
done
exit $ret
%else
: Test suite disabled
%endif


%files -f sqlparser.lang
%license LICENSE.txt
%doc composer.json
%doc README.md
%{_bindir}/%{name}-highlight-query
%{_bindir}/%{name}-lint-query
%{_bindir}/%{name}-tokenize-query
%dir %{_datadir}/php/%{ns_vendor}/%{ns_project}%{major}
     %{_datadir}/php/%{ns_vendor}/%{ns_project}%{major}/*php
     %{_datadir}/php/%{ns_vendor}/%{ns_project}%{major}/Components/
     %{_datadir}/php/%{ns_vendor}/%{ns_project}%{major}/Contexts/
     %{_datadir}/php/%{ns_vendor}/%{ns_project}%{major}/Exceptions/
     %{_datadir}/php/%{ns_vendor}/%{ns_project}%{major}/Statements/
     %{_datadir}/php/%{ns_vendor}/%{ns_project}%{major}/Tools/
     %{_datadir}/php/%{ns_vendor}/%{ns_project}%{major}/Utils/
%dir %{_datadir}/php/%{ns_vendor}/%{ns_project}%{major}/locale/
%dir %{_datadir}/php/%{ns_vendor}/%{ns_project}%{major}/locale/*/
%dir %{_datadir}/php/%{ns_vendor}/%{ns_project}%{major}/locale/*/LC_MESSAGES/


%changelog
* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 5.5.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 5.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Dec  9 2021 Remi Collet <remi@remirepo.net> - 5.5.0-1
- update to 5.5.0

* Fri Oct 29 2021 Remi Collet <remi@remirepo.net> - 5.4.2-3
- add upstream patches for PHP 8.1

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 5.4.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Feb  5 2021 Remi Collet <remi@remirepo.net> - 5.4.2-1
- update to 5.4.2

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 5.4.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Oct 16 2020 Remi Collet <remi@remirepo.net> - 5.4.1-1
- update to 5.4.1

* Fri Oct  9 2020 Remi Collet <remi@remirepo.net> - 5.4.0-1
- update to 5.4.0
- switch to phpunit9

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 5.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sat Mar 21 2020 Remi Collet <remi@remirepo.net> - 5.3.1-1
- update to 5.3.1

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 5.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jan  8 2020 Remi Collet <remi@remirepo.net> - 5.2.0-1
- update to 5.2.0

* Tue Nov 12 2019 Remi Collet <remi@remirepo.net> - 5.1.0-1
- update to 5.1.0
- drop patch merged upstream
- use phpunit8

* Thu Sep 19 2019 Remi Collet <remi@remirepo.net> - 5.0.0-2
- rename patch, use local copy instead of remote URI

* Mon Sep  2 2019 Remi Collet <remi@remirepo.net> - 5.0.0-1
- update to 5.0.0
- rename to php-phpmyadmin-sql-parser5
- move to /usr/share/php/PhpMyAdmin/SqlParser5
- raise dependency on PHP 7.1
- switch to phpunit7
- add patch for PHP 7.4 from
  https://github.com/phpmyadmin/sql-parser/pull/258

* Tue Jun  4 2019 Remi Collet <remi@remirepo.net> - 4.3.2-1
- update to 4.3.2
- add php-phpmyadmin-sql-parser-tokenize-query command

* Sun Jan  6 2019 Remi Collet <remi@remirepo.net> - 4.3.1-1
- update to 4.3.1

* Wed Dec 26 2018 Remi Collet <remi@remirepo.net> - 4.3.0-1
- update to 4.3.0

* Thu Nov  1 2018 Remi Collet <remi@remirepo.net> - 4.2.5-1
- update to 4.2.5
- switch to phpunit6

* Wed Feb 21 2018 Remi Collet <remi@remirepo.net> - 4.2.4-3
- allow motranslator v4

* Thu Dec  7 2017 Remi Collet <remi@remirepo.net> - 4.2.4-1
- Update to 4.2.4

* Wed Oct 11 2017 Remi Collet <remi@remirepo.net> - 4.2.3-1
- Update to 4.2.3

* Fri Sep 29 2017 Remi Collet <remi@remirepo.net> - 4.2.2-1
- Update to 4.2.2

* Sat Sep  9 2017 Remi Collet <remi@remirepo.net> - 4.2.1-1
- Update to 4.2.1

* Thu Aug 31 2017 Remi Collet <remi@remirepo.net> - 4.2.0-1
- Update to 4.2.0

* Mon Aug 21 2017 Remi Collet <remi@remirepo.net> - 4.1.10-1
- Update to 4.1.10

* Thu Jul 13 2017 Remi Collet <remi@remirepo.net> - 4.1.9-1
- Update to 4.1.9

* Sun Jul  9 2017 Remi Collet <remi@remirepo.net> - 4.1.8-1
- Update to 4.1.8

* Tue Jun  6 2017 Remi Collet <remi@remirepo.net> - 4.1.7-1
- Update to 4.1.7

* Fri Jun  2 2017 Remi Collet <remi@remirepo.net> - 4.1.6-1
- Update to 4.1.6

* Mon May 15 2017 Remi Collet <remi@remirepo.net> - 4.1.5-1
- Update to 4.1.5

* Fri May  5 2017 Remi Collet <remi@remirepo.net> - 4.1.4-1
- Update to 4.1.4

* Sun Apr 30 2017 Remi Collet <remi@remirepo.net> - 4.1.3-2
- fix lang files installation from review #1415686

* Thu Apr  6 2017 Remi Collet <remi@remirepo.net> - 4.1.3-1
- Update to 4.1.3

* Mon Feb 20 2017 Remi Collet <remi@fedoraproject.org> - 4.1.2-1
- update to 4.1.2

* Wed Feb  8 2017 Remi Collet <remi@fedoraproject.org> - 4.1.1-1
- update to 4.1.1

* Mon Jan 23 2017 Remi Collet <remi@fedoraproject.org> - 4.1.0-1
- update to 4.1.0
- add dependency on phpmyadmin/motranslator
- rename commands and always provide them
- manage locales

* Mon Jan 23 2017 Remi Collet <remi@fedoraproject.org> - 4.0.0-1
- update to 4.0.0
- rename to php-phpmyadmin-sql-parser

* Fri Jan 20 2017 Remi Collet <remi@fedoraproject.org> - 3.4.17-1
- update to 3.4.17
- sources from a git snapshot to retrieve test suite
- switch to PSR-4 autoloader

* Fri Jan  6 2017 Remi Collet <remi@fedoraproject.org> - 3.4.16-1
- update to 3.4.16

* Mon Jan  2 2017 Remi Collet <remi@fedoraproject.org> - 3.4.15-1
- update to 3.4.15

* Wed Nov 30 2016 Remi Collet <remi@fedoraproject.org> - 3.4.14-1
- update to 3.4.14

* Wed Nov 16 2016 Remi Collet <remi@fedoraproject.org> - 3.4.13-1
- update to 3.4.13

* Wed Nov  9 2016 Remi Collet <remi@fedoraproject.org> - 3.4.12-1
- update to 3.4.12
- switch to fedora/autoloader

* Tue Oct 25 2016 Remi Collet <remi@fedoraproject.org> - 3.4.11-1
- update to 3.4.11

* Tue Oct  4 2016 Remi Collet <remi@fedoraproject.org> - 3.4.10-1
- update to 3.4.10

* Mon Oct  3 2016 Remi Collet <remi@fedoraproject.org> - 3.4.9-1
- update to 3.4.9

* Thu Sep 22 2016 Remi Collet <remi@fedoraproject.org> - 3.4.8-1
- update to 3.4.8 (no change)

* Tue Sep 20 2016 Remi Collet <remi@fedoraproject.org> - 3.4.7-1
- update to 3.4.7

* Tue Sep 13 2016 Remi Collet <remi@fedoraproject.org> - 3.4.6-1
- update to 3.4.6
- lower dependency on php >= 5.3

* Tue Sep 13 2016 Remi Collet <remi@fedoraproject.org> - 3.4.5-1
- update to 3.4.5

* Tue Jul 26 2016 Remi Collet <remi@fedoraproject.org> - 3.4.4-1
- update to 3.4.4
- switch from udan11/sql-parser to phpmyadmin/sql-parser
- add sql-parser-highlight-query and sql-parser-lint-query commands

* Tue Mar  1 2016 Remi Collet <remi@fedoraproject.org> - 3.4.0-1
- update to 3.4.0 (for phpMyAdmin 4.5.5.1)
- add patch from phpMyAdmin
- raise dependency on php >= 5.4

* Tue Feb 23 2016 Remi Collet <remi@fedoraproject.org> - 3.3.1-1
- update to 3.3.1 (for phpMyAdmin 4.5.5)
- don't run test with old PHPUnit (EPEL-6)

* Sat Dec 26 2015 Remi Collet <remi@fedoraproject.org> - 3.0.8-1
- update to 3.0.8 (for phpMyAdmin 4.5.3)

* Fri Nov 13 2015 Remi Collet <remi@fedoraproject.org> - 3.0.7-1
- update to 3.0.7
- run test suite with both PHP 5 and 7 when available

* Sun Nov  8 2015 Remi Collet <remi@fedoraproject.org> - 3.0.5-1
- update to 3.0.5

* Thu Oct 22 2015 Remi Collet <remi@fedoraproject.org> - 3.0.4-1
- update to 3.0.4 (for upcoming phpMyAdmin 4.5.1)

* Mon Oct 19 2015 Remi Collet <remi@fedoraproject.org> - 3.0.3-1
- update to 3.0.3 (for upcoming phpMyAdmin 4.5.1)

* Wed Sep 23 2015 Remi Collet <remi@fedoraproject.org> - 1.0.0-2
- upstream patch for phpMyAdmin 4.5.0.2

* Wed Sep 23 2015 Remi Collet <remi@fedoraproject.org> - 1.0.0-1
- tagged as 1.0.0 (no change)

* Sun Sep 20 2015 Remi Collet <remi@fedoraproject.org> - 0-0.3.20150820git1b2988f
- fix provides and self-obsoletion (review #1262807)

* Mon Sep 14 2015 Remi Collet <remi@fedoraproject.org> - 0-0.2.20150820git1b2988f
- rename to php-udan11-sql-parser

* Mon Sep 14 2015 Remi Collet <remi@fedoraproject.org> - 0-0.1.20150629git4aaed44
- initial package
