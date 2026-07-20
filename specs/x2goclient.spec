Name:           x2goclient
Version:        4.1.2.3
Release:        %autorelease
Summary:        X2Go Client application

# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
URL:            http://www.x2go.org
Source0:        http://code.x2go.org/releases/source/%{name}/%{name}-%{version}.tar.gz
Source1:        org.x2go.X2GoClient.metainfo.xml
# Drop clumsy attempt at Kerberos delegation
# http://bugs.x2go.org/cgi-bin/bugreport.cgi?bug=731
Patch0:         x2goclient-krb5.patch
# ensure RPM_LD_FLAGS/RPM_OPT_FLAGS are used
# https://bugzilla.redhat.com/show_bug.cgi?id=1306463
Patch2:         x2goclient-optflags.patch
# Select X11 backend on wayland
# https://bugzilla.redhat.com/show_bug.cgi?id=1756430
# https://bugs.x2go.org/cgi-bin/bugreport.cgi?bug=1414
Patch4:         0001-Select-X11-backend-on-wayland.patch
# Also fix desktop files created by session manager
# https://bugzilla.redhat.com/show_bug.cgi?id=1820989
Patch5:         0002-Select-X11-backend-for-desktop-files-created-by-sess.patch

BuildRequires: make
BuildRequires:  gcc-c++
BuildRequires:  cups-devel
BuildRequires:  desktop-file-utils
BuildRequires:  libappstream-glib
BuildRequires:  libssh-devel
BuildRequires:  libXpm-devel
BuildRequires:  man2html-core
BuildRequires:  openldap-devel
BuildRequires:  pkgconfig(Qt5)
BuildRequires:  pkgconfig(Qt5Svg)
BuildRequires:  pkgconfig(Qt5X11Extras)
BuildRequires:  qt5-linguist
Requires:       hicolor-icon-theme
Requires:       nxproxy
# For GSSAPI authenticated connections
Requires:       openssh-clients
# For local folder sharing and printing
Requires:       openssh-server
Obsoletes:      x2goplugin < 4.1.2.1
ExcludeArch:    %{ix86}

%description
X2Go is a server-based computing environment with
    - session resuming
    - low bandwidth support
    - session brokerage support
    - client-side mass storage mounting support
    - client-side printing support
    - audio support
    - authentication by smartcard and USB stick

X2Go Client is a graphical client for the X2Go system.
You can use it to connect to running sessions and start new sessions.


%prep
%autosetup -p1
# Fix up install issues
sed -i -e 's/-o root -g root//' Makefile
sed -i -e '/^MOZPLUGDIR=/s/lib/%{_lib}/' Makefile
sed -i -e '/^MAKEOVERRIDES *=/d' Makefile
sed -i -e 's/qt4/qt5/' Makefile
sed -i -e '/^LIBS /s/$/ -ldl/' x2goclient.pro


%build
export PATH=%{_qt5_bindir}:$PATH
%make_build


%install
%make_install PREFIX=%{_prefix}
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop

install -D -p -m644 %{SOURCE1} %{buildroot}%{_metainfodir}/org.x2go.X2GoClient.metainfo.xml
appstream-util validate-relax \
  --nonet %{buildroot}%{_metainfodir}/org.x2go.X2GoClient.metainfo.xml

mkdir -p %{buildroot}%{_sysconfdir}/httpd/conf.d


%files
%license COPYING LICENSE 
%doc AUTHORS
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/128x128/apps/%{name}.png
%{_datadir}/icons/hicolor/16x16/apps/%{name}.png
%{_datadir}/icons/hicolor/32x32/apps/%{name}.png
%{_datadir}/icons/hicolor/64x64/apps/%{name}.png
%{_datadir}/mime/packages/x-x2go.xml
%{_datadir}/%{name}/
%{_mandir}/man1/%{name}.1.gz
%{_metainfodir}/org.x2go.X2GoClient.metainfo.xml


%changelog
%autochangelog
