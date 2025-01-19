%global commit df8547ff075d4352db2eb802775b7fa7a92756db
%global short_commit %(c=%{commit}; echo ${c:0:7})
%global commit_date 20240205
%global commit_release .%{commit_date}git%{short_commit}

# To make rpmdev-bumpspec and similar tools happy
%global baserelease 12

Name:           libvmi
Version:        0.14.0
Release:        11.20240205gitdf8547f%{?dist}
Summary:        A library for performing virtual-machine introspection

License:        LGPL-3.0-or-later
URL:            http://libvmi.com/
Source0:        https://github.com/%{name}/%{name}/archive/%{commit}.tar.gz#/%{name}-%{commit}.tar.gz

# disable '-Werror'
Patch0001:      libvmi-no_werror.patch

# Cannot presently build on other architectures.
ExclusiveArch:  x86_64

BuildRequires:  cmake
BuildRequires:  gcc bison flex xen-devel fuse-devel
BuildRequires:  pkgconfig(json-c)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(check)
BuildRequires:  pkgconfig(libvirt)

%description
LibVMI is a C library with Python bindings that makes it easy to monitor
the low-level details of a running virtual machine by viewing its memory,
trapping on hardware events, and accessing the vCPU registers.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package        utils
Summary:        Utilities which make use of %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    utils
The %{name}-utils package contains a number of programs which make
use of %{name}.

%prep
%autosetup -n libvmi-%{commit} -p1

%build
%cmake -DCMAKE_BUILD_TYPE="Release"
%cmake_build

%install
%cmake_install
find %{buildroot}%{_libdir} -name '*.la' -delete -print
find %{buildroot}%{_libdir} -name '*.a' -delete -print

%ldconfig_scriptlets

%files
%license COPYING.LESSER
%doc README
%{_libdir}/libvmi.so.*

%files devel
%doc examples/*.c
%{_includedir}/%{name}/
%{_libdir}/libvmi.so
%{_libdir}/pkgconfig/libvmi.pc

%files utils
%{_bindir}/*

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.14.0-11.20240205gitdf8547f
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.14.0-11.20240205gitdf8547f
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sun Jun 02 2024 W. Michael Petullo <mike@flyn.org> - 0.14.0-10.20240205gitdf8547f
- Update to Git master

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.14.0-9.20231220git8f37f07
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.14.0-8.20231220git8f37f07
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Dec 31 2023 W. Michael Petullo <mike@flyn.org> - 0.14.0-7.20231220git8f37f07
- Update to Git master

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.14.0-7.20230517git79ace5c
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu May 18 2023 W. Michael Petullo <mike@flyn.org> - 0.14.0-6.20230517git79ace5c
- Update to Git commit 79ace5c3844ec53c42e96995fd951683845e446c

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.14.0-5.20220512git932a87a
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.14.0-4.20220512git932a87a
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri May 13 2022 W. Michael Petullo <mike@flyn.org> - 0.14.0-3.20220512git932a87a
- Use %autochangelog

* Thu May 12 2022 W. Michael Petullo <mike@flyn.org> - 0.14.0-3.20220512git932a87a
- Update to Git master

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.14.0-2.20201230git1ae3950
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Dec 15 2021 Björn Esser <besser82@fedoraproject.org> - 0.14.0-1.20201230git1ae3950
- Update to 0.14.0

* Wed Dec 15 2021 Björn Esser <besser82@fedoraproject.org> - 0.13.0-8.20200730gitaeb8d1d
- Add patch to fix build with recent cmake
- Build with proper build type "Release"

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.13.0-7.20200730gitaeb8d1d
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Sat Jul 10 2021 Björn Esser <besser82@fedoraproject.org> - 0.13.0-6.20200730gitaeb8d1d
- Rebuild for versioned symbols in json-c

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.13.0-5.20200730gitaeb8d1d
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Aug 01 2020 W. Michael Petullo <mike@flyn.org> - 0.13.0-4.20200730gitaeb8d1d
- Update to Git master
- Use cmake macros to build

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.13.0-3.20200506git55248db
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.13.0-2.20200506git55248db
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri May 08 2020 W. Michael Petullo <mike@flyn.org> - 0.13.0-1.20200506git55248db8
- Update to Git master, now called 0.13.0

* Tue Apr 21 2020 Björn Esser <besser82@fedoraproject.org> - 0.11.0-18.20170706gite919365
- Rebuild (json-c)

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.0-17.20170706gite919365
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.0-16.20170706gite919365
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.0-15.20170706gite919365
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.0-14.20170706gite919365
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Mar 06 2018 Björn Esser <besser82@fedoraproject.org> - 0.11.0-13.20170706gite919365
- Rebuilt for libjson-c.so.4 (json-c v0.13.1)

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.0-12.20170706gite919365
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sun Dec 10 2017 Björn Esser <besser82@fedoraproject.org> - 0.11.0-11.20170706gite919365
- Rebuilt for libjson-c.so.3

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.0-10.20170706gite919365
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.0-9.20170706gite919365
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Jul 15 2017 W. Michael Petullo <mike@flyn.org> - 0.11.0-8.20170706gite919365
- Bump Release so NVR is bigger than the previous release

* Thu Jul 06 2017 W. Michael Petullo <mike@flyn.org> - 0.11.0-1.20170706gite919365
- Update to Git master

* Thu Mar 16 2017 W. Michael Petullo <mike@flyn.org> - 0.11.0-7.20170214git1a85386
- Update to Git master

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.0-6.20170208gitd7d5714
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 09 2017 W. Michael Petullo <mike@flyn.org> - 0.11.0-5.20170208gitd7d5714
- Update to Git master
- Add utils sub-package

* Tue Jan 24 2017 W. Michael Petullo <mike@flyn.org> - 0.11.0-4.20170124git42cd3b2
- Update to Git master

* Tue Jan 24 2017 W. Michael Petullo <mike@flyn.org> - 0.11.0-3.20161206gitb4bf45e
- Build with Rekall support

* Wed Dec 21 2016 Peter Robinson <pbrobinson@fedoraproject.org> 0.11.0-2.20161206gitb4bf45e
- Bump Release so NVR is bigger than the previous release

* Mon Dec 19 2016 W. Michael Petullo <mike@flyn.org> - 0.11.0-1.20161206gitb4bf45e
- Update to Git master

* Sun Dec 11 2016 W. Michael Petullo <mike@flyn.org> - 0.11.0-2.20161202gitb9b020c
- Rebuild for Xen 4.8

* Mon Dec 05 2016 W. Michael Petullo <mike@flyn.org> - 0.11.0-1.20161202gitb9b020c
- New upstream release
- Fix incorrect version in previous log entry
- Remove patch merged upstream
- Fix Source0

* Tue Jul 12 2016 W. Michael Petullo <mike@flyn.org> - 0.11.0-1.20161003git5ad492c
- Initial package
