# fedora spec file for php-giggsey-locale
#
# Copyright (c) 2020 Christopher Engelhard
# License: MIT
#
# Please, preserve the changelog entries

# package and composer name
%global vendor   giggsey
%global project  locale

# PHP namespace and directory
%global ns_project  Giggsey\\Locale
%global ns_dir      %( echo "%{ns_project}" | sed  's|\\\\|\/|g' )

# Github
%global gh_vendor   giggsey
%global gh_project  Locale
%global commit      b07f1eace8072ccc61445ad8fbd493ff9d783043
%global scommit     %(c=%{commit}; echo ${c:0:7})

# tests
%global with_tests 1

#-- PREAMBLE ------------------------------------------------------------------#
Name:           php-%{vendor}-%{project}
Version:        1.9
Release:        %autorelease
Summary:        Locale functions required by libphonenumber-for-php

License:        MIT
URL:            https://github.com/%{gh_vendor}/%{gh_project}
Source0:        https://github.com/%{gh_vendor}/%{gh_project}/archive/%{commit}/%{gh_project}-%{version}-%{scommit}.tar.gz

BuildArch:      noarch

# for the autoloader
Requires:       php-composer(fedora/autoloader)

# from composer.json
Requires:       php(language) >= 5.3.2

# from phpcompatinfo
Requires:       php-spl

# for autoloader check
BuildRequires:  php-composer(fedora/autoloader)
BuildRequires:  %{_bindir}/php
BuildRequires:  php(language) >= 5.3.2

%if 0%{?with_tests}
# for tests
%endif

# composer provides
Provides:       php-composer(%{vendor}/%{project}) = %{version}

%description
A library providing up to date CLDR. Primarily as a requirement of
libphonenumber-for-php.

Autoloader: %{_datadir}/php/%{ns_dir}/autoload.php


#-- PREP, BUILD & INSTALL -----------------------------------------------------#
%prep
%autosetup -p1 -n %{gh_project}-%{commit}

%build
: Nothing to build.

%install
: Create a PSR-0 tree
mkdir -p   %{buildroot}%{_datadir}/php/%{ns_dir}
cp -pr src %{buildroot}%{_datadir}/php/%{ns_dir}
cp -pr data %{buildroot}%{_datadir}/php/%{ns_dir}

: Generate an autoloader
cat <<'EOF' | tee %{buildroot}%{_datadir}/php/%{ns_dir}/autoload.php
<?php
require_once '%{_datadir}/php/Fedora/Autoloader/autoload.php';

\Fedora\Autoloader\Autoload::addPsr4('%{ns_project}', __DIR__.'/src');

\Fedora\Autoloader\Dependencies::required(array(
    // no required dependencies
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
        class_exists('%{ns_project}\Locale')
        ? 0 : 1
    );
"
%if 0%{?with_tests}
: Run tests
: No tests implemented
%endif

#-- FILES ---------------------------------------------------------------------#
%files
%license LICENSE
%doc composer.json
%doc README.md
%{_datadir}/php/%{ns_dir}


#-- CHANGELOG -----------------------------------------------------------------#
%changelog
%autochangelog
