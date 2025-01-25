%if 0%{?fedora}
%global distro fedora
%else
%global distro epel
%endif

Name:           nextcloud
Version:        30.0.5
Release:        %autorelease
Summary:        Private file sync and share server
# Automatically converted from old format: AGPLv3+ and MIT and BSD and ASL 2.0 and WTFPL and CC-BY-SA and GPLv3+ and Adobe - review is highly recommended.
License:        AGPL-3.0-or-later AND LicenseRef-Callaway-MIT AND LicenseRef-Callaway-BSD AND Apache-2.0 AND WTFPL AND LicenseRef-Callaway-CC-BY-SA AND GPL-3.0-or-later AND Adobe-2006
URL:            http://nextcloud.com
Source0:        https://download.nextcloud.com/server/releases/%{name}-%{version}.tar.bz2

# basic nextcloud config.php, nextcloud's
# initial setup will fill out other settings appropriately
Source1:        %{name}-config.php
# Systemd timer for background jobs
Source2:       %{name}-systemd-timer.service
Source3:       %{name}-systemd-timer.timer
# httpd config files
Source100:      %{name}-httpd.conf
Source101:      %{name}-access-httpd.conf.avail
Source102:      %{name}-auth-any.inc
Source103:      %{name}-auth-local.inc
Source104:      %{name}-auth-none.inc
Source105:      %{name}-defaults.inc
# nginx/php-fpm  config files
Source200:      %{name}-default-nginx.conf
Source201:      %{name}-conf-nginx.conf
Source202:      %{name}-php-fpm.conf
Source203:      %{name}-php.ini
# packaging notes and doc
Source300:      %{name}-README.fedora
Source301:      %{name}-mysql.txt
Source302:      %{name}-postgresql.txt
Source303:      %{name}-MIGRATION.fedora

# Remove updater version check, we know that updates across more than one
# version are possible
Patch0:         0000-disable-update-version-check.patch
# Add the ability to exclude files we specify from the nextcloud integrity checker
Patch1:         nextcloud-integritycheck-exclusion.patch

BuildArch:      noarch

# Set this to the minimum supported php version Nextcloud will run on
# Exists to prevent accidental building on distros with outdated php's
BuildRequires:  php(language) >= 8.1
BuildRequires:  systemd-rpm-macros
BuildRequires:  sed

# expand pear macros on install
BuildRequires:  php-pear

# Require one webserver and database backend
Requires:       %{name}-webserver = %{version}-%{release}
Requires:       %{name}-database = %{version}-%{release}
Requires:       php-bcmath
# Require php CLI for occ command
Requires:       php-cli
# Core PHP libs/extensions required by OC core
Requires:       php-curl
Requires:       php-dom
Requires:       php-exif
Requires:       php-fileinfo
Requires:       php-filter
Requires:       php-gd
Requires:       php-gmp
Requires:       php-iconv
Requires:       php-intl
Requires:       php-json
Requires:       php-ldap
Requires:       php-mbstring
Requires:       php-openssl
Requires:       php-pcre
Requires:       php-pdo
Requires:       php-pecl-apcu
Requires:       php-pecl-imagick
Requires:       php-pecl-memcached
Requires:       (php-pecl-redis6 or php-pecl-redis5)
Requires:       php-process
Requires:       php-session
Requires:       php-simplexml
Requires:       php-smbclient
Requires:       php-spl
Recommends:     php-sodium
Requires:       php-opcache
Requires:       php-xmlwriter
Requires:       php-zip
# For systemd support during install/uninstall
%{?systemd_requires}
# the CA cert bundle is linked to from the config dir
Requires:       %{_sysconfdir}/pki/tls/certs/ca-bundle.crt

# Bundled composer libraries
# generated with utils/get-bundled-versions.py
# tar xf nextcloud-28.0.6.tar.bz2
# cd nextcloud
# ../utils/get-bundled-versions.py
# many of these can be unbundled
# I think utils/get-composer-requires.py is a tool to check if these are available on Fedora
Provides: bundled(php-composer(christian-riesen/base32)) = 1.6.0
Provides: bundled(php-composer(rullzer/easytotp)) = 0.1.4
Provides: bundled(php-composer(adhocore/cli)) = 1.7.1
Provides: bundled(php-composer(nextcloud/openapi-extractor)) = 1.0.0
Provides: bundled(php-composer(nikic/php-parser)) = 5.1.0
Provides: bundled(php-composer(phpstan/phpdoc-parser)) = 1.29.1
Provides: bundled(php-composer(icewind/smb)) = 3.5.4
Provides: bundled(php-composer(icewind/streams)) = 0.7.7
Provides: bundled(php-composer(bamarni/composer-bin-plugin)) = 1.8.2
Provides: bundled(php-composer(hexogen/kdtree)) = 0.2.6
Provides: bundled(php-composer(amphp/amp)) = 2.6.4
Provides: bundled(php-composer(amphp/byte-stream)) = 1.8.1
Provides: bundled(php-composer(amphp/parallel)) = 1.4.3
Provides: bundled(php-composer(amphp/parser)) = 1.1.0
Provides: bundled(php-composer(amphp/process)) = 1.1.4
Provides: bundled(php-composer(amphp/serialization)) = 1.0.0
Provides: bundled(php-composer(amphp/sync)) = 1.4.2
Provides: bundled(php-composer(bamarni/composer-bin-plugin)) = 1.8.2
Provides: bundled(php-composer(league/flysystem)) = 2.5.0
Provides: bundled(php-composer(league/mime-type-detection)) = 1.11.0
Provides: bundled(php-composer(psr/log)) = 1.1.4
Provides: bundled(php-composer(rubix/ml)) = 2.1.1
Provides: bundled(php-composer(rubix/tensor)) = 2.2.3
Provides: bundled(php-composer(symfony/polyfill-mbstring)) = 1.27.0
Provides: bundled(php-composer(symfony/polyfill-php73)) = 1.26.0
Provides: bundled(php-composer(symfony/polyfill-php80)) = 1.27.0
Provides: bundled(php-composer(aws/aws-crt-php)) = 1.2.5
Provides: bundled(php-composer(aws/aws-sdk-php)) = 3.311.2
Provides: bundled(php-composer(bantu/ini-get-wrapper)) = 1.0.1
Provides: bundled(php-composer(brick/math)) = 0.12.1
Provides: bundled(php-composer(cweagans/composer-patches)) = 1.7.3
Provides: bundled(php-composer(deepdiver/zipstreamer)) = 2.0.3
Provides: bundled(php-composer(deepdiver1975/tarstreamer)) = 2.1.0
Provides: bundled(php-composer(doctrine/cache)) = 2.2.0
Provides: bundled(php-composer(doctrine/dbal)) = 3.9.1
Provides: bundled(php-composer(doctrine/deprecations)) = 1.1.3
Provides: bundled(php-composer(doctrine/event-manager)) = 2.0.1
Provides: bundled(php-composer(doctrine/lexer)) = 3.0.1
Provides: bundled(php-composer(egulias/email-validator)) = 4.0.2
Provides: bundled(php-composer(fusonic/opengraph)) = 2.3.0
Provides: bundled(php-composer(giggsey/libphonenumber-for-php-lite)) = 8.13.45
Provides: bundled(php-composer(guzzlehttp/guzzle)) = 7.8.2
Provides: bundled(php-composer(guzzlehttp/promises)) = 2.0.4
Provides: bundled(php-composer(guzzlehttp/psr7)) = 2.7.0
Provides: bundled(php-composer(guzzlehttp/uri-template)) = 1.0.3
Provides: bundled(php-composer(icewind/searchdav)) = 3.1.0
Provides: bundled(php-composer(icewind/streams)) = 0.7.7
Provides: bundled(php-composer(justinrainbow/json-schema)) = 5.2.13
Provides: bundled(php-composer(kornrunner/blurhash)) = 1.2.2
Provides: bundled(php-composer(laravel/serializable-closure)) = 1.3.5
Provides: bundled(php-composer(lcobucci/clock)) = 3.0.0
Provides: bundled(php-composer(masterminds/html5)) = 2.9.0
Provides: bundled(php-composer(mexitek/phpcolors)) = 1.0.4
Provides: bundled(php-composer(microsoft/azure-storage-blob)) = 1.5.4
Provides: bundled(php-composer(microsoft/azure-storage-common)) = 1.5.2
Provides: bundled(php-composer(mlocati/ip-lib)) = 1.18.0
Provides: bundled(php-composer(mtdowling/jmespath.php)) = 2.7.0
Provides: bundled(php-composer(nextcloud/lognormalizer)) = 1.0.0
Provides: bundled(php-composer(paragonie/constant_time_encoding)) = 2.7.0
Provides: bundled(php-composer(pear/archive_tar)) = 1.5.0
Provides: bundled(php-composer(pear/console_getopt)) = 1.4.3
Provides: bundled(php-composer(pear/pear-core-minimal)) = 1.10.15
Provides: bundled(php-composer(pear/pear_exception)) = 1.0.2
Provides: bundled(php-composer(php-http/guzzle7-adapter)) = 1.0.0
Provides: bundled(php-composer(php-http/httplug)) = 2.2.0
Provides: bundled(php-composer(php-http/promise)) = 1.1.0
Provides: bundled(php-composer(php-opencloud/openstack)) = 3.10.0
Provides: bundled(php-composer(phpseclib/phpseclib)) = 2.0.47
Provides: bundled(php-composer(pimple/pimple)) = 3.5.0
Provides: bundled(php-composer(psr/cache)) = 3.0.0
Provides: bundled(php-composer(psr/clock)) = 1.0.0
Provides: bundled(php-composer(psr/container)) = 2.0.2
Provides: bundled(php-composer(psr/event-dispatcher)) = 1.0.0
Provides: bundled(php-composer(psr/http-client)) = 1.0.3
Provides: bundled(php-composer(psr/http-factory)) = 1.1.0
Provides: bundled(php-composer(psr/http-message)) = 1.1
Provides: bundled(php-composer(psr/log)) = 2.0.0
Provides: bundled(php-composer(punic/punic)) = 3.8.1
Provides: bundled(php-composer(ralouphie/getallheaders)) = 3.0.3
Provides: bundled(php-composer(sabre/dav)) = 4.6.0
Provides: bundled(php-composer(sabre/event)) = 5.1.4
Provides: bundled(php-composer(sabre/http)) = 5.1.10
Provides: bundled(php-composer(sabre/uri)) = 2.3.3
Provides: bundled(php-composer(sabre/vobject)) = 4.5.4
Provides: bundled(php-composer(sabre/xml)) = 2.2.7
Provides: bundled(php-composer(scssphp/scssphp)) = 1.12.1
Provides: bundled(php-composer(spomky-labs/cbor-php)) = 3.1.0
Provides: bundled(php-composer(spomky-labs/pki-framework)) = 1.2.1
Provides: bundled(php-composer(stecman/symfony-console-completion)) = 0.13.0
Provides: bundled(php-composer(symfony/console)) = 6.4.12
Provides: bundled(php-composer(symfony/css-selector)) = 6.4.3
Provides: bundled(php-composer(symfony/deprecation-contracts)) = 3.5.0
Provides: bundled(php-composer(symfony/dom-crawler)) = 6.4.4
Provides: bundled(php-composer(symfony/event-dispatcher)) = 6.4.8
Provides: bundled(php-composer(symfony/event-dispatcher-contracts)) = 3.0.2
Provides: bundled(php-composer(symfony/http-foundation)) = 6.4.12
Provides: bundled(php-composer(symfony/mailer)) = 6.4.12
Provides: bundled(php-composer(symfony/mime)) = 6.4.12
Provides: bundled(php-composer(symfony/polyfill-ctype)) = 1.29.0
Provides: bundled(php-composer(symfony/polyfill-intl-grapheme)) = 1.31.0
Provides: bundled(php-composer(symfony/polyfill-intl-idn)) = 1.31.0
Provides: bundled(php-composer(symfony/polyfill-intl-normalizer)) = 1.31.0
Provides: bundled(php-composer(symfony/polyfill-mbstring)) = 1.31.0
Provides: bundled(php-composer(symfony/polyfill-php80)) = 1.29.0
Provides: bundled(php-composer(symfony/polyfill-php83)) = 1.31.0
Provides: bundled(php-composer(symfony/polyfill-uuid)) = 1.31.0
Provides: bundled(php-composer(symfony/process)) = 6.4.12
Provides: bundled(php-composer(symfony/routing)) = 6.4.12
Provides: bundled(php-composer(symfony/service-contracts)) = 3.0.2
Provides: bundled(php-composer(symfony/string)) = 6.0.19
Provides: bundled(php-composer(symfony/translation)) = 6.4.12
Provides: bundled(php-composer(symfony/translation-contracts)) = 3.4.2
Provides: bundled(php-composer(symfony/uid)) = 6.4.12
Provides: bundled(php-composer(wapmorgan/mp3info)) = 0.1.0
Provides: bundled(php-composer(web-auth/cose-lib)) = 4.4.0
Provides: bundled(php-composer(web-auth/webauthn-lib)) = 4.9.1

# OpenIconic icons bundled via sabre-dav
Provides:       bundled(openiconic-fonts) = 1.0.0
# jscolor bundled via themeing app
Provides:       bundled(jscolor) = 2.0.4
# jquery-ui-multiselect bundled via user_ldap app
Provides:       bundled(jquery-ui-multiselect) = 0.3.1
# zxcvbn bundled via core
Provides:       bundled(zxcvbn) = 4.4.2

%description
NextCloud gives you universal access to your files through a web interface or
WebDAV. It also provides a platform to easily view & sync your contacts,
calendars and bookmarks across all your devices and enables basic editing right
on the web. NextCloud is extendable via a simple but powerful API for
applications and plugins.


%package httpd
Summary:        Httpd integration for NextCloud
Provides:       %{name}-webserver = %{version}-%{release}
Requires:       %{name} = %{version}-%{release}
# PHP dependencies
Requires:       php-fpm httpd

%description httpd
%{summary}.


%package nginx
Summary:        Nginx integration for NextCloud
Provides:       %{name}-webserver = %{version}-%{release}
Requires:       %{name} = %{version}-%{release}
# PHP dependencies
Requires:       php-fpm nginx

%description nginx
%{summary}.


%package mysql
Summary:        MySQL database support for NextCloud
Provides:       %{name}-database = %{version}-%{release}
Requires:       %{name} = %{version}-%{release}
# From getSupportedDatabases, mysql => pdo, mysql
Requires:       php-mysqlnd

%description mysql
This package ensures the necessary dependencies are in place for NextCloud to
work with MySQL / MariaDB databases. It does not require a MySQL / MariaDB
server to be installed, as you may well wish to use a remote database
server.

If you want the database to be on the same system as NextCloud itself, you must
also install and enable a MySQL / MariaDB server package. See README.mysql for
more details.

%package postgresql
Summary:        PostgreSQL database support for NextCloud
Provides:       %{name}-database = %{version}-%{release}
Requires:       %{name} = %{version}-%{release}
# From getSupportedDatabases, pgsql => function, pg_connect
Requires:       php-pgsql

%description postgresql
This package ensures the necessary dependencies are in place for NextCloud to
work with a PostgreSQL database. It does not require the PostgreSQL server
package to be installed, as you may well wish to use a remote database
server.

If you want the database to be on the same system as NextCloud itself, you must
also install and enable the PostgreSQL server package. See README.postgresql
for more details.


%package sqlite
Summary:        SQLite 3 database support for NextCloud
Provides:       %{name}-database = %{version}-%{release}
Requires:       %{name} = %{version}-%{release}
# From getSupportedDatabases, pgsql => class, SQLite3

%description sqlite
This package ensures the necessary dependencies are in place for NextCloud to
work with an SQLite 3 database stored on the local system.

%prep
%autosetup -n %{name} -p1

# Fix php shebang in occ
sed -ri 's\^#!/usr/bin/env php$\#!%{_bindir}/php\' occ

# patch backup files and .git stuff
find . -name \*.orig    -type f -delete -print
find . -name .gitignore -type f -delete -print
find . -name .github    -type d -prune -exec rm -r {} \; -print

# fix CLI upgrade advise on splash screen
sed -i -e 's#./\(occ upgrade\)#sudo -u apache php /usr/share/nextcloud/\1#' core/templates/update.admin.php

# prepare package doc
cp %{SOURCE300} README.%{distro}
cp %{SOURCE301} README.mysql
cp %{SOURCE302} README.postgresql
cp %{SOURCE303} MIGRATION.%{distro}

# point the reader to the correct README filename
sed -i 's/distro/%{distro}/g' README.%{distro}

# Locate license files and put them sensibly in place
# get rid of all composer licenses
find -wholename "*/composer/LICENSE" -exec mv {} composer-LICENSE \;

# Deal with licenses automatically
find . -mindepth 2 \( -name '*LICENSE*' -o -name '*LICENCE*' \) | { while read a ; do mv "$a" $(echo $a | sed "s_^./__" | tr "/ " "__" )-LICENSE ; done ; }
find . -mindepth 2 -name '*COPYING*' | { while read a ; do mv "$a" $(echo $a | sed "s_^./__" | tr "/ " "__" )-COPYING ; done ; }

# case-sensitive list of partial matches to exclude from the nextcloud integrity checker
# include readme, license, other docs, and any files we move or patch during the build
excludedFilenames="
README
readme
LICENSE
LICENCE
license
copying
COPYING
AUTHORS
htaccess
gitignore
user.ini
update.admin.php
Updater.php
occ
Checker.php
"

# nextcloud source files use tabs rather than spaces, ew
tabs="				"
cr="
"

# Add quotes, commas, and escaped newlines
for f in $excludedFilenames; do
  formattedlist="$formattedlist$tabs'$f',\\$cr"
done

# look for our sed placeholder we patched in earlier, then insert our formatted list of keywords
sed -i "s|//sedplaceholder|${formattedlist}|" lib/private/IntegrityCheck/Checker.php

# Build nextcloud-defaults.inc from upstream .htaccess. We will install it later.
cat .htaccess >> %{SOURCE105}

%check
# Make sure there are no license files left over
: Check for leftover license files
find . -mindepth 2 \( -name '*LICENSE*' -o -name '*LICENCE*' -o  -name '*COPYING*' \)
nb=$( find . -mindepth 2 \( -name '*LICENSE*' -o -name '*LICENCE*' -o  -name '*COPYING*' \) | wc -l )
if [ $nb -gt 0 ]
  then
  false Found unexpected licenses to verify
fi


%build
# Nothing to build

%install
install -dm 755 %{buildroot}%{_datadir}/%{name}

# create nextcloud datadir
mkdir -p %{buildroot}%{_localstatedir}/lib/%{name}/data
# create writable app dir for appstore
mkdir -p %{buildroot}%{_localstatedir}/lib/%{name}/apps
# create nextcloud sysconfdir
mkdir -p %{buildroot}%{_sysconfdir}/%{name}

# install content
for d in $(find . -mindepth 1 -maxdepth 1 -type d | grep -v config); do
    cp -a "$d" %{buildroot}%{_datadir}/%{name}
done

for f in {*.php,*.html,robots.txt}; do
    install -pm 644 "$f" %{buildroot}%{_datadir}/%{name}
done

# occ should be executable
install -pm 755 occ %{buildroot}%{_datadir}/%{name}

# symlink config dir
ln -s ../../../%{_sysconfdir}/%{name} %{buildroot}%{_datadir}/%{name}/config

# nextcloud looks for ca-bundle.crt in config dir
ln -s ../pki/tls/certs/ca-bundle.crt %{buildroot}%{_sysconfdir}/%{name}/ca-bundle.crt

# set default config
install -pm 644 %{SOURCE1}    %{buildroot}%{_sysconfdir}/%{name}/config.php

# httpd config
install -Dpm 644 %{SOURCE100} \
    %{buildroot}%{_sysconfdir}/httpd/conf.d/%{name}.conf
install -Dpm 644 %{SOURCE101} \
    %{buildroot}%{_sysconfdir}/httpd/conf.d/%{name}-access.conf.avail
install -Dpm 644 %{SOURCE102} %{SOURCE103} %{SOURCE104} %{SOURCE105} \
    %{buildroot}%{_sysconfdir}/httpd/conf.d/

# nginx config
install -Dpm 644 %{SOURCE200} \
    %{buildroot}%{_sysconfdir}/nginx/default.d/%{name}.conf
install -Dpm 644 %{SOURCE201} \
    %{buildroot}%{_sysconfdir}/nginx/conf.d/%{name}.conf

# php-fpm config
install -Dpm 644 %{SOURCE202} \
    %{buildroot}%{_sysconfdir}/php-fpm.d/%{name}.conf

# php.ini config
install -Dpm 644 %{SOURCE203} \
    %{buildroot}%{_sysconfdir}/php.d/60-%{name}.ini

# Install the systemd timer
install -Dpm 644 %{SOURCE2} %{buildroot}%{_unitdir}/nextcloud-cron.service
install -Dpm 644 %{SOURCE3} %{buildroot}%{_unitdir}/nextcloud-cron.timer

# If there's a new installation activate the installation wizard
%post
INSTALLED=$(grep -c secret /etc/nextcloud/config.php)
if [ "${INSTALLED}" -eq "0" ]; then
  echo "First time installation, enabling installation wizard"
  touch %{_sysconfdir}/%{name}/CAN_INSTALL
  chown apache:apache %{_sysconfdir}/%{name}/CAN_INSTALL
fi

/usr/bin/systemctl restart php-fpm.service > /dev/null 2>&1 || :

%post httpd
/usr/bin/systemctl reload httpd.service > /dev/null 2>&1 || :
/usr/bin/systemctl reload php-fpm.service > /dev/null 2>&1 || :

%postun httpd
if [ $1 -eq 0 ]; then
  /usr/bin/systemctl reload httpd.service > /dev/null 2>&1 || :
  /usr/bin/systemctl reload php-fpm.service > /dev/null 2>&1 || :
fi

%post nginx
/usr/bin/systemctl reload nginx.service > /dev/null 2>&1 || :
/usr/bin/systemctl reload php-fpm.service > /dev/null 2>&1 || :

%postun nginx
if [ $1 -eq 0 ]; then
  /usr/bin/systemctl reload nginx.service > /dev/null 2>&1 || :
  /usr/bin/systemctl reload php-fpm.service > /dev/null 2>&1 || :
fi

%files
%doc AUTHORS README.%{distro} MIGRATION.%{distro} config/config.sample.php
%license *-LICENSE
%dir %attr(-,apache,apache) %{_sysconfdir}/%{name}
# contains sensitive data (dbpassword, passwordsalt)
%config(noreplace) %attr(0600,apache,apache) %{_sysconfdir}/%{name}/config.php
%config(noreplace) %{_sysconfdir}/php.d/60-%{name}.ini
# need the symlink in confdir but it's not config
%{_sysconfdir}/%{name}/ca-bundle.crt
%{_datadir}/%{name}
%dir %attr(0755,apache,apache) %{_localstatedir}/lib/%{name}
# user data must not be world readable
%dir %attr(0750,apache,apache) %{_localstatedir}/lib/%{name}/data
%attr(-,apache,apache) %{_localstatedir}/lib/%{name}/apps
%{_unitdir}/nextcloud-cron.service
%{_unitdir}/nextcloud-cron.timer

%files httpd
%config(noreplace) %{_sysconfdir}/httpd/conf.d/%{name}.conf
%{_sysconfdir}/httpd/conf.d/%{name}-access.conf.avail
%{_sysconfdir}/httpd/conf.d/%{name}*.inc
%config(noreplace) %{_sysconfdir}/php-fpm.d/%{name}.conf

%files nginx
%config(noreplace) %{_sysconfdir}/nginx/default.d/%{name}.conf
%config(noreplace) %{_sysconfdir}/nginx/conf.d/%{name}.conf
%config(noreplace) %{_sysconfdir}/php-fpm.d/%{name}.conf

%files mysql
%doc README.mysql
%files postgresql
%doc README.postgresql
%files sqlite


%changelog
%autochangelog
