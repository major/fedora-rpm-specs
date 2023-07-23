# remirepo/fedora spec file for php-phpunit-PHPUnit-SkeletonGenerator
#
# Copyright (c) 2012-2018 Remi Collet
# License: CC-BY-SA
# http://creativecommons.org/licenses/by-sa/4.0/
#
# Please, preserve the changelog entries
#
%global gh_commit    c0eeb18f31893c2f0c387bce84f8a3816a0eacd1
%global gh_short     %(c=%{gh_commit}; echo ${c:0:7})
%global gh_owner     sebastianbergmann
%global gh_project   phpunit-skeleton-generator
%global php_home     %{_datadir}/php
%global pear_name    PHPUnit_SkeletonGenerator
%global pear_channel pear.phpunit.de
%global with_tests   %{?_without_tests:0}%{!?_without_tests:1}

Name:           php-phpunit-PHPUnit-SkeletonGenerator
Version:        2.0.1
Release:        21%{?dist}
Summary:        Tool that can generate skeleton test classes

License:        BSD
URL:            https://github.com/%{gh_owner}/%{gh_project}
Source0:        https://github.com/%{gh_owner}/%{gh_project}/archive/%{gh_commit}/%{gh_project}-%{version}.tar.gz

# Autoloader
Patch0:         %{name}-rpm.patch
# For PHP 7.3
Patch1:         %{name}-php73.patch

BuildArch:      noarch
BuildRequires:  php(language) >= 5.3.3
BuildRequires:  %{_bindir}/phpab
%if %{with_tests}
BuildRequires:  php-composer(phpunit/php-text-template) <  2
BuildRequires:  php-composer(phpunit/php-text-template) >= 1.2
BuildRequires:  php-composer(sebastian/version)         <  3
BuildRequires:  php-composer(sebastian/version)         >= 1.0
BuildRequires:  php-composer(symfony/console)           <  3
BuildRequires:  php-composer(symfony/console)           >= 2.4
# From composer.json, requires-dev
#        "mikey179/vfsStream": "~1.2"
#        "phpunit/phpunit": "~4.0",
BuildRequires:  php-composer(mikey179/vfsStream)        <  2
BuildRequires:  php-composer(mikey179/vfsStream)        >= 1.2
BuildRequires:  %{_bindir}/phpunit
# For our autoloader
BuildRequires:  php-fedora-autoloader-devel
%endif

# From composer.json, requires
#        "php": ">=5.3.3",
#        "phpunit/php-text-template": "~1.2",
#        "sebastian/version": "~1.0",
#        "symfony/console": "~2.4"
Requires:       php(language) >= 5.3.3
Requires:       php-composer(phpunit/php-text-template) >= 1.2
Requires:       php-composer(phpunit/php-text-template) <  2
Requires:       php-composer(sebastian/version)         >= 1.0
Requires:       php-composer(sebastian/version)         <  3
Requires:       php-composer(symfony/console)           >= 2.4
Requires:       php-composer(symfony/console)           <  3
# Need for our autoloader patch
Requires:       php-composer(fedora/autoloader)
# From phpcompatinfo report from 2.0.0
Requires:       php-date
Requires:       php-pcre
Requires:       php-spl
Requires:       php-tokenizer

Provides:       php-composer(phpunit/phpunit-skeleton-generator) = %{version}


%description
Tool that can generate skeleton test classes from production code classes
and vice versa.


%prep
%setup -q -n %{gh_project}-%{gh_commit}

%patch0 -p1 -b .rpm
%patch1 -p1

find . -type f -name \*.rpm -delete


%build
%{_bindir}/phpab \
  --output   src/autoload.php \
  --template fedora \
  src
cat << 'EOF' | tee -a src/autoload.php
\Fedora\Autoloader\Dependencies::required(array(
    '%{php_home}/Symfony/Component/Console/autoload.php',
    '%{php_home}/Text/Template/Autoload.php',
    '%{php_home}/SebastianBergmann/Version/autoload.php',
));
EOF


%install
mkdir -p   %{buildroot}%{php_home}/SebastianBergmann/PHPUnit
cp -pr src %{buildroot}%{php_home}/SebastianBergmann/PHPUnit/SkeletonGenerator

install -D -p -m 755 phpunit-skelgen %{buildroot}%{_bindir}/phpunit-skelgen


%if %{with_tests}
%check
mkdir vendor
cat << 'EOF' | tee vendor/autoload.php
<?php
require_once '%{buildroot}%{php_home}/SebastianBergmann/PHPUnit/SkeletonGenerator/autoload.php';
require_once '%{php_home}/org/bovigo/vfs/autoload.php';
EOF

cd build
for cmd in php php56 php70 php71 php72 php73; do
  if which $cmd; then
    $cmd %{_bindir}/phpunit --verbose
  fi
done
%endif


%post
if [ -x %{_bindir}/pear ]; then
   %{_bindir}/pear uninstall --nodeps --ignore-errors --register-only \
      %{pear_channel}/%{pear_name} >/dev/null || :
fi


%files
%{!?_licensedir:%global license %%doc}
%license LICENSE
%doc README.md
%doc composer.json
%{_bindir}/phpunit-skelgen
%dir %{php_home}/SebastianBergmann
%dir %{php_home}/SebastianBergmann/PHPUnit
     %{php_home}/SebastianBergmann/PHPUnit/SkeletonGenerator


%changelog
* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Oct 15 2018 Remi Collet <remi@fedoraproject.org> - 2.0.1-11
- add patch for PHP 7.3

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Thu May 11 2017 Remi Collet <remi@fedoraproject.org> - 2.0.1-7
- switch to fedora/autoloader

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Apr 18 2016 Remi Collet <remi@fedoraproject.org> - 2.0.1-5
- allow sebastian/version 2.0

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Jun 29 2015 Remi Collet <remi@fedoraproject.org> - 2.0.1-3
- use $fedoraClassLoader autoloader

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Jul 22 2014 Remi Collet <remi@fedoraproject.org> - 2.0.1-1
- update to 2.0.1 (no change)
- add BR mikey179/vfsStream
- enable test during build
- composer dependencies

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue May 13 2014 Remi Collet <remi@fedoraproject.org> - 2.0.0-1
- update to 2.0.0
- add generated autoloader
- switch from php-ezc-ConsoleTools to php-symfony-Console
- add dependency on php-phpunit-Version

* Wed Apr 30 2014 Remi Collet <remi@fedoraproject.org> - 1.2.1-4
- cleanup pear registry

* Tue Apr 29 2014 Remi Collet <remi@fedoraproject.org> - 1.2.1-3
- sources from github

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sat Jun 01 2013 Remi Collet <remi@fedoraproject.org> - 1.2.1-1
- Update to 1.2.1
- add explicit requires

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Mon Oct 22 2012 Remi Collet <remi@fedoraproject.org> - 1.2.0-1
- Version 1.2.0 (stable) - API 1.2.0 (stable)
- raise dependency: php >= 5.3.3

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Mar 03 2012 Remi Collet <remi@fedoraproject.org> - 1.1.0-1
- Version 1.1.0 (stable) - API 1.1.0 (stable)

* Sat Jan 21 2012 Remi Collet <remi@fedoraproject.org> - 1.0.0-1
- initial package

