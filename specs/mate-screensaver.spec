%global branch 1.28

Name:          mate-screensaver
Version:       %{branch}.0
Release:       %autorelease
Summary:       MATE Screensaver
# Automatically converted from old format: GPLv2+ and LGPLv2+ - review is highly recommended.
License:       GPL-2.0-or-later AND LicenseRef-Callaway-LGPLv2+
URL:           http://pub.mate-desktop.org
Source0:       http://pub.mate-desktop.org/releases/%{branch}/%{name}-%{version}.tar.xz

Patch1:        mate-screensaver_0001-add-the-number-of-minutes-for-GUI-settings-to-lock-t.patch
Patch2:        mate-screensaver_0002-mate-screensaver-preferences-Add-mnemonic-for-backgr.patch
Patch3:        mate-screensaver_0003-mate-screensaver-preferences-Cleanup-UI-file-after-l.patch
Patch4:        mate-screensaver_0004-mate-screensaver-preferences-Add-missing-mnemonic.patch
Patch5:        mate-screensaver_0005-mate-screensaver-preferences-Add-tooltip-for-lock-de.patch
Patch6:        mate-screensaver_0006-mate-screensaver-preferences-Improve-and-cleanup-tim.patch

Requires:      redhat-menus
Requires:      system-logos
Requires:      gnome-keyring-pam

BuildRequires: dbus-glib-devel
BuildRequires: desktop-file-utils
BuildRequires: gtk3-devel
BuildRequires: libX11-devel
BuildRequires: libXScrnSaver-devel
BuildRequires: libXinerama-devel
BuildRequires: libXmu-devel
BuildRequires: libXtst-devel
BuildRequires: libXxf86vm-devel
BuildRequires: libmatekbd-devel
BuildRequires: libnotify-devel
BuildRequires: make
BuildRequires: mate-common
BuildRequires: mate-desktop-devel
BuildRequires: mate-menus-devel
BuildRequires: mesa-libGL-devel
BuildRequires: pam-devel
BuildRequires: systemd-devel
BuildRequires: xorg-x11-proto-devel
BuildRequires: xmlto

%description
mate-screensaver is a screen saver and locker that aims to have
simple, sane, secure defaults and be well integrated with the desktop.


%package devel
Summary: Development files for mate-screensaver
Requires: %{name}%{?_isa} = %{version}-%{release}

%description devel
Development files for mate-screensaver


%prep
%autosetup -p1

#NOCONFIGURE=1 ./autogen.sh

%build
%configure                          \
            --with-x                \
            --disable-schemas-compile \
            --enable-docbook-docs   \
            --with-mit-ext          \
            --with-xf86gamma-ext    \
            --with-libgl            \
            --with-shadow           \
            --enable-locking        \
            --with-systemd          \
            --enable-pam            \
            --without-console-kit

make %{?_smp_mflags} V=1


%install
%{make_install}

desktop-file-install --delete-original             \
  --dir %{buildroot}%{_datadir}/applications    \
%{buildroot}%{_datadir}/applications/mate-screensaver-preferences.desktop

desktop-file-install                                          \
   --delete-original                                          \
   --dir %{buildroot}%{_datadir}/applications/screensavers    \
%{buildroot}%{_datadir}/applications/screensavers/*.desktop

# fix versioned doc dir
mkdir -p %{buildroot}%{_docdir}/mate-screensaver
mv %{buildroot}%{_docdir}/mate-screensaver-%{version}/mate-screensaver.html %{buildroot}%{_docdir}/mate-screensaver/mate-screensaver.html

%find_lang %{name} --with-gnome --all-name


%files -f %{name}.lang
%doc AUTHORS NEWS README COPYING
%{_bindir}/mate-screensaver*
%{_sysconfdir}/pam.d/mate-screensaver
%{_sysconfdir}/xdg/menus/mate-screensavers.menu
%{_sysconfdir}/xdg/autostart/mate-screensaver.desktop
%{_libexecdir}/mate-screensaver-*
%{_libexecdir}/mate-screensaver/
%{_datadir}/applications/mate-screensaver-preferences.desktop
%{_datadir}/applications/screensavers/*.desktop
%{_datadir}/mate-screensaver/
%{_datadir}/backgrounds/cosmos/
%{_datadir}/pixmaps/mate-logo-white.svg
%{_datadir}/pixmaps/gnome-logo-white.svg
%{_datadir}/desktop-directories/mate-screensaver.directory
%{_datadir}/glib-2.0/schemas/org.mate.screensaver.gschema.xml
%{_datadir}/mate-background-properties/cosmos.xml
%{_datadir}/dbus-1/services/org.mate.ScreenSaver.service
%{_docdir}/mate-screensaver/mate-screensaver.html
%{_mandir}/man1/*

%files devel
%{_libdir}/pkgconfig/*


%changelog
%autochangelog
