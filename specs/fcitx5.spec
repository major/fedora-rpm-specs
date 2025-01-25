%global _xinputconf %{_sysconfdir}/X11/xinit/xinput.d/fcitx5.conf
%global __provides_exclude_from ^%{_libdir}/%{name}/.*\\.so$

Name:           fcitx5
Version:        5.1.12
Release:        %autorelease
Summary:        Next generation of fcitx
# Automatically converted from old format: LGPLv2+ - review is highly recommended.
License:        LicenseRef-Callaway-LGPLv2+
URL:            https://github.com/fcitx/fcitx5
Source:         https://download.fcitx-im.org/fcitx5/fcitx5/fcitx5-%{version}_dict.tar.zst
Source1:        https://download.fcitx-im.org/fcitx5/fcitx5/fcitx5-%{version}_dict.tar.zst.sig
# Checked by chatting, this key is used to verify fcitx* tarballs
Source2:        https://pgp.key-server.io/download/0x8E8B898CBF2412F9
Source3:        fcitx5-xinput
Source4:        fcitx5.sh

BuildRequires:  cmake
BuildRequires:  ninja-build
BuildRequires:  gnupg2
BuildRequires:  desktop-file-utils
BuildRequires:  extra-cmake-modules
BuildRequires:  gcc-c++
BuildRequires:  systemd-rpm-macros
BuildRequires:  pkgconfig(cairo)
BuildRequires:  pkgconfig(cldr-emoji-annotation)
BuildRequires:  pkgconfig(dri)
BuildRequires:  pkgconfig(enchant-2)
BuildRequires:  pkgconfig(expat)
BuildRequires:  pkgconfig(fmt)
BuildRequires:  pkgconfig(gdk-pixbuf-2.0)
BuildRequires:  pkgconfig(iso-codes)
BuildRequires:  pkgconfig(json-c)
BuildRequires:  pkgconfig(pango)
BuildRequires:  pkgconfig(uuid)
BuildRequires:  pkgconfig(libsystemd)
BuildRequires:  pkgconfig(wayland-egl)
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(wayland-protocols)
BuildRequires:  pkgconfig(xcb)
BuildRequires:  pkgconfig(xkbcommon-x11)
BuildRequires:  pkgconfig(xkbfile)
BuildRequires:  pkgconfig(xcb-ewmh)
BuildRequires:  pkgconfig(xcb-imdkit)
BuildRequires:  pkgconfig(xcb-icccm)
BuildRequires:  pkgconfig(xcb-keysyms)
BuildRequires:  pkgconfig(xkeyboard-config)
BuildRequires:  /usr/bin/appstream-util
Requires:       dbus-common
Requires:       %{name}-data = %{version}-%{release}
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}
Requires:       setup
Requires(post):     %{_sbindir}/alternatives
Requires(postun):   %{_sbindir}/alternatives

Recommends:       (fcitx5-gtk if (gtk2 or gtk3 or gtk4))
Recommends:       (fcitx5-qt if (qt5-qtbase or qt6-qtbase))
Recommends:       (fcitx5-qt-module if (qt5-qtbase or qt6-qtbase))
Recommends:       fcitx5-configtool

%description
Fcitx 5 is a generic input method framework released under LGPL-2.1+.

%package libs
Summary:        Libraries for %{name}

%description libs
The %{name}-libs package contains runtime shared libraries necessary for
running programs using Fcitx5 libraries.

%package data
Summary:        Data files of Fcitx5
BuildArch:      noarch
# require with isa will lead to problem on koji build
Requires:       %{name} = %{version}-%{release}
Requires:       hicolor-icon-theme
Requires:       dbus

%description data
The %{name}-data package provides shared data for Fcitx5.

%package devel
Summary:        Development files for %{name}
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

%description devel
The %{name}-devel package contains libraries and header files necessary for
developing programs using Fcitx5 libraries.

%package autostart
Summary:        This package will make fcitx5 start with your GUI session
BuildArch:      noarch
Requires:       %{name} = %{version}-%{release}

%description autostart
This package will setup autostart and environment needed for fcitx5 to work properly.

%prep
%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup -p1

%build
%cmake -GNinja
%cmake_build 

%install
%cmake_install
install -pm 644 -D %{S:3} %{buildroot}%{_xinputconf}
install -pm 644 -D %{S:4} %{buildroot}%{_sysconfdir}/profile.d/fcitx5.sh
install -d                %{buildroot}%{_datadir}/%{name}/inputmethod
install -d                %{buildroot}%{_datadir}/%{name}/table
desktop-file-install --delete-original \
  --dir %{buildroot}%{_datadir}/applications \
  %{buildroot}%{_datadir}/applications/%{name}-configtool.desktop
 
desktop-file-install --delete-original \
  --dir %{buildroot}%{_datadir}/applications \
  %{buildroot}%{_datadir}/applications/org.fcitx.Fcitx5.desktop

desktop-file-install --delete-original \
  --dir %{buildroot}%{_datadir}/applications \
  %{buildroot}%{_datadir}/applications/%{name}-wayland-launcher.desktop
  
# convert symlinked icons to copied icons, this will help co-existing with
# fcitx4
for iconfile in $(find %{buildroot}%{_datadir}/icons -type l)
do
  origicon=$(readlink -f ${iconfile})
  rm -f ${iconfile}
  cp ${origicon} ${iconfile}
done 
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/*.metainfo.xml
%find_lang %{name}

%check
%ctest

%post
%{_sbindir}/alternatives --install %{_sysconfdir}/X11/xinit/xinputrc xinputrc %{_xinputconf} 55 || :

%postun
if [ "$1" = "0" ]; then
  %{_sbindir}/alternatives --remove xinputrc %{_xinputconf} || :
  # if alternative was set to manual, reset to auto
  [ -L %{_sysconfdir}/alternatives/xinputrc -a "`readlink %{_sysconfdir}/alternatives/xinputrc`" = "%{_xinputconf}" ] && %{_sbindir}/alternatives --auto xinputrc || :
fi

%files -f %{name}.lang
%license LICENSES/LGPL-2.1-or-later.txt
%doc README.md 
%config %{_xinputconf}
%{_bindir}/%{name}
%{_bindir}/%{name}-configtool
%{_bindir}/%{name}-remote
%{_bindir}/%{name}-diagnose
%{_libdir}/%{name}/
%{_libexecdir}/fcitx5-wayland-launcher
%{_sysconfdir}/xdg/Xwayland-session.d/20-fcitx-x11

%files libs
%license LICENSES/LGPL-2.1-or-later.txt
%{_libdir}/libFcitx5*.so.*.*
%{_libdir}/libFcitx5Config.so.6
%{_libdir}/libFcitx5Core.so.7
%{_libdir}/libFcitx5Utils.so.2

%files devel
%{_includedir}/Fcitx5/
%{_libdir}/cmake/Fcitx5*
%{_libdir}/libFcitx5*.so
%{_libdir}/pkgconfig/Fcitx5*.pc


%files data
%{_datadir}/%{name}
%{_datadir}/dbus-1/services/org.fcitx.Fcitx5.service
%{_datadir}/applications/org.fcitx.Fcitx5.desktop
%{_metainfodir}/org.fcitx.Fcitx5.metainfo.xml
%{_datadir}/applications/%{name}-configtool.desktop
%{_datadir}/applications/%{name}-wayland-launcher.desktop
%{_datadir}/icons/hicolor/*/apps/*

%files autostart
%config %{_sysconfdir}/xdg/autostart/org.fcitx.Fcitx5.desktop
%config %{_sysconfdir}/profile.d/fcitx5.sh

%changelog
%autochangelog
