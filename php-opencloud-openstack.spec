# This package depends on automagic byte compilation
# https://fedoraproject.org/wiki/Changes/No_more_automagic_Python_bytecompilation_phase_2
%global _py_byte_compile %nil

#
# Fedora spec file for php-opencloud-openstack
#
# Copyright (c) 2013-2017 Gregor Tätzner <brummbq@fedoraproject.org>
#                         Shawn Iwinski <shawn.iwinski@gmail.com>
#                         Christian Glombek <lorbus@fedoraproject.org>
#
# License: MIT
# http://opensource.org/licenses/MIT
#
# Please preserve changelog entries
#

%global github_owner   php-opencloud
%global github_name    openstack
%global github_version 3.0.7
%global github_commit  5d73ff577731fc473448c489acfca9730aa39c88

%global composer_vendor  php-opencloud
%global composer_project openstack

# "php" : "~7.0"
%global php_min_ver 7.0
# "guzzlehttp/http" : "^6.1"
%global guzzle_min_ver 6.1
%global guzzle_max_ver 7
# "justinrainbow/json-schema": "^5.2"
%global json_schema_min_ver 5.2
%global json_schema_max_ver 6

# Build using "--without tests" to disable tests
%global with_tests 0%{!?_without_tests:1}

%global with_docs 0

%{!?phpdir:  %global phpdir  %{_datadir}/php}

Name:           php-opencloud-openstack
Version:        %{github_version}
Release:        13%{?github_release}%{?dist}
Summary:        PHP SDK for OpenStack clouds

License:        ASL 2.0
URL:            https://php-openstack-sdk.readthedocs.io/
Source0:        https://github.com/%{github_owner}/%{github_name}/archive/%{github_commit}/%{name}-%{github_version}-%{github_commit}.tar.gz

BuildArch:      noarch

# Docs
%if %{with_docs}
BuildRequires:  python3dist(sphinx)
BuildRequires:  python3dist(sphinxcontrib-phpdomain)
BuildRequires:  fontawesome-fonts
Requires:       fontawesome-fonts
BuildRequires:  fontawesome-fonts-web
Requires:       fontawesome-fonts-web
BuildRequires:  lato-fonts
Requires:       lato-fonts
BuildRequires:  google-roboto-slab-fonts
Requires:       google-roboto-slab-fonts
%if 0%{?fedora} >= 29
BuildRequires:  levien-inconsolata-fonts
Requires:       levien-inconsolata-fonts
%endif
%endif

# Tests
%if %{with_tests}
## composer.json
BuildRequires:  php(language) >= %{php_min_ver}
BuildRequires: (php-guzzlehttp-guzzle6 >= %{guzzle_min_ver} with php-guzzlehttp-guzzle6 < %{guzzle_max_ver})
BuildRequires: (php-justinrainbow-json-schema5 >= %{json_schema_min_ver} with php-justinrainbow-json-schema5 < %{json_schema_max_ver})
BuildRequires:  phpunit7
## Autoloader
BuildRequires:  php-fedora-autoloader
%endif

# composer.json
Requires:       php(language) >= %{php_min_ver}
Requires:      (php-guzzlehttp-guzzle6 >= %{guzzle_min_ver} with php-guzzlehttp-guzzle6 < %{guzzle_max_ver})
Requires:      (php-justinrainbow-json-schema5 >= %{json_schema_min_ver} with php-justinrainbow-json-schema5 < %{json_schema_max_ver})
# Autoloader
Requires:       php-fedora-autoloader

# Composer
Provides:       php-composer(%{composer_vendor}/%{composer_project}) = %{version}

%description
php-opencloud/openstack is an SDK which allows PHP developers to easily connect
to OpenStack APIs in a simple and idiomatic way. This binding is specifically
designed for OpenStack APIs, but other provider SDKs are available. Multiple
OpenStack services, and versions of services, are supported.

Autoloader: %{phpdir}/OpenStack/autoload.php


%if %{with_docs}
%package doc
Summary: Documentation for PHP SDK for OpenStack clouds


%description doc
Documentation for PHP SDK for OpenStack clouds
%endif

%prep
%setup -qn %{github_name}-%{github_commit}


%build
%if %{with_docs}
# Generate html docs
PYTHONPATH=${PWD} sphinx-build-3 doc html
# Remove the sphinx-build leftovers
rm -rf html/.{doctrees,buildinfo}
# Unbundle fonts
pushd html/_static/fonts/
for file in FontAwesome*; do
    rm -f $file
    ln -s /usr/share/fonts/fontawesome/$file $file
done
for file in fontawesome*; do
    rm -f $file
    ln -s /usr/share/fonts/fontawesome/$file $file
done
for file in Lato*; do
    rm -f $file
    ln -s /usr/share/fonts/lato/$file $file
done
for file in RobotoSlab*; do
    rm -f $file
    ln -s /usr/share/fonts/google-roboto-slab/$file $file
done
%if 0%{?fedora} >= 29
for file in Inconsolata*; do
    rm -f $file
    ln -s /usr/share/fonts/levien-inconsolata/$file $file
done
%endif
popd
%endif

: Create autoloader
cat <<'AUTOLOAD' | tee src/autoload.php
<?php
/**
 * Autoloader for %{name} and its' dependencies
 * (created by %{name}-%{version}-%{release}).
 */
require_once '%{phpdir}/Fedora/Autoloader/autoload.php';

\Fedora\Autoloader\Autoload::addPsr4('OpenStack\\', __DIR__);

\Fedora\Autoloader\Dependencies::required(array(
    '%{phpdir}/GuzzleHttp6/autoload.php',
    '%{phpdir}/JsonSchema5/autoload.php',
));
AUTOLOAD


%install
mkdir -p %{buildroot}%{phpdir}/OpenStack
cp -pr src/* %{buildroot}%{phpdir}/OpenStack/


%check
%if %{with_tests}
: Create mock Composer autoloader
mkdir vendor
cat <<'AUTOLOAD' | tee vendor/autoload.php
<?php
require '%{buildroot}%{phpdir}/OpenStack/autoload.php';

\Fedora\Autoloader\Autoload::addPsr4('OpenStack\\Test\\', __DIR__.'/../tests/unit');
\Fedora\Autoloader\Autoload::addPsr4('OpenStack\\Integration\\', __DIR__.'/../tests/integration/');
AUTOLOAD

# Skip test_it_chunks_according_to_provided_segment_size
# failing in Guzzle v6 (TODO remove in 3.1 using Guzzle v7)

: Upstream tests
$cmd %{_bindir}/phpunit7 \
  --filter '^((?!(test_it_chunks_according_to_provided_segment_size)).)*$' \
  --verbose
%else
: Tests skipped
%endif


%files
%{!?_licensedir:%global license %%doc}
%license LICENSE
%doc *.md
%doc composer.json
%{phpdir}/OpenStack


%if %{with_docs}
%files doc
%doc doc
%doc samples
%endif


%changelog
* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.7-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.7-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.7-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.7-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.7-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.7-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.7-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jun 30 2021 Christopher Engelhard <remi@remirepo.net> - 3.0.7-6
- disable -doc subpackage since this is incompatible with Sphinx 4.x.
  Fixes RHBZ 1977297

* Wed Mar 24 2021 Remi Collet <remi@remirepo.net> - 3.0.7-5
- switch to phpunit7
- ignore 1 failing test

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.7-3
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Feb 07 2020 Christian Glombek <lorbus@fedoraproject.org> - 3.0.7-1
- Update to version 3.0.7

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Jul 28 2019 Christian Glombek <lorbus@fedoraproject.org> - 3.0.6-1
- Update to version 3.0.6

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sun Jul 01 2018 Christian Glombek <lorbus@fedoraproject.org> - 3.0.5-1
- Update to version 3.0.5
- Rename to php-opencloud-openstack

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.16.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Nov  2 2017 Remi Collet <remi@remimrepo.net> - 1.16.0-4
- fix FTBFS from Koschei, add patch for PHP 7.2 from
  https://github.com/mikemccabe/json-patch-php/pull/17

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.16.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon May 29 2017 Shawn Iwinski <shawn.iwinski@gmail.com> - 1.16.0-2
- Fix autoloader dependency

* Sun Feb 26 2017 Shawn Iwinski <shawn.iwinski@gmail.com> - 1.16.0-1
- Update to 1.16.0 (RHBZ #1312624)
- Fix FTBFS (skip tests known to fail)
- Add bundled dependency php-composer(mikemccabe/json-patch-php)
- Use php-composer(fedora/autoloader)

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.12.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sat Mar 26 2016 Shawn Iwinski <shawn.iwinski@gmail.com> - 1.12.2-1
- Updated to 1.12.2
- Updated URL
- Updated dependencies to use php-composer(*)
- Added autoloader (and bumped dependency versions for their autoloaders)

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.12.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.12.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Jan 02 2015 Shawn Iwinski <shawn.iwinski@gmail.com> - 1.12.1-1
- Updated to 1.12.1 (BZ #1172637)
- Added php-composer(rackspace/php-opencloud) virtual provide

* Sat Nov 22 2014 Shawn Iwinski <shawn.iwinski@gmail.com> - 1.11.0-3
- Removed obsolete of php-cloudfiles

* Sun Nov 02 2014 Shawn Iwinski <shawn.iwinski@gmail.com> - 1.11.0-2
- No BuildRequires unless with tests

* Sun Nov 02 2014 Shawn Iwinski <shawn.iwinski@gmail.com> - 1.11.0-1
- Updated to 1.11.0 (BZ #1159522)
- Spec cleanup

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu Jan 30 2014 Gregor Tätzner <brummbq@fedoraproject.org> - 1.6.0-4
- obsolete php-cloudfiles

* Sat Jan 25 2014 Gregor Tätzner <brummbq@fedoraproject.org> - 1.6.0-3
- use commit revision in source url

* Fri Jan 03 2014 Gregor Tätzner <brummbq@fedoraproject.org> - 1.6.0-2
- move lib to psr-0 compliant location
- drop autoloader

* Tue Dec 31 2013 Gregor Tätzner <brummbq@fedoraproject.org> - 1.6.0-1
- initial packaging
