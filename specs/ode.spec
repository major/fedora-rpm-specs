%global somajor 8

Name:           ode
Version:        0.16.6
Release:        1%{?dist}
Summary:        High performance library for simulating rigid body dynamics
License:        BSD-3-Clause AND LGPL-2.1-or-later
URL:            https://bitbucket.org/odedevs/ode
Source0:        https://bitbucket.org/odedevs/ode/downloads/ode-%{version}.tar.gz
Patch1:         ode-0.11.1-multilib.patch
# Modify ode-double.pc and ode-double-config to set dDOUBLE, link right lib
Patch2:         ode-0.16.6-double-config.patch
# Modify ode.pc and ode-config to set dSINGLE
Patch3:         ode-0.16.3-single-config.patch
BuildRequires:  make gcc-c++
BuildRequires:  libGL-devel libGLU-devel libtool

%description
ODE is an open source, high performance library for simulating rigid body
dynamics. It is fully featured, stable, mature and platform independent with
an easy to use C/C++ API. It has advanced joint types and integrated collision
detection with friction. ODE is useful for simulating vehicles, objects in
virtual reality environments and virtual creatures. It is currently used in
many computer games, 3D authoring tools and simulation tools.


%package        double
Summary:        Ode physics library compiled with double precision

%description    double
The %{name}-double package contains a version of the ODE library for simulating
rigid body dynamics compiled with double precision.


%package        devel
Summary:        Development files for %{name}
Requires:       %{name} = %{version}-%{release}
Requires:       %{name}-double = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name} or %{name}-double.


%prep
%setup -q
./bootstrap
%patch -P 1 -p1
# allow overriding EXTRA_LIBTOOL_LDFLAGS from the make cmdline
sed -i 's/libode_la_LDFLAGS = @EXTRA_LIBTOOL_LDFLAGS@/libode_la_LDFLAGS = $(EXTRA_LIBTOOL_LDFLAGS)/' \
  ode/src/Makefile.in
# mv some license files around to give them all a unique name
mv OPCODE/COPYING OPCODE-COPYING
for i in ou/LICENSE*.TXT; do
  sed -i.bak 's/\r//' $i
  touch -r $i.bak $i
  mv $i `echo $i|sed 's|ou/LICENSE|OU-LICENSE|'`
done
mv libccd/BSD-LICENSE LIBCCD-LICENSE.TXT


%build
# Use internal libccd as system libccd is not build with double support
ODE_CONFIGURE_FLAGS="--enable-shared --disable-static --with-libccd=internal \
  --with-cylinder-cylinder=libccd --with-capsule-cylinder=libcdd \
  --with-convex-box=libccd --with-convex-capsule=libccd \
  --with-convex-cylinder=libccd"
%configure $ODE_CONFIGURE_FLAGS --enable-double-precision
make %{?_smp_mflags} X_LIBS=-lX11 EXTRA_LIBTOOL_LDFLAGS="-release double"
mv ode-config ode-double-config
mv ode.pc ode-double.pc
# Adjust ode-double-config and ode-double.pc to set dDOUBLE, use proper lib
patch -p1 < %{PATCH2}
mv ode/src/.libs/libode-double.so.%{somajor}.?.? .
make distclean

CFLAGS="%{optflags} -ffast-math"
CXXFLAGS="%{optflags} -ffast-math"
%configure $ODE_CONFIGURE_FLAGS
make %{?_smp_mflags} X_LIBS=-lX11
# Modify ode-config and ode.pc to set dSINGLE
patch -p1 < %{PATCH3}


%install
make install DESTDIR=$RPM_BUILD_ROOT
rm $RPM_BUILD_ROOT%{_libdir}/libode.la
# DIY libode-double install
install -m 755 ode-double-config $RPM_BUILD_ROOT%{_bindir}
install -m 755 libode-double.so.%{somajor}.?.? $RPM_BUILD_ROOT%{_libdir}
ln -s libode-double.so.%{somajor}.?.? $RPM_BUILD_ROOT%{_libdir}/libode-double.so.%{somajor}
ln -s libode-double.so.%{somajor}.?.? $RPM_BUILD_ROOT%{_libdir}/libode-double.so
install -m 644 ode-double.pc $RPM_BUILD_ROOT%{_libdir}/pkgconfig


%ldconfig_scriptlets

%ldconfig_scriptlets double


%files
%doc CHANGELOG.txt README.md
%license *COPYING *LICENSE*.TXT
%{_libdir}/libode.so.%{somajor}*

%files double
%doc CHANGELOG.txt README.md
%license *COPYING *LICENSE*.TXT
%{_libdir}/libode-double.so.%{somajor}*

%files devel
%{_bindir}/%{name}-config
%{_bindir}/%{name}-double-config
%{_includedir}/%{name}
%{_libdir}/libode.so
%{_libdir}/libode-double.so
%{_libdir}/pkgconfig/%{name}.pc
%{_libdir}/pkgconfig/%{name}-double.pc


%changelog
* Fri Jan 17 2025 Gwyn Ciesla <gwync@protonmail.com> - 0.16.6-1
- 0.16.6

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.16.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Tue Mar 26 2024 Gwyn Ciesla <gwync@protonmail.com> - 0.16.5-1
- 0.16.5

* Fri Feb 02 2024 Gwyn Ciesla <gwync@protonmail.com> - 0.16.4-2
- SPDX license tags

* Thu Feb 01 2024 Gwyn Ciesla <gwync@protonmail.com> - 0.16.4-1
- 0.16.4

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.16.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.16.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.16.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Mon Mar 20 2023 Hans de Goede <hdegoede@redhat.com> - 0.16.3-1
- Update to 0.16.3 (rhbz#2155091)

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.16.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.16.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Apr 07 2022 Hedayat Vatankhah <hedayat.fwd+rpmchlog@gmail.com> - 0.16.2-1
- Update to 0.16.2 (rhbz#1438205)

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.14-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.14-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.14-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.14-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.14-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.14-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.14-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.14-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.14-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.14-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.14-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Feb 21 2017 Hans de Goede <hdegoede@redhat.com> - 0.14-4
- Fix FTBFS (rhbz#1424008)

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.14-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.14-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Dec 18 2015 Hans de Goede <hdegoede@redhat.com> - 0.14-1
- Update to 0.14 (rhbz#1292651)

* Wed Dec 16 2015 Hans de Goede <hdegoede@redhat.com> - 0.13.2-1
- Update to 0.13.2 (rhbz#1291676)

* Wed Sep  9 2015 Hans de Goede <hdegoede@redhat.com> - 0.13.1-4
- Enable libccd colliders for collision types for which ode has no builtin
  colission detection (rhbz#1260964)

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.13.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 0.13.1-2
- Rebuilt for GCC 5 C++11 ABI change

* Wed Oct 29 2014 Hans de Goede <hdegoede@redhat.com> - 0.13.1-1
- Fix URLs to point to new upstream (rhbz#1131050)
- Update to 0.13.1 (rhbz#1131050)

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.12-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.12-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.12-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon Mar 18 2013 Hans de Goede <hdegoede@redhat.com> - 0.12-3
- Fix ode-double soname not version tracking the ode soname (rhbz#922812)

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.12-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sun Aug 19 2012 Jon Ciesla <limburgher@gmail.com> - 0.12-1
- New upstream, BZ 845478.

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.11.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.11.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.11.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Nov  8 2010 Hans de Goede <hdegoede@redhat.com> 0.11.1-5
- Add a -double subpackage providing a version of ode compiled with
  double precision (#574034)

* Tue Feb 16 2010 Hans de Goede <hdegoede@redhat.com> 0.11.1-4
- Fix FTBFS (#564642)

* Thu Nov 12 2009 Hans de Goede <hdegoede@redhat.com> 0.11.1-3
- Fix multilib conflict in -devel sub package (#507981)

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.11.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon May 25 2009 Hans de Goede <hdegoede@redhat.com> 0.11.1-1
- New upstream release 0.11.1

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Fri Jan 30 2009 Hans de Goede <hdegoede@redhat.com> 0.11-1
- New upstream release 0.11

* Mon Sep 15 2008 Hans de Goede <j.w.r.degoede@hhs.nl> 0.10.1-1
- New upstream release 0.10.1 (bz 460033)

* Thu Apr  3 2008 Hans de Goede <j.w.r.degoede@hhs.nl> 0.9-4
- Force proper use of RPM_OPT_FLAGS during build

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 0.9-3
- Autorebuild for GCC 4.3

* Thu Oct 18 2007 Hans de Goede <j.w.r.degoede@hhs.nl> 0.9-2
- Drop workaround for stormbaancoureur crash, it is now fixed in
  stormbaancoureur

* Fri Oct 12 2007 Hans de Goede <j.w.r.degoede@hhs.nl> 0.9-1
- New upstream release 0.9 (final)

* Fri Sep 28 2007 Hans de Goede <j.w.r.degoede@hhs.nl> 0.9-0.1.rc1
- New upstream release 0.9-rc1

* Tue Sep 11 2007 Hans de Goede <j.w.r.degoede@hhs.nl> 0.8.1-0.1.rc1
- New upstream release 0.8.1-rc1

* Wed Aug 15 2007 Hans de Goede <j.w.r.degoede@hhs.nl> 0.8-2
- Update License tag for new Licensing Guidelines compliance

* Wed Feb 14 2007 Hans de Goede <j.w.r.degoede@hhs.nl> 0.8-1
- New upstream release 0.8

* Thu Oct 05 2006 Christian Iseli <Christian.Iseli@licr.org> 0.7-2
 - rebuilt for unwind info generation, broken in gcc-4.1.1-21

* Fri Sep 22 2006 Hans de Goede <j.w.r.degoede@hhs.nl> 0.7-1
- New upstream release 0.7

* Mon Aug 28 2006 Hans de Goede <j.w.r.degoede@hhs.nl> 0.6-3
- FE6 Rebuild

* Wed Jul  5 2006 Hans de Goede <j.w.r.degoede@hhs.nl> 0.6-2
- Change name from libode to ode
- Fix soname & /usr/lib64 usage
- Patch configure to accept our CFLAGS instead of always using its own
- Patch configure to never activate the generation of asm-code which is then
  used unconditionally, the build CPU may be very different from the CPU on
  which the package gets run.

* Sun Jun 18 2006 Hugo Cisneiros <hugo@devin.com.br> 0.6-1
- Initial RPM release
