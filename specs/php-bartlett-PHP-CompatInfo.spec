# remirepo/fedora spec file for php-bartlett-PHP-CompatInfo
#
# Copyright (c) 2011-2024 Remi Collet
# License: CC-BY-SA-4.0
# http://creativecommons.org/licenses/by-sa/4.0/
#
# Please, preserve the changelog entries
#


%bcond_with          generators

%{!?php_version:  %global php_version  %(php -r 'echo PHP_VERSION;' 2>/dev/null)}
%global gh_commit    9875282a35266aa2b66416303c06edcd70fc50a1
%global gh_short     %(c=%{gh_commit}; echo ${c:0:7})
%global gh_date      2024-04-24
%global gh_owner     llaville
%global gh_project   php-compatinfo

%global upstream_version  7.1.4
#global upstream_prever   RC1

Name:           php-bartlett-PHP-CompatInfo
Version:        %{upstream_version}%{?upstream_prever:~%{upstream_prever}}
Release:        5%{?dist}
Summary:        Find out version and the extensions required for a piece of code to run

# SPDX: see bundled libraries list below
License:        BSD-3-Clause and MIT
URL:            https://github.com/llaville/php-compatinfo
Source0:        %{name}-%{version}-%{gh_short}.tgz
# Script for fedora-review
Source1:        fedora-review-check
# Generate the archive will all dependencies
Source9:        makesrc.sh

# Relocate the database
Patch0:         %{name}-6.0.0-rpm.patch

BuildArch:      noarch
BuildRequires:  php(language) >= 8.1
BuildRequires:  php-cli
BuildRequires:  php-json
%if %{with generators}
BuildRequires:  composer-generators
%endif

Requires:       php(language) >= 8.1
Requires:       php-cli
Requires:       php-dom
Requires:       php-json
Requires:       php-libxml
Requires:       php-pcre
Requires:       php-phar
Requires:       php-pdo
Requires:       php-pdo_sqlite
Requires:       php-simplexml
Requires:       php-spl
Requires:       php-xmlreader

%if %{without generators}
# Bundled libraries
# License BSD-3-Clause
Provides: bundled(php-composer(bartlett/php-compatinfo-db)) = 6.12.0
Provides: bundled(php-composer(nikic/php-parser)) = v5.3.1
# License MIT
Provides: bundled(php-composer(bartlett/sarif-php-sdk)) = 1.5.0
Provides: bundled(php-composer(brick/math)) = 0.12.1
Provides: bundled(php-composer(composer/semver)) = 3.4.3
Provides: bundled(php-composer(doctrine/cache)) = 2.2.0
Provides: bundled(php-composer(doctrine/collections)) = 1.8.0
Provides: bundled(php-composer(doctrine/common)) = 3.4.5
Provides: bundled(php-composer(doctrine/dbal)) = 3.9.3
Provides: bundled(php-composer(doctrine/deprecations)) = 1.1.3
Provides: bundled(php-composer(doctrine/event-manager)) = 2.0.1
Provides: bundled(php-composer(doctrine/inflector)) = 2.0.10
Provides: bundled(php-composer(doctrine/instantiator)) = 2.0.0
Provides: bundled(php-composer(doctrine/lexer)) = 3.0.1
Provides: bundled(php-composer(doctrine/orm)) = 2.20.0
Provides: bundled(php-composer(doctrine/persistence)) = 3.4.0
Provides: bundled(php-composer(psr/cache)) = 3.0.0
Provides: bundled(php-composer(psr/clock)) = 1.0.0
Provides: bundled(php-composer(psr/container)) = 2.0.2
Provides: bundled(php-composer(psr/event-dispatcher)) = 1.0.0
Provides: bundled(php-composer(psr/log)) = 3.0.2
Provides: bundled(php-composer(ramsey/collection)) = 2.0.0
Provides: bundled(php-composer(ramsey/uuid)) = 4.7.6
Provides: bundled(php-composer(symfony/cache)) = v6.4.14
Provides: bundled(php-composer(symfony/cache-contracts)) = v3.5.0
Provides: bundled(php-composer(symfony/clock)) = v6.4.13
Provides: bundled(php-composer(symfony/config)) = v6.4.14
Provides: bundled(php-composer(symfony/console)) = v6.4.14
Provides: bundled(php-composer(symfony/dependency-injection)) = v6.4.13
Provides: bundled(php-composer(symfony/deprecation-contracts)) = v3.5.0
Provides: bundled(php-composer(symfony/event-dispatcher)) = v6.4.13
Provides: bundled(php-composer(symfony/event-dispatcher-contracts)) = v3.5.0
Provides: bundled(php-composer(symfony/filesystem)) = v6.4.13
Provides: bundled(php-composer(symfony/finder)) = v6.4.13
Provides: bundled(php-composer(symfony/http-client)) = v6.4.14
Provides: bundled(php-composer(symfony/http-client-contracts)) = v3.5.0
Provides: bundled(php-composer(symfony/messenger)) = v6.4.13
Provides: bundled(php-composer(symfony/polyfill-ctype)) = v1.31.0
Provides: bundled(php-composer(symfony/polyfill-intl-grapheme)) = v1.31.0
Provides: bundled(php-composer(symfony/polyfill-intl-normalizer)) = v1.31.0
Provides: bundled(php-composer(symfony/polyfill-mbstring)) = v1.31.0
Provides: bundled(php-composer(symfony/polyfill-php72)) = v1.31.0
Provides: bundled(php-composer(symfony/polyfill-php80)) = v1.31.0
Provides: bundled(php-composer(symfony/polyfill-php83)) = v1.31.0
Provides: bundled(php-composer(symfony/polyfill-php84)) = v1.31.0
Provides: bundled(php-composer(symfony/process)) = v6.4.14
Provides: bundled(php-composer(symfony/requirements-checker)) = v2.0.1
Provides: bundled(php-composer(symfony/serializer)) = v6.4.13
Provides: bundled(php-composer(symfony/service-contracts)) = v3.5.0
Provides: bundled(php-composer(symfony/stopwatch)) = v6.4.13
Provides: bundled(php-composer(symfony/string)) = v6.4.13
Provides: bundled(php-composer(symfony/var-exporter)) = v6.4.13

Provides: php-composer(bartlett/php-compatinfo) = %{version}
%endif
Provides: phpcompatinfo = %{version}


%description
PHP_CompatInfo will parse a file/folder/array to find out the minimum
version and extensions required for it to run. CLI version has many reports
(extension, interface, class, function, constant) to display and ability to
show content of dictionary references.


%prep
%setup -q -n %{gh_project}-%{gh_commit}
%patch -P0 -p1 -b .rpm
rm bin/*rpm

# https://github.com/llaville/php-compatinfo-db/issues/112
sed -e 's/touch/@touch/' -i vendor/bartlett/php-compatinfo-db/config/set/default.php

: Gather all license files and cleanup tests
mv vendor/composer/LICENSE composer_LICENSE
for vendor in $(ls vendor)
do
  for proj in $(ls vendor/$vendor)
  do
    [ -d vendor/$vendor/$proj/tests ]   && rm -r vendor/$vendor/$proj/tests
    [ -f vendor/$vendor/$proj/LICENSE ] && mv vendor/$vendor/$proj/LICENSE ${vendor}_${proj}_LICENSE
  done
done
rm -r vendor/bartlett/*/.github
rm -r vendor/bartlett/*/.changes

: Hack for PHP 8.4
sed -e '/php83/d;s/php82/php83/' config/set/up-to-php83.php | tee config/set/up-to-php84.php

%if %{without generators}
: List bundled libraries and Licenses
php -r '
    $pkgs = file_get_contents("vendor/composer/installed.json");
    $pkgs = json_decode($pkgs, true);
    if (!is_array($pkgs) || !isset($pkgs["packages"])) {
        echo "cant decode json file\n";
        exit(3);
    }
    $res = [];
    foreach($pkgs["packages"] as $pkg) {
        $lic = implode(" and ", $pkg["license"]);
        if (!isset($res[$lic])) $res[$lic] = [];
        $res[$lic][] = sprintf("Provides: bundled(php-composer(%s)) = %s", $pkg["name"], $pkg["version"]);
    }
    foreach($res as $lic => $lib) {
        sort($lib);
        printf("# License %s\n%s\n", $lic, implode("\n", $lib));
    }
'
%endif


%build
# Nothing


%install
mkdir -p %{buildroot}%{_datadir}/%{name}
for i in bin config data resources src vendor composer.*
do cp -pr $i %{buildroot}%{_datadir}/%{name}/$i
done

mkdir -p %{buildroot}%{_bindir}
ln -s ../share/%{name}/bin/phpcompatinfo %{buildroot}%{_bindir}/phpcompatinfo

mkdir -p %{buildroot}%{_mandir}/man1
mv %{buildroot}%{_datadir}/%{name}/bin/phpcompatinfo.1 \
   %{buildroot}%{_mandir}/man1/phpcompatinfo.1

install -D -p -m 755 %{SOURCE1} \
   %{buildroot}%{_datadir}/%{name}/fedora-review-check


%check
%{buildroot}%{_bindir}/phpcompatinfo --version | grep %{version} && exit 0


%files
%license *LICENSE
%doc *md
%doc docs
%doc examples
%doc composer.json
%doc vendor/composer/installed.json
%{_bindir}/phpcompatinfo
%{_datadir}/%{name}
%{_mandir}/man1/phpcompatinfo.1*


%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 7.1.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Nov  7 2024 Remi Collet <remi@remirepo.net> - 7.1.4-4
- hack for PHP 8.4

* Thu Nov  7 2024 Remi Collet <remi@remirepo.net> - 7.1.4-3
- update bundled bartlett/php-compatinfo-db to 6.12.0
- update bundled dependencies
- optional support build with composer-generators

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 7.1.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Apr 24 2024 Remi Collet <remi@remirepo.net> - 7.1.4-1
- update to 7.1.4
- update bundled bartlett/php-compatinfo-db to 6.5.0

* Tue Mar 19 2024 Remi Collet <remi@remirepo.net> - 7.1.3-1
- update to 7.1.3
- update bundled bartlett/php-compatinfo-db to 6.4.2

* Thu Feb  8 2024 Remi Collet <remi@remirepo.net> - 7.1.2-1
- update to 7.1.2
- update bundled bartlett/php-compatinfo-db to 6.2.1

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 7.1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 7.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jan 18 2024 Remi Collet <remi@remirepo.net> - 7.1.1-1
- update to 7.1.1
- cleanup installation tree
- move docs and examples in package documentation

* Tue Jan  2 2024 Remi Collet <remi@remirepo.net> - 7.1.0-1
- update to 7.1.0

* Wed Dec  6 2023 Remi Collet <remi@remirepo.net> - 7.0.2-1
- update to 7.0.2
- update bundled bartlett/php-compatinfo-db to 6.0.0
- open https://github.com/llaville/php-compatinfo/issues/365 8.0 compatibility
- raise dependency on PHP 8.1

* Tue Nov 14 2023 Remi Collet <remi@remirepo.net> - 7.0.1-1
- update to 7.0.1
- update bundled bartlett/php-compatinfo-db to 5.13.0

* Mon Nov 13 2023 Remi Collet <remi@remirepo.net> - 7.0.0-3
- update bundled bartlett/php-compatinfo-db to 5.12.0

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 7.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue May 16 2023 Remi Collet <remi@remirepo.net> - 7.0.0-1
- update to 7.0.0
- raise dependency on PHP 8.0
- update bundled bartlett/php-compatinfo-db to 5.5.0

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 6.5.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Tue Jan 10 2023 Remi Collet <remi@remirepo.net> - 6.5.4-2
- update bundled bartlett/php-compatinfo-db to 4.11.0

* Wed Dec 14 2022 Remi Collet <remi@remirepo.net> - 6.5.4-1
- update to 6.5.4
- update bundled bartlett/php-compatinfo-db to 4.10.0

* Mon Nov  7 2022 Remi Collet <remi@remirepo.net> - 6.5.3-1
- update to 6.5.3
- update bundled bartlett/php-compatinfo-db to 4.8.0

* Tue Oct 25 2022 Remi Collet <remi@remirepo.net> - 6.5.2-1
- update to 6.5.2

* Tue Sep 27 2022 Remi Collet <remi@remirepo.net> - 6.4.2-1
- update to 6.4.2

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 6.4.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Apr 20 2022 Remi Collet <remi@remirepo.net> - 6.4.1-2
- update bundled bartlett/php-compatinfo-db to 4.2.0

* Thu Apr  7 2022 Remi Collet <remi@remirepo.net> - 6.4.1-1
- update to 6.4.1

* Wed Apr  6 2022 Remi Collet <remi@remirepo.net> - 6.4.0-1
- update to 6.4.0
- update bundled bartlett/php-compatinfo-db to 4.2.0

* Mon Mar  7 2022 Remi Collet <remi@remirepo.net> - 6.3.0-1
- update to 6.3.0
- update bundled bartlett/php-compatinfo-db to 4.1.0

* Mon Feb  7 2022 Remi Collet <remi@remirepo.net> - 6.2.0-1
- update to 6.2.0
- update bundled bartlett/php-compatinfo-db to 4.0.0

* Fri Jan 28 2022 Remi Collet <remi@remirepo.net> - 6.1.2-1
- update to 6.1.2

* Thu Jan 27 2022 Remi Collet <remi@remirepo.net> - 6.1.1-5
- update bundled bartlett/php-compatinfo-db 3.18.0
- use better process to create the database, as discussed on
  https://github.com/llaville/php-compatinfo-db/issues/113
- silent touch on read only database, reported as
  https://github.com/llaville/php-compatinfo-db/issues/112

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 6.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Jan 18 2022 Remi Collet <remi@remirepo.net> - 6.1.1-1
- update to 6.1.1
- update bundled bartlett/php-compatinfo-db 3.17.1

* Thu Jan  6 2022 Remi Collet <remi@remirepo.net> - 6.1.0-1
- update to 6.1.0

* Wed Jan  5 2022 Remi Collet <remi@remirepo.net> - 6.0.3-1
- update to 6.0.3
- use all PHP bundled libraries instead of system ones

* Mon Jan  3 2022 Remi Collet <remi@remirepo.net> - 6.0.2-1
- update to 6.0.2
- open https://github.com/llaville/php-compatinfo/issues/316
  regression, compatibility with Symfony 4

* Mon Dec 13 2021 Remi Collet <remi@remirepo.net> - 6.0.1-1
- update to 6.0.1
- raise dependency on PHP 7.4
- drop dependency on bartlett/php-reflect
- add dependency on nikic/php-parser

* Fri Dec 10 2021 Remi Collet <remi@remirepo.net> - 5.5.4-1
- update to 5.5.4
- raise dependency on bartlett/php-compatinfo-db 3.6

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 5.5.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon May  3 2021 Remi Collet <remi@remirepo.net> - 5.5.3-1
- update to 5.5.3

* Tue Apr 13 2021 Remi Collet <remi@remirepo.net> - 5.5.2-1
- update to 5.5.2

* Mon Mar 15 2021 Remi Collet <remi@remirepo.net> - 5.5.1-1
- update to 5.5.1
- raise dependency on PHP 7.2
- raise dependency on bartlett/php-compatinfo-db 3.4

* Mon Feb 22 2021 Remi Collet <remi@remirepo.net> - 5.4.4-1
- update to 5.4.4 (no change)

* Mon Feb 15 2021 Remi Collet <remi@remirepo.net> - 5.4.3-1
- update to 5.4.3

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 5.4.2-1.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Nov 23 2020 Remi Collet <remi@remirepo.net> - 5.4.2-1
- update to 5.4.2

* Tue Oct  6 2020 Remi Collet <remi@remirepo.net> - 5.4.1-1
- update to 5.4.1
- switch to phpunit9
- add dependency on ramsey/uuid
- add dependency on symfony components: config, console, dependency-injection,
  event-dispatcher, finder, serializer and stopwatch
- add dependency on doctrine/collections
- drop dependency on doctrine/cache
- switch to classmap autoloader
- drop configuration file (no more supported)

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 5.3.0-1.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul  8 2020 Remi Collet <remi@remirepo.net> - 5.3.0-1
- update to 5.3.0
- raise dependency on PHP 7.1.3
- raise dependency on bartlett/php-reflect 4.4
- raise dependency on bartlett/php-compatinfo-db 2.0
- switch to phpunit8

* Wed Apr 29 2020 Remi Collet <remi@remirepo.net> - 5.2.3-1
- update to 5.2.3

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 5.2.1-1.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Oct 22 2019 Remi Collet <remi@remirepo.net> - 5.2.1-1
- update to 5.2.1 (no change)

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 5.2.0-1.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Jun  3 2019 Remi Collet <remi@remirepo.net> - 5.2.0-1
- update to 5.2.0
- allow bartlett/php-compatinfo-db v2

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 5.1.0-1.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Nov 28 2018 Remi Collet <remi@remirepo.net> - 5.1.0-1
- update to 5.1.0
- raise dependency on bartlett/php-reflect 4.3
- add explicit dependency on nikic/php-parser
- add explicit dependency on doctrine/cache
- add dependency on psr/log
- switch to phpunit7

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.12-1.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.12-1.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Feb  2 2018 Remi Collet <remi@remirepo.net> - 5.0.12-1
- Update to 5.0.12 (no change)
- use range dependency on F27+

* Tue Dec 12 2017 Remi Collet <remi@remirepo.net> - 5.0.11-1
- Update to 5.0.11 (no change)
- raise dependency on PHP 5.5

* Tue Dec 12 2017 Remi Collet <remi@remirepo.net> - 5.0.10-1
- Update to 5.0.10 (no change)
- raise dependency on bartlett/php-reflect 4.2
- only require a single Symfony version

* Wed Dec  6 2017 Remi Collet <remi@remirepo.net> - 5.0.9-1
- Update to 5.0.9

* Mon Aug  7 2017 Remi Collet <remi@remirepo.net> - 5.0.8-1
- Update to 5.0.8

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.7-1.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Jun 10 2017 Remi Collet <remi@remirepo.net> - 5.0.7-1
- Update to 5.0.7

* Mon Mar 27 2017 Remi Collet <remi@remirepo.net> - 5.0.6-1
- Update to 5.0.6

* Fri Mar 17 2017 Remi Collet <remi@remirepo.net> - 5.0.5-1
- Update to 5.0.5

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.4-1.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Jan 17 2017 Remi Collet <remi@fedoraproject.org> - 5.0.4-1
- update to 5.0.4

* Wed Jan 11 2017 Remi Collet <remi@fedoraproject.org> - 5.0.3-1
- update to 5.0.3

* Fri Dec 16 2016 Remi Collet <remi@fedoraproject.org> - 5.0.2-1
- update to 5.0.2

* Mon Oct 31 2016 Remi Collet <remi@fedoraproject.org> - 5.0.1-2
- switch to fedora/autoloader

* Wed Jul  6 2016 Remi Collet <remi@fedoraproject.org> - 5.0.1-1
- update to 5.0.1
- display DB version instead of build date

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Dec 10 2015 Remi Collet <remi@fedoraproject.org> - 5.0.0-1
- update to 5.0.0
- raise dependency on bartlett/php-reflect ~4.0
- raise minimal php version to 5.4
- add dependency on bartlett/php-compatinfo-db

* Wed Nov 25 2015 Remi Collet <remi@fedoraproject.org> - 4.5.2-1
- update to 4.5.2

* Sun Oct 11 2015 Remi Collet <remi@fedoraproject.org> - 4.5.1-1
- update to 4.5.1

* Tue Oct  6 2015 Remi Collet <remi@fedoraproject.org> - 4.5.0-1
- update to 4.5.0

* Mon Jul 20 2015 Remi Collet <remi@fedoraproject.org> - 4.4.0-2
- add upstream patch for Intl reference

* Mon Jul 13 2015 Remi Collet <remi@fedoraproject.org> - 4.4.0-1
- update to 4.4.0

* Mon Jun 29 2015 Remi Collet <remi@fedoraproject.org> - 4.3.0-4
- upstream patch for ldap extension in 5.6.11RC1 (thanks Koschei)

* Fri Jun 26 2015 Remi Collet <remi@fedoraproject.org> - 4.3.0-3
- rewrite autoloader

* Sun Jun 21 2015 Remi Collet <remi@fedoraproject.org> - 4.3.0-2
- fix autoloader

* Tue Jun 16 2015 Remi Collet <remi@fedoraproject.org> - 4.3.0-1
- update to 4.3.0

* Tue May 19 2015 Remi Collet <remi@fedoraproject.org> - 4.2.0-1
- update to 4.2.0
- raise dependency on bartlett/php-reflect 3.1
- add dependency on bartlett/umlwriter
- add fedora-review-check script
- handle --without tests option to skip test suite during build

* Mon Feb  2 2015 Remi Collet <remi@fedoraproject.org> - 3.7.3-1
- Update to 3.7.3

* Mon Jan  5 2015 Remi Collet <remi@fedoraproject.org> - 3.7.2-1
- Update to 3.7.2
- open https://github.com/llaville/php-compat-info/pull/157

* Fri Dec 19 2014 Remi Collet <remi@fedoraproject.org> - 3.7.1-1
- Update to 3.7.1

* Thu Nov 20 2014 Remi Collet <remi@fedoraproject.org> - 3.6.1-1
- Update to 3.6.1

* Thu Nov 13 2014 Remi Collet <remi@fedoraproject.org> - 3.6.0-1
- Update to 3.6.0
- add dependency on justinrainbow/json-schema
- raise dependency on bartlett/php-reflect 2.6

* Thu Oct 16 2014 Remi Collet <remi@fedoraproject.org> - 3.5.0-1
- Update to 3.5.0
- add dependency on sebastian/version
- raise dependency on bartlett/php-reflect 2.5

* Mon Oct  6 2014 Remi Collet <remi@fedoraproject.org> - 3.4.0-2
- fix FTBFS with PHP 5.6.1 (Thanks to Koschei)

* Thu Sep 25 2014 Remi Collet <remi@fedoraproject.org> - 3.4.0-1
- Update to 3.4.0

* Fri Aug 22 2014 Remi Collet <remi@fedoraproject.org> - 3.3.0-1
- Update to 3.2.0
- add dependency on seld/jsonlint
- raise dependency on bartlett/php-reflect 2.3
- enable the cache plugin in default configuration

* Fri Jul 25 2014 Remi Collet <remi@fedoraproject.org> - 3.2.0-1
- Update to 3.2.0
- add manpage
- sources from github
- patch autoloader to not rely on composer
- drop documentation (link to online doc in description)
- add upstream patch for SNMP extension

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.26.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Dec 13 2013 Remi Collet <remi@fedoraproject.org> - 2.26.0-1
- Update to 2.26.0 (stable)

* Thu Nov 14 2013 Remi Collet <remi@fedoraproject.org> - 2.25.0-1
- Update to 2.25.0
- remove phpci temporary compat command

* Fri Oct 18 2013 Remi Collet <remi@fedoraproject.org> - 2.24.0-1
- update to 2.24.0
- raise dependency, PHP_Reflect 1.9.0

* Mon Sep 23 2013 Remi Collet <remi@fedoraproject.org> - 2.23.1-1
- Update to 2.23.1
- raise dependencies: PHP 5.3.0, PHP_Reflect 1.8.0 (and < 2)

* Fri Aug 23 2013 Remi Collet <remi@fedoraproject.org> - 2.22.0-1
- Update to 2.22.0

* Tue Aug 20 2013 Remi Collet <remi@fedoraproject.org> - 2.21.0-1
- Update to 2.21.0
- patch for https://github.com/llaville/php-compat-info/issues/99

* Thu Jul 25 2013 Remi Collet <remi@fedoraproject.org> - 2.20.0-1
- Update to 2.20.0
- patch from https://github.com/llaville/php-compat-info/pull/98

* Fri Jul 12 2013 Remi Collet <remi@fedoraproject.org> - 2.19.0-1
- Update to 2.19.0
- add module and install to fileExtensions in default configuration
  for drupal packages, #979830
- patch from https://github.com/llaville/php-compat-info/pull/95

* Wed Jun 26 2013 Remi Collet <remi@fedoraproject.org> - 2.18.0-1
- Update to 2.18.0
- raise dependencies, PHP_Reflect 1.7.0
- drop PHP 5.5 patches, applied upstream
- add patch for windows only constants

* Fri Jun 07 2013 Remi Collet <remi@fedoraproject.org> - 2.17.0-2
- keep phpci command for now

* Fri Jun 07 2013 Remi Collet <remi@fedoraproject.org> - 2.17.0-1
- Update to 2.17.0
- phpci command renamed to phpcompatinfo

* Fri May 10 2013 Remi Collet <remi@fedoraproject.org> - 2.16.0-1
- Update to 2.16.0

* Fri Apr 12 2013 Remi Collet <remi@fedoraproject.org> - 2.15.0-2
- add upstream man page (from github)
- Update to 2.15.0
- raise dependencies, PHP_Reflect 1.6.2
- add more patches for PHP 5.5 reference

* Tue Apr 02 2013 Remi Collet <remi@fedoraproject.org> - 2.14.1-1
- Update to 2.14.1
- make cache path user dependent

* Mon Mar 18 2013 Remi Collet <remi@fedoraproject.org> - 2.14.0-2
- update References for PHP 5.5 from
  https://github.com/llaville/php-compat-info/commits/php-5.5

* Mon Mar 18 2013 Remi Collet <remi@fedoraproject.org> - 2.14.0-1
- Update to 2.14.0

* Tue Feb 26 2013 Remi Collet <remi@fedoraproject.org> - 2.13.2-1
- Update to 2.13.2
- raise dependencies, PHP_Reflect 1.6.1
- provides phpci
- patch for https://github.com/llaville/php-compat-info/issues/69

* Fri Feb 22 2013 Remi Collet <remi@fedoraproject.org> - 2.13.0-1
- Update to 2.13.0
- raise dependencies, PHP_Reflect 1.6.0

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.12.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jan 18 2013 Remi Collet <remi@fedoraproject.org> - 2.12.1-1
- update to Version 2.12.1
- fix path to documentation in description
- drop dependency on eZ components
- raise PHPUnit dependency to 3.6.0
- skip HashTest (mhash not available) on EL-6

* Fri Dec 21 2012 Remi Collet <remi@fedoraproject.org> - 2.11.0-1
- update to Version 2.11.0
- html documentation is now provided by upstream
- raise dependencies, PHP_Reflect 1.5.0, Console_CommandLine 1.2.0

* Sat Sep 29 2012 Remi Collet <remi@fedoraproject.org> - 2.8.1-1
- Version 2.8.1 (stable) - API 2.8.0 (stable)

* Mon Sep 17 2012 Remi Collet <remi@fedoraproject.org> - 2.8.0-1
- Version 2.8.0 (stable) - API 2.8.0 (stable)
- new extensions : amqp, geoip, inclued, xcache

* Mon Sep  3 2012 Remi Collet <remi@fedoraproject.org> - 2.7.0-1
- Version 2.7.0 (stable) - API 2.7.0 (stable)

* Sun Aug 19 2012 Remi Collet <remi@fedoraproject.org> - 2.6.0-3
- rebuilt for new pear_datadir

* Tue Aug 14 2012 Remi Collet <remi@fedoraproject.org> - 2.6.0-2
- rebuildt for new pear_testdir

* Wed Aug 01 2012 Remi Collet <remi@fedoraproject.org> - 2.6.0-1
- Version 2.6.0 (stable) - API 2.6.0 (stable)
- raise dependencies: PHPUnit 3.6.0, PHP_Reflect 1.4.2

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.5.0-2.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sun Jul  8 2012 Remi Collet <remi@fedoraproject.org> - 2.5.0-1.1
- drop XslTest in EL-6

* Fri Jun 22 2012 Remi Collet <remi@fedoraproject.org> - 2.5.0-1
- Version 2.5.0 (stable) - API 2.5.0 (stable)
- use reference="ALL" in provided config

* Fri May 11 2012 Remi Collet <remi@fedoraproject.org> - 2.4.0-1.1
- add patch for old libxml

* Fri May 11 2012 Remi Collet <remi@fedoraproject.org> - 2.4.0-1
- Version 2.4.0 (stable) - API 2.3.0 (stable)

* Mon Mar 05 2012 Remi Collet <remi@fedoraproject.org> - 2.3.0-1
- Version 2.3.0 (stable) - API 2.3.0 (stable)

* Sat Feb 25 2012 Remi Collet <remi@fedoraproject.org> - 2.2.5-1
- Version 2.2.5 (stable) - API 2.2.0 (stable)

* Fri Feb 17 2012 Remi Collet <remi@fedoraproject.org> - 2.2.4-1
- Version 2.2.4 (stable) - API 2.2.0 (stable)

* Tue Feb 14 2012 Remi Collet <remi@fedoraproject.org> - 2.2.3-1
- Version 2.2.3 (stable) - API 2.2.0 (stable)

* Thu Feb 09 2012 Remi Collet <remi@fedoraproject.org> - 2.2.2-1
- Version 2.2.2 (stable) - API 2.2.0 (stable)

* Sun Feb 05 2012 Remi Collet <remi@fedoraproject.org> - 2.2.1-1
- Version 2.2.1 (stable) - API 2.2.0 (stable)

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sat Sep 24 2011 Remi Collet <remi@fedoraproject.org> - 2.1.0-3.1
- no html doc on EL6

* Wed Sep 21 2011 Remi Collet <remi@fedoraproject.org> - 2.1.0-3
- remove all files with licensing issue
  don't use it during test, don't install it
  can keep it in sources are this files are still under free license

* Tue Sep 20 2011 Remi Collet <remi@fedoraproject.org> - 2.1.0-2
- comments from review #693204
- remove ascii*js (not used)
- add MIT to license for bundled jquery

* Thu Aug 25 2011 Remi Collet <Fedora@FamilleCollet.com> - 2.1.0-1
- Version 2.1.0 (stable) - API 2.1.0 (stable)
- fix documentation for asciidoc 8.4

* Thu Jun 02 2011 Remi Collet <Fedora@FamilleCollet.com> - 2.0.0-1
- Version 2.0.0 (stable) - API 2.0.0 (stable)
- add HTML documentation

* Tue Apr 26 2011 Remi Collet <Fedora@FamilleCollet.com> - 2.0.0-0.3.RC4
- Version 2.0.0RC4 (beta) - API 2.0.0 (beta)

* Fri Mar 25 2011 Remi Collet <Fedora@FamilleCollet.com> - 2.0.0-0.2.RC3
- Version 2.0.0RC3

* Fri Feb 25 2011 Remi Collet <Fedora@FamilleCollet.com> - 2.0.0-0.1.RC2
- Version 2.0.0RC2
- Initial Release

