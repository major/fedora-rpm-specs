#
# Fedora spec file for php-pdepend-PHP-Depend
#
# License: MIT
# http://opensource.org/licenses/MIT
#
# Please, preserve the changelog entries
#
%global gh_commit    7a892d56ceafd804b4a2ecc85184640937ce9e84
%global gh_short     %(c=%{gh_commit}; echo ${c:0:7})
%global gh_owner     pdepend
%global gh_project   pdepend
%{!?__pear: %global __pear %{_bindir}/pear}
%global pear_name    PHP_Depend
%global pear_channel pear.pdepend.org
%global php_home     %{_datadir}/php/PDepend
%global with_tests   0%{!?_without_tests:1}

%global sym_pref php-symfony4
%global sym_path %{_datadir}/php/Symfony4

Name:           php-pdepend-PHP-Depend
Version:        2.12.1
Release:        1%{?dist}
Summary:        PHP_Depend design quality metrics for PHP package

License:        BSD
URL:            http://pdepend.org/
# git snashop to get upstream test suite
Source0:        %{name}-%{version}-%{gh_short}.tgz
Source1:        makesrc.sh

# Autoloader
Patch0:         %{name}-rpm.patch

BuildArch:      noarch
%if %{with_tests}
# From composer/json, "require-dev": {
#        "phpunit/phpunit": "^4.8.36|^5.7.27",
#        "squizlabs/php_codesniffer": "^2.0.0"
BuildRequires:  php-composer(phpunit/phpunit) >= 5.7.27
BuildRequires:  php(language) >= 5.3.7
BuildRequires:  %{sym_pref}-dependency-injection
BuildRequires:  %{sym_pref}-filesystem
BuildRequires:  %{sym_pref}-config
BuildRequires:  php-bcmath
BuildRequires:  php-date
BuildRequires:  php-dom
BuildRequires:  php-iconv
BuildRequires:  php-libxml
BuildRequires:  php-mbstring
BuildRequires:  php-pcre
BuildRequires:  php-reflection
BuildRequires:  php-simplexml
BuildRequires:  php-spl
BuildRequires:  php-tokenizer
BuildRequires:  php-xml
# Autoloader
BuildRequires:  php-composer(fedora/autoloader)
%endif

# From composer.json, "require": {
#        "php": ">=5.3.7"
#        "symfony/dependency-injection": "^2.3.0|^3|^4|^5|^6.0",
#        "symfony/filesystem": "^2.3.0|^3|^4|^5|^6.0",
#        "symfony/config": "^2.3.0|^3|^4|^5|^6.0",
Requires:       php(language) >= 5.3.7
Requires:       %{sym_pref}-dependency-injection
Requires:       %{sym_pref}-filesystem
Requires:       %{sym_pref}-config
# From phpcompatinfo report for version 2.3.0
Requires:       php-bcmath
Requires:       php-date
Requires:       php-dom
Requires:       php-iconv
Requires:       php-libxml
Requires:       php-mbstring
Requires:       php-pcre
Requires:       php-reflection
Requires:       php-simplexml
Requires:       php-spl
Requires:       php-tokenizer
Requires:       php-xml
# Autoloader
Requires:       php-composer(fedora/autoloader)

# Single package in this channel
Obsoletes:      php-channel-pdepend <= 1.3

Provides:       php-pear(%{pear_channel}/%{pear_name}) = %{version}
Provides:       php-composer(%{gh_owner}/%{gh_project}) = %{version}
Provides:       pdepend = %{version}


%description
PHP_Depend is an adaption of the established Java development tool JDepend.
This tool shows you the quality of your design in the terms of extensibility,
reusability and maintainability.


%prep
%setup -q -n %{gh_project}-%{gh_commit}

%patch0 -p0
cat << 'EOF' | tee src/main/php/PDepend/autoload.php
<?php
/* Autoloader for %{name} and its dependencies */

require_once '%{_datadir}/php/Fedora/Autoloader/autoload.php';
\Fedora\Autoloader\Autoload::addPsr4('PDepend\\', __DIR__);
\Fedora\Autoloader\Dependencies::required([
    '%{sym_path}/Component/DependencyInjection/autoload.php',
    '%{sym_path}/Component/Filesystem/autoload.php',
    '%{sym_path}/Component/Config/autoload.php',
]);
EOF

find src/main/php -name \*php -exec sed -e 's:@package_version@:%{version}:' -i {} \;
find src/test/php -name \*xml -exec sed -e 's:@package_version@:%{version}:' -i {} \;


%build
# Empty build section, most likely nothing required.


%install
: Library
mkdir -p $(dirname %{buildroot}%{php_home})
cp -pr src/main/php/PDepend %{buildroot}%{php_home}

: Resources
mkdir -p %{buildroot}%{_datadir}/%{name}
cp -pr src/main/resources %{buildroot}%{_datadir}/%{name}/resources

: Command
install -Dpm 0755 src/bin/pdepend %{buildroot}%{_bindir}/pdepend


%check
%if %{with_tests}
cat << 'EOF' | tee src/test/php/PDepend/bootstrap.php
<?php
require '%{buildroot}%{php_home}/autoload.php';
\Fedora\Autoloader\Autoload::addPsr4('PDepend\\', __DIR__);
EOF

# testBinCanReadInput rely on git layout
ret=0
for cmd in php php74 php80 php81 php82; do
  if which $cmd; then
    $cmd %{_bindir}/phpunit -d memory_limit=1G \
      --no-coverage \
      --filter '^((?!(testBinCanReadInput)).)*$' \
      --verbose || ret=1
  fi
done
exit $ret
%else
: Test suite disabled
%endif


%pre
if [ -x %{_bindir}/pear ]; then
   %{_bindir}/pear uninstall --nodeps --ignore-errors --register-only \
      %{pear_channel}/%{pear_name} >/dev/null || :
fi


%files
%license LICENSE
%doc composer.json
%doc CHANGELOG.md
%{php_home}
%{_datadir}/%{name}
%{_bindir}/pdepend


%changelog
* Mon Sep 12 2022 Remi Collet <remi@remirepo.net> - 2.12.1-1
- update to 2.12.1

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.10.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Feb 23 2022 Remi Collet <remi@remirepo.net> - 2.10.3-1
- update to 2.10.3

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.10.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Nov 17 2021 Remi Collet <remi@remirepo.net> - 2.10.2-1
- update to 2.10.2

* Mon Oct 11 2021 Remi Collet <remi@remirepo.net> - 2.10.1-1
- update to 2.10.1

* Thu Jul 22 2021 Remi Collet <remi@remirepo.net> - 2.10.0-1
- update to 2.10.0

* Fri Apr 16 2021 Remi Collet <remi@remirepo.net> - 2.9.1-1
- update to 2.9.1

* Thu Mar 11 2021 Remi Collet <remi@remirepo.net> - 2.9.0-1
- update to 2.9.0

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun 23 2020 Remi Collet <remi@remirepo.net> - 2.8.0-1
- update to 2.8.0

* Thu Feb 13 2020 Remi Collet <remi@remirepo.net> - 2.7.1-1
- update to 2.7.1

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Jan 27 2020 Remi Collet <remi@remirepo.net> - 2.7.0-1
- update to 2.7.0

* Fri Jan  3 2020 Remi Collet <remi@remirepo.net> - 2.6.1-1
- update to 2.6.1

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Dec 13 2017 Remi Collet <remi@remirepo.net> - 2.5.2-2
- Update to 2.5.2 (new sources)

* Wed Dec 13 2017 Remi Collet <remi@remirepo.net> - 2.5.2-1
- Update to 2.5.2
- switch to symfony package names
- open https://github.com/pdepend/pdepend/issues/357 missing changelog

* Tue Nov 21 2017 Remi Collet <remi@remirepo.net> - 2.5.1-1
- Update to 2.5.1
- open https://github.com/pdepend/pdepend/issues/337 missing changelog

* Wed Nov  1 2017 Remi Collet <remi@fedoraproject.org> - 2.5.0-5
- fix FTBFS from Koschei, add patch for PHP 7.2 from
  https://github.com/pdepend/pdepend/pull/303
- provide pdepend
- allow only a symfony version

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed May 10 2017 Remi Collet <remi@fedoraproject.org> - 2.5.0-3
- adapt for Symfony v3

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Jan 19 2017 Remi Collet <remi@fedoraproject.org> - 2.5.0-1
- update to 2.5.0

* Wed Jan 11 2017 Remi Collet <remi@fedoraproject.org> - 2.4.1-1
- update to 2.4.1

* Tue Jan 10 2017 Remi Collet <remi@fedoraproject.org> - 2.4.0-1
- update to 2.4.0

* Thu Nov 24 2016 Remi Collet <remi@fedoraproject.org> - 2.3.2-1
- update to 2.3.2

* Wed Nov 23 2016 Remi Collet <remi@fedoraproject.org> - 2.3.0-1
- update to 2.3.0
- add dependency on iconv, mbstring and xml

* Tue Nov 22 2016 Remi Collet <remi@fedoraproject.org> - 2.2.6-1
- update to 2.2.6
- switch to fedora/autoloader

* Thu Mar 10 2016 Remi Collet <remi@fedoraproject.org> - 2.2.4-1
- update to 2.2.4

* Tue Feb 23 2016 Remi Collet <remi@fedoraproject.org> - 2.2.3-1
- update to 2.2.3

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Oct 16 2015 Remi Collet <remi@fedoraproject.org> - 2.2.2-1
- update to 2.2.2

* Fri Sep 25 2015 Remi Collet <remi@fedoraproject.org> - 2.2.1-1
- update to 2.2.1

* Mon Sep 21 2015 Remi Collet <remi@fedoraproject.org> - 2.2.0-1
- update to 2.2.0

* Mon Jul 13 2015 Remi Collet <remi@fedoraproject.org> - 2.1.0-1
- update to 2.1.0
- switch from pear channel to git snapshot sources
- run upstream test suite during build

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Nov 16 2013 Christof Damian <christof@damian.net> - 1.1.2-1
- upstream 1.1.2

* Mon Aug  5 2013 Christof Damian <christof@damian.net> - 1.1.1-2
- explicit requires from Remi
- use tar -i for broken source

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue Jul 30 2013 Christof Damian <christof@damian.net> - 1.1.1-1
- upstream 1.1.1

* Sat Feb 23 2013 Christof Damian <christof@damian.net> - 1.1.0-3
- use pear_metadir FTBFS 914350

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Sep 12 2012 Christof Damian <christof@damian.net> - 1.1.0-1
- upstream 1.1.0

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue May  1 2012 Christof Damian <christof@damian.net> - 1.0.7-1
- upstream 1.0.7

* Wed Apr 11 2012 Christof Damian <christof@damian.net> - 1.0.5-1
- upstream 1.0.5

* Fri Mar  2 2012 Christof Damian <christof@damian.net> - 1.0.4-1
- upstream 1.0.4

* Thu Feb  9 2012 Christof Damian <christof@damian.net> - 1.0.1-1
- upstream 1.0.1

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sun Oct 30 2011 Christof Damian <christof@damian.net> - 0.10.6-1
- upstream 0.10.6

* Fri May 20 2011 Christof Damian <christof@damian.net> - 0.10.5-1
- upstream 0.10.5

* Fri Mar  4 2011 Christof Damian <christof@damian.net> - 0.10.3-1
- upstream 0.10.3

* Mon Feb 28 2011 Christof Damian <cdamian@robin.gotham.krass.com> - 0.10.2-1
- upstream 0.10.2

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sun Feb  6 2011 Christof Damian <christof@damian.net> - 0.10.1-1
- upstream stable release 0.10.1 

* Fri Sep 17 2010 Christof Damian <christof@damian.net> - 0.9.19-1
- upstream 0.9.19

* Fri Sep  3 2010 Christof Damian <christof@damian.net> - 0.9.18-1
- upstream 0.9.18

* Fri Jul 30 2010 Christof Damian <christof@damian.net> - 0.9.17-1
- upstream 0.9.17

* Sun Jun 20 2010 Christof Damian <christof@damian.net> - 0.9.16-1
- upstream 0.9.16: bugfixes

* Sat May 22 2010 Christof Damian <christof@damian.net> - 0.9.14-1
- upstream 0.9.14

* Mon May 10 2010 Christof Damian <christof@damian.net> - 0.9.13-1
- upstream 0.9.13 important bugfixes

* Tue Apr 27 2010 Christof Damian <christof@damian.net> - 0.9.12-1
- upstream 0.9.12
- upstream removed all tests

* Wed Mar  3 2010 Christof Damian <christof@damian.net> - 0.9.11-1
- upstream 0.9.11

* Tue Feb 23 2010 Christof Damian <christof@damian.net> - 0.9.10-1
- upstream 0.9.10
- replaced define macro with global

* Tue Jan 26 2010 Christof Damian <christof@damian.net> 0.9.9-2
- require pecl imagick, which is an optional requirement
- require php-xml for dom
- change postun to use channel macro for consistency
- own /usr/share/pear/PHP
- include test files (which currently don't work)

* Fri Jan 1 2010 Christof Damian <christof@damian.net> 0.9.9-1
- initial release
