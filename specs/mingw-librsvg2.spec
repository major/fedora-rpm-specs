%{?mingw_package_header}

Name:           mingw-librsvg2
Version:        2.57.1
Release:        5%{?dist}
Summary:        SVG library based on cairo for MinGW

License:        LGPL-2.0-or-later
URL:            https://wiki.gnome.org/Projects/LibRsvg
BuildArch:      noarch
Source0:        https://download.gnome.org/sources/librsvg/2.57/librsvg-%{version}.tar.xz
# tar xf librsvg-${version}.tar.xz
# cd librsvg-${version}
# cargo vendor
# tar cfJ ../librsvg-${version}-vendor.tar.xz vendor
Source1:        librsvg-%{version}-vendor.tar.xz
# Add missing link libs
Patch0:         librsvg_libs.patch


BuildRequires:  cargo
BuildRequires:  make
BuildRequires:  automake

BuildRequires:  mingw32-filesystem >= 95
BuildRequires:  mingw32-gcc
BuildRequires:  mingw32-gdk-pixbuf
BuildRequires:  mingw32-glib2
BuildRequires:  mingw32-gtk3
BuildRequires:  mingw32-libcroco
BuildRequires:  mingw32-pango
BuildRequires:  rust-std-static-i686-pc-windows-gnu

BuildRequires:  mingw64-filesystem >= 95
BuildRequires:  mingw64-gcc
BuildRequires:  mingw64-gdk-pixbuf
BuildRequires:  mingw64-glib2
BuildRequires:  mingw64-gtk3
BuildRequires:  mingw64-libcroco
BuildRequires:  mingw64-pango
BuildRequires:  rust-std-static-x86_64-pc-windows-gnu

# we need to call the host gdk-pixbuf-query-loaders executable
BuildRequires:  gdk-pixbuf2
BuildRequires:  perl-File-Temp

%description
An SVG library based on cairo for MinGW.

%package -n mingw32-librsvg2
Summary:        MinGW SVG library based on cairo
Requires:       pkgconfig

%description -n mingw32-librsvg2
This package contains the header files and libraries needed to develop
applications that use librsvg2.


%package -n mingw32-librsvg2-static
Summary:        MinGW SVG static library based on cairo
Requires:       mingw32-librsvg2 = %{version}-%{release}

%description -n mingw32-librsvg2-static
This package contains the static libraries needed to develop
applications that use librsvg2.


%package -n mingw64-librsvg2
Summary:        MinGW SVG library based on cairo
Requires:       pkgconfig

%description -n mingw64-librsvg2
This package contains the header files and libraries needed to develop
applications that use librsvg2.


%package -n mingw64-librsvg2-static
Summary:        MinGW static color daemon
Requires:       mingw64-librsvg2 = %{version}-%{release}

%description -n mingw64-librsvg2-static
This package contains the static libraries needed to develop
applications that use librsvg2.

%{?mingw_debug_package}


%prep
%autosetup -p1 -n librsvg-%{version} -a1

mkdir -p .cargo
cat > .cargo/config.toml <<EOF
[source.crates-io]
replace-with = "vendored-sources"

[source.vendored-sources]
directory = "vendor"
EOF


%build
MINGW32_CONFIGURE_ARGS="RUST_TARGET=i686-pc-windows-gnu" \
MINGW64_CONFIGURE_ARGS="RUST_TARGET=x86_64-pc-windows-gnu" \
%mingw_configure \
        --disable-gtk-doc \
        --enable-introspection=no \
        --without-pic
%mingw_make_build


%install
%mingw_make_install

find %{buildroot} -name "*.la" -delete

# Delete docs already part of native package
rm -rf %{buildroot}%{mingw32_datadir}/man
rm -rf %{buildroot}%{mingw32_datadir}/gtk-doc
rm -rf %{buildroot}%{mingw32_datadir}/doc/librsvg
rm -rf %{buildroot}%{mingw64_datadir}/man
rm -rf %{buildroot}%{mingw64_datadir}/gtk-doc
rm -rf %{buildroot}%{mingw64_datadir}/doc/librsvg


%files -n mingw32-librsvg2
%license COPYING.LIB
%{mingw32_bindir}/librsvg-2-2.dll
%{mingw32_bindir}/rsvg-convert.exe
%{mingw32_includedir}/librsvg-2.0
%{mingw32_libdir}/gdk-pixbuf-2.0/2.10.0/loaders/libpixbufloader-svg.dll
%{mingw32_libdir}/gdk-pixbuf-2.0/2.10.0/loaders/libpixbufloader-svg.dll.a
%{mingw32_libdir}/librsvg-2.dll.a
%{mingw32_libdir}/pkgconfig/*.pc
%dir %{mingw32_datadir}/thumbnailers
%{mingw32_datadir}/thumbnailers/librsvg.thumbnailer

%files -n mingw32-librsvg2-static
%{mingw32_libdir}/gdk-pixbuf-2.0/2.10.0/loaders/libpixbufloader-svg.a
%{mingw32_libdir}/librsvg-2.a


%files -n mingw64-librsvg2
%license COPYING.LIB
%{mingw64_bindir}/librsvg-2-2.dll
%{mingw64_bindir}/rsvg-convert.exe
%{mingw64_includedir}/librsvg-2.0
%{mingw64_libdir}/gdk-pixbuf-2.0/2.10.0/loaders/libpixbufloader-svg.dll
%{mingw64_libdir}/gdk-pixbuf-2.0/2.10.0/loaders/libpixbufloader-svg.dll.a
%{mingw64_libdir}/librsvg-2.dll.a
%{mingw64_libdir}/pkgconfig/*.pc
%dir %{mingw64_datadir}/thumbnailers
%{mingw64_datadir}/thumbnailers/librsvg.thumbnailer

%files -n mingw64-librsvg2-static
%{mingw64_libdir}/gdk-pixbuf-2.0/2.10.0/loaders/libpixbufloader-svg.a
%{mingw64_libdir}/librsvg-2.a


%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.57.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.57.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.57.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.57.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Dec 18 2023 Sandro Mani <manisandro@gmail.com> - 2.57.1-1
- Update to 2.57.1

* Tue Oct 03 2023 Sandro Mani <manisandro@gmail.com> - 2.57.0-1
- Update to 2.57.0

* Wed Aug 23 2023 Sandro Mani <manisandro@gmail.com> - 2.56.92-1
- Update to 2.56.92

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.56.90-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jul 04 2023 Sandro Mani <manisandro@gmail.com> - 2.56.90-1
- Update to 2.56.90

* Thu Jun 01 2023 Sandro Mani <manisandro@gmail.com> - 2.56.1-1
- Update to 2.56.1

* Fri Mar 31 2023 Sandro Mani <manisandro@gmail.com> - 2.56.0-1
- Update to 2.56.0

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.55.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Tue Nov 22 2022 Sandro Mani <manisandro@gmail.com> - 2.55.1-1
- Update to 2.55.1

* Tue Aug 30 2022 Sandro Mani <manisandro@gmail.com> - 2.54.5-1
- Update to 2.54.5

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.54.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jun 15 2022 Sandro Mani <manisandro@gmail.com> - 2.54.4-1
- Update to 2.54.4

* Fri May 20 2022 Sandro Mani <manisandro@gmail.com> - 2.54.3-1
- Update to 2.54.3

* Tue Apr 26 2022 Sandro Mani <manisandro@gmail.com> - 2.54.1-1
- Update to 2.54.1

* Fri Mar 25 2022 Sandro Mani <manisandro@gmail.com> - 2.54.0-2
- Rebuild with mingw-gcc-12

* Thu Mar 17 2022 Sandro Mani <manisandro@gmail.com> - 2.54.0-1
- Update to 2.54.0

* Tue Mar 15 2022 Sandro Mani <manisandro@gmail.com> - 2.53.2-1
- Update to 2.53.2

* Tue Mar 08 2022 Sandro Mani <manisandro@gmail.com> - 2.53.1-2
- Rebuild to fix missing entry point error

* Mon Feb 14 2022 Sandro Mani <manisandro@gmail.com> - 2.53.1-1
- Update to 2.53.1

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.53.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Mon Jan 10 2022 Sandro Mani <manisandro@gmail.com> - 2.53.0-1
- Update to 2.53.0

* Sat Jan 08 2022 Sandro Mani <manisandro@gmail.com> - 2.52.5-1
- Update to 2.52.5

* Tue Oct 26 2021 Sandro Mani <manisandro@gmail.com> - 2.52.1-1
- Update to 2.52.1

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.40.21-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Mar 02 2021 David King <amigadave@amigadave.com> - 2.40.21-1
- Update to 2.40.21

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.40.19-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Aug 12 13:43:13 GMT 2020 Sandro Mani <manisandro@gmail.com> - 2.40.19-9
- Rebuild (mingw-gettext)

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.40.19-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Apr 20 2020 Sandro Mani <manisandro@gmail.com> - 2.40.19-7
- Rebuild (gettext)

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.40.19-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.40.19-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.40.19-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.40.19-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.40.19-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sun Oct 15 2017 Kalev Lember <klember@redhat.com> - 2.40.19-1
- Update to 2.40.19

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.40.18-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Thu Jul 20 2017 Kalev Lember <klember@redhat.com> - 2.40.18-1
- Update to 2.40.18

* Tue Jun 20 2017 Kalev Lember <klember@redhat.com> - 2.40.17-1
- Update to 2.40.17

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.40.16-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Sep 16 2016 Kalev Lember <klember@redhat.com> - 2.40.16-1
- Update to 2.40.16

* Tue May 03 2016 Kalev Lember <klember@redhat.com> - 2.40.15-1
- Update to 2.40.15

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.40.12-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Dec 02 2015 David King <amigadave@amigadave.com> - 2.40.12-1
- Update to 2.40.12

* Sat Nov 21 2015 David King <amigadave@amigadave.com> - 2.40.11-1
- Update to 2.40.11

* Sat Aug 29 2015 David King <amigadave@amigadave.com> - 2.40.10-1
- Update to 2.40.10

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.40.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Apr 21 2015 David King <amigadave@amigadave.com> - 2.40.9-1
- Update to 2.40.9

* Fri Mar 13 2015 David King <amigadave@amigadave.com> - 2.40.8-1
- Update to 2.40.8
- Use license macro for COPYING
- Update URL

* Wed Nov 19 2014 Richard Hughes <richard@hughsie.com> - 2.40.6-1
- Initial packaging attempt
