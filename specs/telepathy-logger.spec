Name:           telepathy-logger
Version:        0.8.2
Release:        22%{?dist}
Summary:        Telepathy framework logging daemon

# Automatically converted from old format: LGPLv2+ - review is highly recommended.
License:        LicenseRef-Callaway-LGPLv2+
URL:            http://telepathy.freedesktop.org/wiki/Logger
Source0:        http://telepathy.freedesktop.org/releases/%{name}/%{name}-%{version}.tar.bz2

# https://bugzilla.redhat.com/show_bug.cgi?id=1800190
Patch0:         0001-tools-Fix-the-build-with-Python-3.patch

BuildRequires: make
BuildRequires:  dbus-daemon
BuildRequires:  dbus-devel >= 1.1.0
BuildRequires:  dbus-glib-devel >= 0.82
BuildRequires:  telepathy-glib-devel >= 0.19.2
BuildRequires:  glib2-devel >= 2.25.11
BuildRequires:  sqlite-devel
BuildRequires:  libxml2-devel
BuildRequires:  gnome-doc-utils
BuildRequires:  intltool
BuildRequires:  gobject-introspection-devel
BuildRequires:  python3-devel
## Build Requires needed for tests.
#BuildRequires:	python-twisted

Requires:       telepathy-filesystem

%description
%{name} is a headless Observer client that logs information
received by the Telepathy framework. It features pluggable
backends to log different sorts of messages, in different formats.


%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%autosetup -p1

# https://fedoraproject.org/wiki/Changes/Make_ambiguous_python_shebangs_error
%py3_shebang_fix tools

# more rpath hacks
%if "%{_libdir}" != "/usr/lib"
sed -i.rpath -e 's|"/lib /usr/lib|"/%{_lib} %{_libdir}|' configure
%endif


%build
%configure --disable-static --enable-introspection=yes
#sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool
make %{?_smp_mflags} V=1


%install
make install DESTDIR=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'


%check
make check


%files
%doc COPYING NEWS README
%{_libexecdir}/%{name}
%{_libdir}/libtelepathy-logger.so.3*
%{_datadir}/glib-2.0/schemas/org.freedesktop.Telepathy.Logger.gschema.xml
%{_datadir}/telepathy/clients/Logger.client
%{_datadir}/dbus-1/services/org.freedesktop.Telepathy.Client.Logger.service
%{_datadir}/dbus-1/services/org.freedesktop.Telepathy.Logger.service
%{_libdir}/girepository-1.0/TelepathyLogger-0.2.typelib


%files devel
%doc %{_datadir}/gtk-doc/html/%{name}/
%{_libdir}/libtelepathy-logger.so
%{_libdir}/pkgconfig/telepathy-logger-0.2.pc
%dir %{_includedir}/telepathy-logger-0.2
%{_includedir}/telepathy-logger-0.2/telepathy-logger/
%{_datadir}/gir-1.0/TelepathyLogger-0.2.gir


%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.2-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Sep 04 2024 Miroslav Suchý <msuchy@redhat.com> - 0.8.2-21
- convert license to SPDX

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.2-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.2-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.2-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.2-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.2-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.2-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.2-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.2-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.2-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Feb 10 2020 Debarshi Ray <rishi@fedoraproject.org> - 0.8.2-11
- Fix the build with Python 3 (RH #1800190)
- Disambiguate the Python shebangs

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Apr 30 2015 Debarshi Ray <rishi@fedoraproject.org> - 0.8.2-1
- Update to 0.8.2

* Tue Apr 21 2015 Debarshi Ray <rishi@fedoraproject.org> - 0.8.0-8
- Backport bug-fixes from upstream (FDO #40675, #54814, #89595)

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Tue Jul 22 2014 Kalev Lember <kalevlember@gmail.com> - 0.8.0-6
- Rebuilt for gobject-introspection 1.41.4

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Feb 14 2014 Debarshi Ray <rishi@fedoraproject.org> - 0.8.0-4
- Enable %%check section

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Mon Jan 21 2013 Debarshi Ray <rishi@fedoraproject.org> - 0.8.0-1
- Update to 0.8.0

* Fri Nov 30 2012 Brian Pepple <bpepple@fedoraproject.org> - 0.6.0-3
- Rebuild.

* Wed Oct 31 2012 Rex Dieter <rdieter@fedoraproject.org> - 0.6.0-2
- track sonames so bumps aren't a surprise
- verbose build
- rpath whack-a-mole

* Tue Oct 30 2012 Brian Pepple <bpepple@fedoraproject.org> - 0.6.0-1
- Update to 0.6.0
- Bump minimum version of tp-glib needed.

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jun 21 2012 Brian Pepple <bpepple@fedoraproject.org> - 0.4.0-3
- Drop depreciated enable-call option.

* Tue Apr 24 2012 Kalev Lember <kalevlember@gmail.com> - 0.4.0-2
- Silence rpm scriptlet output

* Thu Apr  5 2012 Brian Pepple <bpepple@fedoraproject.org> - 0.4.0-1
- Update to 0.4.0.

* Tue Apr  3 2012 Brian Pepple <bpepple@fedoraproject.org> - 0.2.13-1
- Update to 0.2.13.

* Sun Jan 08 2012 Brian Pepple <bpepple@fedoraproject.org> - 0.2.12-3
- Rebuild for new gcc.

* Mon Dec 19 2011 Brian Pepple <bpepple@fedoraproject.org> - 0.2.12-2
- Enable call support again.

* Wed Nov  2 2011 Brian Pepple <bpepple@fedoraproject.org> - 0.2.12-1
- Update to 0.2.12.

* Mon Oct 31 2011 Brian Pepple <bpepple@fedoraproject.org> - 0.2.11-1
- Update to 0.2.11.

* Tue Aug 23 2011 Brian Pepple <bpepple@fedoraproject.org> - 0.2.10-3
- Disable call logging.

* Fri Jun 24 2011 Brian Pepple <bpepple@fedoraproject.org> - 0.2.10-2
- Enable call support.

* Thu May 26 2011 Brian Pepple <bpepple@fedoraproject.org> - 0.2.10-1
- Update to 0.2.10.

* Fri May  6 2011 Brian Pepple <bpepple@fedoraproject.org> - 0.2.9-1
- Update to 0.2.9.

* Thu Mar 31 2011 Brian Pepple <bpepple@fedoraproject.org> - 0.2.8-1
- Update to 0.2.8.
- Bump minimum version of tp-glib needed.
- Drop infinite loop patch. Fixed upstream.

* Wed Mar 30 2011 Brian Pepple <bpepple@fedoraproject.org> - 0.2.7-2
- Backport patch from upstream git for a change that wasn't included with original
  tarball. Refer to http://lists.freedesktop.org/archives/telepathy/2011-March/005381.html

* Fri Mar 25 2011 Brian Pepple <bpepple@fedoraproject.org> - 0.2.7-1
- Update to 0.2.7.

* Tue Mar 22 2011 Brian Pepple <bpepple@fedoraproject.org> - 0.2.6-1
- Update to 0.2.6.
- Enable gobject-introspection.

* Tue Mar  8 2011 Brian Pepple <bpepple@fedoraproject.org> - 0.2.5-1
- Update to 0.2.5.

* Tue Mar  1 2011 Brian Pepple <bpepple@fedoraproject.org> - 0.2.4-1
- Update to 0.2.4.

* Mon Feb 28 2011 Brian Pepple <bpepple@fedoraproject.org> - 0.2.3-1
- Update to 0.2.3.

* Mon Feb 28 2011 Brian Pepple <bpepple@fedoraproject.org> - 0.2.2-1
- Update to 0.2.2.

* Thu Feb 24 2011 Brian Pepple <bpepple@fedoraproject.org> - 0.2.1-1
- Update to 0.2.1.

* Thu Feb 24 2011 Brian Pepple <bpepple@fedoraproject.org> - 0.2.0-1
- Update to 0.2.0.

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Nov 29 2010 Brian Pepple <bpepple@fedoraproject.org> - 0.1.7-1
- Update to 0.1.7.

* Wed Oct 13 2010 Brian Pepple <bpepple@fedoraproject.org> - 0.1.6-1
- Update to 0.1.6.

* Mon Aug 16 2010 Brian Pepple <bpepple@fedoraproject.org> - 0.1.5-1
- Update to 0.1.5.
- Modify spec for change from GConf to gsettings.
- Add BR on intltool.

* Fri Jul  9 2010 Brian Pepple <bpepple@fedoraproject.org> - 0.1.4-1
- Update to 0.1.4.

* Wed Jul  7 2010 Brian Pepple <bpepple@fedoraproject.org> - 0.1.3-2
- Remove unnecessary buildroot info.
- Remove rpath.

* Mon Jun 28 2010 Brian Pepple <bpepple@fedoraproject.org> - 0.1.3-1
- Initial Fedora spec file.
