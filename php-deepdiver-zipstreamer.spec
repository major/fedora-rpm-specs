# fedora spec file for php-deepdiver-zipstreamer
#
# Copyright (c) 2020 Christopher Engelhard
# License: MIT
#
# Please preserve the changelog entries

# package and composer name
%global vendor      deepdiver
%global project     zipstreamer

# PHP namespace and directory
%global ns_project  ZipStreamer
%global ns_dir      %( echo "%{ns_project}" | sed  's|\\\\|\/|g' )

# Github
%global gh_vendor   DeepDiver1975
%global gh_project  PHPZipStreamer
%global commit      b8c59647ff34fb97e8937aefb2a65de2bc4b4755
%global scommit     %(c=%{commit}; echo ${c:0:7})

# tests
%global with_tests 1

#-- PREAMBLE ------------------------------------------------------------------#
Name:           php-%{vendor}-%{project}
Version:        2.0.0
Release:        %autorelease
Summary:        Stream zip files without i/o overhead

License:        GPLv3+
URL:            https://github.com/%{gh_vendor}/%{gh_project}
Source0:        https://github.com/%{gh_vendor}/%{gh_project}/archive/%{commit}/%{gh_project}-%{version}-%{scommit}.tar.gz

BuildArch:      noarch

Patch0:         0001-psr4fixes.patch

# for the autoloader
Requires:       php-composer(fedora/autoloader)
Recommends:     php-pecl(pecl_http)

# from composer.json
Requires:       php(language) >= 5.6

# from phpcompatinfo
Requires:       php-date
Requires:       php-hash
Requires:       php-mbstring
Requires:       php-spl

# for autoloader check
BuildRequires:  php-composer(fedora/autoloader)
BuildRequires:  %{_bindir}/php
BuildRequires:  php(language) >= 5.6

%if 0%{?with_tests}
# for tests
BuildRequires:  php-composer(phpunit/phpunit) >= 5.7
BuildRequires:  php-pecl(pecl_http)
BuildRequires:  php-pecl(Xdebug)
BuildRequires:  php-date
BuildRequires:  php-hash
BuildRequires:  php-mbstring
BuildRequires:  php-spl
%endif

# composer provides
Provides:       php-composer(%{vendor}/%{project}) = %{version}
Obsoletes:      php-mcnetic-zipstreamer < %{version}
Provides:       php-composer(mcnetic/zipstreamer) = %{version}

%description
Simple Class to create zip files on the fly and stream directly to the
HTTP client as the content is added (without using temporary files).

Autoloader: %{_datadir}/php/%{ns_dir}/autoload.php


#-- PREP, BUILD & INSTALL -----------------------------------------------------#
%prep
%autosetup -p1 -n %{gh_project}-%{commit}

%build
: Nothing to build.

%install
: Create a PSR-0 tree
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
%{_bindir}/php -r '
    require_once "%{buildroot}%{_datadir}/php/%{ns_dir}/autoload.php";
    exit(
        class_exists("\\%{ns_project}\\ZipStreamer")
        ? 0 : 1
    );
'

%if 0%{?with_tests}
: Run test suite
%{_bindir}/phpunit --bootstrap \
    %{buildroot}%{_datadir}/php/%{ns_dir}/autoload.php test
%endif

#-- FILES ---------------------------------------------------------------------#
%files
%license COPYING
%doc composer.json
%doc README.md
%doc MANUAL.md
%{_datadir}/php/%{ns_dir}


#-- CHANGELOG -----------------------------------------------------------------#
%changelog
%autochangelog
