Name:           srt
Version:        1.5.1
Release:        3%{?dist}
Summary:        Secure Reliable Transport protocol tools

License:        MPLv2.0
URL:            https://www.srtalliance.org
Source0:        https://github.com/Haivision/srt/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires: make
BuildRequires:  cmake gcc-c++
BuildRequires:  gnutls-devel
BuildRequires:  gmock-devel
BuildRequires:  gtest-devel

Requires: srt-libs%{?_isa} = %{version}-%{release}


%description
Secure Reliable Transport (SRT) is an open source transport technology that
optimizes streaming performance across unpredictable networks, such as 
the Internet.

%package libs
Summary: Secure Reliable Transport protocol libraries

%description libs
Secure Reliable Transport protocol libraries

%package devel
Summary: Secure Reliable Transport protocol development libraries and headers
Requires: srt-libs%{?_isa} = %{version}-%{release}

%description devel
Secure Reliable Transport protocol development libraries and header files


%prep
%autosetup -p1


%build
%cmake \
  -DENABLE_STATIC=OFF \
  -DENABLE_UNITTESTS=ON \
  -DENABLE_GETNAMEINFO=ON \
  -DENABLE_BONDING=ON \
  -DUSE_ENCLIB=gnutls

%cmake_build


%install
%cmake_install
# remove old upstream temporary compatibility pc
rm -f %{buildroot}/%{_libdir}/pkgconfig/haisrt.pc


%check
# - test are broken on s390x for some slowness/timing reason
# - tests can't be run in parallel because they reuse port numbers
# - TestIPv6 are known broken due to v4_v6 mapping differnces between platforms
#   https://github.com/Haivision/srt/issues/1972#
# - Skip one more test (TestSocketOptions.InvalidVals) for now
#   https://github.com/Haivision/srt/issues/2623
%ifnarch s390x
%define _smp_build_ncpus 1
%ctest -E 'TestIPv6|TestSocketOptions.InvalidVals'
%endif


%ldconfig_scriptlets libs


%files
%license LICENSE
%doc README.md docs
%{_bindir}/srt-ffplay
%{_bindir}/srt-file-transmit
%{_bindir}/srt-live-transmit
%{_bindir}/srt-tunnel

%files libs
%license LICENSE
%{_libdir}/libsrt.so.1.5*

%files devel
%doc examples
%{_includedir}/srt
%{_libdir}/libsrt.so
%{_libdir}/pkgconfig/srt.pc


%changelog
* Sat Jan 21 2023 Yanko Kaneti <yaneti@declera.com> - 1.5.1-3
- Additional test tweaks

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Mon Sep 26 2022 Yanko Kaneti <yaneti@declera.com> - 1.5.1-1
- Update to 1.5.1

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jun 15 2022 Yanko Kaneti <yaneti@declera.com> - 1.5.0-1
- Update to 1.5.0. Major API/ABI update

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Mon Oct  4 2021 Yanko Kaneti <yaneti@declera.com> - 1.4.4-1
- Update to 1.4.4
- Various tweaks around tests/checks
- Tighten soname wildcard

* Mon Sep  6 2021 Yanko Kaneti <yaneti@declera.com> - 1.4.3-3
- Bump rebuild for gtest soname change

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Sun May  9 2021 Yanko Kaneti <yaneti@declera.com> - 1.4.3-1
- Update to 1.4.3. New soname

* Tue Mar 30 2021 Jonathan Wakely <jwakely@redhat.com> - 1.4.2-4
- Rebuilt for removed libstdc++ symbol (#1937698)

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Nov 02 2020 Jeff Law <law@redhat.com> - 1.4.2-2
- Fix missing #includes for gcc-11

* Thu Oct 29 2020 Nicolas Chauvet <kwizart@gmail.com> - 1.4.2-1
- Update to 1.4.2

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jul 24 2020 Jeff Law <law@redhat.com> - 1.4.1-4
- Use __cmake_in_source_build 

* Mon Apr 06 2020 Nicolas Chauvet <kwizart@gmail.com> - 1.4.1-3
- Switch to gnutls instead of openssl
- Enable tests
- Enforce strict EVR from main to -libs

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Dec  9 2019 Yanko Kaneti <yaneti@declera.com> - 1.4.1-1
- Update to 1.4.1

* Mon Sep 16 2019 Yanko Kaneti <yaneti@declera.com> - 1.4.0-1
- Update to 1.4.0

* Wed Sep 11 2019 Yanko Kaneti <yaneti@declera.com> - 1.3.4-1
- Update to 1.3.4

* Thu Aug  1 2019 Yanko Kaneti <yaneti@declera.com> - 1.3.3-3
- First attempt
- Adjustments suggested by review
