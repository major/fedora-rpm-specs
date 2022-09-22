# fedora spec file for php-league-uri-interfaces
#
# Copyright (c) 2020 Christopher Engelhard
# License: MIT
#
# Please preserve the changelog entries

# package and composer name
%global vendor      league
%global project     uri-interfaces

# PHP namespace and directory
%global ns_project  League\\Uri
%global vendordir   League
%global ns_dir      League/UriInterfaces

# Github
%global gh_vendor   thephpleague
%global gh_project  uri-interfaces
%global commit      00e7e2943f76d8cb50c7dfdc2f6dee356e15e383
%global scommit     %(c=%{commit}; echo ${c:0:7})

# tests
%bcond_without tests

#-- PREAMBLE ------------------------------------------------------------------#
Name:           php-%{vendor}-%{project}
Version:        2.3.0
Release:        %autorelease
Summary:        Common interface for URI representation

License:        MIT
URL:            https://github.com/%{gh_vendor}/%{gh_project}
# Since github tarballs are lacking the tests, source is created via a local git checkout instead.
# Use ./makesrc.sh in the same directory as the specfile to generate the source archive
Source0:        %{name}-%{version}-%{scommit}.tgz
Source1:        makesrc.sh

BuildArch:      noarch

# for the autoloader
Requires:       php-composer(fedora/autoloader)

# from composer.json
Requires:       php(language) >= 7.2
Requires:       php-json
Recommends:     php-intl

# from phpcompatinfo
Requires:       php-pcre
Requires:       php-spl

# for autoloader check
BuildRequires:  php-composer(fedora/autoloader)
BuildRequires:  %{_bindir}/php
BuildRequires:  php(language) >= 7.2

%if %{with tests}
# for tests
BuildRequires: phpunit9
BuildRequires: php-json
BuildRequires: php-pcre
BuildRequires: php-spl
BuildRequires: php-intl
%endif

# composer provides
Provides:       php-composer(%{vendor}/%{project}) = %{version}

%description
Package containing an interface to represents URI objects according to RFC 3986.

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
require_once '%{_datadir}/php/Fedora/Autoloader/autoload.php';

// classes
\Fedora\Autoloader\Autoload::addPsr4('%{ns_project}', __DIR__);

// files & dependencies
\Fedora\Autoloader\Dependencies::required(array(
  // no mandatory dependencies
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
        class_exists('%{ns_project}\Exceptions\SyntaxError')
        ? 0 : 1
    );
"
%if %{with tests}
: Run phpunit tests
%{_bindir}/phpunit9 --verbose --bootstrap %{buildroot}%{_datadir}/php/%{ns_dir}/autoload.php
%endif

#-- FILES ---------------------------------------------------------------------#
%files
%license LICENSE
%doc composer.json
%doc *.md
%dir %{_datadir}/php/%{vendordir}
%{_datadir}/php/%{ns_dir}


#-- CHANGELOG -----------------------------------------------------------------#
%changelog
%autochangelog
