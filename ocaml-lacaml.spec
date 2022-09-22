%undefine _package_note_flags

%global opt %(test -x %{_bindir}/ocamlopt && echo 1 || echo 0)

%if 0%{?fedora} >= 33
%bcond_without flexiblas
%endif

Name:           ocaml-lacaml
Version:        11.0.8
Release:        3%{?dist}
Summary:        BLAS/LAPACK-interface for OCaml

License:        LGPLv2 with exceptions
URL:            https://github.com/mmottl/lacaml
Source0:        https://github.com/mmottl/lacaml/archive/refs/tags/%{version}.tar.gz

# Break a circular dependency on ocaml-odoc
%bcond_with doc

BuildRequires:  make
BuildRequires:  ocaml
BuildRequires:  ocaml-findlib-devel
BuildRequires:  ocaml-compiler-libs
BuildRequires:  ocaml-dune-devel
%if %{with flexiblas}
BuildRequires:	flexiblas-devel
%else
BuildRequires:	blas-devel, lapack-devel
%endif

%if %{with doc}
BuildRequires:  ocaml-odoc
%endif

%global __ocaml_requires_opts -i Asttypes -i Parsetree -i Common -i Utils
%global __ocaml_provides_opts -i Common -i Install_printers -i Io -i Utils


%description
This OCaml-library interfaces the BLAS-library (Basic Linear Algebra
Subroutines) and LAPACK-library (Linear Algebra routines), which are
written in FORTRAN.

This allows people to write high-performance numerical code for
applications that need linear algebra.


%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}


%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.


%prep
%setup -q -n lacaml-%{version}

%ifarch %{power64}
# Otherwise we add the -march=native flag which ppc64le does not
# understand.  This flag is added by the lacaml build system.
# https://github.com/mmottl/lacaml/issues/51
sed -i 's/-march=native//' `find -name dune`
%endif


%build
%if %{with flexiblas}
export LACAML_LIBS="-lflexiblas"
%endif
dune build %{?_smp_mflags}
%if %{with doc}
dune build %{?_smp_mflags} @doc
%endif


%install
dune install --destdir=%{buildroot}

%if %{with doc}
# We do not want the dune markers
find _build/default/_doc/_html -name .dune-keep -delete
%endif

# We install the documentation with the doc macro
rm -fr %{buildroot}%{_prefix}/doc


%files
%license LICENSE.md
%{_libdir}/ocaml/lacaml
%if %opt
%exclude %{_libdir}/ocaml/lacaml/*.a
%exclude %{_libdir}/ocaml/lacaml/*.cmxa
%exclude %{_libdir}/ocaml/lacaml/*.cmx
%endif
%exclude %{_libdir}/ocaml/lacaml/*.mli
%exclude %{_libdir}/ocaml/lacaml/*.ml
%{_libdir}/ocaml/stublibs/dlllacaml_stubs.so


%files devel
%license LICENSE.md
%doc CHANGES.md README.md
%if %opt
%{_libdir}/ocaml/lacaml/*.a
%{_libdir}/ocaml/lacaml/*.cmxa
%{_libdir}/ocaml/lacaml/*.cmx
%endif
%{_libdir}/ocaml/lacaml/*.mli
%{_libdir}/ocaml/lacaml/*.ml


%changelog
* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 11.0.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jun 18 2022 Richard W.M. Jones <rjones@redhat.com> - 11.0.8-2
- Fix build and make doc conditional

* Sat Jun 18 2022 Richard W.M. Jones <rjones@redhat.com> - 11.0.8-1
- New upstream version 11.0.8
- OCaml 4.14.0 rebuild

* Fri Feb 04 2022 Richard W.M. Jones <rjones@redhat.com> - 9.3.2-31
- OCaml 4.13.1 rebuild to remove package notes

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 9.3.2-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Mon Oct 04 2021 Richard W.M. Jones <rjones@redhat.com> - 9.3.2-29
- OCaml 4.13.1 build

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 9.3.2-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon Mar  1 17:12:23 GMT 2021 Richard W.M. Jones <rjones@redhat.com> - 9.3.2-27
- OCaml 4.12.0 build

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 9.3.2-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Sep 01 2020 Richard W.M. Jones <rjones@redhat.com> - 9.3.2-25
- OCaml 4.11.1 rebuild

* Thu Aug 27 2020 Iñaki Úcar <iucar@fedoraproject.org> - 9.3.2-24
- https://fedoraproject.org/wiki/Changes/FlexiBLAS_as_BLAS/LAPACK_manager

* Fri Aug 21 2020 Richard W.M. Jones <rjones@redhat.com> - 9.3.2-23
- OCaml 4.11.0 rebuild

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 9.3.2-22
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 9.3.2-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon May 04 2020 Richard W.M. Jones <rjones@redhat.com> - 9.3.2-20
- OCaml 4.11.0+dev2-2020-04-22 rebuild

* Tue Apr 21 2020 Richard W.M. Jones <rjones@redhat.com> - 9.3.2-19
- OCaml 4.11.0 pre-release attempt 2

* Fri Apr 17 2020 Richard W.M. Jones <rjones@redhat.com> - 9.3.2-18
- OCaml 4.11.0 pre-release

* Thu Apr 02 2020 Richard W.M. Jones <rjones@redhat.com> - 9.3.2-17
- Update all OCaml dependencies for RPM 4.16.

* Wed Feb 26 2020 Richard W.M. Jones <rjones@redhat.com> - 9.3.2-16
- OCaml 4.10.0 final.

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 9.3.2-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Jan 19 2020 Richard W.M. Jones <rjones@redhat.com> - 9.3.2-14
- OCaml 4.10.0+beta1 rebuild.

* Thu Jan 09 2020 Richard W.M. Jones <rjones@redhat.com> - 9.3.2-13
- OCaml 4.09.0 for riscv64

* Fri Dec 06 2019 Richard W.M. Jones <rjones@redhat.com> - 9.3.2-12
- OCaml 4.09.0 (final) rebuild.

* Fri Aug 16 2019 Richard W.M. Jones <rjones@redhat.com> - 9.3.2-11
- OCaml 4.08.1 (final) rebuild.

* Thu Aug 01 2019 Richard W.M. Jones <rjones@redhat.com> - 9.3.2-10
- OCaml 4.08.1 (rc2) rebuild.

* Sat Jul 27 2019 Richard W.M. Jones <rjones@redhat.com> - 9.3.2-9
- Drop unnecessary camlp4 dependency.

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 9.3.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 9.3.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 9.3.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Jul 11 2018 Richard W.M. Jones <rjones@redhat.com> - 9.3.2-5
- OCaml 4.07.0 (final) rebuild.

* Wed Jun 20 2018 Richard W.M. Jones <rjones@redhat.com> - 9.3.2-4
- OCaml 4.07.0-rc1 rebuild.

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 9.3.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Nov 18 2017 Richard W.M. Jones <rjones@redhat.com> - 9.3.2-2
- OCaml 4.06.0 rebuild.

* Tue Aug 08 2017 Richard W.M. Jones <rjones@redhat.com> - 9.3.2-1
- New upstream version 9.3.2.
- OCaml 4.05.0 rebuild.

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 9.1.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 9.1.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Jun 27 2017 Richard W.M. Jones <rjones@redhat.com> - 9.1.1-5
- OCaml 4.04.2 rebuild.

* Sat May 13 2017 Richard W.M. Jones <rjones@redhat.com> - 9.1.1-4
- OCaml 4.04.1 rebuild.

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 9.1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Nov 09 2016 Dan Horák <dan@danny.cz> - 9.1.1-2
- rebuild for s390x codegen bug

* Mon Nov 07 2016 Richard W.M. Jones <rjones@redhat.com> - 9.1.1-1
- New upstream version 9.1.1.
- Add explicit dependency on ocamlbuild.

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 7.2.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Jul 28 2015 Richard W.M. Jones <rjones@redhat.com> - 7.2.5-2
- OCaml 4.02.3 rebuild.

* Tue Jul 21 2015 Richard W.M. Jones <rjones@redhat.com> - 7.2.5-1
- New upstream version 7.2.5.

* Wed Jun 24 2015 Richard W.M. Jones <rjones@redhat.com> - 7.1.3-9
- ocaml-4.02.2 final rebuild.

* Thu Jun 18 2015 Richard W.M. Jones <rjones@redhat.com> - 7.1.3-8
- ocaml-4.02.2 rebuild.

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 7.1.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Feb 17 2015 Richard W.M. Jones <rjones@redhat.com> - 7.1.3-6
- ocaml-4.02.1 rebuild.

* Sun Aug 31 2014 Richard W.M. Jones <rjones@redhat.com> - 7.1.3-5
- ocaml-4.02.0 final rebuild.

* Sat Aug 23 2014 Richard W.M. Jones <rjones@redhat.com> - 7.1.3-4
- ocaml-4.02.0+rc1 rebuild.

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 7.1.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Aug 02 2014 Richard W.M. Jones <rjones@redhat.com> - 7.1.3-2
- ocaml-4.02.0-0.8.git10e45753.fc22 rebuild.

* Mon Jul 21 2014 Richard W.M. Jones <rjones@redhat.com> - 7.1.3-1
- New upstream version 7.1.3.
- Change source URLs.
- OCaml 4.02.0 beta rebuild.

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 7.0.9-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Apr 15 2014 Richard W.M. Jones <rjones@redhat.com> - 7.0.9-3
- Remove ocaml_arches macro (RHBZ#1087794).

* Sat Sep 21 2013 Richard W.M. Jones <rjones@redhat.com> - 7.0.9-2
- Ignore Common and Utils when calculating requires.

* Wed Sep 18 2013 Jerry James <loganjerry@gmail.com> - 7.0.9-1
- New upstream version 7.0.9
- Rebuild for OCaml 4.01.0
- Enable debuginfo
- Minor spec file cleanups

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 7.0.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 7.0.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Mon Oct 29 2012 Richard W.M. Jones <rjones@redhat.com> - 7.0.3-1
- New upstream version 7.0.3.
- Clean up the spec file.
- Rebuild for OCaml 4.00.1.
- +BR ocamldoc.

* Mon Jul 30 2012 Richard W.M. Jones <rjones@redhat.com> - 5.5.2-4
- Rebuild for OCaml 4.00.0 official.

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.5.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jun 09 2012 Richard W.M. Jones <rjones@redhat.com> - 5.5.2-2
- Rebuild for OCaml 4.00.0.
- Patch Makefile to disable warn-error and to include +compiler-libs.

* Wed Jan 11 2012 Richard W.M. Jones <rjones@redhat.com> - 5.5.2-1
- New upstream version 5.5.2.
- Rebuild for OCaml 3.12.1.

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.4.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Jan  6 2011 Richard W.M. Jones <rjones@redhat.com> - 5.4.8-1
- New upstream version 5.4.8.
- Rebuild for OCaml 3.12.0.

* Wed Dec 30 2009 Richard W.M. Jones <rjones@redhat.com> - 5.4.7-2
- Rebuild for OCaml 3.11.2.

* Sun Oct  4 2009 Richard W.M. Jones <rjones@redhat.com> - 5.4.7-1
- New upstream release 5.4.7.

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Sat May 23 2009 Richard W.M. Jones <rjones@redhat.com> - 5.1.0-1
- Rebuild for OCaml 3.11.1.
- New upstream release 5.1.0.

* Thu Apr 16 2009 S390x secondary arch maintainer <fedora-s390x@lists.fedoraproject.org>
- ExcludeArch sparc64, s390, s390x as we don't have OCaml on those archs
  (added sparc64 per request from the sparc maintainer)

* Tue Mar 10 2009 Richard W.M. Jones <rjones@redhat.com> - 4.7.6-1
- New upstream version 4.7.6.
- Name of documentation files has changed slightly.

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.6.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Dec  4 2008 Richard W.M. Jones <rjones@redhat.com> - 4.6.8-2
- Rebuild.

* Thu Nov 20 2008 Richard W.M. Jones <rjones@redhat.com> - 4.6.8-1
- New upstream version 4.6.8.

* Wed Nov 19 2008 Richard W.M. Jones <rjones@redhat.com> - 4.3.3-2
- Rebuild for OCaml 3.11.0

* Sun Aug 31 2008 Richard W.M. Jones <rjones@redhat.com> - 4.3.3-1
- New upstream version 4.3.3.

* Fri May  2 2008 Richard W.M. Jones <rjones@redhat.com> - 4.3.2-1
- New upstream version 4.3.2.

* Wed Apr 23 2008 Richard W.M. Jones <rjones@redhat.com> - 4.3.1-2
- Rebuild for OCaml 3.10.2

* Mon Apr 21 2008 Richard W.M. Jones <rjones@redhat.com> - 4.3.1-1
- New upstream release 4.3.1.
- Fix upstream URL.

* Tue Mar  4 2008 Richard W.M. Jones <rjones@redhat.com> - 4.3.0-2
- Rebuild for ppc64.

* Wed Feb 20 2008 Richard W.M. Jones <rjones@redhat.com> - 4.3.0-1
- Initial RPM release.
