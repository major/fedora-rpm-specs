# OCaml packages not built on i686 since OCaml 5 / Fedora 39.
ExcludeArch: %{ix86}

Name:           ocaml-lablgl
Epoch:          1
Version:        1.07
Release:        15%{?dist}
Summary:        LablGL is an OpenGL interface for Objective Caml
License:        BSD-3-Clause

URL:            https://github.com/garrigue/lablgl
VCS:            git:%{url}.git
Source0:        %{url}/archive/v%{version}/lablgl-%{version}.tar.gz

# Adapt to OCaml 5
Patch0:         %{name}-ocaml5.patch
# Fix a use-after-free bug
# https://github.com/garrigue/lablgl/pull/5
Patch1:         %{name}-use-after-free.patch
# Fix a build error with the Modern C initiative
# https://github.com/garrigue/lablgl/pull/6
Patch2:         %{name}-mismatched-types.patch

BuildRequires:  make
BuildRequires:  freeglut-devel 
BuildRequires:  ocaml >= 4.14
BuildRequires:  ocaml-findlib >= 1.2.1
BuildRequires:  ocaml-camlp-streams-devel
BuildRequires:  ocaml-compiler-libs
BuildRequires:  ocaml-labltk-devel
BuildRequires:  ocaml-rpm-macros
BuildRequires:  tcl-devel
BuildRequires:  tk-devel
BuildRequires:  libX11-devel
BuildRequires:  libXext-devel
BuildRequires:  libXmu-devel
BuildRequires:  mesa-libGL-devel
BuildRequires:  mesa-libGLU-devel


%description
LablGL is is an Objective Caml interface to OpenGL. Support is
included for use inside LablTk, and LablGTK also includes specific
support for LablGL.  It can be used either with proprietary OpenGL
implementations (SGI, Digital Unix, Solaris...), with XFree86 GLX
extension, or with open-source Mesa.


%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{epoch}:%{version}-%{release}
Requires:       ocaml-labltk-devel%{?_isa}
Requires:       freeglut-devel%{?_isa}


%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.


%prep
%autosetup -n lablgl-%{version} -p1

cat > Makefile.config <<EOF
BINDIR = %{_bindir}
XINCLUDES = -I%{_prefix}/X11R6/include
XLIBS = -lXext -lXmu -lX11
TKINCLUDES = -I%{_includedir}
TKLIBS = $(pkg-config --libs tk)
GLINCLUDES =
GLLIBS = -lGL -lGLU
GLUTLIBS = -lglut
RANLIB = :
LIBDIR = %{_libdir}/ocaml
DLLDIR = %{_libdir}/ocaml/stublibs
INSTALLDIR = %{_libdir}/ocaml/lablGL
TOGLDIR=Togl
COPTS = %{build_cflags}
EOF

# Prepare the examples for inclusion in the docs
mkdir -p examples/LablGlut examples/Togl
cp -a LablGlut/examples examples/LablGlut
cp -a Togl/examples examples/Togl

# Fix the version number in META
sed -i.orig 's/1\.05/%{version}/' META
touch -r META.orig META

# Build with debuginfo
sed -i 's/\$(CAMLC)/& -g/;s/\$(CAMLOPT)/& -g/;s/ocamlmklib/& -g/' Makefile.common
sed -i 's/ocamlmktop/& -g/' LablGlut/src/Makefile Togl/src/Makefile


%build
# Parallel builds don't work.
unset MAKEFLAGS
make all \
%ifarch %{ocaml_native_compiler}
opt
%endif


%install
mkdir -p $RPM_BUILD_ROOT%{_bindir}
mkdir -p $RPM_BUILD_ROOT%{_libdir}/ocaml/lablGL
mkdir -p $RPM_BUILD_ROOT%{_libdir}/ocaml/stublibs
make INSTALLDIR=$RPM_BUILD_ROOT%{_libdir}/ocaml/lablGL \
    DLLDIR=$RPM_BUILD_ROOT%{_libdir}/ocaml/stublibs \
    BINDIR=$RPM_BUILD_ROOT%{_bindir} \
    install

# Install package META.
cp -p META $RPM_BUILD_ROOT%{_libdir}/ocaml/lablGL/

# Remove unnecessary *.ml files (ones which have a *.mli).
pushd $RPM_BUILD_ROOT%{_libdir}/ocaml/lablGL
for f in *.ml; do \
  b=`basename $f .ml`; \
  if [ -f "$b.mli" ]; then \
    rm $f; \
  fi; \
done
popd

%ocaml_files


%files -f .ofiles
%doc README
%license COPYRIGHT


%files devel -f .ofiles-devel
%doc CHANGES README examples/LablGlut examples/Togl
%license COPYRIGHT


%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.07-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jan  9 2025 Jerry James <loganjerry@gmail.com> - 1:1.07-14
- OCaml 5.3.0 rebuild for Fedora 42
- Add VCS field

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.07-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jun 19 2024 Richard W.M. Jones <rjones@redhat.com> - 1:1.07-12
- OCaml 5.2.0 ppc64le fix

* Wed May 29 2024 Richard W.M. Jones <rjones@redhat.com> - 1:1.07-11
- OCaml 5.2.0 for Fedora 41

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.07-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.07-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Dec 18 2023 Richard W.M. Jones <rjones@redhat.com> - 1:1.07-8
- Bump release and rebuild

* Mon Dec 18 2023 Richard W.M. Jones <rjones@redhat.com> - 1:1.07-7
- OCaml 5.1.1 + s390x code gen fix for Fedora 40

* Tue Dec 12 2023 Richard W.M. Jones <rjones@redhat.com> - 1:1.07-6
- OCaml 5.1.1 rebuild for Fedora 40

* Fri Dec  1 2023 Jerry James <loganjerry@gmail.com> - 1:1.07-5
- Fix a build error with the Modern C initiative

* Thu Oct 05 2023 Richard W.M. Jones <rjones@redhat.com> - 1:1.07-4
- OCaml 5.1 rebuild for Fedora 40

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.07-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Jul 12 2023 Richard W.M. Jones <rjones@redhat.com> - 1:1.07-2
- OCaml 5.0 rebuild for Fedora 39

* Mon Jul 10 2023 Jerry James <loganjerry@gmail.com> - 1:1.07-1
- Version 1.07
- Convert License tag to SPDX
- Drop unnecessary freeglut patch
- New project URL
- Add dependencies on ocaml-findlib and ocaml-camlp-streams
- Add patch to update Tk code for OCaml 5
- Add patch to fix use-after-free in the Tk code

* Tue Jan 24 2023 Richard W.M. Jones <rjones@redhat.com> - 1:1.06-28
- Rebuild OCaml packages for F38

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.06-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.06-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jun 18 2022 Richard W.M. Jones <rjones@redhat.com> - 1:1.06-25
- OCaml 4.14.0 rebuild

* Fri Feb 04 2022 Richard W.M. Jones <rjones@redhat.com> - 1:1.06-24
- OCaml 4.13.1 rebuild to remove package notes

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.06-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Mon Oct 04 2021 Richard W.M. Jones <rjones@redhat.com> - 1:1.06-22
- OCaml 4.13.1 build

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.06-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon Jul 19 2021 Jerry James <loganjerry@gmail.com> - 1:1.06-20
- Move META file to main package

* Mon Mar  1 2021 Richard W.M. Jones <rjones@redhat.com> - 1:1.06-20
- Rebuild for updated ocaml-labltk

* Mon Mar  1 09:37:07 GMT 2021 Richard W.M. Jones <rjones@redhat.com> - 1:1.06-19
- OCaml 4.12.0 build

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.06-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Sep 01 2020 Richard W.M. Jones <rjones@redhat.com> - 1:1.06-17
- OCaml 4.11.1 rebuild

* Fri Aug 21 2020 Richard W.M. Jones <rjones@redhat.com> - 1:1.06-16
- OCaml 4.11.0 rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.06-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon May 04 2020 Richard W.M. Jones <rjones@redhat.com> - 1:1.06-14
- OCaml 4.11.0+dev2-2020-04-22 rebuild

* Tue Apr 21 2020 Richard W.M. Jones <rjones@redhat.com> - 1:1.06-13
- OCaml 4.11.0 pre-release attempt 2

* Fri Apr 17 2020 Richard W.M. Jones <rjones@redhat.com> - 1:1.06-12
- OCaml 4.11.0 pre-release

* Thu Apr 02 2020 Richard W.M. Jones <rjones@redhat.com> - 1:1.06-11
- Update all OCaml dependencies for RPM 4.16.

* Wed Feb 26 2020 Richard W.M. Jones <rjones@redhat.com> - 1:1.06-10
- OCaml 4.10.0 final.

* Tue Feb 25 2020 Richard W.M. Jones <rjones@redhat.com> - 1:1.06-9
- Remove self META file (RHBZ#1806040).

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.06-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Jan 19 2020 Richard W.M. Jones <rjones@redhat.com> - 1:1.06-7
- OCaml 4.10.0+beta1 rebuild.

* Thu Jan 09 2020 Richard W.M. Jones <rjones@redhat.com> - 1:1.06-6
- OCaml 4.09.0 for riscv64

* Fri Dec 06 2019 Richard W.M. Jones <rjones@redhat.com> - 1:1.06-5
- OCaml 4.09.0 (final) rebuild.

* Tue Sep 17 2019 Gwyn Ciesla <gwync@protonmail.com> - 1:1.06-3
- Rebuilt for new freeglut

* Fri Aug 16 2019 Richard W.M. Jones <rjones@redhat.com> - 1:1.06-2
- OCaml 4.08.1 (final) rebuild.

* Sat Aug 10 2019 Richard W.M. Jones <rjones@redhat.com> - 1:1.06-1
- New upstream version 1.06.
- This removes the camlp4 dependency (RHBZ#1736347).
- Fix for new source URL.

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.05-33
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.05-32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.05-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Jul 11 2018 Richard W.M. Jones <rjones@redhat.com> - 1:1.05-30
- OCaml 4.07.0 (final) rebuild.

* Tue Jun 19 2018 Richard W.M. Jones <rjones@redhat.com> - 1:1.05-29
- OCaml 4.07.0-rc1 rebuild.

* Fri Feb 09 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1:1.05-28
- Escape macros in %%changelog

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.05-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Nov 07 2017 Richard W.M. Jones <rjones@redhat.com> - 1:1.05-26
- OCaml 4.06.0 rebuild.

* Mon Aug 07 2017 Richard W.M. Jones <rjones@redhat.com> - 1:1.05-25
- OCaml 4.05.0 rebuild.

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.05-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.05-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jun 26 2017 Richard W.M. Jones <rjones@redhat.com> - 1:1.05-22
- OCaml 4.04.2 rebuild.

* Thu May 11 2017 Richard W.M. Jones <rjones@redhat.com> - 1:1.05-21
- OCaml 4.04.1 rebuild.

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.05-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Nov 04 2016 Richard W.M. Jones <rjones@redhat.com> - 1:1.05-19
- Rebuild for OCaml 4.04.0.

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.05-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Jul 28 2015 Richard W.M. Jones <rjones@redhat.com> - 1:1.05-17
- OCaml 4.02.3 rebuild.

* Wed Jul 22 2015 Richard W.M. Jones <rjones@redhat.com> - 1:1.05-16
- Fix bytecode builds (patch supplied by Rafael Fonseca).

* Wed Jun 24 2015 Richard W.M. Jones <rjones@redhat.com> - 1:1.05-15
- ocaml-4.02.2 final rebuild.

* Wed Jun 17 2015 Richard W.M. Jones <rjones@redhat.com> - 1:1.05-14
- ocaml-4.02.2 rebuild.

* Mon Feb 16 2015 Richard W.M. Jones <rjones@redhat.com> - 1:1.05-13
- Bump release and rebuild.

* Mon Feb 16 2015 Richard W.M. Jones <rjones@redhat.com> - 1:1.05-12
- ocaml-4.02.1 rebuild.

* Sat Aug 30 2014 Richard W.M. Jones <rjones@redhat.com> - 1:1.05-11
- Bump release and rebuild.

* Sat Aug 30 2014 Richard W.M. Jones <rjones@redhat.com> - 1:1.05-10
- ocaml-4.02.0 final rebuild.

* Fri Aug 22 2014 Richard W.M. Jones <rjones@redhat.com> - 1:1.05-9
- Bump release and rebuild.

* Fri Aug 22 2014 Richard W.M. Jones <rjones@redhat.com> - 1:1.05-8
- ocaml-4.02.0+rc1 rebuild.

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:1.05-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Fri Aug 01 2014 Richard W.M. Jones <rjones@redhat.com> - 1:1.05-6
- Bump release and rebuild.

* Fri Aug 01 2014 Richard W.M. Jones <rjones@redhat.com> - 1:1.05-5
- ocaml-4.02.0-0.8.git10e45753.fc22 rebuild.

* Tue Jul 22 2014 Richard W.M. Jones <rjones@redhat.com> - 1:1.05-4
- OCaml 4.02.0 beta rebuild.

* Thu Jun 19 2014 Richard W.M. Jones <rjones@redhat.com> - 1.05-3
- Make -devel subpackage depend on the epoch + base version.

* Wed Jun 18 2014 Richard W.M. Jones <rjones@redhat.com> - 1.05-1
- New upstream version 1.05.
- Requires Epoch because upstream version went from 20120306->1.05.
- Fixes FTBFS (RHBZ#1106619).
- Use ExclusiveArch and add a comment about how we could fix this.

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20120306-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Sep 14 2013 Richard W.M. Jones <rjones@redhat.com> - 20120306-7
- Rebuild for OCaml 4.01.0.
- Enable debuginfo.
- Modernize the spec file.

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20120306-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20120306-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Oct 17 2012 Orion Poplawski <orion@cora.nwra.com> - 20120306-4
- Rebuild for OCaml 4.00.1.

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20120306-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sun Jun 10 2012 Richard W.M. Jones <rjones@redhat.com> - 20120306-2
- Rebuild for OCaml 4.00.0.

* Fri Jun 8 2012 Orion Poplawski <orion@cora.nwra.com> - 20120306-1
- Update to version 20120306.
- Update URL.
- Build for OCaml 4.00.0.

* Sat Apr 28 2012 Richard W.M. Jones <rjones@redhat.com> - 1.04-7
- Bump and rebuild against new OCaml compiler in ARM.

* Fri Jan 06 2012 Richard W.M. Jones <rjones@redhat.com> - 1.04-6
- Rebuild for OCaml 3.12.1.

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.04-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Jan 05 2011 Richard W.M. Jones <rjones@redhat.com> - 1.04-4
- Rebuild for OCaml 3.12 (http://fedoraproject.org/wiki/Features/OCaml3.12).

* Wed Dec 30 2009 Richard W.M. Jones <rjones@redhat.com> - 1.04-3
- Rebuild for OCaml 3.11.2.

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.04-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Fri May 22 2009 Richard W.M. Jones <rjones@redhat.com> - 1.04-1
- Rebuild for OCaml 3.11.1.
- New upstream version 1.04.
- Patch for Tk 8.5 is now upstream.

* Thu Apr 16 2009 S390x secondary arch maintainer <fedora-s390x@lists.fedoraproject.org>
- ExcludeArch sparc64, s390, s390x as we don't have OCaml on those archs
  (added sparc64 per request from the sparc maintainer)

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.03-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Wed Nov 26 2008 Richard W.M. Jones <rjones@redhat.com> - 1.03-6
- Rebuild for OCaml 3.11.0+rc1.

* Wed Nov 19 2008 Richard W.M. Jones <rjones@redhat.com> - 1.03-5
- Rebuild for OCaml 3.11.0

* Wed May 14 2008 Richard W.M. Jones <rjones@redhat.com> - 1.03-4
- Remove BRs for camlp4, labltk.
- Remove old Provides.

* Wed Apr 23 2008 Richard W.M. Jones <rjones@redhat.com> - 1.03-3
- Rebuild for OCaml 3.10.2.

* Sat Mar  1 2008 Richard W.M. Jones <rjones@redhat.com> - 1.03-2
- Rebuild for ppc64.

* Tue Feb 12 2008 Richard W.M. Jones <rjones@redhat.com> - 1.03-1
- New upstream version 1.03.
- Fix for Tk 8.5.
- Rebuild for OCaml 3.10.1.

* Fri Sep  7 2007 Gerard Milmeister <gemi@bluewin.ch> - 1.02-15
- Rebuild

* Thu Aug 30 2007 Gerard Milmeister <gemi@bluewin.ch> - 1.02-13
- Rebuild

* Sat Jul  7 2007 Gerard Milmeister <gemi@bluewin.ch> - 1.02-12
- exclude arch ppc64

* Sat Jul  7 2007 Gerard Milmeister <gemi@bluewin.ch> - 1.02-11
- added buildreq ocaml-camlp4-devel

* Fri Jul  6 2007 Gerard Milmeister <gemi@bluewin.ch> - 1.02-10
- renamed package from lablgl to ocaml-lablgl

* Sat Dec  2 2006 Gerard Milmeister <gemi@bluewin.ch> - 1.02-9
- Rebuild for ocaml 3.09.3

* Mon Aug 28 2006 Gerard Milmeister <gemi@bluewin.ch> - 1.02-8
- Rebuild for FE6

* Wed May 10 2006 Gerard Milmeister <gemi@bluewin.ch> - 1.02-7
- rebuilt for ocaml 3.09.2

* Sun Feb 26 2006 Gerard Milmeister <gemi@bluewin.ch> - 1.02-4
- Rebuild for ocaml 3.09.1

* Sat Feb 25 2006 Gerard Milmeister <gemi@bluewin.ch> - 1.02-3
- Rebuild for Fedora Extras 5

* Tue Nov  1 2005 Gerard Milmeister <gemi@bluewin.ch> - 1.02-2
- build opt libraries

* Tue Nov  1 2005 Gerard Milmeister <gemi@bluewin.ch> - 1.02-1
- New Version 1.02

* Sun Sep 11 2005 Gerard Milmeister <gemi@bluewin.ch> - 1.01-7
- Rebuild with new ocaml

* Thu May 26 2005 Toshio Kuratomi <toshio-tiki-lounge.com> - 1.01-6
- Bump and rebuild with new ocaml.
  
* Sun May 22 2005 Jeremy Katz <katzj@redhat.com> - 1.01-5
- rebuild on all arches

* Fri Apr  8 2005 Michael Schwendt <mschwendt[AT]users.sf.net>
- rebuilt

* Fri Apr  1 2005 Gerard Milmeister <gemi@bluewin.ch> - 1.01-3
- Rebuild for ocaml 3.08.3

* Sat Feb 12 2005 Gerard Milmeister <gemi@bluewin.ch> - 0:1.01-2
- Removed %%{_smp_mflags} as it breaks the build

* Thu Aug 19 2004 Gerard Milmeister <gemi@bluewin.ch> - 0:1.01-0.fdr.1
- New Version 1.01

* Mon Dec  1 2003 Gerard Milmeister <gemi@bluewin.ch> - 0:1.00-0.fdr.4
- Patch to used GL/freeglut.h instead of GL/glut.h
- Add BuildRequires for labltk

* Fri Nov 28 2003 Gerard Milmeister <gemi@bluewin.ch> - 0:1.00-0.fdr.3
- Add BuildRequires for camlp4
