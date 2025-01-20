# remirepo/fedora spec file for php-sabre-dav4
#
# Copyright (c) 2013-2024 Remi Collet
# License: CC-BY-SA
# http://creativecommons.org/licenses/by-sa/4.0/
#
# Please, preserve the changelog entries
#

%bcond_without       tests

# Github
%global gh_commit    074373bcd689a30bcf5aaa6bbb20a3395964ce7a
%global gh_short     %(c=%{gh_commit}; echo ${c:0:7})
%global gh_owner     sabre-io
%global gh_project   dav
# Packagist
%global pk_vendor    sabre
%global pk_project   %{gh_project}
# Namespace
%global ns_vendor    Sabre
%global ns_project   DAV
%global major        4

Name:           php-%{pk_vendor}-%{pk_project}%{major}
Summary:        WebDAV Framework for PHP
Version:        4.7.0
Release:        2%{?dist}

URL:            https://github.com/%{gh_owner}/%{gh_project}
# sabre is BSD
# assets/openiconic is MIT
License:        BSD-3-Clause AND MIT
Source0:        %{name}-%{version}-%{gh_short}.tgz
# git snapshot to retrieve tests
Source1:        makesrc.sh

# replace composer autoloader
Patch0:         %{name}-autoload.patch

BuildArch:      noarch
%if %{with tests}
BuildRequires:  php(language) >= 7.1
BuildRequires: (php-composer(sabre/vobject)   >= 4.2.1  with php-composer(sabre/vobject)  < 5)
BuildRequires: (php-composer(sabre/event)     >= 5.0    with php-composer(sabre/event)    < 6)
BuildRequires: (php-composer(sabre/xml)       >= 2.0.1  with php-composer(sabre/xml)      < 3)
BuildRequires: (php-composer(sabre/http)      >= 5.0.5  with php-composer(sabre/http)     < 6)
BuildRequires: (php-composer(sabre/uri)       >= 2.0    with php-composer(sabre/uri)      < 3)
BuildRequires: (php-composer(psr/log)         >= 1.0.1  with php-composer(psr/log)        < 4)
BuildRequires: (php-composer(monolog/monolog) >= 1.27 with php-composer(monolog/monolog)  < 3)
BuildRequires:  php-dom
BuildRequires:  php-pcre
BuildRequires:  php-spl
BuildRequires:  php-simplexml
BuildRequires:  php-mbstring
BuildRequires:  php-ctype
BuildRequires:  php-date
BuildRequires:  php-iconv
BuildRequires:  php-libxml
BuildRequires:  php-curl
BuildRequires:  php-pdo
BuildRequires:  php-json
# From composer.json, "require-dev" : {
#        "friendsofphp/php-cs-fixer": "^2.19",
#        "monolog/monolog": "^1.27 || ^2.0",
#        "phpstan/phpstan": "^0.12 || ^1.0",
#        "phpstan/phpstan-phpunit": "^1.0",
#        "phpunit/phpunit": "^7.5 || ^8.5 || ^9.6"
BuildRequires:  phpunit9 >= 9.6
%global phpunit %{_bindir}/phpunit9
%endif
# Autoloader
BuildRequires:  php-fedora-autoloader-devel
BuildRequires:  php-pdo_sqlite

# From composer.json,    "require": {
#        "php": ">=7.1.0 || ^8.0",
#        "sabre/vobject": "^4.2.1",
#        "sabre/event" : "^5.0",
#        "sabre/xml"  : "^2.0.1",
#        "sabre/http" : "^5.0.5",
#        "sabre/uri" : "^2.0",
#        "ext-dom": "*",
#        "ext-pcre": "*",
#        "ext-spl": "*",
#        "ext-simplexml": "*",
#        "ext-mbstring" : "*",
#        "ext-ctype" : "*",
#        "ext-date" : "*",
#        "ext-iconv" : "*",
#        "lib-libxml" : ">=2.7.0",
#        "psr/log": "^1.0 || ^2.0 || ^3.0",
#        "ext-json": "*"
Requires:       php(language) >= 7.1
Requires:      (php-composer(sabre/vobject) >= 4.2.1  with php-composer(sabre/vobject) < 5)
Requires:      (php-composer(sabre/event)   >= 5.0    with php-composer(sabre/event)   < 6)
Requires:      (php-composer(sabre/xml)     >= 2.0.1  with php-composer(sabre/xml)     < 3)
Requires:      (php-composer(sabre/http)    >= 5.0.5  with php-composer(sabre/http)    < 6)
Requires:      (php-composer(sabre/uri)     >= 2.0    with php-composer(sabre/uri)     < 3)
Requires:      (php-composer(psr/log)       >= 1.0.1  with php-composer(psr/log)       < 4)
Requires:       php-dom
Requires:       php-pcre
Requires:       php-spl
Requires:       php-simplexml
Requires:       php-mbstring
Requires:       php-ctype
Requires:       php-date
Requires:       php-iconv
Requires:       php-libxml
Requires:       php-json
# From composer.json, "suggest" : {
#        "ext-curl" : "*",
#        "ext-pdo" : "*",
#        "ext-imap": "*"
Recommends:     php-curl
Recommends:     php-pdo
Recommends:     php-imap
# Autoloader
Requires:       php-composer(fedora/autoloader)

Provides:       php-composer(%{pk_vendor}/%{pk_project}) = %{version}


%description
What is SabreDAV

SabreDAV allows you to easily add WebDAV support to a PHP application.
SabreDAV is meant to cover the entire standard, and attempts to allow
integration using an easy to understand API.

Feature list:
* Fully WebDAV compliant
* Supports Windows XP, Windows Vista, Mac OS/X, DavFSv2, Cadaver, Netdrive,
  Open Office, and probably more.
* Passing all Litmus tests.
* Supporting class 1, 2 and 3 Webdav servers.
* Locking support.
* Custom property support.
* CalDAV (tested with Evolution, iCal, iPhone and Lightning).
* CardDAV (tested with OS/X addressbook, the iOS addressbook and Evolution).
* Over 97% unittest code coverage.

Autoloader: %{_datadir}/php/%{ns_vendor}/%{ns_project}%{major}/autoload.php


%prep
%setup -q -n %{gh_project}-%{gh_commit}
mv lib/DAV/Browser/assets/openiconic/ICON-LICENSE .

%patch -P0 -p1 -b .rpm

: relocate
for dir in CalDAV CardDAV DAV DAVACL; do
    mv lib/${dir} lib/${dir}%{major}
done

: autoloader
phpab -t fedora -o lib/%{ns_project}%{major}/autoload.php lib
cat << 'EOF' | tee -a lib/%{ns_project}%{major}/autoload.php

// Dependencies
\Fedora\Autoloader\Dependencies::required([
    '%{_datadir}/php/%{ns_vendor}/Event5/autoload.php',
    '%{_datadir}/php/%{ns_vendor}/Xml2/autoload.php',
    '%{_datadir}/php/%{ns_vendor}/Uri2/autoload.php',
    '%{_datadir}/php/%{ns_vendor}/HTTP5/autoload.php',
    '%{_datadir}/php/%{ns_vendor}/VObject4/autoload.php',
    [
        '%{_datadir}/php/Psr/Log3/autoload.php',
        '%{_datadir}/php/Psr/Log2/autoload.php',
        '%{_datadir}/php/Psr/Log/autoload.php',
    ],
]);
EOF

# drop executable as only provided as doc
chmod -x bin/*


%build
# nothing to build


%install
# Install as a PSR-0 library
mkdir -p   %{buildroot}%{_datadir}/php/
cp -pr lib %{buildroot}%{_datadir}/php/%{ns_vendor}


%check
%if %{with tests}
: Fix bootstrap
cd tests
sed -e 's:@BUILDROOT@:%{buildroot}:' -i bootstrap.php

: Run upstream test suite against installed library
ret=0
for cmdarg in "php %{phpunit}" php81 php82 php83 php84; do
  if which $cmdarg; then
    set $cmdarg
    for ts in sabre-dav sabre-davacl sabre-caldav sabre-carddav; do
      $1 ${2:-%{_bindir}/phpunit9} \
        --testsuite $ts || ret=1
    done
  fi
done
exit $ret
%else
: Skip upstream test suite
%endif


%files
%license *LICENSE
%doc *md
%doc composer.json
%doc examples bin
%{_datadir}/php/%{ns_vendor}/DAV%{major}
%{_datadir}/php/%{ns_vendor}/DAVACL%{major}
%{_datadir}/php/%{ns_vendor}/CalDAV%{major}
%{_datadir}/php/%{ns_vendor}/CardDAV%{major}


%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 4.7.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Tue Oct 29 2024 Remi Collet <remi@remirepo.net> - 4.7.0-1
- update to 4.7.0

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.6.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Mon Jan 29 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.6.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.6.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.6.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Dec 11 2023 Remi Collet <remi@remirepo.net> - 4.6.0-1
- update to 4.6.0

* Thu Nov 23 2023 Remi Collet <remi@remirepo.net> - 4.5.1-1
- update to 4.5.1

* Tue Nov 14 2023 Remi Collet <remi@remirepo.net> - 4.5.0-1
- update to 4.5.0

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 4.4.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 4.4.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 27 2022 Remi Collet <remi@remirepo.net> - 4.4.0-1
- update to 4.4.0

* Fri Jan 21 2022 Remi Collet <remi@remirepo.net> - 4.3.1-1
- update to 4.3.1

* Tue Dec 14 2021 Remi Collet <remi@remirepo.net> - 4.3.0-1
- update to 4.3.0

* Thu Dec  9 2021 Remi Collet <remi@remirepo.net> - 4.2.3-1
- update to 4.2.3

* Thu Dec  9 2021 Remi Collet <remi@remirepo.net> - 4.2.2-1
- update to 4.2.2
- allow psr/log v2 and v3

* Tue Nov 30 2021 Remi Collet <remi@remirepo.net> - 4.2.1-1
- update to 4.2.1

* Wed Nov 17 2021 Remi Collet <remi@remirepo.net> - 4.2.0-1
- update to 4.2.0

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon Feb 15 2021 Remi Collet <remi@remirepo.net> - 4.1.5-1
- update to 4.1.5

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jan 12 2021 Remi Collet <remi@remirepo.net> - 4.1.4-1
- update to 4.1.4
- sources from git snapshot

* Mon Nov  9 2020 Remi Collet <remi@remirepo.net> - 4.1.3-1
- update to 4.1.3

* Mon Oct  5 2020 Remi Collet <remi@remirepo.net> - 4.1.2-1
- update to 4.1.2
- switch to phpunit9

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 14 2020 Remi Collet <remi@remirepo.net> - 4.1.1-1
- update to 4.1.1

* Fri Mar 20 2020 Remi Collet <remi@remirepo.net> - 4.1.0-1
- update to 4.1.0
- raise dependency on PHP 7.1
- raise dependency on sabre/vobject 4.2.1
- raise dependency on sabre/http 5.0.5
- switch to phpunit7

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jan 10 2020 Remi Collet <remi@remirepo.net> - 4.0.3-1
- update to 4.0.3

* Mon Oct 21 2019 Remi Collet <remi@remirepo.net> - 4.0.2-1
- update to 4.0.2
- drop patch merged upstream

* Tue Aug 20 2019 Remi Collet <remi@remirepo.net> - 4.0.1-2
- update to 4.0.1
- add patch for 7.4 from
  https://github.com/sabre-io/dav/pull/1187

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Jul 15 2019 Remi Collet <remi@remirepo.net> - 4.0.0-2
- fix LICENSE for assets/openiconic

* Fri Jul  5 2019 Remi Collet <remi@remirepo.net> - 4.0.0-1
- update to 4.0.0
- rename to php-sabre-dav4
- move to /usr/share/php/Sabre/DAV4
- raise dependency on PHP 7
- raise dependency on sabre/vobject 4.2.0
- raise dependency on sabre/event 5.0
- raise dependency on sabre/xml 2.0.1
- raise dependency on sabre/http 5.0
- raise dependency on sabre/uri 2.0
- switch to classmap autoloader

* Mon Jul  1 2019 Remi Collet <remi@remirepo.net> - 3.2.3-3
- change autoloader order to ensure same versions are used

* Wed Jan  9 2019 Remi Collet <remi@remirepo.net> - 3.2.3-1
- update to 3.2.3

* Mon Oct 15 2018 Remi Collet <remi@remirepo.net> - 3.2.2-7
- add upstream patch for PHP 7.3

* Tue Jun  5 2018 Remi Collet <remi@remirepo.net> - 3.2.2-5
- use range dependencies on F27+
- ignore 1 test failing with sabre/http 4.2.4
- fix project URL

* Fri Oct  6 2017 Remi Collet <remi@remirepo.net> - 3.2.2-3
- add patch for PHP 7.2 from https://github.com/fruux/sabre-dav/pull/1006

* Wed Feb 15 2017 Remi Collet <remi@fedoraproject.org> - 3.2.2-1
- update to 3.2.2

* Sun Jan 29 2017 Remi Collet <remi@fedoraproject.org> - 3.2.1-1
- update to 3.2.1

* Tue Jan 17 2017 Remi Collet <remi@fedoraproject.org> - 3.2.0-1
- update to 3.2.0
- raise dependency on PHP version 5.5
- raise dependency on sabre/vobject version 4.1
- raise dependency on sabre/xml version 1.4
- raise dependency on sabre/http version 4.2.1
- raise dependency on sabre/uri version 1.0.1
- add dependency on psr/log

* Wed Nov 23 2016 Remi Collet <remi@fedoraproject.org> - 3.0.9-3
- add upstream patch to fix FTBFS with php 7.1

* Sat Oct 29 2016 Remi Collet <remi@fedoraproject.org> - 3.0.9-2
- switch from symfony/class-loader to fedora/autoloader

* Thu Apr  7 2016 Remi Collet <remi@fedoraproject.org> - 3.0.9-1
- update to 3.0.9
- add dependency on sabre/xml
- add dependency on sabre/uri
- raise dependency on sabre/http >= 4

* Tue Mar 22 2016 Remi Collet <remi@fedoraproject.org> - 2.1.10-1
- update to 2.1.10

* Mon Mar 21 2016 Remi Collet <remi@fedoraproject.org> - 2.1.6-2
- provide missing php-composer(sabre/dav)

* Wed Feb 24 2016 James Hogarth <james.hogarth@gmail.com> - 2.1.6-1
- update to 2.1.6

* Wed Feb 24 2016 Remi Collet <remi@fedoraproject.org> - 2.1.5-1
- update to 2.1.5

* Fri Mar 06 2015 Adam Williamson <awilliam@redhat.com> - 1.8.12-1
- update to 1.8.12 (bugfix release, no bc breaks)

* Thu May 22 2014 Remi Collet <remi@fedoraproject.org> - 1.8.10-1
- update to 1.8.10

* Sun Mar  2 2014 Remi Collet <remi@fedoraproject.org> - 1.8.9-1
- update to 1.8.9

* Thu Feb 20 2014 Remi Collet <remi@fedoraproject.org> - 1.8.8-2
- drop max version for VObject

* Tue Feb 11 2014 Remi Collet <remi@fedoraproject.org> - 1.8.8-1
- update to 1.8.8

* Tue Dec 31 2013 Remi Collet <remi@fedoraproject.org> - 1.8.7-1
- Initial packaging
