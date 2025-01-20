# remirepo/fedora spec file for php-league-flysystem
#
# Copyright (c) 2016-2022 Remi Collet
# License: CC-BY-SA
# http://creativecommons.org/licenses/by-sa/4.0/
#
# Please, preserve the changelog entries
#
# Github
%global gh_commit    3239285c825c152bcc315fe0e87d6b55f5972ed1
%global gh_short     %(c=%{gh_commit}; echo ${c:0:7})
%global gh_owner     thephpleague
%global gh_project   flysystem
# Packagist
%global pk_vendor    league
%global pk_name      flysystem
# PSR-0 namespace
%global ns_vendor    League
%global ns_project   Flysystem

Name:           php-%{pk_vendor}-%{pk_name}
Version:        1.1.10
Release:        7%{?dist}
Summary:        Filesystem abstraction: Many filesystems, one API

License:        MIT
URL:            https://github.com/%{gh_owner}/%{gh_project}
Source0:        %{name}-%{version}-%{gh_short}.tgz
# Create git snapshot as tests are excluded from official tarball
Source1:        makesrc.sh

BuildArch:      noarch
BuildRequires:  php(language) >= 7.2
BuildRequires:  php-fileinfo
BuildRequires: (php-composer(league/mime-type-detection) >= 1.3   with php-composer(league/mime-type-detection) < 2)
BuildRequires:  php-date
BuildRequires:  php-ftp
BuildRequires:  php-hash
BuildRequires:  php-mbstring
BuildRequires:  php-pcre
BuildRequires:  php-spl
# From composer.json, "require-dev": {
#        "phpspec/prophecy": "^1.11.1",
#        "phpunit/phpunit": "^8.5.8"
BuildRequires:  phpunit8 >= 8.5.8
# Autoloader
BuildRequires:  php-fedora-autoloader-devel

# From composer.json, "require": {
#        "php": "^7.2.5 || ^8.0",
#        "ext-fileinfo": "*",
#        "league/mime-type-detection": "^1.3"
Requires:       php(language) >= 7.2.5
Requires:       php-fileinfo
Requires:      (php-composer(league/mime-type-detection) >= 1.3   with php-composer(league/mime-type-detection) < 2)
# From phpcompatifo report for 1.1.3
Requires:       php-date
Requires:       php-ftp
Requires:       php-hash
Requires:       php-mbstring
Requires:       php-pcre
Requires:       php-spl
# Autoloader
Requires:       php-composer(fedora/autoloader)

Provides:       php-composer(%{pk_vendor}/%{pk_name}) = %{version}


%description
Flysystem is a filesystem abstraction which allows you to easily swap out
a local filesystem for a remote one.

Autoloader: %{_datadir}/php/%{ns_vendor}/%{ns_project}/autoload.php


%prep
%setup -q -n %{gh_project}-%{gh_commit}


%build
: Create classmap autoloader
phpab \
  --template fedora \
  --output src/autoload.php \
  src

cat << 'EOF' | tee -a src/autoload.php
\Fedora\Autoloader\Dependencies::required([
    '%{_datadir}/php/%{ns_vendor}/MimeTypeDetection/autoload.php',
]);

EOF

%install
# Restore PSR-0 tree
mkdir -p   %{buildroot}%{_datadir}/php/%{ns_vendor}
cp -pr src %{buildroot}%{_datadir}/php/%{ns_vendor}/%{ns_project}


%check
: Generate a simple autoloader
mkdir vendor
cat << 'EOF' | tee vendor/autoload.php
<?php
// Installed library
require '%{buildroot}%{_datadir}/php/%{ns_vendor}/%{ns_project}/autoload.php';

// Test suite
\Fedora\Autoloader\Autoload::addPsr4('%{ns_vendor}\\%{ns_project}\\Stub\\', dirname(__DIR__).'/stub');
EOF

ret=0
for cmd in php php74 php80 php81 php82; do
  if which $cmd; then
   : Run upstream test suite
   $cmd %{_bindir}/phpunit8 \
     --exclude-group integration \
     --filter '^((?!(testPathinfoHandlesUtf8|testStreamSizeForUrl)).)*$' \
     --no-coverage --verbose || ret=1
  fi
done
exit $ret


%files
%{!?_licensedir:%global license %%doc}
%license LICENSE
%doc *.md
%doc composer.json
%{_datadir}/php/%{ns_vendor}/%{ns_project}


%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.10-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.10-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.10-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.10-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.10-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Oct 14 2022 Remi Collet <remi@remirepo.net> - 1.1.10-1
- update to 1.1.10

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.9-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jan  5 2022 Remi Collet <remi@remirepo.net> - 1.1.9-1
- update to 1.1.9

* Tue Nov 30 2021 Remi Collet <remi@remirepo.net> - 1.1.8-1
- update to 1.1.8

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 25 2021 Remi Collet <remi@remirepo.net> - 1.1.4-1
- update to 1.1.4

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Aug 24 2020 Remi Collet <remi@remirepo.net> - 1.1.3-1
- update to 1.1.3
- raise dependency on PHP 7.2
- add dependency on league/mime-type-detection
- switch to classmap autoloader
- switch to phpunit8

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.66-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Mar 18 2020 Remi Collet <remi@remirepo.net> - 1.0.66-1
- update to 1.0.66

* Mon Mar  9 2020 Remi Collet <remi@remirepo.net> - 1.0.65-1
- update to 1.0.65

* Thu Feb  6 2020 Remi Collet <remi@remirepo.net> - 1.0.64-1
- update to 1.0.64

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.63-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Jan  6 2020 Remi Collet <remi@remirepo.net> - 1.0.63-1
- update to 1.0.63

* Mon Dec  9 2019 Remi Collet <remi@remirepo.net> - 1.0.61-1
- update to 1.0.61

* Thu Oct 17 2019 Remi Collet <remi@remirepo.net> - 1.0.57-1
- update to 1.0.57

* Sun Oct 13 2019 Remi Collet <remi@remirepo.net> - 1.0.56-1
- update to 1.0.56
- drop patch merged upstream

* Fri Oct 11 2019 Remi Collet <remi@remirepo.net> - 1.0.55-2
- add patch for PHP 7.4 from
  https://github.com/thephpleague/flysystem/pull/1081

* Mon Aug 26 2019 Remi Collet <remi@remirepo.net> - 1.0.55-1
- update to 1.0.55

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.53-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Jun 19 2019 Remi Collet <remi@remirepo.net> - 1.0.53-1
- update to 1.0.53

* Tue May 21 2019 Remi Collet <remi@remirepo.net> - 1.0.52-1
- update to 1.0.52

* Mon Apr  1 2019 Remi Collet <remi@remirepo.net> - 1.0.51-1
- update to 1.0.51

* Fri Feb  1 2019 Remi Collet <remi@remirepo.net> - 1.0.50-1
- update to 1.0.50

* Mon Nov 26 2018 Remi Collet <remi@remirepo.net> - 1.0.49-1
- update to 1.0.49

* Tue Oct 16 2018 Remi Collet <remi@remirepo.net> - 1.0.48-1
- update to 1.0.48

* Sat Sep 15 2018 Remi Collet <remi@remirepo.net> - 1.0.47-1
- update to 1.0.47

* Wed Aug 22 2018 Remi Collet <remi@remirepo.net> - 1.0.46-1
- update to 1.0.46

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.45-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon May 14 2018 Remi Collet <remi@remirepo.net> - 1.0.45-1
- update to 1.0.45

* Mon Apr  9 2018 Remi Collet <remi@remirepo.net> - 1.0.44-1
- update to 1.0.44

* Thu Mar  1 2018 Remi Collet <remi@remirepo.net> - 1.0.43-1
- Update to 1.0.43

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.42-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Jan 29 2018 Remi Collet <remi@remirepo.net> - 1.0.42-1
- Update to 1.0.42
- switch to phpunit 6 and phpspec 4

* Mon Aug  7 2017 Remi Collet <remi@remirepo.net> - 1.0.41-1
- Update to 1.0.41

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.40-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Apr 28 2017 Remi Collet <remi@remirepo.net> - 1.0.40-1
- Update to 1.0.40

* Wed Apr 26 2017 Remi Collet <remi@remirepo.net> - 1.0.39-1
- Update to 1.0.39

* Mon Apr 24 2017 Remi Collet <remi@remirepo.net> - 1.0.38-1
- Update to 1.0.38

* Thu Mar 23 2017 Remi Collet <remi@remirepo.net> - 1.0.37-1
- Update to 1.0.37

* Mon Mar 20 2017 Remi Collet <remi@remirepo.net> - 1.0.36-1
- Update to 1.0.36

* Thu Feb  9 2017 Remi Collet <remi@fedoraproject.org> - 1.0.35-1
- update to 1.0.35

* Wed Feb  1 2017 Remi Collet <remi@fedoraproject.org> - 1.0.34-1
- update to 1.0.34

* Mon Jan 23 2017 Remi Collet <remi@fedoraproject.org> - 1.0.33-1
- update to 1.0.33 (windows only)
- switch to fedora/autoloader

* Wed Oct 19 2016 Remi Collet <remi@fedoraproject.org> - 1.0.30-1
- update to 1.0.30
- lower dependency on PHP 5.5.9

* Tue Oct 18 2016 Remi Collet <remi@fedoraproject.org> - 1.0.29-1
- update to 1.0.29
- raise dependency on PHP 5.6

* Fri Oct  7 2016 Remi Collet <remi@fedoraproject.org> - 1.0.28-1
- update to 1.0.28

* Wed Aug 10 2016 Remi Collet <remi@fedoraproject.org> - 1.0.27-1
- update to 1.0.27

* Wed Aug  3 2016 Remi Collet <remi@fedoraproject.org> - 1.0.26-1
- update to 1.0.26

* Mon Jul 18 2016 Remi Collet <remi@fedoraproject.org> - 1.0.25-1
- update to 1.0.25
- disable spec test suite with phpspec 3

* Sat Jun  4 2016 Remi Collet <remi@fedoraproject.org> - 1.0.24-1
- update to 1.0.24

* Thu Apr 28 2016 Remi Collet <remi@fedoraproject.org> - 1.0.22-1
- update to 1.0.22

* Fri Apr 22 2016 Remi Collet <remi@fedoraproject.org> - 1.0.21-1
- update to 1.0.21

* Tue Mar 15 2016 Remi Collet <remi@fedoraproject.org> - 1.0.20-1
- update to 1.0.20

* Tue Mar  8 2016 Remi Collet <remi@fedoraproject.org> - 1.0.18-1
- update to 1.0.18

* Sat Feb 20 2016 Remi Collet <remi@fedoraproject.org> - 1.0.17-1
- update to 1.0.17

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.16-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jan 14 2016 Remi Collet <remi@fedoraproject.org> - 1.0.16-1
- initial package
- open https://github.com/thephpleague/flysystem/pull/592 - PHPUnit
