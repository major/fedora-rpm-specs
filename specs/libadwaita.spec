%bcond mingw %[0%{?fedora} && !0%{?flatpak}]

%global apiver  1
%global gtk_version 4.17.5
%global glib_version 2.80.0

%global tarball_version %%(echo %{version} | tr '~' '.')

Name:           libadwaita
Version:        1.8~beta
Release:        %autorelease
Summary:        Building blocks for modern GNOME applications

# part of src/adw-spring-animation.c is MIT
License:        LGPL-2.1-or-later AND MIT
URL:            https://gitlab.gnome.org/GNOME/libadwaita
Source0:        https://download.gnome.org/sources/%{name}/1.8/%{name}-%{tarball_version}.tar.xz

BuildRequires:  desktop-file-utils
BuildRequires:  gcc
BuildRequires:  gettext
BuildRequires:  gi-docgen
BuildRequires:  libappstream-glib
BuildRequires:  meson >= 0.63.0
BuildRequires:  vala
BuildRequires:  /usr/bin/sassc
BuildRequires:  pkgconfig(appstream)
BuildRequires:  pkgconfig(fribidi)
BuildRequires:  pkgconfig(glib-2.0) >= %{glib_version}
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(gtk4) >= %{gtk_version}

Requires:       gtk4%{?_isa} >= %{gtk_version}

%if %{with mingw}
BuildRequires:  mingw32-filesystem >= 95
BuildRequires:  mingw32-gcc-c++
BuildRequires:  mingw32-gtk4 >= %{gtk_version}
BuildRequires:  mingw32-appstream

BuildRequires:  mingw64-filesystem >= 95
BuildRequires:  mingw64-gcc-c++
BuildRequires:  mingw64-gtk4 >= %{gtk_version}
BuildRequires:  mingw64-appstream
%endif

%description
Building blocks for modern GNOME applications.


%package        devel
Summary:        Development files for %{name}

Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       vala
Recommends:     %{name}-demo = %{version}-%{release}
Recommends:     %{name}-doc = %{version}-%{release}

%description    devel
Development files for %{name}.


%package        doc
Summary:        Documentation files for %{name}
BuildArch:      noarch

Recommends:     %{name}-devel = %{version}-%{release}
# Because web fonts from upstream are not bundled in the gi-docgen package,
# packages containing documentation generated with gi-docgen should depend on
# this metapackage to ensure the proper system fonts are present.
Recommends:     gi-docgen-fonts

%description    doc
Documentation files for %{name}.


%package        demo
Summary:        Demo files for %{name}
BuildArch:      noarch

Requires:       %{name} = %{version}-%{release}
Suggests:       %{name}-devel = %{version}-%{release}

%description    demo
Demo files for %{name}.


%if %{with mingw}
%package -n mingw32-%{name}
Summary:       MinGW Windows %{name} library

%description -n mingw32-%{name}
MinGW Windows %{name} library.

%package -n mingw64-%{name}
Summary:       MinGW Windows %{name} library

%description -n mingw64-%{name}
MinGW Windows %{name} library.
%endif


%prep
%autosetup -p1 -n %{name}-%{tarball_version}


%build
%meson \
    -Ddocumentation=true \
    %{nil}
%meson_build

%if %{with mingw}
%mingw_meson -Dintrospection=disabled -Dtests=false -Ddocumentation=false -Dexamples=true
%mingw_ninja
%endif

%install
%meson_install
%if %{with mingw}
%mingw_ninja_install
%endif

%find_lang %{name}


%check
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/*.xml
desktop-file-validate %{buildroot}%{_datadir}/applications/*.desktop


%files -f %{name}.lang
%license COPYING
%doc README.md AUTHORS NEWS
%{_bindir}/adwaita-%{apiver}-demo
%{_libdir}/%{name}-%{apiver}.so.0
%{_libdir}/girepository-1.0/*.typelib

%files devel
%dir %{_datadir}/gir-1.0
%{_datadir}/gir-1.0/*-%{apiver}.gir
%{_datadir}/vala/vapi/%{name}-%{apiver}.*
%{_includedir}/%{name}-%{apiver}/
%{_libdir}/%{name}-%{apiver}.so
%{_libdir}/pkgconfig/*-%{apiver}.pc

%files doc
%{_docdir}/%{name}-%{apiver}/

%files demo
%{_datadir}/applications/*.desktop
%{_datadir}/icons/hicolor/*/apps/*.svg
%{_metainfodir}/*.metainfo.xml


%if %{with mingw}
%files -n mingw32-libadwaita
%license COPYING
%doc README.md AUTHORS NEWS
%{mingw32_bindir}/%{name}-%{apiver}-0.dll
%{mingw32_bindir}/adwaita-%{apiver}-demo.exe
%{mingw32_libdir}/%{name}-%{apiver}.dll.a
%{mingw32_libdir}/pkgconfig/*-%{apiver}.pc
%{mingw32_includedir}/%{name}-%{apiver}/
%{mingw32_datadir}/applications/*.desktop
%{mingw32_datadir}/icons/hicolor/*/apps/*.svg
%{mingw32_datadir}/metainfo/*.metainfo.xml

%files -n mingw64-libadwaita
%license COPYING
%doc README.md AUTHORS NEWS
%{mingw64_bindir}/%{name}-%{apiver}-0.dll
%{mingw64_bindir}/adwaita-%{apiver}-demo.exe
%{mingw64_libdir}/%{name}-%{apiver}.dll.a
%{mingw64_libdir}/pkgconfig/*-%{apiver}.pc
%{mingw64_includedir}/%{name}-%{apiver}/
%{mingw64_datadir}/applications/*.desktop
%{mingw64_datadir}/icons/hicolor/*/apps/*.svg
%{mingw64_datadir}/metainfo/*.metainfo.xml
%endif

%changelog
%autochangelog
