# fedora spec file for php-fgrosse-phpasn1
#
# Copyright (c) 2020 Christopher Engelhard
# License: MIT
#
# Please preserve the changelog entries

# package and composer name
%global vendor      fgrosse
%global project     phpasn1

# PHP namespace and directory
%global ns_project  FG
%global ns_dir      %( echo "%{ns_project}" | sed  's|\\\\|\/|g' )

# Github
%global gh_vendor   FGrosse
%global gh_project  PHPASN1
%global commit      20299033c35f4300eb656e7e8e88cf52d1d6694e
%global scommit     %(c=%{commit}; echo ${c:0:7})

# tests
%bcond_without tests

#-- PREAMBLE ------------------------------------------------------------------#
Name:           php-%{vendor}-%{project}
Version:        2.3.0
Release:        %autorelease
Summary:        A PHP Framework that allows you to encode and decode arbitrary ASN.1 structures

License:        MIT
URL:            https://github.com/%{gh_vendor}/%{gh_project}
# Since github tarballs are lacking the tests, source is created via a local git checkout instead.
# Use ./makesrc.sh in the same directory as the specfile to generate the source archive
Source0:        %{name}-%{version}-%{scommit}.tgz
Source1:        makesrc.sh

# fixes missing function type declaration for use with phpunit8
# https://github.com/fgrosse/PHPASN1/pull/85
Patch1:         0001-fix-tests-for-php8.patch
# modifies some tests to work on 32bit systems
# https://github.com/fgrosse/PHPASN1/issues/84
Patch2:         0002-fix-tests-for-32bit.patch

BuildArch:      noarch

# for the autoloader
Requires:       php-composer(fedora/autoloader)

# from composer.json
Requires:       php(language) >= 7.0
Requires:       (php-gmp or php-bcmath)
Recommends:     php-curl

# from phpcompatinfo
Requires:       php-date
Requires:       php-pcre
Requires:       php-spl

# for autoloader check
BuildRequires:  php-composer(fedora/autoloader)
BuildRequires:  %{_bindir}/php
BuildRequires:  php(language) >= 7.0

%if %{with tests}
# for tests
BuildRequires: phpunit8
BuildRequires: php-date
BuildRequires: php-pcre
BuildRequires: php-spl
BuildRequires: php-gmp
BuildRequires: php-bcmath
%endif

# composer provides
Provides:       php-composer(%{vendor}/%{project}) = %{version}

%description
A PHP Framework that allows you to encode and decode arbitrary ASN.1 structures
using the ITU-T X.690 Encoding Rules. This encoding is very frequently used in
X.509 PKI environments or the communication between heterogeneous computer
systems.

The API allows you to encode ASN.1 structures to create binary data such as
certificate signing requests (CSR), X.509 certificates or certificate
revocation lists (CRL). PHPASN1 can also read BER encoded binary data into
separate PHP objects that can be manipulated by the user and re-encoded
afterwards.

The library autoloader is: %{_datadir}/php/%{ns_dir}/autoload.php


#-- PREP, BUILD & INSTALL -----------------------------------------------------#
%prep
%autosetup -p1 -n %{gh_project}-%{commit}

%build
: Nothing to build.

%install
: Create installation directory
mkdir -p   %{buildroot}%{_datadir}/php/%{ns_dir}
cp -pr lib/* %{buildroot}%{_datadir}/php/%{ns_dir}

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
        class_exists('%{ns_project}\ASN1\Universal\Integer')
        ? 0 : 1
    );
"
%if %{with tests}
: Create a autoloader for tests
mkdir vendor
cat << 'EOF' | tee vendor/autoload.php
<?php
require_once '%{buildroot}%{_datadir}/php/%{ns_dir}/autoload.php';
\Fedora\Autoloader\Autoload::addPsr4('%{ns_project}\Test', dirname(__DIR__).'/tests');
EOF

: Run phpunit tests
%{_bindir}/phpunit8 --verbose
%endif

#-- FILES ---------------------------------------------------------------------#
%files
%license LICENSE
%doc composer.json
%doc *.md
%{_datadir}/php/%{ns_dir}


#-- CHANGELOG -----------------------------------------------------------------#
%changelog
%autochangelog
