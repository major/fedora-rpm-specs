# remirepo/fedora spec file for php-google-recaptcha
#
# Copyright (c) 2017-2020 Remi Collet
# License: CC-BY-SA
# http://creativecommons.org/licenses/by-sa/4.0/
#
# Please, preserve the changelog entries
#
%global gh_commit    614f25a9038be4f3f2da7cbfd778dc5b357d2419
%global gh_short     %(c=%{gh_commit}; echo ${c:0:7})
%global gh_owner     google
%global gh_project   recaptcha
%global with_tests   0%{!?_without_tests:1}
%global psr0         ReCaptcha

Name:           php-%{gh_owner}-%{gh_project}
Version:        1.2.4
Release:        6%{?dist}
Summary:        reCAPTCHA PHP client library

License:        BSD
URL:            https://github.com/%{gh_owner}/%{gh_project}
Source0:        %{url}/archive/%{gh_commit}/%{name}-%{version}-%{?gh_short}.tar.gz

BuildArch:      noarch
%if %{with_tests}
BuildRequires:  php(language) >= 5.5
BuildRequires:  php-curl
BuildRequires:  php-date
BuildRequires:  php-json
BuildRequires:  php-pcre
BuildRequires:  php-spl
# For tests, from composer.json "require-dev": {
#        "phpunit/phpunit": "^4.8.36|^5.7.27|^6.59|^7.5.11",
#        "friendsofphp/php-cs-fixer": "^2.2.20|^2.15",
BuildRequires:  phpunit7 >= 7.5.11
%global phpunit %{_bindir}/phpunit7
%endif
# For autoloader
BuildRequires:  php-composer(fedora/autoloader)

# From composer.json, "require": {
#        "php": ">=5.5"
Requires:       php(language) >= 5.5
# From phpcompatinfo report for 1.2.1
Requires:       php-curl
Requires:       php-date
Requires:       php-json
Requires:       php-pcre
Requires:       php-spl
# For generated autoloader
Requires:       php-composer(fedora/autoloader)

# Composer
Provides:       php-composer(%{gh_owner}/%{gh_project}) = %{version}


%description
reCAPTCHA PHP client library.

reCAPTCHA is a free CAPTCHA service that protect websites from spam and abuse.
This is Google authored code that provides plugins for third-party integration
with reCAPTCHA.

See https://www.google.com/recaptcha/

Autoloader: %{_datadir}/php/%{psr0}/autoload.php


%prep
%setup -q -n %{gh_project}-%{gh_commit}
rm src/autoload.php


%build
: Create autoloader
cat <<'AUTOLOAD' | tee src/%{psr0}/autoload.php
<?php
/* Autoloader for %{name} and its dependencies */
require_once '%{_datadir}/php/Fedora/Autoloader/autoload.php';

\Fedora\Autoloader\Autoload::addPsr4('%{psr0}\\', __DIR__);
AUTOLOAD


%install
: Library
mkdir -p           %{buildroot}%{_datadir}/php
cp -pr src/%{psr0} %{buildroot}%{_datadir}/php/%{psr0}


%check
%if %{with_tests}
BOOTSTRAP=%{buildroot}%{_datadir}/php/%{psr0}/autoload.php
ret=0

for cmdarg in "php %phpunit" php72 php73 php74; do
  if which $cmdarg; then
    set $cmdarg
    $1 ${2:-%{_bindir}/phpunit7}  --bootstrap=$BOOTSTRAP --verbose || ret=0
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
%doc *.md
%{_datadir}/php/%{psr0}


%changelog
* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Apr  1 2020 Remi Collet <remi@remirepo.net> - 1.2.4-1
- update to 1.2.4

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Aug 19 2019 Remi Collet <remi@remirepo.net> - 1.2.3-1
- update to 1.2.3

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Jun 19 2019 Remi Collet <remi@remirepo.net> - 1.2.2-1
- update to 1.2.2

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Aug 20 2018 Remi Collet <remi@remirepo.net> - 1.2.1-1
- update to 1.2.1
- use phpunit7
- open https://github.com/google/recaptcha/issues/250 - CHANGELOG

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Mar 10 2017 Remi Collet <remi@remirepo.net> - 1.1.3-1
- Update to 1.1.3
- raise dependency on PHP 5.5

* Sat Jan 21 2017 Remi Collet <remi@remirepo.net> - 1.1.2-1
- initial package

