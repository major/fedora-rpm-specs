# correct the Obsoletes version in case of disabling it after being enabled
%global with_akonadi 0

Summary:       SyncML client for evolution
Name:          syncevolution
Epoch:         1
Version:       2.0.0
Release:       15%{?dist}
License:       LGPL-2.0-or-later
URL:           http://syncevolution.org/
Source:        http://downloads.syncevolution.org/%{name}/sources/%{name}-%{version}.tar.gz

Patch1:        syncevolution-1.5.1-libical2.patch
Patch2:        syncevolution-1.5.3-autoconf-2.71.patch
Patch3:        003-pcre2.patch
Patch4:        004-cpp-curl.patch
Patch5:        005-gcc-c23-changes.patch

BuildRequires: pkgconfig(dbus-glib-1)

%if 0%{with_akonadi}
BuildRequires: pkgconfig(akonadi)
BuildRequires: kdelibs-devel
BuildRequires: kdepimlibs-devel
%else
Obsoletes: %{name}-libs-akonadi < 2.0.0-10
%endif

BuildRequires: perl-generators
BuildRequires: bluez-libs-devel
BuildRequires: boost-devel >= 1.73.0
BuildRequires: cppunit-devel
BuildRequires: evolution-data-server-devel >= 3.45.1
BuildRequires: expat-devel
BuildRequires: glib2-devel
BuildRequires: gnome-online-accounts-devel
BuildRequires: gtk3-devel
BuildRequires: libcurl-devel
BuildRequires: libgnome-keyring-devel
BuildRequires: libical-devel >= 2.0.0
BuildRequires: libnotify-devel
BuildRequires: neon-devel
BuildRequires: pkgconfig(libpcre2-8)
BuildRequires: python3
BuildRequires: python3-docutils
BuildRequires: python3-pygments
BuildRequires: unique3-devel
%ifnarch s390 s390x
BuildRequires: openobex-devel
%endif

BuildRequires: desktop-file-utils
BuildRequires: gcc
BuildRequires: gcc-c++
BuildRequires: gettext
BuildRequires: intltool
BuildRequires: libtool
BuildRequires: make
BuildRequires: systemd

Requires: python3-dbus
Requires: python3-twisted

%description
syncevolution is designed to provide a SyncML client that can
connect to and sync with various SyncML-based servers

%package libs
Summary: Library package for %{name}

%description libs
Libraries for %{name}.

%package devel
Summary: Development package for %{name}
Requires: %{name} = %{epoch}:%{version}-%{release}
Requires: pkgconfig

%description devel
Files for development with %{name}.

%package gtk
Summary: GTK+ GUI for %{name}
Requires: %{name} = %{epoch}:%{version}-%{release}

%description gtk
GTK+ GUI for use with %{name}.

%package perl
Summary: Perl utils for %{name}
Requires: %{name} = %{epoch}:%{version}-%{release}

%description perl
Perl utils for use with %{name}.

%if 0%{with_akonadi}
%package libs-akonadi
Summary: Akonadi backend package for %{name}

%description libs-akonadi
Akonadi backend for %{name}.
%endif

%prep
%autosetup -p1 -S gendiff

# use the ac macros in Makefile.am
sed -i '/^ACLOCAL_AMFLAGS/{ /m4-repo/!s/$/ -I m4-repo/ }' Makefile*.am

%build
autoupdate
intltoolize --automake --copy --force
autoreconf -fiv

pushd src/synthesis
autoupdate
autoreconf -fi
./autogen.sh
popd

%configure --enable-libcurl --disable-libsoup --enable-dbus-service --enable-shared \
    --disable-static --enable-gtk=3 --enable-gui --with-gio-gdbus \
    --enable-dav --disable-static --enable-gtk=3 --enable-gui \
    --enable-gnome-keyring --enable-pbap \
%if 0%{with_akonadi}
     --enable-akonadi \
%else
     --disable-akonadi \
%endif
%ifnarch s390 s390x
    --enable-bluetooth
%else
    --disable-bluetooth
%endif

sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g
	s|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool

make %{?_smp_mflags} V=1
find . -type d -perm 02755 -exec chmod 0755 '{}' \;

%install
make install DESTDIR=%{buildroot} docdir=%{_docdir}
rm -rf %{buildroot}%{_datadir}/doc

# even the build is disabled, there is still created the file with some minimal content
%if !0%{with_akonadi}
rm %{buildroot}%{_libdir}/syncevolution/backends/syncakonadi.so
%endif

#Remove libtool archives
find %{buildroot} -type f -name "*.la" -delete

%find_lang %{name}

desktop-file-validate %{buildroot}/%{_datadir}/applications/sync.desktop

%ldconfig_scriptlets

%files -f %{name}.lang
%doc AUTHORS NEWS README HACKING README.html README.rst
%{_sysconfdir}/xdg/autostart/syncevo-dbus-server.desktop
%{_userunitdir}/syncevo-dbus-server.service
%{_bindir}/syncevolution
%{_bindir}/syncevo-http-server
%{_bindir}/syncevo-phone-config
%{_bindir}/syncevo-webdav-lookup
%{_bindir}/synclog2html
%{_libexecdir}/syncevo-dbus-helper
%{_libexecdir}/syncevo-dbus-server
%{_libexecdir}/syncevo-dbus-server-startup.sh
%{_libexecdir}/syncevo-local-sync
%{_datadir}/syncevolution
%{_datadir}/dbus-1/services/org.syncevolution.service
%{_datadir}/man/man1/syncevolution.1.gz
%exclude %{_datadir}/syncevolution/xml/*.pl

%files libs
%doc COPYING LICENSE.LGPL-21 LICENSE.txt
%{_libdir}/*so.0*
%dir %{_libdir}/syncevolution
%{_libdir}/syncevolution/backends/platformgnome.so
%{_libdir}/syncevolution/backends/platformkde.so
%{_libdir}/syncevolution/backends/platformtde.so
%{_libdir}/syncevolution/backends/providergoa.so
%{_libdir}/syncevolution/backends/syncactivesync.so
%{_libdir}/syncevolution/backends/syncdav.so
%{_libdir}/syncevolution/backends/syncebook.so
%{_libdir}/syncevolution/backends/syncecal.so
%{_libdir}/syncevolution/backends/syncfile.so
%{_libdir}/syncevolution/backends/synckcalextended.so
%{_libdir}/syncevolution/backends/syncmaemocal.so
%{_libdir}/syncevolution/backends/syncpbap.so
%{_libdir}/syncevolution/backends/syncqtcontacts.so
%{_libdir}/syncevolution/backends/syncsqlite.so
%{_libdir}/syncevolution/backends/synctdepimabc.so
%{_libdir}/syncevolution/backends/synctdepimcal.so
%{_libdir}/syncevolution/backends/synctdepimnotes.so
%{_libdir}/syncevolution/backends/syncxmlrpc.so

%if 0%{with_akonadi}
%files libs-akonadi
%{_libdir}/syncevolution/backends/syncakonadi.so
%endif

%files devel
%{_includedir}/syncevo
%{_includedir}/syncevo-dbus
%{_includedir}/synthesis
%{_libdir}/pkgconfig/s*.pc
%{_libdir}/*.so
%{_libdir}/*.a

%files gtk
%{_bindir}/sync-ui
%{_datadir}/applications/sync.desktop
%{_datadir}/icons/hicolor/48x48/apps/sync.png

%files perl
%{_bindir}/synccompare
%{_datadir}/syncevolution/xml/*.pl

%changelog
* Wed Jan 22 2025 Milan Crha <mcrha@redhat.com> - 1:2.0.0-15
- Add patch to build with gcc C23

* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1:2.0.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1:2.0.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1:2.0.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 08 2024 Milan Crha <mcrha@redhat.com> - 1:2.0.0-11
- Rebuilt for evolution-data-server soname version bump

* Mon Dec 18 2023 Milan Crha <mcrha@redhat.com> - 1:2.0.0-10
- Disable build of libs-akonadi subpackage

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1:2.0.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Mar 03 2023 Milan Crha <mcrha@redhat.com> - 1:2.0.0-8
- Resolves: #2172377 (Crash under Curl_fillreadbuffer())

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1:2.0.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Sep 21 2022 Milan Crha <mcrha@redhat.com> - 1:2.0.0-6
- Resolves: #2128381 (Port to pcre2)
- Disable build of the libsoup transport layer (previous change only enabled libcurl)

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1:2.0.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue Jul 19 2022 Milan Crha <mcrha@redhat.com> - 1:2.0.0-4
- Rebuilt for evolution-data-server soname version bump
- Switch from libsoup to libcurl for transport

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1:2.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1:2.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Apr 06 2021 Milan Crha <mcrha@redhat.com> - 1:2.0.0-1
- Update to 2.0.0

* Fri Mar 26 2021 Milan Crha <mcrha@redhat.com> - 1:1.5.3-18
- Add patch to build with autoconf 2.71

* Fri Feb 12 2021 Milan Crha <mcrha@redhat.com> - 1:1.5.3-17
- Rebuilt for evolution-data-server soname version bump

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.5.3-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Aug 18 2020 Jeff Law <law@redhat.com> - 1:1.5.3-15
- Force C++14 as this code is not C++17 ready

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.5.3-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 07 2020 Milan Crha <mcrha@redhat.com> - 1:1.5.3-13
- Rebuilt for evolution-data-server soname version bump
- Add patch to build with boost 1.73.0

* Mon May 11 2020 Milan Crha <mcrha@redhat.com> - 1:1.5.3-12
- Add patch by David Hampton to correct python3 conversion (RH bug #1833578)

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.5.3-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Nov 11 2019 Milan Crha <mcrha@redhat.com> - 1:1.5.3-10
- Add patch to fix a crash when synchronizing events (related to libecal-2.0 port)

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.5.3-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed May 22 2019 Milan Crha <mcrha@redhat.com> - 1:1.5.3-8
- Add patch to switch to python3

* Tue May 21 2019 Milan Crha <mcrha@redhat.com> - 1:1.5.3-7
- Add patch to build against newer evolution-data-server (libecal-2.0)

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.5.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Jul 16 2018 Milan Crha <mcrha@redhat.com> - 1:1.5.3-5
- Add patch to use /usr/bin/python2 shebangs

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.5.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Kalev Lember <klember@redhat.com> - 1:1.5.3-4
- Rebuilt for evolution-data-server soname bump

* Thu Feb 01 2018 Iryna Shcherbina <ishcherb@redhat.com> - 1:1.5.3-3
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Thu Jan 18 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1:1.5.3-2
- Remove obsolete scriptlets

* Wed Jan 10 2018 Milan Crha <mcrha@redhat.com> - 1:1.5.3-1
- Update to 1.5.3

* Thu Nov 16 2017 Milan Crha <mcrha@redhat.com> - 1:1.5.2-6
- Add patch to build with libical 3.0.0

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.5.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.5.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri May 05 2017 Milan Crha <mcrha@redhat.com> - 1:1.5.2-3
- Rebuild for newer cppunit

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.5.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Nov 10 2016 Milan Crha <mcrha@redhat.com> - 1:1.5.2-1
- Update to 1.5.2
- Remove patch for GCC 6 build break (fixed upstream)

* Tue Oct 25 2016 Milan Crha <mcrha@redhat.com> - 1:1.5.1-12
- Rebuild for newer evolution-data-server

* Mon Jul 18 2016 Milan Crha <mcrha@redhat.com> - 1:1.5.1-11
- Rebuild for newer evolution-data-server

* Tue Jun 21 2016 Milan Crha <mcrha@redhat.com> - 1:1.5.1-10
- Rebuild for newer evolution-data-server

* Mon Feb 15 2016 Milan Crha <mcrha@redhat.com> - 1:1.5.1-9
- Add patch for GCC 6 build break
- Use -std=gnu++98 and -fPIC in CXXFLAGS

* Sun Feb 14 2016 David Tardon <dtardon@redhat.com> - 1:1.5.1-9
- rebuild for cppunit 1.13.2

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.5.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Jan 18 2016 Milan Crha <mcrha@redhat.com> - 1:1.5.1-7
- Rebuild for newer evolution-data-server
- Add patch to build against libical 2.0.0

* Thu Aug 27 2015 Jonathan Wakely <jwakely@redhat.com> - 1:1.5.1-6
- Rebuilt for Boost 1.59

* Wed Jul 29 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:1.5.1-5
- Rebuilt for https://fedoraproject.org/wiki/Changes/F23Boost159

* Wed Jul 22 2015 David Tardon <dtardon@redhat.com> - 1:1.5.1-4
- rebuild for Boost 1.58

* Wed Jul 22 2015 Milan Crha <mcrha@redhat.com> - 1:1.5.1-3
- Rebuild for newer evolution-data-server

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:1.5.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Jun 09 2015 Milan Crha <mcrha@redhat.com> - 1:1.5.1-1
- Update to 1.5.1

* Tue Apr 28 2015 Milan Crha <mcrha@redhat.com> - 1:1.5-3
- Rebuild for newer evolution-data-server

* Tue Jan 27 2015 Petr Machata <pmachata@redhat.com> - 1:1.5-2
- Rebuild for boost 1.57.0

* Wed Nov 05 2014 Milan Crha <mcrha@redhat.com> - 1:1.5-1
- Update to 1.5 stable release

* Wed Sep 24 2014 Milan Crha <mcrha@redhat.com> - 1:1.4.1-7
- Rebuild against newer evolution-data-server

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:1.4.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Wed Jul 30 2014 Milan Crha <mcrha@redhat.com> - 1:1.4.1-5
- Rebuild against newer evolution-data-server

* Fri Jun 27 2014 Milan Crha <mcrha@redhat.com> - 1:1.4.1-4
- Enable Akonadi and pbap backends

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:1.4.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu May 22 2014 Petr Machata <pmachata@redhat.com> - 1:1.4.1-2
- Rebuild for boost 1.55.0

* Mon Apr 14 2014 Peter Robinson <pbrobinson@fedoraproject.org> 1.4.1-1
- Update to 1.4.1 stable release

* Tue Feb 18 2014 Peter Robinson <pbrobinson@fedoraproject.org> 1.4-1
- Update to 1.4 stable release
- Enable gnome-online-accounts support

* Tue Feb  4 2014 Peter Robinson <pbrobinson@fedoraproject.org> 1.3.99.7-1
- 1.3.99.7 devel release

* Mon Feb 03 2014 Milan Crha <mcrha@redhat.com> - 1.3.99.6-3
- Rebuild against newer evolution-data-server

* Tue Jan 14 2014 Milan Crha <mcrha@redhat.com> - 1.3.99.6-2
- Rebuild against newer evolution-data-server

* Tue Dec 10 2013 Peter Robinson <pbrobinson@fedoraproject.org> 1.3.99.6-1
- 1.3.99.6 devel release

* Thu Nov 21 2013 Milan Crha <mcrha@redhat.com> - 1.3.99.3-9
- Rebuild for new libical (RH bug #1023020)

* Tue Nov 19 2013 Milan Crha <mcrha@redhat.com> - 1.3.99.3-8
- Rebuild against newer evolution-data-server

* Fri Nov 08 2013 Milan Crha <mcrha@redhat.com> - 1.3.99.3-7
- Rebuild against newer evolution-data-server
- Add an upstream patch for a build break

* Mon Aug 19 2013 Milan Crha <mcrha@redhat.com> - 1.3.99.3-6
- Rebuild against newer evolution-data-server

* Tue Jul 30 2013 Petr Machata <pmachata@redhat.com> - 1:1.3.99.3-5
- Rebuild for boost 1.54.0

* Tue Jul 30 2013 Milan Crha <mcrha@redhat.com> - 1.3.99.3-4
- Rebuild against newer evolution-data-server

* Wed Jul 10 2013 Milan Crha <mcrha@redhat.com> - 1.3.99.3-3
- Rebuild against newer evolution-data-server

* Fri May 24 2013 Rex Dieter <rdieter@fedoraproject.org> 1.3.99.3-2
- rebuild (libical)

* Mon Mar 18 2013 Peter Robinson <pbrobinson@fedoraproject.org> 1.3.99.3-1
- 1.3.99.3 devel release

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:1.3.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Tue Dec 25 2012 Bruno Wolff III <bruno@wolff.to> - 1:1.3.2-2
- Rebuild for libcamel soname bump

* Sat Dec  1 2012 Peter Robinson <pbrobinson@fedoraproject.org> 1:1.3.2-1
- 1.3.2 stable release
- Drop old dependencies and force build against gtk3
- Update icon cache for desktop icon

* Tue Nov 20 2012 Milan Crha <mcrha@redhat.com> - 1:1.3.1-4
- Rebuild against newer evolution-data-server

* Thu Oct 25 2012 Milan Crha <mcrha@redhat.com> - 1:1.3.1-3
- Rebuild against newer evolution-data-server

* Sat Oct 20 2012 Peter Robinson <pbrobinson@fedoraproject.org>	1:1.3.1-2
- Fix desktop file, enable DAV

* Mon Oct  8 2012 Peter Robinson <pbrobinson@fedoraproject.org> 1:1.3.1-1
- 1.3.1 stable release

* Tue Sep 18 2012 Peter Robinson <pbrobinson@fedoraproject.org> - 1:1.3-2
- Add patch to fix build detecting gio

* Mon Sep 17 2012 Peter Robinson <pbrobinson@fedoraproject.org> - 1:1.3-1
- 1.3 stable release

* Wed Aug  8 2012 Peter Robinson <pbrobinson@fedoraproject.org> - 1:1.2.99.4-1
- Update to 1.2.99.4 devel release

* Sat Jul 28 2012 Peter Robinson <pbrobinson@fedoraproject.org> - 1:1.2.99.3-1
- Update to 1.2.99.3 devel release
- Drop MeeGo sub package
- Drop gdbus patch as it's now fixed upstream

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:1.2.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed May 02 2012 Milan Crha <mcrha@redhat.com> - 1:1.2.2-3
- Rebuild against newer evolution-data-server

* Fri Feb 10 2012 Petr Pisar <ppisar@redhat.com> - 1:1.2.2-2
- Rebuild against PCRE 8.30

* Tue Jan 17 2012 Peter Robinson <pbrobinson@fedoraproject.org> - 1:1.2.2-1
- 1.2.2 stable release

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:1.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Nov 28 2011 Peter Robinson <pbrobinson@fedoraproject.org> - 1:1.2.1-1
- 1.2.1 stable release
- Add patch to build it (help from Patrick Ohly)

* Tue Nov 22 2011 Peter Robinson <pbrobinson@fedoraproject.org> - 1:1.2-3
- Rebuild against newer evolution-data-server

* Sun Oct 30 2011 Bruno Wolff III <bruno@wolff.to> - 1:1.2-2
- Rebuild against newer evolution-data-server

* Mon Oct 17 2011 Peter Robinson <pbrobinson@fedoraproject.org> - 1:1.2-1
- 1.2 stable release

* Thu Oct 13 2011 Peter Robinson <pbrobinson@fedoraproject.org> - 1:1.1.99.7-2
- Own syncevolution directory - fixes RHBZ 744929

* Fri Sep 16 2011 Peter Robinson <pbrobinson@fedoraproject.org> - 1:1.1.99.7-1
- update to 1.1.99.7

* Tue Aug 30 2011 Milan Crha <mcrha@redhat.com> - 1:1.1.99.6-3
- Sync version with f16 branch

* Mon Aug 29 2011 Milan Crha <mcrha@redhat.com> - 1:1.1.99.6-2
- Rebuild against newer evolution-data-server

* Thu Aug 18 2011 Peter Robinson <pbrobinson@fedoraproject.org> - 1:1.1.99.6-1
- update to 1.1.99.6
- Add static libs to devel as they are needed for dev :-/ Fixes # 715131

* Tue Aug 16 2011 Milan Crha <mcrha@redhat.com> - 1:1.1.99.5a-3
- Rebuild against newer evolution-data-server

* Sun Jul 24 2011 Peter Robinson <pbrobinson@fedoraproject.org> - 1:1.1.99.5a-2
- Rebuild against newer evolution-data-server

* Fri Jul 15 2011 Peter Robinson <pbrobinson@fedoraproject.org> - 1:1.1.99.5a-1
- Update to 1.1.99.5a devel release

* Thu Jun 16 2011 Milan Crha <mcrha@redhat.com> 1:1.1.99.4-3
- Rebuild against newer evolution-data-server

* Fri May 20 2011 Kalev Lember <kalev@smartlink.ee> - 1:1.1.99.4-2
- Rebuilt for libcamel soname bump

* Thu Apr 28 2011 Peter Robinson <pbrobinson@fedoraproject.org> - 1:1.1.99.4-1
- Update to 1.1.99.4 devel release

* Thu Mar 3 2011 Adam Williamson <awilliam@redhat.com> - 1:1.1.1-6
- build the private libgdbus statically again for now to avoid crasher

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:1.1.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Feb  3 2011 Dan Horák <dan[at]danny.cz> 1:1.1.1-4
- fix build on s390 where size_t != unsigned int

* Tue Feb  1 2011 Dan Horák <dan[at]danny.cz> 1:1.1.1-3
- fix build with gcc 4.6
- disable bluetooth on s390(x)

* Wed Jan 12 2011 Milan Crha <mcrha@redhat.com> 1:1.1.1-2
- Rebuild against newer evolution-data-server

* Sun Dec 26 2010 Peter Robinson <pbrobinson@fedoraproject.org> - 1:1.1.1-1
- Update to 1.1.1 stable release

* Tue Dec 14 2010 Adam Williamson <awilliam@redhat.com> - 1:1.1-4
- really fix the obsolete

* Sun Dec  5 2010 Peter Robinson <pbrobinson@fedoraproject.org> - 1:1.1-3
- Update deps and other spec bits

* Wed Nov 24 2010 Adam Williamson <awilliam@redhat.com> - 1:1.1-2
- add libnotify07 patch to build against libnotify 0.7

* Tue Oct 26 2010 Peter Robinson <pbrobinson@fedoraproject.org> - 1:1.1-1
- Update to 1.1 stable release

* Sat Oct 16 2010 Peter Robinson <pbrobinson@fedoraproject.org> - 1:1.0.99.7-2
- Bump build, rename moblin subpackage to meego

* Fri Oct  1 2010 Peter Robinson <pbrobinson@fedoraproject.org> - 1:1.0.99.7-1
- Update to 1.0.99.7 devel release

* Wed Sep 29 2010 jkeating - 1:1.0.99.6-3
- Rebuilt for gcc bug 634757

* Tue Sep 21 2010 Peter Robinson <pbrobinson@fedoraproject.org> - 1:1.0.99.6-2
- Enable bluetooth support. Fixes RHBZ # 612000

* Tue Sep 14 2010 Peter Robinson <pbrobinson@fedoraproject.org> - 1:1.0.99.6-1
- Update to 1.0.99.6 devel release

ntteo centra Sat Aug  7 2010 Peter Robinson <pbrobinson@fedoraproject.org> - 1:1.0.1-5
- fix the binary name in the desktop file

* Fri Jul 23 2010 Peter Robinson <pbrobinson@fedoraproject.org> - 1:1.0.1-4
- And twice more with feeling

* Fri Jul 23 2010 Peter Robinson <pbrobinson@fedoraproject.org> - 1:1.0.1-3
- And once more with feeling

* Fri Jul 23 2010 Peter Robinson <pbrobinson@fedoraproject.org> - 1:1.0.1-2
- Add patch to fix linking against libnotify and gtk-2.0 (thanks hadess)

* Fri Jul 23 2010 Peter Robinson <pbrobinson@fedoraproject.org> - 1:1.0.1-1
- Update to new 1.0.1 stable release

* Mon Jul 12 2010 Peter Robinson <pbrobinson@fedoraproject.org> - 1:1.0-2
- Move license to libs

* Sun Jun 20 2010 Peter Robinson <pbrobinson@fedoraproject.org> - 1:1.0-1
- Add epoch to fix upgrades

* Sat Jun 19 2010 Peter Robinson <pbrobinson@fedoraproject.org> - 1.0-1
- Update to new 1.0.0 stable release, split out libs

* Wed May 26 2010 Peter Robinson <pbrobinson@fedoraproject.org> - 1.0beta3-2
- Bump build for new evolution

* Tue May  4 2010 Peter Robinson <pbrobinson@fedoraproject.org> - 1.0beta3-2
- Fix file moves and additions

* Wed Apr 21 2010 Peter Robinson <pbrobinson@fedoraproject.org> - 1.0beta3-1
- Update to 1.0.0 beta 3

* Wed Jan 27 2010 Peter Robinson <pbrobinson@fedoraproject.org> - 1.0beta1-1
- Update to 1.0.0 beta 1

* Thu Dec  3 2009 Peter Robinson <pbrobinson@fedoraproject.org> - 0.9.2+1.0alpha1-1
- Update to 1.0.0 alpha 1

* Tue Nov 17 2009 Peter Robinson <pbrobinson@fedoraproject.org> - 0.9-3
- Spec updates, split perl utils into sub-package

* Fri Oct 16 2009 Peter Robinson <pbrobinson@fedoraproject.org> - 0.9-2
- Enable the gtk and moblin guis

* Fri Sep 25 2009 Matěj Cepl <mcepl@redhat.com> - 0.9-1
- New upstream release.

* Wed Aug  5 2009 Matěj Cepl <mcepl@redhat.com> - 0.8.1+0.9+beta3+20090723-1.0.3
- missing BuildRequires

* Wed Aug  5 2009 Stepan Kasal <skasal@redhat.com> - 0.8.1+0.9+beta3+20090723-1.0.2
- fixing autoconfigury; now it fails in a later stage of build ;-)

* Wed Aug  5 2009 Matěj Cepl <mcepl@redhat.com> - 0.8.1+0.9+beta3+20090723-1.0.1
- fixing rpath, currently FTBFS!!!

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.1a-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon Mar 23 2009 Matej Cepl <mcepl@redhat.com> 0.8.1a-1
- New upstream release.
- make a fix for one #elif which should be #else

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Oct  6 2008 Alex Lancaster <alexlan[AT] fedoraproject.org> - 0.7-4
- Rebuild against new libcppunit to fix broken deps

* Fri Aug 01 2008 Matěj Cepl <mcepl@redhat.com> 0.7-3
- Bump the release to fix broken update path for Rawhide

* Fri Feb 15 2008 Matěj Cepl <mcepl@redhat.com> 0.7-2
- Add #include <memory> to syncevolution.cpp according
  to https://sourceforge.net/tracker/\
  ?func=detail&amp;atid=764733&amp;aid=1893582&amp;group_id=146288

* Wed Feb 13 2008 Matěj Cepl <mcepl@redhat.com> 0.7-1
- New upstream version.

* Mon Oct 15 2007 matej <mcepl@redhat.com> 0.6-2
- updated SPEC to make the package approved for the Fedora
  review process.

* Fri Oct 12 2007 Matěj Cepl <mcepl@redhat.com> 0.6-1
- Fixing .spec -- use make install and others
- Install also configuration templates to %%docs

* Sun Sep 30 2007 Matěj Cepl <mcepl@redhat.com> 0.6-0
- Experimental build from upstream source.

* Tue Jan 16 2007 Richard Monk <rmonk@redhat.com> 0.5-1
- Inital packaging
