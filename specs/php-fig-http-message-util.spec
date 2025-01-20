# remirepo/fedora spec file for php-fig-http-message-util
#
# Copyright (c) 2016-2020 Remi Collet
# License: CC-BY-SA
# http://creativecommons.org/licenses/by-sa/4.0/
#
# Please, preserve the changelog entries
#

%global gh_commit    9d94dc0154230ac39e5bf89398b324a86f63f765
%global gh_short     %(c=%{gh_commit}; echo ${c:0:7})
%global gh_owner     php-fig
%global gh_project   http-message-util
%global pk_owner     fig
%global pk_project   %{gh_project}

Name:           php-%{pk_owner}-%{pk_project}
Version:        1.1.5
Release:        11%{?dist}
Summary:        PSR Http Message Util

License:        MIT
URL:            https://github.com/%{gh_owner}/%{gh_project}
Source0:        https://github.com/%{gh_owner}/%{gh_project}/archive/%{gh_commit}/%{gh_project}-%{version}-%{gh_short}.tar.gz

BuildArch:      noarch
BuildRequires:  php-cli
%if 0%{?fedora} >= 27 || 0%{?rhel} >= 8
BuildRequires: (php-composer(psr/http-message) >= 1.0 with php-composer(psr/http-message) < 2)
%else
BuildRequires:  php-composer(psr/http-message) <  2
BuildRequires:  php-composer(psr/http-message) >= 1.0
%endif
BuildRequires:  php-composer(fedora/autoloader)

# From composer.json, "require": {
#        "php": "^5.3 || ^7.0 || ^8.0",
Requires:       php(language) > 5.3
# From composer.json, "suggest": {
#        "psr/http-message": "^1.0"
%if 0%{?fedora} >= 27 || 0%{?rhel} >= 8
Recommends:     php-composer(psr/http-message)
%endif
# From phpcompatinfo: none
# Autoloader
Requires:       php-composer(fedora/autoloader)

Provides:       php-composer(%{pk_owner}/%{pk_project}) = %{version}


%description
This library holds utility classes and constants to facilitate common
operations of PSR-7; the primary purpose is to provide constants for
referring to request methods, response status codes and messages, and
potentially common headers.

Autoloader: %{_datadir}/php/Fig/Http/Message/autoload.php


%prep
%setup -q -n %{gh_project}-%{gh_commit}


%build
cat << 'AUTOLOAD' | tee src/autoload.php
<?php
/* Autoloader for %{pk_owner}/%{pk_project} and its dependencies */

require_once '%{_datadir}/php/Fedora/Autoloader/autoload.php';
\Fedora\Autoloader\Autoload::addPsr4('Fig\\Http\\Message\\', __DIR__);
\Fedora\Autoloader\Dependencies::optional(array(
    '%{_datadir}/php/Psr/Http/Message/autoload.php',
));
AUTOLOAD


%install
mkdir -p   %{buildroot}%{_datadir}/php/Fig/Http
cp -pr src %{buildroot}%{_datadir}/php/Fig/Http/Message


%check
php -r '
require "%{buildroot}%{_datadir}/php/Fig/Http/Message/autoload.php";
$ok = interface_exists("Fig\\Http\\Message\\StatusCodeInterface");
echo "Autoload " . ($ok ? "Ok\n" : "fails\n");
exit ($ok ? 0 : 1);
'


%files
%{!?_licensedir:%global license %%doc}
%license LICENSE
%doc *.md
%doc composer.json
%dir %{_datadir}/php/Fig
%dir %{_datadir}/php/Fig/Http
     %{_datadir}/php/Fig/Http/Message


%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.5-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.5-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.5-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.5-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.5-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.5-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Nov 25 2020 Remi Collet <remi@remirepo.net> - 1.1.5-1
- update to 1.1.5 (no change)

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Mar 19 2020 Remi Collet <remi@remirepo.net> - 1.1.4-1
- update to 1.1.4
- psr/http-message is optional
- use range dependencies

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Nov 26 2018 Remi Collet <remi@remirepo.net> - 1.1.3-1
- update to 1.1.3

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Thu Feb  9 2017 Remi Collet <remi@remirepo.net> - 1.1.2-1
- update to 1.1.2

* Tue Feb  7 2017 Remi Collet <remi@remirepo.net> - 1.1.1-1
- update to 1.1.1

* Wed Dec 14 2016 Remi Collet <remi@fedoraproject.org> - 1.1.0-1
- initial package

