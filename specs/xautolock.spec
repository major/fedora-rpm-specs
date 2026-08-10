Name:           xautolock
Version:        2.2
Release:        %autorelease
Summary:        Launches a program when your X session has been idle

# Automatically converted from old format: GPLv2 - review is highly recommended.
License:        GPL-2.0-only
URL:            http://freshmeat.net/projects/xautolock/
Source0:        http://www.ibiblio.org/pub/Linux/X11/screensavers/%{name}-%{version}.tgz
Patch0:         xautolock-2.2-XSS-fix.patch
# All of Debian's patches look pretty sane, so let's swipe 'em
# All by Roland Stigge, except 14 by Aurelien Jarno
Patch1:         https://sources.debian.org/data/main/x/xautolock/1:2.2-5.1/debian/patches/10-fix-memory-corruption.patch
Patch2:         https://sources.debian.org/data/main/x/xautolock/1:2.2-5.1/debian/patches/11-fix-no-dpms.patch
Patch3:         https://sources.debian.org/data/main/x/xautolock/1:2.2-5.1/debian/patches/12-fix-manpage.patch
Patch4:         https://sources.debian.org/data/main/x/xautolock/1:2.2-5.1/debian/patches/13-fix-hppa-build.patch
Patch5:         https://sources.debian.org/data/main/x/xautolock/1:2.2-5.1/debian/patches/14-do-not-use-union-wait-type.patch

# See RHBZ#956271. Local change; worth upstreaming?
Patch100:       xautolock-longer-times.patch
ExcludeArch:    %{ix86}

BuildRequires:  gcc
BuildRequires:  imake
BuildRequires:  libXScrnSaver-devel
BuildRequires:  make

%description
A program that launches a given program when
your X session has been idle for a given time.


%prep
%autosetup -p1
xmkmf


%build
%make_build CDEBUGFLAGS="%{optflags}" LOCAL_LDFLAGS="%{build_ldflags}" CC="%{__cc}"


%install
make install install.man DESTDIR=%{buildroot} INSTALL="install -p"


%check


%files
%doc Changelog License Readme Todo
%{_bindir}/xautolock
%{_mandir}/man1/xautolock.1*


%changelog
%autochangelog
