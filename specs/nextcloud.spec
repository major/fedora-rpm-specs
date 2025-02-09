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

# Auto-generate Provides from bundled php-composer libraries
BuildRequires:  composer-generators

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

# jquery-ui-multiselect bundled via user_ldap app
Provides:       bundled(jquery-ui-multiselect) = 1.13
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
sed -i -e 's#\./\(occ upgrade\)#sudo -u apache php /usr/share/nextcloud/\1#' core/templates/update.admin.php

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
