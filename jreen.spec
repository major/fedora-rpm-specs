
Name:    jreen
Summary: Qt4 XMPP Library
Version: 1.2.1
Release: 25%{?dist}
 
License: GPLv2+
#URL:     http://qutim.org/jreen
URL:     https://github.com/euroelessar/jreen
%if 0%{?snap}
# git clone git://github.com/euroelessar/jreen.git ; cd jreen
# git archive --prefix=jreen-1.0.1/ v1.0.1 | xz > ../jreen-1.0.1.tar.xz
#Source0: jreen-%{version}.tar.xz
%else
#Source0: http://qutim.org/dwnl/44/libjreen-%{version}.tar.bz2
Source0: https://github.com/euroelessar/jreen/archive/v%{version}.tar.gz
%endif

Patch2: 0002-Added-ability-to-listen-to-ChatStates-in-MUC.patch
Patch3: 0003-Use-QSsl-SecureProtocols-instead-of-QSsl-TlsV1.patch
Patch4: 0004-Added-JREEN_EXPORT-to-entitytime.h.patch
Patch5: 0005-Fixed-invites-in-MUC.patch
Patch6: 0006-Changed-query-to-x.patch
Patch7: 0007-Fixed-parsing-of-time-with-milliseconds-in-UTC-forma.patch

## upstreamable patches
Patch100: jreen-1.2.1-no_undefined.patch
Patch101: jreen-1.2.1-qt56.patch

BuildRequires: cmake
BuildRequires: libidn-devel
BuildRequires: pkgconfig(libgsasl)
BuildRequires: pkgconfig(qjdns)
BuildRequires: pkgconfig(QtNetwork) 
BuildRequires: pkgconfig(Qt5Network)
BuildRequires: pkgconfig(speex)
BuildRequires: zlib-devel
BuildRequires: make

# apparently dlopens libidn
Requires: libidn%{?_isa}

%description
%{summary}.
 
%package devel
Summary:  Development files for %{name} 
Requires: %{name}%{?_isa} = %{version}-%{release}
%description devel
%{summary}.

%package qt5
Summary: Qt5 XMPP Library
Requires: %{name}%{?_isa} = %{version}-%{release}
%description qt5
%{summary}.

%package qt5-devel
Summary:  Development files for %{name}-qt5
Requires: %{name}-qt5%{?_isa} = %{version}-%{release}
%description qt5-devel
%{summary}.
 
 
%prep
%autosetup -n jreen-%{version} -p1

# nuke bundled libs out of paranoia -- rex
rm -rfv 3rdparty/{jdns,simplesasl}


%build
%global _vpath_builddir %{_target_platform}
%cmake .. \
  -DCMAKE_BUILD_TYPE:STRING="Release" \
  -DJREEN_FORCE_QT4:BOOL=ON \
  -DJREEN_USE_SYSTEM_JDNS:BOOL=ON

%cmake_build

%global _vpath_builddir %{_target_platform}-qt5
%{cmake} .. \
  -DCMAKE_BUILD_TYPE:STRING="Release" \
  -DJREEN_FORCE_QT4:BOOL=OFF \
  -DJREEN_USE_SYSTEM_JDNS:BOOL=ON

%cmake_build


%install
make install/fast DESTDIR=%{buildroot} -C %{_target_platform}
make install/fast DESTDIR=%{buildroot} -C %{_target_platform}-qt5


%check
export PKG_CONFIG_PATH=%{buildroot}%{_datadir}/pkgconfig:%{buildroot}%{_libdir}/pkgconfig
test "$(pkg-config --modversion libjreen)" = "%{version}"
test "$(pkg-config --modversion libjreen-qt5)" = "%{version}"

 
%ldconfig_scriptlets
 
%files 
%doc AUTHORS ChangeLog README.md
%license COPYING
%{_libdir}/libjreen.so.1*

%files devel
%{_includedir}/jreen-qt4/
%{_libdir}/libjreen.so
%{_libdir}/pkgconfig/libjreen.pc

%ldconfig_scriptlets qt5

%files qt5
%doc AUTHORS ChangeLog README.md
%license COPYING
%{_libdir}/libjreen-qt5.so.1*

%files qt5-devel
%{_includedir}/jreen-qt5/
%{_libdir}/libjreen-qt5.so
%{_libdir}/pkgconfig/libjreen-qt5.pc

 
%changelog
* Sat Jan 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Sep 07 2020 Than Ngo <than@redhat.com> - 1.2.1-18
- Fixed FTBFS

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-17
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jun 28 2018 Rex Dieter <rdieter@fedoraproject.org> - 1.2.1-11
- use %%make_build %%ldconfig_scriptlets

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 19 2016 Rex Dieter <rdieter@fedoraproject.org> 1.2.1-6
- fix build against qt-5.6 (#1307664)

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sun Nov 15 2015 Rex Dieter <rdieter@fedoraproject.org> 
- 1.2.1-4
- drop JREEN_USE_IRISICE=ON, needs work (missing headers/symbols) (#1282176)
- pull in upstream fixes

* Mon Nov 02 2015 Rex Dieter <rdieter@fedoraproject.org> 1.2.1-3
- rebuild (qjdns)

* Mon Jun 22 2015 Rex Dieter <rdieter@fedoraproject.org> 1.2.1-2
- s/BOON/BOOL/ typos

* Mon Jun 22 2015 Rex Dieter <rdieter@fedoraproject.org> 1.2.1-1
- 1.2.1, %%build: -DCMAKE_BUILD_TYPE=Release, use %%license

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 1.2.0-5
- Rebuilt for GCC 5 C++11 ABI change

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue May 13 2014 Rex Dieter <rdieter@fedoraproject.org> 1.2.0-2
- add Qt5 support, qt5/qt5-devel subpkgs

* Tue May 13 2014 Rex Dieter <rdieter@fedoraproject.org> 1.2.0-1
- jreen-1.2.0 (#1097347)

* Fri Apr 25 2014 Rex Dieter <rdieter@fedoraproject.org> 1.1.1-5
- fix build with recent cmake/moc handling

* Fri Apr 25 2014 Rex Dieter <rdieter@fedoraproject.org> 1.1.1-4
- rebuild (qjdns)

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Tue Jan 08 2013 Rex Dieter <rdieter@fedoraproject.org> 1.1.1-1
- jreen-1.1.1

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Apr 23 2012 Rex Dieter <rdieter@fedoraproject.org> 1.1.0-1
- jreen-1.1.0

* Sun Apr 01 2012 Rex Dieter <rdieter@fedoraproject.org> 1.0.5-1
- jreen-1.0.5 (#807634)

* Wed Mar 28 2012 Rex Dieter <rdieter@fedoraproject.org> 1.0.4-1
- jreen-1.0.4 (#807634)

* Sat Jan 07 2012 Rex Dieter <rdieter@fedoraproject.org> 1.0.1-4
- upstream gcc47 patch

* Sat Jan 07 2012 Rex Dieter <rdieter@fedoraproject.org> 1.0.1-3
- update URL, Source0

* Fri Jan 06 2012 Rex Dieter <rdieter@fedoraproject.org> 1.0.1-2
- fix URL
- Requires: qca-ossl
- delete bundled libs

* Fri Jan 06 2012 Rex Dieter <rdieter@fedoraproject.org> 1.0.1-1
- 1.0.1
- -DJREEN_USE_SYSTEM_JDNS:BOOL=ON

* Mon Nov 14 2011 Rex Dieter <rdieter@fedoraproject.org> 0.1.0-0.4.20110901
- pkgconfig-style deps

* Thu Sep 01 2011 Rex Dieter <rdieter@fedoraproject.org> 0.1.0-0.3.20110901
- 20110901 snapshot

* Tue Aug 16 2011 Rex Dieter <rdieter@fedoraproject.org> 0.1.0-0.2.20110816
- 20110816 snapshot

* Thu Jun 02 2011 Rex Dieter <rdieter@fedoraproject.org> 0.1.0-0.1.20010602
- first try, 0.1.0 20010602 git snapshot

