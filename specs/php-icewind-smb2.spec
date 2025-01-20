# remirepo/fedora spec file for php-icewind-smb2
#
# Copyright (c) 2015-2019 Remi Collet
# License: CC-BY-SA
# http://creativecommons.org/licenses/by-sa/4.0/
#
# Please, preserve the changelog entries
#
# Github information
%global gh_commit    464459aa5d4ab6bd59f13b4455c8fc3558bb6e07
%global gh_short     %(c=%{gh_commit}; echo ${c:0:7})
%global gh_owner     icewind1991
%global gh_project   SMB
# Packagist information
%global pk_vendor    icewind
%global pk_name      smb
# Namespace information
%global ns_vendor    Icewind
%global ns_name      SMB
# API version, for parallel installation
%global major        2
# Test suite requires a Samba server and configuration file
#   yum install samba
#   systemctl start smb
#   systemctl start nmb
#   useradd testsmb
#   install -o testsmb -m 755 -d /home/testsmb/test
#   smbpasswd -a testsmb
#   create php-icewind-smb-config.json using config.json from sources
%global with_tests   0%{?_with_tests:1}

Name:           php-%{pk_vendor}-%{pk_name}%{major}
Version:        2.0.7
Release:        14%{?dist}
Summary:        php wrapper for smbclient and libsmbclient-php

License:        MIT
URL:            https://github.com/%{gh_owner}/%{gh_project}
Source0:        %{url}/archive/%{gh_commit}/%{name}-%{version}-%{gh_short}.tar.gz
%if %{with_tests}
# Can't be provided, contains credential
Source2:        %{name}-config.json
%endif

BuildArch:      noarch
%if %{with_tests}
# For tests
BuildRequires:  php(language) >= 5.4
BuildRequires:  php-composer(%{pk_vendor}/streams) >= 0.2
BuildRequires:  php-date
BuildRequires:  php-mbstring
BuildRequires:  php-pcre
BuildRequires:  php-posix
# From composer.json, "require-dev": {
#        "phpunit/phpunit": "^4.8"
BuildRequires:  php-composer(phpunit/phpunit) >= 4.8
BuildRequires:  php-composer(theseer/autoload)
# Autoloader
BuildRequires:  php-composer(fedora/autoloader)
%endif

# From composer.json, "require": {
#        "php": ">=5.4"
#        "icewind/streams": ">=0.2.0"
Requires:       php(language) >= 5.4
Requires:       php-composer(%{pk_vendor}/streams) >= 0.2
# From phpcompatinfo report for version 2.0.2
Requires:       %{_bindir}/smbclient
Requires:       php-date
Requires:       php-mbstring
Requires:       php-pcre
Requires:       php-posix
# Autoloader
Requires:       php-composer(fedora/autoloader)
%if 0%{?fedora} > 21
Recommends:     php-smbclient
%endif

Provides:       php-composer(%{pk_vendor}/%{pk_name}) = %{version}


%description
PHP wrapper for smbclient and libsmbclient-php

* Reuses a single smbclient instance for multiple requests
* Doesn't leak the password to the process list
* Simple 1-on-1 mapping of SMB commands
* A stream-based api to remove the need for temporary files
* Support for using libsmbclient directly trough libsmbclient-php

Autoloader: %{_datadir}/php/%{ns_vendor}/%{ns_name}%{major}/autoload.php


%prep
%setup -q -n %{gh_project}-%{gh_commit}

cat << 'EOF' | tee src/autoload.php
<?php
/* Autoloader for icewind/smb and its dependencies */

require_once '%{_datadir}/php/Fedora/Autoloader/autoload.php';

\Fedora\Autoloader\Autoload::addPsr4('Icewind\\SMB\\', __DIR__);
\Fedora\Autoloader\Dependencies::required([
    '%{_datadir}/php/Icewind/Streams/autoload.php',
]);
EOF


%build
# Empty build section, most likely nothing required.


%install
mkdir -p   %{buildroot}%{_datadir}/php/%{ns_vendor}
cp -pr src %{buildroot}%{_datadir}/php/%{ns_vendor}/%{ns_name}%{major}


%if %{with_tests}
%check
mkdir vendor
cat << 'EOF' | tee vendor/autoload.php
<?php
require_once '%{buildroot}%{_datadir}/php/%{ns_vendor}/%{ns_name}%{major}/autoload.php';
\Fedora\Autoloader\Autoload::addPsr4('Icewind\\SMB\\Test\\', dirname(__DIR__) . '/tests');
EOF

cd tests
: Client configuration
cp %{SOURCE2} config.json

: Run the test suite
ret=0
for cmd in php php70 php71 php72; do
  if which $cmd; then
    $cmd %{_bindir}/phpunit || ret=1
  fi
done
exit $ret
%endif


%files
%{!?_licensedir:%global license %%doc}
%license LICENSE.txt
%doc composer.json
%doc *.md example.php
%{_datadir}/php/%{ns_vendor}/%{ns_name}%{major}


%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.7-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.7-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.7-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.7-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.7-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.7-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.7-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.7-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.7-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.7-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Mar  6 2019 Remi Collet <remi@remirepo.net> - 2.0.7-1
- update to 2.0.7

* Thu Feb  7 2019 Remi Collet <remi@remirepo.net> - 2.0.6-1
- update to 2.0.6

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Apr 17 2018 Remi Collet <remi@remirepo.net> - 2.0.5-1
- update to 2.0.5

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Jan 22 2018 Remi Collet <remi@remirepo.net> - 2.0.4-1
- Update to 2.0.4

* Wed Nov 15 2017 Remi Collet <remi@remirepo.net> - 2.0.3-1
- Update to 2.0.3

* Wed Nov  1 2017 Remi Collet <remi@remirepo.net> - 2.0.2-1
- rename to php-icewind-smb2
- update to 2.0.2

* Thu Dec  8 2016 Remi Collet <remi@fedoraproject.org> - 1.1.2-1
- update to 1.1.2
- raise dependency on PHP 5.4
- add dependency on smbclient command
- switch to fedora/autoloader

* Tue Jun 14 2016 Remi Collet <remi@fedoraproject.org> - 1.1.1-1
- update to 1.1.1

* Fri Jun  3 2016 Remi Collet <remi@fedoraproject.org> - 1.1.0-1
- update to 1.1.0

* Thu Mar 17 2016 Remi Collet <remi@fedoraproject.org> - 1.0.8-1
- update to 1.0.8

* Thu Mar 17 2016 Remi Collet <remi@fedoraproject.org> - 1.0.7-1
- update to 1.0.7
- lower dependency on icewind/streams >= 0.2

* Thu Mar 17 2016 Remi Collet <remi@fedoraproject.org> - 1.0.6-1
- update to 1.0.6
- raise dependency on icewind/streams >= 0.3
- add optional dependency on php-smbclient

* Sun Feb 21 2016 Remi Collet <remi@fedoraproject.org> - 1.0.5-1
- update to 1.0.5

* Sun Sep 20 2015 Remi Collet <remi@fedoraproject.org> - 1.0.4-2
- don't own /usr/share/php/Icewind (review #1259172)

* Wed Sep  2 2015 Remi Collet <remi@fedoraproject.org> - 1.0.4-1
- initial package, version 1.0.4
