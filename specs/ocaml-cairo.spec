# OCaml packages not built on i686 since OCaml 5 / Fedora 39.
ExcludeArch: %{ix86}

# Important note!
# There are at least two quite separate OCaml cairo projects.
#
# This is (packaged in Fedora >= 23):
#   http://forge.ocamlcore.org/projects/cairo/
#   https://github.com/Chris00/ocaml-cairo
#
# The other one (which used to be packaged in Fedora <= 22) is:
#   http://cairographics.org/cairo-ocaml/

Name:           ocaml-cairo
Epoch:          2
Version:        0.6.5
Release:        1%{?dist}
Summary:        OCaml library for accessing cairo graphics

License:        LGPL-3.0-or-later WITH OCaml-LGPL-linking-exception
URL:            https://github.com/Chris00/%{name}
VCS:            git:%{url}.git

Source0:        %{url}/releases/download/%{version}/cairo2-%{version}.tbz
# Fix a segfault when a Cairo error occurs
# See https://github.com/Chris00/ocaml-cairo/issues/36
Patch0:         https://github.com/Chris00/ocaml-cairo/pull/37.patch

BuildRequires:  ocaml >= 4.03
BuildRequires:  ocaml-dune >= 2.7.0
BuildRequires:  ocaml-dune-configurator-devel >= 2.7.0
BuildRequires:  ocaml-lablgtk-devel
BuildRequires:  pkgconfig(cairo) >= 1.2.0
BuildRequires:  pkgconfig(freetype2)

%global _description %{expand:
Cairo is a multi-platform library providing anti-aliased vector-based
rendering for multiple target backends. Paths consist of line segments
and cubic splines and can be rendered at any width with various join
and cap styles. All colors may be specified with optional translucence
(opacity/alpha) and combined using the extended Porter/Duff
compositing algebra as found in the X Render Extension.

Cairo exports a stateful rendering API similar in spirit to the path
construction, text, and painting operators of PostScript, (with the
significant addition of translucence in the imaging model). When
complete, the API is intended to support the complete imaging model of
PDF 1.4.}

%description %_description

This package contains OCaml bindings for Cairo.


%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{epoch}:%{version}-%{release}
Requires:       cairo-devel%{?_isa}


%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.


%package        gtk
Summary:        OCaml library to render cairo on a gtk2 canvas
Requires:       %{name}%{?_isa} = %{epoch}:%{version}-%{release}


%description    gtk %_description

This package contains OCaml bindings for rendering cairo on a gtk2 canvas.


%package        gtk-devel
Summary:        Development files for %{name}-gtk
Requires:       %{name}-gtk%{?_isa} = %{epoch}:%{version}-%{release}
Requires:       %{name}-devel%{?_isa} = %{epoch}:%{version}-%{release}
Requires:       ocaml-lablgtk-devel%{?_isa}


%description    gtk-devel
The %{name}-gtk-devel package contains libraries and signature files for
developing applications that use %{name}-gtk.



%package        pango
Summary:        OCaml library to use pango with cairo
Requires:       %{name}%{?_isa} = %{epoch}:%{version}-%{release}


%description    pango %_description

This package contains OCaml bindings to use pango with cairo.


%package        pango-devel
Summary:        Development files for %{name}-pango
Requires:       %{name}-pango%{?_isa} = %{epoch}:%{version}-%{release}
Requires:       %{name}-devel%{?_isa} = %{epoch}:%{version}-%{release}
Requires:       ocaml-lablgtk-devel%{?_isa}
Requires:       pango-devel%{?_isa}


%description    pango-devel
The %{name}-pango-devel package contains libraries and signature files
for developing applications that use %{name}-pango.


%prep
%autosetup -n cairo2-%{version} -p1


%build
cairo_cflags="$(pkgconf --cflags cairo)"
cairo_libs="$(pkgconf --libs cairo)"
gtk_cflags="$(pkgconf --cflags gtk+-2.0)"
gtk_libs="$(pkgconf --libs gtk+-2.0)"
export CAIRO_CFLAGS="%{build_cflags} $cairo_cflags"
export CAIRO_LIBS="%{build_ldflags} $cairo_libs"
export GTK_CFLAGS="%{build_cflags} $gtk_cflags"
export GTK_LIBS="%{build_ldflags} $gtk_libs"
%dune_build


%install
%dune_install -s


%check
%dune_check


%files -f .ofiles-cairo2
%doc CHANGES.md README.md
%license GPL3.md LICENSE.md


%files devel -f .ofiles-cairo2-devel
# XXX The tutorial doesn't build.
%doc examples


%files gtk -f .ofiles-cairo2-gtk


%files gtk-devel -f .ofiles-cairo2-gtk-devel


%files pango -f .ofiles-cairo2-pango


%files pango-devel -f .ofiles-cairo2-pango-devel


%changelog
* Mon Dec 23 2024 Jerry James <loganjerry@gmail.com> - 2:0.6.5-1
- Version 0.6.5

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2:0.6.4-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jun 19 2024 Richard W.M. Jones <rjones@redhat.com> - 2:0.6.4-13
- OCaml 5.2.0 ppc64le fix

* Wed May 29 2024 Richard W.M. Jones <rjones@redhat.com> - 2:0.6.4-12
- OCaml 5.2.0 for Fedora 41

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2:0.6.4-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2:0.6.4-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Dec 18 2023 Richard W.M. Jones <rjones@redhat.com> - 2:0.6.4-9
- OCaml 5.1.1 + s390x code gen fix for Fedora 40

* Tue Dec 12 2023 Richard W.M. Jones <rjones@redhat.com> - 2:0.6.4-8
- OCaml 5.1.1 rebuild for Fedora 40

* Thu Oct 05 2023 Richard W.M. Jones <rjones@redhat.com> - 2:0.6.4-7
- OCaml 5.1 rebuild for Fedora 40

* Sat Sep 30 2023 Jerry James <loganjerry@gmail.com> - 2:0.6.4-6
- Add patch to fix segfault in Cairo error reporting

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2:0.6.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jul 11 2023 Richard W.M. Jones <rjones@redhat.com> - 2:0.6.4-5
- OCaml 5.0 rebuild for Fedora 39

* Mon Jul 10 2023 Jerry James <loganjerry@gmail.com> - 2:0.6.4-4
- OCaml 5.0.0 rebuild

* Tue Jan 24 2023 Richard W.M. Jones <rjones@redhat.com> - 2:0.6.4-3
- Rebuild OCaml packages for F38

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2:0.6.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Oct 12 2022 Jerry James <loganjerry@gmail.com> - 2:0.6.4-1
- New upstream version 0.6.4
- Convert License tag to SPDX
- Use new OCaml macros

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2:0.6.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jun 18 2022 Richard W.M. Jones <rjones@redhat.com> - 2:0.6.2-7
- OCaml 4.14.0 rebuild

* Fri Feb 04 2022 Richard W.M. Jones <rjones@redhat.com> - 2:0.6.2-6
- OCaml 4.13.1 rebuild to remove package notes

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2:0.6.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Jan 04 2022 Richard W.M. Jones <rjones@redhat.com> - 2:0.6.2-4
- Build and rebuild for new ocaml-lablgtk (RHBZ#2036636)

* Mon Oct 04 2021 Richard W.M. Jones <rjones@redhat.com> - 2:0.6.2-3
- OCaml 4.13.1 build

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2:0.6.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jun 22 2021 Jerry James <loganjerry@gmail.com> - 2:0.6.2-1
- New upstream version 0.6.2
- Drop all patches

* Mon Mar  1 15:16:08 GMT 2021 Richard W.M. Jones <rjones@redhat.com> - 2:0.6.1-11
- OCaml 4.12.0 build

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2:0.6.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Sep 01 2020 Richard W.M. Jones <rjones@redhat.com> - 2:0.6.1-9
- OCaml 4.11.1 rebuild

* Fri Aug 21 2020 Richard W.M. Jones <rjones@redhat.com> - 2:0.6.1-8
- OCaml 4.11.0 rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2:0.6.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon May 04 2020 Richard W.M. Jones <rjones@redhat.com> - 2:0.6.1-6
- OCaml 4.11.0+dev2-2020-04-22 rebuild

* Tue Apr 21 2020 Richard W.M. Jones <rjones@redhat.com> - 2:0.6.1-5
- OCaml 4.11.0 pre-release attempt 2

* Fri Apr 03 2020 Richard W.M. Jones <rjones@redhat.com> - 2:0.6.1-4
- Update all OCaml dependencies for RPM 4.16.

* Wed Feb 26 2020 Richard W.M. Jones <rjones@redhat.com> - 2:0.6.1-3
- OCaml 4.10.0 final.

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2:0.6.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jan 22 2020 Jerry James <loganjerry@gmail.com> - 2:0.6.1-1
- New upstream version 0.6.1
- Add -gtk and -pango subpackages corresponding to upstream's opam packages
- Add -gtk-devel and -pango-devel subpackages to manage dependencies
- Add %%check script
- Add -test patch until upstream weighs in on GC issues
- Add -fno-common patch to fix builds of consuming packages with GCC 10

* Sun Jan 19 2020 Richard W.M. Jones <rjones@redhat.com> - 2:0.4.7-0.28.gitbe5a298
- OCaml 4.10.0+beta1 rebuild.

* Thu Jan 09 2020 Richard W.M. Jones <rjones@redhat.com> - 2:0.4.7-0.27.gitbe5a298
- OCaml 4.09.0 for riscv64

* Fri Dec 06 2019 Richard W.M. Jones <rjones@redhat.com> - 2:0.4.7-0.26.gitbe5a298
- OCaml 4.09.0 (final) rebuild.

* Fri Aug 16 2019 Richard W.M. Jones <rjones@redhat.com> - 2:0.4.7-0.25.gitbe5a298
- OCaml 4.08.1 (final) rebuild.

* Thu Aug 01 2019 Richard W.M. Jones <rjones@redhat.com> - 2:0.4.7-0.24.gitbe5a298
- OCaml 4.08.1 (rc2) rebuild.

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2:0.4.7-0.23.gitbe5a298
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2:0.4.7-0.22.gitbe5a298
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2:0.4.7-0.21.gitbe5a298
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Jul 11 2018 Richard W.M. Jones <rjones@redhat.com> - 2:0.4.7-0.20.gitbe5a298
- OCaml 4.07.0 (final) rebuild.

* Wed Jun 20 2018 Richard W.M. Jones <rjones@redhat.com> - 2:0.4.7-0.19.gitbe5a298
- OCaml 4.07.0-rc1 rebuild.

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2:0.4.7-0.18.gitbe5a298
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Nov 17 2017 Richard W.M. Jones <rjones@redhat.com> - 2:0.4.7-0.17.gitbe5a298
- OCaml 4.06.0 rebuild.

* Tue Aug 08 2017 Richard W.M. Jones <rjones@redhat.com> - 2:0.4.7-0.16.gitbe5a298
- OCaml 4.05.0 rebuild.

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2:0.4.7-0.15.gitbe5a298
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2:0.4.7-0.14.gitbe5a298
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jun 26 2017 Richard W.M. Jones <rjones@redhat.com> - 2:0.4.7-0.13.gitbe5a298
- OCaml 4.04.2 rebuild.

* Fri May 12 2017 Richard W.M. Jones <rjones@redhat.com> - 2:0.4.7-0.12.gitbe5a298
- OCaml 4.04.1 rebuild.

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2:0.4.7-0.11.gitbe5a298
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sat Nov 05 2016 Richard W.M. Jones <rjones@redhat.com> - 2:0.4.7-0.10
- Move to latest git commit upstream.

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2:0.4.7-0.9.git675e51b
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Jul 28 2015 Richard W.M. Jones <rjones@redhat.com> - 2:0.4.7-0.8.git675e51b
- OCaml 4.02.3 rebuild.

* Wed Jul 22 2015 Richard W.M. Jones <rjones@redhat.com> - 2:0.4.7-0.7.git675e51b
- Move to latest git commit upstream.
- Enable bytecode builds.

* Wed Jun 24 2015 Richard W.M. Jones <rjones@redhat.com> - 2:0.4.7-0.6.git5c1df15
- ocaml-4.02.2 final rebuild.

* Wed Jun 17 2015 Richard W.M. Jones <rjones@redhat.com> - 2:0.4.7-0.5.git5c1df15
- ocaml-4.02.2 rebuild.

* Thu Mar 19 2015 Richard W.M. Jones <rjones@redhat.com> - 2:0.4.7-0.4.git5c1df15
- Switch bindings to https://github.com/Chris00/ocaml-cairo
- See: https://lists.fedoraproject.org/pipermail/devel/2015-March/209182.html

* Tue Feb 17 2015 Richard W.M. Jones <rjones@redhat.com> - 1:1.2.0-0.20.git872c9bc92e6
- ocaml-4.02.1 rebuild.

* Fri Oct 31 2014 Orion Poplawski <orion@cora.nwra.com> - 1:1.2.0-0.19.git872c9bc92e6
- Update to latest git

* Sat Aug 30 2014 Richard W.M. Jones <rjones@redhat.com> - 1:1.2.0-0.18.git08b40192975
- ocaml-4.02.0 final rebuild.

* Sat Aug 23 2014 Richard W.M. Jones <rjones@redhat.com> - 1:1.2.0-0.17.git08b40192975
- ocaml-4.02.0+rc1 rebuild.

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:1.2.0-0.16.git08b40192975
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Aug 02 2014 Richard W.M. Jones <rjones@redhat.com> - 1:1.2.0-0.15.git08b40192975
- ocaml-4.02.0-0.8.git10e45753.fc22 rebuild.

* Wed Jul 23 2014 Richard W.M. Jones <rjones@redhat.com> - 1:1.2.0-0.14.git08b40192975
- OCaml 4.02.0 beta rebuild.

* Mon Jul 14 2014 Orion Poplawski <orion@cora.nwra.com> - 1:1.2.0-0.13.git08b40192975
- Rebuild for OCaml 4.02

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:1.2.0-0.12.git08b40192975
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Sep 14 2013 Richard W.M. Jones <rjones@redhat.com> - 1:1.2.0-0.11.git08b40192975
- Rebuild for OCaml 4.01.0.
- Enable debuginfo.
- Modernize the spec file.

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:1.2.0-0.10.git08b40192975
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:1.2.0-0.9.git08b40192975
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Oct 17 2012 Orion Poplawski <orion@cora.nwra.com> - 1:1.2.0-0.8.git08b40192975
- Rebuild for OCaml 4.00.1.

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:1.2.0-0.7.git08b40192975
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jun 8 2012 Orion Poplawski <orion@cora.nwra.com> - 1:1.2.0-0.6.git08b40192975
- Rebuild for OCaml 4.00.0.

* Fri Jan  6 2012 Richard W.M. Jones <rjones@redhat.com> - 1:1.2.0-0.5.git08b40192975
- Update to git commit 08b40192975 (dated 2011-09-11).
- Rebuild for OCaml 3.12.1.

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:1.2.0-0.4.gita5c5ee9f
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Jan 5 2011 Orion Poplawski <orion@cora.nwra.com> - 1:1.2.0-0.3.gita5c5ee9f
- Rebuild for OCaml 3.12

* Wed Dec 30 2009 Richard W.M. Jones <rjones@redhat.com> - 1:1.2.0-0.2.gita5c5ee9f
- Rebuild for OCaml 3.11.2.

* Mon Dec  7 2009 Richard W.M. Jones <rjones@redhat.com> - 1:1.2.0-0.1.gita5c5ee9f
- So we are wrong, version numbers did NOT roll backwards.
- Revert to current git head (a5c5ee9f) which is a pre-release of 1.2.0
  (RHBZ#541542).
- Replace %%define with %%global.
- Patch0 is now upstream.
- Checked package with rpmlint - no problems.

* Thu Nov 26 2009 Richard W.M. Jones <rjones@redhat.com> - 1:1.0.0-2
- ocaml-cairo-devel requires ocaml-lablgtk-devel (RHBZ#541427).

* Thu Oct  8 2009 Richard W.M. Jones <rjones@redhat.com> - 1:1.0.0-1
- New upstream version 1.0.0.
- Yes, version number really did roll backwards, so now we're using Epoch.
- Patch for compatibility with OCaml 3.11.1 (renamed bigarray structs).

* Tue Sep 29 2009 Richard W.M. Jones <rjones@redhat.com> - 1.2.0.cvs20080301-11
- Force rebuild against newer lablgtk.

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.0.cvs20080301-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Sat May 23 2009 Richard W.M. Jones <rjones@redhat.com> - 1.2.0.cvs20080301-9
- Rebuild for OCaml 3.11.1

* Thu Apr 16 2009 S390x secondary arch maintainer <fedora-s390x@lists.fedoraproject.org>
- ExcludeArch sparc64, s390, s390x as we don't have OCaml on those archs
  (added sparc64 per request from the sparc maintainer)

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.0.cvs20080301-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sat Feb  7 2009 Richard W.M. Jones <rjones@redhat.com> - 1.2.0.cvs20080301-7
- Rebuild against updated lablgtk.

* Tue Dec  9 2008 Richard W.M. Jones <rjones@redhat.com> - 1.2.0.cvs20080301-6
- Include cairo.a and cairo_lablgtk.a (fixes BZ 475349).

* Thu Dec  4 2008 Richard W.M. Jones <rjones@redhat.com> - 1.2.0.cvs20080301-5
- Rebuild.

* Wed Nov 19 2008 Richard W.M. Jones <rjones@redhat.com> - 1.2.0.cvs20080301-4
- Rebuild for OCaml 3.11.0

* Wed Apr 23 2008 Richard W.M. Jones <rjones@redhat.com> - 1.2.0.cvs20080301-3
- Rebuild for OCaml 3.10.2

* Sat Mar  1 2008 Richard W.M. Jones <rjones@redhat.com> - 1.2.0.cvs20080301-2
- Upgrade to latest CVS.
- Include instructions on how check out versions from CVS.
- Build for ppc64.

* Fri Feb 29 2008 Richard W.M. Jones <rjones@redhat.com> - 1.2.0.cvs20080224-2
- Added BRs for automake and gtk2-devel.

* Sun Feb 24 2008 Richard W.M. Jones <rjones@redhat.com> - 1.2.0.cvs20080224-1
- Initial RPM release.
