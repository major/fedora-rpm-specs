Summary: Rendering of internationalized text for SDL2 (Simple DirectMedia Layer)
Name: SDL2_Pango
Version: 2.1.5
Release: 3%{?dist}
License: LGPL-2.1-or-later
URL: https://github.com/markuskimius/SDL2_Pango

Source0: https://github.com/markuskimius/SDL2_Pango/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires: gcc make
BuildRequires: pango-devel
BuildRequires: SDL2-devel

%description
SDL2_Pango is a library for graphically rendering
internationalized and tagged text in SDL2 using TrueType fonts.


%package devel
Summary: Development files for SDL2_pango
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: pango-devel%{?_isa}
Requires: SDL2-devel%{?_isa}
Requires: pkgconfig

%description devel
Development files for SDL2_pango.


%prep
%setup -q


%build
%configure --disable-static
make %{?_smp_mflags}


%install
make install DESTDIR=%{buildroot}


%ldconfig_scriptlets


%files
%license COPYING
%doc AUTHORS ChangeLog NEWS README
%{_libdir}/*.so.4*

%files devel
%doc docs/html/*
%{_includedir}/SDL2_Pango.h
%{_libdir}/pkgconfig/SDL2_Pango.pc
%{_libdir}/*.so


%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jan 26 2024 Gwyn Ciesla <gwync@protonmail.com> - 2.1.5-1
- 2.1.5

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Aug 26 2022 Gwyn Ciesla <gwync@protonmail.com> - 2.1.4-2
- Review fixes.

* Thu Aug 18 2022 Gwyn Ciesla <gwync@protonmail.com> - 2.1.4-1
- Initial build.
