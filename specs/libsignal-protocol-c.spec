Name:       libsignal-protocol-c
Version:    2.3.3
Release:    15%{?dist}

# Automatically converted from old format: GPLv3 - review is highly recommended.
License:    GPL-3.0-only
Summary:    Signal Protocol C library
URL:        https://github.com/signalapp/libsignal-protocol-c
Source0:    %{url}/archive/v%{version}/%{name}-%{version}.tar.gz
# CVE-2022-48468: https://bugzilla.redhat.com/show_bug.cgi?id=2186673
# Upstream is gone, so sadly we must carry this patch downstream.
Patch0:     0001-CVE-2022-48468-unsigned-integer-overflow.patch

BuildRequires: cmake
BuildRequires: gcc
BuildRequires: gcc-c++
BuildRequires: openssl-devel

# https://github.com/signalapp/libsignal-protocol-c/issues/103
Provides: bundled(protobuf-c) = 1.1.1


%description
This is a ratcheting forward secrecy protocol that works in synchronous
and asynchronous messaging environments.


%package devel
Summary:    Development files for libsignal-protocol-c

Requires:   %{name}%{?_isa} = %{version}-%{release}


%description devel
Development files for libsignal-protocol-c.


%prep
%autosetup -p1 -n %{name}-%{version}


%build
%cmake -DCMAKE_BUILD_TYPE=Debug .
%cmake_build


%install
%cmake_install


%check
ctest -V %{?_smp_mflags}


%files
%license LICENSE
%doc README.md
%{_libdir}/libsignal-protocol-c.so.2*


%files devel
%{_includedir}/signal
%{_libdir}/libsignal-protocol-c.so
%{_libdir}/pkgconfig/libsignal-protocol-c.pc


%changelog
* Mon Jan 20 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.3-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Jul 29 2024 Miroslav Suchý <msuchy@redhat.com> - 2.3.3-14
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.3-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.3-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.3-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.3-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Apr 19 2023 Randy Barlow <bowlofeggs@fedoraproject.org> - 2.3.3-9
- Fix CVE-2022-48468: unsigned integer overflow (#2186673).

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.3-3
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sun Apr 26 2020 Randy Barlow <bowlofeggs@fedoraproject.org> - 2.3.3-1
- Update to 2.3.3 (#1818448).

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Jan 05 2019 Randy Barlow <bowlofeggs@fedoraproject.org> - 2.3.2-1
- Initial release.
