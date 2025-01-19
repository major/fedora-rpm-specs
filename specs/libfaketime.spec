Summary: Manipulate system time per process for testing purposes
Name: libfaketime
Version: 0.9.10
Release: 11%{?dist}
# most of the code is GPL-2.0-or-later AND GPL-3.0-only
# part of src/libfaketime.c is GPLv3
License: GPL-2.0-or-later AND GPL-3.0-only
Url: https://github.com/wolfcw/libfaketime
Source: https://github.com/wolfcw/libfaketime/archive/v%{version}/%{name}-%{version}.tar.gz

Patch0: libfaketime-backports.patch
Patch1: libfaketime-symver.patch
Patch2: 0001-Disable-unused-result-warning-in-tests.patch

Provides: faketime = %{version}

BuildRequires:  gcc
BuildRequires:  perl-interpreter
BuildRequires:  perl-Time-HiRes
BuildRequires: make
%if 0%{?fedora} >= 36 || 0%{?rhel} >= 10
Excludearch: %{ix86} %{arm}
%endif

%description
libfaketime intercepts various system calls which programs use to
retrieve the current date and time. It can then report faked dates and
times (as specified by you, the user) to these programs. This means you
can modify the system time a program sees without having to change the
time system- wide.

%prep
%autosetup -p1

%build

cd src

# https://github.com/wolfcw/libfaketime/blob/master/README.packagers
# Upstream libfaketime requires a mess of different compile time flags for different glibc versions and architectures.
# https://github.com/wolfcw/libfaketime/pull/178
# Goal is to build time autodetect these with autotools in the next release ...

FAKETIME_COMPILE_CFLAGS="BOGUS"
%if 0%{?el7}
  %ifarch x86_64
    echo "force_monotonic https://github.com/wolfcw/libfaketime/issues/202"
    export FAKETIME_COMPILE_CFLAGS="-DFORCE_MONOTONIC_FIX"
  %endif
  %ifarch aarch64 ppc64le
    echo "force_monotonic and pthread_nonver https://github.com/wolfcw/libfaketime/issues/205"
    export FAKETIME_COMPILE_CFLAGS="-DFORCE_MONOTONIC_FIX -DFORCE_PTHREAD_NONVER"
  %endif
  %ifarch armv7hl
    unset FAKETIME_COMPILE_CFLAGS
  %endif
%endif
%if 0%{?fedora} == 30 || 0%{?el8}
  # only ppc64le needs a workaround
  %ifarch ppc64le
    echo "pthread_nonver https://github.com/wolfcw/libfaketime/issues/204"
    export FAKETIME_COMPILE_CFLAGS="-DFORCE_PTHREAD_NONVER"
  %else
    unset FAKETIME_COMPILE_CFLAGS
  %endif
%endif
%if 0%{?fedora} >= 31 || 0%{?rhel} >=9
  # for reasons we don't know the old glibc workaround is required here but not on archv7hl and aarch64 ...
  %ifarch i686 x86_64 s390x
    echo "force_monotonic"
    export FAKETIME_COMPILE_CFLAGS="-DFORCE_MONOTONIC_FIX"
  %endif
  %ifarch ppc64le riscv64
    echo "force_monotonic and pthread_nonver"
    export FAKETIME_COMPILE_CFLAGS="-DFORCE_MONOTONIC_FIX -DFORCE_PTHREAD_NONVER"
  %endif
  %ifarch armv7hl aarch64
    unset FAKETIME_COMPILE_CFLAGS
  %endif
%endif

if [ "$FAKETIME_COMPILE_CFLAGS" == "BOGUS" ]; then
  echo "SHOULD NEVER REACH HERE ... YOU HAVE AN UNTESTED VERSION+ARCH, see rpm spec for details ... ABORT"
  exit 1
fi

CFLAGS="%{optflags} -Wno-nonnull-compare -Wno-strict-aliasing" make %{?_smp_mflags} \
         PREFIX="%{_prefix}" LIBDIRNAME="/%{_lib}/faketime" all

%check
make %{?_smp_mflags} -C test

%install
make PREFIX="%{_prefix}" DESTDIR=%{buildroot} LIBDIRNAME="/%{_lib}/faketime" install
rm -r %{buildroot}/%{_docdir}/faketime
# needed for stripping/debug package
chmod a+rx %{buildroot}/%{_libdir}/faketime/*.so.*


%files
%{_bindir}/faketime
%dir %attr(0755, root, root) %{_libdir}/faketime/
%attr(0755, root, root) %{_libdir}/faketime/libfaketime*so.*
%license COPYING
%doc README NEWS README.developers
%{_mandir}/man1/*

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.10-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.10-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.10-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.10-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jan 10 2024 Paul Wouters <paul.wouters@aiven.io> - 0.9.10-7
- Fix for building for riscv64

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.10-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Feb 22 2023 Pablo Greco <pgreco@centosproject.org> - 0.9.10-5
- Fix tests in ELN builds (yselkowitz)

* Tue Feb 21 2023 Pablo Greco <pgreco@centosproject.org> - 0.9.10-4
- Also disable i686 in rhel>=10 (ELN failures)

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.10-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue May 10 2022 Pablo Greco <pgreco@centosproject.org> - 0.9.10-1
- Update to 0.9.10
- Disable i686 and armhfp in fedora >=36

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.8-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.8-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.8-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Sep 02 2020 Pablo Greco <pgreco@centosproject.org> - 0.9.8-10
- Conditionals to build 0.9.8-9 in f31 and epel7-8
- Use upstream's version of the gcc10 fix

* Wed Sep 02 2020 Jeff Law <law@redhat.com> - 0.9.8-9
- Use symver attribute instead of asms for symbol versioning
- Enable LTO

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.8-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jul 10 2020 Jeff Law <law@redhat.com> - 0.9.8-7
- Disable LTO

* Sat Feb 08 2020 Pablo Greco <pgreco@centosproject.org> - 0.9.8-6
- Fix build with gcc10

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.8-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Oct 29 2019 Paul Wouters <pwouters@redhat.com> - 0.9.8-5
- Resolves: rhbz#1766749 libfaketime rfe: please add Provides:faketime
- Use license tag, remove duplicate README entry, update make test target

* Tue Sep 03 2019 Warren Togami <warren@blockstream.com> - 0.9.8-4
- upstream says to use FORCE_PTHREAD_NONVER on any glibc+arch that gets stuck
  For Fedora 31+ "make test" gets stuck on i686 x86_64 ppc64le s390x

* Wed Aug 28 2019 Warren Togami <warren@blockstream.com> - 0.9.8-3
- 0.9.8
- x86_64  EL7: DFORCE_MONOTONIC_FIX
  aarch64 EL7: DFORCE_MONOTONIC_FIX and FORCE_PTHREAD_NONVER
  ppc64le EL7: DFORCE_MONOTONIC_FIX and FORCE_PTHREAD_NONVER
  ppc64le F30+ FORCE_PTHREAD_NONVER

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.6-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.6-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.6-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.6-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.6-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Oct 12 2016 Paul Wouters <pwouters@redhat.com> - 0.9.6-4
- Add support for CLOCK_BOOTTIME (patch by Mario Pareja <pareja.mario@gmail.com>)

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Oct 28 2014 Paul Wouters <pwouters@redhat.com> - 0.9.6-1
- Upgraded to 0.9.6 which adds option to disable monotonic time faking
- fix permissions for symbol stripping for debug package

* Tue Oct 15 2013 Paul Wouters <pwouters@redhat.com> - 0.9.5-4
- Infinite recursion patch is still needed, make test causes
  segfaults otherwise.

* Mon Oct 14 2013 Paul Wouters <pwouters@redhat.com> - 0.9.5-3
- Work around from upstream for autodetecting glibc version bug on i686

* Mon Oct 14 2013 Paul Wouters <pwouters@redhat.com> - 0.9.5-2
- Remove use of ifarch for _lib macro for multilib

* Sun Oct 13 2013 Paul Wouters <pwouters@redhat.com> - 0.9.5-1
- Initial package
