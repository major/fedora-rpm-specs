# OCaml packages not built on i686 since OCaml 5 / Fedora 39.
ExcludeArch: %{ix86}

# rpmlint "no-binary" error is not really an error - see:
# https://www.redhat.com/archives/fedora-packaging/2008-August/msg00017.html
# and ocaml-ocamlgraph spec file for a discussion of this issue.

# The major and minor releases contain a full tarball.  Patch releases, however,
# contain only the parts that have changed, typically just the sources
# directory.  Use this to set up everything appropriately.
%global minorver 2.3
%global patchrel 3

Name:		alt-ergo
Version:	%{minorver}.%{patchrel}
Release:	23%{?dist}
Summary:	Automated theorem prover including linear arithmetic

# The top-level license files apply to the non-free main distribution of
# alt-ergo.  The alt-ergo-free distribution, which we package, is distributed
# with the CeCILL-C license, as noted on the webiste and also in
# sources/tools/gui/main_gui.ml.
# The AB-Why3 plugin is LGPL-2.1-only WITH OCaml-LGPL-linking-exception
License:	CECILL-C AND LGPL-2.1-only WITH OCaml-LGPL-linking-exception
URL:		https://alt-ergo.ocamlpro.com/
# The patch releases contain only the sources directory.  The other files come
# from the minor releases.
Source0:	https://alt-ergo.ocamlpro.com/http/%{name}-free-%{minorver}.0/%{name}-free-%{minorver}.0.tar.gz
%if 0%{?patchrel} > 0
Source1:	https://alt-ergo.ocamlpro.com/http/%{name}-free-%{version}/%{name}-free-%{version}.tar.gz
%endif
# Created with gimp from official upstream icon
Source2:	%{name}-icons.tar.xz
Source3:	%{name}.desktop
Source4:	%{name}.metainfo.xml
# Do not use the deprecated Pervasives interface
Patch0:		%{name}-pervasives.patch
# Adapt to recent changes in psmt2-frontend
Patch1:		%{name}-psmt2-frontend.patch
# Temporarily use the menhir table backend instead of the code backend for the
# AB plugin.  Menhir is unable to infer types with the current code and layout.
# Check each new release to see if this is still necessary.
Patch2:         %{name}-menhir.patch
# Fedora does not need the forward compatibility seq and stdlib-shims packages
Patch3:         %{name}-forward-compat.patch
# Dune 3 eliminated the external-lib-deps command
Patch4:         %{name}-dune3.patch
# Avoid errors due to misplaced inline attributes
Patch5:         %{name}-inline-error.patch

BuildRequires:	desktop-file-utils
BuildRequires:	gtksourceview2-devel
BuildRequires:	libappstream-glib
BuildRequires:	make
BuildRequires:	ocaml >= 4.04.0
BuildRequires:	ocaml-dune
BuildRequires:	ocaml-lablgtk-devel
BuildRequires:	ocaml-menhir
BuildRequires:	ocaml-num-devel
BuildRequires:	ocaml-ocplib-simplex-devel >= 0.4
BuildRequires:	ocaml-psmt2-frontend-devel >= 0.2
BuildRequires:	ocaml-zarith-devel
BuildRequires:	ocaml-zip-devel

Requires:	ocaml-alt-ergo-parsers%{?_isa} = %{version}-%{release}

%global _desc %{expand:
Alt-Ergo is an automated theorem prover implemented in OCaml. It is
based on CC(X) - a congruence closure algorithm parameterized by an
equational theory X. This algorithm is reminiscent of the Shostak
algorithm. Currently CC(X) is instantiated by the theory of linear
arithmetics. Alt-Ergo also contains a home made SAT-solver and an
instantiation mechanism by which it fully supports quantifiers.}

%description %_desc

%package gui
Summary:	Graphical front end for Alt-Ergo
License:	CECILL-C
Requires:	%{name}%{?_isa} = %{version}-%{release}
Requires:	gtksourceview2
Requires:	hicolor-icon-theme

%description gui %_desc

This package contains a graphical front end for the Alt-Ergo theorem
prover.

%package -n ocaml-alt-ergo-parsers
Summary:	Parser library used by the Alt-Ergo SMT solver
License:	CECILL-C
Requires:	ocaml-alt-ergo-lib%{?_isa} = %{version}-%{release}

%description -n ocaml-alt-ergo-parsers %_desc

This package contains the parser library used by the Alt-Ergo SMT solver.

%package -n ocaml-alt-ergo-parsers-devel
Summary:	Development files for ocaml-alt-ergo-parsers
License:	CECILL-C
Requires:	ocaml-alt-ergo-parsers%{?_isa} = %{version}-%{release}
Requires:	ocaml-alt-ergo-lib-devel%{?_isa} = %{version}-%{release}
Requires:	ocaml-psmt2-frontend-devel%{?_isa}
Requires:	ocaml-zip-devel%{?_isa}

%description -n ocaml-alt-ergo-parsers-devel %_desc

This package contains development files needed to build applications
that use the Alt-Ergo parser library.

%package -n ocaml-alt-ergo-lib
Summary:	Automated theorem prover library
License:	CECILL-C

%description -n ocaml-alt-ergo-lib %_desc

This package is the core of Alt-Ergo as an OCaml library.

%package -n ocaml-alt-ergo-lib-devel
Summary:	Development files for ocaml-alt-ergo-lib
License:	CECILL-C
Requires:	ocaml-alt-ergo-lib%{?_isa} = %{version}-%{release}
Requires:	ocaml-num-devel%{?_isa}
Requires:	ocaml-ocplib-simplex-devel%{?_isa}
Requires:	ocaml-zarith-devel%{?_isa}

%description -n ocaml-alt-ergo-lib-devel %_desc

This package contains development files needed to build applications
that use the Alt-Ergo library.

%prep
%autosetup -n %{name}-%{minorver}.0-free -N -a 2

%if 0%{?patchrel} > 0
# See above.  Replace the minor release sources with the patch release sources.
rm -rf sources
tar xf %{SOURCE1}
%endif

%autopatch -p1

%conf
cd sources
cp -p %{SOURCE3} com.ocamlpro.%{name}.desktop

# Unzip an example
cd examples/AB-Why3-plugin
unzip p4_34.why.zip
rm p4_34.why.zip
cd -

%ifnarch %{ocaml_native_compiler}
# Do not require native plugins
sed -i '/cmxs/d' plugins/{AB-Why3,fm-simplex}/dune
%endif

# This is not an autoconf-generated script.  Do NOT use %%configure.
./configure --prefix=%{_prefix} --libdir=%{ocamldir} --sharedir=%{ocamldir}

%build
cd sources
%make_build

%install
cd sources
%make_install

# We do not want the ml files
find %{buildroot}%{ocamldir} -name \*.ml -delete

# We install the documentation with the doc macro
rm -fr %{buildroot}%{_prefix}/doc

# Install the man page
mkdir -p %{buildroot}%{_mandir}/man1
cp -p doc/alt-ergo.1 %{buildroot}%{_mandir}/man1

# The install target in the Makefile puts these in the wrong place
mv %{buildroot}%{_datadir}/alt-ergo/{plugins,preludes} \
   %{buildroot}%{ocamldir}/alt-ergo
rmdir %{buildroot}%{_datadir}/alt-ergo

# Install the gtksourceview file
mkdir -p %{buildroot}%{_datadir}/gtksourceview-2.0/language-specs
cp -p doc/gtk-lang/alt-ergo.lang \
   %{buildroot}%{_datadir}/gtksourceview-2.0/language-specs

# Install the desktop file
mkdir -p %{buildroot}%{_datadir}/applications
desktop-file-install --dir %{buildroot}%{_datadir}/applications \
  com.ocamlpro.%{name}.desktop

# Install the AppData file
mkdir -p %{buildroot}%{_metainfodir}
install -pm 644 %{SOURCE4} \
  %{buildroot}%{_metainfodir}/com.ocamlpro.%{name}.metainfo.xml
appstream-util validate-relax --nonet \
  %{buildroot}%{_metainfodir}/com.ocamlpro.%{name}.metainfo.xml

# Install the icons
cd -
mkdir -p %{buildroot}%{_datadir}/icons
cp -a icons %{buildroot}%{_datadir}/icons/hicolor

%check
cd sources
%dune_check

%files
%doc README.md sources/CHANGES sources/examples publications/*.pdf
%{_bindir}/%{name}
%{_mandir}/man1/alt-ergo.1.*
%{ocamldir}/%{name}/
%{ocamldir}/%{name}-free/

%files gui
%{_bindir}/altgr-ergo
%{_datadir}/applications/com.ocamlpro.%{name}.desktop
%{_datadir}/gtksourceview-2.0/language-specs/%{name}.lang
%{_datadir}/icons/hicolor/*/apps/%{name}.png
%{ocamldir}/altgr-ergo/
%{_metainfodir}/com.ocamlpro.%{name}.metainfo.xml

%files -n ocaml-%{name}-parsers
%dir %{ocamldir}/%{name}-parsers/
%{ocamldir}/%{name}-parsers/META
%{ocamldir}/%{name}-parsers/*.cma
%{ocamldir}/%{name}-parsers/*.cmi
%ifarch %{ocaml_native_compiler}
%{ocamldir}/%{name}-parsers/*.cmxs
%endif
%{ocamldir}/%{name}-parsers-free/

%files -n ocaml-%{name}-parsers-devel
%{ocamldir}/%{name}-parsers/dune-package
%{ocamldir}/%{name}-parsers/opam
%ifarch %{ocaml_native_compiler}
%{ocamldir}/%{name}-parsers/*.a
%{ocamldir}/%{name}-parsers/*.cmx
%{ocamldir}/%{name}-parsers/*.cmxa
%endif
%{ocamldir}/%{name}-parsers/*.mli
%{ocamldir}/%{name}-parsers/*.cmt
%{ocamldir}/%{name}-parsers/*.cmti

%files -n ocaml-%{name}-lib
%dir %{ocamldir}/%{name}-lib/
%license LGPL-License.txt LICENSE.md License.OCamlPro
%{ocamldir}/%{name}-lib/META
%{ocamldir}/%{name}-lib/*.cma
%{ocamldir}/%{name}-lib/*.cmi
%ifarch %{ocaml_native_compiler}
%{ocamldir}/%{name}-lib/*.cmxs
%endif
%{ocamldir}/%{name}-lib-free/

%files -n ocaml-%{name}-lib-devel
%{ocamldir}/%{name}-lib/dune-package
%{ocamldir}/%{name}-lib/opam
%{ocamldir}/%{name}-lib/frontend/
%{ocamldir}/%{name}-lib/reasoners/
%{ocamldir}/%{name}-lib/structures/
%{ocamldir}/%{name}-lib/util/
%ifarch %{ocaml_native_compiler}
%{ocamldir}/%{name}-lib/*.a
%{ocamldir}/%{name}-lib/*.cmx
%{ocamldir}/%{name}-lib/*.cmxa
%endif
%{ocamldir}/%{name}-lib/*.cmt
%{ocamldir}/%{name}-lib/*.cmti

%changelog
* Thu Jan  9 2025 Jerry James <loganjerry@gmail.com> - 2.3.3-23
- OCaml 5.3.0 rebuild for Fedora 42
- Correct License fields from Apache-2.0 to CECILL-C
- Do configuration steps in %%conf

* Mon Aug  5 2024 Jerry James <loganjerry@gmail.com> - 2.3.3-22
- Rebuild for ocaml-menhir 20240715 and ocaml-zip 1.12

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.3-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Tue Jul 16 2024 Jerry James <loganjerry@gmail.com> - 2.3.3-20
- Rebuild for ocaml-zarith 1.14

* Wed Jun 19 2024 Richard W.M. Jones <rjones@redhat.com> - 2.3.3-19
- OCaml 5.2.0 ppc64le fix

* Wed May 29 2024 Richard W.M. Jones <rjones@redhat.com> - 2.3.3-18
- OCaml 5.2.0 for Fedora 41

* Thu May 23 2024 Jerry James <loganjerry@gmail.com> - 2.3.3-17
- Add patch to fix misplaced inline attributes

* Fri Feb  2 2024 Jerry James <loganjerry@gmail.com> - 2.3.3-17
- Rebuild for changed ocamlx(Dynlink) hash

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.3-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.3-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Tue Jan  2 2024 Jerry James <loganjerry@gmail.com> - 2.3.3-14
- Rebuild for ocaml-num and ocaml-menhir 20231231

* Mon Dec 18 2023 Richard W.M. Jones <rjones@redhat.com> - 2.3.3-13
- OCaml 5.1.1 + s390x code gen fix for Fedora 40

* Tue Dec 12 2023 Richard W.M. Jones <rjones@redhat.com> - 2.3.3-12
- OCaml 5.1.1 rebuild for Fedora 40

* Thu Oct 05 2023 Richard W.M. Jones <rjones@redhat.com> - 2.3.3-11
- OCaml 5.1 rebuild for Fedora 40

* Thu Jul 27 2023 Jerry James <loganjerry@gmail.com> - 2.3.3-10
- Rebuild for ocaml-zarith 1.13

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.3-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jul 18 2023 Jerry James <loganjerry@gmail.com> - 2.3.3-8
- Validate appdata with appstream-util

* Wed Jul 12 2023 Richard W.M. Jones <rjones@redhat.com> - 2.3.3-8
- OCaml 5.0 rebuild for Fedora 39

* Mon Jul 10 2023 Jerry James <loganjerry@gmail.com> - 2.3.3-7
- OCaml 5.0.0 rebuild

* Fri Mar 24 2023 Jerry James <loganjerry@gmail.com> - 2.3.3-6
- Dune 3.7.0 changed the install location of mli files

* Tue Jan 24 2023 Richard W.M. Jones <rjones@redhat.com> - 2.3.3-5
- Rebuild OCaml packages for F38

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Aug 11 2022 Jerry James <loganjerry@gmail.com> - 2.3.3-3
- Convert License tag to SPDX
- Note that the AB plugin has a different license

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue Jul  5 2022 Jerry James <loganjerry@gmail.com> - 2.3.3-2
- Patch out uses of the dune external-lib-deps command
- Patch out references to the seq forward compatibility module
- Use new OCaml macros

* Mon Jun 20 2022 Jerry James <loganjerry@gmail.com> - 2.3.3-1
- Version 2.3.3
- Add -menhir patch to fix FTBFS
- Add -stdlib-shims patch since Fedora does not need stdlib-shims

* Sun Jun 19 2022 Richard W.M. Jones <rjones@redhat.com> - 2.3.0-5
- OCaml 4.14.0 rebuild

* Mon Feb 28 2022 Jerry James <loganjerry@gmail.com> - 2.3.0-4
- Switch to the correct tarball
- Drop unneeded ocaml-findlib BR
- Add dependency on ocaml-alt-ergo-parsers from ocaml-alt-ergo-parsers-devel

* Fri Feb 04 2022 Richard W.M. Jones <rjones@redhat.com> - 2.3.0-3
- OCaml 4.13.1 rebuild to remove package notes

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Mon Dec 27 2021 Jerry James <loganjerry@gmail.com> - 2.3.0-1
- Version 2.3.0
- New ocaml-alt-ergo-lib and ocaml-alt-ergo-parsers subpackages

* Tue Oct 05 2021 Richard W.M. Jones <rjones@redhat.com> - 2.2.0-14
- OCaml 4.13.1 build

* Thu Jul 29 2021 Jerry James <loganjerry@gmail.com> - 2.2.0-13
- Rebuild for changed ocamlx(Dynlink)

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon Jul 19 2021 Jerry James <loganjerry@gmail.com> - 2.2.0-11
- Move META to the main package

* Tue Jun 22 2021 Jerry James <loganjerry@gmail.com> - 2.2.0-11
- Rebuild for ocaml-lablgtk without gnomeui

* Wed Mar  3 2021 Jerry James <loganjerry@gmail.com> - 2.2.0-10
- Rebuild for ocaml-zarith 1.12

* Tue Mar  2 11:26:14 GMT 2021 Richard W.M. Jones <rjones@redhat.com> - 2.2.0-9
- OCaml 4.12.0 build

* Thu Feb  4 2021 Jerry James <loganjerry@gmail.com> - 2.2.0-8
- Updates to the desktop and metainfo files
- Add -pervasives patch

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Nov 16 2020 Jerry James <loganjerry@gmail.com> - 2.2.0-6
- Rebuild for ocaml-zarith 1.11

* Fri Sep 25 2020 Jerry James <loganjerry@gmail.com> - 2.2.0-5
- Rebuild for ocaml-zarith 1.10

* Tue Sep 01 2020 Richard W.M. Jones <rjones@redhat.com> - 2.2.0-4
- OCaml 4.11.1 rebuild

* Fri Aug 21 2020 Richard W.M. Jones <rjones@redhat.com> - 2.2.0-3
- OCaml 4.11.0 rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jun 19 2020 Jerry James <loganjerry@gmail.com> - 2.2.0-1
- Version 2.2.0
- Drop upstreamed -newline patch

* Tue May 05 2020 Richard W.M. Jones <rjones@redhat.com> - 2.0.0-15
- OCaml 4.11.0+dev2-2020-04-22 rebuild

* Wed Apr 22 2020 Richard W.M. Jones <rjones@redhat.com> - 2.0.0-14
- OCaml 4.11.0 pre-release attempt 2

* Wed Apr  8 2020 Jerry James <loganjerry@gmail.com> - 2.0.0-13
- Filter out Requires for private interfaces we do not Provide

* Fri Apr 03 2020 Richard W.M. Jones <rjones@redhat.com> - 2.0.0-12
- Update all OCaml dependencies for RPM 4.16.

* Mon Mar 30 2020 Jerry James <loganjerry@gmail.com> - 2.0.0-11
- Rebuild for ocaml-zip 1.10

* Tue Mar 24 2020 Jerry James <loganjerry@gmail.com> - 2.0.0-10
- Rebuild for ocaml-menhir 20200211

* Wed Feb 26 2020 Richard W.M. Jones <rjones@redhat.com> - 2.0.0-9
- OCaml 4.10.0 final.

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Jan 19 2020 Richard W.M. Jones <rjones@redhat.com> - 2.0.0-7
- OCaml 4.10.0+beta1 rebuild.

* Fri Dec 06 2019 Richard W.M. Jones <rjones@redhat.com> - 2.0.0-6
- OCaml 4.09.0 (final) rebuild.

* Fri Sep  6 2019 Jerry James <loganjerry@gmail.com> - 2.0.0-5
- Rebuild for ocaml-zarith 1.9

* Fri Aug 16 2019 Richard W.M. Jones <rjones@redhat.com> - 2.0.0-4
- OCaml 4.08.1 (final) rebuild.

* Wed Jul 31 2019 Richard W.M. Jones <rjones@redhat.com> - 2.0.0-3
- OCaml 4.08.1 (rc2) rebuild.

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Jun  5 2019 Jerry James <loganjerry@gmail.com> - 2.0.0-1
- Update to version 2.0.0
- Add -newline patch to fix FTBFS
- Add a 256x256 icon

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.30-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.30-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Jul 11 2018 Richard W.M. Jones <rjones@redhat.com> - 1.30-14
- OCaml 4.07.0 (final) rebuild.

* Wed Jun 20 2018 Richard W.M. Jones <rjones@redhat.com> - 1.30-13
- OCaml 4.07.0-rc1 rebuild.

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.30-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sun Jan 07 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.30-11
- Remove obsolete scriptlets

* Wed Nov 08 2017 Richard W.M. Jones <rjones@redhat.com> - 1.30-10
- OCaml 4.06.0 rebuild.

* Mon Aug 07 2017 Richard W.M. Jones <rjones@redhat.com> - 1.30-9
- OCaml 4.05.0 rebuild.

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.30-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.30-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jun 26 2017 Richard W.M. Jones <rjones@redhat.com> - 1.30-6
- OCaml 4.04.2 rebuild.

* Fri May 12 2017 Richard W.M. Jones <rjones@redhat.com> - 1.30-5
- Bump release and rebuild.

* Fri May 12 2017 Richard W.M. Jones <rjones@redhat.com> - 1.30-4
- Bump release and rebuild.

* Fri May 12 2017 Richard W.M. Jones <rjones@redhat.com> - 1.30-3
- OCaml 4.04.1 rebuild.

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.30-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Nov 28 2016 Jerry James <loganjerry@gmail.com> - 1.30-1
- Update to version 1.30

* Mon Nov 07 2016 Richard W.M. Jones <rjones@redhat.com> - 1.01-3
- Rebuild for OCaml 4.04.0.

* Sat Apr 16 2016 Jerry James <loganjerry@gmail.com> - 1.01-2
- Rebuild for ocaml-ocamlgraph 1.8.7

* Wed Feb 17 2016 Jerry James <loganjerry@gmail.com> - 1.01-1
- Update to version 1.01

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.99.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Nov 25 2015 Jerry James <loganjerry@gmail.com> - 0.99.1-9
- Rebuild for zarith 1.4.1

* Tue Jul 28 2015 Richard W.M. Jones <rjones@redhat.com> - 0.99.1-8
- OCaml 4.02.3 rebuild.

* Wed Jun 24 2015 Richard W.M. Jones <rjones@redhat.com> - 0.99.1-7
- ocaml-4.02.2 final rebuild.

* Wed Jun 17 2015 Richard W.M. Jones <rjones@redhat.com> - 0.99.1-6
- ocaml-4.02.2 rebuild.

* Tue Jun 16 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.99.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Mar 18 2015 Jerry James <loganjerry@gmail.com> - 0.99.1-4
- Rebuild for ocaml-ocamlgraph 1.8.6

* Fri Mar 13 2015 Jerry James <loganjerry@gmail.com> - 0.99.1-3
- Fix FTBFS (bz 1099153)

* Wed Feb 18 2015 Richard W.M. Jones <rjones@redhat.com> - 0.99.1-2
- ocaml-4.02.1 rebuild.

* Tue Jan  6 2015 Jerry James <loganjerry@gmail.com> - 0.99.1-1
- Update to version 0.99.1

* Thu Oct 30 2014 Jerry James <loganjerry@gmail.com> - 0.95.2-14
- Rebuild for new ocaml-lablgtk

* Tue Oct 14 2014 Jerry James <loganjerry@gmail.com> - 0.95.2-13
- Rebuild for ocaml-zarith 1.3
- Fix license handling

* Tue Sep  2 2014 Jerry James <loganjerry@gmail.com> - 0.95.2-12
- ocaml-4.02.0 final rebuild.

* Sat Aug 23 2014 Richard W.M. Jones <rjones@redhat.com> - 0.95.2-11
- ocaml-4.02.0+rc1 rebuild.

* Fri Aug 15 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.95.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Aug 02 2014 Richard W.M. Jones <rjones@redhat.com> - 0.95.2-9
- ocaml-4.02.0-0.8.git10e45753.fc22 rebuild.

* Fri Jul 25 2014 Richard W.M. Jones <rjones@redhat.com> - 0.95.2-8
- Bump release and rebuild.

* Fri Jul 25 2014 Richard W.M. Jones <rjones@redhat.com> - 0.95.2-7
- Rebuild for OCaml 4.02.0 beta.

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.95.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon Apr 21 2014 Jerry James <loganjerry@gmail.com> - 0.95.2-5
- Rebuild for ocamlgraph 1.8.5

* Tue Apr 15 2014 Richard W.M. Jones <rjones@redhat.com> - 0.95.2-4
- Remove ocaml_arches macro (RHBZ#1087794).

* Mon Mar 24 2014 Jerry James <loganjerry@gmail.com> - 0.95.2-3
- Add desktop icons
- Drop unnecessary gmp-devel BR (pulled in by ocaml-zarith-devel)
- Fix bytecode build
- Drop screenshot, now hosted externally

* Tue Mar  4 2014 Jerry James <loganjerry@gmail.com> - 0.95.2-2
- Add an AppData file and screenshot
- Adapt to ocamlgraph 1.8.4

* Fri Sep 20 2013 Jerry James <loganjerry@gmail.com> - 0.95.2-1
- Update to version 0.95.2
- Web pages and downloads now hosted by ocamlpro.com
- Add ocaml-findlib, ocaml-zarith, and gmp-devel BRs
- Drop prelink BR; execstack is no longer set
- Fix bogus changelog dates

* Sat Sep 14 2013 Richard W.M. Jones <rjones@redhat.com> - 0.95.1-4
- Rebuild for OCaml 4.01.0.
- Enable debuginfo.
- Change some define -> global.
- Remove Group lines not needed by modern RPM.

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.95.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue May 14 2013 Jerry James <loganjerry@gmail.com> - 0.95.1-2
- Rebuild for ocaml-ocamlgraph 1.8.3
- Make the binaries full RELRO due to network use

* Tue Mar  5 2013 Jerry James <loganjerry@gmail.com> - 0.95.1-1
- Update to version 0.95.1
- Drop upstreamed -install patch

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.95-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Mon Jan 14 2013 Jerry James <loganjerry@gmail.com> - 0.95-1
- Update to version 0.95
- Add -install patch to fix installation failure

* Wed Oct 17 2012 Jerry James <loganjerry@gmail.com> - 0.94-7
- Rebuild for OCaml 4.00.1

* Mon Jul 30 2012 Jerry James <loganjerry@gmail.com> - 0.94-6
- Rebuild for ocaml-ocamlgraph 1.8.2

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.94-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Jun 12 2012 Jerry James <loganjerry@gmail.com> - 0.94-4
- Rebuild for OCaml 4.00.0

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.94-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sat Jan  7 2012 Jerry James <loganjerry@gmail.com> - 0.94-2
- Rebuild for OCaml 3.12.1

* Tue Dec  6 2011 Jerry James <loganjerry@gmail.com> - 0.94-1
- Add a desktop file for the gui.
- Update to version 0.94.  This means:
- The theory of records replaces the theory of pairs
- Bug fixes (intervals, term data-structure, stack-overflows, matching,
  existentials, distincts, CC, GUI)
- Improvements (SMT-Lib2 front-end, intervals, case-splits, triggers, lets)
- Multiset ordering for AC(X)
- Manual lemma instantiation in the GUI

* Mon Nov 14 2011 Jerry James <loganjerry@gmail.com> - 0.93-2
- Build on all arches with ocaml

* Thu May 12 2011 Jerry James <loganjerry@gmail.com> - 0.93-1
- Update to version 0.93.  This means:
- New command-line options -steps, -max-split, and -proof
- New polymorphic theory of arrays
- Built-in support for enumeration types
- Graphical front end
- New predicate distinct()
- New constructs: let x = <term> in <term>, let x = <term> in <formula>
- Partial support for the division operator
- Unspecified bug fixes

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.92.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Oct 06 2010 David A. Wheeler <dwheeler@dwheeler.com> 0.92.1-1
- Update to version 0.92.1. This means:
- New built-in syntax for the theory of arrays
- Fixes a bug in the arithmetic module
- Allows folding and unfolding of predicate definitions

* Tue Jun 08 2010 David A. Wheeler <dwheeler@dwheeler.com> 0.91-1
- Update to version 0.91. This means:
- partial support for non-linear arithmetics
- support case split on integer variables
- new support for Euclidean division and modulo operators


* Tue Aug 04 2009 Alan Dunn <amdunn@gmail.com> 0.9-2
- Added ExcludeArch sparc64 due to no OCaml

* Fri Jul 24 2009 Alan Dunn <amdunn@gmail.com> 0.9-1
- New upstream version
- Removed code for check for Fedora version (8) that is EOL
- Removed comments re: CeCILL-C license as it is ok to have (no
  rpmlint warnings to explain either).

* Wed Jun 17 2009 Karsten Hopp <karsten@redhat.com> 0.8-5.1
- ExcludeArch s390x as there's no ocaml available

* Mon Feb 23 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Wed Dec 24 2008 Alan Dunn <amdunn@gmail.com> 0.8-4
- Rebuild: Source upstream appears to have changed even with same version number
  (seems like bug fix from examination of changes)
- Changed hardcoded version number in source string
* Fri Sep 05 2008 Alan Dunn <amdunn@gmail.com> 0.8-3
- Fixed BuildRequires to add prelink (for execstack).
* Tue Aug 26 2008 Alan Dunn <amdunn@gmail.com> 0.8-2
- Fixed BuildRequires to add ocaml-ocamlgraph-devel instead of
  ocaml-ocamlgraph, made other minor changes.
* Mon Aug 25 2008 Alan Dunn <amdunn@gmail.com> 0.8-1
- Initial Fedora RPM version.
