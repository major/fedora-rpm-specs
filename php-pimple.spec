#
# Fedora spec file for php-pimple
#
# Copyright (c) 2015-2018 Shawn Iwinski <shawn.iwinski@gmail.com>
#                         Christian Glombek <christian.glombek@rwth-aachen.de>
#
# License: MIT
# http://opensource.org/licenses/MIT
#
# Please preserve changelog entries
#

%global github_owner     silexphp
%global github_name      Pimple
%global github_version   3.5.0
%global github_commit    a94b3a4db7fb774b3d78dad2315ddc07629e1bed

%global composer_vendor  pimple
%global composer_project pimple

# "php": ">=5.3.0"
%global php_min_ver 7.2.5
# "psr/container": "^1.1|^2.0"
%global psr_container_min_ver 1.1
%global psr_container_max_ver 3.0
# "symfony/phpunit-bridge": "^5.4@dev"
# symfony5 isn't in the repos, but 4.4 works as well
%global phpunit_bridge_min_ver 4.4
%global phpunit_bridge_max_ver 6.0


# Build using "--without tests" to disable tests
%global with_tests  %{?_without_tests:0}%{!?_without_tests:1}

%{!?phpdir:  %global phpdir  %{_datadir}/php}

Name:          php-%{composer_project}
Version:       %{github_version}
Release:       13%{?dist}
Summary:       A simple dependency injection container for PHP

License:       MIT
URL:           http://pimple.sensiolabs.org
Source0:       https://github.com/%{github_owner}/%{github_name}/archive/%{github_commit}/%{name}-%{github_version}-%{github_commit}.tar.gz

BuildArch:     noarch
# Tests
%if %{with_tests}
BuildRequires: phpunit8
## composer.json
BuildRequires: php-composer(psr/container) <  %{psr_container_max_ver}
BuildRequires: php-composer(psr/container) >= %{psr_container_min_ver}
BuildRequires: php-composer(symfony/phpunit-bridge) < %{phpunit_bridge_max_ver}
BuildRequires: php-composer(symfony/phpunit-bridge) >= %{phpunit_bridge_min_ver}
## phpcompatinfo (computed from version 3.5.0)
BuildRequires: php-reflection
BuildRequires: php-spl
## Autoloader
BuildRequires: php-composer(fedora/autoloader)
%endif

# composer.json
Requires:  php(language) >= %{php_min_ver}
Requires:  php-composer(psr/container) <  %{psr_container_max_ver}
Requires:  php-composer(psr/container) >= %{psr_container_min_ver}
# phpcompatinfo (computed from version 3.2.3)
Requires:  php-spl
## Autoloader
Requires:  php-composer(fedora/autoloader)

# Composer
Provides:  php-composer(%{composer_vendor}/%{composer_project}) = %{version}
# Rename
Obsoletes: php-Pimple < %{version}-%{release}
Provides:  php-Pimple = %{version}-%{release}
# Drop extension
Obsoletes: php-pimple-lib < %{version}-%{release}
Provides:  php-pimple-lib = %{version}-%{release}

%description
%{summary}.

Autoloader: %{phpdir}/Pimple/autoload.php


%prep
%setup -qn %{github_name}-%{github_commit}


%build
: Create autoloader
cat <<'AUTOLOAD' | tee src/Pimple/autoload.php
<?php
/**
 * Autoloader for %{name} and its' dependencies
 * (created by %{name}-%{version}-%{release}).
 */
require_once '%{phpdir}/Fedora/Autoloader/autoload.php';

\Fedora\Autoloader\Autoload::addPsr4('Pimple\\', __DIR__);

\Fedora\Autoloader\Dependencies::required(array(
    array(
        '%{phpdir}/Psr/Container2/autoload.php', // v2 preferred
        '%{phpdir}/Psr/Container/autoload.php', // v1 as fallback
)));
AUTOLOAD


%install
mkdir -p %{buildroot}/%{phpdir}/
cp -rp src/Pimple %{buildroot}/%{phpdir}/


%check
: Check the autoloader
%{_bindir}/php -r "
    require_once '%{buildroot}/%{phpdir}/Pimple/autoload.php';
    exit(
        class_exists('\Pimple\Container')
        ? 0 : 1
    );
"

%if %{with_tests}
: Create a autoloader for tests
mkdir vendor
cat << 'EOF' | tee vendor/autoload.php
<?php
require_once '%{buildroot}/%{phpdir}/Pimple/autoload.php';
require_once '%{phpdir}/Symfony4/Bridge/PhpUnit/autoload.php';
EOF

: Upstream tests
: Run phpunit tests
#%{_bindir}/phpunit8 --verbose --bootstrap %{buildroot}/%{phpdir}/Pimple/autoload.php
%{_bindir}/phpunit8 --verbose
%else
: Tests skipped
%endif


%files
%{!?_licensedir:%global license %%doc}
%license LICENSE
%doc CHANGELOG
%doc README.rst
%doc composer.json
%{phpdir}/Pimple
%exclude %{phpdir}/Pimple/Tests


%changelog
* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.5.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.5.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Tue Aug 2 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.5.0-11
- Update to 3.5.0 (rhbz#1809679, rhbz#1987852)

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.3-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.3-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Christian Glombek <christian.glombek@rwth-aachen.de> - 3.2.3-1
- Update to 3.2.3 (RHBZ #1467881)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Aug 05 2017 Shawn Iwinski <shawn.iwinski@gmail.com> - 3.2.2-1
- Update to 3.2.2 (RHBZ #1467881)
- Drop extension completely
- Switch autoloader to php-composer(fedora/autoloader)
- Test with SCLs if available

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Jul 07 2017 Igor Gnatenko <ignatenko@redhat.com> - 3.0.2-5
- Rebuild due to bug in RPM (RHBZ #1468476)

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Jun 27 2016 Remi Collet <remi@fedoraproject.org> - 3.0.2-3
- disable the extension with PHP 7

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sat Sep 12 2015 Shawn Iwinski <shawn.iwinski@gmail.com> - 3.0.2-1
- Updated to 3.0.2 (RHBZ #1262507)

* Sun Aug 02 2015 Shawn Iwinski <shawn.iwinski@gmail.com> - 3.0.1-1
- Updated to 3.0.1

* Mon Jul 20 2015 Shawn Iwinski <shawn.iwinski@gmail.com> - 3.0.0-5
- Autoloader changed to Symfony ClassLoader

* Thu May 21 2015 Shawn Iwinski <shawn.iwinski@gmail.com> - 3.0.0-4
- Add library autoloader
- Spec cleanup

* Wed Sep 03 2014 Shawn Iwinski <shawn.iwinski@gmail.com> - 3.0.0-3
- Separate extension and library (i.e. sub-package library)

* Mon Aug 25 2014 Shawn Iwinski <shawn.iwinski@gmail.com> - 3.0.0-2
- Fixed compat file location in description
- Included real class in compat file
- Always run extension minimal load test
- Fixed test suite with previous installed version
- "make test NO_INTERACTION=1 REPORT_EXIT_STATUS=1" instead of "echo "n" | make test"

* Thu Jul 31 2014 Shawn Iwinski <shawn.iwinski@gmail.com> - 3.0.0-1
- Updated to 3.0.0
- Added custom compat file for obsoleted php-Pimple

* Tue Jul 29 2014 Shawn Iwinski <shawn.iwinski@gmail.com> - 2.1.1-1
- Initial package
