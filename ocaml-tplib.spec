%undefine _package_note_flags
Name:           ocaml-tplib
Version:        1.3
Release:        72%{?dist}
Summary:        Tropical Polyhedra Library

License:        LGPL-2.1-or-later
URL:            https://gforge.inria.fr/projects/tplib
Source0:        https://gforge.inria.fr/frs/download.php/32084/tplib-%{version}.tar.gz
# Man pages written by Jerry James using text from the sources; i.e., I
# contributed only the formatting.  Thus, the license and copyright for these
# files is the same as for the sources.
Source1:        compute_ext_rays.1
Source2:        compute_ext_rays_polar.1
Source3:        compute_halfspaces.1
Source4:        compute_minimal_external_representations.1
Source5:        compute_tangent_hypergraph.1
Source6:        compute_tropical_complex.1
# Upstream patch to adapt to new ocamlbuild behavior.  See
# https://github.com/ocaml/opam-repository/blob/master/packages/tplib/tplib.1.3/files/fix-makefile.diff
Patch0:         %{name}-ocamlbuild.patch
# Adapt to current versions of mlgmpidl
Patch1:         %{name}-mlgmpidl.patch

BuildRequires:  make
BuildRequires:  mpfr-devel
BuildRequires:  ocaml
BuildRequires:  ocaml-ocamlbuild-devel
BuildRequires:  ocaml-camlidl-devel
BuildRequires:  ocaml-findlib-devel
BuildRequires:  ocaml-mlgmpidl-devel
BuildRequires:  ocaml-num-devel
BuildRequires:  ocaml-ocamldoc
BuildRequires:  ocaml-zarith-devel

# This is an internal symbol that winds up in Requires, but not Provides
%global __requires_exclude ocamlx?\\\(Numeric_plugin\\\)

# Don't advertise the numeric plugins or symbols that belong to other packages
%global __provides_exclude plugin|ocamlx?\\\(Bigarray|Gmp_random|Mpq|Mpz|Unix(Labels)?|Q|Z|Zarith_version\\\)

%description
TPLib computes a description by means of vertices and rays of tropical
polyhedra defined by means of inequalities, and conversely.

It also provides a numerical abstract domain based on tropical
polyhedra, in order to infer min-/max- invariants over programs.

%package devel
Summary:        Library files and headers for developing with TPLib
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       ocaml-findlib-devel%{?_isa}
Requires:       ocaml-num-devel%{?_isa}
Provides:       %{name}-static = %{version}-%{release}

%description devel
Library files and headers for developing applications that use TPLib.

%package tools
Summary:        Tools that use TPLib
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description tools
Tools that use TPLib.

%prep
%setup -q -n tplib-%{version}
%patch0
%patch1

# Enable debuginfo generation
sed -i 's/@OCAMLBUILD@/& -cflag -g -lflag -g/' Makefile.in

# Use the PIC version of libasmrun
sed -i 's/-lasmrun/&_pic/g' Makefile.in configure
sed -i 's/libasmrun\.a/libasmrun_pic.a/' Makefile.in

# Build the bindings with -fPIC
sed -i 's,CFLAGS += -I\$(OCAML_HOME_DIR),& -fPIC,' Makefile.in

%build
%configure
# Don't use %%{?_smp_mflags}; it leads to build failures
make

%install
export OCAMLFIND_DESTDIR=%{buildroot}%{_libdir}/ocaml
mkdir -p $OCAMLFIND_DESTDIR
mkdir -p %{buildroot}%{_includedir}
make install bindir=%{buildroot}%{_bindir} libdir=%{buildroot}%{_libdir} \
  includedir=%{buildroot}%{_includedir}

mkdir -p %{buildroot}%{_mandir}/man1
cp -p %{SOURCE1} %{SOURCE2} %{SOURCE3} %{SOURCE4} %{SOURCE5} %{SOURCE6} \
   %{buildroot}%{_mandir}/man1

%check
make test
_build/tests/test_tplib_double
_build/tests/test_tplib_rational

%files
%doc README
%license LICENSE
%{_libdir}/ocaml/tplib/
%exclude %{_libdir}/ocaml/tplib/*.a
%exclude %{_libdir}/ocaml/tplib/*.cmxa
%exclude %{_libdir}/ocaml/tplib/*.mli

%files devel
%{_includedir}/tplib_*.h
%{_libdir}/*.a
%{_libdir}/ocaml/tplib/*.a
%{_libdir}/ocaml/tplib/*.cmxa
%{_libdir}/ocaml/tplib/*.mli

%files tools
%{_bindir}/*
%doc %{_mandir}/man1/*

%changelog
* Wed Feb 15 2023 Jerry James <loganjerry@gmail.com> - 1.3-72
- Convert License tag to SPDX

* Tue Jan 24 2023 Richard W.M. Jones <rjones@redhat.com> - 1.3-72
- Rebuild OCaml packages for F38

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-71
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-70
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jun 18 2022 Richard W.M. Jones <rjones@redhat.com> - 1.3-69
- OCaml 4.14.0 rebuild

* Fri Feb 04 2022 Richard W.M. Jones <rjones@redhat.com> - 1.3-68
- OCaml 4.13.1 rebuild to remove package notes

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-67
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Mon Dec 27 2021 Jerry James <loganjerry@gmail.com> - 1.3-66
- Rebuild for ocaml-mlgmpidl 1.2.14

* Mon Oct 04 2021 Richard W.M. Jones <rjones@redhat.com> - 1.3-65
- OCaml 4.13.1 build

* Thu Jul 29 2021 Jerry James <loganjerry@gmail.com> - 1.3-64
- Filter ocaml, mlgmpidl, and zarith symbols out of Provides

* Thu Jul 29 2021 Jerry James <loganjerry@gmail.com> - 1.3-63
- Rebuild for changed ocamlx(Dynlink)

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-62
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon Mar 15 2021 Richard W.M. Jones <rjones@redhat.com> - 1.3-61
- Bump and rebuild for updated ocaml-findlib.

* Wed Mar  3 2021 Jerry James <loganjerry@gmail.com> - 1.3-60
- Rebuild for ocaml-zarith 1.12

* Mon Mar  1 17:06:22 GMT 2021 Richard W.M. Jones <rjones@redhat.com> - 1.3-59
- OCaml 4.12.0 build

* Wed Feb 17 2021 Jerry James <loganjerry@gmail.com> - 1.3-58
- Bump and rebuild for updated ocaml Dynlink dependency

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-57
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Nov 23 2020 Jerry James <loganjerry@gmail.com> - 1.3-56
- Rebuild for ocaml-zarith 1.11

* Fri Sep 25 2020 Jerry James <loganjerry@gmail.com> - 1.3-55
- Rebuild for ocaml-zarith 1.10

* Tue Sep 01 2020 Richard W.M. Jones <rjones@redhat.com> - 1.3-54
- OCaml 4.11.1 rebuild

* Fri Aug 21 2020 Richard W.M. Jones <rjones@redhat.com> - 1.3-53
- OCaml 4.11.0 rebuild

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-52
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-51
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon May 04 2020 Richard W.M. Jones <rjones@redhat.com> - 1.3-50
- OCaml 4.11.0+dev2-2020-04-22 rebuild

* Tue Apr 21 2020 Richard W.M. Jones <rjones@redhat.com> - 1.3-49
- OCaml 4.11.0 pre-release attempt 2

* Fri Apr 17 2020 Richard W.M. Jones <rjones@redhat.com> - 1.3-48
- OCaml 4.11.0 pre-release

* Mon Apr 13 2020 Jerry James <loganjerry@gmail.com> - 1.3-47
- Exclude ocamlx(Numeric_plugin) from Requires

* Thu Apr 02 2020 Richard W.M. Jones <rjones@redhat.com> - 1.3-46
- Update all OCaml dependencies for RPM 4.16.

* Wed Feb 26 2020 Richard W.M. Jones <rjones@redhat.com> - 1.3-45
- OCaml 4.10.0 final.

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-44
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Jan 19 2020 Richard W.M. Jones <rjones@redhat.com> - 1.3-43
- OCaml 4.10.0+beta1 rebuild.

* Fri Dec 06 2019 Richard W.M. Jones <rjones@redhat.com> - 1.3-42
- OCaml 4.09.0 (final) rebuild.

* Fri Oct 11 2019 Jerry James <loganjerry@gmail.com> - 1.3-41
- Rebuild for mpfr 4

* Tue Sep  3 2019 Jerry James <loganjerry@gmail.com> - 1.3-40
- Rebuild for ocaml-zarith 1.9

* Fri Aug 16 2019 Richard W.M. Jones <rjones@redhat.com> - 1.3-39
- OCaml 4.08.1 (final) rebuild.

* Thu Aug 01 2019 Richard W.M. Jones <rjones@redhat.com> - 1.3-38
- OCaml 4.08.1 (rc2) rebuild.

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-37
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jul  4 2019 Jerry James <loganjerry@gmail.com> - 1.3-36
- Rebuild for ocaml 4.08.0

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-35
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-34
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Jul 11 2018 Richard W.M. Jones <rjones@redhat.com> - 1.3-33
- OCaml 4.07.0 (final) rebuild.

* Wed Jun 20 2018 Richard W.M. Jones <rjones@redhat.com> - 1.3-32
- OCaml 4.07.0-rc1 rebuild.

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Nov 18 2017 Richard W.M. Jones <rjones@redhat.com> - 1.3-30
- OCaml 4.06.0 rebuild.

* Wed Aug 09 2017 Richard W.M. Jones <rjones@redhat.com> - 1.3-29
- OCaml 4.05.0 rebuild.

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Jun 27 2017 Richard W.M. Jones <rjones@redhat.com> - 1.3-26
- OCaml 4.04.2 rebuild.

* Sat May 13 2017 Richard W.M. Jones <rjones@redhat.com> - 1.3-25
- OCaml 4.04.1 rebuild.

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Nov 09 2016 Dan Horák <dan@danny.cz> - 1.3-23
- rebuild for s390x codegen bug

* Mon Nov 07 2016 Richard W.M. Jones <rjones@redhat.com> - 1.3-22
- Rebuild for OCaml 4.04.0.
- Add explicit dependency on ocamlbuild.

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Nov 25 2015 Jerry James <loganjerry@gmail.com> - 1.3-20
- Rebuild for ocaml-zarith 1.4.1

* Tue Jul 28 2015 Richard W.M. Jones <rjones@redhat.com> - 1.3-19
- OCaml 4.02.3 rebuild.

* Wed Jun 24 2015 Richard W.M. Jones <rjones@redhat.com> - 1.3-18
- ocaml-4.02.2 final rebuild.

* Thu Jun 18 2015 Richard W.M. Jones <rjones@redhat.com> - 1.3-17
- ocaml-4.02.2 rebuild.

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Feb 18 2015 Richard W.M. Jones <rjones@redhat.com> - 1.3-15
- ocaml-4.02.1 rebuild.

* Tue Oct 14 2014 Jerry James <loganjerry@gmail.com> - 1.3-14
- Rebuild for ocaml-zarith 1.3

* Fri Sep 19 2014 Jerry James <loganjerry@gmail.com> - 1.3-13
- Add -ocamlbuild patch to fix build with ocaml 4.02.0
- Fix license handling

* Sun Aug 24 2014 Richard W.M. Jones <rjones@redhat.com> - 1.3-12
- Bump release and rebuild.

* Sat Aug 23 2014 Richard W.M. Jones <rjones@redhat.com> - 1.3-11
- ocaml-4.02.0+rc1 rebuild.

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Aug 02 2014 Richard W.M. Jones <rjones@redhat.com> - 1.3-9
- ocaml-4.02.0-0.8.git10e45753.fc22 rebuild.

* Fri Jul 25 2014 Richard W.M. Jones <rjones@redhat.com> - 1.3-8
- OCaml 4.02.0 beta rebuild.

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Apr 18 2014 Jerry James <loganjerry@gmail.com> - 1.3-6
- Remove ocaml_arches macro (bz 1087794)
- Drop unnecessary gmp-devel BR

* Mon Sep 16 2013 Jerry James <loganjerry@gmail.com> - 1.3-5
- Rebuild for OCaml 4.01.0
- Enable debuginfo

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Jun 21 2013 Jerry James <loganjerry@gmail.com> - 1.3-3
- Rebuild for ocaml-zarith 1.2.1

* Thu May 23 2013 Jerry James <loganjerry@gmail.com> - 1.3-2
- Rebuild for ocaml-zarith 1.2

* Tue Feb 19 2013 Jerry James <loganjerry@gmail.com> - 1.3-1
- New upstream release
- Upstream dropped MLGMPIDL support in favor of MLGMP, which we don't ship

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jan 16 2013 Jerry James <loganjerry@gmail.com> - 1.2-2
- Add man pages
- Don't Provide the numeric plugins
- Make -devel also Provide -static

* Wed Oct 31 2012 Jerry James <loganjerry@gmail.com> - 1.2-1
- Initial RPM
