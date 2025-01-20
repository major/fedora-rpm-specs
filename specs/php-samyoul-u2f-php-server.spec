# remirepo/fedora spec file for php-samyoul-u2f-php-server
#
# Copyright (c) 2018 Remi Collet
# License: CC-BY-SA
# http://creativecommons.org/licenses/by-sa/4.0/
#
# Please, preserve the changelog entries
#

%global with_tests   0%{!?_without_tests:1}
# Github
%global gh_commit    0625202c79d570e58525ed6c4ae38500ea3f0883
%global gh_short     %(c=%{gh_commit}; echo ${c:0:7})
%global gh_owner     Samyoul
%global gh_project   U2F-php-server
# Packagist
%global pk_vendor    samyoul
%global pk_project   u2f-php-server
# Namespace
%global ns_vendor    Samyoul
%global ns_project   U2F
%global ns_library   U2FServer

Name:           php-%{pk_vendor}-%{pk_project}
Version:        1.1.4
Release:        16%{?gh_date?%{gh_date}git%{gh_short}}%{?dist}
Summary:        Server side handling class for FIDO U2F registration and authentication

# Automatically converted from old format: BSD - review is highly recommended.
License:        LicenseRef-Callaway-BSD
URL:            https://github.com/%{gh_owner}/%{gh_project}
Source0:        https://github.com/%{gh_owner}/%{gh_project}/archive/%{gh_commit}/%{name}-%{version}-%{?gh_short}.tar.gz

BuildArch:      noarch
%if %{with_tests}
BuildRequires:  php-cli
BuildRequires:  php-hash
BuildRequires:  php-json
BuildRequires:  php-openssl
BuildRequires:  php-spl
# For autoloader
BuildRequires:  php-composer(fedora/autoloader)
%endif

# From composer.json, "require": {
#        "ext-openssl":"*"
Requires:       php-openssl
# From phpcompatinfo report for 1.1.3
Requires:       php-hash
Requires:       php-json
Requires:       php-spl
# For generated autoloader
Requires:       php-composer(fedora/autoloader)

# Composer
Provides:       php-composer(%{pk_vendor}/%{pk_project}) = %{version}


%description
Server-side handling of FIDO U2F registration and authentication for PHP.

Securing your online accounts and doing your bit to protect your data is
extremely important and increasingly more so as hackers get more sophisticated.
FIDO's U2F enables you to add a simple unobtrusive method of 2nd factor
authentication, allowing users of your service and/or application to link
a hardware key to their account.

Autoloader: %{_datadir}/php/%{ns_vendor}/%{ns_project}/%{ns_library}/autoload.php


%prep
%setup -q -n %{gh_project}-%{gh_commit}

mv LICENCE.md LICENCE

: Create autoloader
cat <<'AUTOLOAD' | tee src/autoload.php
<?php
/* Autoloader for %{name} and its dependencies */
require_once '%{_datadir}/php/Fedora/Autoloader/autoload.php';

\Fedora\Autoloader\Autoload::addPsr4('%{ns_vendor}\\%{ns_project}\\%{ns_library}\\', __DIR__);
AUTOLOAD


%build
: Nothing to build


%install
: Library
mkdir -p      %{buildroot}%{_datadir}/php/%{ns_vendor}/%{ns_project}
cp -pr src    %{buildroot}%{_datadir}/php/%{ns_vendor}/%{ns_project}/%{ns_library}


%check
%if %{with_tests}
# No upstream test suite, only check our autoloader
php -r '
  require "%{buildroot}%{_datadir}/php/%{ns_vendor}/%{ns_project}/%{ns_library}/autoload.php";
  exit (%{ns_vendor}\%{ns_project}\%{ns_library}\U2FServer::checkOpenSSLVersion() ? 0 : 1);
'
%endif


%files
%{!?_licensedir:%global license %%doc}
%license LICENCE
%doc composer.json
%doc *.md
%dir %{_datadir}/php/%{ns_vendor}
%dir %{_datadir}/php/%{ns_vendor}/%{ns_project}
     %{_datadir}/php/%{ns_vendor}/%{ns_project}/%{ns_library}


%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.4-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Sep 04 2024 Miroslav Suchý <msuchy@redhat.com> - 1.1.4-15
- convert license to SPDX

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.4-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.4-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.4-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.4-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.4-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.4-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.4-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.4-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Oct 27 2018 Remi Collet <remi@remirepo.net> - 1.1.4-1
- update to 1.1.4

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Mar  7 2018 Remi Collet <remi@remirepo.net> - 1.1.3-1
- initial package
