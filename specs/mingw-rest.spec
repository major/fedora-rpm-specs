%{?mingw_package_header}

Name:           mingw-rest
Version:        0.8.0
Release:        24%{?dist}
Summary:        A library for access to RESTful web services

# Automatically converted from old format: LGPLv2 - review is highly recommended.
License:        LicenseRef-Callaway-LGPLv2
URL:            https://wiki.gnome.org/Projects/Librest
Source0:        http://download.gnome.org/sources/rest/0.8/rest-%{version}.tar.xz

BuildArch:      noarch

BuildRequires: make
BuildRequires:  mingw32-filesystem >= 98
BuildRequires:  mingw64-filesystem >= 98
BuildRequires:  mingw32-gcc
BuildRequires:  mingw64-gcc
BuildRequires:  mingw32-binutils
BuildRequires:  mingw64-binutils
BuildRequires:  mingw32-glib2
BuildRequires:  mingw32-libsoup
BuildRequires:  mingw32-libxml2
BuildRequires:  mingw64-glib2
BuildRequires:  mingw64-libsoup
BuildRequires:  mingw64-libxml2

%description
This library was designed to make it easier to access web services that
claim to be "RESTful". A RESTful service should have urls that represent
remote objects, which methods can then be called on. The majority of services
don't actually adhere to this strict definition. Instead, their RESTful end
point usually has an API that is just simpler to use compared to other types
of APIs they may support (XML-RPC, for instance). It is this kind of API that
this library is attempting to support.

%package -n     mingw32-rest
Requires:       pkgconfig
Summary:        A library for access to RESTful web services

%description -n mingw32-rest
This library was designed to make it easier to access web services that
claim to be "RESTful". A RESTful service should have urls that represent
remote objects, which methods can then be called on. The majority of services
don't actually adhere to this strict definition. Instead, their RESTful end
point usually has an API that is just simpler to use compared to other types
of APIs they may support (XML-RPC, for instance). It is this kind of API that
this library is attempting to support.

%package -n     mingw32-rest-static
Requires:       pkgconfig
Requires:       mingw32-rest = %{version}-%{release}
Summary:        A library for access to RESTful web services

%description -n mingw32-rest-static
This library was designed to make it easier to access web services that
claim to be "RESTful". A RESTful service should have urls that represent
remote objects, which methods can then be called on. The majority of services
don't actually adhere to this strict definition. Instead, their RESTful end
point usually has an API that is just simpler to use compared to other types
of APIs they may support (XML-RPC, for instance). It is this kind of API that
this library is attempting to support.

%package -n     mingw64-rest
Requires:       pkgconfig
Summary:        A library for access to RESTful web services

%description -n mingw64-rest
This library was designed to make it easier to access web services that
claim to be "RESTful". A RESTful service should have urls that represent
remote objects, which methods can then be called on. The majority of services
don't actually adhere to this strict definition. Instead, their RESTful end
point usually has an API that is just simpler to use compared to other types
of APIs they may support (XML-RPC, for instance). It is this kind of API that
this library is attempting to support.

%package -n     mingw64-rest-static
Requires:       pkgconfig
Requires:       mingw64-rest = %{version}-%{release}
Summary:        A library for access to RESTful web services

%description -n mingw64-rest-static
This library was designed to make it easier to access web services that
claim to be "RESTful". A RESTful service should have urls that represent
remote objects, which methods can then be called on. The majority of services
don't actually adhere to this strict definition. Instead, their RESTful end
point usually has an API that is just simpler to use compared to other types
of APIs they may support (XML-RPC, for instance). It is this kind of API that
this library is attempting to support.

%{?mingw_debug_package}

%prep
%setup -q -n rest-%{version}

%build
%mingw_configure                            \
    --disable-gtk-doc                       \
    --enable-introspection=no               \
    --enable-static

%mingw_make %{?_smp_mflags} V=1

%install
%mingw_make install "DESTDIR=$RPM_BUILD_ROOT" INSTALL="install -p"

# Libtool files don't need to be bundled
find $RPM_BUILD_ROOT -name "*.la" -delete

%files -n mingw32-rest
%license COPYING
%doc AUTHORS README
%{mingw32_bindir}/librest-0.7-0.dll
%{mingw32_libdir}/librest-0.7.dll.a
%{mingw32_bindir}/librest-extras-0.7-0.dll
%{mingw32_libdir}/librest-extras-0.7.dll.a
%{mingw32_libdir}/pkgconfig/rest*
%{mingw32_includedir}/rest-0.7

%files -n mingw32-rest-static
%{mingw32_libdir}/librest-0.7.a
%{mingw32_libdir}/librest-extras-0.7.a

%files -n mingw64-rest
%license COPYING
%doc AUTHORS README
%{mingw64_bindir}/librest-0.7-0.dll
%{mingw64_libdir}/librest-0.7.dll.a
%{mingw64_bindir}/librest-extras-0.7-0.dll
%{mingw64_libdir}/librest-extras-0.7.dll.a
%{mingw64_libdir}/pkgconfig/rest*
%{mingw64_includedir}/rest-0.7

%files -n mingw64-rest-static
%{mingw64_libdir}/librest-0.7.a
%{mingw64_libdir}/librest-extras-0.7.a

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.0-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Sep 02 2024 Miroslav Suchý <msuchy@redhat.com> - 0.8.0-23
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.0-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.0-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.0-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.0-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.0-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.0-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Mar 25 2022 Sandro Mani <manisandro@gmail.com> - 0.8.0-16
- Rebuild with mingw-gcc-12

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.0-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Aug 12 13:45:37 GMT 2020 Sandro Mani <manisandro@gmail.com> - 0.8.0-12
- Rebuild (mingw-gettext)

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Nov 07 2019 Marc-André Lureau <marcandre.lureau@redhat.com> - 0.8.0-9
- Add back libsoup-gnome dependency

* Thu Nov 07 2019 Marc-André Lureau <marcandre.lureau@redhat.com> - 0.8.0-8
- Rebuild to drop libsoup-gnome dependency

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Sep 16 2016 Kalev Lember <klember@redhat.com> - 0.8.0-1
- Update to 0.8.0
- Use license macro for COPYING
- Don't set group tags

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.92-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.92-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Nov 24 2014 Fabiano Fidêncio <fidencio@redhat.com> 0.7.92-1
- Initial Fedora packaging
