Name:       qxmpp
Version:    0.9.3
Release:    16%{?dist}
License:    LGPLv2+

Source0:    https://github.com/qxmpp-project/qxmpp/archive/v%{version}.tar.gz
Obsoletes:  qxmpp-dev < %{version}
Provides:   qxmpp-dev = %{version}-%{release}

Summary:    Qt XMPP Library
URL:        http://code.google.com/p/qxmpp/

BuildRequires: make
BuildRequires:  doxygen
BuildRequires:  qt5-qtbase-devel
BuildRequires:  qt4-devel
BuildRequires:  speex-devel

Patch1: 001-generate-html-docs.patch

%description
QXmpp is a cross-platform C++ XMPP client library. It is based on Qt and C++.

QXmpp is pretty intuitive and easy to use. It uses Qt extensively. Qt is the only
third party library it is dependent on. Users need to a have working knowledge of
C++ and Qt basics (Signals and Slots and Qt data types). The underlying TCP socket
and the XMPP RFCs (RFC3920 and RFC3921) have been encapsulated into classes and
functions. Therefore the user would not be bothered with these details. But it is
always recommended to the advanced users to read and enjoy the low level details.


%package devel
Summary:      QXmpp Development Files
Requires:     %{name}%{?_isa} = %{version}-%{release}
Obsoletes: qxmpp-dev-devel < 0.7.5
Provides:  qxmpp-dev-devel = %{version}-%{release}

%description devel
It's a development package for qxmpp.

QXmpp is a cross-platform C++ XMPP client library. It is based on Qt and C++.


%package qt5
Summary: QXmpp library for Qt5

%description qt5
QXmpp is a cross-platform C++ XMPP client library. It is based on Qt and C++.


%package qt5-devel
Summary: QXmpp Development Files for Qt5
Requires:     %{name}-qt5%{?_isa} = %{version}-%{release}

%description qt5-devel
It's a development package for qxmpp-qt5.

QXmpp is a cross-platform C++ XMPP client library. It is based on Qt and C++.


%package doc
Summary: QXmpp library documentation

%description doc
QXmpp libraries documentation.


%prep
%setup -q
%patch1 -p1

pushd ..
  cp -r %{name}-%{version} %{name}-qt5-%{version}
  pushd %{name}-qt5-%{version}
  sed -i 's/QXMPP_LIBRARY_NAME = qxmpp/QXMPP_LIBRARY_NAME = qxmpp-qt5/g' qxmpp.pri
  sed -i 's/\$\$PREFIX\/include\/qxmpp/\$\$PREFIX\/include\/qxmpp-qt5/' src/src.pro
popd


%build
%{qmake_qt4} \
  PREFIX=%{_prefix} \
  LIBDIR=%{_lib} \
  QXMPP_USE_DOXYGEN=1 \
  QXMPP_AUTOTEST_INTERNAL=1
make %{?_smp_mflags}

pushd ../%{name}-qt5-%{version}
%{qmake_qt5} PREFIX=%{_prefix} LIBDIR=%{_lib}
make %{?_smp_mflags}
popd

%install
%make_install INSTALL_ROOT=${RPM_BUILD_ROOT}
pushd ../%{name}-qt5-%{version}
  %make_install INSTALL_ROOT=${RPM_BUILD_ROOT}
popd


# move installed docs to include them in -devel package via %%doc magic
rm -rf __tmp_doc ; mkdir __tmp_doc
mv ${RPM_BUILD_ROOT}%{_docdir}/%{name}/* __tmp_doc

%ldconfig_scriptlets -n %{name}

%files
%doc AUTHORS CHANGELOG LICENSE.LGPL README.md
%{_libdir}/libqxmpp.so.0
%{_libdir}/libqxmpp.so.0.9
%{_libdir}/libqxmpp.so.%{version}

%files qt5
%{_libdir}/lib%{name}-qt5.so.0
%{_libdir}/lib%{name}-qt5.so.0.9
%{_libdir}/lib%{name}-qt5.so.%{version}

%files doc
%doc __tmp_doc/*

%files devel
%{_libdir}/lib%{name}.so
%{_includedir}/%{name}
%{_libdir}/pkgconfig/%{name}.pc

%files qt5-devel
%{_libdir}/lib%{name}-qt5.so
%{_includedir}/%{name}-qt5
%{_libdir}/pkgconfig/%{name}-qt5.pc

%changelog
* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.3-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.3-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.3-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.3-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.3-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.3-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.3-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.3-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Feb 01 2016 Rex Dieter <rdieter@fedoraproject.org> - 0.9.3-2
- use %%qmake_qt5/%%qmake_qt4 macros to ensure proper build flags

* Mon Dec 21 2015 Minh Ngo <nlminhtl@gmail.com> - 0.9.3-1
- v0.9.3

* Thu Sep 03 2015 Minh Ngo <nlminhtl@gmail.com> - 0.9.2-1
- v0.9.2. Introducing libraries for qt5. Documentation into the separate package

* Sat Aug 29 2015 Minh Ngo <nlminhtl@gmail.com> - 0.9.0-1
- v0.9.0

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.5-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 0.7.5-6
- Rebuilt for GCC 5 C++11 ABI change

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Dec 13 2013 Michael Schwendt <mschwendt@fedoraproject.org> - 0.7.5-3
- Fix duplicate documentation (#1001295)

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Minh Ngo <nlminhtl@gmail.com> 0.7.5-1
- new version

* Fri Nov 09 2012 Minh Ngo <nlminhtl@gmail.com> 0.7.4-1
- new version

* Sun Sep 30 2012 Minh Ngo <nlminhtl@gmail.com> 0.7.3-4
- Upd. to the last version for leechcraft IC compatibility.

* Wed Sep 26 2012 Minh Ngo <nlminhtl@gmail.com> 0.7.3-2
- Adding obsoletes

* Tue Sep 11 2012 Minh Ngo <nlminhtl@gmail.com> 0.7.3-1
- Renaming package name. Merging code bases between qxmpp-dev and qxmpp.

* Sat Aug 11 2012 Minh Ngo <nlminhtl@gmail.com> 0.6.3.1-1
- Updating to the new version
- Changelog https://raw.github.com/0xd34df00d/qxmpp-dev/master/CHANGELOG

* Thu Apr 26 2012 Minh Ngo <nlminhtl@gmail.com> 0.3.61-1
- XEP 0033

* Sat Mar 17 2012 Minh Ngo <nlminhtl@gmail.com> 0.3.47-1
- Synchronization with upstream
- updating patches

* Wed Mar 14 2012 Minh Ngo <nlminhtl@gmail.com> 0.3.45.2-1
- Synchronization with upstream

* Tue Feb 28 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.45.1-6
- Rebuilt for c++ ABI breakage

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.45.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sun Jan 08 2012 Minh Ngo <nlminhtl@gmail.com> 0.3.45.1-4
- fixing summary/description in the devel package
- adding a dependence for the devel package

* Fri Nov 11 2011 Minh Ngo <nlminhtl@gmail.com> 0.3.45.1-3
- rename the lib to libqxmpp-dev

* Tue Aug 02 2011 Minh Ngo <nlminhtl@gmail.com> 0.3.45.1-2
- dynamic libs

* Mon Jul 25 2011 Minh Ngo <nlminhtl@gmail.com> 0.3.45.1-1
- new version

* Mon Jun 06 2011 Minh Ngo <nlminhtl@gmail.com> 0.3.44-0.1.pre21062011
- initial build
