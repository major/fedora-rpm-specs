# remirepo/fedora spec file for php-cs-fixer
#
# Copyright (c) 2016-2024 Remi Collet
# License: CC-BY-SA-4.0
# http://creativecommons.org/licenses/by-sa/4.0/
#
# Please, preserve the changelog entries
#

%bcond_with          generators

%global gh_commit    73f78d8b2b34a0dd65fedb434a602ee4c2c8ad4c
%global gh_short     %(c=%{gh_commit}; echo ${c:0:7})
%global gh_date      2025-01-13
%global gh_owner     FriendsOfPHP
%global gh_project   PHP-CS-Fixer

Name:           php-cs-fixer
Version:        3.68.0
Release:        1%{?dist}
Summary:        PHP Coding Standards Fixer

# see bundled list below, SPDX
License:        MIT AND BSD-3-Clause
URL:            https://github.com/%{gh_owner}/%{gh_project}
# git snapshot to get upstream test suite
Source0:        %{name}-%{version}-%{gh_short}.tgz
Source2:        makesrc.sh

# Use our autoloader
Patch0:         %{name}-autoload.patch

BuildArch:      noarch
BuildRequires:  php(language) >= 8.1
BuildRequires:  php-cli
BuildRequires:  php-json
%if %{with generators}
BuildRequires:  composer-generators >= 0.1.1
%endif

# see composer.json and makesrc.sh
Requires:       php(language) >= 8.1
Requires:       php-json
Requires:       php-tokenizer
# From phpcompatinfo report for version 3.5.0
Requires:       php-dom
Requires:       php-intl
Requires:       php-mbstring

# Package was renamed
Obsoletes:      php-cs-fixer3 < 3.5
Provides:       php-cs-fixer3 = %{version}

%if %{without generators}
# Bundled PHP libraries
# License BSD-3-Clause
Provides:       bundled(php-composer(sebastian/diff)) = 5.1.1
# License MIT
Provides:       bundled(php-composer(clue/ndjson-react)) = 1.3.0
Provides:       bundled(php-composer(composer/pcre)) = 3.3.2
Provides:       bundled(php-composer(composer/semver)) = 3.4.3
Provides:       bundled(php-composer(composer/xdebug-handler)) = 3.0.5
Provides:       bundled(php-composer(evenement/evenement)) = 3.0.2
Provides:       bundled(php-composer(fidry/cpu-core-counter)) = 1.2.0
Provides:       bundled(php-composer(psr/container)) = 2.0.2
Provides:       bundled(php-composer(psr/event-dispatcher)) = 1.0.0
Provides:       bundled(php-composer(psr/log)) = 2.0.0
Provides:       bundled(php-composer(react/cache)) = 1.2.0
Provides:       bundled(php-composer(react/child-process)) = 0.6.6
Provides:       bundled(php-composer(react/dns)) = 1.13.0
Provides:       bundled(php-composer(react/event-loop)) = 1.5.0
Provides:       bundled(php-composer(react/promise)) = 3.2.0
Provides:       bundled(php-composer(react/socket)) = 1.16.0
Provides:       bundled(php-composer(react/stream)) = 1.4.0
Provides:       bundled(php-composer(symfony/console)) = 6.4.17
Provides:       bundled(php-composer(symfony/deprecation-contracts)) = 3.5.1
Provides:       bundled(php-composer(symfony/event-dispatcher)) = 6.4.13
Provides:       bundled(php-composer(symfony/event-dispatcher-contracts)) = 3.5.1
Provides:       bundled(php-composer(symfony/filesystem)) = 6.4.13
Provides:       bundled(php-composer(symfony/finder)) = 6.4.17
Provides:       bundled(php-composer(symfony/options-resolver)) = 6.4.16
Provides:       bundled(php-composer(symfony/polyfill-ctype)) = 1.31.0
Provides:       bundled(php-composer(symfony/polyfill-intl-grapheme)) = 1.31.0
Provides:       bundled(php-composer(symfony/polyfill-intl-normalizer)) = 1.31.0
Provides:       bundled(php-composer(symfony/polyfill-mbstring)) = 1.31.0
Provides:       bundled(php-composer(symfony/polyfill-php80)) = 1.31.0
Provides:       bundled(php-composer(symfony/polyfill-php81)) = 1.31.0
Provides:       bundled(php-composer(symfony/process)) = 6.4.15
Provides:       bundled(php-composer(symfony/service-contracts)) = 3.5.1
Provides:       bundled(php-composer(symfony/stopwatch)) = 6.4.13
Provides:       bundled(php-composer(symfony/string)) = 6.4.15

Provides:       php-composer(friendsofphp/php-cs-fixer) = %{version}
%endif


%description
The PHP Coding Standards Fixer (PHP CS Fixer) tool fixes your code to follow
standards; whether you want to follow PHP coding standards as defined in the
PSR-1, PSR-2, etc., or other community driven ones like the Symfony one. You
can also define your (team's) style through configuration.

It can modernize your code (like converting the pow function to the ** operator
on PHP 5.6) and (micro) optimize it.

If you are already using a linter to identify coding standards problems in your
code, you know that fixing them by hand is tedious, especially on large
projects. This tool does not only detect them, but also fixes them for you.


%prep
%setup -q -n %{gh_project}-%{gh_commit}
%patch -P0 -p1 -b .rpm

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
        $res[$lic][] = sprintf("Provides:       bundled(php-composer(%s)) = %s", $pkg["name"], ltrim($pkg["version"], "v"));
    }
    ksort($res);
    foreach($res as $lic => $lib) {
        sort($lib);
        printf("# License %s\n%s\n", $lic, implode("\n", $lib));
    }
'
%endif

%build
# Empty build section, most likely nothing required.


%install
: Library
mkdir -p      %{buildroot}%{_datadir}/%{name}
cp -pr src    %{buildroot}%{_datadir}/%{name}/src
cp -pr vendor %{buildroot}%{_datadir}/%{name}/vendor

: Command
install -Dpm755 %{name} %{buildroot}%{_bindir}/%{name}


%check
sed -e 's:%{_datadir}:%{buildroot}%{_datadir}:' -i %{name}
PHP_CS_FIXER_IGNORE_ENV=1 ./%{name} --version | grep %{version}


%files
%license LICENSE
%doc composer.json
%doc vendor/composer/installed.json
%doc *.md
%{_datadir}/%{name}
%{_bindir}/%{name}


%changelog
* Tue Jan 14 2025 Remi Collet <remi@remirepo.net> - 3.68.0-1
- update to 3.68.0

* Tue Jan  7 2025 Remi Collet <remi@remirepo.net> - 3.66.2-1
- update to 3.66.2

* Mon Jan  6 2025 Remi Collet <remi@remirepo.net> - 3.66.1-1
- update to 3.66.1

* Mon Dec 30 2024 Remi Collet <remi@remirepo.net> - 3.66.0-1
- update to 3.66.0
- add option to use composer-generators

* Mon Nov 25 2024 Remi Collet <remi@remirepo.net> - 3.65.0-1
- update to 3.65.0

* Sat Aug 31 2024 Remi Collet <remi@remirepo.net> - 3.64.0-1
- update to 3.64.0

* Tue Aug 27 2024 Remi Collet <remi@remirepo.net> - 3.63.1-1
- update to 3.63.1

* Thu Aug  8 2024 Remi Collet <remi@remirepo.net> - 3.62.0-1
- update to 3.62.0

* Thu Aug  1 2024 Remi Collet <remi@remirepo.net> - 3.61.1-1
- update to 3.61.1

* Thu Jul 25 2024 Remi Collet <remi@remirepo.net> - 3.60.0-1
- update to 3.60.0

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.59.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Tue Jul  2 2024 Remi Collet <remi@remirepo.net> - 3.59.3-1
- update to 3.59.3

* Thu May 30 2024 Remi Collet <remi@remirepo.net> - 3.58.1-1
- update to 3.58.1

* Wed May 29 2024 Remi Collet <remi@remirepo.net> - 3.58.0-1
- update to 3.58.0

* Wed May 22 2024 Remi Collet <remi@remirepo.net> - 3.57.2-1
- update to 3.57.2

* Mon May 13 2024 Remi Collet <remi@remirepo.net> - 3.56.1-1
- update to 3.56.1

* Wed Apr 17 2024 Remi Collet <remi@remirepo.net> - 3.54.0-1
- update to 3.54.0

* Tue Apr  9 2024 Remi Collet <remi@remirepo.net> - 3.53.0-1
- update to 3.53.0
- bump dependency on PHP 8.1

* Wed Mar 20 2024 Remi Collet <remi@remirepo.net> - 3.52.1-1
- update to 3.52.1

* Tue Mar 19 2024 Remi Collet <remi@remirepo.net> - 3.52.0-1
- update to 3.52.0

* Thu Feb 29 2024 Remi Collet <remi@remirepo.net> - 3.51.0-1
- update to 3.51.0

* Mon Feb 26 2024 Remi Collet <remi@remirepo.net> - 3.50.0-1
- update to 3.50.0

* Mon Feb  5 2024 Remi Collet <remi@remirepo.net> - 3.49.0-1
- update to 3.49.0

* Mon Jan 22 2024 Remi Collet <remi@remirepo.net> - 3.48.0-1
- update to 3.48.0

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.47.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jan 17 2024 Remi Collet <remi@remirepo.net> - 3.47.1-1
- update to 3.47.1

* Thu Jan  4 2024 Remi Collet <remi@remirepo.net> - 3.46.0-1
- update to 3.46.0

* Sat Dec 30 2023 Remi Collet <remi@remirepo.net> - 3.45.0-1
- update to 3.45.0

* Mon Dec 11 2023 Remi Collet <remi@remirepo.net> - 3.41.1-1
- update to 3.41.1

* Mon Dec  4 2023 Remi Collet <remi@remirepo.net> - 3.40.2-1
- update to 3.40.2

* Mon Nov 27 2023 Remi Collet <remi@remirepo.net> - 3.40.0-1
- update to 3.40.0

* Wed Nov 22 2023 Remi Collet <remi@remirepo.net> - 3.39.0-1
- update to 3.39.0

* Tue Nov 14 2023 Remi Collet <remi@remirepo.net> - 3.38.2-1
- update to 3.38.2

* Mon Oct 30 2023 Remi Collet <remi@remirepo.net> - 3.37.1-1
- update to 3.37.1

* Fri Oct 27 2023 Remi Collet <remi@remirepo.net> - 3.36.0-1
- update to 3.36.0

* Fri Oct 13 2023 Remi Collet <remi@remirepo.net> - 3.35.1-1
- update to 3.35.1

* Wed Oct  4 2023 Remi Collet <remi@remirepo.net> - 3.34.1-1
- update to 3.34.1

* Fri Sep 29 2023 Remi Collet <remi@remirepo.net> - 3.31.0-1
- update to 3.31.0

* Wed Sep 27 2023 Remi Collet <remi@remirepo.net> - 3.30.0-1
- update to 3.30.0

* Mon Sep 25 2023 Remi Collet <remi@remirepo.net> - 3.28.0-1
- update to 3.28.0

* Mon Sep 18 2023 Remi Collet <remi@remirepo.net> - 3.27.0-1
- update to 3.27.0

* Mon Sep 11 2023 Remi Collet <remi@remirepo.net> - 3.26.1-1
- update to 3.26.1

* Fri Sep  8 2023 Remi Collet <remi@remirepo.net> - 3.26.0-1
- update to 3.26.0

* Mon Sep  4 2023 Remi Collet <remi@remirepo.net> - 3.25.1-1
- update to 3.25.1

* Fri Sep  1 2023 Remi Collet <remi@remirepo.net> - 3.25.0-1
- update to 3.25.0

* Thu Aug 31 2023 Remi Collet <remi@remirepo.net> - 3.24.0-1
- update to 3.24.0

* Fri Aug 18 2023 Remi Collet <remi@remirepo.net> - 3.23.0-1
- update to 3.23.0

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.22.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Mon Jul 17 2023 Remi Collet <remi@remirepo.net> - 3.22.0-1
- update to 3.22.0

* Thu Jul  6 2023 Remi Collet <remi@remirepo.net> - 3.21.1-1
- update to 3.21.1
- bump dependency on PHP 8.0

* Wed Jun 28 2023 Remi Collet <remi@remirepo.net> - 3.20.0-1
- update to 3.20.0

* Mon Jun 26 2023 Remi Collet <remi@remirepo.net> - 3.19.2-1
- update to 3.19.2

* Tue Jun 20 2023 Remi Collet <remi@remirepo.net> - 3.18.0-1
- update to 3.18.0

* Wed May 24 2023 Remi Collet <remi@remirepo.net> - 3.17.0-1
- update to 3.17.0

* Mon Apr  3 2023 Remi Collet <remi@remirepo.net> - 3.16.0-1
- update to 3.16.0

* Tue Mar 14 2023 Remi Collet <remi@remirepo.net> - 3.15.1-1
- update to 3.15.1

* Mon Mar 13 2023 Remi Collet <remi@remirepo.net> - 3.15.0-1
- update to 3.15.0

* Fri Feb 10 2023 Remi Collet <remi@remirepo.net> - 3.14.4-1
- update to 3.14.4

* Tue Jan 31 2023 Remi Collet <remi@remirepo.net> - 3.14.3-1
- update to 3.14.3

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.13.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Tue Jan  3 2023 Remi Collet <remi@remirepo.net> - 3.13.2-1
- update to 3.13.2

* Mon Dec 19 2022 Remi Collet <remi@remirepo.net> - 3.13.1-1
- update to 3.13.1

* Wed Nov  2 2022 Remi Collet <remi@remirepo.net> - 3.13.0-1
- update to 3.13.0

* Wed Oct 12 2022 Remi Collet <remi@remirepo.net> - 3.12.0-1
- update to 3.12.0

* Thu Sep  8 2022 Remi Collet <remi@remirepo.net> - 3.11.0-1
- update to 3.11.0

* Thu Aug 18 2022 Remi Collet <remi@remirepo.net> - 3.10.0-1
- update to 3.10.0

* Fri Jul 22 2022 Remi Collet <remi@remirepo.net> - 3.9.5-1
- update to 3.9.5

* Mon Jul 18 2022 Remi Collet <remi@remirepo.net> - 3.9.4-1
- update to 3.9.4

* Wed Jul 13 2022 Remi Collet <remi@remirepo.net> - 3.9.3-1
- update to 3.9.3

* Tue Jul 12 2022 Remi Collet <remi@remirepo.net> - 3.9.2-1
- update to 3.9.2

* Mon Jul 11 2022 Remi Collet <remi@remirepo.net> - 3.9.1-1
- update to 3.9.1

* Mon Mar 21 2022 Remi Collet <remi@remirepo.net> - 3.8.0-1
- update to 3.8.0

* Tue Mar  8 2022 Remi Collet <remi@remirepo.net> - 3.7.0-1
- update to 3.7.0 #StandWithUkraine️

* Tue Feb  8 2022 Remi Collet <remi@remirepo.net> - 3.6.0-1
- update to 3.6.0

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jan 14 2022 Remi Collet <remi@remirepo.net> - 3.5.0-1
- update to 3.5.0
- install in /usr/share/php-cs-fixer with all bundled libraries

* Tue Nov 16 2021 Remi Collet <remi@remirepo.net> - 2.19.3-1
- update to 2.19.3

* Thu Sep  2 2021 Remi Collet <remi@remirepo.net> - 2.19.2-1
- update to 2.19.2

* Tue Aug  3 2021 Remi Collet <remi@remirepo.net> - 2.19.1-1
- update to 2.19.1

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.19.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue May  4 2021 Remi Collet <remi@remirepo.net> - 2.19.0-1
- update to 2.19.0

* Tue Apr 20 2021 Remi Collet <remi@remirepo.net> - 2.18.6-1
- update to 2.18.6
- switch to composer/xdebug-handler version 2

* Wed Apr  7 2021 Remi Collet <remi@remirepo.net> - 2.18.5-1
- update to 2.18.5

* Mon Mar 22 2021 Remi Collet <remi@remirepo.net> - 2.18.4-1
- update to 2.18.4

* Thu Mar 11 2021 Remi Collet <remi@remirepo.net> - 2.18.3-1
- update to 2.18.3

* Tue Mar  2 2021 Remi Collet <remi@remirepo.net> - 2.18.2-1
- update to 2.18.2
- switch to phpunit9
  with phpspec/prophecy-phpunit and sanmai/phpunit-legacy-adapter

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.17.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Dec  9 2020 Remi Collet <remi@remirepo.net> - 2.17.1-1
- update to 2.17.1

* Tue Dec  8 2020 Remi Collet <remi@remirepo.net> - 2.17.0-1
- update to 2.17.0

* Wed Oct 28 2020 Remi Collet <remi@remirepo.net> - 2.16.7-1
- update to 2.16.7
- raise dependency on composer/semver v3

* Mon Oct 26 2020 Remi Collet <remi@remirepo.net> - 2.16.4-3
- raise dependency on PHP 7.2
- drop dependency on symfony-polyfill

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.16.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jun 29 2020 Remi Collet <remi@remirepo.net> - 2.16.4-1
- update to 2.16.4

* Thu Apr 16 2020 Remi Collet <remi@remirepo.net> - 2.16.3-1
- update to 2.16.3

* Mon Apr 13 2020 Remi Collet <remi@remirepo.net> - 2.16.2-1
- update to 2.16.2

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.16.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Nov 26 2019 Remi Collet <remi@remirepo.net> - 2.16.1-1
- update to 2.16.1

* Mon Nov  4 2019 Remi Collet <remi@remirepo.net> - 2.16.0-1
- update to 2.16.0

* Sun Sep  1 2019 Remi Collet <remi@remirepo.net> - 2.15.3-1
- update to 2.15.3

* Thu Aug 29 2019 Remi Collet <remi@remirepo.net> - 2.15.2-1
- update to 2.15.2

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.15.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Jun  4 2019 Remi Collet <remi@remirepo.net> - 2.15.1-1
- update to 2.15.1

* Mon May  6 2019 Remi Collet <remi@remirepo.net> - 2.15.0-1
- update to 2.15.0
- add patch for libpcre2 10.33 from
  https://github.com/FriendsOfPHP/PHP-CS-Fixer/pull/4406

* Mon Feb 18 2019 Remi Collet <remi@remirepo.net> - 2.14.2-1
- update to 2.14.2 (no change)

* Mon Feb 11 2019 Remi Collet <remi@remirepo.net> - 2.14.1-1
- update to 2.14.1

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.14.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jan  5 2019 Remi Collet <remi@remirepo.net> - 2.14.0-1
- update to 2.14.0

* Wed Jan  2 2019 Remi Collet <remi@remirepo.net> - 2.13.2-1
- update to 2.13.2

* Tue Dec 11 2018 Remi Collet <remi@remirepo.net> - 2.13.1-2
- skip 1 test failing with PHPUnit 7.5

* Sun Oct 21 2018 Remi Collet <remi@remirepo.net> - 2.13.1-1
- update to 2.13.1

* Fri Aug 24 2018 Remi Collet <remi@remirepo.net> - 2.13.0-1
- update to 2.13.0

* Mon Aug 20 2018 Remi Collet <remi@remirepo.net> - 2.12.3-1
- update to 2.12.3
- raise dependency on composer/xdebug-handler 1.2

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.12.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Jul  6 2018 Remi Collet <remi@remirepo.net> - 2.12.2-1
- update to 2.12.2

* Mon Jun 11 2018 Remi Collet <remi@remirepo.net> - 2.12.1-1
- update to 2.12.1

* Mon Jun  4 2018 Remi Collet <remi@remirepo.net> - 2.12.0-1
- update to 2.12.0
- add dependency on composer/xdebug-handler
- add dependency on php-cs-fixer/phpunit-constraint-isidenticalstring
- add dependency on php-cs-fixer/phpunit-constraint-xmlmatchesxsd

* Thu Mar 22 2018 Remi Collet <remi@remirepo.net> - 2.11.1-1
- update to 2.11.1

* Wed Mar 21 2018 Remi Collet <remi@remirepo.net> - 2.11.0-1
- update to 2.11.0
- use phpunit7 on F28+

* Thu Mar  8 2018 Remi Collet <remi@remirepo.net> - 2.10.4-1
- update to 2.10.4

* Fri Feb 23 2018 Remi Collet <remi@remirepo.net> - 2.10.3-1
- Update to 2.10.3
- drop dependency on gecko-packages/gecko-php-unit
- update bundled php-cs-fixer/diff to 1.3.0

* Tue Feb  6 2018 Remi Collet <remi@remirepo.net> - 2.10.2-1
- Update to 2.10.2
- use range dependencies

* Thu Jan 11 2018 Remi Collet <remi@remirepo.net> - 2.10.0-1
- Update to 2.10.0

* Thu Dec 28 2017 Remi Collet <remi@remirepo.net> - 2.9.0-2
- mikey179/vfsStream only required at builtime

* Sat Dec  9 2017 Remi Collet <remi@remirepo.net> - 2.9.0-1
- Update to 2.9.0

* Mon Nov 27 2017 Remi Collet <remi@remirepo.net> - 2.8.3-1
- Update to 2.8.3
- open https://github.com/FriendsOfPHP/PHP-CS-Fixer/issues/3279
  bad tag for 2.8.3

* Mon Nov 20 2017 Remi Collet <remi@remirepo.net> - 2.8.2-1
- Update to 2.8.2

* Fri Nov 10 2017 Remi Collet <remi@remirepo.net> - 2.8.1-1
- Update to 2.8.1

* Tue Nov  7 2017 Remi Collet <remi@remirepo.net> - 2.8.0-2
- fix FTBFS from Koschei using symfony package names

* Fri Nov  3 2017 Remi Collet <remi@remirepo.net> - 2.8.0-1
- Update to 2.8.0

* Mon Oct  2 2017 Remi Collet <remi@remirepo.net> - 2.7.1-1
- Update to 2.7.1
- drop dependency on sebastian/diff, bundle fork instead

* Tue Sep 12 2017 Remi Collet <remi@remirepo.net> - 2.6.0-1
- Update to 2.6.0
- add dependency on composer/semver

* Wed Aug 23 2017 Remi Collet <remi@remirepo.net> - 2.5.0-1
- Update to 2.5.0
- add dependency on php-cs-fixer/accessible-object
- raise dependency on symfony 3.2

* Thu Aug  3 2017 Remi Collet <remi@remirepo.net> - 2.4.0-1
- Update to 2.4.0
- add dependency on symfony/polyfill-php72

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Thu May 25 2017 Remi Collet <remi@remirepo.net> - 2.3.2-1
- Update to 2.3.2
- add dependency on gecko-packages/gecko-php-unit

* Tue May  9 2017 Remi Collet <remi@remirepo.net> - 2.3.1-1
- Update to 2.3.1
- raise dependency on PHP 5.6
- raise dependency on Symfony 3

* Wed Apr 26 2017 Remi Collet <remi@remirepo.net> - 2.2.3-1
- Update to 2.2.3

* Mon Apr 24 2017 Remi Collet <remi@remirepo.net> - 2.2.2-1
- Update to 2.2.2
- raise dependency on sebastian/diff >= 1.4

* Mon Apr 10 2017 Remi Collet <remi@remirepo.net> - 2.2.1-1
- Update to 2.2.1

* Sat Apr  1 2017 Remi Collet <remi@remirepo.net> - 2.2.0-1
- Update to 2.2.0
- add dependency on doctrine/annotations
- add dependency on symfony/options-resolver
- raise dependency on symfony 2.6
- fix autoloader to allow Symfony 3

* Fri Mar 31 2017 Remi Collet <remi@remirepo.net> - 2.1.3-1
- Update to 2.1.3
- add dependency on php-mbstring

* Wed Mar 15 2017 Remi Collet <remi@remirepo.net> - 2.1.2-1
- Update to 2.1.2

* Sat Feb 11 2017 Remi Collet <remi@fedoraproject.org> - 2.1.0-1
- update to 2.1.0
- add dependency on symfony/polyfill-php55 (for EPEL-7)

* Thu Feb  9 2017 Remi Collet <remi@fedoraproject.org> - 2.0.1-1
- update to 2.0.1

* Thu Dec  1 2016 Remi Collet <remi@fedoraproject.org> - 2.0.0-1
- update to 2.0.0

* Tue Nov 29 2016 Remi Collet <remi@fedoraproject.org> - 1.13.0-1
- update to 1.13.0

* Tue Nov 15 2016 Remi Collet <remi@fedoraproject.org> - 1.12.4-1
- update to 1.12.4

* Sun Oct 30 2016 Remi Collet <remi@fedoraproject.org> - 1.12.3-1
- update to 1.12.3
- switch from symfony/class-loader to fedora/autoloader

* Tue Sep 27 2016 Remi Collet <remi@fedoraproject.org> - 1.12.2-1
- update to 1.12.2

* Fri Sep  9 2016 Remi Collet <remi@fedoraproject.org> - 1.12.1-1
- initial package, version 1.12.1

