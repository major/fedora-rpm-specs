
## toggle qt4 support, default off
#global qt4 1

Summary: A multi-platform helper library for other libraries
Name: gwenhywfar
Version: 5.12.0
Release: 2%{?dist}

URL: http://www.aquamaniac.de/sites/download/packages.php?package=01&showall=1
# Download is PHP form at http://www.aquamaniac.de/sites/download/packages.php
Source: https://www.aquamaniac.de/rdm/attachments/download/529/%{name}-%{version}.tar.gz
License: LGPL-2.1-or-later

BuildRequires: cmake gcc gcc-c++
BuildRequires: gnutls-devel gettext libgcrypt-devel openssl-devel
BuildRequires: gtk3-devel >= 3.14.0
BuildRequires: qt5-qtbase-devel

Requires: ca-certificates

%description
This is Gwenhywfar, a multi-platform helper library for networking and
security applications and libraries. It is heavily used by libchipcard
and AqBanking/AqHBCI, the German online banking libraries.

%package devel
Summary: Gwenhywfar core development kit
Requires: %{name}%{?_isa} = %{version}-%{release}
%description devel
This package contains gwenhywfar-config and header files for writing and
compiling programs using Gwenhywfar.

%package gui-gtk3
Summary: Gwenhywfar GUI framework for GTK3
Obsoletes: %{name}-gui-gtk2 <= %{version}-%{release}
Requires: %{name}%{?_isa} = %{version}-%{release}
%description gui-gtk3
This package contains the gtk3 gwenhywfar GUI backend.

%package gui-gtk3-devel
Summary: Development files for %{name}-gui-gtk3
Obsoletes: %{name}-gui-gtk2-devel <= %{version}-%{release}
Requires: %{name}%{?_isa} = %{version}-%{release}
%description gui-gtk3-devel
%{summary}.

%package gui-cpp
Summary: Gwenhywfar GUI framework for cpp
Requires: %{name}%{?_isa} = %{version}-%{release}
%if ! 0%{?qt4}
Obsoletes: %{name}-gui-qt4 < %{version}-%{release}
%endif
%description gui-cpp
This package contains the cpp gwenhywfar GUI backend.

%package gui-cpp-devel
Summary: Development files for %{name}-gui-cpp
%if ! 0%{?qt4}
Obsoletes: %{name}-gui-qt4-devel < %{version}-%{release}
%endif
Requires: %{name}-gui-cpp%{?_isa} = %{version}-%{release}
%description gui-cpp-devel
%{summary}.

%if 0%{?qt4}
%package gui-qt4
Summary: Gwenhywfar GUI framework for Qt4
BuildRequires: qt4-devel >= 4.3.0
BuildRequires: make
Requires: %{name}-gui-cpp%{?_isa} = %{version}-%{release}
%description gui-qt4
This package contains the qt4 gwenhywfar GUI backend.

%package gui-qt4-devel
Summary: Development files for %{name}-qt4-cpp
Requires: %{name}-gui-qt4%{?_isa} = %{version}-%{release}
Requires: %{name}-gui-cpp-devel%{?_isa} = %{version}-%{release}
%description gui-qt4-devel
%{summary}.
%endif

%package gui-qt5
Summary: Gwenhywfar GUI framework for Qt5
Requires: %{name}-gui-cpp%{?_isa} = %{version}-%{release}
%description gui-qt5
This package contains the qt5 gwenhywfar GUI backend.

%package gui-qt5-devel
Summary: Development files for %{name}-qt4-cpp
Requires: %{name}-gui-qt5%{?_isa} = %{version}-%{release}
Requires: %{name}-gui-cpp-devel%{?_isa} = %{version}-%{release}
%description gui-qt5-devel
%{summary}.


%prep
%autosetup -n %{name}-%{version}


%build
export CFLAGS="$CFLAGS -std=gnu17"
export CXXFLAGS="$CXXFLAGS -std=gnu++17"
# avoid detection/use of stuff like x86_64-redhat-linux-gnu-pkg-config -- rdieter
export PKG_CONFIG=/usr/bin/pkg-config
# help configure find qt5 lrelease/lupdate
export QT5_HOST_BINS=$($PKG_CONFIG --variable=host_bins Qt5Core)
export PATH=$PATH:$QT5_HOST_BINS

%configure \
  --disable-static\
  --enable-system-certs \
  --with-guis="gtk3 %{?qt4:qt4} qt5" \
  --with-openssl-libs=%{_libdir} \
%if 0%{?qt4}
  --with-qt4-libs=%{_qt4_libdir} --with-qt4-includes=%{_qt4_headerdir} \
  --with-qt4-moc=%{_bindir}/moc-qt4 \
  --with-qt4-uic=%{_bindir}/uic-qt4 \
%endif
  --with-qt5-qmake=$QT5_HOST_BINS/qmake \
  --with-qt5-moc=$QT5_HOST_BINS/moc \
  --with-qt5-uic=$QT5_HOST_BINS/uic \


# kill rpath
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool

%make_build


%install
%make_install

# use system ca-certificates
rm -f  %{buildroot}%{_datadir}/%{name}/ca-bundle.crt
ln -sf %{_sysconfdir}/pki/tls/certs/ca-bundle.crt \
       %{buildroot}%{_datadir}/%{name}/ca-bundle.crt

rm -fv %{buildroot}%{_libdir}/lib*.la

%find_lang %{name}


%ldconfig_scriptlets

%files -f %{name}.lang
%doc AUTHORS README ChangeLog
%license COPYING
%{_bindir}/gct-tool
%{_libdir}/libgwenhywfar.so.79*
%{_libdir}/gwenhywfar/
%dir %{_datadir}/gwenhywfar/
%{_datadir}/gwenhywfar/dialogs
# symlink
%{_datadir}/gwenhywfar/ca-bundle.crt

%files devel
%{_bindir}/gsa
%{_bindir}/gwenhywfar-config
%{_bindir}/mklistdoc
%{_bindir}/typemaker*
%{_bindir}/xmlmerge
%{_bindir}/gwbuild
%dir %{_includedir}/gwenhywfar5/
%{_includedir}/gwenhywfar5/gwenhywfar/
%{_libdir}/libgwenhywfar.so
%{_libdir}/cmake/gwenhywfar-*/
%{_datadir}/aclocal/gwenhywfar.m4
%{_datadir}/%{name}/typemaker*
%{_libdir}/pkgconfig/gwenhywfar.pc
%{_datadir}/gwenbuild/templates
%{_datadir}/%{name}/gwenbuild
%ldconfig_scriptlets gui-gtk3

%files gui-gtk3
%{_libdir}/libgwengui-gtk3.so.79*

%files gui-gtk3-devel
%{_libdir}/libgwengui-gtk3.so
%{_libdir}/pkgconfig/gwengui-gtk3.pc
%{_includedir}/gwenhywfar5/gwen-gui-gtk3/

%ldconfig_scriptlets gui-cpp

%files gui-cpp
%{_libdir}/libgwengui-cpp.so.79*
%{_includedir}/gwenhywfar5/gwen-gui-cpp/

%files gui-cpp-devel
%{_libdir}/libgwengui-cpp.so
%{_libdir}/cmake/gwengui-cpp-*/

%if 0%{?qt4}
%ldconfig_scriptlets gui-qt4

%files gui-qt4
%{_libdir}/libgwengui-qt4.so.*

%files gui-qt4-devel
%{_libdir}/libgwengui-qt4.so
%{_libdir}/cmake/gwengui-qt4-*/
%{_libdir}/pkgconfig/gwengui-qt4.pc
%{_includedir}/gwenhywfar5/gwen-gui-qt4/
%endif

%ldconfig_scriptlets gui-qt5

%files gui-qt5
%{_libdir}/libgwengui-qt5.so.79*

%files gui-qt5-devel
%{_libdir}/libgwengui-qt5.so
%{_libdir}/cmake/gwengui-qt5-*/
%{_libdir}/pkgconfig/gwengui-qt5.pc
%{_includedir}/gwenhywfar5/gwen-gui-qt5/


%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 5.12.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Tue Dec 17 2024 Gwyn Ciesla <gwync@protonmail.com> - 5.12.0-1
- 5.12.0

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 5.10.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 5.10.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jan 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 5.10.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 28 2023 Gwyn Ciesla <gwync@protonmail.com> - 5.10.2-1
- 5.10.2

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 5.10.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Mar 03 2023 Gwyn Ciesla <gwync@protonmail.com> - 5.10.1-3
- migrated to SPDX license

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 5.10.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Aug 10 2022 Gwyn Ciesla <gwync@protonmail.com> - 5.10.1-1
- 5.10.1

* Mon Aug 01 2022 Gwyn Ciesla <gwync@protonmail.com> - 5.10.0-1
- 5.10.0

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 5.9.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue Feb 15 2022 Gwyn Ciesla <gwync@protonmail.com> - 5.9.0-1
- 5.9.0

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 5.8.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jan 13 2022 Gwyn Ciesla <gwync@protonmail.com> - 5.8.2-1
- 5.8.2

* Thu Dec 30 2021 Gwyn Ciesla <gwync@protonmail.com> - 5.8.1-1
- 5.8.1

* Tue Dec 28 2021 Gwyn Ciesla <gwync@protonmail.com> - 5.8.0-1
- 5.8.0

* Tue Sep 14 2021 Sahana Prasad <sahana@redhat.com> - 5.6.0-3
- Rebuilt with OpenSSL 3.0.0

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 5.6.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon Feb 22 2021 Vasiliy N. Glazov <vascom2@gmail.com> - 5.6.0-1
- Update to 5.6.0

* Tue Feb 16 2021 Vasiliy N. Glazov <vascom2@gmail.com> - 5.5.1-1
- Update to 5.5.1

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 5.4.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jan 20 2021 Vasiliy N. Glazov <vascom2@gmail.com> - 5.4.1-1
- Update to 5.4.1

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 5.3.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 12 2020 Rex Dieter <rdieter@fedoraproject.org> - 5.3.0-2
- track library sonames closer

* Sun May 03 2020 Rex Dieter <rdieter@fedoraproject.org> - 5.3.0-1
- 5.3.0

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 5.1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Jan 21 2020 Rex Dieter <rdieter@fedoraproject.org> - 5.1.2-1
- 5.1.2
- toggle qt4 support off

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.20.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.20.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.20.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Apr 03 2018 Bill Nottingham <notting@splat.cc> - 4.20.0-2
- update to 4.20.0
- s/gtk2/gtk3/
- add obsoletes for gtk2 package

* Mon Mar 19 2018 Rex Dieter <rdieter@fedoraproject.org> - 4.15.3-9
- spilt out gui-{cpp,gtk2,qt4,qt5}-devel

* Sun Mar 18 2018 Rex Dieter <rdieter@fedoraproject.org> - 4.15.3-8
- .spec cleanup
- drop deprecated bits (Group, %%defattr)
- use %%make_build %%make_install %%license %%ldconfig_scriptlets

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.15.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Aug 07 2017 Björn Esser <besser82@fedoraproject.org> - 4.15.3-6
- Rebuilt for AutoReq cmake-filesystem

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.15.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.15.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.15.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Jul 26 2016 Rex Dieter <rdieter@fedoraproject.org> - 4.15.3-2
- BR: cmake , for cmake() auto-generated Provides

* Thu Jul 07 2016 Bill Nottingham <notting@splat.cc> - 4.15.3-1
- update to 4.15.3

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 4.13.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Dec 11 2015 Bill Nottingham <notting@splat.cc> - 4.13.1-5
- Use system ca-certificates (#1272503, <yselkowi@redhat.com>)
- Fix build (#1239551)

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.13.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 4.13.1-3
- Rebuilt for GCC 5 C++11 ABI change

* Wed Apr  1 2015 Bill Nottingham <notting@splat.cc> - 4.13.1-2
- hardcode some dependencies in -devel package to work around #1207945

* Mon Mar 23 2015 Robert Scheck <robert@fedoraproject.org> - 4.13.1-1
- update to latest upstream

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.10.0-0.4.beta
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.10.0-0.3.beta
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Apr 22 2014 Tomas Mraz <tmraz@redhat.com> - 4.10.0-0.2.beta
- rebuilt with new libgcrypt

* Fri Jan 31 2014 Bill Nottingham <notting@redhat.com> - 4.10.0-0.1.beta
- update to latest upstream

* Wed Jan 15 2014 Bill Nottingham <notting@redhat.com> - 4.9.0-0.2.beta
- update to latest upstream

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.3.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue Apr 23 2013 Bill Nottingham <notting@redhat.com> - 4.3.3-1
- update to latest upstream

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.3.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.3.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jan 19 2012 Bill Nottingham <notting@redhat.com> - 4.3.1-2
- update to latest upstream

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Fri Oct  7 2011 Bill Nottingham <notting@redhat.com> - 4.3.0-1
- update to latest upstream

* Fri Feb 11 2011 Bill Nottingham <notting@redhat.com> - 4.0.5-1
- update to latest upstream

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.11.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Jan 21 2010 Bill Nottingham <notting@redhat.com> - 3.11.3-2
- update to latest upstream
- shuffle some files between main and devel package

* Fri Aug 21 2009 Tomas Mraz <tmraz@redhat.com> - 3.7.2-4
- rebuilt with new openssl

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.7.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Apr 15 2009 Bill Nottingham <notting@redhat.com> - 3.7.2-2
- buildrequire openssl-devel, for gct-tool (#495813)

* Thu Mar  5 2009 Bill Nottingham <notting@redhat.com> - 3.7.2-1
- update to 3.7.2

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.4.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Tue Sep  9 2008 Bill Nottingham <notting@redhat.com> - 3.4.1-1
- update to 3.4.1

* Thu Feb 14 2008 Bill Nottingham <notting@redhat.com> - 2.6.2-2
- rebuild with gcc-4.3

* Tue Jan 15 2008 Bill Nottingham <notting@redhat.com> - 2.6.2-1
- update to 2.6.2

* Wed Dec  5 2007 Bill Nottingham <notting@redhat.com> - 2.6.1-3
- rebuild for new openssl

* Wed Oct 10 2007 Bill Nottingham <notting@redhat.com> - 2.6.1-2
- fix build, rebuild for buildid

* Fri Aug  3 2007 Bill Nottingham <notting@redhat.com>
- tweak license tag

* Wed Jul 11 2007 Bill Nottingham <notting@redhat.com> - 2.6.1-1
- update to 2.6.1

* Mon Jun 11 2007 Bill Nottingham <notting@redhat.com> - 2.6.0-1
- update to 2.6.0

* Mon Mar 19 2007 Bill Nottingham <notting@redhat.com> - 2.5.4-1
- update to 2.5.4

* Thu Feb 22 2007 Bill Nottingham <notting@redhat.com> - 2.3.0-7
- build for Extras

* Wed Jan 10 2007 Bill Nottingham <notting@redhat.com> - 2.3.0-6
- make gwen-public-ca.crt %%config(noreplace)

* Tue Jan  9 2007 Bill Nottingham <notting@redhat.com> - 2.3.0-5
- spec tweaks

* Thu Sep  7 2006 Bill Nottingham <notting@redhat.com> - 2.3.0-4
- rebuild for fixed debuginfo (#205501)

* Tue Sep  5 2006 Bill Nottingham <notting@redhat.com> - 2.3.0-3
- fix multilib conflicts (#205213)

* Fri Jul 14 2006 Bill Nottingham <notting@redhat.com> - 2.3.0-2
- rather than modifying the m4 file, make gwenhywfar-config use pkgconfig

* Wed Jul 12 2006 Jesse Keating <jkeating@redhat.com> - 2.3.0-1.1
- rebuild

* Tue Jul 11 2006 Bill Nottingham <notting@redhat.com> - 2.3.0-1
- update to 2.3.0

* Fri Feb 10 2006 Jesse Keating <jkeating@redhat.com> - 1.99.2-1.2
- bump again for double-long bug on ppc(64)

* Tue Feb 07 2006 Jesse Keating <jkeating@redhat.com> - 1.99.2-1.1
- rebuilt for new gcc4.1 snapshot and glibc changes

* Thu Dec 22 2005 Bill Nottingham <notting@redhat.com> 1.99.2-1
- update to 1.99.2
- use the pkgconfig file, not gwenhywfar-config

* Fri Dec 09 2005 Jesse Keating <jkeating@redhat.com>
- rebuilt

* Wed Nov  9 2005 Tomas Mraz <tmraz@redhat.com> 1.7.2-3
- rebuilt against new openssl

* Wed Mar  2 2005 Bill Nottingham <notting@redhat.com> 1.7.2-2
- rebuild against new openssl

* Wed Feb  9 2005 Bill Nottingham <notting@redhat.com> 1.7.2-1
- initial packaging, adopt upstream package
