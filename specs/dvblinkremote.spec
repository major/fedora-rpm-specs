%global prerelease beta

Name:           dvblinkremote
Version:        0.2.0
Release:        0.35.%{prerelease}%{?dist}
Summary:        Tool for interacting with a DVBLink Connect! Server

License:        MIT
URL:            https://github.com/marefr/dvblinkremote
Source0:        https://github.com/marefr/%{name}/archive/v%{version}-%{prerelease}/%{name}-%{version}-%{prerelease}.tar.gz
# Fix curl detection
Patch0:         %{name}-0.2.0-curl.patch
# Fix build with tinyxml2 >= 6.0.0
Patch1:         %{name}-0.2.0-tinyxml2.patch
# Fix compilation issues on Linux with recent gcc versions (see
# https://github.com/marefr/dvblinkremote/commit/b32af4a)
Patch2:         %{name}-0.2.0-build.patch
# Build a shared library instead of a static one
Patch3:         %{name}-0.2.0-shared_library.patch
# Fix installation
Patch4:         %{name}-0.2.0-install.patch
# Fix ordered pointer comparison against zero
Patch5:		%{name}-gcc11.patch

BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  libcurl-devel
BuildRequires:  tinyxml2-devel

%description
A command line tool for interacting with a DVBLink Connect! Server using the
DVBLink Remote API.


%package        libs
Summary:        Pure C++ DVBLink Remote API library
%description    libs
libdvblinkremote is a pure C++ DVBLink Remote API static library. It currently
supports DVBLink Remote API version 0.2.


%package        devel
Summary:        Development files for %{name}
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}
Requires:       libcurl-devel%{?_isa}
%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use libdvblinkremote.


%prep
%autosetup -n %{name}-%{version}-%{prerelease} -p1


%build
%cmake \
  -DDVBLINKREMOTE_BIN_DIR=%{_bindir} \
  -DDVBLINKREMOTE_INCLUDE_DIR=%{_includedir}/lib%{name} \
  -DDVBLINKREMOTE_LIB_DIR=%{_libdir}
%cmake_build


%install
%cmake_install


%files
%{_bindir}/%{name}


%files libs
%doc COPYING README.md
%{_libdir}/*.so.*


%files devel
%{_includedir}/lib%{name}/
%{_libdir}/*.so


%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-0.35.beta
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Nov 11 2024 Dominik Mierzejewski <dominik@greysector.net> - 0.2.0-0.34.beta
- rebuild for tinyxml2

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-0.33.beta
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-0.32.beta
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-0.31.beta
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-0.30.beta
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-0.29.beta
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sun Sep 25 2022 Rich Mattes <richmattes@gmail.com> - 0.2.0-0.28.beta
- Rebuild for tinyxml2-9.0.0

* Thu Aug 04 2022 Mohamed El Morabity <melmorabity@fedoraproject.org> - 0.2.0-0.27.beta
- Fix FTBFS on Fedora 37

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-0.26.beta
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-0.25.beta
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-0.24.beta
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-0.23.beta
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Aug 18 2020 Jeff Law <law@redhat.com> - 0.2.0-0.22.beta
- Fix ordered pointer comparison against zero

* Thu Aug 13 2020 Mohamed El Morabity <melmorabity@fedoraproject.org> - 0.2.0-0.21.beta
- Use new cmake macros
- Clean up patches

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-0.20.beta
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-0.19.beta
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-0.18.beta
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-0.17.beta
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-0.16.beta
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Nov 27 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.2.0-0.15.beta
- Rebuild for tinyxml2 7.x

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-0.14.beta
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-0.13.beta
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Jan 23 2018 Mohamed El Morabity <melmorabity@fedoraproject.org> - 0.2.0-0.12.beta
- Fix build with tinyxml2 >= 6.0.0

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-0.11.beta
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-0.10.beta
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-0.9.beta
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun May 22 2016 Rich Mattes <richmattes@gmail.com> - 0.2.0-0.8.beta
- Rebuild for tinyxml2-3.0.0

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-0.7.beta
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.0-0.6.beta
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 0.2.0-0.5.beta
- Rebuilt for GCC 5 C++11 ABI change

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.0-0.4.beta
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.0-0.3.beta
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat May 24 2014 Mohamed El Morabity <melmorabity@fedoraproject.org> - 0.2.0-0.2.beta
- Rebuild for new tinyxml2

* Tue Mar 25 2014 Mohamed El Morabity <melmorabity@fedoraproject.org> - 0.2.0-0.1.beta
- Initial RPM release
