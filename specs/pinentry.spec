%if 0%{?fedora} && 0%{?fedora} < 39 || 0%{?rhel} && 0%{?rhel} < 10
%bcond_without gtk2
%endif

%if 0%{?fedora}
%bcond_without kf6
%endif


Name:    pinentry
Version: 1.3.3
Release: %{autorelease}
Summary: Collection of simple PIN or passphrase entry dialogs

License: GPL-2.0-or-later
URL:     https://www.gnupg.org/
Source0: https://gnupg.org/ftp/gcrypt/pinentry/%{name}-%{version}.tar.bz2
Source1: https://gnupg.org/ftp/gcrypt/pinentry/%{name}-%{version}.tar.bz2.sig
Source2: https://gnupg.org/signature_key.asc

Patch1: pinentry-1.1.1-coverity.patch

# borrowed from opensuse
Source10: pinentry-wrapper

BuildRequires: autoconf automake gettext-devel
BuildRequires: make
BuildRequires: gcc
BuildRequires: libcap-devel
BuildRequires: ncurses-devel
BuildRequires: libgpg-error-devel
BuildRequires: libassuan-devel
BuildRequires: pkgconfig(gcr-4)
BuildRequires: pkgconfig(libsecret-1)
%if %{with gtk2}
BuildRequires: pkgconfig(gtk+-2.0)
%endif
BuildRequires: pkgconfig(Qt6Core) pkgconfig(Qt6Gui) pkgconfig(Qt6Widgets)
%if %{with kf6}
BuildRequires: pkgconfig(KF6WindowSystem) pkgconfig(KF6GuiAddons)
%endif
BuildRequires: desktop-file-utils
BuildRequires: gnupg2

Provides: %{name}-curses = %{version}-%{release}

%description
Pinentry is a collection of simple PIN or passphrase entry dialogs which
utilize the Assuan protocol as described by the aegypten project; see
http://www.gnupg.org/aegypten/ for details.
This package contains the curses (text) based version of the PIN entry dialog.

%package gnome3
Summary: Passphrase/PIN entry dialog for GNOME 3
Requires: %{name} = %{version}-%{release}
Provides: %{name}-gui = %{version}-%{release}
%description gnome3
Pinentry is a collection of simple PIN or passphrase entry dialogs which
utilize the Assuan protocol as described by the aegypten project; see
http://www.gnupg.org/aegypten/ for details.
This package contains the GNOME 3 version of the PIN entry dialog.

%if %{with gtk2}
%package gtk
Summary: Passphrase/PIN entry dialog based on GTK+
Requires: %{name} = %{version}-%{release}
Provides: %{name}-gui = %{version}-%{release}
Provides: pinentry-gtk2 = %{version}-%{release}
%description gtk
Pinentry is a collection of simple PIN or passphrase entry dialogs which
utilize the Assuan protocol as described by the aegypten project; see
http://www.gnupg.org/aegypten/ for details.
This package contains the GTK GUI based version of the PIN entry dialog.
%endif

%package qt
Summary: Passphrase/PIN entry dialog based on Qt6
Requires: %{name} = %{version}-%{release}
Provides: %{name}-gui = %{version}-%{release}
Obsoletes: pinentry-qt4 < 0.8.0-2
Obsoletes: pinentry-qt5 < 1.2.1-7
Provides:  pinentry-qt6 = %{version}-%{release}
%if ! %{with gtk2}
# Special case to handle replacement of "default" pinentry implementation
Obsoletes: %{name}-gtk < %{version}-%{release}
%endif
%description qt
Pinentry is a collection of simple PIN or passphrase entry dialogs which
utilize the Assuan protocol as described by the aegypten project; see
http://www.gnupg.org/aegypten/ for details.
This package contains the Qt6 GUI based version of the PIN entry dialog.

%package emacs
Summary: Passphrase/PIN entry dialog based on emacs
Requires: %{name} = %{version}-%{release}
%description emacs
Pinentry is a collection of simple PIN or passphrase entry dialogs which
utilize the Assuan protocol as described by the aegypten project; see
http://www.gnupg.org/aegypten/ for details.
This package contains the emacs based version of the PIN entry dialog.

%package tty
Summary: Passphrase/PIN entry dialog in tty
Requires: %{name} = %{version}-%{release}
%description tty
Pinentry is a collection of simple PIN or passphrase entry dialogs which
utilize the Assuan protocol as described by the aegypten project; see
http://www.gnupg.org/aegypten/ for details.
This package contains the tty version of the PIN entry dialog.

%prep
%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup -p1


%build
export ACLOCAL_PATH=/usr/share/gettext/m4/
autoreconf -fiv
%configure \
  --disable-rpath \
  --disable-dependency-tracking \
  --without-libcap \
  --disable-pinentry-fltk \
  --enable-pinentry-gnome3 \
%if %{with gtk2}
  --enable-pinentry-gtk2 \
%else
  --disable-pinentry-gtk2 \
%endif
  --enable-pinentry-qt \
  --disable-pinentry-qt5 \
  --enable-pinentry-emacs \
  --enable-pinentry-tty \
  --enable-libsecret

%make_build


%install
%make_install

# Symlink for Backward compatibility
%if %{with gtk2}
ln -s pinentry-gtk-2 $RPM_BUILD_ROOT%{_bindir}/pinentry-gtk
%endif
ln -s pinentry-qt $RPM_BUILD_ROOT%{_bindir}/pinentry-qt4
ln -s pinentry-qt $RPM_BUILD_ROOT%{_bindir}/pinentry-qt5

install -p -m755 -D %{SOURCE10} $RPM_BUILD_ROOT%{_bindir}/pinentry

# unpackaged files
rm -fv $RPM_BUILD_ROOT%{_infodir}/dir

desktop-file-validate %{buildroot}/%{_datadir}/applications/org.gnupg.pinentry-qt.desktop
install -d %{buildroot}%{_datadir}/pixmaps

%files
%license COPYING
%doc AUTHORS ChangeLog NEWS README THANKS TODO
%{_bindir}/pinentry-curses
%{_bindir}/pinentry
%{_infodir}/pinentry.info*

%files gnome3
%{_bindir}/pinentry-gnome3

%if %{with gtk2}
%files gtk
%{_bindir}/pinentry-gtk-2
# symlink for backward compatibility
%{_bindir}/pinentry-gtk
%endif

%files qt
%{_bindir}/pinentry-qt
# symlinks for backward compatibility
%{_bindir}/pinentry-qt4
%{_bindir}/pinentry-qt5
%{_datadir}/applications/org.gnupg.pinentry-qt.desktop
%{_datadir}/pixmaps/pinentry.png

%files emacs
%{_bindir}/pinentry-emacs

%files tty
%{_bindir}/pinentry-tty

%changelog
%autochangelog
