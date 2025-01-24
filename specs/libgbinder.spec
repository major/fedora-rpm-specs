Name: libgbinder
Version: 1.1.42
Release: 1%{?dist}
Summary: Binder client library
License: BSD
URL: https://github.com/mer-hybris/libgbinder
Source0: %{url}/archive/refs/tags/%{version}.tar.gz

# Fix compatibility with C23 for gcc15
Patch0:  c23.patch

%global libglibutil_version 1.0.52

BuildRequires: pkgconfig(glib-2.0)
BuildRequires: pkgconfig(libglibutil) >= %{libglibutil_version}
BuildRequires: pkgconfig
BuildRequires: make
BuildRequires: gcc
BuildRequires: bison flex
Requires: libglibutil >= %{libglibutil_version}

%description
GLib-style interface to binder (Android IPC mechanism)

Key features:
1. Integration with GLib event loop
2. Detection of 32 vs 64 bit kernel at runtime
3. Asynchronous transactions that don't block the event thread
4. Stable service manager and low-level transaction APIs

Android keeps changing both low-level RPC and service manager
protocols from version to version. To counter that, libgbinder
implements configirable backends for different variants of those,
and yet keeping its own API unchanged.

%package devel
Summary: Development library for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}

%description devel
This package contains the development library for %{name}.

%prep
%autosetup -p1

%build
%{make_build} LIBDIR=%{_libdir} KEEP_SYMBOLS=1 release pkgconfig
%{make_build} -C test/binder-bridge KEEP_SYMBOLS=1 release
%{make_build} -C test/binder-list KEEP_SYMBOLS=1 release
%{make_build} -C test/binder-ping KEEP_SYMBOLS=1 release
%{make_build} -C test/binder-call KEEP_SYMBOLS=1 release

%install
%{make_build} LIBDIR=%{_libdir} DESTDIR=%{buildroot} install-dev
%{make_build} -C test/binder-bridge DESTDIR=%{buildroot} install
%{make_build} -C test/binder-list DESTDIR=%{buildroot} install
%{make_build} -C test/binder-ping DESTDIR=%{buildroot} install
%{make_build} -C test/binder-call DESTDIR=%{buildroot} install

%check
%{make_build} -C unit test

%files
%{_libdir}/%{name}.so.*
%license LICENSE

%files devel
%{_libdir}/pkgconfig/*.pc
%{_libdir}/%{name}.so
%{_includedir}/gbinder

# Tools
# Missing manpages: https://github.com/mer-hybris/libgbinder/issues/107
%package tools
Summary: Binder tools
Requires: %{name} >= %{version}

%description tools
Binder command line utilities

%files tools
%{_bindir}/binder-bridge
%{_bindir}/binder-list
%{_bindir}/binder-ping
%{_bindir}/binder-call

%changelog
* Wed Jan 22 2025 Alessandro Astone <ales.astone@gmail.com> - 1.1.42-1
- new version (rhbz#2324966)
- Add patch to fix FTBFS with gcc15 (rhbz#2340731)

* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.40-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 19 2024 Alessandro Astone <ales.astone@gmail.com> - 1.1.40-1
- new version

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.36-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Feb 14 2024 Alessandro Astone <ales.astone@gmail.com> - 1.1.36-1
- new version

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.34-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.34-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.34-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue May 23 2023 Alessandro Astone <ales.astone@gmail.com> - 1.1.34-1
- Update to 1.1.34

* Mon Feb 27 2023 Alessandro Astone <ales.astone@gmail.com> - 1.1.33-1
- Update to 1.1.33

* Mon Jan 23 2023 Alessandro Astone <ales.astone@gmail.com> - 1.1.32-1
- Update to 1.1.32

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.31-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jan 06 2023 Alessandro Astone <ales.astone@gmail.com> - 1.1.31-1
- Update to 1.1.31
- Re-enable s390x builds

* Mon Dec 05 2022 Alessandro Astone <ales.astone@gmail.com> - 1.1.30-1
- Update to 1.1.30

* Sat Nov 26 2022 Alessandro Astone <ales.astone@gmail.com> - 1.1.29-1
- Update to 1.1.29
- Build binder-call tool

* Sat Oct 29 2022 Alessandro Astone <ales.astone@gmail.com> - 1.1.26-1
- Update to 1.1.26

* Tue Jul 19 2022 Alessandro Astone <ales.astone@gmail.com> - 1.1.25-1
- Handle RPC protocol change at run time

* Wed Jul 06 2022 Alessandro Astone <ales.astone@gmail.com> - 1.1.23-1
- Support API 31

* Mon Jun 20 2022 Alessandro Astone <ales.astone@gmail.com> - 1.1.21-1
- Tests pass again!

* Sat Jun 11 2022 Alessandro Astone <ales.astone@gmail.com> - 1.1.20-1
- Make RPC protocol selectable at runtime

* Tue Feb 22 2022 Mo 森 <rmnscnce@ya.ru> - 1.1.19-1
- Added reader and writer for aidl parcelables

* Wed Jan 19 2022 Mo 森 <rmnscnce@ya.ru> - 1.1.18-1
- Make sure stale object pointers don't hang around
- Properly shut down remote object inside the proxy
- Read ref_count from GObject atomically
- Don't release remote proxy handle too early (sometimes never)
- Disassociate auto-created proxies to stop them from piling up

* Tue Dec 28 2021 Mo 森 <rmnscnce@ya.ru> - 1.1.15-1
- Added readers and writers for int8 and int16

* Sun Nov 28 2021 Mo 森 <rmnscnce@ya.ru> - 1.1.14-2
- Support for FMQ (Fast Message Queues)
- Support for Android 11 (API level 30)
- Made GBinderReader API slightly more NULL tolerant
- Added gbinder_client_rpc_header()
- Added gbinder_reader_get_data()
- Added gbinder_writer_get_data()
- Added gbinder_servicemanager_device()
- Added gbinder_local_reply_append_fd()
