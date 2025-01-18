Name:           cmrt
Version:        1.0.6
Release:        24%{?dist}
Summary:        C for Media Runtime
License:        MIT
URL:            https://github.com/intel/cmrt
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz

Patch0:         cmrt-1.0.6_replace_obsolete_AC_PROG_LIBTOOL.patch

#This library depends on specific intel instructions like sse, avx…
ExclusiveArch:  %{ix86} x86_64 ia64

BuildRequires:  gcc-c++
BuildRequires:  libtool
BuildRequires:  pkgconfig(libdrm) >= 2.4.23
BuildRequires:  pkgconfig(libva) >= 0.34
BuildRequires: make


%description
Media GPU kernel manager for Intel G45 & HD Graphics family. Allows to
interface between Intel GPU's driver and a host program through a high 
level language.


%package devel
Summary:        Development files for the C for Media Runtime
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       pkgconfig


%description devel
Media GPU kernel manager for Intel G45 & HD Graphics family, 
development files.


%prep
%autosetup -p1


%build
autoreconf -vif
%configure
%make_build


%install
%make_install 
find %{buildroot} -name "*.la" -delete


%ldconfig_scriptlets


%files
%license AUTHORS COPYING
%doc NEWS README
%config(noreplace) %{_sysconfdir}/%{name}.conf
%{_libdir}/lib%{name}.so.*


%files devel
%{_includedir}/cm_rt.h
%{_includedir}/cm_rt_linux.h
%{_libdir}/lib%{name}.so
%{_libdir}/pkgconfig/libcmrt.pc


%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.6-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.6-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.6-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.6-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.6-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.6-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.6-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.6-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.6-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.6-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.6-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.6-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Sep 23 2019 Nicolas Chauvet <kwizart@gmail.com> - 1.0.6-12
- Rebuilt for libva

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.6-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.6-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.6-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jul 10 2018 Nicolas Chauvet <kwizart@gmail.com> - 1.0.6-8
- Switch github url

* Sun Feb 18 2018 Robert-André Mauchin <zebob.m@gmail.com> - 1.0.6-7
- Add missing BR for gcc-c++
- Use new ldconfig scriplets

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.6-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Jan 15 2018 Nicolas Chauvet <kwizart@gmail.com> - 1.0.6-5
- Rebuilt for libva-2.0.0

* Sat Aug 05 2017 Robert-André Mauchin <zebob.m@gmail.com> - 1.0.6-4
- Updated description

* Tue Jul 25 2017 Robert-André Mauchin <zebob.m@gmail.com> - 1.0.6-3
- Added patch to replace the obsolete AC_PROG_LIBTOOL

* Wed Jul 19 2017 Robert-André Mauchin <zebob.m@gmail.com> - 1.0.6-2
- Update to Fedora Packaging Guidelines specification

* Wed Jul 19 2017 Robert-André Mauchin <zebob.m@gmail.com> - 1.0.6-1
- First RPM release
