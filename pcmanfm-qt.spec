%global __cmake_in_source_build 1

Name:           pcmanfm-qt
Version:        1.3.0
Release:        %autorelease
Summary:        LxQt file manager PCManFM

License:        GPL-2.0-or-later
URL:            https://lxqt-project.org
VCS:            https://github.com/lxde/pcmanfm-qt
Source0:        %{vcs}/releases/download/%{version}/%{name}-%{version}.tar.xz

BuildRequires:  %{?fedora:cmake}%{!?fedora:cmake3} >= 3.0
BuildRequires:  desktop-file-utils
BuildRequires:  doxygen
BuildRequires:  gcc-c++
BuildRequires:  kf5-kwindowsystem-devel
BuildRequires:  make
BuildRequires:  pkgconfig(Qt5Help)
BuildRequires:  pkgconfig(Qt5X11Extras)
BuildRequires:  pkgconfig(exiv2)
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(gio-unix-2.0)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(libexif)
BuildRequires:  pkgconfig(libfm)
BuildRequires:  pkgconfig(libfm-qt)
BuildRequires:  pkgconfig(libmenu-cache)
BuildRequires:  pkgconfig(lxqt) >= 1.0.0
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xcb)
%if 0%{?el7}
BuildRequires:  devtoolset-7-gcc-c++
%endif
Requires:       lxqt-sudo

%if 0%{?fedora}
Requires:       desktop-backgrounds-compat
%endif
Obsoletes:      pcmanfm-qt5 < 0.9.0
Provides:       pcmanfm-qt5 = %{version}-%{release}
Obsoletes:      pcmanfm-qt4 <= 0.9.0
Obsoletes:      pcmanfm-qt-common <= 0.9.0

%if 0%{?fedora}
# gvfs is optional depencency at runtime, so we add a weak dependency here
Recommends:     gvfs
# configuration patched to use qterminal instead as the default terminal emulator but allow to use others
Requires:       qterminal
%endif

%description
PCManFM-Qt is a Qt-based file manager which uses GLib for file management. It
was started as the Qt port of PCManFM, the file manager of LXDE.

PCManFM-Qt is used by LXQt for handling the desktop. Nevertheless, it can also
be used independently of LXQt and under any desktop environment.

%package        l10n
Summary:        Translations for pcmanfm-qt
BuildArch:      noarch
Requires:       pcmanfm-qt = %{?epoch:%{epoch}:}%{version}-%{release}

%description    l10n
This package provides translations for the pcmanfm-qt package.

%prep
%autosetup -p1
sed '/Wallpaper=/c\Wallpaper=\%{datadir}\/backgrounds\/default.png' config/pcmanfm-qt/lxqt/settings.conf.in

%build
%if 0%{?el7}
scl enable devtoolset-7 - <<\EOF
%endif
mkdir -p %{_target_platform}
pushd %{_target_platform}
    %{cmake_lxqt} -DBUILD_DOCUMENTATION=ON -DPULL_TRANSLATIONS=NO -S .. -B .
popd

%{make_build} -C %{_target_platform}

%if 0%{?el7}
EOF
%endif

%install
make install/fast DESTDIR=%{buildroot} -C %{_target_platform}

for dfile in pcmanfm-qt-desktop-pref pcmanfm-qt; do
    desktop-file-edit \
        --remove-category=LXQt --add-category=X-LXQt \
        --remove-category=Help --add-category=X-Help \
        --remove-only-show-in=LXQt \
        %{buildroot}/%{_datadir}/applications/${dfile}.desktop
done

%find_lang %{name} --with-qt

%if 0%{?el7}
%post
/usr/bin/update-desktop-database &> /dev/null || :

%postun
/usr/bin/update-desktop-database &> /dev/null || :
%endif


%files
%doc AUTHORS CHANGELOG README.md
%license LICENSE
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/applications/%{name}-desktop-pref.desktop
%{_docdir}/%{name}
%{_mandir}/man1/%{name}.*
%{_sysconfdir}/xdg/autostart/lxqt-desktop.desktop
%{_datadir}/%{name}/lxqt/settings.conf
%{_datadir}/%{name}

%files l10n -f %{name}.lang
%doc AUTHORS CHANGELOG README.md
%dir %{_datadir}/%{name}/translations

%changelog
%autochangelog
