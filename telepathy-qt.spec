
%if 0%{?build_from_snapshot}
%global snap 20140403
%global git_commit 0191a6ddf0c094d9ae61b9ee48f1b282e13a9ef2
%global git_hash   0191a6dd
%endif

%global farstream 1

## unit tests
%global enable_tests 1

Name:    telepathy-qt
Version: 0.9.8
Release: 11%{?dist}
Summary: High-level bindings for Telepathy

License: LGPLv2+
URL:     http://telepathy.freedesktop.org/doc/telepathy-qt/
%if 0%{?snap:1}
# git clone http://anongit.freedesktop.org/git/telepathy/telepathy-qt.git; cd telepathy-qt
# git archive --prefix=telepathy-qt-0.9.3.1/ 0191a6ddf0c094d9ae61b9ee48f1b282e13a9ef2 | gzip -9 >
Source0: telepathy-qt-%{version}-%{git_hash}.tar.gz
%else
Source0: http://telepathy.freedesktop.org/releases/telepathy-qt/telepathy-qt-%{version}.tar.gz
%endif

## upstreamable patches

## upstream patches

BuildRequires: cmake
BuildRequires: python3-dbus, python3-devel
BuildRequires: doxygen
BuildRequires: dbus-daemon
%if 0%{?farstream}
BuildRequires: pkgconfig(gstreamer-1.0)
BuildRequires: pkgconfig(farstream-0.2)
BuildRequires: pkgconfig(telepathy-farstream) >= 0.6
BuildRequires: pkgconfig(telepathy-glib) >= 0.18
%endif

%if 0%{?enable_tests}
BuildRequires: pkgconfig(gio-2.0)
BuildRequires: pkgconfig(telepathy-glib) >= 0.18
%endif

Requires: telepathy-mission-control

%description
Telepathy-qt are high level bindings for Telepathy and provides both
the low level 1:1 auto generated API, and a high-level API build
on top of that, in the same library.

%package -n telepathy-qt5
Summary: High-level Qt5 bindings for Telepathy
BuildRequires: pkgconfig(Qt5DBus) pkgconfig(Qt5Network) pkgconfig(Qt5Xml)
Requires: telepathy-mission-control
%description -n telepathy-qt5
Telepathy-qt5 are high level bindings for Telepathy and provides both
the low level 1:1 auto generated API, and a high-level API build
on top of that, in the same library.

%package -n telepathy-qt5-devel
Summary: Development files for telepathy-qt5
Requires: telepathy-qt5%{?_isa} = %{version}-%{release}
Requires: telepathy-filesystem
%if 0%{?farstream}
Requires: telepathy-qt5-farstream%{?_isa} = %{version}-%{release}
%endif
%description -n telepathy-qt5-devel
%{summary}.

%if 0%{?farstream}
%package -n telepathy-qt5-farstream
Summary: Farstream telepathy-qt5 bindings
Requires: telepathy-qt5%{?_isa} = %{version}-%{release}
%description -n telepathy-qt5-farstream
%{summary}.
%endif


%prep
%autosetup -n telepathy-qt-%{version} -p1


%build
%cmake \
  -DCMAKE_BUILD_TYPE:STRING=release \
  -DDESIRED_QT_VERSION=5 \
  -DDISABLE_WERROR:BOOL=ON \
  -DENABLE_TESTS:BOOL=%{?enable_tests:ON}%{!?enable_tests:OFF} \
  %{?farstream:-DENABLE_FARSTREAM:BOOL=ON} \
  %{!?farstream:-DENABLE_FARSTREAM:BOOL=OFF}

%cmake_build


%install
%cmake_install


%check
%if 0%{?enable_tests}
export CTEST_OUTPUT_ON_FAILURE=1
%ctest ||:
%endif


%ldconfig_scriptlets -n telepathy-qt5

%files -n telepathy-qt5
%doc AUTHORS NEWS README ChangeLog
%license COPYING
%{_libdir}/libtelepathy-qt5.so.0
%{_libdir}/libtelepathy-qt5.so.0.%{version}
%{_libdir}/libtelepathy-qt5-service.so.1
%{_libdir}/libtelepathy-qt5-service.so.0.%{version}

%if 0%{?farstream}
%ldconfig_scriptlets -n telepathy-qt5-farstream

%files -n telepathy-qt5-farstream
%{_libdir}/libtelepathy-qt5-farstream.so.0
%{_libdir}/libtelepathy-qt5-farstream.so.0.%{version}
%endif

%files -n telepathy-qt5-devel
%doc HACKING
%dir %{_includedir}/telepathy-qt5/
%{_includedir}/telepathy-qt5/TelepathyQt/
%{_libdir}/libtelepathy-qt5.so
%{_libdir}/pkgconfig/TelepathyQt5.pc
%{_libdir}/pkgconfig/TelepathyQt5Service.pc
%dir %{_libdir}/cmake
%{_libdir}/cmake/TelepathyQt5/
%{_libdir}/cmake/TelepathyQt5Service/
%{_libdir}/libtelepathy-qt5-service.so
%if 0%{?farstream}
%{_libdir}/libtelepathy-qt5-farstream.so
%{_libdir}/pkgconfig/TelepathyQt5Farstream.pc
%{_libdir}/cmake/TelepathyQt5Farstream/
%endif


%changelog
* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.8-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.8-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.8-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.8-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Sep 07 2020 Than Ngo <than@redhat.com> - 0.9.8-7
- Fix FTBFS

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.8-6
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.8-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jun 25 2020 Rex Dieter <rdieter@fedoraproject.org> - 0.9.8-4
- 0.9.8+ builds are now qt5 only (#1850943)

* Mon May 11 2020 Rex Dieter <rdieter@fedoraproject.org> - 0.9.8-3
- track sonames closer

* Mon May 11 2020 Rex Dieter <rdieter@fedoraproject.org> - 0.9.8-2
- drop qt4 support on f33+ only
- use %%make_build

* Tue Feb 18 2020 Than Ngo <than@redhat.com> - 0.9.8-1
- support python3

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.7-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.7-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.7-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.7-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sun Mar 18 2018 Iryna Shcherbina <ishcherb@redhat.com> - 0.9.7-6
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.7-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Thu Feb 09 2017 Rex Dieter <rdieter@fedoraproject.org> - 0.9.7-2
- one more upstream fix

* Mon Aug 29 2016 Rex Dieter <rdieter@fedoraproject.org> - 0.9.7-1
- 0.9.7
- (re)enable tests (qt5 only)
- Obsoletes: telepathy-qt4-farstream

* Tue Feb 16 2016 Rex Dieter <rdieter@fedoraproject.org> 0.9.6.1-4
- pull in upstream cmake fix, disable tests

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.6.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Oct 06 2015 Rex Dieter <rdieter@fedoraproject.org> 0.9.6.1-2
- some upstream fixes (gst1.5 in particular)

* Sat Jun 20 2015 Rex Dieter <rdieter@fedoraproject.org> 0.9.6.1-1
- 0.9.6.1
- workaround FTBFS against gstreamer-1.5 (#1234051)

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 0.9.5-4
- Rebuilt for GCC 5 C++11 ABI change

* Mon Feb 23 2015 Rex Dieter <rdieter@fedoraproject.org> - 0.9.5-3
- build static libtelepathy-qt?-service.a with -fPIC
- pull in a couple minor upstream fixes

* Fri Oct 03 2014 Rex Dieter <rdieter@fedoraproject.org> 0.9.5-2
- bump deps for newer farstream/gst1
- Qt5 support
- rename base pkg to telepathy-qt (to match upstream), but...
- keep subpkg names the same (telepathy-qt4), for simple/obvious upgrade path

* Wed Sep 17 2014 Jan Grulich <jgrulich@redhat.com> - 0.9.5.0-1
- Update to 0.9.5.0

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.3.1-0.4.20140403git0191a6dd
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Wed Jul 23 2014 Kevin Kofler <Kevin@tigcc.ticalc.org> 0.9.3.1-0.3.20140403git0191a6dd
- build against farstream 0.2 and GStreamer 1 on F21+ (#1092654)

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.3.1-0.2.20140403git0191a6dd
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Apr 29 2014 Rex Dieter <rdieter@fedoraproject.org> 0.9.3.1-0.1.20140403git0191a6dd
- 0.9.3.1 snapshot, fixes FTBFS

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Mon Jan 07 2013 Rex Dieter <rdieter@fedoraproject.org> 0.9.3-6
- respin farstream_compat patch

* Wed Oct 31 2012 Rex Dieter <rdieter@fedoraproject.org> 0.9.3-5
- fix build for newer compat-telepathy-farstream

* Wed Oct 31 2012 Rex Dieter <rdieter@fedoraproject.org> 0.9.3-4
- rework spec/macro conditionals a bit

* Tue Oct 09 2012 Rex Dieter <rdieter@fedoraproject.org> 0.9.3-3
- (Build)Requires: compat-telepathy-farstream-devel (f18+)

* Fri Oct 05 2012 Rex Dieter <rdieter@fedoraproject.org> 0.9.3-2
- rebuild (farstream)

* Fri Aug 03 2012 Rex Dieter <rdieter@fedoraproject.org> 0.9.3-1.1
- move Obsoletes: -farsight to main pkg

* Mon Jul 16 2012 Rex Dieter <rdieter@fedoraproject.org> 0.9.3-1
- telepathy-qt-0.9.3

* Wed Jul 11 2012 Rex Dieter <rdieter@fedoraproject.org> 0.9.2-1
- 0.9.2

* Tue May 22 2012 Radek Novacek <rnovacek@redhat.com> 0.9.1-4
- add rhel condition

* Thu Apr 05 2012 Rex Dieter <rdieter@fedoraproject.org> 0.9.1-3
- -farsight subpkg (f16)

* Mon Apr 02 2012 Rex Dieter <rdieter@fedoraproject.org> 0.9.1-2
- drop -farstream-devel subpkg

* Sat Mar 24 2012 Rex Dieter <rdieter@fedoraproject.org> 0.9.1-1
- 0.9.1
- -farstream(-devel) subpkgs

* Tue Mar 06 2012 Rex Dieter <rdieter@fedoraproject.org> 0.9.0-3
- drop telepathy-farsight support (awaiting upstream -farstream love)

* Fri Feb 17 2012 Rex Dieter <rdieter@fedoraproject.org> 0.9.0-2
- Requires: telepathy-mission-control

* Wed Jan 25 2012 Rex Dieter <rdieter@fedoraproject.org> 0.9.0-1
- telepathy-qt-0.9.0

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Fri Nov 25 2011 Rex Dieter <rdieter@fedoraproject.org> 0.8.0-2
- drop Requires: gnome-keyring

* Sat Nov 19 2011 Rex Dieter <rdieter@fedoraproject.org> 0.8.0-1
- 0.8.0

* Mon Nov 07 2011 Rex Dieter <rdieter@fedoraproject.org> 0.7.3-1
- 0.7.3
- pkgconfig-style deps

* Wed Aug 10 2011 Rex Dieter <rdieter@fedoraproject.org> 0.7.2-1
- 0.7.2
- Requires: gnome-keyring

* Fri Jul 15 2011 Jaroslav Reznik <jreznik@redhat.com> - 0.7.1-1
- initial package
