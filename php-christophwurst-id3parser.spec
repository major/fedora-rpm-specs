# fedora spec file for php-christophewurst-id3parser
#
# Copyright (c) 2020 Christopher Engelhard
# License: MIT
#
# Please preserve the changelog entries

# package and composer name
%global vendor      christophwurst
%global project     id3parser

# PHP namespace and directory
%global ns_vendor   ChristophWurst
%global ns_project  ID3Parser
%global ns_dir      %{ns_vendor}/%( echo "%{ns_project}" | sed  's|\\\\|\/|g' )

# Github
%global gh_vendor   ChristophWurst
%global gh_project  ID3Parser
%global commit      d7f5e9e7db69a24e3111a2033cbdf640f9456f2f
%global scommit     %(c=%{commit}; echo ${c:0:7})

# tests
%global with_tests 1

#-- PREAMBLE ------------------------------------------------------------------#
Name:           php-%{vendor}-%{project}
Version:        0.1.2
Release:        %autorelease
Summary:        A pure ID3 parser based upon getID3

License:        GPLv3
URL:            https://github.com/%{gh_vendor}/%{gh_project}
Source0:        https://github.com/%{gh_vendor}/%{gh_project}/archive/%{commit}/%{gh_project}-%{version}-%{scommit}.tar.gz

BuildArch:      noarch

# for the autoloader
Requires:       php-composer(fedora/autoloader)

# from composer.json
Requires:       php(language) >= 5.4

# from phpcompatinfo
Requires:       php-date
Requires:       php-pcre
Requires:       php-iconv
Requires:       php-zlib

# for autoloader check
BuildRequires:  php-composer(fedora/autoloader)
BuildRequires:  %{_bindir}/php
BuildRequires:  php(language) >= 5.4

%if 0%{?with_tests}
# for tests
%endif

# composer provides
Provides:       php-composer(%{vendor}/%{project}) = %{version}
# this is a fork of lukasreschke/id3parser, which is abandoned upstream
Provides:       php-lukasreschke-%{project} = %{version}
Provides:       php-composer(lukasreschke/%{project}) = %{version}
Obsoletes:      php-lukasreschke-%{project} < %{version}

%description
ID3Parser is a pure ID3 parser based upon getID3. This library takes the ID3
parsing code from getID3 and strips all other functions.

Autoloader: %{_datadir}/php/%{ns_dir}/autoload.php


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
        class_exists('%{ns_project}\ID3Parser')
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
%dir %{_datadir}/php/%{ns_vendor}
%{_datadir}/php/%{ns_dir}


#-- CHANGELOG -----------------------------------------------------------------#
%changelog
%autochangelog
