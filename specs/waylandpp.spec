Name:           waylandpp
Version:        1.0.0
Release:        8%{?dist}
Summary:        Wayland C++ bindings

# waylandpp includes part of Wayland under MIT, wayland-scanner++ is GPLv3+
# Automatically converted from old format: BSD and MIT and GPLv3+ - review is highly recommended.
License:        LicenseRef-Callaway-BSD AND LicenseRef-Callaway-MIT AND GPL-3.0-or-later
URL:            https://github.com/NilsBrause/%{name}/
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz
# Fix build with GCC 13
Patch0:         %{name}-1.0.0-gcc13.patch

BuildRequires:  cmake
BuildRequires:  doxygen
BuildRequires:  gcc-c++
BuildRequires:  mesa-libEGL-devel
BuildRequires:  pkgconfig(pugixml)
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(wayland-cursor)
BuildRequires:  pkgconfig(wayland-egl)
BuildRequires:  pkgconfig(wayland-server)

%description
Wayland is an object oriented display protocol, which features request and
events. Requests can be seen as method calls on certain objects, whereas events
can be seen as signals of an object. This makes the Wayland protocol a perfect
candidate for a C++ binding.

The goal of this library is to create such a C++ binding for Wayland using the
most modern C++ technology currently available, providing an easy to use C++ API
to Wayland.


%package devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
The %{name}-devel package contains libraries and header files for developing
applications that use %{name}.


%package doc
Summary:        Documentation for %{name}
BuildArch:      noarch

%description doc
The %{name}-doc package contains development documentation for %{name}.


%prep
%autosetup -p0


%build
%cmake -DCMAKE_INSTALL_DOCDIR=%{_defaultdocdir}/%{name}-doc/
%cmake_build


%install
%cmake_install

# Drop LaTeX documentation (HTML documentation is already built)
rm -r $RPM_BUILD_ROOT%{_defaultdocdir}/%{name}-doc/latex/


%check
%ctest


%files
%doc README.md
%license LICENSE
%{_libdir}/*.so.*


%files devel
%doc example/
%{_bindir}/wayland-scanner++
%{_libdir}/*.so
%{_libdir}/cmake/%{name}/
%{_libdir}/pkgconfig/*.pc
%{_includedir}/*
%{_datadir}/%{name}/
%{_mandir}/man3/*.3.*


%files doc
%doc README.md
%license LICENSE
%{_defaultdocdir}/%{name}-doc/*


%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Sep 04 2024 Miroslav Suchý <msuchy@redhat.com> - 1.0.0-7
- convert license to SPDX

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sun Mar 26 2023 Mohamed El Morabity <melmorabity@fedoraproject.org> - 1.0.0-3
- Fix build with GCC 13

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Oct 05 2022 Mohamed El Morabity <melmorabity@fedoraproject.org> - 1.0.0-1
- Update to 1.0.0

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue Feb 01 2022 Mohamed El Morabity <melmorabity@fedoraproject.org> - 0.2.9-1
- Update to 0.2.9

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.8-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 29 2021 Mohamed El Morabity <melmorabity@fedoraproject.org> - 0.2.8-7
- Fix FTBFS (RHBZ #1988041)

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.8-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.8-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Aug 05 2020 Mohamed El Morabity <melmorabity@fedoraproject.org> - 0.2.8-4
- Fix different output on different architectures

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.8-3
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 01 2020 Mohamed El Morabity <melmorabity@fedoraproject.org> - 0.2.8-1
- Update to 0.2.8

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Dec 14 2019 Jeff Law <law@redhat.com> - 0.2.7-2
- Fix missing #include for gcc-10

* Wed Dec 04 2019 Mohamed El Morabity <melmorabity@fedoraproject.org> - 0.2.7-1
- Update to 0.2.7

* Fri Aug 09 2019 Mohamed El Morabity <melmorabity@fedoraproject.org> - 0.2.5-1
- Update to 0.2.5

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue May 08 2018 Mohamed El Morabity <melmorabity@fedoraproject.org> - 0.2.3-1
- Update to 0.2.3

* Tue Mar 06 2018 Mohamed El Morabity <melmorabity@fedoraproject.org> - 0.2.2-2
- Fix License tag
- Fix documentation installation path

* Mon Mar 05 2018 Mohamed El Morabity <melmorabity@fedoraproject.org> - 0.2.2-1
- Initial RPM release
