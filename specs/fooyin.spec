Name:           fooyin
Version:        0.9.2
Release:        %autorelease
Summary:        A customizable music player

License:        GPL-3.0-or-later
URL:            https://www.fooyin.org/
Source0:        https://github.com/fooyin/fooyin/archive/v%{version}/fooyin-%{version}.tar.gz
Patch0:         https://github.com/fooyin/fooyin/commit/c93d58283121c6aed44d137d88f5837f6995bbee.patch
Patch1:         https://github.com/fooyin/fooyin/commit/9a8573cdd55691fb996d3bfa542d6b63cb78e6f2.patch

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6Widgets)
BuildRequires:  cmake(Qt6Gui)
BuildRequires:  cmake(Qt6Sql)
BuildRequires:  cmake(Qt6Concurrent)
BuildRequires:  cmake(Qt6Network)
BuildRequires:  cmake(Qt6Svg)
BuildRequires:  cmake(Qt6LinguistTools)
BuildRequires:  cmake(KDSingleApplication-qt6)
BuildRequires:  pkgconfig(icu-uc)
BuildRequires:  pkgconfig(icu-i18n)
BuildRequires:  pkgconfig(taglib)
BuildRequires:  pkgconfig(libavcodec)
BuildRequires:  pkgconfig(libavfilter)
BuildRequires:  pkgconfig(libavformat)
BuildRequires:  pkgconfig(libavutil)
BuildRequires:  pkgconfig(libswresample)
BuildRequires:  pkgconfig(alsa)
BuildRequires:  pkgconfig(libpipewire-0.3)
BuildRequires:  pkgconfig(sdl2)
BuildRequires:  pkgconfig(sndfile)
BuildRequires:  pkgconfig(libopenmpt)
BuildRequires:  pkgconfig(libgme)
BuildRequires:  pkgconfig(libarchive)
BuildRequires:  pkgconfig(libebur128)
BuildRequires:  cmake(GTest)
BuildRequires:  desktop-file-utils
BuildRequires:  libappstream-glib
Requires:       hicolor-icon-theme

%description
fooyin is a music player built around customization. It provides a variety
of widgets to help you manage and play your local collection.

%package devel
Summary:        Support for developing fooyin plugins
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
This package provides development files used to create plugins for fooyin.

%prep
%autosetup -p1

%build
%cmake -DBUILD_LIBVGM=OFF -DBUILD_TESTING=ON -DINSTALL_HEADERS=ON
%cmake_build

%install
%cmake_install
%find_lang fooyin --with-qt
rm %{buildroot}%{_docdir}/fooyin/LICENSE
rm %{buildroot}%{_docdir}/fooyin/README

%check
%ctest --test-dir %{_vpath_builddir}/tests/
desktop-file-validate %{buildroot}%{_datadir}/applications/*.desktop
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/*.metainfo.xml

%files -f fooyin.lang
%license COPYING
%doc README.md
%doc CHANGELOG.md
%{_bindir}/fooyin
%{_libdir}/fooyin/libfooyin_utils.so.0.0.0
%{_libdir}/fooyin/libfooyin_core.so.0.0.0
%{_libdir}/fooyin/libfooyin_gui.so.0.0.0
%{_libdir}/fooyin/plugins/
%{_datadir}/applications/org.fooyin.fooyin.desktop
%{_datadir}/icons/hicolor/*/apps/org.fooyin.fooyin.*
%{_metainfodir}/org.fooyin.fooyin.metainfo.xml
%dir %{_libdir}/fooyin/
%dir %{_datadir}/fooyin/
%dir %{_datadir}/fooyin/translations/

%files devel
%{_includedir}/fooyin/
%{_libdir}/fooyin/libfooyin_utils.so
%{_libdir}/fooyin/libfooyin_core.so
%{_libdir}/fooyin/libfooyin_gui.so
%{_libdir}/cmake/fooyin/

%changelog
%autochangelog
