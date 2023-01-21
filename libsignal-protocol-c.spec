Name:       libsignal-protocol-c
Version:    2.3.3
Release:    8%{?dist}

License:    GPLv3
Summary:    Signal Protocol C library
URL:        https://github.com/signalapp/libsignal-protocol-c
Source0:    %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

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
%setup -q -n %{name}-%{version}


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
