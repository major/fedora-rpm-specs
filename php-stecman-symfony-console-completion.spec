# fedora spec file for php-fgrosse-phpasn1
#
# Copyright (c) 2020-2022 Christopher Engelhard <ce@lcts.de>
# Copyright (c) 2017-2019 Shawn Iwinski <shawn@iwin.ski>
# License: MIT
#
# Please preserve the changelog entries

# package and composer name
%global vendor      stecman
%global project     symfony-console-completion

# PHP namespace and directory
%global ns_vendor   Stecman
%global ns_project  Component\\Symfony\\Console\\BashCompletion
%global ns_dir      %{ns_vendor}/%( echo '%{ns_project}' | sed  's|\\\\|\/|g' )

# Github
%global gh_vendor   stecman
%global gh_project  symfony-console-completion
%global commit      a9502dab59405e275a9f264536c4e1cb61fc3518
%global scommit     %(c=%{commit}; echo ${c:0:7})

# tests
%bcond_without tests

#-- PREAMBLE ------------------------------------------------------------------#
Name:          php-%{vendor}-%{project}
Version:       0.11.0
Release:       4%{?dist}
Summary:       Automatic BASH completion for Symfony Console based applications

License:       MIT
URL:           https://github.com/%{gh_vendor}/%{gh_project}
# Since github tarballs are lacking the tests, source is created via a local git checkout instead.
# Use ./makesrc.sh in the same directory as the specfile to generate the source archive
Source0:        %{name}-%{version}-%{scommit}.tgz
Source1:        makesrc.sh

# phpunit8 compatibility fixes
Patch01:	01-fix-phpunit8-errors.patch
Patch02:	02-disable-failing-tests.patch

BuildArch:     noarch

# for the autoloader
Requires:	php-composer(fedora/autoloader)

# from composer.json
Requires:	php(language) >= 5.3.2
Requires:      (php-composer(symfony/console) >= 2.7.1 with php-composer(symfony/console) < 6.0)

# from phpcompatinfo
Requires:      php-pcre
Requires:      php-spl

# for autoloader check
BuildRequires:  php-composer(fedora/autoloader)
BuildRequires:  %{_bindir}/php
BuildRequires:  php(language) >= 7.0

%if %{with tests}
# for tests
BuildRequires: phpunit8
BuildRequires: php-pcre
BuildRequires: php-spl
BuildRequires: (php-composer(symfony/console) >= 2.7.1 with php-composer(symfony/console) < 6.0)
BuildRequires: zsh
%endif

# composer provides
Provides:	php-composer(%{vendor}/%{project}) = %{version}

%description
This package provides automatic (tab) completion in BASH and ZSH for Symfony
Console Component based applications. With zero configuration, this package
allows completion of available command names and the options they provide.
User code can define custom completion behaviour for argument and option values.

The library autoloader is: %{_datadir}/php/%{ns_dir}/autoload.php


#-- PREP, BUILD & INSTALL -----------------------------------------------------#
%prep
%autosetup -p1 -n %{gh_project}-%{commit}

%build
: Nothing to build.

%install
: Create installation directory
mkdir -p   %{buildroot}%{_datadir}/php/%{ns_dir}
cp -pr src/* %{buildroot}%{_datadir}/php/%{ns_dir}

: Generate an autoloader
cat <<'EOF' | tee %{buildroot}%{_datadir}/php/%{ns_dir}/autoload.php
<?php
/**
 * Autoloader for %{name} and its' dependencies
 * (created by %{name}-%{version}-%{release}).
 */

require_once '%{_datadir}/php/Fedora/Autoloader/autoload.php';

// classes
\Fedora\Autoloader\Autoload::addPsr4('%{ns_vendor}\%{ns_project}', __DIR__);

// files & dependencies
\Fedora\Autoloader\Dependencies::required(array(
    array(
        '%{_datadir}/php/Symfony4/Component/Console/autoload.php',
        '%{_datadir}/php/Symfony3/Component/Console/autoload.php',
        '%{_datadir}/php/Symfony/Component/Console/autoload.php',
    ),
));

\Fedora\Autoloader\Dependencies::optional(array(
   // no optional dependencies
));
EOF

%check
: Check the autoloader
%{_bindir}/php -r "
    require_once '%{buildroot}%{_datadir}/php/%{ns_dir}/autoload.php';
    exit(
	class_exists('%{ns_vendor}\%{ns_project}\CompletionCommand')
        ? 0 : 1
    );
"
%if %{with tests}
: Create a autoloader for tests
mkdir vendor
cat << 'EOF' | tee vendor/autoload.php
<?php
require_once '%{buildroot}%{_datadir}/php/%{ns_dir}/autoload.php';
\Fedora\Autoloader\Autoload::addPsr4('%{ns_vendor}\%{ns_project}\Test', dirname(__DIR__).'/tests');
EOF

: Run phpunit tests
%{_bindir}/phpunit8 --verbose
%endif

#-- FILES ---------------------------------------------------------------------#
%files
%{!?_licensedir:%global license %%doc}
%license LICENCE
%doc *.md
%doc composer.json
%dir %{_datadir}/php/%{ns_vendor}
%dir %{_datadir}/php/%{ns_vendor}/Component
%dir %{_datadir}/php/%{ns_vendor}/Component/Symfony
%dir %{_datadir}/php/%{ns_vendor}/Component/Symfony/Console
%{_datadir}/php/%{ns_dir}


#-- CHANGELOG -----------------------------------------------------------------#
%changelog
* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Mon Aug 8 2022 Christopher Engelhard <ce@lcts.de> - 0.11.0-1
- Update to 0.11.0 (rhbz#1794618)
- Get sources as a git checkout for complete tests
- Update tests to PHPUnit 8 / PHP 8 (rhbz#2113593)
- Include zsh as BuildRequires to run completion tests on ZSH
- Disable some failing tests

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue May 14 2019 Shawn Iwinski <shawn@iwin.ski> - 0.10.1-2
- Fix EPEL6 build

* Tue May 14 2019 Shawn Iwinski <shawn@iwin.ski> - 0.10.1-1
- Update to 0.10.1 (RHBZ #1562562)
- Add range version dependencies for Fedora >= 27 || RHEL >= 8

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Nov 03 2017 Shawn Iwinski <shawn@iwin.ski> - 0.7.0-2
- Remove rename of license file

* Thu Oct 26 2017 Shawn Iwinski <shawn@iwin.ski> - 0.7.0-1
- Initial package
