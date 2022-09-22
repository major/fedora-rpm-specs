# remirepo/fedora spec file for php-endroid-qrcode
#
# Copyright (c) 2017-2018 Remi Collet
# License: CC-BY-SA
# http://creativecommons.org/licenses/by-sa/4.0/
#
# Please, preserve the changelog entries
#
%global gh_commit    c9644bec2a9cc9318e98d1437de3c628dcd1ef93
%global gh_short     %(c=%{gh_commit}; echo ${c:0:7})
%global gh_owner     endroid
%global gh_project   QrCode

%global pk_vendor    %{gh_owner}
%global pk_project   qrcode

%global ns_vendor    Endroid
%global ns_project   QrCode
%global php_home     %{_datadir}/php
%global with_tests   0%{!?_without_tests:1}

Name:           php-%{pk_vendor}-%{pk_project}
Version:        1.9.3
Release:        13%{?dist}
Summary:        Endroid QR Code

License:        MIT
URL:            https://github.com/%{gh_owner}/%{gh_project}
Source0:        https://github.com/%{gh_owner}/%{gh_project}/archive/%{gh_commit}/%{name}-%{version}-%{gh_short}.tar.gz

# Assets relocation
Patch0:         %{name}-rpm.patch
Patch1:         %{name}-el6-rpm.patch

BuildArch:      noarch
%if %{with_tests}
# For tests
BuildRequires:  php(language) >= 5.4
BuildRequires:  php-gd
BuildRequires:  php-composer(symfony/options-resolver) <  4
BuildRequires:  php-composer(symfony/options-resolver) >= 2.3
BuildRequires:  php-reflection
BuildRequires:  php-pcre
BuildRequires:  php-spl
# From composer.json, "require-dev": {
#        "symfony/browser-kit": "^2.3|^3.0",
#        "symfony/framework-bundle": "^2.3|^3.0",
#        "symfony/http-kernel": "^2.3|^3.0",
#        "sensio/framework-extra-bundle": "^3.0",
#        "phpunit/phpunit": "^4.0|^5.0"
BuildRequires:  php-composer(phpunit/phpunit)
# Required by autoloader
BuildRequires:  php-composer(fedora/autoloader)
%endif
# Unbundled assets
%if 0%{?rhel} != 6
BuildRequires:  open-sans-fonts
%endif

# From composer.json, "require": {
#        "php": ">=5.4",
#        "ext-gd": "*",
#        "symfony/options-resolver": "^2.3|^3.0"
Requires:       php(language) >= 5.4
Requires:       php-gd
Requires:       php-composer(symfony/options-resolver) <  4
Requires:       php-composer(symfony/options-resolver) >= 2.3
# From phpcompatinfo report for version 1.9.3
Requires:       php-reflection
Requires:       php-pcre
Requires:       php-spl
# Required by autoloader
Requires:       php-composer(fedora/autoloader)
# Unbundled assets
%if 0%{?rhel} != 6
Requires:       open-sans-fonts
%else
Provides:       bundled(open-sans-fonts)
%endif

Provides:       php-composer(%{pk_vendor}/%{pk_project}) = %{version}


%description
This library based on QRcode Perl CGI & PHP scripts by Y. Swetake
helps you generate images containing a QR code.

Autoloader: %{php_home}/%{ns_vendor}/%{ns_project}/autoload.php


%prep
%setup -q -n %{gh_project}-%{gh_commit}

%if 0%{?rhel} != 6
: Drop bundled font
rm -r assets/font

: Relocate assets
%patch0 -p0
%else
%patch1 -p0
%endif
sed -e 's:@ASSETS@:%{_datadir}/%{name}/assets:' -i src/QrCode.php

: Fix wrong-file-end-of-line-encoding
sed -e 's/\r//' -i *.md

: Fix perms
find . -type f -exec chmod -x {} \;

: Generate autoloader
cat << 'EOF' | tee src/autoload.php
<?php
/* Autoloader for %{name} and its dependencies */
require_once '%{php_home}/Fedora/Autoloader/autoload.php';

\Fedora\Autoloader\Autoload::addPsr4('%{ns_vendor}\\%{ns_project}\\', __DIR__);
if (file_exists('%{php_home}/Symfony3/Component/OptionsResolver/autoload.php')) {
    \Fedora\Autoloader\Autoload::addPsr4('Symfony\\Component\\', '%{php_home}/Symfony3/Component');
} else {
    \Fedora\Autoloader\Autoload::addPsr4('Symfony\\Component\\', '%{php_home}/Symfony/Component');
}
EOF


%build
# Empty build section, most likely nothing required.


%install
: Library
mkdir -p      %{buildroot}%{php_home}/%{ns_vendor}
cp -pr src    %{buildroot}%{php_home}/%{ns_vendor}/%{ns_project}

: Assets
mkdir -p      %{buildroot}%{_datadir}/%{name}
cp -pr assets %{buildroot}%{_datadir}/%{name}/assets


%check
%if %{with_tests}
mkdir vendor
cat << 'EOF' | tee vendor/autoload.php
<?php
require '%{buildroot}%{php_home}/%{ns_vendor}/%{ns_project}/autoload.php';
\Fedora\Autoloader\Autoload::addPsr4('%{ns_vendor}\\%{ns_project}\\Tests\\', __DIR__ . '/../tests');
EOF

export RPM_ASSETS_BUILDROOT=%{buildroot}

: Minimal test suite without Symfony integration
ret=0
for cmd in php php56 php70 php71 php72; do
  if which $cmd; then
    $cmd %{_bindir}/phpunit --bootstrap vendor/autoload.php --verbose tests/QrCodeTest.php || ret=1
  fi
done
exit $ret
%else
: Test suite disabled
%endif


%files
%{!?_licensedir:%global license %%doc}
%license LICENSE
%doc composer.json
%doc README.md
%{_datadir}/%{name}
%dir %{php_home}/%{ns_vendor}
     %{php_home}/%{ns_vendor}/%{ns_project}

%changelog
* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.3-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.3-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.3-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.3-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.3-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Jan 15 2018 Remi Collet <remi@remirepo.net> - 1.9.3-2
- simpler autoloader for Symfony

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Jun 27 2017 Remi Collet <remi@remirepo.net> - 1.9.3-1
- initial package, version 1.9.3
