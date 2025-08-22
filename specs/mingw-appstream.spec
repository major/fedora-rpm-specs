%{?mingw_package_header}

Summary: Utilities to generate, maintain and access the AppStream database
Name:    mingw-appstream
Version: 1.0.6
Release: 1%{?dist}

# lib LGPLv2+, tools GPLv2+
License: GPL-2.0-or-later AND LGPL-2.1-or-later
#URL:     http://www.freedesktop.org/wiki/Distributions/AppStream
URL:     https://github.com/ximion/appstream
Source0: https://www.freedesktop.org/software/appstream/releases/AppStream-%{version}.tar.xz

Patch0002: 0001-Lower-native-appstream-requirement-for-now.patch

BuildArch: noarch
BuildRequires: meson >= 0.62
BuildRequires: git-core
BuildRequires: appstream-devel
BuildRequires: gperf
BuildRequires: gettext
BuildRequires: intltool
BuildRequires: itstool
BuildRequires: xmlto
BuildRequires: libxslt

BuildRequires: mingw32-filesystem >= 95
BuildRequires: mingw32-gcc-c++
BuildRequires: mingw32-cairo
BuildRequires: mingw32-freetype
BuildRequires: mingw32-fontconfig
BuildRequires: mingw32-gdk-pixbuf
BuildRequires: mingw32-glib2
BuildRequires: mingw32-curl
BuildRequires: mingw32-librsvg2
BuildRequires: mingw32-libxml2
BuildRequires: mingw32-pango
BuildRequires: mingw32-libxmlb
BuildRequires: mingw32-libyaml

BuildRequires: mingw64-filesystem >= 95
BuildRequires: mingw64-gcc-c++
BuildRequires: mingw64-cairo
BuildRequires: mingw64-freetype
BuildRequires: mingw64-fontconfig
BuildRequires: mingw64-gdk-pixbuf
BuildRequires: mingw64-glib2
BuildRequires: mingw64-curl
BuildRequires: mingw64-librsvg2
BuildRequires: mingw64-libxml2
BuildRequires: mingw64-pango
BuildRequires: mingw64-libxmlb
BuildRequires: mingw64-libyaml


%description
MinGW Windows appstream library.

%package -n mingw32-appstream
Summary: MinGW utilities to generate, maintain and access the AppStream database
BuildArch: noarch
%description -n mingw32-appstream
%{summary}.

%package -n mingw64-appstream
Summary: MinGW utilities to generate, maintain and access the AppStream database
BuildArch: noarch
%description -n mingw64-appstream
%{summary}.

%{?mingw_debug_package}


%prep
%autosetup -n AppStream-%{version} -S git_am


%build
%mingw_meson \
 -Dsystemd=false \
 -Dgir=false \
 -Dstemming=false \
 -Dapidocs=false \
 -Dinstall-docs=false \
 -Ddocs=false \
 -Dqt=false
%mingw_ninja

%install
%mingw_ninja_install
%mingw_find_lang %{name} --all-name


%files -n mingw32-appstream -f mingw32-%{name}.lang
%license COPYING
%{mingw32_bindir}/appstreamcli.exe
%{mingw32_bindir}/libappstream-5.dll
%{mingw32_mandir}/man1/appstreamcli.1*
%{mingw32_libdir}/libappstream.dll.a
%{mingw32_libdir}/pkgconfig/appstream.pc
%{mingw32_datadir}/metainfo/org.freedesktop.appstream.cli.*.xml
%dir %{mingw32_includedir}/appstream/
%{mingw32_includedir}/appstream/*.h
%dir %{mingw32_datadir}/appstream/
%{mingw32_datadir}/appstream/appstream.conf
%{mingw32_datadir}/gettext/its/metainfo.*
%dir %{mingw32_datadir}/installed-tests/appstream/
%{mingw32_datadir}/installed-tests/appstream/*

%files -n mingw64-appstream -f mingw64-%{name}.lang
%license COPYING
%{mingw64_bindir}/appstreamcli.exe
%{mingw64_bindir}/libappstream-5.dll
%{mingw64_mandir}/man1/appstreamcli.1*
%{mingw64_libdir}/libappstream.dll.a
%{mingw64_libdir}/pkgconfig/appstream.pc
%{mingw64_datadir}/metainfo/org.freedesktop.appstream.cli.*.xml
%dir %{mingw64_includedir}/appstream/
%{mingw64_includedir}/appstream/*.h
%dir %{mingw64_datadir}/appstream/
%{mingw64_datadir}/appstream/appstream.conf
%{mingw64_datadir}/gettext/its/metainfo.*
%dir %{mingw64_datadir}/installed-tests/appstream/
%{mingw64_datadir}/installed-tests/appstream/*

%changelog
* Wed Jul 30 2025 Marc-André Lureau <marcandre.lureau@redhat.com> - 1.0.6-1
- Initial MinGW package. Fixes: rhbz#2385230
