#global commit 3a0d285b225207b3eccbb7b0ec3f27a2fbdc5be3

Name:           x2goserver
Version:        4.1.0.6
Release:        7%{?dist}
Summary:        X2Go Server

# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
URL:            http://www.x2go.org
Source0:        http://code.x2go.org/releases/source/%{name}/%{name}-%{version}.tar.gz
# git clone git://code.x2go.org/x2goserver
# cd x2goserver
# git archive --prefix=x2goserver-4.1.0.0-20130722git65169c9/ 65169c9d65b117802e50631be0bbd719163d969e | gzip > ../x2goserver-4.1.0.0-20130722git65169c9.tar.gz
#Source0:        %{name}/%{name}-%{version}-%{commit}.tar.gz
Source1:        x2gocleansessions.service
Source2:        x2gocleansessions.init

BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  desktop-file-utils
BuildRequires:  findutils
BuildRequires:  perl-generators
BuildRequires:  perl(ExtUtils::MakeMaker)
%if 0%{?fedora} || 0%{?rhel} >= 7
BuildRequires:  man2html-core
BuildRequires:  systemd
%else
BuildRequires:  man
%endif
# So XSESSIONDIR gets linked
BuildRequires:  xorg-x11-xinit
# For x2goruncommand - for now
Requires:       bc
Requires:       grep
# For ss in x2gogetfreeport
Requires:       iproute
# For x2goshowblocks
Requires:       lsof
Requires:       openssh-server
# For killall in x2gosuspend-session
Requires:       psmisc
# For x2godbadmin
Requires:       pwgen
Requires:       setxkbmap
# For printing, file-sharing
Requires:       sshfs
# For /etc/sudoers.d
Requires:       sudo
Requires:       which
Requires:       x2goagent = %{version}-%{release}
Requires:       x2goserver-common = %{version}-%{release}
Requires:       xorg-x11-fonts-misc
Requires:       xorg-x11-xauth
Requires:       xwininfo
Requires(pre):  shadow-utils
Requires(post): coreutils
Requires(post): grep
Requires(post): perl-X2Go-Server-DB
Requires(post): x2goserver-common

%if 0%{?fedora} || 0%{?rhel} >= 7
%{?systemd_requires}
%endif

%if 0%{?fedora}
Suggests:       x2goserver-fmbindings = %{version}-%{release}
Suggests:       x2goserver-printing = %{version}-%{release}
%endif
Requires:       x2goserver-xsession = %{version}-%{release}

# Provide upgrade path from upstream rpms
# http://bugs.x2go.org/cgi-bin/bugreport.cgi?bug=755
Obsoletes:      x2goserver-extensions < %{version}-%{release}
Provides:       x2goserver-extensions = %{version}-%{release}
Requires:       x2goserver-xsession
%if 0%{?fedora} >= 21
Suggests:       x2goserver-fmbindings
Suggests:       x2goserver-printing
%endif

%{?perl_default_filter}

%description
X2Go is a server based computing environment with
    - session resuming
    - low bandwidth support
    - session brokerage support
    - client side mass storage mounting support
    - client side printing support
    - audio support
    - authentication by smartcard and USB stick

This package contains the main daemon and tools for X2Go server-side session
administrations.


%package common
Summary:        X2Go Server (common files)
# for useradd/groupadd
BuildRequires:  shadow-utils
Requires(pre):  shadow-utils
BuildArch:      noarch

%description common
X2Go is a server based computing environment with
    - session resuming
    - low bandwidth support
    - session brokerage support
    - client side mass storage mounting support
    - client side printing support
    - audio support
    - authentication by smartcard and USB stick

This package contains common files needed by the X2Go Server
and the X2Go::Server Perl API.


%package fmbindings
Summary:        X2Go Server file manager bindings
Requires:       %{name} = %{version}-%{release}
Requires:       xdg-utils

%description fmbindings
X2Go is a server based computing environment with
    - session resuming
    - low bandwidth support
    - session brokerage support
    - client side mass storage mounting support
    - client side printing support
    - audio support
    - authentication by smartcard and USB stick

This package contains generic MIME type information
for X2Go's local folder sharing. It can be used with all
freedesktop.org compliant desktop shells.

However, this package can be superseded by other, more specific
desktop binding components, if installed and being used with the
corresponding desktop shell:
    - under LXDE by x2golxdebindings
    - under GNOMEv2 by x2gognomebindings
    - under KDE4 by plasma-widget-x2go
    - under MATE by x2gomatebindings


%package printing
Summary:        X2Go Server printing support
Requires:       %{name} = %{version}-%{release}

%description printing
The X2Go Server printing package provides client-side printing support for
X2Go.

This package has to be installed on X2Go servers that shall be able to pass
X2Go print jobs on to the X2Go client.

This package co-operates with the cups-x2go CUPS backend. If CUPS server and
X2Go server are hosted on different machines, then make sure you install
this package on the X2Go server(s) (and the cups-x2go package on the CUPS
server).


%package desktopsharing
Summary:        X2Go Server (Desktop Sharing support)
Requires:       %{name} = %{version}-%{release}
Requires:       x2godesktopsharing >= 3.2.0.0

%description desktopsharing
X2Go is a server based computing environment with
    - session resuming
    - low bandwidth support
    - session brokerage support
    - client side mass storage mounting support
    - audio support
    - authentication by smartcard and USB stick

X2Go Desktop Sharing is an X2Go add-on feature that allows a user to
grant other X2Go users access to the current session (shadow session
support). The user's current session may be an X2Go session itself or
simply a local X11 session.

This package contains all the integration and configuration logics
of a system-wide manageable desktop sharing setup.


%package xsession
Summary:        X2Go Server Xsession runner
Requires:       %{name} = %{version}-%{release}
# Not detected automatically
Requires:       perl(Cwd)
Requires:       xmessage
# Symlinks to xinit files
Requires:       xorg-x11-xinit
%if 0%{?fedora}
Requires:       dbus
%endif
BuildArch:      noarch

%description xsession
X2Go is a server based computing environment with
   - session resuming
   - low bandwidth support
   - session brokerage support
   - client side mass storage mounting support
   - client side printing support
   - audio support
   - authentication by smartcard and USB stick

This X2Go server add-on enables Xsession script handling
when starting desktop sessions with X2Go.

Amongst others the parsing of Xsession scripts will
enable desktop-profiles, ssh-agent startups, gpgagent
startups and many more Xsession related features on
X2Go session login automagically.


%package -n perl-X2Go-Server
Summary:        Perl X2Go::Server package
Requires:       x2goserver-common = %{version}-%{release}
Requires:       perl-X2Go-Log = %{version}-%{release}
Requires:       perl-X2Go-Server-DB = %{version}-%{release}
BuildArch:      noarch

%description -n perl-X2Go-Server
X2Go is a server based computing environment with
    - session resuming
    - low bandwidth support
    - session brokerage support
    - client side mass storage mounting support
    - client side printing support
    - audio support
    - authentication by smartcard and USB stick

This package contains the X2Go::Server Perl package.


%package -n perl-X2Go-Server-DB
Summary:        Perl X2Go::Server::DB package
Requires:       x2goserver-common = %{version}-%{release}
Requires:       perl-X2Go-Log = %{version}-%{release}
# We need a database
Requires(post): perl(DBD::SQLite)
Requires:       perl(DBD::SQLite)

%description -n perl-X2Go-Server-DB
X2Go is a server based computing environment with
    - session resuming
    - low bandwidth support
    - session brokerage support
    - client side mass storage mounting support
    - client side printing support
    - audio support
    - authentication by smartcard and USB stick

This package contains the X2Go::Server::DB Perl package.


%package -n perl-X2Go-Log
Summary:        Perl X2Go::Log package
Requires:       x2goserver-common = %{version}-%{release}
BuildArch:      noarch

%description -n perl-X2Go-Log
X2Go is a server based computing environment with
    - session resuming
    - low bandwidth support
    - session brokerage support
    - client side mass storage mounting support
    - client side printing support
    - audio support
    - authentication by smartcard and USB stick

This package contains the X2Go::Log Perl package.


%package -n x2goagent
Summary:        X2Go Server's X2Go Agent Xserver
Requires:       nxagent >= 3.5.99.17

%description -n x2goagent
X2Go is a server based computing environment with
    - session resuming
    - low bandwidth support
    - session brokerage support
    - client side mass storage mounting support
    - client side printing support
    - audio support
    - authentication by smartcard and USB stick

X2Go agent functionality has been completely incorporated into NX
agent's code base. If the nxagent binary is executed under the name of
`x2goagent', the X2Go functionalities get activated.

This package is a wrapper that activates X2Go branding in nxagent.
Please refer to the nxagent package's description for more information
on NX.


%package x2gokdrive
Summary:        X2Go Server's X2Go KDrive Xserver
Requires:       xorg-x11-server-x2gokdrive

%description x2gokdrive
X2Go is a server based computing environment with
    - session resuming
    - low bandwidth support
    - session brokerage support
    - client side mass storage mounting support
    - client side printing support
    - audio support
    - authentication by smartcard and USB stick

X2Go KDrive technology implements a remote X11 Xserver backend for
modern desktop environments, namely desktops derived from the GNOME
desktop shell.

X2Go KDrive does not require an XServer on the client-side, only the
X11-independent x2gokdriveclient. Desktop session data transfers from
server to client use differential image compression and image data gets
cached client-side.


%prep
%autosetup -p1

# Don't try to be root
sed -i -e 's/-o root -g root//' */Makefile


%build
export PATH=%{_qt4_bindir}:$PATH
%make_build CFLAGS="%{optflags}" PERL_INSTALLDIRS=vendor PREFIX=%{_prefix} NXLIBDIR=%{_libdir}/nx LIBDIR=%{_libdir}/x2go SBINDIR=%{_sbindir}


%install
make install DESTDIR=%{buildroot} PREFIX=%{_prefix} NXLIBDIR=%{_libdir}/nx LIBDIR=%{_libdir}/x2go SBINDIR=%{_sbindir}

# Make sure the .packlist file is removed from %%{perl_vendorarch}...
find %{buildroot}%{perl_vendorarch} -name .packlist -delete

# Remove placeholder files
rm %{buildroot}%{_libdir}/x2go/extensions/*.d/.placeholder

# x2gouser homedir, state dir
mkdir -p %{buildroot}%{_sharedstatedir}/x2go
# Create empty session file for %%ghost
touch %{buildroot}%{_sharedstatedir}/x2go/x2go_sessions

# Printing spool dir
mkdir -p %{buildroot}%{_localstatedir}/spool/x2goprint

%if 0%{?fedora} || 0%{?rhel} >= 7
# systemd session cleanup script
mkdir -p %{buildroot}%{_unitdir}
install -pm0644 %SOURCE1 %{buildroot}%{_unitdir}
%else
# SysV session cleanup script
mkdir -p %{buildroot}%{_initddir}
install -pm0755 %SOURCE2 %{buildroot}%{_initddir}/x2gocleansessions
%endif

desktop-file-validate %{buildroot}%{_datadir}/applications/x2gofm.desktop

# applications link
ln -s ../..%{_datadir}/applications %{buildroot}%{_sysconfdir}/x2go/applications

# Delete tmpfiles.d configuration file on systems not using systemd.
%if 0%{?rhel} && 0%{?rhel} == 6
rm -f %{buildroot}/etc/tmpfiles.d/x2goserver.conf
%endif


%pre common
getent group x2gouser >/dev/null || groupadd -r x2gouser
getent passwd x2gouser >/dev/null || \
    useradd -r -g x2gouser -d /var/lib/x2go -s /sbin/nologin \
    -c "x2go" x2gouser
exit 0

%post
# Initialize the session database
[ ! -s %{_sharedstatedir}/x2go/x2go_sessions ] &&
    grep -E "^backend=sqlite.*" /etc/x2go/x2gosql/sql >/dev/null 2>&1 &&
    %{_sbindir}/x2godbadmin --createdb >/dev/null 2>&1 || :

# Update the session database
[ -s %{_sharedstatedir}/x2go/x2go_sessions ] &&
    grep -E "^backend=sqlite.*" /etc/x2go/x2gosql/sql >/dev/null 2>&1 &&
    %{_sbindir}/x2godbadmin --updatedb >/dev/null 2>&1 || :

# create /etc/x2go/applications symlink if not already there
# as a regular file, as a symlink, as a special file or as a directory
if ! [ -e %{_sysconfdir}/x2go/applications ]; then
    ln -s ../..%{_datadir}/applications %{_sysconfdir}/x2go/applications
fi

%if 0%{?fedora} || 0%{?rhel} >= 7
%systemd_post x2gocleansessions.service
%else
/sbin/chkconfig --add x2gocleansessions
%endif

%preun
if [ "$1" = 0 ]; then
    if [ -L %{_sysconfdir}/x2go/applications ]; then
        rm -f %{_sysconfdir}/x2go/applications
    fi
fi

%if 0%{?fedora} || 0%{?rhel} >= 7
%systemd_preun x2gocleansessions.service
%else
if [ "$1" = 0 ]; then
    /sbin/service x2gocleansessions stop >/dev/null 2>&1
    /sbin/chkconfig --del x2gocleansessions
fi
%endif


%postun
%if 0%{?fedora} || 0%{?rhel} >= 7
%systemd_postun_with_restart x2gocleansessions.service
%else
if [ "$1" -ge "1" ] ; then
    /sbin/service x2gocleansessions condrestart >/dev/null 2>&1 || :
fi
%endif

%pre printing
getent group x2goprint >/dev/null || groupadd -r x2goprint
getent passwd x2goprint >/dev/null || \
    useradd -r -g x2goprint -d /var/spool/x2goprint -s /sbin/nologin \
    -c "x2go" x2goprint
exit 0


%files
%license COPYING
%doc ChangeLog README.md
%config(noreplace) %{_sysconfdir}/logcheck
%config(noreplace) %{_sysconfdir}/sudoers.d/x2goserver
%dir %{_sysconfdir}/x2go/
%ghost %config(noreplace) %{_sysconfdir}/x2go/applications
%config(noreplace) %{_sysconfdir}/x2go/x2goagent.options
%{_bindir}/x2go*
%exclude %{_bindir}/x2gofm
%exclude %{_bindir}/x2goprint
%exclude %{_bindir}/x2goagent
%exclude %{_bindir}/x2go*-desktopsharing
%dir %{_libdir}/x2go
%{_libdir}/x2go/extensions
%{_libdir}/x2go/x2gochangestatus
%{_libdir}/x2go/x2gocheckport
%{_libdir}/x2go/x2gocreatesession
%{_libdir}/x2go/x2gocreateshadowsession
%{_libdir}/x2go/x2gogetagent
%{_libdir}/x2go/x2gogetagentstate
%{_libdir}/x2go/x2gogetdisplays
%{_libdir}/x2go/x2gogetfreeport
%{_libdir}/x2go/x2gogetports
%{_libdir}/x2go/x2gogetrandomport
%{_libdir}/x2go/x2gogetstatus
%{_libdir}/x2go/x2goinsertport
%{_libdir}/x2go/x2goinsertsession
%{_libdir}/x2go/x2goinsertshadowsession
%{_libdir}/x2go/x2goisint
%{_libdir}/x2go/x2goistrue
%{_libdir}/x2go/x2golistsessions_sql
%{_libdir}/x2go/x2gologlevel
%{_libdir}/x2go/x2goqueryconfig
%{_libdir}/x2go/x2goresume
%{_libdir}/x2go/x2gormforward
%{_libdir}/x2go/x2gormport
%{_libdir}/x2go/x2gosuspend-agent
%{_libdir}/x2go/x2gosyslog
%{_sbindir}/x2go*
%{_mandir}/man1/x2gooptionsstring.1*
%{_mandir}/man8/x2go*.8*
%exclude %{_mandir}/man8/x2gofm.8*
%exclude %{_mandir}/man8/x2goprint.8*
%exclude %{_mandir}/man8/x2go*-desktopsharing.8*
%dir %{_datadir}/x2go/
%{_datadir}/x2go/versions/VERSION.x2goserver
%{_datadir}/x2go/versions/VERSION.x2goserver-extensions
%dir %{_datadir}/x2go/x2gofeature.d
%{_datadir}/x2go/x2gofeature.d/x2goserver.features
%{_datadir}/x2go/x2gofeature.d/x2goserver-extensions.features
%attr(0775,root,x2gouser) %dir %{_sharedstatedir}/x2go/
%ghost %attr(0660,root,x2gouser) %{_sharedstatedir}/x2go/x2go_sessions
%if 0%{?fedora} || 0%{?rhel} >= 7
%{_unitdir}/x2gocleansessions.service
%else
%{_initddir}/x2gocleansessions
%endif

%files common
%license COPYING
%doc ChangeLog
%attr(0775,root,x2gouser) %dir %{_localstatedir}/lib/x2go/
%if 0%{?rhel} != 6
%{_tmpfilesdir}/x2goserver.conf
%endif
%dir %{_sysconfdir}/x2go/
%dir %{_sysconfdir}/x2go/x2gosql
%dir %{_sysconfdir}/x2go/x2gosql/passwords
%config(noreplace) %{_sysconfdir}/x2go/x2goserver.conf
%config(noreplace) %{_sysconfdir}/x2go/x2gosql/sql
%config(noreplace) %{_sysconfdir}/x2go/x2go_logout*
%{_mandir}/man5/x2goserver.conf.5.gz
%dir %{_datadir}/x2go/versions
%{_datadir}/x2go/versions/VERSION.x2goserver-common

%files desktopsharing
%license COPYING
%doc ChangeLog
%{_bindir}/x2go*-desktopsharing
%{_datadir}/x2go/versions/VERSION.x2goserver-desktopsharing
%{_datadir}/x2go/x2gofeature.d/x2goserver-desktopsharing.features
%{_mandir}/man8/x2go*-desktopsharing.8*
%dir %{_sysconfdir}/x2go/desktopsharing
%config(noreplace) %{_sysconfdir}/x2go/desktopsharing/settings

%files fmbindings
%{_bindir}/x2gofm
%{_datadir}/applications/x2gofm.desktop
%{_datadir}/mime/packages/sshfs-x2go.xml
%{_datadir}/x2go/versions/VERSION.x2goserver-fmbindings
%{_datadir}/x2go/x2gofeature.d/x2goserver-fmbindings.features
%{_mandir}/man8/x2gofm.8*

%files printing
%{_bindir}/x2goprint
%{_datadir}/x2go/versions/VERSION.x2goserver-printing
%{_datadir}/x2go/x2gofeature.d/x2goserver-printing.features
%attr(0700,x2goprint,x2goprint) %{_localstatedir}/spool/x2goprint
%{_mandir}/man8/x2goprint.8*

%files xsession
%{_sysconfdir}/x2go/xinitrc.d
%{_sysconfdir}/x2go/Xclients.d
%{_sysconfdir}/x2go/Xresources
%config(noreplace) %{_sysconfdir}/x2go/Xsession
%{_datadir}/x2go/x2gofeature.d/x2goserver-xsession.features
%{_datadir}/x2go/versions/VERSION.x2goserver-xsession

%files -n perl-X2Go-Log
%license COPYING
%doc ChangeLog
%dir %{perl_vendorlib}/X2Go
%{perl_vendorlib}/X2Go/Log.pm
%{_mandir}/man3/X2Go::Log.*

%files -n perl-X2Go-Server
%license COPYING
%doc ChangeLog
%dir %{perl_vendorlib}/X2Go/Server
%{perl_vendorlib}/X2Go/Config.pm
%{perl_vendorlib}/X2Go/Server.pm
%{perl_vendorlib}/X2Go/SupeReNicer.pm
%{perl_vendorlib}/X2Go/Utils.pm
%{perl_vendorlib}/X2Go/Server/Agent*
%{_mandir}/man3/X2Go::Config.*
%{_mandir}/man3/X2Go::Server.*
%{_mandir}/man3/X2Go::SupeReNicer.*
%{_mandir}/man3/X2Go::Utils.*
%{_mandir}/man3/X2Go::Server::Agent.*
%{_mandir}/man3/X2Go::Server::Agent::*

%files -n perl-X2Go-Server-DB
%license COPYING
%doc ChangeLog
%dir %{_libdir}/x2go
%{perl_vendorlib}/X2Go/Server/DB*
%attr(2755,root,x2gouser) %{_libdir}/x2go/libx2go-server-db-sqlite3-wrapper
%{_libdir}/x2go/libx2go-server-db-sqlite3-wrapper.pl
%{_mandir}/man3/X2Go::Server::DB.*
%{_mandir}/man3/X2Go::Server::DB::*

%files -n x2goagent
%license COPYING
%doc ChangeLog
%{_bindir}/x2goagent
# %%{_libdir}/nx/bin/ is owned by nxagent package...
%{_libdir}/nx/bin/x2goagent
%{_datadir}/x2go/versions/VERSION.x2goserver-x2goagent
%{_datadir}/pixmaps/x2goagent.xpm
%{_datadir}/x2go/x2gofeature.d/x2goserver-x2goagent.features
%{_mandir}/man1/x2goagent.1*
%config(noreplace) %{_sysconfdir}/x2go/x2goagent.options
%config(noreplace) %{_sysconfdir}/x2go/keystrokes.cfg

%files x2gokdrive
%license COPYING
%doc ChangeLog
%{_datadir}/x2go/versions/VERSION.x2goserver-x2gokdrive
%{_datadir}/x2go/x2gofeature.d/x2goserver-x2gokdrive.features
%config(noreplace) %{_sysconfdir}/x2go/x2gokdrive.options


%changelog
* Fri Jan 24 2025 Orion Poplawski <orion@nwra.com> - 4.1.0.6-7
- Define SBINDIR for sbin merge (FTBFS rhbz#2341558)

* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.0.6-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 26 2024 Miroslav Suchý <msuchy@redhat.com> - 4.1.0.6-5
- convert license to SPDX

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.0.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.0.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Nov 25 2023 Orion Poplawski <orion@nwra.com> - 4.1.0.6-2
- Fix typo in description (bz#2251291)

* Fri Aug 18 2023 Orion Poplawski <orion@nwra.com> - 4.1.0.6-1
- Update to 4.1.0.6

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.0.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue May 30 2023 Orion Poplawski <orion@nwra.com> - 4.1.0.4-1
- Update to 4.1.0.4

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.0.3-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.0.3-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon May 30 2022 Jitka Plesnikova <jplesnik@redhat.com> - 4.1.0.3-18
- Perl 5.36 rebuild

* Fri Feb 04 2022 Orion Poplawski <orion@nwra.com> - 4.1.0.3-17
- Add upstream patch to fix x2goversion (bz#2050350)

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.0.3-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jan 19 2022 Orion Poplawski <orion@nwra.com> - 4.1.0.3-15
- Add Requires on xwininfo and xmessage (bz#2025390)

* Tue Nov 16 2021 René Genz <liebundartig@freenet.de> - 4.1.0.3-14
- fix typing mistakes

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.0.3-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri May 21 2021 Jitka Plesnikova <jplesnik@redhat.com> - 4.1.0.3-12
- Perl 5.34 rebuild

* Tue Mar 02 2021 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 4.1.0.3-11
- Rebuilt for updated systemd-rpm-macros
  See https://pagure.io/fesco/issue/2583.

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.0.3-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Nov 06 2020 Orion Poplawski <orion@nwra.com> - 4.1.0.3-9
- Change requires from xorg-x11-xkb-utils to setxkbmap (bz#1894794)

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.0.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jun 22 2020 Jitka Plesnikova <jplesnik@redhat.com> - 4.1.0.3-7
- Perl 5.32 rebuild

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.0.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.0.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu May 30 2019 Jitka Plesnikova <jplesnik@redhat.com> - 4.1.0.3-4
- Perl 5.30 rebuild

* Thu Apr 18 2019 Orion Poplawski <orion@nwra.com> - 4.1.0.3-3
- Upstream replaced netstat with ss in 4.1.0.0 (bugz#1496167)

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.0.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Nov 29 2018 Orion Poplawski <orion@nwra.com> - 4.1.0.3-1
- Update to 4.1.0.3

* Tue Aug 14 2018 Orion Poplawski <orion@nwra.com> - 4.1.0.2-1
- Update to 4.1.0.2

* Tue Jul 31 2018 Florian Weimer <fweimer@redhat.com> - 4.1.0.1-2
- Rebuild with fixed binutils

* Sun Jul 29 2018 Orion Poplawski <orion@nwra.com> - 4.1.0.1-1
- Update to 4.1.0.1

* Fri Jul 20 2018 Orion Poplawski <orion@nwra.com> - 4.1.0.0-4
- Add BR gcc

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Jun 27 2018 Jitka Plesnikova <jplesnik@redhat.com> - 4.1.0.0-2
- Perl 5.28 rebuild

* Mon Mar 5 2018 Orion Poplawski <orion@nwra.com> - 4.1.0.0-1
- Update to 4.1.0.0

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.1.22-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Nov 11 2017 Orion Poplawski <orion@cora.nwra.com> - 4.0.1.22-1
- Update to 4.0.1.22

* Wed Nov 8 2017 Orion Poplawski <orion@cora.nwra.com> - 4.0.1.21-1
- Update to 4.0.1.21

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.1.20-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.1.20-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Jun 04 2017 Jitka Plesnikova <jplesnik@redhat.com> - 4.0.1.20-3
- Perl 5.26 rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.1.20-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun Nov 20 2016 Orion Poplawski <orion@cora.nwra.com> - 4.0.1.20-1
- Update to 4.0.1.20
- Drop patches applied upstream

* Thu Oct 6 2016 Orion Poplawski <orion@cora.nwra.com> - 4.0.1.19-12
- Fix x2golistdesktops on EL7 (bug #1371690)

* Fri Jun 24 2016 Orion Poplawski <orion@cora.nwra.com> - 4.0.1.19-11
- Add upstream patch to drop blowfish cipher (bug #1350014)

* Sun May 15 2016 Jitka Plesnikova <jplesnik@redhat.com> - 4.0.1.19-10
- Perl 5.24 rebuild

* Fri Mar 18 2016 Orion Poplawski <orion@cora.nwra.com> - 4.0.1.19-9
- Add requires grep (bug #1319154)

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.1.19-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.0.1.19-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Jun 12 2015 Orion Poplawski <orion@cora.nwra.com> - 4.0.1.19-6
- Fix X2Go capitalization in service file (bug #1231177)

* Wed Jun 03 2015 Jitka Plesnikova <jplesnik@redhat.com> - 4.0.1.19-5
- Perl 5.22 rebuild

* Wed Apr 29 2015 Orion Poplawski <orion@cora.nwra.com> - 4.0.1.19-4
- Add requires xorg-x11-xkb-utils

* Sun Apr 26 2015 Orion Poplawski <orion@cora.nwra.com> - 4.0.1.19-3
- Install applications symlink by default so that "Published
  Applications" is populated (bug #1215474)

* Wed Mar 18 2015 Orion Poplawski <orion@cora.nwra.com> - 4.0.1.19-2
- Provide x2goserver-extensions for upstream compatibility

* Tue Feb 24 2015 Orion Poplawski <orion@cora.nwra.com> - 4.0.1.19-1
- Update to 4.0.1.19
- Drop Xsession and path patches fixed upstream

* Mon Jan 26 2015 Orion Poplawski <orion@cora.nwra.com> - 4.0.1.18-6
- Obsolete x2goserver-extensions to provide upgrade path from upstream rpms

* Thu Jan 8 2015 Orion Poplawski <orion@cora.nwra.com> - 4.0.1.18-5
- Fix local desktop sharing breakage (bug #1180303)

* Tue Dec 9 2014 Orion Poplawski <orion@cora.nwra.com> - 4.0.1.18-4
- Apply upstream fix for issue with Xsession aborting

* Fri Oct 24 2014 Orion Poplawski <orion@cora.nwra.com> - 4.0.1.18-3
- Do not require x2goserver-xession, do not ship feature file in main package

* Fri Oct 24 2014 Orion Poplawski <orion@cora.nwra.com> - 4.0.1.18-2
- Require x2goserver-xession

* Mon Oct 06 2014 Orion Poplawski <orion@cora.nwra.com> - 4.0.1.18-1
- Update to 4.0.1.18

* Fri Oct 03 2014 Orion Poplawski <orion@cora.nwra.com> - 4.0.1.17-1
- Update to 4.0.1.17

* Thu Oct 02 2014 Rex Dieter <rdieter@fedoraproject.org> 4.0.1.16-2
- -fmbindings: update mime scriptlets

* Thu Sep 25 2014 Orion Poplawski <orion@cora.nwra.com> - 4.0.1.16-1
- Update to 4.0.1.16

* Tue Sep 09 2014 Jitka Plesnikova <jplesnik@redhat.com> - 4.0.1.15-7
- Perl 5.20 mass

* Wed Aug 27 2014 Jitka Plesnikova <jplesnik@redhat.com> - 4.0.1.15-6
- Perl 5.20 rebuild

* Tue Aug 26 2014 Orion Poplawski <orion@cora.nwra.com> - 4.0.1.15-5
- Fix scriptlet requires

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.0.1.15-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.0.1.15-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri May 2 2014 Orion Poplawski <orion@cora.nwra.com> - 4.0.1.15-2
- Add Requires xorg-x11-xauth

* Thu Apr 3 2014 Orion Poplawski <orion@cora.nwra.com> - 4.0.1.15-1
- Update to 4.0.1.15

* Wed Apr 2 2014 Orion Poplawski <orion@cora.nwra.com> - 4.0.1.14-1
- Update to 4.0.1.14

* Mon Mar 24 2014 Orion Poplawski <orion@cora.nwra.com> - 4.0.1.13-4
- Create /tmp/.X11-unix with correct SELinux context (bug #1079772)

* Wed Feb 5 2014 Orion Poplawski <orion@cora.nwra.com> - 4.0.1.13-3
- Fix x2gocleansession.service unit file

* Mon Jan 27 2014 Orion Poplawski <orion@cora.nwra.com> - 4.0.1.13-2
- Fix xinitrd.d path in Xsession

* Sun Jan 26 2014 Orion Poplawski <orion@cora.nwra.com> - 4.0.1.13-1
- Update 4.0.1.13
- Add xsession sub-package

* Tue Jan 7 2014 Orion Poplawski <orion@cora.nwra.com> - 4.0.1.12-1
- Update 4.0.1.12

* Mon Jan 6 2014 Orion Poplawski <orion@cora.nwra.com> - 4.0.1.11-1
- Update 4.0.1.11
- Drop mimetype patch applied upstream

* Fri Jan 3 2014 Orion Poplawski <orion@cora.nwra.com> - 4.0.1.10-1
- Update to 4.0.1.10
- Drop pwgen and mktemp patches applied upstream

* Sat Dec 7 2013 Orion Poplawski <orion@cora.nwra.com> - 4.0.1.9-2
- Disable Xsession support for now - Debian specific (Bug #1038834)

* Mon Dec 2 2013 Orion Poplawski <orion@cora.nwra.com> - 4.0.1.9-1
- Update to 4.0.1.9
- Drop incorrect keyboard patch

* Wed Nov 27 2013 Orion Poplawski <orion@cora.nwra.com> - 4.0.1.8-2
- Use mktemp instead of tempfile
- BR xorg-x11-xinit for Xsession.d link creation
- Add patch to fix keyboard setting (bug #1033876)

* Sat Nov 23 2013 Orion Poplawski <orion@cora.nwra.com> - 4.0.1.8-1
- Update to 4.0.1.8
- Fix x2gocleansessions init script for EL6 (bug #1031150)

* Tue Oct 22 2013 Orion Poplawski <orion@cora.nwra.com> - 4.0.1.6-6
- Fix bug in x2gocleansessions init script, enable by default

* Wed Sep 11 2013 Orion Poplawski <orion@cora.nwra.com> - 4.0.1.6-5
- Add some needed requires

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.0.1.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue Jul 30 2013 Orion Poplawski <orion@cora.nwra.com> - 4.0.1.6-3
- Mark /var/lib/x2go as a directory
- Add patch to make the following changes:
- Remove Xsession.options
- Make /etc/x2go/Xsession.d point to /etc/X11/xinit/Xclients.d
- Make /etc/x2go/Xsession executable

* Mon Jul 29 2013 Orion Poplawski <orion@cora.nwra.com> - 4.0.1.6-2
- Add SysV init script for EL6

* Mon Jul 29 2013 Orion Poplawski <orion@cora.nwra.com> - 4.0.1.6-1
- Use 4.0.1.6 release
- Drop patches applied upstream

* Mon Jul 22 2013 Rok Mandeljc <rok.mandeljc@gmail.com> - 4.1.0.0-0.4.20130722git65169c9
- Update to latest git
- Use PREFIX=%%{_prefix} when building, not just when installing.
- Use pwgen instead of makepasswd, which is not available on Fedora.
- Fixed a missing function import in x2golistsessions.
- Added dependencies for xorg-x11-fonts-misc
- Added systemd script for session cleanup on start.
- Fixed x2goruncommand for TERMINAL -> gnome-terminal; the latter seems to return immediately in Fedora 19.

* Thu May 30 2013 Orion Poplawski <orion@cora.nwra.com> - 4.1.0.0-0.3.20130520gitbd2cfe4
- Update to latest git
- Split out printing sub-package

* Wed Jan 23 2013 Orion Poplawski <orion@cora.nwra.com> - 4.1.0.0-0.2.20130122git
- Add post script to create session database if needed

* Tue Jan 22 2013 Orion Poplawski <orion@cora.nwra.com> - 4.1.0.0-0.1.20130122git
- Update to 4.1.0.0 git

* Fri Jan 18 2013 Orion Poplawski <orion@cora.nwra.com> - 4.0.0.0-1
- Update to 4.0.0.0

* Tue Dec 11 2012 Orion Poplawski <orion@cora.nwra.com> - 3.1.1.9-1
- Initial Fedora package
