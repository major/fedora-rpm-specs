# remirepo/fedora spec file for php-swaggest-json-diff
#
# Copyright (c) 2019-2024 Remi Collet
# License: CC-BY-SA-4.0
# http://creativecommons.org/licenses/by-sa/4.0/
#
# Please, preserve the changelog entries
#

%bcond_without       tests

# Github
%global gh_commit    c55d38a3cb372753b5d5ee4c9b7d8470e486e6a5
%global gh_short     %(c=%{gh_commit}; echo ${c:0:7})
%global gh_owner     swaggest
%global gh_project   json-diff
# Packagist
%global pk_vendor    %{gh_owner}
%global pk_project   %{gh_project}
# Namespace
%global ns_vendor    Swaggest
%global ns_project   JsonDiff
%global major        %nil

Name:           php-%{pk_vendor}-%{pk_project}%{major}
Version:        3.11.0
Release:        3%{?gh_date?%{gh_date}git%{gh_short}}%{?dist}
Summary:        JSON diff/rearrange/patch/pointer library for PHP

License:        MIT
URL:            https://github.com/%{gh_owner}/%{gh_project}
Source0:        %{name}-%{version}-%{?gh_short}.tgz
Source1:        makesrc.sh

BuildArch:      noarch
%if %{with tests}
BuildRequires:  php-json
# For tests, from composer.json "require-dev": {
#    "phpunit/phpunit": "4.8.37"
BuildRequires:  phpunit9
%global phpunit %{_bindir}/phpunit9
BuildRequires:  php-filter
BuildRequires:  php-pcre
# For autoloader
BuildRequires:  php-fedora-autoloader-devel
%endif

# From composer.json, "require": {
#    "ext-json": "*"
Requires:       php-json
# From phpcompatinfo report for 3.7.0
Requires:       php-filter
Requires:       php-pcre
# For generated autoloader
Requires:       php-composer(fedora/autoloader)

# Composer
Provides:       php-composer(%{pk_vendor}/%{pk_project}) = %{version}


%description
A PHP implementation for finding unordered diff between two JSON documents.

Autoloader: %{_datadir}/php/%{ns_vendor}/%{ns_project}%{major}/autoload.php


%prep
%setup -q -n %{gh_project}-%{gh_commit}


%build
: Create autoloader
%{_bindir}/phpab -t fedora -o src/autoload.php src


%install
: Library
mkdir -p      %{buildroot}%{_datadir}/php/%{ns_vendor}
cp -pr src    %{buildroot}%{_datadir}/php/%{ns_vendor}/%{ns_project}%{major}


%check
%if %{with tests}
mkdir vendor
cat << 'EOF' | tee vendor/autoload.php
<?php
require '%{buildroot}%{_datadir}/php/%{ns_vendor}/%{ns_project}%{major}/autoload.php';
\Fedora\Autoloader\Autoload::addPsr4('%{ns_vendor}\\%{ns_project}\\Tests\\', dirname(__DIR__).'/tests');

class PHPUnit_Framework_TestCase extends \PHPUnit\Framework\Testcase {
	function setExpectedException($e, $m) {
		$this->expectException($e);
		$this->expectExceptionMessage($m);
	}
}
EOF

ret=0
for cmd in php php81 php82 php83; do
   if which $cmd; then
      $cmd %{phpunit} --no-coverage || ret=1
   fi
done
exit $ret
%else
: Test suite disabled
%endif


%files
%license LICENSE
%doc composer.json
%doc README.md
%doc CHANGELOG.md
%dir %{_datadir}/php/%{ns_vendor}
     %{_datadir}/php/%{ns_vendor}/%{ns_project}%{major}


%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 3.11.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.11.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jul  3 2024 Remi Collet <remi@remirepo.net> - 3.11.0-1
- update to 3.11.0

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.10.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.10.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Nov 17 2023 Remi Collet <remi@remirepo.net> - 3.10.5-1
- update to 3.10.5

* Fri Oct  6 2023 Remi Collet <remi@remirepo.net> - 3.10.4-4
- switch to phpunit9

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.10.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.10.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Nov 10 2022 Remi Collet <remi@remirepo.net> - 3.10.4-1
- update to 3.10.4

* Tue Nov  8 2022 Remi Collet <remi@remirepo.net> - 3.10.3-1
- update to 3.10.3

* Tue Oct 25 2022 Remi Collet <remi@remirepo.net> - 3.10.1-1
- update to 3.10.1

* Fri Oct 21 2022 Remi Collet <remi@remirepo.net> - 3.10.0-1
- update to 3.10.0

* Mon Sep 12 2022 Remi Collet <remi@remirepo.net> - 3.9.0-1
- update to 3.9.0

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.8.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.8.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Mon Sep 27 2021 Remi Collet <remi@remirepo.net> - 3.8.3-1
- update to 3.8.3

* Wed Sep 22 2021 Remi Collet <remi@remirepo.net> - 3.8.2-1
- update to 3.8.2

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.8.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.8.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Sep 28 2020 Remi Collet <remi@remirepo.net> - 3.8.1-1
- update to 3.8.1

* Fri Sep 25 2020 Remi Collet <remi@remirepo.net> - 3.8.0-1
- update to 3.8.0

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.7.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed May 27 2020 Remi Collet <remi@remirepo.net> - 3.7.5-1
- update to 3.7.5

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.7.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Jan 27 2020 Remi Collet <remi@remirepo.net> - 3.7.4-1
- update to 3.7.4

* Wed Oct 23 2019 Remi Collet <remi@remirepo.net> - 3.7.2-1
- update to 3.7.2 (no change)

* Thu Sep 26 2019 Remi Collet <remi@remirepo.net> - 3.7.1-1
- update to 3.7.1

* Thu Sep 12 2019 Remi Collet <remi@remirepo.net> - 3.7.0-1
- initial package
