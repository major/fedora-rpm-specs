# libs3
%global commit 66885387c9f761253988321de9c4bbfc1660717d
%global shortcommit %(c=%{commit}; echo ${c:0:7})

%global uid 133
%global username bacula

Name:               bacula
Version:            15.0.3
Release:            %autorelease
Summary:            Cross platform network backup for Linux, Unix, Mac and Windows
# See LICENSE for details
# See https://gitlab.com/fedora/legal/fedora-license-data/-/issues/277
License:            LicenseRef-Bacula
URL:                http://www.bacula.org

# AGPL-3.0-only with exceptions
Source0:            http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz

Source2:            quickstart_postgresql.txt
Source3:            quickstart_mysql.txt
Source4:            quickstart_sqlite3.txt
Source5:            README.md
Source6:            %{name}.logrotate
# Firewalld cumulative (bacula.xml) and fd (bacula-client.xml) services are in firewalld:
Source7:            %{name}-storage.xml
Source8:            %{name}-director.xml
Source10:           %{name}-fd.service
Source11:           %{name}-dir.service
Source12:           %{name}-sd.service
Source15:           %{name}-fd.sysconfig
Source16:           %{name}-dir.sysconfig
Source17:           %{name}-sd.sysconfig
Source19:           https://salsa.debian.org/bacula-team/bacula/-/raw/master/debian/additions/bacula-tray-monitor.png#/bacula-tray-monitor.png

# LGPL-3.0-only - S3 libs with AWS glacier support
# https://gitlab.bacula.org/bacula-community-edition/libs3/-/commits/master?ref_type=heads
Source20:            https://gitlab.bacula.org/bacula-community-edition/libs3/-/archive/%{commit}/libs3-%{shortcommit}.tar.bz2
Source21:            libs3-openssl.patch

Patch1:             %{name}-openssl.patch
Patch2:             %{name}-seg-fault.patch
Patch3:             %{name}-non-free-code.patch
Patch4:             %{name}-traceback-man.patch
Patch5:             %{name}-compile-options.patch
Patch6:             %{name}-install.patch
Patch7:             %{name}-desktop.patch
Patch8:             %{name}-docker-plugin.patch
# Original patch removed by mistake, upstream is not willing to add it again:
# http://www.bacula.org/git/cgit.cgi/bacula/commit/?h=Branch-7.0&id=51b3b98fb77ab3c0decee455cc6c4d2eb3c5303a
# Without this, there is no library providing the correct shared object name
# required by the daemons.
# http://bugs.bacula.org/view.php?id=2084
Patch9:             %{name}-autoconf.patch
Patch10:            %{name}-scripts.patch

BuildRequires:      autoconf
BuildRequires:      automake
BuildRequires:      desktop-file-utils
BuildRequires:      firewalld-filesystem
BuildRequires:      gcc
BuildRequires:      gcc-c++
BuildRequires:      glibc-devel
BuildRequires:      libacl-devel
BuildRequires:      libcurl-devel
BuildRequires:      libstdc++-devel
BuildRequires:      libxml2-devel
BuildRequires:      libcap-devel
BuildRequires:      libpq-devel
BuildRequires:      libxcrypt-devel
BuildRequires:      libzstd-devel
BuildRequires:      lzo-devel
BuildRequires:      make
BuildRequires:      mariadb-connector-c-devel
BuildRequires:      ncurses-devel
BuildRequires:      openldap-devel
BuildRequires:      openssl-devel
BuildRequires:      perl-generators
BuildRequires:      perl-interpreter
BuildRequires:      qt5-qtbase-devel
BuildRequires:      readline-devel
BuildRequires:      sed
BuildRequires:      sqlite-devel
BuildRequires:      systemd
BuildRequires:      zlib-devel

Requires(post):     firewalld-filesystem

%description
Bacula is a set of programs that allow you to manage the backup, recovery, and
verification of computer data across a network of different computers. It is
based on a client/server architecture and is efficient and relatively easy to
use, while offering many advanced storage management features that make it easy
to find and recover lost or damaged files.

%package libs
Summary:            Bacula libraries

%description libs
Bacula is a set of programs that allow you to manage the backup,
recovery, and verification of computer data across a network of
different computers. It is based on a client/server architecture.

This package contains basic Bacula libraries, which are used by all
Bacula programs.

%package libs-sql
Summary:            Bacula SQL libraries

%description libs-sql
Bacula is a set of programs that allow you to manage the backup, recovery, and
verification of computer data across a network of different computers. It is
based on a client/server architecture.

This package contains the SQL Bacula libraries, which are used by Director and
Storage daemons. You have to select your preferred catalog library through the
alternatives system.

%package common
Summary:            Common Bacula files
Provides:           group(%username) = %uid
Provides:           user(%username) = %uid
Requires:           bacula-libs%{?_isa} = %{version}-%{release}
Requires(postun):   shadow-utils

%description common
Bacula is a set of programs that allow you to manage the backup, recovery, and
verification of computer data across a network of different computers. It is
based on a client/server architecture.

This package contains files common to all Bacula daemons.

%package director
Summary:            Bacula Director files
Requires:           bacula-common%{?_isa} = %{version}-%{release}
Requires:           bacula-libs%{?_isa} = %{version}-%{release}
Requires:           bacula-libs-sql%{?_isa} = %{version}-%{release}

Requires(post):     systemd
Requires(preun):    systemd
Requires(postun):   systemd

# For generating the QR code for TOTP authentication on console and director:
Recommends:         qrencode

%description director
Bacula is a set of programs that allow you to manage the backup, recovery, and
verification of computer data across a network of different computers. It is
based on a client/server architecture.

This package contains the director files.

%package logwatch
Summary:            Bacula Director logwatch scripts
BuildArch:          noarch
Requires:           bacula-director = %{version}-%{release}
Requires:           logwatch

%description logwatch
Bacula is a set of programs that allow you to manage the backup, recovery, and
verification of computer data across a network of different computers. It is
based on a client/server architecture.

This package contains logwatch scripts for Bacula Director.

%package storage
Summary:            Bacula storage daemon files
Requires:           bacula-common%{?_isa} = %{version}-%{release}
Requires:           bacula-libs%{?_isa} = %{version}-%{release}
Requires:           bacula-libs-sql%{?_isa} = %{version}-%{release}
Requires:           mt-st
Requires:           mtx
Requires:           sdparm
Provides:           bundled(libs3) = 4.1.bac

Requires(post):     systemd
Requires(preun):    systemd
Requires(postun):   systemd

%description storage
Bacula is a set of programs that allow you to manage the backup, recovery, and
verification of computer data across a network of different computers. It is
based on a client/server architecture.

This package contains the storage daemon, the daemon responsible for writing
the data received from the clients onto tape drives or other mass storage
devices.

%package client
Summary:            Bacula backup client
Requires:           bacula-common%{?_isa} = %{version}-%{release}
Requires:           bacula-libs%{?_isa} = %{version}-%{release}

Requires(post):     systemd
Requires(preun):    systemd
Requires(postun):   systemd

%description client
Bacula is a set of programs that allow you to manage the backup, recovery, and
verification of computer data across a network of different computers. It is
based on a client/server architecture.

This package contains the bacula client, the daemon running on the system to be
backed up.

%package console
Summary:            Bacula management console
Obsoletes:          bacula-console-wxwidgets <= 5.0.3
Requires:           bacula-libs%{?_isa} = %{version}-%{release}

%description console
Bacula is a set of programs that allow you to manage the backup, recovery, and
verification of computer data across a network of different computers. It is
based on a client/server architecture.

This package contains the command-line management console for the bacula backup
system.

%package console-bat
Summary:            Bacula bat console
Requires:           bacula-libs%{?_isa} = %{version}-%{release}
Requires:           dejavu-lgc-sans-fonts

%description console-bat
Bacula is a set of programs that allow you to manage the backup, recovery, and
verification of computer data across a network of different computers. It is
based on a client/server architecture.

This package contains the bat version of the bacula management console.

%package traymonitor
Summary:            Bacula system tray monitor
Requires:           bacula-libs%{?_isa} = %{version}-%{release}
Requires:           dejavu-lgc-sans-fonts

%description traymonitor
Bacula is a set of programs that allow you to manage the backup, recovery, and
verification of computer data across a network of different computers. It is
based on a client/server architecture.

This package contains the Gnome and KDE compatible tray monitor to monitor your
bacula server.

%package devel
Summary:            Bacula development files
Requires:           bacula-libs%{?_isa} = %{version}-%{release}
Requires:           bacula-libs-sql%{?_isa} = %{version}-%{release}

%description devel
Bacula is a set of programs that allow you to manage the backup, recovery, and
verification of computer data across a network of different computers. It is
based on a client/server architecture.

This development package contains static libraries and header files.

%package -n nagios-plugins-bacula
Summary:            Nagios Plugin - check_bacula
Requires:           bacula-libs%{?_isa} = %{version}-%{release}
Requires:           nagios-common%{?_isa}

%description -n nagios-plugins-bacula
Provides check_bacula support for Nagios.

%prep
%autosetup -a20 -p1

cp %{SOURCE2} %{SOURCE3} %{SOURCE4} %{SOURCE5} .

# Regenerate configure
pushd autoconf
aclocal -I bacula-macros/ -I gettext-macros/ -I libtool/
popd
autoconf -I autoconf/ -o configure autoconf/configure.in

# Remove execution permissions from files we're packaging as docs later on
find updatedb -type f | xargs chmod -x

# Create a sysusers.d config file
cat >bacula.sysusers.conf <<EOF
u bacula %uid 'Bacula Backup System' /var/spool/bacula -
EOF

%build
%set_build_flags
export CFLAGS="%{optflags} -fPIC -Wno-error=attribute-warning -I%{_includedir}/ncurses"
export CXXFLAGS="%{optflags} -fPIC -Wno-error=attribute-warning -I%{_includedir}/ncurses"
export PATH="$PATH:%{_qt5_bindir}"

pushd libs3-%{commit}
patch -p1 -i %{SOURCE21}
%make_build exported
popd

%configure \
    --disable-conio \
    --disable-rpath \
    --docdir=%{_datadir}/bacula \
    --enable-antivirus-plugin \
    --enable-bat \
    --enable-antivirus-plugin \
    --enable-batch-insert \
    --enable-build-dird \
    --enable-build-stored \
    --enable-cdp-plugin \
    --enable-docker-plugin \
    --enable-includes \
    --enable-largefile \
    --enable-ldap-bpam \
    --enable-lzo \
    --enable-readline \
    --enable-smartalloc \
    --enable-totp-bpam \
    --enable-ldap-bpam \
    --sysconfdir=%{_sysconfdir}/bacula \
    --with-aws \
    --with-basename=bacula \
    --with-bsrdir=%{_localstatedir}/spool/bacula \
    --with-dir-password=@@DIR_PASSWORD@@ \
    --with-fd-password=@@FD_PASSWORD@@ \
    --with-hostname=localhost \
    --with-ldap \
    --with-logdir=%{_localstatedir}/log/bacula \
    --with-mon-dir-password=@@MON_DIR_PASSWORD@@ \
    --with-mon-fd-password=@@MON_FD_PASSWORD@@ \
    --with-mon-sd-password=@@MON_SD_PASSWORD@@ \
    --with-mysql \
    --with-openssl \
    --with-pid-dir=%{_localstatedir}/run \
    --with-plugindir=%{_libdir}/%{name} \
    --with-postgresql \
    --with-scriptdir=%{_libexecdir}/bacula \
    --with-sd-password=@@SD_PASSWORD@@ \
    --with-smtp-host=localhost \
    --with-s3=`pwd`/libs3-%{commit}/build \
    --with-sqlite3 \
    --with-subsys-dir=%{_localstatedir}/lock/subsys \
    --with-working-dir=%{_localstatedir}/spool/bacula \
    --with-x

# Remove RPATH
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool

%make_build
%make_build -C examples/nagios/check_bacula

%install
%make_install
%make_install -C examples/nagios/check_bacula

# Remove unused unversioned Storage Daemon plugins
rm -f %{buildroot}%{_libdir}/%{name}/%{name}-sd-*-driver.so

# This will be managed through alternatives, as it requires the name to NOT
# change between upgrades, so the versioned library name can not be used.
rm -f %{buildroot}%{_libdir}/libbaccats.so

# Remove placeholder
rm -f %{buildroot}%{_libexecdir}/%{name}/baculabackupreport

# Bat
install -p -m 644 -D src/qt-console/images/bat_icon.png %{buildroot}%{_datadir}/pixmaps/bat_icon.png
install -p -m 644 -D scripts/bat.desktop %{buildroot}%{_datadir}/applications/bat.desktop
install -p -m 755 -D src/qt-console/.libs/bat %{buildroot}%{_sbindir}/bat

install -p -m 644 -D manpages/bacula-tray-monitor.1 %{buildroot}%{_mandir}/man1/bacula-tray-monitor.1
install -p -m 644 -D %{SOURCE19} %{buildroot}%{_datadir}/pixmaps/bacula-tray-monitor.png
install -p -m 644 -D scripts/bacula-tray-monitor.desktop %{buildroot}%{_datadir}/applications/bacula-tray-monitor.desktop
install -p -m 755 -D src/qt-console/tray-monitor/.libs/bacula-tray-monitor %{buildroot}%{_sbindir}/bacula-tray-monitor

# Logrotate
mkdir -p %{buildroot}%{_localstatedir}/log/bacula
install -p -m 644 -D %{SOURCE6} %{buildroot}%{_sysconfdir}/logrotate.d/bacula

# Logwatch
install -p -m 755 -D scripts/logwatch/bacula %{buildroot}%{_sysconfdir}/logwatch/scripts/services/bacula
install -p -m 755 -D scripts/logwatch/applybaculadate %{buildroot}%{_sysconfdir}/logwatch/scripts/shared/applybaculadate
install -p -m 644 -D scripts/logwatch/logfile.bacula.conf %{buildroot}%{_sysconfdir}/logwatch/conf/logfiles/bacula.conf
install -p -m 644 -D scripts/logwatch/services.bacula.conf %{buildroot}%{_sysconfdir}/logwatch/conf/services/bacula.conf

# Systemd unit files
mkdir -p %{buildroot}%{_unitdir}
install -p -m 644 -D %{SOURCE10} %{buildroot}%{_unitdir}/bacula-fd.service
install -p -m 644 -D %{SOURCE11} %{buildroot}%{_unitdir}/bacula-dir.service
install -p -m 644 -D %{SOURCE12} %{buildroot}%{_unitdir}/bacula-sd.service

# Sysconfig
install -p -m 644 -D %{SOURCE15} %{buildroot}%{_sysconfdir}/sysconfig/bacula-fd
install -p -m 644 -D %{SOURCE16} %{buildroot}%{_sysconfdir}/sysconfig/bacula-dir
install -p -m 644 -D %{SOURCE17} %{buildroot}%{_sysconfdir}/sysconfig/bacula-sd

# Spool directory
mkdir -p %{buildroot}%{_localstatedir}/spool/bacula

# Firewalld rules
install -p -m 644 -D %{SOURCE7} %{buildroot}%{_prefix}/lib/firewalld/services/bacula-storage.xml
install -p -m 644 -D %{SOURCE8} %{buildroot}%{_prefix}/lib/firewalld/services/bacula-director.xml

# Remove stuff we do not need
rm -f %{buildroot}%{_libexecdir}/bacula/{bacula,bacula-ctl-*,startmysql,stopmysql,bconsole,make_catalog_backup}
rm -f %{buildroot}%{_sbindir}/bacula
rm -f %{buildroot}%{_mandir}/man8/bacula.8.gz
rm -f %{buildroot}%{_libdir}/*.la
rm -f %{buildroot}%{_datadir}/bacula/{ChangeLog,INSTALL,LICENSE*,README,ReleaseNotes,VERIFYING,technotes}

# Fix up some perms so rpmlint does not complain too much
chmod 755 %{buildroot}%{_sbindir}/*
chmod 755 %{buildroot}%{_libdir}/%{name}/*
chmod 755 %{buildroot}%{_libexecdir}/bacula/*
chmod 644 %{buildroot}%{_libexecdir}/bacula/btraceback.*

install -m0644 -D bacula.sysusers.conf %{buildroot}%{_sysusersdir}/bacula.conf

%post libs-sql
/usr/sbin/alternatives --install %{_libdir}/libbaccats.so libbaccats.so %{_libdir}/libbaccats-mysql.so 50
/usr/sbin/alternatives --install %{_libdir}/libbaccats.so libbaccats.so %{_libdir}/libbaccats-sqlite3.so 40
/usr/sbin/alternatives --install %{_libdir}/libbaccats.so libbaccats.so %{_libdir}/libbaccats-postgresql.so 60

# Fix for automatic selection of backends during upgrades
if readlink /etc/alternatives/libbaccats.so | grep --silent mysql || \
    readlink /etc/alternatives/bacula-dir | grep --silent mysql || \
    readlink /etc/alternatives/bacula-sd | grep --silent mysql; then
    /usr/sbin/alternatives --set libbaccats.so %{_libdir}/libbaccats-mysql.so
elif readlink /etc/alternatives/libbaccats.so | grep --silent sqlite || \
    readlink /etc/alternatives/bacula-dir | grep --silent sqlite || \
    readlink /etc/alternatives/bacula-sd | grep --silent sqlite; then
    /usr/sbin/alternatives --set libbaccats.so %{_libdir}/libbaccats-sqlite3.so
else
    /usr/sbin/alternatives --set libbaccats.so %{_libdir}/libbaccats-postgresql.so
fi

%preun libs-sql
if [ "$1" = 0 ]; then
    /usr/sbin/alternatives --remove libbaccats.so %{_libdir}/libbaccats-mysql.so
    /usr/sbin/alternatives --remove libbaccats.so %{_libdir}/libbaccats-sqlite3.so
    /usr/sbin/alternatives --remove libbaccats.so %{_libdir}/libbaccats-postgresql.so
fi


%post common
%firewalld_reload

%post client
%systemd_post %{name}-fd.service

%preun client
%systemd_preun %{name}-fd.service

%postun client
%systemd_postun_with_restart %{name}-fd.service

%post director
%systemd_post %{name}-dir.service

%preun director
%systemd_preun %{name}-dir.service

%postun director
%systemd_postun_with_restart %{name}-dir.service

%post storage
%systemd_post %{name}-sd.service

%preun storage
%systemd_preun %{name}-sd.service

%postun storage
%systemd_postun_with_restart %{name}-sd.service

%files libs
%license LICENSE
%doc AUTHORS ChangeLog SUPPORT ReleaseNotes LICENSE-FAQ LICENSE-FOSS
%{_libdir}/libbac-%{version}.so
%{_libdir}/libbaccfg-%{version}.so
%{_libdir}/libbacfind-%{version}.so
%{_libdir}/libbacsd-%{version}.so

%files libs-sql
# This gets recreated automatically even if the library is deleted in the
# install section. So leave the library in place until the very end and just
# exclude it:
%exclude %{_libdir}/libbaccats-%{version}.so
%{_libdir}/libbaccats-mysql-%{version}.so
%{_libdir}/libbaccats-mysql.so
%{_libdir}/libbaccats-postgresql-%{version}.so
%{_libdir}/libbaccats-postgresql.so
%{_libdir}/libbaccats-sqlite3-%{version}.so
%{_libdir}/libbaccats-sqlite3.so
%{_libdir}/libbacsql-%{version}.so

%files common
%doc README.md quickstart_*
%config(noreplace) %{_sysconfdir}/logrotate.d/bacula
%dir %{_libdir}/%{name}
%dir %{_localstatedir}/log/bacula %attr(750, bacula, bacula)
%dir %{_localstatedir}/spool/bacula %attr(750, bacula, bacula)
%dir %{_libexecdir}/%{name}
%dir %{_sysconfdir}/%{name} %attr(755,root,root)
%{_libexecdir}/%{name}/btraceback.dbx
%{_libexecdir}/%{name}/btraceback.gdb
%{_libexecdir}/%{name}/bacula_config
%{_libexecdir}/%{name}/btraceback.mdb
%{_mandir}/man8/btraceback.8*
%{_prefix}/lib/firewalld/services/bacula-director.xml
%{_prefix}/lib/firewalld/services/bacula-storage.xml
%{_sbindir}/btraceback
%{_sysusersdir}/bacula.conf

%files director
%doc updatedb examples/sample-query.sql
%config(noreplace) %{_sysconfdir}/bacula/bacula-dir.conf %attr(640,root,bacula)
%config(noreplace) %{_sysconfdir}/bacula/query.sql %attr(640,root,bacula)
%config(noreplace) %{_sysconfdir}/sysconfig/bacula-dir
%{_libdir}/%{name}/ldap-dir.so
%{_libexecdir}/%{name}/create_bacula_database
%{_libexecdir}/%{name}/delete_catalog_backup
%{_libexecdir}/%{name}/drop_bacula_database
%{_libexecdir}/%{name}/drop_bacula_tables
%{_libexecdir}/%{name}/grant_bacula_privileges
%{_libexecdir}/%{name}/install-key-manager.sh
%{_libexecdir}/%{name}/key-manager.py
%{_libexecdir}/%{name}/make_bacula_tables
%{_libexecdir}/%{name}/make_catalog_backup.pl
%{_libexecdir}/%{name}/update_bacula_tables
# MySQL scripts
%{_libexecdir}/%{name}/create_mysql_database
%{_libexecdir}/%{name}/drop_mysql_database
%{_libexecdir}/%{name}/drop_mysql_tables
%{_libexecdir}/%{name}/grant_mysql_privileges
%{_libexecdir}/%{name}/make_mysql_tables
%{_libexecdir}/%{name}/update_mysql_tables
# SQLite scripts
%{_libexecdir}/%{name}/create_sqlite3_database
%{_libexecdir}/%{name}/drop_sqlite3_database
%{_libexecdir}/%{name}/drop_sqlite3_tables
%{_libexecdir}/%{name}/grant_sqlite3_privileges
%{_libexecdir}/%{name}/make_sqlite3_tables
%{_libexecdir}/%{name}/update_sqlite3_tables
# PosgreSQL scripts
%{_libexecdir}/%{name}/create_postgresql_database
%{_libexecdir}/%{name}/drop_postgresql_database
%{_libexecdir}/%{name}/drop_postgresql_tables
%{_libexecdir}/%{name}/grant_postgresql_privileges
%{_libexecdir}/%{name}/make_postgresql_tables
%{_libexecdir}/%{name}/update_postgresql_tables
%{_mandir}/man1/bsmtp.1*
%{_mandir}/man8/bacula-dir.8*
%{_mandir}/man8/bdirjson.8*
%{_mandir}/man8/bregex.8*
%{_mandir}/man8/bwild.8*
%{_mandir}/man8/dbcheck.8*
%{_sbindir}/bacula-dir
%{_sbindir}/bdirjson
%{_sbindir}/bregex
%{_sbindir}/bsmtp
%{_sbindir}/btotp
%{_sbindir}/bwild
%{_sbindir}/dbcheck
%{_sbindir}/get_malware_abuse.ch
%{_sbindir}/ldaptest
%{_sbindir}/md5tobase64.py
%{_unitdir}/bacula-dir.service

%files logwatch
%config(noreplace) %{_sysconfdir}/logwatch/conf/logfiles/bacula.conf
%config(noreplace) %{_sysconfdir}/logwatch/conf/services/bacula.conf
%{_sysconfdir}/logwatch/scripts/services/bacula
%{_sysconfdir}/logwatch/scripts/shared/applybaculadate

%files storage
%config(noreplace) %{_sysconfdir}/bacula/bacula-sd.conf %attr(640,root,root)
%config(noreplace) %{_sysconfdir}/sysconfig/bacula-sd
%{_libdir}/%{name}/bacula-sd-aligned-driver-%{version}.so
%{_libdir}/%{name}/bacula-sd-cloud-aws-driver-%{version}.so
%{_libdir}/%{name}/bacula-sd-cloud-driver-%{version}.so
%{_libdir}/%{name}/bacula-sd-cloud-s3-driver-%{version}.so
%{_libdir}/%{name}/totp-dir.so
%{_libexecdir}/%{name}/disk-changer
%{_libexecdir}/%{name}/isworm
%{_libexecdir}/%{name}/mtx-changer
%{_libexecdir}/%{name}/mtx-changer.conf
%{_libexecdir}/%{name}/tapealert
%{_mandir}/man8/bacula-sd.8*
%{_mandir}/man8/bcopy.8*
%{_mandir}/man8/bextract.8*
%{_mandir}/man8/bls.8*
%{_mandir}/man8/bscan.8*
%{_mandir}/man8/bsdjson.8*
%{_mandir}/man8/btape.8*
%{_sbindir}/bacula-sd
%{_sbindir}/bcopy
%{_sbindir}/bextract
%{_sbindir}/bls
%{_sbindir}/bscan
%{_sbindir}/bsdjson
%{_sbindir}/btape
%{_unitdir}/bacula-sd.service

%files client
%config(noreplace) %{_sysconfdir}/bacula/bacula-fd.conf %attr(640,root,root)
%config(noreplace) %{_sysconfdir}/sysconfig/bacula-fd
%{_mandir}/man8/bacula-fd.8*
%{_mandir}/man8/bfdjson.8*
%{_libdir}/%{name}/antivirus-fd.so
%{_libdir}/%{name}/bpipe-fd.so
%{_libdir}/%{name}/cdp-fd.so
%{_libdir}/%{name}/docker-fd.so
%{_sbindir}/bacula-fd
%{_sbindir}/bfdjson
%{_sbindir}/cdp-client
%{_unitdir}/bacula-fd.service

%files console
%config(noreplace) %{_sysconfdir}/bacula/bconsole.conf %attr(640,root,root)
%{_mandir}/man8/bconsole.8*
%{_mandir}/man8/bbconsjson.8*
%{_sbindir}/bconsole
%{_sbindir}/bbconsjson

%files console-bat
%config(noreplace) %{_sysconfdir}/bacula/bat.conf %attr(640,root,root)
%{_datadir}/applications/bat.desktop
%{_datadir}/bacula/*.html
%{_datadir}/bacula/*.png
%{_datadir}/pixmaps/bat_icon.png
%{_mandir}/man1/bat.1*
%{_sbindir}/bat

%files traymonitor
%config(noreplace) %{_sysconfdir}/bacula/bacula-tray-monitor.conf %attr(640,root,root)
%{_datadir}/applications/bacula-tray-monitor.desktop
%{_datadir}/pixmaps/bacula-tray-monitor.png
%{_mandir}/man1/bacula-tray-monitor.1*
%{_sbindir}/bacula-tray-monitor

%files devel
%{_includedir}/bacula
%{_libdir}/libbac.so
%{_libdir}/libbaccfg.so
%{_libdir}/libbacfind.so
%{_libdir}/libbacsd.so
%{_libdir}/libbacsql.so

%files -n nagios-plugins-bacula
%{_libdir}/nagios/plugins/check_bacula

%changelog
%autochangelog
