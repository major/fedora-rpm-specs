# remirepo/fedora spec file for php-nrk-Predis
#
# Copyright (c) 2013-2022 Remi Collet
# License: CC-BY-SA
# http://creativecommons.org/licenses/by-sa/4.0/
#
# Please, preserve the changelog entries
#

%if 0%{?fedora} >= 31 || 0%{?rhel} >= 8
%bcond_without  tests
%else
%bcond_with     tests
%endif

%global gh_owner     nrk
%global gh_project   predis
%global gh_commit    a2fb02d738bedadcffdbb07efa3a5e7bd57f8d6e
%global gh_short     %(c=%{gh_commit}; echo ${c:0:7})

%global ns_project   Predis

%global pear_name    Predis
%global pear_channel pear.nrk.io

Name:           php-nrk-Predis
Version:        1.1.10
Release:        3%{?dist}
Summary:        PHP client library for Redis

License:        MIT
URL:            https://github.com/%{gh_owner}/%{gh_project}
Source0:        %{name}-%{version}-%{gh_short}.tgz
Source1:        makesrc.sh

BuildArch:      noarch
BuildRequires:  php(language) >= 5.3.9
%if %{with tests}
BuildRequires:  php-phpunit-PHPUnit
BuildRequires:  redis
%endif

Requires:       php(language) >= 5.3.9
Requires:       php-reflection
Requires:       php-filter
Requires:       php-pcre
Requires:       php-session
Requires:       php-sockets
Requires:       php-spl
%if 0%{?fedora} >= 30 || 0%{?rhel} >=8
Recommends:     php-curl
Recommends:     php-phpiredis
%endif

Provides:       php-pear(%{pear_channel}/%{pear_name}) = %{version}
Provides:       php-composer(predis/predis) = %{version}

# This pkg was the only one in this channel so the channel is no longer needed
Obsoletes:     php-channel-nrk < 1.4


%description
Flexible and feature-complete PHP client library for Redis.


%prep
%setup -q -n %{gh_project}-%{gh_commit}


%build
: nothing

%install
mkdir -p   %{buildroot}%{_datadir}/php/
cp -pr src %{buildroot}%{_datadir}/php/%{ns_project}

# for compatibility with PEAR installation
mkdir -p   %{buildroot}%{_datadir}/pear/%{ns_project}
ln -s ../../php/Predis/Autoloader.php %{buildroot}%{_datadir}/pear/%{ns_project}/Autoloader.php


%check
%if %{with tests}
: Launch redis server
port=$(expr 6379 + %{?fedora}%{?rhel})
pidfile=$PWD/redis.pid
mkdir -p data
redis-server                   \
    --bind      127.0.0.1      \
    --port      $port          \
    --daemonize yes            \
    --logfile   $PWD/redis.log \
    --dir       $PWD/data      \
    --pidfile   $pidfile

: Run the installed test Suite against the installed library
sed -e "s/6379/$port/" phpunit.xml.dist > phpunit.xml
sed -e "/expectedExceptionMessageRegExp/s/6379/$port/" -i tests/PHPUnit/PredisConnectionTestCase.php

# testHandlesBinaryData failing with 8.1
# see https://github.com/predis/predis/issues/733
ret=0
php -d memory_limit=1G %{_bindir}/phpunit \
    --include-path=%{buildroot}%{_datadir}/pear \
    --filter '^((?!(testHandlesBinaryData|testThrowsExceptionWhenSettingUnknownConfiguration|testReturnsCommandInfoOnExistingCommand)).)*$' \
    --verbose || ret=1

: Cleanup
if [ -f $pidfile ]; then
   kill $(cat $pidfile)
fi

exit $ret
%else
: Test disabled
%endif


%pre
if [ -x %{_bindir}/pear ]; then
   %{_bindir}/pear uninstall --nodeps --ignore-errors --register-only \
      %{pear_channel}/%{pear_name} >/dev/null || :
fi


%files
%license LICENSE
%doc composer.json
%doc *md
%doc examples
%{_datadir}/php/%{ns_project}
%{_datadir}/pear/%{ns_project}


%changelog
* Thu Aug 11 2022 Remi Collet <remi@remirepo.net> - 1.1.10-3
- skip 2 more tests, FTBFS #2113590

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.10-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jan  6 2022 Remi Collet <remi@remirepo.net> - 1.1.10-1
- update to 1.1.10

* Wed Oct  6 2021 Remi Collet <remi@remirepo.net> - 1.1.9-1
- update to 1.1.9

* Thu Sep 30 2021 Remi Collet <remi@remirepo.net> - 1.1.8-1
- update to 1.1.8

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Apr  6 2021 Remi Collet <remi@remirepo.net> - 1.1.7-1
- update to 1.1.7
- drop patch merged upstream

* Thu Mar 18 2021 Remi Collet <remi@remirepo.net> - 1.1.6-3
- fix test failure with redis 6.2 using patch from
  https://github.com/predis/predis/pull/686

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Sep 12 2020 Remi Collet <remi@remirepo.net> - 1.1.6-1
- update to 1.1.6

* Fri Sep 11 2020 Remi Collet <remi@remirepo.net> - 1.1.5-1
- update to 1.1.5

* Mon Aug 31 2020 Remi Collet <remi@remirepo.net> - 1.1.4-1
- update to 1.1.4

* Wed Aug 19 2020 Remi Collet <remi@remirepo.net> - 1.1.3-1
- update to 1.1.3 (no change)

* Wed Aug 12 2020 Remi Collet <remi@remirepo.net> - 1.1.2-1
- update to 1.1.2
- sources from git snapshot
- obsolete php-channel-nrk
- drop dependency on pear
- move to /usr/share/php with autoloader link for BC

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-11
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Feb 13 2018 Remi Collet <remi@remirepo.net> - 1.1.1-5
- fix FTBFS from Koschei with patch from
  https://github.com/nrk/predis/pull/486

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Nov 17 2016 Remi Collet <remi@fedoraproject.org> - 1.1.1-2
- fix bootstraping to redis server for test suite
- add patch for PHP 7.1
- open https://github.com/nrk/predis/pull/393

* Fri Jun 17 2016 Remi Collet <remi@fedoraproject.org> - 1.1.1-1
- Update to 1.1.1

* Tue Jun 07 2016 Remi Collet <remi@fedoraproject.org> - 1.1.0-1
- Update to 1.1.0

* Tue May 31 2016 Remi Collet <remi@fedoraproject.org> - 1.0.4-1
- Update to 1.0.4

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Dec 28 2015 Remi Collet <remi@fedoraproject.org> - 1.0.3-2
- fix FTBFS detected by Koschei since redis 3.0.6
  open https://github.com/nrk/predis/pull/296

* Fri Jul 31 2015 Remi Collet <remi@fedoraproject.org> - 1.0.3-1
- Update to 1.0.3

* Thu Jul 30 2015 Remi Collet <remi@fedoraproject.org> - 1.0.2-1
- Update to 1.0.2

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Jan 02 2015 Remi Collet <remi@fedoraproject.org> - 1.0.1-1
- Update to 1.0.1

* Fri Nov 07 2014 Remi Collet <remi@fedoraproject.org> - 1.0.0-2
- (re)enable test suite with redis 2.8.x
- add upstream patch for test suite on 32bits

* Mon Nov 03 2014 Remi Collet <remi@fedoraproject.org> - 1.0.0-1
- Update to 1.0.0
- upstream patch for tests
- open https://github.com/nrk/predis/issues/220 - failed tests
  on slow / 32bits computer

* Wed Jul 16 2014 Remi Collet <remi@fedoraproject.org> - 0.8.6-1
- Update to 0.8.6
- provides php-composer(predis/predis)

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu Jan 16 2014 Remi Collet <remi@fedoraproject.org> - 0.8.5-1
- Update to 0.8.5 (stable)
- don't run tests (need latest redis server)

* Sun Jul 28 2013 Remi Collet <remi@fedoraproject.org> - 0.8.4-1
- Update to 0.8.4

* Wed Jul  3 2013 Remi Collet <remi@fedoraproject.org> - 0.8.3-2
- fixed sources, https://github.com/nrk/predis/issues/125

* Wed Jun  5 2013 Remi Collet <remi@fedoraproject.org> - 0.8.3-1
- initial package
