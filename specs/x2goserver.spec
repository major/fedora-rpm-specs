#global commit 3a0d285b225207b3eccbb7b0ec3f27a2fbdc5be3

Name:           x2goserver
Version:        4.1.0.6
Release:        %autorelease
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
BuildRequires:  man2html-core
BuildRequires:  systemd
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
Requires(post): coreutils
Requires(post): grep
Requires(post): perl-X2Go-Server-DB
Requires(post): x2goserver-common

%{?systemd_requires}

Suggests:       x2goserver-fmbindings = %{version}-%{release}
Suggests:       x2goserver-printing = %{version}-%{release}
Requires:       x2goserver-xsession = %{version}-%{release}

# Provide upgrade path from upstream rpms
# http://bugs.x2go.org/cgi-bin/bugreport.cgi?bug=755
Obsoletes:      x2goserver-extensions < %{version}-%{release}
Provides:       x2goserver-extensions = %{version}-%{release}
Requires:       x2goserver-xsession
Suggests:       x2goserver-fmbindings
Suggests:       x2goserver-printing

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
Requires:       dbus
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

# Create a sysusers.d config file
cat >x2goserver.sysusers.conf <<EOF
u x2gouser - 'x2go' /var/lib/x2go -
EOF

# Create a sysusers.d config file for x2goprint
cat >x2goprint.sysusers.conf <<EOF
u x2goprint - "X2Go print spooler user" /var/spool/x2goprint /sbin/nologin
EOF


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

# systemd session cleanup script
mkdir -p %{buildroot}%{_unitdir}
install -pm0644 %SOURCE1 %{buildroot}%{_unitdir}

desktop-file-validate %{buildroot}%{_datadir}/applications/x2gofm.desktop

# applications link
ln -s ../..%{_datadir}/applications %{buildroot}%{_sysconfdir}/x2go/applications

install -m0644 -D x2goserver.sysusers.conf %{buildroot}%{_sysusersdir}/x2goserver.conf
install -m0644 -D x2goprint.sysusers.conf %{buildroot}%{_sysusersdir}/x2goprint.conf


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

%systemd_post x2gocleansessions.service

%preun
if [ "$1" = 0 ]; then
    if [ -L %{_sysconfdir}/x2go/applications ]; then
        rm -f %{_sysconfdir}/x2go/applications
    fi
fi

%systemd_preun x2gocleansessions.service


%postun
%systemd_postun_with_restart x2gocleansessions.service


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
%{_mandir}/man1/x2gooptionsstring.1*
%{_mandir}/man8/x2go*.8*
%exclude %{_mandir}/man8/x2gofm.8*
%exclude %{_mandir}/man8/x2goprint.8*
%exclude %{_mandir}/man8/x2go*-desktopsharing.8*
%if 0%{?fedora} && 0%{?fedora} < 42 || 0%{?rhel} && 0%{?rhel} < 11
%{_sbindir}/x2go*
%endif
%dir %{_datadir}/x2go/
%{_datadir}/x2go/versions/VERSION.x2goserver
%{_datadir}/x2go/versions/VERSION.x2goserver-extensions
%dir %{_datadir}/x2go/x2gofeature.d
%{_datadir}/x2go/x2gofeature.d/x2goserver.features
%{_datadir}/x2go/x2gofeature.d/x2goserver-extensions.features
%attr(0775,root,x2gouser) %dir %{_sharedstatedir}/x2go/
%ghost %attr(0660,root,x2gouser) %{_sharedstatedir}/x2go/x2go_sessions
%{_unitdir}/x2gocleansessions.service

%files common
%license COPYING
%doc ChangeLog
%attr(0775,root,x2gouser) %dir %{_localstatedir}/lib/x2go/
%{_tmpfilesdir}/x2goserver.conf
%dir %{_sysconfdir}/x2go/
%dir %{_sysconfdir}/x2go/x2gosql
%dir %{_sysconfdir}/x2go/x2gosql/passwords
%config(noreplace) %{_sysconfdir}/x2go/x2goserver.conf
%config(noreplace) %{_sysconfdir}/x2go/x2gosql/sql
%config(noreplace) %{_sysconfdir}/x2go/x2go_logout*
%{_mandir}/man5/x2goserver.conf.5.gz
%dir %{_datadir}/x2go/versions
%{_datadir}/x2go/versions/VERSION.x2goserver-common
%{_sysusersdir}/x2goserver.conf

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
%{_sysusersdir}/x2goprint.conf

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
%autochangelog
