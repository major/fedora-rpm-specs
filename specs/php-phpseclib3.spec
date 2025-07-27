%global composer_vendor         phpseclib
%global composer_project        phpseclib

%global github_owner            phpseclib
%global github_name             phpseclib
%bcond_without                  tests

Version:    3.0.44
Release:    2%{?dist}
%global vmajor %(v="%{version}"; v=(${v//./ }); echo "${v[0]}")

Name:       php-%{composer_project}%{vmajor}
Summary:    PHP Secure Communications Library
License:    MIT
URL:        https://github.com/%{github_owner}/%{github_name}

Source0:    %{name}-%{version}.zip
# Generate a full archive from git tag, with tests
Source2:    makesrc.sh

BuildArch:      noarch

%if %{with tests}
BuildRequires:  php(language) >= 5.6.1
BuildRequires:  php-composer(fedora/autoloader)
BuildRequires:  php-fedora-autoloader-devel
BuildRequires:  %{_bindir}/phpunit9
BuildRequires:  %{_bindir}/phpab
# Optional at runtime, to avoid too muck skipped tests
BuildRequires:  php-bcmath
BuildRequires:  php-gmp
%endif

Requires:   php(language) >= 5.6.1
Requires:   php-bcmath
Requires:   php-gmp
Requires:   php-openssl
Requires:   php-xml
# Autoloader
Requires:   php-composer(fedora/autoloader)

Provides:   php-composer(%{composer_vendor}/%{composer_project}) = %{version}


%description
MIT-licensed pure-PHP implementations of an arbitrary-precision integer 
arithmetic library, fully PKCS#1 (v2.1) compliant RSA, DES, 3DES, RC4, 
Rijndael, AES, Blowfish, Twofish, SSH-1, SSH-2, SFTP, and X.509


%prep
%autosetup -p1


%build
phpab \
	--template fedora \
	--output autoload.php \
	--basedir phpseclib/ \
	./composer.json
cat autoload.php


%install
mkdir -p %{buildroot}%{_datadir}/php
cp -a %{composer_project} %{buildroot}%{_datadir}/php/%{composer_project}%{vmajor}

cp autoload.php %{buildroot}%{_datadir}/php/%{composer_project}%{vmajor}/autoload.php


%if %{with tests}
%check
mkdir vendor
cat << 'EOF' | tee vendor/autoload.php
<?php
require "%{buildroot}%{_datadir}/php/%{composer_project}%{vmajor}/autoload.php";
\Fedora\Autoloader\Autoload::addPsr4('phpseclib3\\Tests\\', dirname(__DIR__) . "/tests");
date_default_timezone_set('UTC');
EOF

# avoid already defined class
sed -e 's/CreateKeyTest/RSACreateKeyTest/' -i tests/Unit/Crypt/RSA/CreateKeyTest.php
sed -e 's/CreateKeyTest/DSACreateKeyTest/' -i tests/Unit/Crypt/DSA/CreateKeyTest.php

# Not supported curves ? (need investigations)
rm tests/Unit/Crypt/EC/CurveTest.php

php tests/make_compatible_with_phpunit7.php
php tests/make_compatible_with_phpunit9.php

# from travis/run-phpunit.sh
# testAuthorityInfoAccess fails without internet access
# testCurveExistance as we remove some files
ret=0
for cmd in "php %{phpunit}" php80 php81 php82; do
  if which $cmd; then
    set $cmd
    $1 -d memory_limit=1G ${2:-%{_bindir}/phpunit9} \
       --filter '^((?!(testAuthorityInfoAccess|testCurveExistance|testLoginToInvalidServer)).)*$' \
       --verbose --configuration tests/phpunit.xml || ret=1
  fi
done
exit $ret
%endif


%files
%doc AUTHORS CHANGELOG.md composer.json README.md
%license LICENSE
%{_datadir}/php/%{composer_project}%{vmajor}


%changelog
* Fri Jul 25 2025 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.44-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_43_Mass_Rebuild

* Sun Jun 15 2025 Artur Frenszek-Iwicki <fedora@svgames.pl> - 3.0.44-1
- Update to v3.0.44

* Thu Mar 20 2025 Artur Frenszek-Iwicki <fedora@svgames.pl> - 3.0.43-1
- Update to v3.0.43

* Thu Jan 30 2025 Artur Frenszek-Iwicki <fedora@svgames.pl> - 2.0.48-1
- Update to v2.0.48

* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.44-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.44-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.44-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.44-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.44-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jun 13 2023 Remi Collet <remi@remirepo.net> - 2.0.44-1
- update to 2.0.44

* Tue Jun 13 2023 Remi Collet <remi@remirepo.net> - 2.0.43-1
- update to 2.0.43

* Mon Mar  6 2023 Remi Collet <remi@remirepo.net> - 2.0.42-1
- update to 2.0.42

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.41-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Tue Jan  3 2023 Remi Collet <remi@remirepo.net> - 2.0.41-1
- update to 2.0.41

* Mon Dec 19 2022 Remi Collet <remi@remirepo.net> - 2.0.40-1
- update to 2.0.40

* Mon Oct 24 2022 Remi Collet <remi@remirepo.net> - 2.0.39-1
- update to 2.0.39

* Mon Sep 12 2022 Remi Collet <remi@remirepo.net> - 2.0.38-1
- update to 2.0.38

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.37-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Apr  4 2022 Remi Collet <remi@remirepo.net> - 2.0.37-1
- update to 2.0.37

* Mon Jan 31 2022 Remi Collet <remi@remirepo.net> - 2.0.36-1
- update to 2.0.36

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.35-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Mon Nov 29 2021 Remi Collet <remi@remirepo.net> - 2.0.35-1
- update to 2.0.35

* Wed Oct 27 2021 Remi Collet <remi@remirepo.net> - 2.0.34-1
- update to 2.0.34

* Thu Sep  2 2021 Remi Collet <remi@remirepo.net> - 2.0.33-1
- update to 2.0.33

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.32-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon Jun 14 2021 Remi Collet <remi@remirepo.net> - 2.0.32-1
- update to 2.0.32

* Tue Apr  6 2021 Remi Collet <remi@remirepo.net> - 2.0.31-1
- update to 2.0.31

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.30-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Dec 17 2020 Remi Collet <remi@remirepo.net> - 2.0.30-1
- update to 2.0.30
- switch to phpunit9 on Fedora

* Tue Sep  8 2020 Remi Collet <remi@remirepo.net> - 2.0.29-1
- update to 2.0.29

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.28-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul  8 2020 Remi Collet <remi@remirepo.net> - 2.0.28-1
- update to 2.0.28

* Mon Apr  6 2020 Remi Collet <remi@remirepo.net> - 2.0.27-1
- update to 2.0.27

* Mon Mar 23 2020 Remi Collet <remi@remirepo.net> - 2.0.26-1
- update to 2.0.26

* Tue Feb 25 2020 Remi Collet <remi@remirepo.net> - 2.0.25-1
- update to 2.0.25

* Mon Feb 24 2020 Remi Collet <remi@remirepo.net> - 2.0.24-1
- update to 2.0.24

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.23-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Sep 17 2019 Remi Collet <remi@remirepo.net> - 2.0.23-1
- update to 2.0.23

* Mon Sep 16 2019 Remi Collet <remi@remirepo.net> - 2.0.22-1
- update to 2.0.22

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.21-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Jul 15 2019 Remi Collet <remi@remirepo.net> - 2.0.21-1
- update to 2.0.21

* Tue Jun 25 2019 Remi Collet <remi@remirepo.net> - 2.0.20-1
- update to 2.0.20

* Fri Jun 21 2019 Remi Collet <remi@remirepo.net> - 2.0.19-1
- update to 2.0.19

* Thu Jun 13 2019 Remi Collet <remi@remirepo.net> - 2.0.18-1
- update to 2.0.18

* Mon May 27 2019 Remi Collet <remi@remirepo.net> - 2.0.17-1
- update to 2.0.17

* Mon Mar 11 2019 Remi Collet <remi@remirepo.net> - 2.0.15-1
- update to 2.0.15

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.14-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jan 31 2019 Remi Collet <remi@remirepo.net> - 2.0.14-1
- update to 2.0.14

* Tue Dec 18 2018 Remi Collet <remi@remirepo.net> - 2.0.13-1
- update to 2.0.13

* Mon Nov  5 2018 Remi Collet <remi@remirepo.net> - 2.0.12-1
- update to 2.0.12

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Apr 16 2018 Remi Collet <remi@remirepo.net> - 2.0.11-1
- update to 2.0.11

* Tue Feb 20 2018 Remi Collet <remi@remirepo.net> - 2.0.10-1
- Update to 2.0.10
- use phpunit6 when available
- skip tests with PHPUnit < 4.8.35 (EPEL-6)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Nov 29 2017 Remi Collet <remi@remirepo.net> - 2.0.9-1
- Update to 2.0.9

* Mon Oct 23 2017 Remi Collet <remi@remirepo.net> - 2.0.7-1
- Update to 2.0.7

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jun  5 2017 Remi Collet <remi@remirepo.net> - 2.0.6-1
- Update to 2.0.6

* Mon May  8 2017 Remi Collet <remi@remirepo.net> - 2.0.5-1
- Update to 2.0.5
- switch to fedora/autoloader
- use SCL of PHP when available for test suite
- open https://github.com/phpseclib/phpseclib/issues/1122 - regression with 5.3
- open https://github.com/phpseclib/phpseclib/pull/1121 - fix permission

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Oct  4 2016 Remi Collet <remi@fedoraproject.org> - 2.0.4-1
- update to 2.0.4

* Tue Jun  7 2016 Remi Collet <remi@fedoraproject.org> - 2.0.2-1
- update to 2.0.2

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Jan 19 2016 Remi Collet <remi@fedoraproject.org> - 2.0.1-1
- update to 2.0.1
- sources from git snapshot for tests

* Sun Sep  6 2015 Remi Collet <remi@fedoraproject.org> - 2.0.0-4
- change source0 to commit reference
- add BR for better test coverage
- add needed backport stuff for EL-5 in #remirepo

* Wed Sep 02 2015 François Kooman <fkooman@tuxed.net> - 2.0.0-3
- apply patch for test to avoid loading class that is now autoloaded

* Wed Sep 02 2015 François Kooman <fkooman@tuxed.net> - 2.0.0-2
- add autoload script
- make use of autoload script when running tests during build
- fix double inclusion of directory

* Sat Aug 08 2015 François Kooman <fkooman@tuxed.net> - 2.0.0-1
- initial package
