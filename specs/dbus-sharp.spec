%define debug_package %{nil}

Summary: C# bindings for D-Bus
Name: dbus-sharp
Version: 0.8.1
Release: 23%{?dist}
Epoch: 2
URL: http://mono.github.com/dbus-sharp/
Source0: https://github.com/downloads/mono/dbus-sharp/%{name}-%{version}.tar.gz
Patch0: dbus-sharp-0.8.1-fix-framework.patch
Patch1: dbus-sharp-0.8.1-enable-dbus-property-extraction.patch
Patch2: dbus-sharp-0.8.1-fix-array-writing.patch
Patch3: dbus-sharp-0.8.1-no-check-exists.patch
Patch4: dbus-sharp-0.8.1-mono-4.8-cleanups.patch
# based on https://github.com/mono/dbus-sharp/pull/23/commits/fb4ce33375bd4693e418089e2f379554ee52df67
Patch5: dbus-sharp-0.8.1-trapping.patch
License: MIT
BuildRequires: mono-devel
BuildRequires: autoconf, automake, libtool
BuildRequires: make
# Mono only available on these:
ExclusiveArch: %mono_arches

%description
D-Bus mono bindings for use with mono programs.

%package devel
Summary: Development files for D-Bus Sharp
Requires: %name = %{epoch}:%{version}-%{release}
Requires: pkgconfig

%description devel
Development files for D-Bus Sharp development.

%prep
%setup -q
%patch -P0 -p1 -b .fixframework
%patch -P1 -p1 -b .propfix
# %%patch2 -p1 -b .fixarray
%patch -P3 -p1 -b .nocheckexists
%patch -P4 -p1 -b .cleanups
%patch -P5 -p1 -b .trapping

sed -i "s#gmcs#mcs#g" configure
sed -i "s#gmcs#mcs#g" configure.ac

%build
autoreconf -vif
export MONO_SHARED_DIR=%{_builddir}/%{?buildsubdir}
%configure --libdir=%{_prefix}/lib
export NoCompilerStandardLib=false
make

%install
make install DESTDIR=$RPM_BUILD_ROOT

mkdir -p $RPM_BUILD_ROOT/%{_libdir}/pkgconfig
test "%{_libdir}" = "%{_prefix}/lib" || mv $RPM_BUILD_ROOT/%{_prefix}/lib/pkgconfig/* $RPM_BUILD_ROOT/%{_libdir}/pkgconfig

%files
%doc COPYING README
%{_prefix}/lib/mono/dbus-sharp-2.0
%{_prefix}/lib/mono/gac/dbus-sharp

%files devel
%{_libdir}/pkgconfig/dbus-sharp-2.0.pc

%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2:0.8.1-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2:0.8.1-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2:0.8.1-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2:0.8.1-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2:0.8.1-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2:0.8.1-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2:0.8.1-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2:0.8.1-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2:0.8.1-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2:0.8.1-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2:0.8.1-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2:0.8.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 31 2019 Tom Callaway <spot@fedoraproject.org> - 2:0.8.1-11
- rebuild for auto-provides/requires

* Mon Jul 29 2019 Timotheus Pokorra <timotheus.pokorra@solidcharity.com> - 2:0.8.1-10
- fix for building with xbuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2:0.8.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2:0.8.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2:0.8.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2:0.8.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2:0.8.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2:0.8.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Jul 19 2017 Tom Callaway <spot@fedoraproject.org> 2:0.8.1-3
- disable "fix array writing patch"
- enable signal trapping support

* Tue Jul 18 2017 Tom Callaway <spot@fedoraproject.org> 2:0.8.1-2
- revert to 0.8.1 codebase
- apply cleanups from https://bitbucket.org/hindlemail/dbus-sharp/commits/42e27a8aa85fad79e4c3abdf235dbab348c5448f?at=default

* Mon Feb 27 2017 Tom Callaway <spot@fedoraproject.org> 1:0.8.1-1
- update to 0.8.1

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.7.0-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Oct 13 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:0.7.0-16
- mono rebuild for aarch64 support

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.7.0-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:0.7.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon May 18 2015 Peter Robinson <pbrobinson@fedoraproject.org> 1:0.7.0-13
- Rebuild (mono4)

* Tue Mar 24 2015 Than Ngo <than@redhat.com> - 1:0.7.0-12
- use %%mono_arches

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:0.7.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:0.7.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat May 24 2014 Brent Baude <baude@us.ibm.com> - 1:0.7.0-9
- Change ppc64 to power64 macro

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:0.7.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:0.7.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:0.7.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sun Mar 11 2012 Christian Krause <chkr@fedoraproject.org> - 1:0.7.0-5
- Change paths for mono assemblies according to updated packaging
  guidelines (http://fedoraproject.org/wiki/Packaging:Mono)

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:0.7.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Oct 19 2011 Christian Krause <chkr@fedoraproject.org> - 1:0.7.0-3
- Fix path in pkgconfig file for x86_64

* Tue Oct 18 2011 Christian Krause <chkr@fedoraproject.org> - 1:0.7.0-2
- Minor spec file cleanup (remove unnecessary %%defattr)

* Mon Oct 17 2011 Christian Krause <chkr@fedoraproject.org> - 1:0.7.0-1
- Migrating to new uptream source
- Initial spec file changes by Denis Washington <denisw@online.de>

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.63-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Jan 11 2011 Dan Horák <dan[at]danny.cz> - 0.63-16
- updated the supported arch list

* Tue Oct 26 2010 Christian Krause <chkr@fedoraproject.org> - 0.63-15
- Rebuilt against Mono 2.8

* Mon Oct 26 2009 Dennis Gilmore <dennis@ausil.us> - 0.63-14
- ExcludeArch sparc64

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.63-13.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Jun 17 2009 Karsten Hopp <karsten@redhat.com> 0.63-12.1
- mono is now available on s390x

* Mon May 25 2009 Xavier Lamien <laxathom@fedoraproject.org> - 0.63-12
- build arch ppc64.

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.63-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Wed Jul 16 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 0.63-10
- fix license tag

* Mon Feb 18 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 0.63-9
- Autorebuild for GCC 4.3

* Tue Oct  2 2007 Matthias Clasen <mclasen@redhat.com> - 0.63-8
- Add alpha to ExlusiveArch

* Tue Oct  2 2007 Matthias Clasen <mclasen@redhat.com> - 0.63-7
- Fix license field
- Add pkgconfig dependency to the -devel package

* Wed Aug 30 2006 Alexander Larsson <alexl@redhat.com> - 0.63-6
- Fix connection and message gc problem (#187452)
- Patch from Christian Krause

* Fri Aug 18 2006 Alexander Larsson <alexl@redhat.com> - 0.63-5
- Update for new mono multilib setup
- Don't buildrequire old gtk-sharp

* Thu Jul 20 2006 John (J5) Palmieri <johnp@redhat.com> - 0.63-4
- Remove from the s390 builds

* Thu Jul 20 2006 Warren Togami <wtogami@redhat.com> - 0.63-3
- remove unnecessary obsolete

* Wed Jul 19 2006 John (J5) Palmieri <johnp@redhat.com> - 0.63-2
- Spec file cleanups

* Wed Jul 19 2006 John (J5) Palmieri <johnp@redhat.com> - 0.63-1
- Initial dbus-glib package
