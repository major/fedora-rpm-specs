# remirepo/fedora spec file for php-phpspec
#
# Copyright (c) 2015-2022 Remi Collet
# License: CC-BY-SA
# http://creativecommons.org/licenses/by-sa/4.0/
#
# Please, preserve the changelog entries
#

# passes in local build, fails in mock
%bcond_with          tests

# For compatibility with SCL
%undefine __brp_mangle_shebangs

%global gh_commit    bbeb10f73c02bfa11d92159ad9d3e75abc3faa69
%global gh_short     %(c=%{gh_commit}; echo ${c:0:7})
%global gh_owner     phpspec
%global gh_project   phpspec
#global prever       beta3

# Only allow a single Symfony version
# to ensure components consistency
%global symfony_ns  Symfony4
%global symfony_min 4.4
%global symfony_max 5

Name:           php-phpspec
Version:        7.2.0
Release:        2%{?dist}
Summary:        Specification-oriented BDD framework for PHP

License:        MIT
URL:            https://github.com/%{gh_owner}/%{gh_project}
Source0:        %{name}-%{version}%{?prever}-%{gh_short}.tgz
Source1:        %{gh_project}-autoload.php
# get git snapshot to retrieve tests
Source2:        makesrc.sh

# Use our autoloader
Patch0:         %{gh_project}-4-rpm.patch

BuildArch:      noarch
BuildRequires:  php(language) >= 7.3
%if %{with tests}
BuildRequires: (php-composer(phpspec/prophecy)         >= 1.9   with php-composer(phpspec/prophecy)         <  2)
BuildRequires: (php-composer(phpspec/php-diff)         >= 1.0.0 with php-composer(phpspec/php-diff)         <  2)
BuildRequires: (php-composer(sebastian/exporter)       >= 3     with php-composer(sebastian/exporter)       <  5)
BuildRequires: (php-composer(doctrine/instantiator)    >= 1.0.5 with php-composer(doctrine/instantiator)    <  2)
BuildRequires:  php-symfony4-console                   >= %{symfony_min}
BuildRequires:  php-symfony4-event-dispatcher          >= %{symfony_min}
BuildRequires:  php-symfony4-finder                    >= %{symfony_min}
BuildRequires:  php-symfony4-process                   >= %{symfony_min}
BuildRequires:  php-symfony4-yaml                      >= %{symfony_min}
# From composer.json, require-dev
#        "behat/behat":           "^3.3",
#        "symfony/filesystem":    "^3.4 || ^4.0 || ^5.0 || ^6.0",
#        "phpunit/phpunit":       "^8.0 || ^9.0",
#        "vimeo/psalm": "^4.3"
BuildRequires:  php-symfony4-filesystem                >= %{symfony_min}
%global phpunit %{_bindir}/phpunit9
BuildRequires:  %{phpunit}
%endif
# Autoloader
BuildRequires:  php-composer(fedora/autoloader) >= 1

# From composer.json, require
#        "php":                      "^7.3 || 8.0.* || 8.1.*",
#        "phpspec/prophecy":         "^1.9",
#        "phpspec/php-diff":         "^1.0.0",
#        "sebastian/exporter":       "^3.0 || ^4.0",
#        "symfony/console":          "^3.4 || ^4.4 || ^5.0 || ^6.0",
#        "symfony/event-dispatcher": "^3.4 || ^4.4 || ^5.0 || ^6.0",
#        "symfony/process":          "^3.4 || ^4.4 || ^5.0 || ^6.0",
#        "symfony/finder":           "^3.4 || ^4.4 || ^5.0 || ^6.0",
#        "symfony/yaml":             "^3.4 || ^4.4 || ^5.0 || ^6.0",
#        "doctrine/instantiator":    "^1.0.5"
#        "ext-tokenizer":            "*"

Requires:       php(language) >= 7.3
Requires:      (php-composer(phpspec/prophecy)         >= 1.9   with php-composer(phpspec/prophecy)         <  2)
Requires:      (php-composer(phpspec/php-diff)         >= 1.0.0 with php-composer(phpspec/php-diff)         <  2)
Requires:      (php-composer(sebastian/exporter)       >= 3     with php-composer(sebastian/exporter)       <  5)
Requires:      (php-composer(doctrine/instantiator)    >= 1.0.5 with php-composer(doctrine/instantiator)    <  2)
Requires:       php-symfony4-console                   >= %{symfony_min}
Requires:       php-symfony4-event-dispatcher          >= %{symfony_min}
Requires:       php-symfony4-finder                    >= %{symfony_min}
Requires:       php-symfony4-process                   >= %{symfony_min}
Requires:       php-symfony4-yaml                      >= %{symfony_min}
Requires:       php-tokenizer
# Autoloader
Requires:       php-composer(fedora/autoloader) >= 1
# From phpcompatinfo report
Requires:       php-json
Requires:       php-pcntl
Requires:       php-pcre
Requires:       php-reflection
Requires:       php-spl

# Composer
Provides:       php-composer(phpspec/phpspec) = %{version}
# The application
Provides:       phpspec = %{version}


%description
phpspec is a tool which can help you write clean and working PHP code
using behaviour driven development or BDD. BDD is a technique derived
from test-first development.

BDD is a technique used at story level and spec level. phpspec is a tool
for use at the spec level or SpecBDD. The technique is to first use a tool
like phpspec to describe the behaviour of an object you are about to write.
Next you write just enough code to meet that specification and finally you
refactor this code.


%prep
%setup -q -n %{gh_project}-%{gh_commit}

%patch0 -p0 -b .rpm

sed -e 's/@SYMFONY@/%{symfony_ns}/' \
    %{SOURCE1} > src/PhpSpec/autoload.php


%build
# Nothing


%install
# No namespace, so use a package specific dir
mkdir -p           %{buildroot}%{_datadir}/php
cp -pr src/PhpSpec %{buildroot}%{_datadir}/php/PhpSpec

install -Dpm755 bin/phpspec %{buildroot}%{_bindir}/phpspec


%check
%if %{with tests}
export LANG=C.UTF-8

# Ignore this test which use bossa/phpspec2-expect
rm spec/PhpSpec/Message/CurrentExampleTrackerSpec.php
# Ignore this test which rely on composer installation
rm spec/PhpSpec/NamespaceProvider/ComposerPsrNamespaceProviderSpec.php

for cmdarg in "php %{phpunit}" php74 php80 php81; do
  if which $cmdarg; then
    set $cmdarg
    $1 -d memory_limit=1G -d include_path=.:%{buildroot}%{_datadir}/php \
      bin/phpspec \
        run --format pretty --verbose --no-ansi

    $1 ${2:-%{_bindir}/phpunit9} \
      --verbose \
      --bootstrap %{buildroot}%{_datadir}/php/PhpSpec/autoload.php
  fi
done
%endif


%files
%{!?_licensedir:%global license %%doc}
%license LICENSE
%doc README.* CHANGES.*
%doc composer.json
%{_bindir}/phpspec
%{_datadir}/php/PhpSpec


%changelog
* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 7.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Mar 14 2022 Remi Collet <remi@remirepo.net> - 7.2.0-1
- update to 7.2.0

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 7.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 7.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon Jun 21 2021 Remi Collet <remi@remirepo.net> - 7.1.0-1
- update to 7.1.0

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 7.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jan  6 2021 Remi Collet <remi@remirepo.net> - 7.0.1-1
- update to 7.0.1

* Tue Nov  3 2020 Remi Collet <remi@remirepo.net> - 7.0.0-1
- update to 7.0.0
- raise dependency on PHP 7.3
- raise dependency on Symfony 4.4

* Mon Nov  2 2020 Remi Collet <remi@remirepo.net> - 6.3.0-1
- update to 6.3.0

* Thu Oct 29 2020 Remi Collet <remi@remirepo.net> - 6.2.2-1
- update to 6.2.2
- switch to phpunit9

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 6.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul  8 2020 Remi Collet <remi@remirepo.net> - 6.2.1-1
- update to 6.2.1

* Wed Jun 17 2020 Remi Collet <remi@remirepo.net> - 6.2.0-1
- update to 6.2.0
- allow sebastian/exporter 4

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 6.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Dec 19 2019 Remi Collet <remi@remirepo.net> - 6.1.1-1
- update to 6.1.1

* Fri Nov 29 2019 Remi Collet <remi@remirepo.net> - 6.1.0-1
- update to 6.1.0
- raise dependency on phpspec/prophecy 1.9
- use phpunit7

* Wed Oct  2 2019 Remi Collet <remi@remirepo.net> - 6.0.0-1
- update to 6.0.0
- raise dependency to PHP 7.2

* Wed Oct  2 2019 Remi Collet <remi@remirepo.net> - 5.1.2-1
- update to 5.1.2

* Mon Aug 19 2019 Remi Collet <remi@remirepo.net> - 5.1.1-1
- update to 5.1.1

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 5.1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb  1 2019 Remi Collet <remi@remirepo.net> - 5.1.0-3
- use Symfony component autoloaders

* Tue Nov 20 2018 Remi Collet <remi@remirepo.net> - 5.1.0-2
- ignore failed test on 32-bit arch FTBFS #1651396
  reported as https://github.com/phpspec/phpspec/issues/1234

* Sun Nov 18 2018 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 5.1.0-2
- Use C.UTF-8 locale
  See https://fedoraproject.org/wiki/Changes/Remove_glibc-langpacks-all_from_buildroot

* Mon Oct 29 2018 Remi Collet <remi@remirepo.net> - 5.1.0-1
- update to 5.1.0

* Mon Oct  1 2018 Remi Collet <remi@remirepo.net> - 5.0.3-1
- update to 5.0.3

* Mon Sep 24 2018 Remi Collet <remi@remirepo.net> - 5.0.2-1
- update to 5.0.2

* Tue Jul 17 2018 Remi Collet <remi@remirepo.net> - 5.0.1-1
- update to 5.0.1

* Mon Jul 16 2018 Remi Collet <remi@remirepo.net> - 5.0.0-2
- missing dependency on symfony/yaml

* Mon Jul 16 2018 Remi Collet <remi@remirepo.net> - 5.0.0-1
- update to 5.0.0
- raise dependency on PHP 7.1
- switch to Symfony 4
- raise dependency on phpspec/prophecy 1.7
- undefine __brp_mangle_shebangs

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jul  3 2018 Remi Collet <remi@remirepo.net> - 4.3.1-1
- update to 4.3.1
- use range dependencies

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Dec 23 2017 Remi Collet <remi@remirepo.net> - 4.3.0-1
- Update to 4.3.0

* Thu Dec  7 2017 Remi Collet <remi@remirepo.net> - 4.2.5-1
- Update to 4.2.5

* Mon Nov 27 2017 Remi Collet <remi@remirepo.net> - 4.2.4-1
- Update to 4.2.4

* Sat Nov 18 2017 Remi Collet <remi@remirepo.net> - 4.2.2-1
- Update to 4.2.2

* Sat Nov 11 2017 Remi Collet <remi@remirepo.net> - 4.2.1-1
- Update to 4.2.1

* Tue Nov  7 2017 Remi Collet <remi@remirepo.net> - 4.2.0-2
- fix FTBFS from Koschei using symfony package names

* Sun Oct 29 2017 Remi Collet <remi@remirepo.net> - 4.2.0-1
- Update to 4.2.0

* Thu Oct 19 2017 Remi Collet <remi@remirepo.net> - 4.1.0-1
- Update to 4.1.0

* Sun Aug 27 2017 Remi Collet <remi@remirepo.net> - 4.0.3-1
- Update to 4.0.3
- raise memory_limit for test suite

* Mon Aug  7 2017 Remi Collet <remi@remirepo.net> - 4.0.2-1
- Update to 4.0.2
- raise dependency on symfony 3.2
- raise dependency on PHP 7.0
- switch to phpunit6

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri May 12 2017 Remi Collet <remi@remirepo.net> - 3.4.0-1
- Update to 3.4.0

* Thu May 11 2017 Remi Collet <remi@remirepo.net> - 3.3.0-3
- only allow a single Symfony version

* Mon May  8 2017 Remi Collet <remi@remirepo.net> - 3.3.0-2
- fix autoloader for Symfony 3
- always use symfony 3 during the build (per upstream)

* Thu Apr 27 2017 Remi Collet <remi@remirepo.net> - 3.3.0-1
- Update to 3.3.0
- use phpunit6 on F26+

* Fri Mar  3 2017 Remi Collet <remi@remirepo.net> - 3.2.3-3
- fix autoloader for dep. with multiple versions

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun Jan 29 2017 Remi Collet <remi@fedoraproject.org> - 3.2.3-1
- update to 3.2.3

* Tue Dec  6 2016 Remi Collet <remi@fedoraproject.org> - 3.2.2-1
- update to 3.2.2

* Mon Dec  5 2016 Remi Collet <remi@fedoraproject.org> - 3.2.1-1
- update to 3.2.1

* Mon Nov 28 2016 Remi Collet <remi@fedoraproject.org> - 3.2.0-1
- update to 3.2.0

* Tue Nov 22 2016 Remi Collet <remi@fedoraproject.org> - 3.1.1-2
- ignore sebastian/exporter max version
- switch to fedora/autoloader

* Tue Sep 27 2016 Remi Collet <remi@fedoraproject.org> - 3.1.1-1
- update to 3.1.1

* Mon Sep 19 2016 Remi Collet <remi@fedoraproject.org> - 3.1.0-1
- update to 3.1.0

* Mon Jul 18 2016 Remi Collet <remi@fedoraproject.org> - 3.0.0-1
- update to 3.0.0
- raise dependency on php ^5.6 || ^7.0
- raise dependency on phpspec/prophecy ^1.5
- raise dependency on symfony/console ^2.7 || ^3.0

* Mon Mar 21 2016 Remi Collet <remi@fedoraproject.org> - 2.5.0-1
- update to 2.5.0

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sat Jan  2 2016 Remi Collet <remi@fedoraproject.org> - 2.4.1-1
- update to 2.4.1

* Sun Nov 29 2015 Remi Collet <remi@fedoraproject.org> - 2.4.0-1
- update to 2.4.0
- allow to use symfony 3.0

* Wed Oct 28 2015 Remi Collet <remi@fedoraproject.org> - 2.3.0-1
- update to 2.3.0
- raise dependency on symfony/process ^2.6

* Mon Jun 29 2015 Remi Collet <remi@fedoraproject.org> - 2.2.1-3
- switch to $fedoraClassLoader autoloader
- ensure /usr/share/php is in include_path

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 30 2015 Remi Collet <remi@fedoraproject.org> - 2.2.1-1
- update to 2.2.1

* Sun Apr 19 2015 Remi Collet <remi@fedoraproject.org> - 2.2.0-1
- update to 2.2.0
- raise dependency on phpspec/prophecy 1.4

* Tue Feb 17 2015 Remi Collet <remi@fedoraproject.org> - 2.1.1-1
- initial package
