%undefine _package_note_flags
%global opt %(test -x %{_bindir}/ocamlopt && echo 1 || echo 0)

%global ocamllibdir %{_libdir}/ocaml

Name:           ocaml-ancient
Version:        0.9.0
Release:        69%{?dist}
Summary:        OCaml library for large memory structures and sharing
License:        LGPLv2+ with exceptions

# Upstream website is dead, but the code is maintained at
# http://git.annexia.org/?p=ocaml-ancient.git;a=summary.  The current
# tarball is based on the last one released upstream.
URL:            http://git.annexia.org/?p=ocaml-ancient.git;a=summary
Source0:        ancient-%{version}.tar.gz

Patch1:         ancient-0.9.0-use-ocamlopt-g.patch
# Use header_t with OCaml 4.04.0.
Patch2:         ancient-0.9.0-use-header_t.patch
Patch3: ocaml-ancient-configure-c99.patch

BuildRequires: make
BuildRequires:  ocaml >= 3.10.0
BuildRequires:  ocaml-findlib-devel
BuildRequires:  ocaml-ocamldoc
BuildRequires:  chrpath


%description
Ancient is an OCaml module that allows you to use in-memory data
structures which are larger than available memory and so are kept in
swap. If you try this in normal OCaml code, you'll find that the
machine quickly descends into thrashing as the garbage collector
repeatedly iterates over swapped memory structures. This module lets
you break that limitation. Of course the module doesn't work by magic.
If your program tries to access these large structures, they still
need to be swapped back in, but it is suitable for large, sparsely
accessed structures.

Secondly, this module allows you to share those structures between
processes. In this mode, the structures are backed by a disk file, and
any process that has read/write access to that disk file can map that
file in and see the structures.

Developers should read the README.txt file included with the
ocaml-ancient-devel package carefully.


%package        devel
Summary:        Development files for %{name}
Requires:       %{name} = %{version}-%{release}


%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.


%prep
%setup -q -n ancient-%{version}

%patch1 -p1
%patch2 -p1
%patch3 -p1


%build
pushd mmalloc
%configure
make
popd

CFLAGS='-g -fPIC -Wall -Werror -I%{ocamllibdir} -DOCAML_VERSION_MAJOR=$(OCAML_VERSION_MAJOR) -DOCAML_VERSION_MINOR=$(OCAML_VERSION_MINOR) %{optflags}' \
    make \
%if %opt
    all
%else
    ancient.cma META
%endif

make doc ||:


%install
export DESTDIR=$RPM_BUILD_ROOT
export OCAMLFIND_DESTDIR=$RPM_BUILD_ROOT%{_libdir}/ocaml
mkdir -p $RPM_BUILD_ROOT%{_libdir}
mkdir -p $OCAMLFIND_DESTDIR $OCAMLFIND_DESTDIR/stublibs
%if %opt
ocamlfind install ancient ancient.cmi *.mli *.cma ancient.cmx *.cmxa *.a *.so \
  mmalloc/*.a META
%else
ocamlfind install ancient ancient.cmi *.mli *.cma *.a *.so \
  mmalloc/*.a META
%endif

chrpath --delete $OCAMLFIND_DESTDIR/stublibs/dll*.so


%files
%doc mmalloc/COPYING.LIB
%{_libdir}/ocaml/ancient
%if %opt
%exclude %{_libdir}/ocaml/ancient/*.a
%exclude %{_libdir}/ocaml/ancient/*.cmxa
%exclude %{_libdir}/ocaml/ancient/*.cmx
%endif
%exclude %{_libdir}/ocaml/ancient/*.mli
%{_libdir}/ocaml/stublibs/*.so
%{_libdir}/ocaml/stublibs/*.so.owner


%files devel
%doc README.txt html/*
%if %opt
%{_libdir}/ocaml/ancient/*.a
%{_libdir}/ocaml/ancient/*.cmxa
%{_libdir}/ocaml/ancient/*.cmx
%endif
%{_libdir}/ocaml/ancient/*.mli


%changelog
* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.0-69
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Apr 27 2023 Florian Weimer <fweimer@redhat.com> - 0.9.0-68
- Port configure script to C99

* Mon Jan 23 2023 Richard W.M. Jones <rjones@redhat.com> - 0.9.0-67
- Rebuild OCaml packages for F38

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.0-66
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.0-65
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jun 18 2022 Richard W.M. Jones <rjones@redhat.com> - 0.9.0-64
- OCaml 4.14.0 rebuild

* Fri Feb 04 2022 Richard W.M. Jones <rjones@redhat.com> - 0.9.0-63
- OCaml 4.13.1 rebuild to remove package notes

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.0-62
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Mon Oct 04 2021 Richard W.M. Jones <rjones@redhat.com> - 0.9.0-61
- OCaml 4.13.1 build

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.0-60
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon Mar  1 17:41:01 GMT 2021 Richard W.M. Jones <rjones@redhat.com> - 0.9.0-59
- OCaml 4.12.0 build

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.0-58
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Sep 01 2020 Richard W.M. Jones <rjones@redhat.com> - 0.9.0-57
- OCaml 4.11.1 rebuild

* Fri Aug 21 2020 Richard W.M. Jones <rjones@redhat.com> - 0.9.0-56
- OCaml 4.11.0 rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.0-55
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon May 04 2020 Richard W.M. Jones <rjones@redhat.com> - 0.9.0-54
- OCaml 4.11.0+dev2-2020-04-22 rebuild

* Tue Apr 21 2020 Richard W.M. Jones <rjones@redhat.com> - 0.9.0-53
- OCaml 4.11.0 pre-release attempt 2

* Fri Apr 17 2020 Richard W.M. Jones <rjones@redhat.com> - 0.9.0-52
- OCaml 4.11.0 pre-release

* Thu Apr 02 2020 Richard W.M. Jones <rjones@redhat.com> - 0.9.0-51
- Update all OCaml dependencies for RPM 4.16.

* Wed Feb 26 2020 Richard W.M. Jones <rjones@redhat.com> - 0.9.0-50
- OCaml 4.10.0 final.

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.0-49
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Jan 19 2020 Richard W.M. Jones <rjones@redhat.com> - 0.9.0-48
- OCaml 4.10.0+beta1 rebuild.

* Thu Jan 09 2020 Richard W.M. Jones <rjones@redhat.com> - 0.9.0-47
- OCaml 4.09.0 for riscv64

* Fri Dec 06 2019 Richard W.M. Jones <rjones@redhat.com> - 0.9.0-46
- OCaml 4.09.0 (final) rebuild.

* Fri Aug 16 2019 Richard W.M. Jones <rjones@redhat.com> - 0.9.0-45
- OCaml 4.08.1 (final) rebuild.

* Wed Jul 31 2019 Richard W.M. Jones <rjones@redhat.com> - 0.9.0-44
- OCaml 4.08.1 (rc2) rebuild.

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.0-43
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jun 27 2019 Richard W.M. Jones <rjones@redhat.com> - 0.9.0-42
- OCaml 4.08.0 (final) rebuild.

* Mon Apr 29 2019 Richard W.M. Jones <rjones@redhat.com> - 0.9.0-41
- OCaml 4.08.0 (beta 3) rebuild.

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.0-40
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.0-39
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Jul 11 2018 Richard W.M. Jones <rjones@redhat.com> - 0.9.0-38
- OCaml 4.07.0 (final) rebuild.

* Wed Jun 20 2018 Richard W.M. Jones <rjones@redhat.com> - 0.9.0-37
- OCaml 4.07.0-rc1 rebuild.

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.0-36
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Nov 17 2017 Richard W.M. Jones <rjones@redhat.com> - 0.9.0-35
- OCaml 4.06.0 rebuild.

* Tue Aug 08 2017 Richard W.M. Jones <rjones@redhat.com> - 0.9.0-34
- OCaml 4.05.0 rebuild.

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.0-33
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.0-32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Jun 27 2017 Richard W.M. Jones <rjones@redhat.com> - 0.9.0-31
- OCaml 4.04.2 rebuild.

* Sat May 13 2017 Richard W.M. Jones <rjones@redhat.com> - 0.9.0-30
- OCaml 4.04.1 rebuild.

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.0-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Nov 07 2016 Richard W.M. Jones <rjones@redhat.com> - 0.9.0-28
- Rebuild for OCaml 4.04.0.
- Small fix for OCaml 4.04.0 changes in Hp_val macro.

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.0-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Jan 05 2016 Richard Jones <rjones@redhat.com> - 0.9.0-26
- Use global instead of define.

* Tue Jul 28 2015 Richard W.M. Jones <rjones@redhat.com> - 0.9.0-25
- OCaml 4.02.3 rebuild.

* Tue Jul 21 2015 Richard W.M. Jones <rjones@redhat.com> - 0.9.0-24
- Fix bytecode compilation.

* Wed Jun 24 2015 Richard W.M. Jones <rjones@redhat.com> - 0.9.0-23
- ocaml-4.02.2 final rebuild.

* Thu Jun 18 2015 Richard W.M. Jones <rjones@redhat.com> - 0.9.0-22
- ocaml-4.02.2 rebuild.

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.0-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Feb 17 2015 Richard W.M. Jones <rjones@redhat.com> - 0.9.0-20
- ocaml-4.02.1 rebuild.

* Sun Aug 31 2014 Richard W.M. Jones <rjones@redhat.com> - 0.9.0-19
- ocaml-4.02.0 final rebuild.

* Sat Aug 23 2014 Richard W.M. Jones <rjones@redhat.com> - 0.9.0-18
- ocaml-4.02.0+rc1 rebuild.

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.0-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Fri Aug 01 2014 Richard W.M. Jones <rjones@redhat.com> - 0.9.0-16
- ocaml-4.02.0-0.8.git10e45753.fc22 rebuild.

* Thu Jul 17 2014 Richard W.M. Jones <rjones@redhat.com> - 0.9.0-15
- OCaml 4.02.0 beta rebuild.

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Sep 14 2013 Richard W.M. Jones <rjones@redhat.com> - 0.9.0-13
- Rebuild for OCaml 4.01.0.
- Enable debuginfo.
- Fix URL and Source.
- Modernize spec file.

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Tue Oct 30 2012 Richard W.M. Jones <rjones@redhat.com> - 0.9.0-10
- Rebuild for OCaml 4.00.1.

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jun 09 2012 Richard W.M. Jones <rjones@redhat.com> - 0.9.0-8
- Rebuild for OCaml 4.00.0.

* Fri Jan 06 2012 Richard W.M. Jones <rjones@redhat.com> - 0.9.0-7
- Rebuild for OCaml 3.12.1.

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Jan 06 2011 Richard W.M. Jones <rjones@redhat.com> - 0.9.0-5
- Rebuild for OCaml 3.12 (http://fedoraproject.org/wiki/Features/OCaml3.12).

* Wed Dec 30 2009 Richard W.M. Jones <rjones@redhat.com> - 0.9.0-4
- Rebuild for OCaml 3.11.2.

* Tue Sep 22 2009 Dennis Gilmore <dennis@ausil.us> - 0.9.0-3
- ExcludeArch sparc64 s390 s390x  no ocaml

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue May 26 2009 Richard W.M. Jones <rjones@redhat.com> - 0.9.0-1
- Initial RPM release.
