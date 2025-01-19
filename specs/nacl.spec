Name:           nacl
# http://nacl.cr.yp.to/
URL:            http://nacl.cace-project.eu/
Version:        20110221
Release:        36%{?dist}
License:        LicenseRef-Fedora-Public-Domain
Summary:        Networking and Cryptography library

Source0:        http://hyperelliptic.org/nacl/nacl-%{version}.tar.bz2
Source1:        curvecpclient.1
Source2:        curvecpserver.1
Source3:        curvecpmakekey.1
Source4:        curvecpmessage.1
Source5:        curvecpprintkey.1
Source6:        nacl-sha256.1
Source7:        nacl-sha512.1
Patch0:         nacl-20110221-dist-flags.patch
Patch1:         nacl-20110221-build-dir.patch
Patch2:         nacl-20110221-noexec-stack.patch
# Fix for secondary arches
Patch3:         nacl-20110221-cpufreq-fallback.patch
Patch4:         nacl-20110221-abi-len-limit.patch

BuildRequires:  gcc
BuildRequires:  e2fsprogs

%description
NaCl (pronounced "salt") is a new easy-to-use high-speed software library for
network communication, encryption, decryption, signatures, etc. NaCl's goal
is to provide all of the core operations needed to build higher-level
cryptographic tools.

%package devel
Summary:        Development files
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
Include files and devel library.

%package static
Summary:        Static version of the NaCl library
Provides:       nacl-static%{?_isa} = %{version}-%{release}
Requires:       %{name}-devel%{?_isa} = %{version}-%{release}

%description static
Statically linkable version of the NaCl library.

%prep
%setup -q
%patch -P0 -p1 -b .dist-flags
%patch -P1 -p1 -b .build-dir
%patch -P2 -p1 -b .noexec-stack
%patch -P3 -p1 -b .cpufreq-fallback
%patch -P4 -p1 -b .abi-len-limit

# It's necessary to build in C89 mode because of implicit function
# declarations and implicit int.
%global build_type_safety_c 0
sed -i 's|\${CFLAGS}|%{optflags} -fPIC|g' okcompilers/c okcompilers/cpp

%build
./do
# shared library
gcc -shared -fPIC -Wl,-soname,libnacl.so.0 -o libnacl.so.0.0.0 \
  -Wl,-whole-archive build/fedora/lib/*/libnacl.a -Wl,-no-whole-archive \
  build/fedora/lib/*/cpucycles.o build/fedora/lib/*/randombytes.o

%install
mkdir -p %{buildroot}%{_includedir}/%{name}
install -m 0644 -t %{buildroot}%{_includedir}/%{name} build/fedora/include/*/*.h
mkdir -p %{buildroot}%{_libdir}/
install -m 0644 -t %{buildroot}%{_libdir} build/fedora/lib/*/*.a

# install cpucycles.o and randombytes.o
install -m 0644 -t %{buildroot}%{_libdir} build/fedora/lib/*/cpucycles.o build/fedora/lib/*/randombytes.o

# install shared library
install -m 0755 -t %{buildroot}%{_libdir} libnacl.so.*
pushd %{buildroot}%{_libdir}
ln -s libnacl.so.0.0.0 libnacl.so.0
ln -s libnacl.so.0 libnacl.so
popd

mkdir -p %{buildroot}%{_mandir}/man1
install -m 0644 -t %{buildroot}%{_mandir}/man1 %{SOURCE1} %{SOURCE2} %{SOURCE3} %{SOURCE4} %{SOURCE5} %{SOURCE6} %{SOURCE7}
mkdir -p %{buildroot}%{_bindir}
rm -f build/fedora/bin/ok*
install -m 0755 -t %{buildroot}%{_bindir} build/fedora/bin/*

%files
%{_libdir}/libnacl.so.*
%{_bindir}/*
%{_mandir}/man1/*

%files static
%{_libdir}/libnacl.a
%{_libdir}/cpucycles.o
%{_libdir}/randombytes.o

%files devel
%{_libdir}/libnacl.so
%{_includedir}/nacl

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 20110221-36
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 20110221-35
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 20110221-34
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 20110221-33
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Aug 16 2023 Florian Weimer <fweimer@redhat.com> - 20110221-32
- Set build_type_safety_c to 0 (#2144813)

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 20110221-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 20110221-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Tue Nov 22 2022 Florian Weimer <fweimer@redhat.com> - 20110221-29
- Build in C89 mode (#2144813)

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 20110221-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 20110221-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 20110221-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 20110221-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 20110221-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 20110221-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 20110221-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 20110221-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 20110221-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 20110221-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 20110221-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 20110221-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 20110221-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 20110221-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Nov  3 2015 Jaroslav Škarvada <jskarvad@redhat.com> - 20110221-14
- Fixed shared library to export symbols from all objects
- Explicitly set -fPIC and not relying on default CFLAGS
  Related: rhbz#1276066

* Thu Oct 29 2015 Jaroslav Škarvada <jskarvad@redhat.com> - 20110221-13
- Added shared library, moved static objects to 'static' subpackage
  Resolves: rhbz#1276066

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20110221-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon May 11 2015 Jaroslav Škarvada <jskarvad@redhat.com> - 20110221-11
- Fixed sed optflags patching to work with new distro CFLAGS
- Rebuilt with new distro CFLAGS (PIC)
- Fixed typo in dist-flags patch
- Limit length of ABI string (by abi-len-lmit patch)

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20110221-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20110221-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon Aug 19 2013 Jaroslav Škarvada <jskarvad@redhat.com> - 20110221-8
- The cpucycles.o and randombytes.o moved outside the archive

* Thu Aug  8 2013 Jaroslav Škarvada <jskarvad@redhat.com> - 20110221-7
- Added cpucycles.o and randombytes.o to libnacl.a archive
  Resolves: rhbz#994236

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20110221-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Feb 15 2013 Jaroslav Škarvada <jskarvad@redhat.com> - 20110221-5
- Fixed packaging of devel subpackage not to own debuginfo files
  Resolves: rhbz#911405

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20110221-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Sep  6 2012 Jaroslav Škarvada <jskarvad@redhat.com> - 20110221-3
- Fixed build on secondary arches (cpufreq-fallback patch)

* Tue Sep  4 2012 Jaroslav Škarvada <jskarvad@redhat.com> - 20110221-2
- Updated URL

* Mon Jul 02 2012 Jaroslav Škarvada <jskarvad@redhat.com> - 20110221-1
- Initial release
