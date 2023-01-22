# remirepo/fedora spec file for php-pragmarx-google2fa-qrcode
#
# Copyright (c) 2019 Remi Collet
# License: CC-BY-SA
# http://creativecommons.org/licenses/by-sa/4.0/
#
# Please, preserve the changelog entries
#

%global with_tests   0%{!?_without_tests:1}
# Github
%global gh_commit    fd5ff0531a48b193a659309cc5fb882c14dbd03f
%global gh_short     %(c=%{gh_commit}; echo ${c:0:7})
%global gh_owner     antonioribeiro
%global gh_project   google2fa-qrcode
# Packagist
%global pk_vendor    pragmarx
%global pk_project   %{gh_project}
# Namespace
%global ns_vendor    PragmaRX
%global ns_project   Google2FAQRCode
%global major        %nil

Name:           php-%{pk_vendor}-%{pk_project}%{major}
Version:        1.0.3
Release:        8%{?gh_date?%{gh_date}git%{gh_short}}%{?dist}
Summary:        QR Code package for Google2FA

License:        MIT
URL:            https://github.com/%{gh_owner}/%{gh_project}
Source0:        https://github.com/%{gh_owner}/%{gh_project}/archive/%{gh_commit}/%{name}-%{version}-%{?gh_short}.tar.gz

BuildArch:      noarch
%if %{with_tests}
BuildRequires:  php(language) >= 5.4
%if 0%{?fedora} >= 27 || 0%{?rhel} >= 8
BuildRequires: (php-composer(pragmarx/google2fa)                   >= 5.0   with php-composer(pragmarx/google2fa)                   < 6)
BuildRequires: (php-composer(bacon/bacon-qr-code)                  >= 1.0   with php-composer(bacon/bacon-qr-code)                  < 3)
%else
BuildRequires:  php-pragmarx-google2fa5
BuildRequires:  php-bacon-qr-code
%endif
# For tests, from composer.json "require-dev": {
#        "phpunit/phpunit": "~4|~5|~6|~7",
#        "khanamiryan/qrcode-detector-decoder": "^1.0"
BuildRequires:  php-composer(phpunit/phpunit)
%global phpunit %{_bindir}/phpunit
%if 0%{?fedora} >= 27 || 0%{?rhel} >= 8
BuildRequires: (php-composer(khanamiryan/qrcode-detector-decoder)  >= 1.0   with php-composer(khanamiryan/qrcode-detector-decoder)  < 2)
%else
BuildRequires:  php-khanamiryan-qrcode-detector-decoder
%endif
BuildRequires:  php-date
# For autoloader
BuildRequires:  php-composer(fedora/autoloader)
# Optional dependency of khanamiryan/qrcode-detector-decoder
BuildRequires:  php-imagick
%endif

# From composer.json, "require": {
#        "php": ">=5.4",
#        "pragmarx/google2fa": ">=4.0",
#        "bacon/bacon-qr-code": "~1.0|~2.0"
Requires:       php(language) >= 5.4
%if 0%{?fedora} >= 27 || 0%{?rhel} >= 8
Requires:       (php-composer(pragmarx/google2fa)    >= 5.0   with php-composer(pragmarx/google2fa)   < 6)
Requires:       (php-composer(bacon/bacon-qr-code)   >= 1.0   with php-composer(bacon/bacon-qr-code)  < 3)
%else
Requires:       php-pragmarx-google2fa5
Requires:       php-bacon-qr-code
%endif
# From phpcompatinfo report for 1.0.3
# only Core and standard
# From composer.json, "suggest": {
#      "bacon/bacon-qr-code": "Required to generate inline QR Codes."
%if 0%{?fedora} >= 21 || 0%{?rhel} >= 8
Recommends:     php-composer(bacon/bacon-qr-code)
%endif
# For generated autoloader
Requires:       php-composer(fedora/autoloader)

# Composer
Provides:       php-composer(%{pk_vendor}/%{pk_project}) = %{version}


%description
This is package is Goole2FA integrated with a QRCode generator,
providing an easy way to plot QRCode for your two factor authentication. 

Autoloader: %{_datadir}/php/%{ns_vendor}/%{ns_project}%{major}/autoload.php


%prep
%setup -q -n %{gh_project}-%{gh_commit}

: Create autoloader
cat <<'AUTOLOAD' | tee src/autoload.php
<?php
/* Autoloader for %{name} and its dependencies */
require_once '%{_datadir}/php/Fedora/Autoloader/autoload.php';

\Fedora\Autoloader\Autoload::addPsr4('%{ns_vendor}\\%{ns_project}\\', __DIR__);
\Fedora\Autoloader\Dependencies::required([
    '%{_datadir}/php/%{ns_vendor}/Google2FA5/autoload.php',
    [
        '%{_datadir}/php/BaconQrCode2/autoload.php',
        '%{_datadir}/php/BaconQrCode/autoload.php',
    ],
]);
AUTOLOAD


%build
: Nothing to build


%install
: Library
mkdir -p      %{buildroot}%{_datadir}/php/%{ns_vendor}
cp -pr src    %{buildroot}%{_datadir}/php/%{ns_vendor}/%{ns_project}%{major}


%check
%if %{with_tests}
mkdir vendor
cat << 'EOF' | tee vendor/autoload.php
<?php
require '%{buildroot}%{_datadir}/php/%{ns_vendor}/%{ns_project}%{major}/autoload.php';
\Fedora\Autoloader\Autoload::addPsr4('%{ns_vendor}\\%{ns_project}\\Tests\\', dirname(__DIR__).'/tests');
require '%{_datadir}/php/Zxing/autoload.php';
EOF

ret=0
for cmd in php php71 php72 php73 php74; do
   if which $cmd; then
      $cmd %{phpunit} --no-coverage --verbose || ret=1
   fi
done
exit $ret
%else
: Test suite disabled
%endif


%files
%license LICENSE.md
%doc composer.json
%doc README.md CHANGELOG.md
%dir %{_datadir}/php/%{ns_vendor}
     %{_datadir}/php/%{ns_vendor}/%{ns_project}%{major}


%changelog
* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Sep 11 2019 Remi Collet <remi@remirepo.net> - 1.0.3-1
- initial package
