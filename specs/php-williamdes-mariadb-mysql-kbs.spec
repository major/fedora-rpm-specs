# remirepo/fedora spec file for php-williamdes-mariadb-mysql-kbs
#
# Copyright (c) 2019-2024 Remi Collet
# License: CC-BY-SA
# http://creativecommons.org/licenses/by-sa/4.0/
#
# Please, preserve the changelog entries
#

%bcond_without       tests

# Github
%global gh_commit    07106dab252127c329cc206cd79cf2f51f989e5e
%global gh_short     %(c=%{gh_commit}; echo ${c:0:7})
%global gh_owner     williamdes
%global gh_project   mariadb-mysql-kbs
# Packagist
%global pk_vendor    %{gh_owner}
%global pk_project   %{gh_project}
# Namespace
%global ns_vendor    Williamdes
%global ns_project   MariaDBMySQLKBS
%global major        %nil

Name:           php-%{pk_vendor}-%{pk_project}%{major}
Version:        1.3.0
Release:        3%{?gh_date?%{gh_date}git%{gh_short}}%{?dist}
Summary:        An index of the MariaDB and MySQL Knowledge bases

License:        MPL-2.0
URL:            https://github.com/%{gh_owner}/%{gh_project}
# pull from github to retrieve full data
Source0:        %{name}-%{version}-%{?gh_short}.tgz
Source1:        makesrc.sh

Patch0:         %{name}-layout.patch

BuildArch:      noarch
%if %{with tests}
BuildRequires:  php(language) >= 7.2
BuildRequires:  php-json
BuildRequires:  php-pcre
# For tests, from composer.json "require-dev": {
#        "phpunit/phpunit": "^8 || ^9 || ^10 || ^11"",
#        "phpstan/phpstan": "^1.2",
#        "wdes/coding-standard": "^3.2.1",
#        "swaggest/json-schema": "^0.12.29"
BuildRequires:  phpunit10
%global phpunit %{_bindir}/phpunit10
BuildRequires: (php-composer(swaggest/json-schema)    >= 0.12.29 with php-composer(swaggest/json-schema)    < 1)
# For autoloader
BuildRequires:  php-composer(fedora/autoloader)
%endif

# From composer.json, "require": {
#        "php": "^7.2 || ^8.0"
Requires:       php(language) >= 7.2
# From phpcompatinfo report for 1.2.7
Requires:       php-json
Requires:       php-pcre
# For generated autoloader
Requires:       php-composer(fedora/autoloader)

# Composer
Provides:       php-composer(%{pk_vendor}/%{pk_project}) = %{version}


%description
An index of the MariaDB and MySQL Knowledge bases.


Autoloader: %{_datadir}/php/%{ns_vendor}/%{ns_project}%{major}/autoload.php


%prep
%setup -q -n %{gh_project}-%{gh_commit}
%patch -P0 -p1 -b .rpm
find src -name \*.rpm -delete

: Create autoloader
cat <<'AUTOLOAD' | tee src/autoload.php
<?php
/* Autoloader for %{name} and its dependencies */
require_once '%{_datadir}/php/Fedora/Autoloader/autoload.php';

\Fedora\Autoloader\Autoload::addPsr4('%{ns_vendor}\\%{ns_project}\\', __DIR__);
AUTOLOAD


%build
: Generate merged data
%{_bindir}/php -d auto_prepend_file=src/autoload.php src/merge.php


%install
: Library
mkdir -p       %{buildroot}%{_datadir}/php/%{ns_vendor}
cp -pr src     %{buildroot}%{_datadir}/php/%{ns_vendor}/%{ns_project}%{major}

: Data
mkdir -p       %{buildroot}%{_datadir}/%{name}
# only dist is used at runtime
cp -pr dist    %{buildroot}%{_datadir}/%{name}/dist
cp -pr data    %{buildroot}%{_datadir}/%{name}/data
cp -pr schemas %{buildroot}%{_datadir}/%{name}/schemas


%check
%if %{with tests}
mkdir vendor
cat << 'EOF' | tee vendor/autoload.php
<?php
require '%{buildroot}%{_datadir}/php/%{ns_vendor}/%{ns_project}%{major}/autoload.php';
\Fedora\Autoloader\Autoload::addPsr4('%{ns_vendor}\\%{ns_project}\\Test\\', dirname(__DIR__).'/test');
require '%{_datadir}/php/Swaggest/JsonSchema/autoload.php';
EOF

export RPM_BUILDROOT=%{buildroot}

ret=0
for cmdarg in "php %{phpunit}" php81 php82 php83 php84; do
   if which $cmdarg; then
      set $cmdarg
      $1 ${2:-%{_bindir}/phpunit10} --no-coverage || ret=1
   fi
done
exit $ret
%else
: Test suite disabled
%endif


%files
%license LICENSE
%doc composer.json
%doc *.md
%dir     %{_datadir}/php/%{ns_vendor}/
         %{_datadir}/php/%{ns_vendor}/%{ns_project}%{major}
%exclude %{_datadir}/php/%{ns_vendor}/%{ns_project}%{major}/merge.php
%exclude %{_datadir}/php/%{ns_vendor}/%{ns_project}%{major}/rust
%dir     %{_datadir}/%{name}/
         %{_datadir}/%{name}/dist
%doc     %{_datadir}/%{name}/data
%doc     %{_datadir}/%{name}/schemas


%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Mon Jul  8 2024 Remi Collet <remi@remirepo.net> - 1.3.0-1
- update to 1.3.0

* Sat Apr  13 2024 Miroslav Suchý <msuchy@redhat.com> - 1.2.14-6
- convert license to SPDX

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.14-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.14-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.14-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.14-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Dec  7 2022 Remi Collet <remi@remirepo.net> - 1.2.14-1
- update to 1.2.14

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.13-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.13-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Mon Dec 20 2021 Remi Collet <remi@remirepo.net> - 1.2.13-1
- update to 1.2.13

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.12-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.12-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jan  4 2021 Remi Collet <remi@remirepo.net> - 1.2.12-1
- update to 1.2.12

* Mon Sep 14 2020 Remi Collet <remi@remirepo.net> - 1.2.11-1
- update to 1.2.11
- switch to phpunit9

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Feb 27 2020 Remi Collet <remi@remirepo.net> - 1.2.10-1
- update to 1.2.10
- sources from git snapshot

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Jan 27 2020 Remi Collet <remi@remirepo.net> - 1.2.9-1
- update to 1.2.9
- switch to phpunit8

* Tue Nov 12 2019 Remi Collet <remi@remirepo.net> - 1.2.8-1
- update to 1.2.8

* Thu Sep 12 2019 Remi Collet <remi@remirepo.net> - 1.2.7-1
- initial package
