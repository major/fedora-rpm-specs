Name:          kaffeine
Version:       2.0.18
Release:       %autorelease -b 9
License:       GPL-2.0-or-later AND GFDL-1.3-or-later
Summary:       KDE media player based on VLC
URL:           https://apps.kde.org/kaffeine/
Source:        https://download.kde.org/%{stable_kf5}/%{name}/%{name}-%{version}.tar.xz

BuildRequires: desktop-file-utils
BuildRequires: extra-cmake-modules
BuildRequires: gettext
BuildRequires: kf5-rpm-macros
BuildRequires: libappstream-glib

BuildRequires: cmake(Qt5Core)
BuildRequires: cmake(Qt5Widgets)
BuildRequires: cmake(Qt5Network)
BuildRequires: cmake(Qt5Sql)
BuildRequires: cmake(Qt5X11Extras)

BuildRequires: cmake(KF5CoreAddons)
BuildRequires: cmake(KF5I18n)
BuildRequires: cmake(KF5WidgetsAddons)
BuildRequires: cmake(KF5WindowSystem)
BuildRequires: cmake(KF5XmlGui)
BuildRequires: cmake(KF5KIO)
BuildRequires: cmake(KF5Solid)
BuildRequires: cmake(KF5DBusAddons)
BuildRequires: cmake(KF5DocTools)

BuildRequires: pkgconfig(xscrnsaver)
BuildRequires: pkgconfig(libvlc)
BuildRequires: pkgconfig(libdvbv5)

%if 0%{?fedora} >= 40 || 0%{?rhel} >= 10
Requires:      kio-extras-kf5%{?_isa}
%else
Requires:      kio-extras%{?_isa}
%endif
# Needed for open file dialog translations
Requires:      qt5-qttranslations
Requires:      vlc-plugins-base%{?_isa}
Requires:      vlc-plugins-video-out%{?_isa}
Recommends:    vlc-plugin-ffmpeg%{?_isa}
Recommends:    (vlc-plugin-gnome%{?_isa} if gnome-keyring%{?_isa})
Recommends:    (vlc-plugin-kde%{?_isa} if kf5-kwallet%{?_isa})
Recommends:    (vlc-plugin-pulseaudio%{?_isa} or vlc-plugin-pipewire%{?_isa})

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:   %{ix86}

%description
Kaffeine is a KDE media player. Kaffeine has user-friendly interface,
so that even first time users can start immediately playing their movies
from DVD (including DVD menus, titles, chapters, etc.), VCD, or a file.


%prep
%autosetup -p1

%build
%cmake_kf5
%cmake_build


%install
%cmake_install

%find_lang %{name} --with-qt --with-man --with-html --all-name


%check
desktop-file-validate %{buildroot}%{_kf5_datadir}/applications/org.kde.kaffeine.desktop
appstream-util validate-relax --nonet %{buildroot}%{_kf5_metainfodir}/org.kde.kaffeine.appdata.xml


%files -f %{name}.lang
%doc README.md
%license COPYING COPYING-DOCS
%{_kf5_bindir}/kaffeine
%{_kf5_datadir}/kaffeine/
%{_kf5_datadir}/applications/org.kde.kaffeine.desktop
%{_kf5_datadir}/icons/hicolor/*/*/*
%{_kf5_datadir}/profiles/kaffeine.profile.xml
%{_kf5_datadir}/solid/actions/*.desktop
%{_kf5_mandir}/man1/kaffeine.1.*
%{_kf5_metainfodir}/org.kde.kaffeine.appdata.xml


%changelog
%autochangelog
