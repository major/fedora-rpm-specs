# remirepo/fedora spec file for php-nikic-php-parser4
#
# Copyright (c) 2016-2024 Remi Collet
# License: CC-BY-SA-4.0
# http://creativecommons.org/licenses/by-sa/4.0/
#
# Please, preserve the changelog entries
#


%if 0%{?fedora}
%bcond_without tests
%else
# disabled as phpunit not availble
%bcond_with    tests
%endif

%global gh_commit    715f4d25e225bc47b293a8b997fe6ce99bf987d2
%global gh_short     %(c=%{gh_commit}; echo ${c:0:7})
%global gh_owner     nikic
%global gh_project   PHP-Parser
%global pk_project   php-parser
%global php_home     %{_datadir}/php
%global ns_project   PhpParser
%global major        4

Name:           php-%{gh_owner}-%{pk_project}%{major}
Version:        4.19.4
Release:        2%{?dist}
Summary:        A PHP parser written in PHP - version %{major}

License:        BSD-3-Clause
URL:            https://github.com/%{gh_owner}/%{gh_project}
Source0:        %{name}-%{version}-%{gh_short}.tgz
Source1:        makesrc.sh

# Autoloader
Patch0:         %{name}-rpm.patch

BuildArch:      noarch
%if %{with tests}
# For tests
# as we use phpunit9
BuildRequires:  php(language) >= 7.3
BuildRequires:  php-tokenizer
BuildRequires:  php-reflection
BuildRequires:  php-ctype
BuildRequires:  php-json
BuildRequires:  php-pcre
BuildRequires:  php-spl
# From composer.json, "require-dev": {
#        "phpunit/phpunit": "^7.0 || ^8.0 || ^9.0",
#        "ircmaxell/php-yacc": "0.0.7"
%global phpunit %{_bindir}/phpunit9
BuildRequires:  phpunit9
# Autoloader
%endif
BuildRequires:  php-fedora-autoloader-devel

# From composer.json, "require": {
#        "php": ">=7.1",
#        "ext-tokenizer": "*"
Requires:       php(language) >= 7.1
Requires:       php-tokenizer
# From phpcompatinfo report for version 4.0.0
Requires:       php-reflection
Requires:       php-ctype
Requires:       php-json
Requires:       php-pcre
Requires:       php-spl
Requires:       php-cli
# Autoloader
Requires:       php-composer(fedora/autoloader)

Provides:       php-composer(%{gh_owner}/%{pk_project}) = %{version}


%description
This is a PHP parser written in PHP.
Its purpose is to simplify static code analysis and manipulation.

This package provides the library version %{major} and the php-parse%{major} command.

Documentation: https://github.com/nikic/PHP-Parser/tree/master/doc

Autoloader: %{php_home}/%{ns_project}%{major}/autoload.php


%prep
%setup -q -n %{gh_project}-%{gh_commit}

%patch -P0 -p1 -b .rpm


%build
: Generate an simple classmap autoloader
phpab --template fedora \
      --output lib/%{ns_project}/autoload.php \
      lib/%{ns_project}


%install
: Library
mkdir -p                 %{buildroot}%{php_home}
cp -pr lib/%{ns_project} %{buildroot}%{php_home}/%{ns_project}%{major}

: Command
install -Dpm 0755 bin/php-parse %{buildroot}%{_bindir}/php-parse%{major}


%check
%if %{with tests}
: Test the command
sed -e 's:%{php_home}:%{buildroot}%{php_home}:' \
    bin/php-parse > bin/php-parse-test
php bin/php-parse-test --help

: Test suite autoloader
mkdir vendor
cat << 'AUTOLOAD' | tee vendor/autoload.php
<?php
\Fedora\Autoloader\Autoload::addPsr4('%{ns_project}\\', dirname(__DIR__).'/test/PhpParser/');
AUTOLOAD

: Upstream test suite
FILTER="--filter '^((?!(testLexNewFeatures)).)*$'"

ret=0
for cmdarg in "php %{phpunit}" php81 php82 php83 php84; do
  if which $cmdarg; then
    set $cmdarg
    $1 -d include_path=%{php_home} \
       -d auto_prepend_file=%{buildroot}/%{php_home}/%{ns_project}%{major}/autoload.php \
      ${2:-%{_bindir}/phpunit9} $FILTER --verbose || ret=1
  fi
done
exit $ret
%else
: Test suite disabled
%endif


%files
%license LICENSE
%doc composer.json
%doc *.md
%{_bindir}/php-parse%{major}
%{php_home}/%{ns_project}%{major}


%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 4.19.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Sep 30 2024 Remi Collet <remi@remirepo.net> - 4.19.4-1
- update to 4.19.4

* Wed Sep 18 2024 Remi Collet <remi@remirepo.net> - 4.19.2-1
- update to 4.19.2

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.19.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Tue Mar 19 2024 Remi Collet <remi@remirepo.net> - 4.19.1-1
- update to 4.19.1
- raise dependency on PHP 7.1

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.18.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.18.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Dec 11 2023 Remi Collet <remi@remirepo.net> - 4.18.0-1
- update to 4.18.0

* Fri Aug 18 2023 Remi Collet <remi@remirepo.net> - 4.17.1-1
- update to 4.17.1

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 4.16.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Mon Jun 26 2023 Remi Collet <remi@remirepo.net> - 4.16.0-1
- update to 4.16.0

* Wed May 24 2023 Remi Collet <remi@remirepo.net> - 4.15.5-1
- update to 4.15.5

* Mon Mar  6 2023 Remi Collet <remi@remirepo.net> - 4.15.4-1
- update to 4.15.4

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 4.15.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Tue Jan 17 2023 Remi Collet <remi@remirepo.net> - 4.15.3-1
- update to 4.15.3

* Mon Nov 14 2022 Remi Collet <remi@remirepo.net> - 4.15.2-1
- update to 4.15.2

* Thu Sep  8 2022 Remi Collet <remi@remirepo.net> - 4.15.1-1
- update to 4.15.1

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.14.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Remi Collet <remi@remirepo.net> - 4.14.0-2
- only run test suite on Fedora, not on EL

* Wed Jun  1 2022 Remi Collet <remi@remirepo.net> - 4.14.0-1
- update to 4.14.0

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.13.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Dec  1 2021 Remi Collet <remi@remirepo.net> - 4.13.2-1
- update to 4.13.2

* Thu Nov  4 2021 Remi Collet <remi@remirepo.net> - 4.13.1-1
- update to 4.13.1

* Tue Sep 21 2021 Remi Collet <remi@remirepo.net> - 4.13.0-1
- update to 4.13.0

* Wed Jul 21 2021 Remi Collet <remi@remirepo.net> - 4.12.0-1
- update to 4.12.0

* Mon Jul  5 2021 Remi Collet <remi@remirepo.net> - 4.11.0-1
- update to 4.11.0
- switch to phpunit9

* Tue May  4 2021 Remi Collet <remi@remirepo.net> - 4.10.5-1
- update to 4.10.5

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.10.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Dec 21 2020 Remi Collet <remi@remirepo.net> - 4.10.4-1
- update to 4.10.4

* Fri Dec  4 2020 Remi Collet <remi@remirepo.net> - 4.10.3-1
- update to 4.10.3

* Mon Sep 28 2020 Remi Collet <remi@remirepo.net> - 4.10.2-1
- update to 4.10.2

* Thu Sep 24 2020 Remi Collet <remi@remirepo.net> - 4.10.1-1
- update to 4.10.1

* Sun Sep 20 2020 Remi Collet <remi@remirepo.net> - 4.10.0-1
- update to 4.10.0

* Mon Aug 31 2020 Remi Collet <remi@remirepo.net> - 4.9.1-1
- update to 4.9.1

* Wed Aug 19 2020 Remi Collet <remi@remirepo.net> - 4.9.0-1
- update to 4.9.0

* Mon Aug 10 2020 Remi Collet <remi@remirepo.net> - 4.8.0-1
- update to 4.8.0

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.6.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jul  3 2020 Remi Collet <remi@remirepo.net> - 4.6.0-1
- update to 4.6.0

* Thu Jun 25 2020 Remi Collet <remi@remirepo.net> - 4.5.0-2
- switch to classmap autoloader
- add missing dependency on fedora/autoloader

* Wed Jun  3 2020 Remi Collet <remi@remirepo.net> - 4.5.0-1
- update to 4.5.0

* Mon Apr 13 2020 Remi Collet <remi@remirepo.net> - 4.4.0-1
- update to 4.4.0

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Nov 12 2019 Remi Collet <remi@remirepo.net> - 4.3.0-1
- update to 4.3.0

* Mon Oct 28 2019 Remi Collet <remi@remirepo.net> - 4.2.5-1
- update to 4.2.5
- sources from git snapshot

* Mon Sep  2 2019 Remi Collet <remi@remirepo.net> - 4.2.4-1
- update to 4.2.4

* Mon Aug 19 2019 Remi Collet <remi@remirepo.net> - 4.2.3-1
- update to 4.2.3
- use phpunit8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.2.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon May 27 2019 Remi Collet <remi@remirepo.net> - 4.2.2-1
- update to 4.2.2

* Mon Feb 18 2019 Remi Collet <remi@remirepo.net> - 4.2.1-1
- update to 4.2.1

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sun Jan 13 2019 Remi Collet <remi@remirepo.net> - 4.2.0-1
- update to 4.2.0

* Thu Dec 27 2018 Remi Collet <remi@remirepo.net> - 4.1.1-1
- update to 4.1.1

* Wed Oct 10 2018 Remi Collet <remi@remirepo.net> - 4.1.0-1
- update to 4.1.0
- https://github.com/nikic/PHP-Parser/issues/539 - PHP 7.3

* Tue Sep 18 2018 Remi Collet <remi@remirepo.net> - 4.0.4-1
- update to 4.0.4

* Mon Jul 16 2018 Remi Collet <remi@remirepo.net> - 4.0.3-1
- update to 4.0.3

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Jun  4 2018 Remi Collet <remi@remirepo.net> - 4.0.2-1
- update to 4.0.2

* Mon Mar 26 2018 Remi Collet <remi@remirepo.net> - 4.0.1-1
- update to 4.0.1

* Thu Mar 22 2018 Remi Collet <remi@remirepo.net> - 4.0.0-1
- Update to 4.0.0
- rename to php-nikic-php-parser4 and move to /usr/share/php/PhpParser4
- raise dependency on PHP 7
- use phpunit6 or phpunit7 (F28+)

* Thu Mar  1 2018 Remi Collet <remi@remirepo.net> - 3.1.5-1
- Update to 3.1.5

* Fri Jan 26 2018 Remi Collet <remi@remirepo.net> - 3.1.4-1
- Update to 3.1.4

* Wed Dec 27 2017 Remi Collet <remi@remirepo.net> - 3.1.3-1
- Update to 3.1.3

* Mon Nov  6 2017 Remi Collet <remi@remirepo.net> - 3.1.2-1
- Update to 3.1.2

* Mon Sep  4 2017 Remi Collet <remi@remirepo.net> - 3.1.1-1
- Update to 3.1.1

* Sat Aug  5 2017 Remi Collet <remi@remirepo.net> - 3.1.0-1
- Update to 3.1.0

* Thu Jun 29 2017 Remi Collet <remi@remirepo.net> - 3.0.6-1
- Update to 3.0.6

* Mon Mar  6 2017 Remi Collet <remi@remirepo.net> - 3.0.5-1
- Update to 3.0.5
- always provide the command, with version suffix

* Sat Feb 11 2017 Remi Collet <remi@fedoraproject.org> - 3.0.4-1
- update to 3.0.4

* Sat Feb  4 2017 Remi Collet <remi@fedoraproject.org> - 3.0.3-1
- update to 3.0.3

* Wed Dec 7  2016 Remi Collet <remi@fedoraproject.org> - 3.0.2-1
- new package for library version 3

