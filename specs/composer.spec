# remirepo/fedora spec file for composer
#
# SPDX-FileCopyrightText:  Copyright 2015-2025 Remi Collet
# SPDX-License-Identifier: CECILL-2.1
# http://www.cecill.info/licences/Licence_CeCILL_V2-en.txt
#
# Please, preserve the changelog entries
#


%bcond_with          generators

%global gh_commit    ae208dc1e182bd45d99fcecb956501da212454a1
%global gh_short     %(c=%{gh_commit}; echo ${c:0:7})
%global gh_branch    2.0-dev
%global gh_owner     composer
%global gh_project   composer
%global api_version  2.6.0
%global run_version  2.2.2

%global upstream_version 2.8.5
#global upstream_prever  RC1
#global upstream_lower   rc1

%global _phpunit       %{_bindir}/phpunit9
%global bashcompdir    %(pkg-config --variable=completionsdir bash-completion 2>/dev/null)
%global bashcomproot   %(dirname %{bashcompdir} 2>/dev/null)


Name:           composer
Version:        %{upstream_version}%{?upstream_prever:~%{upstream_lower}}
Release:        1%{?dist}
Summary:        Dependency Manager for PHP

# SPDX: composer and all dependencies are MIT
License:        MIT
URL:            https://getcomposer.org/
Source0:        %{gh_project}-%{upstream_version}%{?upstream_prever}-%{gh_short}.tgz
# Profile scripts
Source1:        %{name}-bash-completion
Source3:        %{name}.sh
Source4:        %{name}.csh
# Create a git snapshot with dependencies
Source5:        makesrc.sh

# Use our autoloader, resources path, fix for tests
Patch0:         %{name}-rpm.patch
# Disable XDG support as only partially implemented
Patch1:         %{name}-noxdg.patch

BuildArch:      noarch
# platform set in makesrc.sh
BuildRequires:  php(language) >= 7.2.5
BuildRequires:  php-cli
BuildRequires:  php-json
BuildRequires:  pkgconfig(bash-completion)
%if %{with generators}
BuildRequires:  composer-generators
%endif

# From composer.json, "require": {
#        "php": "^7.2.5 || ^8.0",
#        "composer/ca-bundle": "^1.0",
#        "composer/metadata-minifier": "^1.0",
#        "composer/semver": "^3.0",
#        "composer/spdx-licenses": "^1.2",
#        "composer/xdebug-handler": "^2.0.2 || ^3.0.3",
#        "justinrainbow/json-schema": "^5.2.11",
#        "psr/log": "^1.0 || ^2.0 || ^3.0"
#        "seld/jsonlint": "~1.4",
#        "seld/phar-utils": "^1.2",
#        "symfony/console": "^5.4.1 || ^6.0",
#        "symfony/filesystem": "^5.4 || ^6.0",
#        "symfony/finder": "^5.4 || ^6.0",
#        "symfony/process": "^5.4 || ^6.0",
#        "react/promise": "^2.8",
#        "composer/pcre": "^2 || ^3"
#        "symfony/polyfill-php73": "^1.24",
#        "symfony/polyfill-php80": "^1.24"
Requires:       php(language)                           >= 7.2.5
Requires:       php-cli
# System certificates
Requires:       ca-certificates

# From composer.json, suggest
#        "ext-openssl": "Enabling the openssl extension allows you to access https URLs for repositories and packages",
#        "ext-zip": "Enabling the zip extension allows you to unzip archives",
#        "ext-zlib": "Allow gzip compression of HTTP requests"
Requires:       php-openssl
Requires:       php-zip
Requires:       php-zlib
# From phpcompatinfo for version 2.2.5
Requires:       php-ctype
Requires:       php-curl
Requires:       php-date
Requires:       php-dom
Requires:       php-filter
Requires:       php-hash
Requires:       php-iconv
Requires:       php-intl
Requires:       php-json
Requires:       php-libxml
Requires:       php-mbstring
Requires:       php-pcntl
Requires:       php-pcre
Requires:       php-phar
Requires:       php-posix
Requires:       php-reflection
Requires:       php-spl
Requires:       php-tokenizer
Requires:       php-xsl
Requires:       php-zlib

# Bundled libraries
%if %{without generators}
# License MIT
Provides:       bundled(php-composer(composer/ca-bundle)) = 1.5.5
Provides:       bundled(php-composer(composer/class-map-generator)) = 1.5.0
Provides:       bundled(php-composer(composer/metadata-minifier)) = 1.0.0
Provides:       bundled(php-composer(composer/pcre)) = 2.3.2
Provides:       bundled(php-composer(composer/semver)) = 3.4.3
Provides:       bundled(php-composer(composer/spdx-licenses)) = 1.5.8
Provides:       bundled(php-composer(composer/xdebug-handler)) = 3.0.5
Provides:       bundled(php-composer(justinrainbow/json-schema)) = 5.3.0
Provides:       bundled(php-composer(psr/container)) = 1.1.1
Provides:       bundled(php-composer(psr/log)) = 1.1.4
Provides:       bundled(php-composer(react/promise)) = 3.2.0
Provides:       bundled(php-composer(seld/jsonlint)) = 1.11.0
Provides:       bundled(php-composer(seld/phar-utils)) = 1.2.1
Provides:       bundled(php-composer(seld/signal-handler)) = 2.0.2
Provides:       bundled(php-composer(symfony/console)) = 5.4.47
Provides:       bundled(php-composer(symfony/deprecation-contracts)) = 2.5.4
Provides:       bundled(php-composer(symfony/filesystem)) = 5.4.45
Provides:       bundled(php-composer(symfony/finder)) = 5.4.45
Provides:       bundled(php-composer(symfony/polyfill-ctype)) = 1.31.0
Provides:       bundled(php-composer(symfony/polyfill-intl-grapheme)) = 1.31.0
Provides:       bundled(php-composer(symfony/polyfill-intl-normalizer)) = 1.31.0
Provides:       bundled(php-composer(symfony/polyfill-mbstring)) = 1.31.0
Provides:       bundled(php-composer(symfony/polyfill-php73)) = 1.31.0
Provides:       bundled(php-composer(symfony/polyfill-php80)) = 1.31.0
Provides:       bundled(php-composer(symfony/polyfill-php81)) = 1.31.0
Provides:       bundled(php-composer(symfony/process)) = 5.4.47
Provides:       bundled(php-composer(symfony/service-contracts)) = 2.5.4
Provides:       bundled(php-composer(symfony/string)) = 5.4.47
# Composer library
Provides:       php-composer(composer/composer) = %{version}
%endif
# Special internal for Plugin API
Provides:       php-composer(composer-plugin-api) = %{api_version}
Provides:       php-composer(composer-runtime-api) = %{run_version}


%description
Composer helps you declare, manage and install dependencies of PHP projects,
ensuring you have the right stack everywhere.

Documentation: https://getcomposer.org/doc/


%prep
%setup -q -n %{gh_project}-%{gh_commit}

%patch -P0 -p1 -b .rpm
%patch -P1 -p1 -b .noxdg
find . \( -name \*.rpm -o -name \*noxdg \) -delete -print

rm vendor/composer/ca-bundle/res/cacert.pem

%if %{without generators}
: List bundled libraries and Licenses
php -r '
	$pkgs = file_get_contents("vendor/composer/installed.json");
	$pkgs = json_decode($pkgs, true);
	if (!is_array($pkgs) || !isset($pkgs["packages"])) {
        echo "cant decode json file\n";
		exit(3);
	}
	$res = [];
    foreach($pkgs["packages"] as $pkg) {
		$lic = implode(" and ", $pkg["license"]);
		if (!isset($res[$lic])) $res[$lic] = [];
		$res[$lic][] = sprintf("Provides:       bundled(php-composer(%s)) = %s", $pkg["name"], trim($pkg["version"], "v"));
	}
	foreach($res as $lic => $lib) {
		sort($lib);
		printf("# License %s\n%s\n", $lic, implode("\n", $lib));
	}
'
%endif

: fix reported version
sed -e '/BRANCH_ALIAS_VERSION/s/@package_branch_alias_version@//' \
    -i src/Composer/Composer.php

: check Plugin API version
php -r '
namespace Composer;
include "src/bootstrap.php";
if (version_compare(Plugin\PluginInterface::PLUGIN_API_VERSION, "%{api_version}")) {
  printf("Plugin API version is %s, expected %s\n", Plugin\PluginInterface::PLUGIN_API_VERSION, "%{api_version}");
  exit(1);
}
if (version_compare(Composer::RUNTIME_API_VERSION, "%{run_version}")) {
  printf("Runtime API version is %s, expected %s\n", Composer::RUNTIME_API_VERSION, "%{run_version}");
  exit(1);
}'


%build
: Nothing to build


%install
: Profile scripts
install -Dpm 644 %{SOURCE1} %{buildroot}%{bashcompdir}/%{name}
mkdir -p %{buildroot}%{_sysconfdir}/profile.d
install -m 644 %{SOURCE3} %{SOURCE4} %{buildroot}%{_sysconfdir}/profile.d/

: Library autoloader for compatibility
mkdir -p     %{buildroot}%{_datadir}/php/Composer
ln -s ../../composer/vendor/autoload.php %{buildroot}%{_datadir}/php/Composer/autoload.php

: Sources
mkdir -p %{buildroot}%{_datadir}/%{name}
cp -pr src res vendor LICENSE\
         %{buildroot}%{_datadir}/%{name}/

: Command
install -Dpm 755 bin/%{name} %{buildroot}%{_bindir}/%{name}

: Licenses
ln -sf ../../%{name}/LICENSE LICENSE
cd vendor
for lic in */*/LICENSE
do dir=$(dirname $lic)
   own=$(dirname $dir)
   prj=$(basename $dir)
   ln -sf ../../composer/vendor/$own/$prj/LICENSE ../$own-$prj-LICENSE
done


%check
: Check autoloader
php -r '
  include "%{buildroot}%{_datadir}/%{name}/src/bootstrap.php";
  exit (class_exists("Composer\\Composer") ? 0 : 1);
'
: Check compatibility autoloader
php -r '
  include "%{buildroot}%{_datadir}/php/Composer/autoload.php";
  exit (class_exists("Composer\\Composer") ? 0 : 2);
'


%files
%license *LICENSE
%doc *.md
%doc doc
%doc composer.json
%config(noreplace) %{_sysconfdir}/profile.d/%{name}.*
%{_bindir}/%{name}
%{_datadir}/php/Composer
%{_datadir}/%{name}
%{bashcomproot}


%changelog
* Tue Jan 21 2025 Remi Collet <remi@remirepo.net> - 2.8.5-1
- update to 2.8.5

* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Dec 11 2024 Remi Collet <remi@remirepo.net> - 2.8.4-1
- update to 2.8.4
- re-license spec file to CECILL-2.1

* Mon Nov 18 2024 Remi Collet <remi@remirepo.net> - 2.8.3-1
- update to 2.8.3

* Wed Oct 30 2024 Remi Collet <remi@remirepo.net> - 2.8.2-3
- keep upstream layout for simplicity

* Wed Oct 30 2024 Remi Collet <remi@remirepo.net> - 2.8.2-2
- update to 2.8.2
- fix diagnose command

* Fri Oct  4 2024 Remi Collet <remi@remirepo.net> - 2.8.1-1
- update to 2.8.1

* Thu Oct  3 2024 Remi Collet <remi@remirepo.net> - 2.8.0-1
- update to 2.8.0

* Wed Sep  4 2024 Remi Collet <remi@remirepo.net> - 2.7.9-1
- update to 2.7.9

* Fri Aug 23 2024 Remi Collet <remi@remirepo.net> - 2.7.8-1
- update to 2.7.8

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Tue Jun 11 2024 Remi Collet <remi@remirepo.net> - 2.7.7-1
- update to 2.7.7

* Sun May  5 2024 Remi Collet <remi@remirepo.net> - 2.7.6-1
- update to 2.7.6

* Tue Apr 23 2024 Remi Collet <remi@remirepo.net> - 2.7.4-1
- update to 2.7.4

* Tue Mar 12 2024 Remi Collet <remi@remirepo.net> - 2.7.2-1
- update to 2.7.2

* Sat Feb 10 2024 Remi Collet <remi@remirepo.net> - 2.7.1-1
- update to 2.7.1

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Dec  9 2023 Remi Collet <remi@remirepo.net> - 2.6.6-1
- update to 2.6.6

* Fri Oct  6 2023 Remi Collet <remi@remirepo.net> - 2.6.5-1
- update to 2.6.5

* Fri Sep 29 2023 Remi Collet <remi@remirepo.net> - 2.6.4-1
- update to 2.6.4

* Fri Sep 15 2023 Remi Collet <remi@remirepo.net> - 2.6.3-1
- update to 2.6.3

* Mon Sep  4 2023 Remi Collet <remi@remirepo.net> - 2.6.2-1
- update to 2.6.2

* Fri Sep  1 2023 Remi Collet <remi@remirepo.net> - 2.6.1-1
- update to 2.6.1

* Fri Sep  1 2023 Remi Collet <remi@remirepo.net> - 2.6.0-1
- update to 2.6.0

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jun 10 2023 Remi Collet <remi@remirepo.net> - 2.5.8-1
- update to 2.5.8

* Wed May 24 2023 Remi Collet <remi@remirepo.net> - 2.5.7-1
- update to 2.5.7

* Wed May 24 2023 Remi Collet <remi@remirepo.net> - 2.5.6-1
- update to 2.5.6

* Tue Mar 21 2023 Remi Collet <remi@remirepo.net> - 2.5.5-1
- update to 2.5.5

* Wed Feb 15 2023 Remi Collet <remi@remirepo.net> - 2.5.4-1
- update to 2.5.4

* Fri Feb 10 2023 Remi Collet <remi@remirepo.net> - 2.5.3-1
- update to 2.5.3

* Mon Feb  6 2023 Remi Collet <remi@remirepo.net> - 2.5.2-1
- update to 2.5.2

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Dec 22 2022 Remi Collet <remi@remirepo.net> - 2.5.1-1
- update to 2.5.1

* Tue Dec 20 2022 Remi Collet <remi@remirepo.net> - 2.5.0-1
- update to 2.5.0

* Fri Oct 28 2022 Remi Collet <remi@remirepo.net> - 2.4.4-1
- update to 2.4.4

* Sat Oct 15 2022 Remi Collet <remi@remirepo.net> - 2.4.3-1
- update to 2.4.3

* Thu Sep 15 2022 Remi Collet <remi@remirepo.net> - 2.4.2-1
- update to 2.4.2

* Mon Aug 29 2022 Remi Collet <remi@remirepo.net> - 2.4.1-1
- update to 2.4.1

* Tue Aug 16 2022 Remi Collet <remi@remirepo.net> - 2.4.0-1
- update to 2.4.0

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jul 14 2022 Remi Collet <remi@remirepo.net> - 2.3.10-1
- update to 2.3.10

* Tue Jul  5 2022 Remi Collet <remi@remirepo.net> - 2.3.9-1
- update to 2.3.9

* Fri Jul  1 2022 Remi Collet <remi@remirepo.net> - 2.3.8-1
- update to 2.3.8
- add bash completion file (for upcoming 2.4)

* Tue Jun  7 2022 Remi Collet <remi@remirepo.net> - 2.3.7-1
- update to 2.3.7

* Thu Jun  2 2022 Remi Collet <remi@remirepo.net> - 2.3.6-1
- update to 2.3.6

* Thu Apr 14 2022 Remi Collet <remi@remirepo.net> - 2.3.5-1
- update to 2.3.5

* Fri Apr  8 2022 Remi Collet <remi@remirepo.net> - 2.3.4-1
- update to 2.3.4

* Sat Apr  2 2022 Remi Collet <remi@remirepo.net> - 2.3.3-1
- update to 2.3.3

* Thu Mar 31 2022 Remi Collet <remi@remirepo.net> - 2.3.2-1
- update to 2.3.2

* Wed Mar 30 2022 Remi Collet <remi@remirepo.net> - 2.3.0-1
- update to 2.3.0
- always use bundled libraries
  as symfony/* 5.4 and composer/pcre 2 are not available

* Wed Mar 30 2022 Remi Collet <remi@remirepo.net> - 2.2.10-1
- update to 2.2.10

* Wed Mar 16 2022 Remi Collet <remi@remirepo.net> - 2.2.9-1
- update to 2.2.9

* Tue Mar 15 2022 Remi Collet <remi@remirepo.net> - 2.2.8-1
- update to 2.2.8

* Fri Feb 25 2022 Remi Collet <remi@remirepo.net> - 2.2.7-1
- update to 2.2.7

* Sat Feb  5 2022 Remi Collet <remi@remirepo.net> - 2.2.6-1
- update to 2.2.6

* Tue Jan 25 2022 Remi Collet <remi@remirepo.net> - 2.2.5-2
- use system libraries on Fedora, bundled libraries on EL

* Sat Jan 22 2022 Remi Collet <remi@remirepo.net> - 2.2.5-1
- update to 2.2.5

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Sun Jan  9 2022 Remi Collet <remi@remirepo.net> - 2.2.4-1
- update to 2.2.4

* Sat Jan  1 2022 Remi Collet <remi@remirepo.net> - 2.2.3-1
- update to 2.2.3

* Thu Dec 23 2021 Remi Collet <remi@remirepo.net> - 2.2.1-1
- update to 2.2.1

* Wed Dec 22 2021 Remi Collet <remi@remirepo.net> - 2.2.0-1
- update to 2.2.0
- add dependency on composer/pcre

* Tue Nov 30 2021 Remi Collet <remi@remirepo.net> - 2.1.14-1
- update to 2.1.14

* Tue Nov  9 2021 Remi Collet <remi@remirepo.net> - 2.1.12-1
- update to 2.1.12

* Tue Nov  2 2021 Remi Collet <remi@remirepo.net> - 2.1.11-1
- update to 2.1.11

* Sat Oct 30 2021 Remi Collet <remi@remirepo.net> - 2.1.10-1
- update to 2.1.10
- allow psr/log v2

* Tue Oct  5 2021 Remi Collet <remi@remirepo.net> - 2.1.9-1
- update to 2.1.9

* Sat Sep 18 2021 Remi Collet <remi@remirepo.net> - 2.1.8-1
- update to 2.1.8

* Tue Sep 14 2021 Remi Collet <remi@remirepo.net> - 2.1.7-1
- update to 2.1.7

* Mon Aug 23 2021 Remi Collet <remi@remirepo.net> - 2.1.6-1
- update to 2.1.6

* Fri Jul 23 2021 Remi Collet <remi@remirepo.net> - 2.1.5-1
- update to 2.1.5

* Thu Jul 22 2021 Remi Collet <remi@remirepo.net> - 2.1.4-1
- update to 2.1.4
- raise dependency on justinrainbow/json-schema 5.2.11

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Thu Jun 10 2021 Remi Collet <remi@remirepo.net> - 2.1.3-1
- update to 2.1.3

* Mon Jun  7 2021 Remi Collet <remi@remirepo.net> - 2.1.2-1
- update to 2.1.2

* Mon Jun  7 2021 Remi Collet <remi@remirepo.net> - 2.1.1-2
- fix Composer\InstalledVersions RPM installation

* Fri Jun  4 2021 Remi Collet <remi@remirepo.net> - 2.1.1-1
- update to 2.1.1

* Thu Jun  3 2021 Remi Collet <remi@remirepo.net> - 2.1.0-1
- update to 2.1.0

* Mon May 31 2021 Remi Collet <remi@remirepo.net> - 2.0.14-2
- disable XDG directories usage, see #1955455

* Sat May 22 2021 Remi Collet <remi@remirepo.net> - 2.0.14-1
- update to 2.0.14
- switch to composer/xdebug-handler v2

* Tue Apr 27 2021 Remi Collet <remi@remirepo.net> - 2.0.13-1
- update to 2.0.13
- add dependency on composer/metadata-minifier

* Thu Apr  1 2021 Remi Collet <remi@remirepo.net> - 2.0.12-1
- update to 2.0.12

* Wed Feb 24 2021 Remi Collet <remi@remirepo.net> - 2.0.11-1
- update to 2.0.11

* Tue Feb 23 2021 Remi Collet <remi@remirepo.net> - 2.0.10-1
- update to 2.0.10

* Thu Jan 28 2021 Remi Collet <remi@remirepo.net> - 2.0.9-1
- update to 2.0.9
- switch to Symfony 4
- switch to phpunit9

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Dec  4 2020 Remi Collet <remi@remirepo.net> - 2.0.8-1
- update to 2.0.8

* Sat Nov 14 2020 Remi Collet <remi@remirepo.net> - 2.0.7-1
- update to 2.0.7

* Sun Nov  8 2020 Remi Collet <remi@remirepo.net> - 2.0.6-1
- update to 2.0.6

* Sat Oct 31 2020 Remi Collet <remi@remirepo.net> - 2.0.4-1
- update to 2.0.4

* Thu Oct 29 2020 Remi Collet <remi@remirepo.net> - 2.0.3-1
- update to 2.0.3

* Mon Oct 26 2020 Remi Collet <remi@remirepo.net> - 2.0.2-1
- update to 2.0.2
- raise dependency on composer/semver 3
- add dependency on react/promise 2.7

* Tue Oct 13 2020 Remi Collet <remi@remirepo.net> - 1.10.15-1
- update to 1.10.15

* Wed Sep  9 2020 Remi Collet <remi@remirepo.net> - 1.10.13-1
- update to 1.10.13

* Wed Sep  9 2020 Remi Collet <remi@remirepo.net> - 1.10.12-1
- update to 1.10.12

* Tue Aug  4 2020 Remi Collet <remi@remirepo.net> - 1.10.10-1
- update to 1.10.10

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jul 16 2020 Remi Collet <remi@remirepo.net> - 1.10.9-1
- update to 1.10.9

* Thu Jun 25 2020 Remi Collet <remi@remirepo.net> - 1.10.8-1
- update to 1.10.8

* Wed Jun  3 2020 Remi Collet <remi@remirepo.net> - 1.10.7-1
- update to 1.10.7
- raise dependency on justinrainbow/json-schema 5.2.10

* Wed May  6 2020 Remi Collet <remi@remirepo.net> - 1.10.6-1
- update to 1.10.6
- provide php-composer(composer-runtime-api)

* Fri Apr 10 2020 Remi Collet <remi@remirepo.net> - 1.10.5-1
- update to 1.10.5

* Thu Apr  9 2020 Remi Collet <remi@remirepo.net> - 1.10.4-1
- update to 1.10.4

* Sat Mar 14 2020 Remi Collet <remi@remirepo.net> - 1.10.1-1
- update to 1.10.1

* Wed Mar 11 2020 Remi Collet <remi@remirepo.net> - 1.10.0-1
- update to 1.10.0

* Tue Feb  4 2020 Remi Collet <remi@remirepo.net> - 1.9.3-1
- update to 1.9.3

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Jan 14 2020 Remi Collet <remi@remirepo.net> - 1.9.2-1
- update to 1.9.2

* Sat Nov  2 2019 Remi Collet <remi@remirepo.net> - 1.9.1-1
- update to 1.9.1

* Wed Oct  9 2019 Remi Collet <remi@remirepo.net> - 1.9.0-2
- add upstream patch for PHP 7.4

* Sat Aug  3 2019 Remi Collet <remi@remirepo.net> - 1.9.0-1
- update to 1.9.0

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Jun 11 2019 Remi Collet <remi@remirepo.net> - 1.8.6-1
- update to 1.8.6

* Wed Apr 10 2019 Remi Collet <remi@remirepo.net> - 1.8.5-1
- update to 1.8.5

* Mon Feb 11 2019 Remi Collet <remi@remirepo.net> - 1.8.4-1
- update to 1.8.4

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Jan 30 2019 Remi Collet <remi@remirepo.net> - 1.8.3-1
- update to 1.8.3

* Mon Dec  3 2018 Remi Collet <remi@remirepo.net> - 1.8.0-1
- update to 1.8.0

* Fri Nov  2 2018 Remi Collet <remi@remirepo.net> - 1.7.3-1
- update to 1.7.3

* Fri Aug 17 2018 Remi Collet <remi@remirepo.net> - 1.7.2-1
- update to 1.7.2
- drop dependency on seld/cli-prompt
- add dependency on composer/xdebug-handler

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri May  4 2018 Remi Collet <remi@remirepo.net> - 1.6.5-1
- update to 1.6.5

* Mon Apr 16 2018 Remi Collet <remi@remirepo.net> - 1.6.4-1
- update to 1.6.4

* Tue Feb 20 2018 Remi Collet <remi@remirepo.net> - 1.6.3-4
- switch to Symfony2 only

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Feb  1 2018 Remi Collet <remi@remirepo.net> - 1.6.3-2
- undefine __brp_mangle_shebangs (F28)

* Thu Feb  1 2018 Remi Collet <remi@remirepo.net> - 1.6.3-1
- Update to 1.6.3

* Sun Jan  7 2018 Remi Collet <remi@remirepo.net> - 1.6.2-1
- Update to 1.6.2

* Thu Jan  4 2018 Remi Collet <remi@remirepo.net> - 1.6.1-1
- Update to 1.6.1

* Thu Jan  4 2018 Remi Collet <remi@remirepo.net> - 1.6.0-2
- open https://github.com/composer/composer/pull/6974
  Fix dependency on composer/spdx-licenses
- raise dependency on composer/spdx-licenses 1.2

* Mon Dec 18 2017 Remi Collet <remi@remirepo.net> - 1.5.6-1
- Update to 1.5.6
- switch to symfony package names

* Fri Dec  1 2017 Remi Collet <remi@remirepo.net> - 1.5.5-1
- Update to 1.5.5

* Fri Dec  1 2017 Remi Collet <remi@remirepo.net> - 1.5.4-1
- Update to 1.5.4

* Fri Dec  1 2017 Remi Collet <remi@remirepo.net> - 1.5.3-1
- Update to 1.5.3

* Mon Sep 11 2017 Remi Collet <remi@remirepo.net> - 1.5.2-1
- Update to 1.5.2

* Wed Aug  9 2017 Remi Collet <remi@remirepo.net> - 1.5.1-1
- Update to 1.5.1

* Tue Aug  8 2017 Remi Collet <remi@remirepo.net> - 1.5.0-1
- Update to 1.5.0

* Mon Aug  7 2017 Remi Collet <remi@remirepo.net> - 1.4.3-1
- Update to 1.4.3
- ignore 2 failed tests related to BC break in symfony

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon May 22 2017 Remi Collet <remi@remirepo.net> - 1.4.2-2
- Update to 1.4.2
- fix autoloader to allow symfony 2 and 3
- raise dependency on justinrainbow/json-schema v5
- open https://github.com/composer/composer/pull/6435 - fix tests

* Fri Mar 10 2017 Remi Collet <remi@remirepo.net> - 1.4.1-1
- Update to 1.4.1

* Wed Mar  8 2017 Remi Collet <remi@remirepo.net> - 1.4.0-1
- Update to 1.4.0
- raise dependency on justinrainbow/json-schema version 3 to 5

* Wed Mar  8 2017 Remi Collet <remi@remirepo.net> - 1.3.3-1
- Update to 1.3.3

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sat Jan 28 2017 Remi Collet <remi@fedoraproject.org> - 1.3.2-1
- update to 1.3.2

* Sat Jan  7 2017 Remi Collet <remi@fedoraproject.org> - 1.3.1-1
- update to 1.3.1

* Sat Dec 24 2016 Remi Collet <remi@fedoraproject.org> - 1.3.0-1
- update to 1.3.0
- raise dependency on symfony 2.7
- allow justinrainbow/json-schema 4

* Fri Dec 16 2016 Remi Collet <remi@fedoraproject.org> - 1.2.4-2
- fix BR for json-schema, FTBFS from Koschei

* Wed Dec  7 2016 Remi Collet <remi@fedoraproject.org> - 1.2.4-1
- update to 1.2.4

* Thu Dec  1 2016 Remi Collet <remi@fedoraproject.org> - 1.2.3-1
- update to 1.2.3

* Thu Nov 17 2016 Remi Collet <remi@fedoraproject.org> - 1.2.2-2
- add profile scripts so globally installed commands
  will be found in default user path #1394577

* Thu Nov  3 2016 Remi Collet <remi@fedoraproject.org> - 1.2.2-1
- update to 1.2.2

* Fri Oct 21 2016 Remi Collet <remi@fedoraproject.org> - 1.2.1-2
- switch from symfony/class-loader to fedora/autoloader

* Mon Sep 12 2016 Remi Collet <remi@fedoraproject.org> - 1.2.1-1
- update to 1.2.1

* Tue Jul 19 2016 Remi Collet <remi@fedoraproject.org> - 1.2.0-1
- update to 1.2.0
- switch to justinrainbow/json-schema v2

* Sun Jun 26 2016 Remi Collet <remi@fedoraproject.org> - 1.1.3-1
- update to 1.1.3

* Wed Jun  1 2016 Remi Collet <remi@fedoraproject.org> - 1.1.2-1
- update to 1.1.2

* Tue May 31 2016 Remi Collet <remi@fedoraproject.org> - 1.1.1-2
- ensure justinrainbow/json-schema v1 is used for the build

* Tue May 17 2016 Remi Collet <remi@fedoraproject.org> - 1.1.1-1
- update to 1.1.1
- add dependency on composer/ca-bundle
- add dependency on psr/log
- bump composer-plugin-api to 1.1.0
- drop dependency on ca-certificates

* Sat Apr 30 2016 Remi Collet <remi@fedoraproject.org> - 1.0.3-1
- update to 1.0.3

* Thu Apr 21 2016 Remi Collet <remi@fedoraproject.org> - 1.0.2-1
- update to 1.0.2

* Tue Apr 19 2016 Remi Collet <remi@fedoraproject.org> - 1.0.1-1
- update to 1.0.1
- add dependency on ca-certificates
- fix patch for RPM path

* Tue Apr  5 2016 Remi Collet <remi@fedoraproject.org> - 1.0.0-1
- update to 1.0.0

* Tue Mar 29 2016 Remi Collet <remi@fedoraproject.org> - 1.0.0-0.22.beta2
- update to 1.0.0beta2

* Fri Mar  4 2016 Remi Collet <remi@fedoraproject.org> - 1.0.0-0.21.beta1
- update to 1.0.0beta1

* Tue Feb 23 2016 Remi Collet <remi@fedoraproject.org> - 1.0.0-0.20.201602git4c0e163
- new snapshot
- raise dependency on justinrainbow/json-schema ^1.6

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-0.19.20160106git64b0d72
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jan  8 2016 Remi Collet <remi@fedoraproject.org> - 1.0.0-0.18.20160106git64b0d72
- add patch for json-schema 1.6, FTBFS detected by Koschei
  open https://github.com/composer/composer/pull/4756
- new snapshot
- raise dependency on seld/jsonlint ^1.4

* Thu Jan  7 2016 Remi Collet <remi@fedoraproject.org> - 1.0.0-0.16.alpha1
- remove duplicated register in autoloader

* Sat Nov 14 2015 Remi Collet <remi@fedoraproject.org> - 1.0.0-0.15.alpha1
- update to 1.0.0alpha11

* Mon Nov  2 2015 Remi Collet <remi@fedoraproject.org> - 1.0.0-0.14.20151030git5a5088e
- new snapshot
- allow symfony 3

* Wed Oct 14 2015 Remi Collet <remi@fedoraproject.org> - 1.0.0-0.13.20151013gita54f84f
- new snapshot
- use autoloader from all dependencies

* Sun Oct 11 2015 Remi Collet <remi@fedoraproject.org> - 1.0.0-0.12.20151007git7a9eb02
- new snapshot
- provide php-composer(composer-plugin-api)
- don't check version in diagnose command
- add dependency on composer/semver
- add dependency on symfony/filesystem

* Tue Sep  8 2015 Remi Collet <remi@fedoraproject.org> - 1.0.0-0.9.20150907git9f6fdfd
- new snapshot
- add LICENSE in application data, as used by the code

* Fri Aug  7 2015 Remi Collet <remi@fedoraproject.org> - 1.0.0-0.8.20150804gitc83650f
- new snapshot

* Tue Jul 21 2015 Remi Collet <remi@fedoraproject.org> - 1.0.0-0.8.20150720git00c2679
- new snapshot
- add dependency on composer/spdx-licenses

* Thu Jul 16 2015 Remi Collet <remi@fedoraproject.org> - 1.0.0-0.7.20150714git92faf1c
- new snapshot
- raise dependency on justinrainbow/json-schema 1.4.4

* Mon Jun 29 2015 Remi Collet <remi@fedoraproject.org> - 1.0.0-0.6.20150626git943107c
- new snapshot
- review autoloader

* Sun Jun 21 2015 Remi Collet <remi@fedoraproject.org> - 1.0.0-0.5.20150620gitd0ff016
- new snapshot
- add missing BR on php-zip
- open https://github.com/composer/composer/pull/4169 for online test

* Mon Jun 15 2015 Remi Collet <remi@fedoraproject.org> - 1.0.0-0.5.20150614git8e9659b
- new snapshot

* Sun Jun  7 2015 Remi Collet <remi@fedoraproject.org> - 1.0.0-0.5.20150605git9fb2d4f
- new snapshot

* Tue Jun  2 2015 Remi Collet <remi@fedoraproject.org> - 1.0.0-0.5.20150531git0ec86be
- new snapshot

* Tue May 26 2015 Remi Collet <remi@fedoraproject.org> - 1.0.0-0.5.20150525git69210d5
- new snapshot
- ensure /usr/share/php is in include_path (for SCL)

* Wed May 13 2015 Remi Collet <remi@fedoraproject.org> - 1.0.0-0.4.20150511gitbc45d91
- new snapshot

* Mon May  4 2015 Remi Collet <remi@fedoraproject.org> - 1.0.0-0.4.20150503git42a9561
- new snapshot
- add dependencies on seld/phar-utils and seld/cli-prompt

* Mon Apr 27 2015 Remi Collet <remi@fedoraproject.org> - 1.0.0-0.3.20150426git1cb427f
- new snapshot

* Fri Apr 17 2015 Remi Collet <remi@fedoraproject.org> - 1.0.0-0.3.20150415git921b3a0
- new snapshot
- raise dependency on justinrainbow/json-schema ~1.4
- keep upstream shebang with /usr/bin/env (for SCL)

* Thu Apr  9 2015 Remi Collet <remi@fedoraproject.org> - 1.0.0-0.3.20150408git4d134ce
- new snapshot
- lower dependency on justinrainbow/json-schema ~1.3

* Tue Mar 24 2015 Remi Collet <remi@fedoraproject.org> - 1.0.0-0.3.20150324gitc5cd184
- new snapshot
- raise dependency on justinrainbow/json-schema ~1.4

* Thu Mar 19 2015 Remi Collet <remi@fedoraproject.org> - 1.0.0-0.2.20150316git829199c
- new snapshot

* Wed Mar  4 2015 Remi Collet <remi@fedoraproject.org> - 1.0.0-0.2.20150302giteadc167
- new snapshot

* Sat Feb 28 2015 Remi Collet <remi@fedoraproject.org> - 1.0.0-0.2.20150227git45b1f35
- new snapshot

* Thu Feb 26 2015 Remi Collet <remi@fedoraproject.org> - 1.0.0-0.1.20150225gite5985a9
- Initial package
