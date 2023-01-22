# fedora spec file for php-scssphp
#
# Copyright (c) 2012-2019 Shawn Iwinski <shawn.iwinski@gmail.com>
#                         Remi Collet <remi@fedoraproject.org>
#                         Christian Glombek <christian.glombek@rwth-aachen.de>
#               2020-2022 Christopher Engelhard <ce@lcts.de>
# License: MIT
#
# Please preserve the changelog entries

# package and composer name
%global vendor      scssphp
%global project     scssphp

# PHP namespace and directory
%global ns_vendor   ScssPhp
%global ns_project  ScssPhp
%global ns_dir      %{ns_vendor}/%( echo '%{ns_project}' | sed  's|\\\\|\/|g' )

# Github
%global gh_vendor   scssphp
%global gh_project  scssphp
%global commit      6d44282ccf283e133ab70b6282f8e068ff2f9bf9
%global scommit     %(c=%{commit}; echo ${c:0:7})

# tests
%bcond_without tests

#-- PREAMBLE ------------------------------------------------------------------#
Name:           php-scssphp
Version:        1.10.5
Release:        2%{?dist}
Summary:        A compiler for SCSS written in PHP

License:        MIT
URL:            https://github.com/%{gh_vendor}/%{gh_project}
# Since github tarballs are lacking the tests, source is created via a local git checkout instead.
# Use ./makesrc.sh in the same directory as the specfile to generate the source archive
Source0:        %{name}-%{version}-%{scommit}.tgz
Source1:        makesrc.sh

# this removes use of Symfony\Bridge\PhpUnit\ExpectDeprecationTrait, which is only available in Symfony5
# tests need to be run with --exclude-group legady because of this patch
Patch01:        01-disable-symfony5-features-in-tests.patch

BuildArch:      noarch

# for the autoloader
Requires:	php-composer(fedora/autoloader)

# from composer.json
Requires:	php(language) >= 5.6.0
Requires:	php-ctype
Requires:       php-json
Recommends:     (php-mbstring or php-iconv)

# from phpcompatinfo
Requires:	php-reflection
Requires:	php-pcre
Requires:	php-spl
Requires:	php-date

# for autoloader check
BuildRequires:  php-composer(fedora/autoloader)
BuildRequires:  %{_bindir}/php
BuildRequires:  php(language) >= 5.6.0

%if %{with tests}
# for tests
BuildRequires: phpunit9
BuildRequires: php-ctype
BuildRequires: php-json
BuildRequires: (php-mbstring or php-iconv)
BuildRequires: php-reflection
BuildRequires: php-pcre
BuildRequires: php-spl
BuildRequires: php-date
#BuildRequires: php-composer(barmani/composer-bin-plugin)
#BuildRequires: php-composer(sass/sass-spec)
BuildRequires: php-composer(squizlabs/php_codesniffer)
BuildRequires: php-composer(symfony/phpunit-bridge)
#BuildRequires: php-composer(thoughtbot/bourbon)
#BuildRequires: php-composer(twbs/bootstrap)
#BuildRequires: php-composer(zurb/foundation)
%endif

# composer provides
Provides:	php-%{vendor}-%{project} = %{version}
Provides:	php-composer(%{vendor}/%{project}) = %{version}

%description
SCSS (http://sass-lang.com/) is a CSS preprocessor that adds many features like
variables, mixins, imports, color manipulation, functions, and tons of other
powerful features.

The entire compiler comes in a single class file ready for including in any kind
of project in addition to a command line tool for running the compiler from the
terminal.

scssphp implements SCSS. It does not implement the SASS syntax, only the SCSS
syntax.

The library autoloader is: %{_datadir}/php/%{ns_dir}/autoload.php


#-- PREP, BUILD & INSTALL -----------------------------------------------------#
%prep
%autosetup -p1 -n %{gh_project}-%{commit}

%build
: Adjust bin autoload require
sed "/scss.inc.php/s#.*#require_once '%{phpdir}/Leafo/ScssPhp/autoload.php';#" \
    -i bin/pscss

%install
: Create installation directory
mkdir -p %{buildroot}%{_bindir}
install -pm 0755 bin/pscss %{buildroot}%{_bindir}/

mkdir -p   %{buildroot}%{_datadir}/php/%{ns_dir}
cp -pr src/* %{buildroot}%{_datadir}/php/%{ns_dir}

: Generate an autoloader
cat <<'EOF' | tee %{buildroot}%{_datadir}/php/%{ns_dir}/autoload.php
<?php
require_once '%{_datadir}/php/Fedora/Autoloader/autoload.php';

// classes
\Fedora\Autoloader\Autoload::addPsr4('%{ns_vendor}\\%{ns_project}', __DIR__);

// files & dependencies
\Fedora\Autoloader\Dependencies::required(array(
  // no mandatory dependencies
));

\Fedora\Autoloader\Dependencies::optional(array(
   // no optional dependencies
));
EOF

%check
: Check the autoloader
%{_bindir}/php -r "
    require_once '%{buildroot}%{_datadir}/php/%{ns_dir}/autoload.php';
    exit(
        class_exists('%{ns_vendor}\%{ns_project}\Compiler')
        ? 0 : 1
    );
"

%if %{with tests}
#: Skip tests requiring non-resolved dependencies
#rm -f tests/ApiTest.php
rm -f tests/FrameworkTest.php

#: Skip flapping/flakey test
#sed '/2147483647/d' -i tests/Base64VLQTest.php

: Create a autoloader for tests
mkdir vendor
cat << 'EOF' | tee vendor/autoload.php
<?php
require_once '%{buildroot}%{_datadir}/php/%{ns_dir}/autoload.php';
require_once '%{_datadir}/php/Symfony4/Bridge/PhpUnit/autoload.php';


\Fedora\Autoloader\Autoload::addPsr4('%{ns_vendor}\%{ns_project}\Test', dirname(__DIR__).'/tests');
EOF

: Run phpunit tests
# exclude test group legacy as it requires symfony 5+
%{_bindir}/phpunit9 --verbose --exclude-group legacy
%endif

#-- FILES ---------------------------------------------------------------------#
%files
%license LICENSE.md
%doc composer.json
%doc README.md
%dir %{_datadir}/php/%{ns_vendor}
%{_datadir}/php/%{ns_dir}
%{_bindir}/pscss

#-- CHANGELOG -----------------------------------------------------------------#
%changelog
* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Tue Aug 9 2022 Christopher Engelhard <ce@lcts.de> - 1.10.5-1
- Update to 1.10.5-1 (rhbz#1876684, rhbz#1933633)
- Upstream has changed from leafo/scssphp to scssphp/scssphp on packagist
- Update tests for PHP 8 and PHPUnit 9

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.4-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Sep 13 2019 Remi Collet <remi@remirepo.net> - 0.8.4-1
- update to 0.8.4
- add patch for PHP 7.4 from
  https://github.com/leafo/scssphp/pull/710

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Jun 03 2019 Shawn Iwinski <shawn.iwinski@gmail.com> - 0.8.3-1
- Update to 0.8.3 (RHBZ #1716011)

* Fri May 10 2019 Shawn Iwinski <shawn.iwinski@gmail.com> - 0.8.2-1
- Update to 0.8.2 (RHBZ #1703256)

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Dec 21 2018 Remi Collet <remi@remirepo.net> - 0.7.7-1
- update to 0.7.7

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon May 28 2018 Shawn Iwinski <shawn.iwinski@gmail.com> - 0.7.6-1
- Update to 0.7.6 (RHBZ #1582167)
- Add composer.json to repo

* Sun Mar 25 2018 Shawn Iwinski <shawn.iwinski@gmail.com> - 0.7.5-2
- Update get source script to save in spec directory
- Update phpcompatinfo computed dependencies
- Remove code sniffer dependency and test
- Modify upstream test run

* Tue Feb 13 2018 Christian Glombek <christian.glombek@rwth-aachen.de> - 0.7.5-1
- Updated to 0.7.5 (RHBZ #1504394)
- Use php_condesniffer for testing

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Mar 04 2017 Shawn Iwinski <shawn.iwinski@gmail.com> - 0.6.7-1
- Updated to 0.6.7 (RHBZ #1426927)
- Switch autoloader to php-composer(fedora/autoloader)
- Test with SCLs if available

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun Sep 25 2016 Shawn Iwinski <shawn.iwinski@gmail.com> - 0.6.6-1
- Updated to 0.6.6 (RHBZ #1376293)

* Sat Jul 23 2016 Shawn Iwinski <shawn.iwinski@gmail.com> - 0.6.5-1
- Updated to 0.6.5 (RHBZ #1347068)
- Dropped pre-0.1.0 compat

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jan 20 2016 Shawn Iwinski <shawn.iwinski@gmail.com> - 0.4.0-1
- Updated to 0.4.0 (RHBZ #1274939)
- Removed php-json dependency

* Sun Oct 11 2015 Shawn Iwinski <shawn.iwinski@gmail.com> - 0.3.2-1
- Updated to 0.3.2 (RHBZ #1268709)

* Sun Sep 20 2015 Shawn Iwinski <shawn.iwinski@gmail.com> - 0.3.1-1
- Updated to 0.3.1 (RHBZ #1256168)
- Updated URL
- Added standard "php-{COMPOSER_VENDOR}-{COMPOSER_PROJECT}" naming provides
- Added library version value check

* Thu Aug 13 2015 Shawn Iwinski <shawn.iwinski@gmail.com> - 0.1.9-1
- Updated to 0.1.9 (RHBZ #1238727)
- As of version 0.1.7 license is just MIT (i.e. GPLv3 removed)

* Sun Jun 28 2015 Shawn Iwinski <shawn.iwinski@gmail.com> - 0.1.6-1
- Updated to 0.1.6 (RHBZ #1226748)
- Added autoloader

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Jan 02 2015 Shawn Iwinski <shawn.iwinski@gmail.com> - 0.1.1-2
- Bump release for Koji/Bodhi

* Thu Oct 30 2014 Shawn Iwinski <shawn.iwinski@gmail.com> - 0.1.1-1
- Updated to 0.1.1 (BZ #1126612)
- Removed man page
- %%license usage

* Tue Aug 19 2014 Shawn Iwinski <shawn.iwinski@gmail.com> - 0.0.15-1
- Updated to 0.0.15 (BZ #1126612)

* Mon Jul 07 2014 Shawn Iwinski <shawn.iwinski@gmail.com> - 0.0.12-1
- Updated to 0.0.12 (BZ #1116615)
- Added option to build without tests ("--without tests")

* Sun Jun 08 2014 Remi Collet <remi@fedoraproject.org> - 0.0.10-2
- fix FTBFS, ignore max version of PHPUnit
- provides php-composer(leafo/scssphp)

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon Apr 21 2014 Shawn Iwinski <shawn.iwinski@gmail.com> - 0.0.10-1
- Updated to 0.0.10 (BZ #1087738)

* Sun Dec 29 2013 Shawn Iwinski <shawn.iwinski@gmail.com> - 0.0.9-1
- Updated to 0.0.9 (BZ #1046671)
- Spec cleanup

* Fri Nov 15 2013 Shawn Iwinski <shawn.iwinski@gmail.com> - 0.0.8-1
- Updated to 0.0.8 (BZ #1009564)

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Jun 07 2013 Shawn Iwinski <shawn.iwinski@gmail.com> - 0.0.7-1
- Updated to 0.0.7 (BZ #967834)

* Sat Mar 16 2013 Shawn Iwinski <shawn.iwinski@gmail.com> - 0.0.5-1
- Updated to version 0.0.5
- php-cli => php(language)
- %%{__php} => %%{_bindir}/php

* Sat Mar 09 2013 Shawn Iwinski <shawn.iwinski@gmail.com> - 0.0.4-2.20130301git3463d7d
- Updated to latest snapshot
- php-common => php-cli
- Added man page
- Removed tests from package

* Tue Nov 27 2012 Shawn Iwinski <shawn.iwinski@gmail.com> - 0.0.4-1
- Initial package
