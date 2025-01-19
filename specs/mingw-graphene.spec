%{?mingw_package_header}

Name:           mingw-graphene
Version:        1.10.8
Release:        6%{?dist}
Summary:        Thin layer of types for graphic libraries

License:        MIT
URL:            https://github.com/ebassi/graphene
Source0:        %{url}/releases/download/%{version}/graphene-%{version}.tar.xz

BuildArch:      noarch

BuildRequires:  meson >= 0.50.1

BuildRequires:  mingw32-filesystem >= 107
BuildRequires:  mingw32-gcc-c++
BuildRequires:  mingw64-filesystem >= 107
BuildRequires:  mingw64-gcc-c++

BuildRequires:  mingw32-glib2
BuildRequires:  mingw64-glib2


%description
Graphene provides a small set of mathematical types needed to implement graphic
libraries that deal with 2D and 3D transformations and projections.

This package contains the MinGW Windows cross compiled graphene library.

%package -n mingw32-graphene
Summary:        MinGW Windows graphene library

%description -n mingw32-graphene
%{description}

%package -n mingw64-graphene
Summary:        MinGW Windows graphene library

%description -n mingw64-graphene
%{description}

%{?mingw_debug_package}


%prep
%autosetup -p1 -n graphene-%{version}


%build
%mingw_meson -Dintrospection=disabled
%mingw_ninja


%install
%mingw_ninja_install
rm -rf %{buildroot}%{mingw32_datadir}/installed-tests/
rm -rf %{buildroot}%{mingw64_datadir}/installed-tests/
rm -rf %{buildroot}%{mingw32_libexecdir}/installed-tests/
rm -rf %{buildroot}%{mingw64_libexecdir}/installed-tests/


%files -n mingw32-graphene
%license LICENSE.txt
%doc README.md
%{mingw32_libdir}/libgraphene-1.0.dll.a
%{mingw32_includedir}/graphene-1.0/
%dir %{mingw32_libdir}/graphene-1.0
%{mingw32_libdir}/graphene-1.0/include/
%{mingw32_bindir}/libgraphene-1.0-0.dll
%{mingw32_libdir}/pkgconfig/graphene-1.0.pc
%{mingw32_libdir}/pkgconfig/graphene-gobject-1.0.pc


%files -n mingw64-graphene
%license LICENSE.txt
%doc README.md
%{mingw64_libdir}/libgraphene-1.0.dll.a
%{mingw64_includedir}/graphene-1.0/
%dir %{mingw64_libdir}/graphene-1.0
%{mingw64_libdir}/graphene-1.0/include/
%{mingw64_bindir}/libgraphene-1.0-0.dll
%{mingw64_libdir}/pkgconfig/graphene-1.0.pc
%{mingw64_libdir}/pkgconfig/graphene-gobject-1.0.pc


%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.8-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.8-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.8-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Mon Jun 05 2023 Marc-André Lureau <marcandre.lureau@redhat.com> - 1.10.8-1
- Update to 1.10.8
  https://bugzilla.redhat.com/show_bug.cgi?id=2065973

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.6-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Mar 25 2022 Sandro Mani <manisandro@gmail.com> - 1.10.6-3
- Rebuild with mingw-gcc-12

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Mon Jan 03 2022 Marc-André Lureau <marcandre.lureau@redhat.com>
- Initial package. rhbz#2036610
