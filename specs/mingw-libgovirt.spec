%{?mingw_package_header}

Name: mingw-libgovirt
Version: 0.3.8
Release: 11%{?dist}
Summary: MinGW support for a GObject library for interacting with oVirt REST API

License: LGPL-2.0-or-later
URL: https://gitlab.gnome.org/GNOME/libgovirt
Source: http://download.gnome.org/sources/libgovirt/0.3/libgovirt-%{version}.tar.xz

BuildArch: noarch

Requires: pkgconfig
Requires: glib2-devel
BuildRequires: make
BuildRequires: glib2-devel
BuildRequires: intltool
BuildRequires: mingw32-gcc
BuildRequires: mingw64-gcc
BuildRequires: mingw32-rest >= 0.7.92
BuildRequires: mingw64-rest >= 0.7.92

%description
libgovirt is a library that allows applications to use oVirt REST API
to list VMs managed by an oVirt instance, and to get the connection
parameters needed to make a SPICE/VNC connection to them.

%package -n     mingw32-libgovirt
Summary:        %{summary}

%description -n mingw32-libgovirt
libgovirt is a library that allows applications to use oVirt REST API
to list VMs managed by an oVirt instance, and to get the connection
parameters needed to make a SPICE/VNC connection to them.

%package -n     mingw32-libgovirt-static
Summary:        %{summary}
Requires:       mingw32-libgovirt = %{version}-%{release}

%description -n mingw32-libgovirt-static
libgovirt is a library that allows applications to use oVirt REST API
to list VMs managed by an oVirt instance, and to get the connection
parameters needed to make a SPICE/VNC connection to them.

%package -n     mingw64-libgovirt
Summary:        %{summary}

%description -n mingw64-libgovirt
libgovirt is a library that allows applications to use oVirt REST API
to list VMs managed by an oVirt instance, and to get the connection
parameters needed to make a SPICE/VNC connection to them.

%package -n     mingw64-libgovirt-static
Summary:        %{summary}
Requires:       mingw64-libgovirt = %{version}-%{release}

%description -n mingw64-libgovirt-static
libgovirt is a library that allows applications to use oVirt REST API
to list VMs managed by an oVirt instance, and to get the connection
parameters needed to make a SPICE/VNC connection to them.

%{?mingw_debug_package}

%prep
%setup -q -n libgovirt-%{version}

%build
%mingw_configure                            \
    --disable-gtk-doc                       \
    --with-introspection=no                 \
    --enable-static

%mingw_make %{?_smp_mflags} V=1

%install
%mingw_make_install "DESTDIR=$RPM_BUILD_ROOT" "INSTALL=install -p"

%mingw_find_lang libgovirt --all-name

# Libtool files don't need to be bundled
find $RPM_BUILD_ROOT -name "*.la" -delete

%files -n mingw32-libgovirt -f mingw32-libgovirt.lang
%doc AUTHORS COPYING MAINTAINERS README
%{mingw32_bindir}/libgovirt-2.dll
%{mingw32_libdir}/libgovirt.dll.a
%{mingw32_libdir}/pkgconfig/govirt-1.0.pc
%dir %{mingw32_includedir}/govirt-1.0/
%dir %{mingw32_includedir}/govirt-1.0/govirt/
%{mingw32_includedir}/govirt-1.0/govirt/*.h

%files -n mingw32-libgovirt-static
%{mingw32_libdir}/libgovirt.a

%files -n mingw64-libgovirt -f mingw64-libgovirt.lang
%doc AUTHORS COPYING MAINTAINERS README
%{mingw64_bindir}/libgovirt-2.dll
%{mingw64_libdir}/libgovirt.dll.a
%{mingw64_libdir}/pkgconfig/govirt-1.0.pc
%dir %{mingw64_includedir}/govirt-1.0/
%dir %{mingw64_includedir}/govirt-1.0/govirt/
%{mingw64_includedir}/govirt-1.0/govirt/*.h

%files -n mingw64-libgovirt-static
%{mingw64_libdir}/libgovirt.a

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.8-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.8-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jul 17 2024 Sandro Bonazzola <sbonazzo@redhat.com> - 0.3.8-9
- Fixes: fedora#2226010
- migrated to SPDX license

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.8-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.8-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.8-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.8-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.8-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Feb 24 2021 Eduardo Lima (Etrunko) <etrunko@redhat.com> - 0.3.8-1
- Sync with native libgovirt package

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Aug 12 13:42:14 GMT 2020 Sandro Mani <manisandro@gmail.com> - 0.3.7-3
- Rebuild (mingw-gettext)

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Feb 06 2020 Eduardo Lima (Etrunko) <etrunko@redhat.com> - 0.3.7-1
- Sync with native libgovirt package

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Jan 16 2019 Marc-André Lureau <marcandre.lureau@redhat.com> - 0.3.4-1
- new version

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Nov 24 2014 Fabiano Fidêncio <fidencio@redhat.com> 0.3.2-1
- Initial Fedora packaging
