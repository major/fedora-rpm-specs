# For EPEL7
%global _hardened_build 1

%global min_meson_ver 0.43.0
%global min_glib2_ver 2.46
%global min_jsonglib_ver 1.2
%global min_libsoup_ver 2.99.2
%global min_gtkdoc_ver 1.20
%global min_gi_ver 0.9.5
%global min_vala_ver 0.16

%global apiver 2

Name:		snapd-glib
Version:	1.66
Release:	2%{?dist}
Summary:	Library providing a GLib interface to snapd

License:	LGPL-2.0-only OR LGPL-3.0-only
URL:		https://github.com/snapcore/%{name}
Source0:	https://github.com/snapcore/%{name}/releases/download/%{version}/%{name}-%{version}.tar.xz

# Backports from upstream

BuildRequires:	gtk-doc >= %{min_gtkdoc_ver}
BuildRequires:  meson >= %{min_meson_ver}
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  gettext
BuildRequires:  gobject-introspection-devel >= %{min_gi_ver}
BuildRequires:  pkgconfig(gio-2.0) >= %{min_glib2_ver}
BuildRequires:  pkgconfig(gio-unix-2.0) >= %{min_glib2_ver}
BuildRequires:  pkgconfig(glib-2.0) >= %{min_glib2_ver}
BuildRequires:  pkgconfig(json-glib-1.0) >= %{min_jsonglib_ver}
BuildRequires:  pkgconfig(libsoup-3.0) >= %{min_libsoup_ver}
BuildRequires:  pkgconfig(Qt6Core)
BuildRequires:  pkgconfig(Qt6Network)
BuildRequires:  pkgconfig(Qt6Qml)
BuildRequires:  vala >= %{min_vala_ver}

# Ensure that weird Provides aren't generated
%global __provides_exclude_from ^%{_qt6_qmldir}/Snapd/.*\\.so$

%description
%{name} is a library that provides an interface to communicate
with snapd for GLib based applications.

%package devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
This package provides the files for developing applications
that use %{name} to communicate with snapd.

%package tests
Summary:        Installed tests for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description tests
This package provides the files for running the test programs
for %{name} to verify the functionality of %{name}.

%package -n snapd-qt
Summary:	Library providing a Qt6 interface to snapd
Requires:	%{name}%{?_isa} = %{version}-%{release}

%description -n snapd-qt
snapd-qt is a library that provides an interface to communicate
with snapd for Qt based applications.

%package -n snapd-qt-qml
Summary:	Library providing a Qt6 QML interface to snapd
Requires:	snapd-qt%{?_isa} = %{version}-%{release}

%description -n snapd-qt-qml
snapd-qt-qml is a library that provides an interface to communicate
with snapd for Qt QML based applications.


%package -n snapd-qt-devel
Summary:	Development files for snapd-qt
Requires:	snapd-qt%{?_isa} = %{version}-%{release}
Requires:	%{name}-devel%{?_isa} = %{version}-%{release}

%description -n snapd-qt-devel
This package provides the files for developing applications
that use snapd-qt to communicate with snapd.

%package -n snapd-qt-tests
Summary:        Installed tests for snapd-qt
Requires:       snapd-qt%{?_isa} = %{version}-%{release}
Requires:       %{name}-tests%{?_isa} = %{version}-%{release}

%description -n snapd-qt-tests
This package provides the files for running the test programs
for snapd-qt to verify the functionality of snapd-qt.


%prep
%autosetup -p1


%build
%meson
%meson_build


%install
%meson_install


%files
%license COPYING.LGPL2 COPYING.LGPL3
%doc NEWS
%{_libdir}/libsnapd-glib-%{apiver}.so.*
%{_libdir}/girepository-1.0/Snapd-%{apiver}.typelib

%files devel
%doc %{_datadir}/gtk-doc/html/snapd-glib
%{_includedir}/snapd-glib-%{apiver}/
%{_libdir}/libsnapd-glib-%{apiver}.so
%{_libdir}/pkgconfig/snapd-glib-%{apiver}.pc
%{_datadir}/vala/vapi/snapd-glib-%{apiver}.*
%{_datadir}/gir-1.0/Snapd-%{apiver}.gir

%files tests
%{_libexecdir}/installed-tests/snapd-glib-%{apiver}/*-glib
%{_datadir}/installed-tests/snapd-glib-%{apiver}/*-glib.test

%files -n snapd-qt
%{_libdir}/libsnapd-qt-%{apiver}.so.*

%files -n snapd-qt-qml
%{_qt6_qmldir}/Snapd%{apiver}/

%files -n snapd-qt-devel
%{_includedir}/snapd-qt-%{apiver}/
%{_libdir}/libsnapd-qt-%{apiver}.so
%{_libdir}/pkgconfig/snapd-qt-%{apiver}.pc
%{_libdir}/cmake/Snapd%{apiver}/

%files -n snapd-qt-tests
%{_libexecdir}/installed-tests/snapd-glib-%{apiver}/*-qt6
%{_datadir}/installed-tests/snapd-glib-%{apiver}/*-qt6.test


%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.66-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Sep 12 2024 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 1.66-1
- 1.66

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.64-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sun Feb 25 2024 Neal Gompa <ngompa@fedoraproject.org> - 1.64-1
- Rebase to 1.64
- Add patch to port snapd-qt to Qt 6

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.58-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.58-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.58-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.58-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.58-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.58-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.58-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Jan 08 2021 Neal Gompa <ngompa13@gmail.com> - 1.58-1
- Update to 1.58
- Fix GIR annotations on snapd_client_get_snap_conf
- Put more information into error messages for unknown errors

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.57-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon May 25 2020 Neal Gompa <ngompa13@gmail.com> - 1.57-1
- Update to 1.57
- Add snapd_interface_make_label
- Add support for new snap types: "core", "base" and "snapd"
- Change way GTK documentation is generated to avoid a Meson bug
- Fix leak in markdown parser
- Fix leak in logout code
- Make build reproducible by fixing comment in generated file

* Sat Feb 15 2020 Neal Gompa <ngompa13@gmail.com> - 1.55-1
- Update to 1.55
- Add new APIs for download and logout actions
- Add support for snap store logout
- Fix QSnapdAuthData () constructor not copying discharge strings correctly
- Remove obsolete screenshot parsing code
- Make all snapd 404 errors return SNAPD_ERROR_NOT_FOUND

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.54-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Nov 25 2019 Neal Gompa <ngompa13@gmail.com> - 1.54-1
- Update to 1.54
- Add API to get snap website
- Add purge option to remove
- Switch build system to Meson
- Fix Qt build with optimisation disabled
- Fix tests breaking on json-glib < 1.2.4
- Use C99 style variable definitions

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.49-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Jul 17 2019 Neal Gompa <ngompa13@gmail.com> - 1.49-1
- Update to 1.49
- New APIs for getting connections and deprecating older variants
- Fix memory leaks
- Use C99 variable style

* Thu Jul 11 2019 Neal Gompa <ngompa13@gmail.com> - 1.48-1
- Update to 1.48
- Many new APIs added
- Allow searching via common-id
- Add a description markdown parser
- Replace SnapdConnection with SnapdPlugRef and SnapdSlotRef
- Support updated connections API (/v2/connections)
- Support updated /v2/interfaces&select= API
- Support snap configuration API
- Add Qt interface attribute API
- Make snapd_client_set_socket_path revert to the default when NULL passed.
- Fix C99 mode not being enabled on older versions of GCC

* Sun Mar 24 2019 Neal Gompa <ngompa13@gmail.com> - 1.47-1
- Update to 1.47
- New API: snapd_channel_get_released_at
- New API: SNAPD_ERROR_DNS_FAILURE
- Fix tests breaking due to undefined order of results
- Remove generated MOC file from tarball

* Mon Feb 04 2019 Kalev Lember <klember@redhat.com> - 1.45-3
- Update BRs for vala packaging changes

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.45-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jan 25 2019 Richard Hughes <rhughes@redhat.com> - 1.45-1
- Update to 1.45
- Support base snap field
- Support filtering apps
- Support maintenance information returned from snapd

* Sun Nov 04 2018 Neal Gompa <ngompa13@gmail.com> - 1.44-1
- Update to 1.44
- Reconnect to snapd if disconnected while trying to send the request
- Handle short writes to snapd

* Sat Aug 25 2018 Neal Gompa <ngompa13@gmail.com> - 1.43-1
- Update to 1.43
- New APIs for getting snaps asynchronously
- New APIs for getting system info and publisher info
- Deprecated async client list APIs
- Fix small memory leak
- Fix compile warnings

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.41-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Jun 22 2018 Neal Gompa <ngompa13@gmail.com> - 1.41-1
- Update to 1.41
- New APIs for getting build and common IDs
- Fix buffer overflows reading HTTP chunked data

* Thu Apr 12 2018 Neal Gompa <ngompa13@gmail.com> - 1.39-1
- Update to 1.39
- Fix memory leak in QSnapdAssertion
- Remove cancelled requests from the request queue.
- Fix SnapdClient reference leak in each request

* Sun Mar 04 2018 Neal Gompa <ngompa13@gmail.com> - 1.38-1
- Update to 1.38
- Fix snapd_snap_match_channel not matching risks correctly
- Fix return value of SnapdSnap::matchChannel when fails to match
- Support new snapd errors SNAPD_ERROR_NOT_FOUND, SNAPD_ERROR_NOT_IN_STORE
- Fix progress callback scope annotations
- Fix reference leak
- Fix missing out annotation in find/find_section
- Remove deprecated snapd-login-service
- Deprecated APIs for snapd-login-service
- Fix small memory leaks
- Fix linking with --no-undefined
- Compile snapd-qt with -fPIC to avoid compile failure on Fedora

* Wed Feb 07 2018 Neal Gompa <ngompa13@gmail.com> - 1.32-1
- Update to 1.32
- Fix crash when calling snapd_login_async
- Support new bad-query, network-timeout errors from snapd
- Support QSnapdClient::find/Section method without flags set
- Assert name parameter set in snapd_snap_match_channel
- Add methods to extrack track/risk/branch from channel names
- Implement snapd_client_abort_change
- Handle incorrectly named tracks field

* Sun Nov 19 2017 Neal Gompa <ngompa13@gmail.com> - 1.29-1
- Update to 1.29
- Add several new APIs for managing snaps
- Fix crash accessing freed memory
- Fix small memory leaks
- Fix crash on 32-bit architectures

* Wed Nov 01 2017 Neal Gompa <ngompa13@gmail.com> - 1.24-1
- Update to 1.24
- Add several new APIs for getting details on snaps
- Fix issues with Qt bindings
- Add support for setting snapd socket
- Add support for snap channels
- Make clients using provided sockets non-blocking

* Sun Oct 08 2017 Neal Gompa <ngompa13@gmail.com> - 1.23-1
- Update to 1.23
- Fix snapd-login-service crash
- Improve failure handling when snapd socket read/writes fail
- Backport from upstream: Fix runtime assertion when snapd socket is NULL

* Tue Sep 12 2017 Neal Gompa <ngompa13@gmail.com> - 1.22-1
- Update to 1.22
- Make QML module depend on libsnapd-qt being compiled first to fix compile failures

* Mon Sep 11 2017 Neal Gompa <ngompa13@gmail.com> - 1.21-1
- Update to 1.21
- Fix MOC detection in Fedora
- Handle Qt configure failures

* Fri Sep 08 2017 Richard Hughes <rhughes@redhat.com> - 1.20-1
- Update to 1.20
- Stop distributing generated files, which allows the build to complete.

* Thu Sep 07 2017 Richard Hughes <rhughes@redhat.com> - 1.19-1
- Update to 1.19
- Add new API required by gnome-software
- Add mutex in request queue

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.16-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.16-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Jul 18 2017 Richard Hughes <rhughes@redhat.com> - 1.16-1
- Update to 1.16
- Bring introspection and vapigen m4 macros into the source
- Fix snapd-qt build failure due to conflict of 'signals' variable with GDBus
- Set a user agent when sending requests to snapd-glib

* Thu Jul 13 2017 Robert Ancell <robert.ancell@canonical.com> - 1.15-1
- Update to 1.15
- Add gcc-c++ build depends

* Wed Jun 28 2017 Neal Gompa <ngompa13@gmail.com> - 1.13-2
- Downgrade snapd to Recommends and remove ExclusiveArch

* Tue Jun 27 2017 Neal Gompa <ngompa13@gmail.com> - 1.13-1
- Update to 1.13
- Version the build dependencies

* Thu May 18 2017 Neal Gompa <ngompa13@gmail.com> - 1.12-1
- Update to 1.12

* Wed Apr 05 2017 Neal Gompa <ngompa13@gmail.com> - 1.10-1
- Update to 1.10

* Fri Mar 31 2017 Neal Gompa <ngompa13@gmail.com> - 1.9-2
- Add ExclusiveArch entry from snapd, since it requires snapd

* Fri Mar 31 2017 Neal Gompa <ngompa13@gmail.com> - 1.9-1
- Rebase to latest upstream release

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Nov 1 2016  Zygmunt Krynicki <me@zygoon.pl> - 1.2-1
- Update to latest upstream release

* Tue Sep 27 2016 Neal Gompa <ngompa13@gmail.com> - 0.14-1
- Flesh out spec and add subpackages for devel and login service

* Thu Sep 08 2016 Zygmunt Krynicki <me@zygoon.pl> - 0.14-0
- Update to 0.14

* Fri Aug 26 2016 Zygmunt Krynicki <me@zygoon.pl> - 0.8-1
- Initial version of the package
