#
# Fedora spec file for php-symfony-polyfill
#
# Copyright (c) 2015-2023 Shawn Iwinski <shawn@iwin.ski>
#
# License: MIT
# http://opensource.org/licenses/MIT
#
# Please preserve changelog entries
#

%global github_owner     symfony
%global github_name      polyfill
%global github_version   1.28.0
%global github_commit    33def419104fb3cf14be4e8638683eb9845c2522

%global composer_vendor  symfony
%global composer_project polyfill

# "php": ">=7.1"
%global php_min_ver 7.1

# Build using "--without tests" to disable tests
%bcond_without     tests

%{!?phpdir:  %global phpdir  %{_datadir}/php}

Name:          php-%{composer_vendor}-%{composer_project}
Version:       %{github_version}
Release:       5%{?github_release}%{?dist}
Summary:       Symfony polyfills backporting features to lower PHP versions

License:       MIT
URL:           https://github.com/%{github_owner}/%{github_name}
Source0:       %{url}/archive/%{github_commit}/%{name}-%{github_version}-%{github_commit}.tar.gz

BuildArch:     noarch
# Autoloader
BuildRequires: php-fedora-autoloader-devel
# Tests
%if %{with tests}
%global phpunit %{_bindir}/phpunit9
BuildRequires: php-symfony4-intl
BuildRequires: php-symfony4-var-dumper
BuildRequires: %{phpunit}
## composer.json
BuildRequires: php(language) >= %{php_min_ver}
## phpcompatinfo (computed from version 1.8.0)
BuildRequires: php-hash
BuildRequires: php-iconv
BuildRequires: php-intl
BuildRequires: php-json
BuildRequires: php-ldap
BuildRequires: php-pcre
BuildRequires: php-reflection
BuildRequires: php-spl
%endif

# composer.json
Requires:      php(language) >= %{php_min_ver}
# phpcompatinfo (computed from version 1.8.0)
Requires:      php-hash
Requires:      php-iconv
Requires:      php-intl
Requires:      php-json
Requires:      php-pcre
Requires:      php-reflection
Requires:      php-spl
# Autoloader
Requires:      php-composer(fedora/autoloader)

# Composer
Provides:      php-composer(%{composer_vendor}/%{composer_project})       = %{version}
Provides:      php-composer(%{composer_vendor}/%{composer_project}-mbstring) = %{version}
Provides:      php-composer(%{composer_vendor}/%{composer_project}-util)  = %{version}
Provides:      php-composer(%{composer_vendor}/%{composer_project}-php72) = %{version}
Provides:      php-composer(%{composer_vendor}/%{composer_project}-php73) = %{version}
Provides:      php-composer(%{composer_vendor}/%{composer_project}-php74) = %{version}
Provides:      php-composer(%{composer_vendor}/%{composer_project}-php80) = %{version}
Provides:      php-composer(%{composer_vendor}/%{composer_project}-php81) = %{version}
Provides:      php-composer(%{composer_vendor}/%{composer_project}-php82) = %{version}
Provides:      php-composer(%{composer_vendor}/%{composer_project}-php83) = %{version}

%description
%{summary}.

Autoloader: %{phpdir}/Symfony/Polyfill/autoload.php


%prep
%setup -qn %{github_name}-%{github_commit}

: Docs
mkdir -p docs/{Mbstring,Php72,Php73,Php74,Php80,Php81,Php82,Php83,Util}
mv *.md composer.json docs/
mv src/Mbstring/{*.md,composer.json}  docs/Mbstring/
mv src/Php72/{*.md,composer.json} docs/Php72/
mv src/Php73/{*.md,composer.json} docs/Php73/
mv src/Php74/{*.md,composer.json} docs/Php74/
mv src/Php80/{*.md,composer.json} docs/Php80/
mv src/Php81/{*.md,composer.json} docs/Php81/
mv src/Php82/{*.md,composer.json} docs/Php82/
mv src/Php83/{*.md,composer.json} docs/Php83/
mv src/Util/{*.md,composer.json}  docs/Util/

: Remove unneeded polyfills as extensions are available
rm -rf {src,tests}/{Apcu,Ctype,Iconv,Intl,Uuid,Xml}


%build
: Create autoloader classmap
%{_bindir}/phpab --template fedora --tolerant --output src/autoload.php src/
cat src/autoload.php

: Create autoloader
cat <<'AUTOLOAD' | tee -a src/autoload.php

\Fedora\Autoloader\Dependencies::required(array(
    __DIR__ . '/bootstrap.php', // load needed PHP version bootstrap
    __DIR__ . '/Mbstring/bootstrap.php',
));
AUTOLOAD


%install

: Library
mkdir -p %{buildroot}%{phpdir}/Symfony/Polyfill
cp -rp src/* %{buildroot}%{phpdir}/Symfony/Polyfill/


%check
%if %{with tests}
mkdir vendor
cat << 'EOF' | tee vendor/autoload.php
<?php
require '%{buildroot}%{phpdir}/Symfony/Polyfill/autoload.php';
require '%{phpdir}/Symfony4/Component/Intl/autoload.php';
require '%{phpdir}/Symfony4/Component/VarDumper/autoload.php';
EOF

: Upstream tests
RETURN_CODE=0
for cmdarg in "php %{phpunit}" php80 php81 php82 php83; do
    if which $cmdarg; then
        set $cmdarg
        $1 ${2:-%{_bindir}/phpunit9} \
            --filter '^((?!(testDecodeNumericEntity|testStrCase|testCurlFileShowsContents)).)*$' \
            --verbose \
            || RETURN_CODE=1
    fi
done
exit $RETURN_CODE
%else
: Tests skipped
%endif


%files
%license LICENSE
%doc docs/*
%dir %{phpdir}/Symfony
     %{phpdir}/Symfony/Polyfill
%exclude %{phpdir}/Symfony/Polyfill/*/LICENSE


%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.28.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.28.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.28.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.28.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Tue Aug 29 2023 Remi Collet <remi@remirepo.net> - 1.28.0-1
- update to 1.28.0

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.27.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.27.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Mon Nov 14 2022 Remi Collet <remi@remirepo.net> - 1.27.0-1
- update to 1.27.0
- provides symfony/polyfill-php83

* Wed Oct 12 2022 Shawn Iwinski <shawn.iwinski@gmail.com> - 1.26.0-3
- Skip tests known to fail

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.26.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jun  2 2022 Remi Collet <remi@remirepo.net> - 1.26.0-1
- update to 1.26.0
- provides symfony/polyfill-php81

* Fri Mar  4 2022 Remi Collet <remi@remirepo.net> - 1.25.0-1
- update to 1.25.0

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.24.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jan  5 2022 Remi Collet <remi@remirepo.net> - 1.24.0-1
- update to 1.24.0

* Tue Jan  4 2022 Remi Collet <remi@remirepo.net> - 1.23.2-1
- update to 1.23.2

* Thu Jul 29 2021 Remi Collet <remi@remirepo.net> - 1.23.1-1
- update to 1.23.1

* Tue Jul 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.23.0-2
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon May 31 2021 Remi Collet <remi@remirepo.net> - 1.23.0-1
- update to 1.23.0

* Tue Feb 16 2021 Remi Collet <remi@remirepo.net> - 1.22.1-1
- update to 1.22.1

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.22.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Jan  8 2021 Remi Collet <remi@remirepo.net> - 1.22.0-1
- update to 1.22.0
- provides symfony/polyfill-php81

* Mon Oct 26 2020 Remi Collet <remi@remirepo.net> - 1.20.0-1
- update to 1.20.0
- raise dependency on PHP 7.1
- switch to phpunit9

* Fri Oct 23 2020 Remi Collet <remi@remirepo.net> - 1.19.0-1
- update to 1.19.0

* Tue Aug 11 2020 Remi Collet <remi@remirepo.net> - 1.18.1-1
- update to 1.18.1

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.18.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 15 2020 Remi Collet <remi@remirepo.net> - 1.18.0-1
- update to 1.18.0

* Thu Jul  2 2020 Remi Collet <remi@remirepo.net> - 1.17.1-1
- update to 1.17.1

* Wed May 13 2020 Remi Collet <remi@remirepo.net> - 1.17.0-1
- update to 1.17.0

* Fri Mar 27 2020 Remi Collet <remi@remirepo.net> - 1.15.0-1
- update to 1.15.0

* Mon Feb 17 2020 Remi Collet <remi@remirepo.net> - 1.14.0-1
- update to 1.14.0
- provides symfony/polyfill-php80

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.13.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Dec  4 2019 Remi Collet <remi@remirepo.net> - 1.13.1-1
- update to 1.13.1 (no change)

* Thu Nov 28 2019 Remi Collet <remi@remirepo.net> - 1.13.0-1
- update to 1.13.0

* Tue Aug 20 2019 Remi Collet <remi@remirepo.net> - 1.12.0-1
- update to 1.12.0
- add symfony/polyfill-php74

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.11.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Mar 26 2019 Remi Collet <remi@remirepo.net> - 1.11.0-1
- update to 1.11.0

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Dec 27 2018 Remi Collet <remi@remirepo.net> - 1.10.0-1
- update to 1.10.0

* Mon Aug 27 2018 Remi Collet <remi@remirepo.net> - 1.9.0-1
- update to 1.9.0

* Mon Jul 16 2018 Remi Collet <remi@remirepo.net> - 1.8.0-3
- raise dependency on PHP 7 and ignore dependencies on
  ircmaxell/password-compat and paragonie/random_compat

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri May  4 2018 Remi Collet <remi@remirepo.net> - 1.8.0-1
- update to 1.8.0
- add symfony/polyfill-php73
- use range dependencies

* Wed Apr 11 2018 Remi Collet <remi@remirepo.net> - 1.7.0-2
- add symfony/polyfill-mbstring for mb_chr, mb_ord, mb_scrub
- add dependency on iconv and intl extensions

* Fri Mar  2 2018 Remi Collet <remi@remirepo.net> - 1.7.0-1
- Update to 1.7.0

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 30 2017 Shawn Iwinski <shawn.iwinski@gmail.com> - 1.5.0-1
- Updated to 1.5.0 (RHBZ #1482156)
- Added version constraints to ircmaxell/password-compat
- Added max version constraint to paragonie/random_compat BuildeRequires
- Removed php-mbstring dependency

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Jul 09 2017 Shawn Iwinski <shawn.iwinski@gmail.com> - 1.4.0-1
- Updated to 1.4.0 (RHBZ #1460473)
- Provide php-composer(symfony/polyfill-php72)
- Test with SCLs if available

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Nov 14 2016 Remi Collet <remi@fedoraproject.org> - 1.3.0-1
- Updated to 1.3.0
- provide php-composer(symfony/polyfill-php71)
- switch to fedora/autoloader

* Thu Jun 16 2016 Shawn Iwinski <shawn.iwinski@gmail.com> - 1.2.0-1
- Updated to 1.2.0 (RHBZ #1301791)

* Tue Apr 12 2016 Shawn Iwinski <shawn.iwinski@gmail.com> - 1.1.1-1
- Updated to 1.1.1 (RHBZ #1301791)

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sun Jan 03 2016 Shawn Iwinski <shawn.iwinski@gmail.com> - 1.0.1-1
- Updated to 1.0.1 (RHBZ #1294916)

* Mon Dec 07 2015 Shawn Iwinski <shawn@iwin.ski> - 1.0.0-3
- Fixed Util docs
- Added "%%dir %%{phpdir}/Symfony" to %%files

* Sun Dec 06 2015 Shawn Iwinski <shawn@iwin.ski> - 1.0.0-2
- Always include ALL polyfills

* Wed Nov 25 2015 Shawn Iwinski <shawn@iwin.ski> - 1.0.0-1
- Initial package
