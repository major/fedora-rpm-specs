# OCaml packages not built on i686 since OCaml 5 / Fedora 39.
ExcludeArch: %{ix86}

Name:           ocaml-mlgmpidl
Version:        1.3.0
Release:        11%{?dist}
Summary:        OCaml interface to GMP and MPFR libraries
License:        LGPL-2.1-only WITH OCaml-LGPL-linking-exception

URL:            https://github.com/nberth/mlgmpidl
VCS:            git:%{url}.git
Source0:        %{url}/archive/%{version}/mlgmpidl-%{version}.tar.gz
Source1:        mlgmpidl_test.ml
Source2:        mlgmpidl_test_result
# Remove dependency on the bigarray-compat forward compatibility shim
Patch:          %{name}-bigarray-compat.patch

BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  ocaml
BuildRequires:  ocaml-ocamldoc
BuildRequires:  ocaml-findlib
BuildRequires:  ocaml-camlidl-devel
BuildRequires:  ocaml-rpm-macros
BuildRequires:  gmp-devel
BuildRequires:  mpfr-devel
BuildRequires:  perl-interpreter
# BuildRequires for documentation build
BuildRequires:  tex(latex)
BuildRequires:  tex(ecrm1000.tfm)
BuildRequires:  tex(fullpage.sty)
BuildRequires:  ghostscript-tools-dvipdf


%description
MLGMPIDL is an OCaml interface to the GMP and MPFR rational and real
number math libraries. Although there is another such interface, this
one is different in that it provides a more imperative (rather than
functional) interface to conserve memory and that this one uses
CAMLIDL to take care of the C/OCaml interface in a convenient and
modular way.


%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       ocaml-camlidl-devel%{?_isa}


%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.

%package        doc
Summary:        Documentation files for %{name}
BuildArch:      noarch

%description    doc
The %{name}-doc package contains documentation for using %{name}.

%prep
%autosetup -n mlgmpidl-%{version} -p1
cp -p %{SOURCE1} %{SOURCE2} .

# Fix install on 64-bit platforms
if [ "%{_lib}" != "lib" ]; then
  sed -i 's,/lib,%{_lib},g' Makefile
fi

# Build with debug information
sed -i 's/^OCAMLOPTFLAGS = -annot/& -g/' configure Makefile.config.in
sed -i 's/\$(OCAMLMKLIB)/& -g/' Makefile

%ifnarch %{ocaml_native_compiler}
# Fix build on bytecode-only architectures
sed -i 's/ocamlc\.opt/ocamlc/g;/ocamlopt\.opt/s/.*/ocamlopt=""/' configure
sed -i '/addprefix/s/OCAMLOPT/OCAMLC/g' Makefile
%endif


%build
# This is not an autoconf-generated script.  Do NOT use %%configure.
./configure \
%ifnarch %{ocaml_native_compiler}
  -no-native-plugins \
%endif
%ifnarch %{ocaml_native_profiling}
  -disable-profiling \
%endif
  -prefix %{ocamldir}

# Upstream Makefile is NOT safe to be called in parallel.
%ifarch %{ocaml_native_compiler}
make all
%else
make byte
%endif
make mlgmpidl.pdf
make html


%check
%ifarch %{ocaml_native_compiler}
ocamlopt -runtime-variant _pic -ccopt -L. -cclib -lgmp gmp.cmxa mlgmpidl_test.ml
%else
ocamlc -ccopt -L. -cclib -lgmp gmp.cma mlgmpidl_test.ml
export LD_LIBRARY_PATH=$PWD
%endif
./a.out > mlgmpidl_test_myresult
diff -u mlgmpidl_test_myresult mlgmpidl_test_result


%install
# Upstream Makefile is NOT safe to be called in parallel.
unset MAKEFLAGS

# Library uses ocamlfind install to install itself.  Set up environment
# so that it works.
export MLGMPIDL_PREFIX=$RPM_BUILD_ROOT%{_prefix}
export OCAMLFIND_DESTDIR=$RPM_BUILD_ROOT%{ocamldir}
mkdir -p $OCAMLFIND_DESTDIR $OCAMLFIND_DESTDIR/stublibs

%ifarch %{ocaml_native_compiler}
%make_install
%else
%make_install HAS_OCAMLOPT=
%endif

# Install the opam file
cp -p opam/opam $RPM_BUILD_ROOT%{ocamldir}/gmp

%ocaml_files


%files -f .ofiles
%doc README
%license COPYING


%files devel -f .ofiles-devel


%files doc
%doc README html mlgmpidl.pdf
%license COPYING


%changelog
* Sat Dec 21 2024 Jerry James <loganjerry@gmail.com> - 1.3.0-12
- Rebuild for OCaml 5.3.0
- Patch out dependency on ocaml-bigarray-compat

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jun 19 2024 Richard W.M. Jones <rjones@redhat.com> - 1.3.0-10
- OCaml 5.2.0 ppc64le fix

* Wed May 29 2024 Richard W.M. Jones <rjones@redhat.com> - 1.3.0-9
- OCaml 5.2.0 for Fedora 41

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Dec 18 2023 Richard W.M. Jones <rjones@redhat.com> - 1.3.0-6
- OCaml 5.1.1 + s390x code gen fix for Fedora 40

* Tue Dec 12 2023 Richard W.M. Jones <rjones@redhat.com> - 1.3.0-5
- OCaml 5.1.1 rebuild for Fedora 40

* Thu Oct 05 2023 Richard W.M. Jones <rjones@redhat.com> - 1.3.0-4
- OCaml 5.1 rebuild for Fedora 40

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jul 11 2023 Richard W.M. Jones <rjones@redhat.com> - 1.3.0-2
- OCaml 5.0 rebuild for Fedora 39

* Mon Jul 10 2023 Jerry James <loganjerry@gmail.com> - 1.3.0-1
- Version 1.3.0
- Convert License tag to SPDX
- Add dependency on ocaml-bigarray-compat
- Drop unnecessary ldflags patch
- Use new OCaml macros

* Tue Jan 24 2023 Richard W.M. Jones <rjones@redhat.com> - 1.2.14-8
- Rebuild OCaml packages for F38

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.14-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.14-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jun 18 2022 Richard W.M. Jones <rjones@redhat.com> - 1.2.14-5
- Bump release and rebuild.

* Sat Jun 18 2022 Richard W.M. Jones <rjones@redhat.com> - 1.2.14-4
- OCaml 4.14.0 rebuild

* Fri Feb 04 2022 Richard W.M. Jones <rjones@redhat.com> - 1.2.14-3
- OCaml 4.13.1 rebuild to remove package notes

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.14-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Mon Dec 27 2021 Jerry James <loganjerry@gmail.com> - 1.2.14-1
- New upstream version 1.2.14
- Drop upstreamed mpfr4 patch
- Invoke the configure script and simplify the spec file accordingly

* Mon Oct 04 2021 Richard W.M. Jones <rjones@redhat.com> - 1.2.12-14
- OCaml 4.13.1 build

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.12-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon Mar  1 11:02:41 GMT 2021 Richard W.M. Jones <rjones@redhat.com> - 1.2.12-12
- OCaml 4.12.0 build

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.12-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Sep 01 2020 Richard W.M. Jones <rjones@redhat.com> - 1.2.12-10
- OCaml 4.11.1 rebuild

* Fri Aug 21 2020 Richard W.M. Jones <rjones@redhat.com> - 1.2.12-9
- OCaml 4.11.0 rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.12-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon May 04 2020 Richard W.M. Jones <rjones@redhat.com> - 1.2.12-7
- OCaml 4.11.0+dev2-2020-04-22 rebuild

* Tue Apr 21 2020 Richard W.M. Jones <rjones@redhat.com> - 1.2.12-6
- OCaml 4.11.0 pre-release attempt 2

* Fri Apr 17 2020 Richard W.M. Jones <rjones@redhat.com> - 1.2.12-5
- OCaml 4.11.0 pre-release

* Thu Apr 02 2020 Richard W.M. Jones <rjones@redhat.com> - 1.2.12-4
- Update all OCaml dependencies for RPM 4.16.

* Wed Feb 26 2020 Richard W.M. Jones <rjones@redhat.com> - 1.2.12-3
- OCaml 4.10.0 final.

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.12-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jan 22 2020 Jerry James <loganjerry@gmail.com> - 1.2.12-1
- New upstream version 1.2.12
- Install the .h in the OCaml libdir as upstream intends
- Put the actual documentation files into the -doc subpackage
- Minor spec file cleanups

* Sun Jan 19 2020 Richard W.M. Jones <rjones@redhat.com> - 1.2.11-5
- OCaml 4.10.0+beta1 rebuild.

* Thu Jan 09 2020 Richard W.M. Jones <rjones@redhat.com> - 1.2.11-4
- OCaml 4.09.0 for riscv64

* Fri Dec 06 2019 Richard W.M. Jones <rjones@redhat.com> - 1.2.11-3
- Bump release and rebuild.

* Fri Dec 06 2019 Richard W.M. Jones <rjones@redhat.com> - 1.2.11-2
- OCaml 4.09.0 (final) rebuild.

* Wed Oct  9 2019 Jerry James <loganjerry@gmail.com> - 1.2.11-1
- New upstream version 1.2.11
- Drop patch 0005; there is now a Makefile.config entry to control profiling
- Add -mpfr patch to build with mpfr 4

* Fri Aug 16 2019 Richard W.M. Jones <rjones@redhat.com> - 1.2.6.1-13
- OCaml 4.08.1 (final) rebuild.

* Wed Jul 31 2019 Richard W.M. Jones <rjones@redhat.com> - 1.2.6.1-12
- OCaml 4.08.1 (rc2) rebuild.

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.6.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jun 27 2019 Richard W.M. Jones <rjones@redhat.com> - 1.2.6.1-10
- OCaml 4.08.0 (final) rebuild.

* Mon Apr 29 2019 Richard W.M. Jones <rjones@redhat.com> - 1.2.6.1-9
- OCaml 4.08.0 (beta 3) rebuild.

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.6.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.6.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Jul 11 2018 Richard W.M. Jones <rjones@redhat.com> - 1.2.6.1-6
- OCaml 4.07.0 (final) rebuild.

* Wed Jun 20 2018 Richard W.M. Jones <rjones@redhat.com> - 1.2.6.1-5
- Bump and rebuild in f29-ocaml side tag.

* Wed Jun 20 2018 Richard W.M. Jones <rjones@redhat.com> - 1.2.6.1-4
- OCaml 4.07.0-rc1 rebuild.

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.6.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Dec  6 2017 Jerry James <loganjerry@gmail.com> - 1.2.6.1-2
- Link the shared library with -lmpfr -lgmp

* Sat Dec  2 2017 Jerry James <loganjerry@gmail.com> - 1.2.6.1-1
- New upstream version 1.2.6-1.
- Drop upstreamed patches 0001, 0002, 0003, and 0004
- Ensure that patch 0005 is in the srpm regardless of build arch
- Use the upstream way of building a cmxs

* Fri Nov 17 2017 Richard W.M. Jones <rjones@redhat.com> - 1.2.4-2
- Add back the no-profiling patch for aarch64 and s390x.

* Thu Nov 09 2017 Richard W.M. Jones <rjones@redhat.com> - 1.2.4-1
- New upstream version 1.2.4.

* Wed Nov 08 2017 Richard W.M. Jones <rjones@redhat.com> - 1.2.1-0.28.20150921
- OCaml 4.06.0 rebuild.

* Tue Aug 08 2017 Richard W.M. Jones <rjones@redhat.com> - 1.2.1-0.27.20150921
- Use ocaml_native_compiler macro instead of opt test.
- Eliminate profiling on arches which do not support it.

* Mon Aug 07 2017 Richard W.M. Jones <rjones@redhat.com> - 1.2.1-0.26.20150921
- OCaml 4.05.0 rebuild.

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-0.25.20150921
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-0.24.20150921
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jun 26 2017 Richard W.M. Jones <rjones@redhat.com> - 1.2.1-0.23.20150921
- OCaml 4.04.2 rebuild.

* Fri May 12 2017 Richard W.M. Jones <rjones@redhat.com> - 1.2.1-0.22.20150921
- OCaml 4.04.1 rebuild.

* Fri Mar 24 2017 Jerry James <loganjerry@gmail.com> - 1.2.1-0.21.20150921
- Update to latest SVN snapshot
- Fix documentation installation and make -doc noarch (bz 1001268)
- Add gcc and perl BRs
- Fix the license field, comes with a static linking exception
- Use the license macro
- Drop Group tags
- Add -compare-ext and -warning patches to fix runtime problems
- Build a cmxs for apron and frama-c, which seem to expect one
- Move *.ml files to -devel

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-0.20.20150204
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun Nov 06 2016 Richard W.M. Jones <rjones@redhat.com> - 1.2.1-0.19.20150204
- Rebuild for OCaml 4.04.0.

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-0.18.20150204
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Jul 28 2015 Richard W.M. Jones <rjones@redhat.com> - 1.2.1-0.17.20150204
- OCaml 4.02.3 rebuild.

* Mon Jul 20 2015 Richard W.M. Jones <rjones@redhat.com> - 1.2.1-0.16.20150204
- Update to 2015-02-04 (from svn).
- Enable bytecode compilation.

* Wed Jun 24 2015 Richard W.M. Jones <rjones@redhat.com> - 1.2.1-0.15.20120830
- ocaml-4.02.2 final rebuild.

* Wed Jun 17 2015 Richard W.M. Jones <rjones@redhat.com> - 1.2.1-0.14.20120830
- ocaml-4.02.2 rebuild.

* Tue Feb 17 2015 Richard W.M. Jones <rjones@redhat.com> - 1.2.1-0.13.20120830
- ocaml-4.02.1 rebuild.

* Sun Aug 31 2014 Richard W.M. Jones <rjones@redhat.com> - 1.2.1-0.12.20120830
- ocaml-4.02.0 final rebuild.

* Sat Aug 23 2014 Richard W.M. Jones <rjones@redhat.com> - 1.2.1-0.11.20120830
- ocaml-4.02.0+rc1 rebuild.

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.1-0.10.20120830
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Aug 02 2014 Richard W.M. Jones <rjones@redhat.com> - 1.2.1-0.9.20120830
- ocaml-4.02.0-0.8.git10e45753.fc22 rebuild.

* Mon Jul 21 2014 Richard W.M. Jones <rjones@redhat.com> - 1.2.1-0.8.20120830
- OCaml 4.02.0 beta rebuild.

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.1-0.7.20120830
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Apr 15 2014 Richard W.M. Jones <rjones@redhat.com> - 1.2.1-0.6.20120830
- Remove ocaml_arches macro (RHBZ#1087794).

* Sat Sep 14 2013 Richard W.M. Jones <rjones@redhat.com> - 1.2.1-0.5.20120830
- Rebuild for OCaml 4.01.0.
- Enable debuginfo.
- Do not prevent stripping -- not needed for modern OCaml.

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.1-0.4.20120830
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.1-0.3.20120830
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Dec 13 2012 Jerry James <loganjerry@gmail.com> - 1.2.1-0.2.20120830
- fullpage.sty is available in TeXLive 2012; use it

* Wed Oct 17 2012 Jerry James <loganjerry@gmail.com> - 1.2.1-0.1.20120830
- Rebuild for OCaml 4.00.1.
- Update to latest upstream SVN.
- Regenerate patch with fuzz.
- Drop fix for \textquotesingle; fixed upstream.
- Replace use of old fullpage style with use of geometry package.

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2-0.5.20120508
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sun Jun 10 2012 Richard W.M. Jones <rjones@redhat.com> - 1.2-0.4.20120508
- Rebuild for OCaml 4.00.0.

* Sat Jun  9 2012 Jerry James <loganjerry@gmail.com> - 1.2-0.3.20120508
- Rebuild for OCaml 4.00.0
- Fix for undefined control sequence \textquotesingle
- Minor spec file cleanups

* Tue May  8 2012 Richard W.M. Jones <rjones@redhat.com> - 1.2-0.2.20120508
- Update to latest upstream SVN.
- Change define -> global.
- Don't create or install a META file, as upstream now creates one
  (RHBZ#819785).
- Remove patch1, no longer needed.
- Library now uses 'ocamlfind install' to install itself.
- Library has moved from 'mlgmpidl' to 'gmp' directory.
- gmptop (toplevel) has disappeared from upstream, so remove it.  We
  can also get rid of the prelink hacks.
- Package stublibs.
- Add missing BR ocaml-findlib-devel.

* Mon Jan  9 2012 Jerry James <loganjerry@gmail.com> - 1.1-7
- Rebuild for OCaml 3.12.1
- Minor spec file cleanups

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Jan 10 2011 Richard W.M. Jones <rjones@redhat.com> - 1.1-6
- Rebuild for OCaml 3.12 (http://fedoraproject.org/wiki/Features/OCaml3.12).
- Remove GMP_RND_MAX and mpfr_random, both no longer in GMP/MPFR.

* Wed Dec 30 2009 Richard W.M. Jones <rjones@redhat.com> - 1.1-4
- Rebuild for OCaml 3.11.2.

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Sat May 23 2009 Richard W.M. Jones <rjones@redhat.com> - 1.1-2
- Rebuild for OCaml 3.11.1

* Thu Apr 16 2009 S390x secondary arch maintainer <fedora-s390x@lists.fedoraproject.org>
- ExcludeArch sparc64, s390, s390x as we don't have OCaml on those archs
  (added sparc64 per request from the sparc maintainer)

* Thu Apr 02 2009 Alan Dunn <amdunn@gmail.com> 1.1-1
- New upstream version incorporates functional interface to Mpfr.
* Sat Mar 28 2009 Alan Dunn <amdunn@gmail.com> 1.0-1
- Initial Fedora RPM version.
