%if 0%{?__isa_bits} == 64
%define target linux-64
%else
%define target linux
%endif

%define variants thr thr-ogl
%define beta b6

Summary: Parallel / Multiprocessor Ray Tracing System
Name: tachyon
Version: 0.99
Release: 0.31.%{beta}%{?dist}
URL: http://jedi.ks.uiuc.edu/~johns/raytracer/
Source0: http://jedi.ks.uiuc.edu/~johns/raytracer/files/%{version}%{beta}/%{name}-%{version}%{beta}.tar.gz
# taken from Debian package
Source1: %{name}.1
Patch0: %{name}-rpm.patch
Patch1: %{name}-shared.patch
License: BSD with advertising
BuildRequires: make
BuildRequires:  gcc
BuildRequires: libGL-devel
BuildRequires: libpng-devel
BuildRequires: libjpeg-devel
BuildRequires: latex2html
BuildRequires: %{_bindir}/dvips
BuildRequires: %{_bindir}/latex
BuildRequires: %{_bindir}/pdflatex

%description
A portable, high performance parallel ray tracing system with
multithreaded implementation.

%package libs
Summary: Parallel / Multiprocessor Ray Tracing System library

%description libs
A portable, high performance parallel ray tracing system with
multithreaded implementation.  Tachyon is built as a C callable
library, which can be used with the included demo programs or within
your own application.

This package contains the shared library.

%package gl
Summary: Parallel / Multiprocessor Ray Tracing System with OpenGL display
Provides: %{name} = %{version}-%{release}

%description gl
A portable, high performance parallel ray tracing system with
multithreaded implementation.

This package contains OpenGL-enabled build.

%package devel
Summary: Development files for tachyon
Requires: %{name}-libs = %{version}-%{release}

%description devel
This package contains development headers and libraries for developing
with tachyon.

%package docs
Summary: Documentation and example scenes for tachyon
Requires: %{name} = %{version}-%{release}

%description docs
This package contains documentation and example scenes for rendering
with tachyon.

%prep
%setup -q -n %{name}
%patch0 -p1 -b .r
%patch1 -p1 -b .shared
find . -name CVS | xargs rm -r
# executable sources
chmod 644 src/hash.{c,h}
chmod 644 src/pngfile.h
chmod 644 demosrc/spaceball.c
chmod 644 demosrc/trackball.{c,h}
chmod 644 scenes/imaps/*
# work around unsupported -m32 gcc option
%ifarch armv7hl aarch64
sed -i -e 's/-m32 //g' unix/Make-arch
sed -i -e 's/-m64 //g' unix/Make-arch
%endif

%build
pushd unix
for variant in %{variants} ; do
  make %{?_smp_mflags} OPTFLAGS="$RPM_OPT_FLAGS" %{target}-$variant
done
popd

pushd docs
make html pdf ps
popd

%install
mkdir -p $RPM_BUILD_ROOT{%{_bindir},%{_libdir},{%{_datadir},%{_includedir}}/tachyon,%{_mandir}/man1}
for variant in %{variants} ; do
  install -pm755 compile/%{target}-$variant/tachyon $RPM_BUILD_ROOT%{_bindir}/tachyon-$variant
done
rename -- -thr "" $RPM_BUILD_ROOT%{_bindir}/*
mkdir docs/html
cp -pr docs/tachyon/*.{css,html,png} docs/html
cp -pr scenes $RPM_BUILD_ROOT%{_datadir}/tachyon/
install -pm644 %{SOURCE1} $RPM_BUILD_ROOT%{_mandir}/man1/
echo ".so tachyon.1" > $RPM_BUILD_ROOT%{_mandir}/man1/tachyon-ogl.1
cp -a compile/%{target}-thr/libtachyon*.so $RPM_BUILD_ROOT%{_libdir}/
install -pm644 src/{hash,tachyon{,_dep},util}.h $RPM_BUILD_ROOT%{_includedir}/tachyon/


%files
%attr(755,root,root) %{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*

%files libs
%doc Copyright README
%{_libdir}/libtachyon-%{version}.so

%files gl
%attr(755,root,root) %{_bindir}/%{name}-ogl
%{_mandir}/man1/%{name}-ogl.1*

%files devel
%{_includedir}/tachyon
%{_libdir}/libtachyon.so

%files docs
%doc Changes docs/tachyon.pdf docs/tachyon.ps docs/html
%{_datadir}/tachyon

%changelog
* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.99-0.31.b6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.99-0.30.b6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.99-0.29.b6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.99-0.28.b6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.99-0.27.b6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.99-0.26.b6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.99-0.25.b6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.99-0.24.b6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.99-0.23.b6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.99-0.22.b6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.99-0.21.b6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.99-0.20.b6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.99-0.19.b6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.99-0.18.b6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.99-0.17.b6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.99-0.16.b6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.99-0.15.b6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Sep 15 2015 Marcin Juszkiewicz <mjuszkiewicz@redhat.com> - 0.99-0.14.b6
- Use __isa_bits macro instead of list of 64-bit architectures

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.99-0.13.b6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.99-0.12.b6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Fri Jun 13 2014 Peter Robinson <pbrobinson@fedoraproject.org> 0.99-0.11.b6
- Fix build on aarch64
- Adjust ppc64 macro
- Cleanup spec

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.99-0.10.b6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Aug 09 2013 Dominik Mierzejewski <rpm@greysector.net> 0.99-0.9.b6
- update to 0.99b6
- fix build on armv7hl

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.99-0.8.b2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.99-0.7.b2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Dec 21 2012 Adam Tkac <atkac redhat com> - 0.99-0.6.b2
- rebuild against new libjpeg

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.99-0.5.b2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jan 12 2012 Adam Jackson <ajax@redhat.com> 0.99-0.4.b2
- Fix invocation of rename(1) in %%install

* Tue Dec 06 2011 Adam Jackson <ajax@redhat.com> - 0.99-0.3.b2
- Rebuild for new libpng

* Sat Jul 23 2011 Dominik Mierzejewski <rpm@greysector.net> 0.99-0.2.b2
- install missing tachyon_dep.h header
- link shared library against libjpeg to avoid unresolved symbols

* Sun Apr 10 2011 Dominik 'Rathann' Mierzejewski <rpm@greysector.net> 0.99-0.1.b2
- updated to 0.99b2
- rebased patch
- updated BRs

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.98.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Feb 09 2010 Dominik 'Rathann' Mierzejewski <rpm@greysector.net> 0.98.9-1
- update to 0.98.9

* Sat Dec 26 2009 Dominik 'Rathann' Mierzejewski <rpm@greysector.net> 0.98.7-2
- drop LAM support
- add shared library (based on Debian patch)
- simplify some specfile constructs
- improve descriptions

* Sun Sep 20 2009 Dominik 'Rathann' Mierzejewski <rpm@greysector.net> 0.98.7-1
- update to 0.98.7 release
- simplify specfile ifdeffery and reduce patch size
- fix build with new environment-modules
- add manpage from Debian package

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.98.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Sat Feb 28 2009 Dominik 'Rathann' Mierzejewski <rpm@greysector.net> 0.98.1-1
- update to 0.98.1 release
- fix mixed-up summaries
- docs are now built separately

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.98-0.8.20070319
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Fri Sep 26 2008 Dominik 'Rathann' Mierzejewski <rpm@greysector.net> 0.98-0.7.20070319
- fix build with new lam package
- use generic BR for libGLU-devel
- move tree cleanup to %%prep to fix short-circuit builds

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 0.98-0.6.20070319
- Autorebuild for GCC 4.3

* Thu Dec 13 2007 Dominik 'Rathann' Mierzejewski <rpm@greysector.net> 0.98-0.5
- more seamless variant handling
- use proper lam cflags and ldflags (as reported by pkgconfig)

* Tue Dec 04 2007 Dominik 'Rathann' Mierzejewski <rpm@greysector.net> 0.98-0.4
- add support for Alpha

* Wed Aug 29 2007 Dominik 'Rathann' Mierzejewski <rpm@greysector.net> 0.98-0.3
- rebuild
- update license tag

* Sat Jul 14 2007 Dominik 'Rathann' Mierzejewski <rpm@greysector.net> 0.98-0.2
- add support for ppc64 and sparc64, simplify target setting

* Sat Jul 07 2007 Dominik 'Rathann' Mierzejewski <rpm@greysector.net> 0.98-0.1
- update to 0.98 pre-release

* Sun Dec 17 2006 Dominik 'Rathann' Mierzejewski <rpm@greysector.net> 0.97-4
- fix copy&paste error in patch

* Sun Dec 17 2006 Dominik 'Rathann' Mierzejewski <rpm@greysector.net> 0.97-3
- add SPARC support

* Wed Nov 29 2006 Dominik 'Rathann' Mierzejewski <rpm@greysector.net> 0.97-2
- use only kosher CFLAGS
- fix target setting

* Tue Nov 28 2006 Dominik 'Rathann' Mierzejewski <rpm@greysector.net> 0.97-1
- initial build
- patch to add necessary build targets
