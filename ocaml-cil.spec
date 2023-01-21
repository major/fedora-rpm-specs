%undefine _package_note_flags
# Disable debuginfo because I cannot get -g passed to ocamlopt -a
%global debug_package %{nil}

Name:           ocaml-cil
Version:        1.7.3
Release:        76%{?dist}
Summary:        CIL - Infrastructure for C Program Analysis and Transformation
License:        BSD

URL:            https://github.com/cil-project/cil
Source0:        https://github.com/cil-project/cil/archive/cil-%{version}.tar.gz

BuildRequires: make
BuildRequires:  ocaml
BuildRequires:  ocaml-ocamlbuild
BuildRequires:  ocaml-findlib-devel
BuildRequires:  ocaml-ocamldoc
BuildRequires:  ocaml-num-devel

Patch0:         0001-Fix-testsuite-on-32-bit-machines.patch
Patch1:         0002-Do-not-fail-testsuite-on-new-gcc-behaviour.patch

# Enable ocamlopt -g.
Patch2:         cil-1.7.3-enable-ocamlopt-g.patch

# Add package directive to App::Cilly::CilConfig so that perl
# dependencies are calculated properly.
Patch3:         cil-1.7.3-add-package-cilconfig.patch

# Fix unsafe use of Obj.magic (upstream in > 1.7.3).
# https://bugzilla.redhat.com/show_bug.cgi?id=1120273
Patch4:         ocaml-4.02.0.patch

# Fix for bytecode compilation (only apply this when !opt).
Patch5:         cil-1.7.3-bytecode-compilation.patch

# Fix compilation with GCC 7.
# gcc -dumpversion prints just "7", adjust the regex accordingly.
Patch6:         cil-1.7.3-gcc-7.patch

# Fix unescaped left brace in regex
Patch7:         cil-1.7.3-Fix-unescaped-left-brace-in-regex.patch

# Fixes for -safe-string in OCaml 4.06.
Patch8:         cil-1.7.3-safe-string.patch

%description
CIL (C Intermediate Language) is a high-level representation along
with a set of tools that permit easy analysis and source-to-source
transformation of C programs.

CIL is both lower-level than abstract-syntax trees, by clarifying
ambiguous constructs and removing redundant ones, and also
higher-level than typical intermediate languages designed for
compilation, by maintaining types and a close relationship with the
source program. The main advantage of CIL is that it compiles all
valid C programs into a few core constructs with a very clean
semantics. Also CIL has a syntax-directed type system that makes it
easy to analyze and manipulate C programs. Furthermore, the CIL
front-end is able to process not only ANSI-C programs but also those
using Microsoft C or GNU C extensions. If you do not use CIL and want
instead to use just a C parser and analyze programs expressed as
abstract-syntax trees then your analysis will have to handle a lot of
ugly corners of the language (let alone the fact that parsing C itself
is not a trivial task).

In essence, CIL is a highly-structured, "clean" subset of C. CIL
features a reduced number of syntactic and conceptual forms. For
example, all looping constructs are reduced to a single form, all
function bodies are given explicit return statements, syntactic sugar
like "->" is eliminated and function arguments with array types become
pointers.


%package        devel
Summary:        Development files for %{name}
Requires:       %{name} = %{version}-%{release}


%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.


%package        doc
Summary:        Documentation for %{name}
Requires:       %{name} = %{version}-%{release}
BuildRequires:  tex(latex), hevea


%description    doc
The %{name}-doc package contains documentation for users of %{name}.


%package        cilly
Summary:        Support programs for %{name}
Requires:       %{name} = %{version}-%{release}
# test and doc use cilly: Requires must also be BuildRequires
BuildRequires:  perl-generators
BuildRequires:  perl(Carp)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(File::Copy)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(FindBin)
BuildRequires:  perl(lib)
BuildRequires:  perl(strict)
BuildRequires:  perl(Text::ParseWords)
# Some more dependencies used only for build and test
BuildRequires:  perl(Getopt::Long)
BuildRequires:  perl(ExtUtils::MakeMaker)
# Filter out wrong Provides (automatically generated)
%global __provides_exclude perl\\(AR|GNUCC|MSLIB|MSLINK|MSVC\\)

%description    cilly
The %{name}-cilly package contains the 'cilly' wrapper/replacement
for gcc.


%prep
%setup -q -n cil-%{version}

%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%ifnarch %{ocaml_native_compiler}
%patch5 -p1
%endif
%patch6 -p1
%patch7 -p1
%patch8 -p1

%build

export PERL_MM_OPT=INSTALLDIRS=vendor

%configure
# make -j is broken, do not use it
unset MAKEFLAGS
make all doc
# Force build of bytecode version even if ocamlopt is available
make OCAMLBEST= bin/cilly.byte

%check
# Test suite is advisory.  Even upstream it does not work fully.
make test ||:

%install

export DESTDIR=$RPM_BUILD_ROOT
export OCAMLFIND_DESTDIR=$RPM_BUILD_ROOT%{_libdir}/ocaml

mkdir -p $OCAMLFIND_DESTDIR
make DESTDIR=$DESTDIR install

# clean up .packlist
find $DESTDIR -name .packlist -type f -exec rm -f {} \;

# make install does not install documentation
# Copy documentation in doc/ocaml-cil, avoiding spurious files not cleaned up by
# CIL
mkdir -p doc/ocaml-cil/html
cp -r doc/html/cil/api doc/ocaml-cil/html
cp -r doc/html/cil/examples doc/ocaml-cil/html
cp doc/html/cil/*.html doc/ocaml-cil/html/
cp doc/html/cil/*.css doc/ocaml-cil/html/
cp doc/html/cil/*.svg doc/ocaml-cil/html/
cp doc/html/cil/CIL.pdf doc/ocaml-cil/cil-manual.pdf


%files
%doc README.md LICENSE
%{_libdir}/ocaml/cil
%ifarch %{ocaml_native_compiler}
%exclude %{_libdir}/ocaml/cil/*.a
%exclude %{_libdir}/ocaml/cil/*.cmxa
%exclude %{_libdir}/ocaml/cil/*.cmx
%endif
%exclude %{_libdir}/ocaml/cil/*.mli


%files devel
%doc README.md LICENSE
%ifarch %{ocaml_native_compiler}
%{_libdir}/ocaml/cil/*.a
%{_libdir}/ocaml/cil/*.cmxa
%{_libdir}/ocaml/cil/*.cmx
%endif
%{_libdir}/ocaml/cil/*.mli


%files doc
%doc README.md LICENSE doc/ocaml-cil/*

%files cilly
%doc README.md LICENSE
%dir %{perl_vendorlib}/App
%{perl_vendorlib}/App/Cilly
%{perl_vendorlib}/App/Cilly.pm
%{_bindir}/cilly*


%changelog
* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.3-76
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.3-75
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jun 18 2022 Richard W.M. Jones <rjones@redhat.com> - 1.7.3-74
- OCaml 4.14.0 rebuild

* Wed Jun 01 2022 Jitka Plesnikova <jplesnik@redhat.com> - 1.7.3-73
- Perl 5.36 rebuild

* Fri Feb 04 2022 Richard W.M. Jones <rjones@redhat.com> - 1.7.3-72
- OCaml 4.13.1 rebuild to remove package notes

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.3-71
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Mon Oct 04 2021 Richard W.M. Jones <rjones@redhat.com> - 1.7.3-70
- OCaml 4.13.1 build

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.3-69
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Sat May 22 2021 Jitka Plesnikova <jplesnik@redhat.com> - 1.7.3-68
- Perl 5.34 rebuild

* Mon Mar  1 17:26:07 GMT 2021 Richard W.M. Jones <rjones@redhat.com> - 1.7.3-67
- OCaml 4.12.0 build

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.3-66
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Sep 01 2020 Richard W.M. Jones <rjones@redhat.com> - 1.7.3-65
- OCaml 4.11.1 rebuild

* Fri Aug 21 2020 Richard W.M. Jones <rjones@redhat.com> - 1.7.3-64
- OCaml 4.11.0 rebuild

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.3-63
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.3-62
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jun 25 2020 Jitka Plesnikova <jplesnik@redhat.com> - 1.7.3-61
- Perl 5.32 rebuild

* Mon May 04 2020 Richard W.M. Jones <rjones@redhat.com> - 1.7.3-60
- OCaml 4.11.0+dev2-2020-04-22 rebuild

* Tue Apr 21 2020 Richard W.M. Jones <rjones@redhat.com> - 1.7.3-59
- OCaml 4.11.0 pre-release attempt 2

* Fri Apr 17 2020 Richard W.M. Jones <rjones@redhat.com> - 1.7.3-58
- OCaml 4.11.0 pre-release

* Fri Apr 03 2020 Richard W.M. Jones <rjones@redhat.com> - 1.7.3-57
- Update all OCaml dependencies for RPM 4.16.

* Wed Feb 26 2020 Richard W.M. Jones <rjones@redhat.com> - 1.7.3-56
- OCaml 4.10.0 final.

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.3-55
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Jan 19 2020 Richard W.M. Jones <rjones@redhat.com> - 1.7.3-54
- OCaml 4.10.0+beta1 rebuild.

* Fri Dec 06 2019 Richard W.M. Jones <rjones@redhat.com> - 1.7.3-53
- OCaml 4.09.0 (final) rebuild.

* Fri Aug 16 2019 Richard W.M. Jones <rjones@redhat.com> - 1.7.3-52
- OCaml 4.08.1 (final) rebuild.

* Wed Jul 31 2019 Richard W.M. Jones <rjones@redhat.com> - 1.7.3-51
- OCaml 4.08.1 (rc2) rebuild.

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.3-50
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jun 27 2019 Richard W.M. Jones <rjones@redhat.com> - 1.7.3-49
- OCaml 4.08.0 (final) rebuild.

* Sat Jun 01 2019 Jitka Plesnikova <jplesnik@redhat.com> - 1.7.3-48
- Perl 5.30 rebuild

* Mon Apr 29 2019 Richard W.M. Jones <rjones@redhat.com> - 1.7.3-47
- OCaml 4.08.0 (beta 3) rebuild.

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.3-46
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Jan 08 2019 Richard W.M. Jones <rjones@redhat.com> - 1.7.3-45
- hevea now generates *.svg instead of *.gif (RHBZ#1664307).

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.3-44
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Jul 11 2018 Richard W.M. Jones <rjones@redhat.com> - 1.7.3-43
- OCaml 4.07.0 (final) rebuild.

* Fri Jun 29 2018 Jitka Plesnikova <jplesnik@redhat.com> - 1.7.3-42
- Perl 5.28 rebuild

* Wed Jun 20 2018 Richard W.M. Jones <rjones@redhat.com> - 1.7.3-41
- OCaml 4.07.0-rc1 rebuild.

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.3-40
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Nov 22 2017 Richard W.M. Jones <rjones@redhat.com> - 1.7.3-39
- OCaml 4.06.0 rebuild.
- Fixes for -safe-string.
- Stop using opt macro.
- Enable debuginfo on all architectures.

* Tue Aug 08 2017 Richard W.M. Jones <rjones@redhat.com> - 1.7.3-38
- OCaml 4.05.0 rebuild.

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.3-37
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.3-36
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Jun 27 2017 Richard W.M. Jones <rjones@redhat.com> - 1.7.3-35
- OCaml 4.04.2 rebuild.

* Wed Jun 07 2017 Jitka Plesnikova <jplesnik@redhat.com> - 1.7.3-34
- Perl 5.26 re-rebuild of bootstrapped packages

* Wed Jun 07 2017 Richard W.M. Jones <rjones@redhat.com> - 1.7.3-33
- Rebuild against ocamlfind 1.7.3.

* Sun Jun 04 2017 Jitka Plesnikova <jplesnik@redhat.com> - 1.7.3-32
- Perl 5.26 rebuild

* Mon May 22 2017 Jitka Plesnikova <jplesnik@redhat.com> - 1.7.3-31
- Fix unescaped left brace in regex

* Sat May 13 2017 Richard W.M. Jones <rjones@redhat.com> - 1.7.3-30
- OCaml 4.04.1 rebuild.

* Tue Feb 14 2017 Richard W.M. Jones <rjones@redhat.com> - 1.7.3-29
- Fix compilation with GCC 7.

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.3-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Nov 07 2016 Richard W.M. Jones <rjones@redhat.com> - 1.7.3-27
- Rebuild for OCaml 4.04.0.
- Add explicit dependency on ocamlbuild.

* Wed Oct 19 2016 Dan Horák <dan[at]danny.cz> - 1.7.3-26
- disable debuginfo subpackage on interpreted builds

* Tue May 17 2016 Jitka Plesnikova <jplesnik@redhat.com> - 1.7.3-25
- Perl 5.24 rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.3-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Jul 28 2015 Richard W.M. Jones <rjones@redhat.com> - 1.7.3-23
- OCaml 4.02.3 rebuild.

* Mon Jul 20 2015 Richard W.M. Jones <rjones@redhat.com> 1.7.3-22
- Add patch for bytecode compilation, and enable on all arches.

* Mon Jun 29 2015 Peter Robinson <pbrobinson@fedoraproject.org> 1.7.3-21
- Build on ARMv7 (rhbz 994968) as it seems to now be fixed

* Wed Jun 24 2015 Richard W.M. Jones <rjones@redhat.com> - 1.7.3-20
- ocaml-4.02.2 final rebuild.

* Thu Jun 18 2015 Richard W.M. Jones <rjones@redhat.com> - 1.7.3-19
- ocaml-4.02.2 rebuild.

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.7.3-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 06 2015 Jitka Plesnikova <jplesnik@redhat.com> - 1.7.3-17
- Perl 5.22 rebuild

* Tue Feb 17 2015 Richard W.M. Jones <rjones@redhat.com> - 1.7.3-16
- ocaml-4.02.1 rebuild.
- Make test suite advisory.  Even upstream it does not work fully.

* Wed Sep 03 2014 Jitka Plesnikova <jplesnik@redhat.com> - 1.7.3-14
- Perl 5.20 rebuild

* Sun Aug 31 2014 Richard W.M. Jones <rjones@redhat.com> - 1.7.3-13
- ocaml-4.02.0 final rebuild.

* Thu Aug 28 2014 Jitka Plesnikova <jplesnik@redhat.com> - 1.7.3-12
- Perl 5.20 rebuild

* Sat Aug 23 2014 Richard W.M. Jones <rjones@redhat.com> - 1.7.3-11
- ocaml-4.02.0+rc1 rebuild.

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.7.3-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Aug 02 2014 Richard W.M. Jones <rjones@redhat.com> - 1.7.3-9
- ocaml-4.02.0-0.8.git10e45753.fc22 rebuild.

* Mon Jul 21 2014 Richard W.M. Jones <rjones@redhat.com> - 1.7.3-8
- OCaml 4.02.0 beta rebuild.
- Add patch from upstream to fix hang during build on 4.02.0.

* Thu Jun 19 2014 Richard W.M. Jones <rjones@redhat.com> - 1.7.3-6
- Fix Perl broken dependencies.

* Thu Jun 12 2014 Richard W.M. Jones <rjones@redhat.com> - 1.7.3-5
- Bump and rebuild to attempt to fix broken dependencies.

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.7.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Sep 14 2013 Richard W.M. Jones <rjones@redhat.com> - 1.7.3-3
- Rebuild for OCaml 4.01.0.
- Enable debuginfo.

* Tue Sep  3 2013 Richard W.M. Jones <rjones@redhat.com> - 1.7.3-2
- ExcludeArch armv7hl (RHBZ#994968).

* Fri Aug 30 2013 Gabriel Kerneis <gabriel@kerneis.info> - 1.7.3-1
- New upstream version 1.7.3.
- Use upstream make install target.
- Build and install documentation.
- Run test suite.
- Fix perl-related Provides and Requires for -cilly.
- Enable on arm and ppc (fixed by upstream ./configure).
- Apply two upstream patches to test suite.

* Sun Aug  4 2013 Richard W.M. Jones <rjones@redhat.com> - 1.4.0-10
- Disable on arm (not supported by upstream ./configure).
- Modernize the spec file.

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Jul 17 2013 Petr Pisar <ppisar@redhat.com> - 1.4.0-8
- Perl 5.18 rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sun Dec 02 2012 Bruno Wolff III <bruno@wolff.to> - 1.4.0-6
- Rebuild for ocaml 4.0.1.

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jun 28 2012 Petr Pisar <ppisar@redhat.com> - 1.4.0-4
- Perl 5.16 rebuild

* Sun Jun 10 2012 Richard W.M. Jones <rjones@redhat.com> - 1.4.0-3
- Rebuild for OCaml 4.00.0.

* Thu Jun 07 2012 Petr Pisar <ppisar@redhat.com> - 1.4.0-2
- Perl 5.16 rebuild
- Specify all Perl dependencies

* Fri Jan  6 2012 Richard W.M. Jones <rjones@redhat.com> - 1.4.0-1
- New upstream version 1.4.0.
- Rebuild for OCaml 3.12.1.

* Mon Jun 20 2011 Marcela Mašláňová <mmaslano@redhat.com> - 1.3.7-10
- Perl mass rebuild

* Thu Jun 09 2011 Marcela Mašláňová <mmaslano@redhat.com> - 1.3.7-9
- Perl 5.14 mass rebuild

* Fri Jan 07 2011 Richard W.M. Jones <rjones@redhat.com> - 1.3.7-8
- Rebuild for OCaml 3.12 (http://fedoraproject.org/wiki/Features/OCaml3.12).
- Patch: Remove '-lstr' option.
- Move configure into %%build section.

* Tue Jun 01 2010 Marcela Maslanova <mmaslano@redhat.com> - 1.3.7-6
- Mass rebuild with perl-5.12.0

* Wed Dec 30 2009 Richard W.M. Jones <rjones@redhat.com> - 1.3.7-5
- Rebuild for OCaml 3.11.2.

* Mon Dec  7 2009 Stepan Kasal <skasal@redhat.com> - 1.3.7-4
- rebuild against perl 5.10.1

* Fri Oct 23 2009 Richard W.M. Jones <rjones@redhat.com> - 1.3.7-3
- Include natively compiled files and *.mli files (RHBZ#521324).

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue May 26 2009 Richard W.M. Jones <rjones@redhat.com> - 1.3.7-1
- New upstream version 1.3.7.
- Rebuild for OCaml 3.11.1.

* Thu Apr 16 2009 S390x secondary arch maintainer <fedora-s390x@lists.fedoraproject.org>
- ExcludeArch sparc64, s390, s390x as we don't have OCaml on those archs
  (added sparc64 per request from the sparc maintainer)

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.6-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Wed Jan 21 2009 Richard W.M. Jones <rjones@redhat.com> - 1.3.6-10
- Fix prelink configuration file.

* Fri Dec  5 2008 Richard W.M. Jones <rjones@redhat.com> - 1.3.6-9
- Patch to fix stricter -output-obj checks in OCaml 3.11.0.

* Wed Nov 19 2008 Richard W.M. Jones <rjones@redhat.com> - 1.3.6-8
- Rebuild for OCaml 3.11.0

* Tue Sep  2 2008 Richard W.M. Jones <rjones@redhat.com> - 1.3.6-7
- Prevent unwanted bytecode stripping by RPM and prelink.
- Place *.ml files into the -devel subpackage.

* Mon Jul  7 2008 Richard W.M. Jones <rjones@redhat.com> - 1.3.6-6
- Fix Perl paths (rhbz#453759).

* Wed Apr 23 2008 Richard W.M. Jones <rjones@redhat.com> - 1.3.6-5
- Rebuild for OCaml 3.10.2

* Wed Nov  7 2007 Richard W.M. Jones <rjones@redhat.com> - 1.3.6-4
- ExcludeArch ppc - CIL doesn't build on PPC as it turns out.

* Wed Nov  7 2007 Richard W.M. Jones <rjones@redhat.com> - 1.3.6-3
- Change upstream URL.
- perl(CilConfig) set to package version
- Split out documentation into a separate -doc package.

* Mon Aug 20 2007 Richard W.M. Jones <rjones@redhat.com> - 1.3.6-2
- Initial RPM release.
