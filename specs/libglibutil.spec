Name: libglibutil
Version: 1.0.79
Release: 2%{?dist}
Summary: Library of glib utilities
License: BSD
URL: https://github.com/sailfishos/libglibutil
Source0: %{url}/archive/refs/tags/%{version}.tar.gz

BuildRequires: pkgconfig
BuildRequires: pkgconfig(glib-2.0)
BuildRequires: make gcc

%description
Provides glib utility functions and macros

%package devel
Summary: Development library for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: pkgconfig

%description devel
This package contains the development library for %{name}.

%prep
%setup -q

%build
%make_build LIBDIR=%{_libdir} KEEP_SYMBOLS=1 release pkgconfig

%install
%{make_build} LIBDIR=%{_libdir} DESTDIR=%{buildroot} install-dev

%check
%{make_build} -C test test

%files
%license LICENSE
%{_libdir}/%{name}.so.*

%files devel
%{_libdir}/pkgconfig/*.pc
%{_libdir}/%{name}.so
%{_includedir}/gutil

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.79-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 19 2024 Alessandro Astone <ales.astone@gmail.com> - 1.0.79-1
- new version

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.76-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Feb 14 2024 Alessandro Astone <ales.astone@gmail.com> - 1.0.76-1
- new version

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.74-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.74-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Sep 16 2023 Alessandro Astone <ales.astone@gmail.com> - 1.0.74-1
- Update to 1.0.74

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.70-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jun 15 2023 Alessandro Astone <ales.astone@gmail.com> - 1.0.70-1
- Update to 1.0.70

* Tue Apr 25 2023 Alessandro Astone <ales.astone@gmail.com> - 1.0.69-1
- Update to 1.0.69

* Fri Feb 24 2023 Alessandro Astone <ales.astone@gmail.com> - 1.0.68-1
- Update to 1.0.68

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.67-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Oct 29 2022 Alessandro Astone <ales.astone@gmail.com> - 1.0.67-1
- Update to 1.0.67

* Mon Aug 22 2022 Benson Muite <benson_muite@emailplus.org> - 1.0.66-1
- Update to new release

* Sun Dec 12 2021 Mo 森 <rmnscnce@ya.ru> - 1.0.61-1
- Track a new upstream URL
- Use the 'make_build' macro
- 1.0.61
