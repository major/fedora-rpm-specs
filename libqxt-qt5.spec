%global commit  eaf6872f6ad490a4355c5c46279ddb81a9a15f92
%global shortcommit %(c=%{commit}; echo ${c:0:12})
%global commitdate 20130718

%global soname 0.7.0

Name:           libqxt-qt5
Version:        0.7.0
Release:        0.31.%{commitdate}git%{shortcommit}%{?dist}
Summary:        Extended version of the original Qt extension library
License:        BSD and (CPL or LGPLv2)
URL:            https://bitbucket.org/libqxt/libqxt/wiki/Home
Source0:        https://bitbucket.org/libqxt/libqxt/get/%{commit}.tar.gz#/%{name}-%{shortcommit}.tar.gz
# Fix DSO linking
Patch0:         libqxt-linking.patch
# Fix build with GCC 6
Patch1:         libqxt-gcc6.patch
Patch2:         libqxt-header-fix.patch
#Debian patches
Patch3:         libqxt-use-system-qdoc3.patch
Patch4:         libqxt-fix-compiler-flags.patch
Patch5:         libqxt-qt5-libname.patch
Patch6:         libqxt-qt5-moc-pre-processing-order.patch

BuildRequires:  pkgconfig(avahi-compat-libdns_sd)
BuildRequires:  pkgconfig(avahi-core)
BuildRequires:  pkgconfig(libssh2)
BuildRequires:  libdb-devel
BuildRequires:  pkgconfig(xrandr)
# match what openssl version qt5-qtbase uses
%if 0%{?fedora} == 26
BuildRequires:  compat-openssl10-devel
%else
BuildRequires:  openssl-devel
%endif
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5Designer)
BuildRequires:  pkgconfig(Qt5X11Extras)
BuildRequires:  qt5-qtbase-private-devel
BuildRequires: make

%description
LibQxt, an extension library for Qt5, provides a suite of cross-platform
utility classes to add functionality not readily available in the Qt toolkit.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name} = %{version}-%{release}
Requires:       pkgconfig(avahi-compat-libdns_sd)
Requires:       pkgconfig(avahi-core)
Requires:       libdb-devel

%description    devel
This package contains qt5 libraries and header files for developing applications
that use LibQxt.

%package        doc
Summary:        Documentation files for %{name}
BuildArch:      noarch

%description    doc
The %{name}-doc package contains html documentation
that use %{name}.

%prep
%setup -qc -n libqxt-libqxt-%{shortcommit}

mv libqxt-libqxt-%{shortcommit} qt5
pushd qt5
%patch0 -p1 -b .linking
%patch1 -p1 -b .gcc6
%patch2 -p1 -b .header-fix
%patch3 -p1 -b .use-system-qdoc3
%patch4 -p1 -b .fix-compiler-flags
%patch5 -p1 -b .libname
%patch6 -p1 -b .moc-pre-processing-order

# Remove bundled lib
rm -rf src/3rdparty/libssh2

# Fix wrong-file-end-of-line-encoding
sed -i 's/\r$//' examples/qxtsnapshot/{README,qxtsnapshotpreview.h,qxtsnapshot.h,qxtsnapshottooltip.h}

mkdir config.tests/qt5/
cp config.tests/qt4/qt4.pro config.tests/qt5/qt5.pro
cp config.tests/qt4/main.cpp config.tests/qt5/main.cpp
sed -i -e 's|configtest qt4 QT|configtest qt5 QT|' configure
sed -i -e 's|TARGET = qt4|TARGET = qt5|' config.tests/qt5/qt5.pro 
sed -i -e 's|qt4|qt5|' config.tests/qt5/main.cpp 
sed -i -e 's|qdoc3|qdoc|' doc/doc.pri
sed -i -e 's| -DQXT_DOXYGEN_RUN||' doc/doc.pri

# We don't want rpath
sed -i '/RPATH/d' src/qxtlibs.pri
popd

%build
############### QT5 ######################
pushd qt5
./configure -verbose                      \
 -I %{_includedir}/avahi-compat-libdns_sd \
 -qmake-bin %{_qt5_bindir}/qmake          \
 -prefix %{_prefix}                       \
 -libdir %{_libdir}                       \
 -headerdir %{_qt5_headerdir}             \
 -docdir %{_datadir}/doc/libqxt-qt5-doc/html \
 -debug
# manually running qmake here may end up being fragile, if so,
# introducing a qmake wrapper is the next best thing -- rex
%{qmake_qt5} -r %{_qt5_qmake_flags} \
 QMAKE_LFLAGS="${RPM_LD_FLAGS} -Wl,--as-needed"
%make_build
%make_build docs
popd

%install
############### QT5 ######################
pushd qt5

# We are installing these to the proper location
rm -fr %{buildroot}%{_prefix}/doc/

# Fix pkgconfig includedir qt5 path
sed -i -e 's|includedir=${prefix}/include/QxtNetwork|includedir=${prefix}/include/qt5/QxtNetwork|' lib/pkgconfig/QxtNetwork-qt5.pc
sed -i -e 's|includedir=${prefix}/include/QxtSql|includedir=${prefix}/include/qt5/QxtSql|' lib/pkgconfig/QxtSql-qt5.pc
sed -i -e 's|includedir=${prefix}/include/QxtWeb|includedir=${prefix}/include/qt5/QxtWeb|' lib/pkgconfig/QxtWeb-qt5.pc
sed -i -e 's|includedir=${prefix}/include/QxtCore|includedir=${prefix}/include/qt5/QxtCore|' lib/pkgconfig/QxtCore-qt5.pc
sed -i -e 's|includedir=${prefix}/include/QxtZeroconf|includedir=${prefix}/include/qt5/QxtZeroconf|' lib/pkgconfig/QxtZeroconf-qt5.pc
sed -i -e 's|includedir=${prefix}/include/QxtWidgets|includedir=${prefix}/include/qt5/QxtWidgets|' lib/pkgconfig/QxtWidgets-qt5.pc

# Fix pkgconfig files install dependencies
sed -i -e 's|Requires: QtCore|Requires: Qt5Core|' lib/pkgconfig/QxtCore-qt5.pc
sed -i -e 's|Requires: QxtCore QtNetwork|Requires: QxtCore-qt5 Qt5Network|' lib/pkgconfig/QxtNetwork-qt5.pc
sed -i -e 's|Requires: QxtCore QtSql|Requires: QxtCore-qt5 Qt5Sql|' lib/pkgconfig/QxtSql-qt5.pc
sed -i -e 's|Requires: QxtCore QxtNetwork|Requires: QxtCore-qt5 QxtNetwork-qt5|' lib/pkgconfig/QxtWeb-qt5.pc
sed -i -e 's|Requires: QtCore QxtCore QtGui|Requires: Qt5Core QxtCore-qt5 Qt5Gui|' lib/pkgconfig/QxtWidgets-qt5.pc
sed -i -e 's|Requires: QxtCore QxtNetwork|Requires: QxtCore-qt5 QxtNetwork-qt5|' lib/pkgconfig/QxtZeroconf-qt5.pc

make install --ignore-errors INSTALL_ROOT=%{buildroot}

%ldconfig_scriptlets

%files
%doc qt5/AUTHORS qt5/CHANGES qt5/README
%license qt5/COPYING qt5/*.txt
%{_bindir}/qxtjsonrpc
%{_qt5_libdir}/*.so.*

%files devel
%{_qt5_headerdir}/QxtCore/
%{_qt5_headerdir}/QxtNetwork/
%{_qt5_headerdir}/QxtSql/
%{_qt5_headerdir}/QxtWeb/
%{_qt5_headerdir}/QxtWidgets/
%{_qt5_headerdir}/QxtZeroconf/
%{_qt5_libdir}/*.so
%{_qt5_plugindir}/designer/*.so
%{_qt5_libdir}/libQxt*.prl
%{_qt5_libdir}/pkgconfig/*.pc
%{_qt5_libdir}/qt5/mkspecs/features/qxt*.prf
%dir %{_qt5_libdir}/qt5/plugins/designer/pkgconfig
%{_qt5_libdir}/qt5/plugins/designer/pkgconfig/QxtDesignerPlugins-qt5.pc

%files doc
%doc qt5/examples/ qt5/doc/html/
%{_datadir}/doc/libqxt-qt5-doc/html/

%changelog
* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-0.31.20130718giteaf6872f6ad4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-0.30.20130718giteaf6872f6ad4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jul 14 2022 Jan Grulich <jgrulich@redhat.com> - 0.7.0-0.29.20130718giteaf6872f6ad4
- Rebuild (qt5)

* Tue May 17 2022 Jan Grulich <jgrulich@redhat.com> - 0.7.0-0.28.20130718giteaf6872f6ad4
- Rebuild (qt5)

* Tue Mar 08 2022 Jan Grulich <jgrulich@redhat.com> - 0.7.0-0.27.20130718giteaf6872f6ad4
- Rebuild (qt5)

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-0.26.20130718giteaf6872f6ad4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-0.25.20130718giteaf6872f6ad4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-0.24.20130718giteaf6872f6ad4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-0.23.20130718giteaf6872f6ad4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu May 14 2020 Martin Gansser <martinkg@fedoraproject.org> - 0.7.0-0.22.20130718giteaf6872f6ad4
- Use RR libdb-devel in subpackage devel

* Mon Apr 06 2020 Rex Dieter <rdieter@fedoraproject.org> - 0.7.0-0.21.20130718giteaf6872f6ad4
- cleanup qt5 deps (drop qt5-devel, versioned runtime dep)

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-0.20.20130718giteaf6872f6ad4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Oct 01 2019 Martin Gansser <martinkg@fedoraproject.org> - 0.7.0-0.19.20130718giteaf6872f6ad4
- Use BR libdb-devel due EPEL8 dependencies

* Thu Sep 26 2019 Martin Gansser <martinkg@fedoraproject.org> - 0.7.0-0.18.20130718giteaf6872f6ad4
- Create EPEL8 package (RHBZ#1755961)

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-0.17.20130718giteaf6872f6ad4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Apr 28 2019 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 0.7.0-0.16.20130718giteaf6872f6ad4
- Rebuild for libQt5.12

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-0.15.20130718giteaf6872f6ad4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sun Oct 21 2018 Robert-André Mauchin <zebob.m@gmail.com> - 0.7.0-0.14.20130718giteaf6872f6ad4
- Fix pkgconfig files install dependencies, avoid pulling Qt4 libraries

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-0.13.20130718giteaf6872f6ad4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-0.12.20130718giteaf6872f6ad4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Dec 01 2017 Martin Gansser <martinkg@fedoraproject.org> - 0.7.0-0.11.20130718giteaf6872f6ad4
- Rebuilt

* Thu Nov 30 2017 Martin Gansser <martinkg@fedoraproject.org> - 0.7.0-0.10.20130718giteaf6872f6ad4
- Add libqxt-qt5-moc-pre-processing-order.patch
- Add -lQt5X11Extras flag to libqxt-linking.patch

* Mon Nov 27 2017 Leigh Scott <leigh123linux@googlemail.com> - 0.7.0-0.9.20130718giteaf6872f6ad4
- Remove bundled libssh2

* Sun Nov 26 2017 Rex Dieter <rdieter@fedoraproject.org> - 0.7.0-0.8.giteaf6872f6ad4
- use compat-openssl10-devel only on f26 (to match qt5-qtbase usage)

* Wed Nov 22 2017 Martin Gansser <martinkg@fedoraproject.org> - 0.7.0-0.7.20130718giteaf6872f6ad4
- Fix pkgconfig files install dependencies

* Wed Nov 22 2017 Martin Gansser <martinkg@fedoraproject.org> - 0.7.0-0.6.20130718giteaf6872f6ad4
- Fix pkgconfig includedir qt5 path

* Tue Nov 21 2017 Martin Gansser <martinkg@fedoraproject.org> - 0.7.0-0.5.20130718giteaf6872f6ad4
- Add libqxt-qt5-libname.patch

* Sat Nov 18 2017 Martin Gansser <martinkg@fedoraproject.org> - 0.7.0-0.4.20130718giteaf6872f6ad4
- Fix Package must own all directories that it creates

* Sat Nov 18 2017 Martin Gansser <martinkg@fedoraproject.org> - 0.7.0-0.3.20130718giteaf6872f6ad4
- Add QMAKE_LFLAGS to fix unused-direct-shlib-dependency warnings
- Add doc subpkg
- Add cpl1.0.txt and lgpl-2.1.txt into %%license section
- Add BSD to license tag

* Fri Nov 17 2017 Martin Gansser <martinkg@fedoraproject.org> - 0.7.0-0.2.20130718giteaf6872f6ad4
- Correct url address

* Tue Nov 14 2017 Martin Gansser <martinkg@fedoraproject.org> - 0.7.0-1
- Build QT5 library
