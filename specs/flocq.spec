# Coq's plugin architecture requires cmxs files, so:
ExclusiveArch: %{ocaml_native_compiler}

# This package is installed into an archful location, but contains no ELF
# objects.
%global debug_package %{nil}

%global flocqdir %{ocamldir}/coq/user-contrib/Flocq
%global coqver  8.20.0
%global commit  c85132b8b2a97bf18ad13f34a67688f2dddf0bfe
%global giturl  https://gitlab.inria.fr/flocq/flocq

Name:           flocq
Version:        4.2.0
Release:        3%{?dist}
Summary:        Formalization of floating point numbers for Coq

License:        LGPL-3.0-or-later
URL:            https://flocq.gitlabpages.inria.fr/
VCS:            git:%{giturl}.git
Source:         %{giturl}/-/archive/%{name}-%{version}/%{name}-%{version}.tar.gz

BuildRequires:  autoconf
BuildRequires:  gcc-c++
BuildRequires:  remake
BuildRequires:  coq = %{coqver}
BuildRequires:  ocaml
BuildRequires:  ocaml-findlib
Requires:       coq%{?_isa} = %{coqver}

%description
Flocq (Floats for Coq) is a floating-point formalization for the Coq
system.  It provides a comprehensive library of theorems on a
multi-radix multi-precision arithmetic.  It also supports efficient
numerical computations inside Coq.

%package source
Summary:        Source Coq files
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description source
This package contains the source Coq files for flocq.  These files are
not needed to use flocq.  They are made available for informational
purposes.

%prep
%autosetup -n %{name}-%{name}-%{version}-%{commit}

# Point to the local coqdoc files
sed -i 's,\(--coqlib \)[^[:blank:]]*,\1%{ocamldir}/coq,' Remakefile.in

# Generate the configure script
autoconf -f

%build
# We do NOT want to specify --libdir, and we don't need CFLAGS, etc.
./configure

# Use the system remake
rm -f remake
ln -s %{_bindir}/remake remake

# Workaround for a stack overflow compiling one file on ppc64le when
# using OCaml 5.2.  I observed this only happens with coqc, not with
# coqc.byte, so use coqc.byte for this one file.
#
# File "./src/Core/Digits.v", line 948, characters 0-4:
# Error: Stack overflow.
# Failed to build src/Core/Digits.vo
%ifarch %{power64}
remake -d %{?_smp_mflags} all ||: ;# expected to fail
coqc.byte -q -R src Flocq src/Core/Digits.v
%endif

remake -d %{?_smp_mflags} all doc

%install
sed -i "s,%{_libdir},$RPM_BUILD_ROOT%{_libdir}," Remakefile
remake install

# Also install the source files
cp -p src/*.v $RPM_BUILD_ROOT%{flocqdir}
cp -p src/Calc/*.v $RPM_BUILD_ROOT%{flocqdir}/Calc
cp -p src/Core/*.v $RPM_BUILD_ROOT%{flocqdir}/Core
cp -p src/IEEE754/*.v $RPM_BUILD_ROOT%{flocqdir}/IEEE754
cp -p src/Pff/*.v $RPM_BUILD_ROOT%{flocqdir}/Pff
cp -p src/Prop/*.v $RPM_BUILD_ROOT%{flocqdir}/Prop

%files
%doc AUTHORS NEWS.md README.md html
%license COPYING
%{flocqdir}
%exclude %{flocqdir}/*.v
%exclude %{flocqdir}/*/*.v

%files source
%{flocqdir}/*.v
%{flocqdir}/Calc/*.v
%{flocqdir}/Core/*.v
%{flocqdir}/IEEE754/*.v
%{flocqdir}/Pff/*.v
%{flocqdir}/Prop/*.v

%changelog
* Fri Jan 10 2025 Jerry James <loganjerry@gmail.com> - 4.2.0-3
- OCaml 5.3.0 rebuild for Fedora 42

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Tue Jul 16 2024 Jerry James <loganjerry@gmail.com> - 4.2.0-1
- Version 4.2.0

* Wed Jun 19 2024 Richard W.M. Jones <rjones@redhat.com> - 4.1.4-3
- OCaml 5.2.0 ppc64le fix

* Wed May 29 2024 Richard W.M. Jones <rjones@redhat.com> - 4.1.4-2
- OCaml 5.2.0 for Fedora 41

* Fri Feb  2 2024 Jerry James <loganjerry@gmail.com> - 4.1.4-1
- Version 4.1.4

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Tue Jan  2 2024 Jerry James <loganjerry@gmail.com> - 4.1.3-1
- Version 4.1.3

* Mon Dec 18 2023 Richard W.M. Jones <rjones@redhat.com> - 4.1.1-8
- OCaml 5.1.1 + s390x code gen fix for Fedora 40

* Tue Dec 12 2023 Richard W.M. Jones <rjones@redhat.com> - 4.1.1-7
- OCaml 5.1.1 rebuild for Fedora 40

* Thu Oct 05 2023 Richard W.M. Jones <rjones@redhat.com> - 4.1.1-6
- OCaml 5.1 rebuild for Fedora 40

* Thu Jul 27 2023 Jerry James <loganjerry@gmail.com> - 4.1.1-5
- Rebuild for ocaml-zarith 1.13

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Jul 12 2023 Richard W.M. Jones <rjones@redhat.com> - 4.1.1-3
- OCaml 5.0 rebuild for Fedora 39

* Mon Jul 10 2023 Jerry James <loganjerry@gmail.com> - 4.1.1-2
- OCaml 5.0.0 rebuild

* Sat Apr  1 2023 Jerry James <loganjerry@gmail.com> - 4.1.1-1
- Version 4.1.1

* Tue Jan 24 2023 Richard W.M. Jones <rjones@redhat.com> - 4.1.0-5
- Bump release and rebuild

* Tue Jan 24 2023 Richard W.M. Jones <rjones@redhat.com> - 4.1.0-4
- Rebuild OCaml packages for F38

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Nov 26 2022 Jerry James <loganjerry@gmail.com> - 4.1.0-2
- Rebuild for coq 8.16.1

* Fri Sep 16 2022 Jerry James <loganjerry@gmail.com> - 4.1.0-1
- Version 4.1.0

* Thu Aug 18 2022 Jerry James <loganjerry@gmail.com> - 3.4.3-5
- Rebuild to fix coq dependency
- Convert License tag to SPDX

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue Jul 19 2022 Jerry James <loganjerry@gmail.com> - 3.4.3-3
- Remove i686 support
- Use new OCaml macros

* Sun Jun 19 2022 Richard W.M. Jones <rjones@redhat.com> - 3.4.3-3
- OCaml 4.14.0 rebuild

* Fri Mar 25 2022 Jerry James <loganjerry@gmail.com> - 3.4.3-2
- Rebuild for coq 8.15.1

* Mon Feb 28 2022 Jerry James <loganjerry@gmail.com> - 3.4.3-1
- Version 3.4.3
- Use local coqdoc files

* Fri Feb 04 2022 Richard W.M. Jones <rjones@redhat.com> - 3.4.2-10
- OCaml 4.13.1 rebuild to remove package notes

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Mon Jan  3 2022 Jerry James <loganjerry@gmail.com> - 3.4.2-8
- Rebuild due to rebuilt coq

* Tue Nov 30 2021 Jerry James <loganjerry@gmail.com> - 3.4.2-7
- Rebuild for coq 8.14.1

* Thu Oct 21 2021 Jerry James <loganjerry@gmail.com> - 3.4.2-6
- Rebuild for coq 8.14.0
- New URLs

* Tue Oct 05 2021 Richard W.M. Jones <rjones@redhat.com> - 3.4.2-5
- OCaml 4.13.1 build

* Mon Oct 04 2021 Richard W.M. Jones <rjones@redhat.com> - 3.4.2-4
- Try to build on s390x with OCaml 4.13

* Fri Jul 30 2021 Jerry James <loganjerry@gmail.com> - 3.4.2-2
- Rebuild for rebuilt coq

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jul 14 2021 Jerry James <loganjerry@gmail.com> - 3.4.2-1
- Version 3.4.2

* Tue Jun  8 2021 Jerry James <loganjerry@gmail.com> - 3.4.0-6
- Rebuild for coq 8.13.2

* Wed Mar  3 2021 Jerry James <loganjerry@gmail.com> - 3.4.0-5
- Rebuild for coq 8.13.1 and ocaml-zarith 1.12

* Tue Mar  2 11:03:43 GMT 2021 Richard W.M. Jones <rjones@redhat.com> - 3.4.0-4
- OCaml 4.12.0 build

* Sat Feb 20 2021 Jerry James <loganjerry@gmail.com> - 3.4.0-3
- Rebuild for coq 8.13.0
- Use native compilation when available

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Jan  1 2021 Jerry James <loganjerry@gmail.com> - 3.4.0-1
- Version 3.4.0

* Wed Dec 23 2020 Jerry James <loganjerry@gmail.com> - 3.3.1-9
- Rebuild for coq 8.12.2

* Wed Dec  2 2020 Jerry James <loganjerry@gmail.com> - 3.3.1-8
- Rebuild for coq 8.12.1

* Fri Sep 25 2020 Jerry James <loganjerry@gmail.com> - 3.3.1-7
- Flocq is installed in an archful directory, so cannot be noarch
- ExcludeArch s390x due to bz 1874879

* Wed Sep 02 2020 Richard W.M. Jones <rjones@redhat.com> - 3.3.1-6
- OCaml 4.11.1 rebuild

* Tue Sep  1 2020 Jerry James <loganjerry@gmail.com> - 3.3.1-5
- Rebuild for coq 8.12.0
- Revert to a noarch package

* Sat Aug 22 2020 Richard W.M. Jones <rjones@redhat.com> - 3.3.1-5
- OCaml 4.11.0 rebuild

* Thu Aug  6 2020 Jerry James <loganjerry@gmail.com> - 3.3.1-4
- Rebuild to fix OCaml dependencies

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jun 15 2020 Jerry James <loganjerry@gmail.com> - 3.3.1-2
- Rebuild for coq 8.11.2

* Sat Jun 13 2020 Jerry James <loganjerry@gmail.com> - 3.3.1-1
- Version 3.3.1

* Wed May 20 2020 Jerry James <loganjerry@gmail.com> - 3.2.1-3
- Rebuild for coq 8.11.1

* Tue May 05 2020 Richard W.M. Jones <rjones@redhat.com> - 3.2.1-2
- OCaml 4.11.0+dev2-2020-04-22 rebuild

* Wed Apr  8 2020 Jerry James <loganjerry@gmail.com> - 3.2.1-1
- Version 3.2.1
- Drop -coq811 patch in favor of upstream's solution

* Sat Apr 04 2020 Richard W.M. Jones <rjones@redhat.com> - 3.2.0-8
- Update all OCaml dependencies for RPM 4.16.

* Mon Mar 30 2020 Jerry James <loganjerry@gmail.com> - 3.2.0-7
- Add -coq811 patch so gappalib-coq can be built with coq 8.11

* Mon Mar 23 2020 Jerry James <loganjerry@gmail.com> - 3.2.0-6
- Rebuild for coq 8.11.0

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jan 22 2020 Jerry James <loganjerry@gmail.com> - 3.2.0-4
- OCaml 4.10.0+beta1 rebuild.

* Fri Dec 06 2019 Richard W.M. Jones <rjones@redhat.com> - 3.2.0-3
- OCaml 4.09.0 (final) rebuild.

* Fri Sep  6 2019 Jerry James <loganjerry@gmail.com> - 3.2.0-2
- OCaml 4.08.1 (final) rebuild.

* Thu Aug  1 2019 Jerry James <loganjerry@gmail.com> - 3.2.0-1
- New upstream release

* Wed Jul 31 2019 Richard W.M. Jones <rjones@redhat.com> - 3.1.0-3
- OCaml 4.08.1 (rc2) rebuild.

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Jun  5 2019 Jerry James <loganjerry@gmail.com> - 3.1.0-1
- New upstream release

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jan 26 2019 Jerry James <loganjerry@gmail.com> - 3.0.0-1
- New upstream release

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Jul 11 2018 Richard W.M. Jones <rjones@redhat.com> - 2.6.0-8
- OCaml 4.07.0 (final) rebuild.

* Wed Jun 20 2018 Richard W.M. Jones <rjones@redhat.com> - 2.6.0-7
- OCaml 4.07.0-rc1 rebuild.

* Mon Feb 12 2018 Jerry James <loganjerry@gmail.com> - 2.6.0-6
- Rebuild for coq 8.7.1

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Nov 17 2017 Richard W.M. Jones <rjones@redhat.com> - 2.6.0-4
- Rebuild against new Coq package.

* Wed Nov 08 2017 Richard W.M. Jones <rjones@redhat.com> - 2.6.0-3
- Bump release and rebuild.

* Wed Nov 08 2017 Richard W.M. Jones <rjones@redhat.com> - 2.6.0-2
- OCaml 4.06.0 rebuild.

* Thu Oct  5 2017 Jerry James <loganjerry@gmail.com> - 2.6.0-1
- New upstream release

* Wed Sep 06 2017 Richard W.M. Jones <rjones@redhat.com> - 2.5.2-12
- OCaml 4.05.0 rebuild.

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.2-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jun 26 2017 Richard W.M. Jones <rjones@redhat.com> - 2.5.2-9
- Bump release and rebuild.

* Mon Jun 26 2017 Richard W.M. Jones <rjones@redhat.com> - 2.5.2-8
- OCaml 4.04.2 rebuild.

* Fri May 12 2017 Richard W.M. Jones <rjones@redhat.com> - 2.5.2-7
- OCaml 4.04.1 rebuild.

* Fri Mar 24 2017 Jerry James <loganjerry@gmail.com> - 2.5.2-6
- Rebuild to fix coq consistency issue

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Jan 12 2017 Jerry James <loganjerry@gmail.com> - 2.5.2-4
- Rebuild for coq 8.6

* Mon Nov 07 2016 Richard W.M. Jones <rjones@redhat.com> - 2.5.2-3
- Rebuild for OCaml 4.04.0.

* Fri Oct 28 2016 Jerry James <loganjerry@gmail.com> - 2.5.2-2
- Rebuild for coq 8.5pl3

* Thu Sep 29 2016 Jerry James <loganjerry@gmail.com> - 2.5.2-1
- New upstream release

* Wed Jul 13 2016 Jerry James <loganjerry@gmail.com> - 2.5.1-3
- Rebuild for coq 8.5pl2

* Fri Apr 22 2016 Jerry James <loganjerry@gmail.com> - 2.5.1-2
- Rebuild for coq 8.5pl1

* Fri Feb 12 2016 Jerry James <loganjerry@gmail.com> - 2.5.1-1
- New upstream release

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Oct 14 2015 Jerry James <loganjerry@gmail.com> - 2.5.0-1
- New upstream release

* Wed Jun 24 2015 Richard W.M. Jones <rjones@redhat.com> - 2.4.0-10
- ocaml-4.02.2 final rebuild.

* Wed Jun 17 2015 Richard W.M. Jones <rjones@redhat.com> - 2.4.0-9
- ocaml-4.02.2 rebuild.

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Apr 11 2015 Jerry James <loganjerry@gmail.com> - 2.4.0-7
- Rebuild for coq 8.4pl6

* Tue Feb 17 2015 Richard W.M. Jones <rjones@redhat.com> - 2.4.0-6
- Bump release and rebuild.

* Mon Feb 16 2015 Richard W.M. Jones <rjones@redhat.com> - 2.4.0-5
- Bump release and rebuild.

* Mon Feb 16 2015 Richard W.M. Jones <rjones@redhat.com> - 2.4.0-4
- ocaml-4.02.1 rebuild.

* Thu Nov  6 2014 Jerry James <loganjerry@gmail.com> - 2.4.0-3
- Rebuild with coq that was rebuilt with ocaml-camlp5 6.12

* Thu Oct 30 2014 Jerry James <loganjerry@gmail.com> - 2.4.0-2
- Rebuild for coq 8.4pl5

* Tue Sep  2 2014 Jerry James <loganjerry@gmail.com> - 2.4.0-1
- New upstream release

* Sun Aug 31 2014 Richard W.M. Jones <rjones@redhat.com> - 2.3.0-9
- ocaml-4.02.0 final rebuild.

* Sun Aug 24 2014 Richard W.M. Jones <rjones@redhat.com> - 2.3.0-8
- Bump release and rebuild.

* Sun Aug 24 2014 Richard W.M. Jones <rjones@redhat.com> - 2.3.0-7
- ocaml-4.02.0+rc1 rebuild.

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Fri Aug 08 2014 Richard W.M. Jones <rjones@redhat.com> - 2.3.0-5
- ocaml-4.02.0-0.8.git10e45753.fc22 rebuild.

* Mon Aug  4 2014 Jerry James <loganjerry@gmail.com> - 2.3.0-4
- Bump and rebuild as part of ocaml rebuild
- Fix license handling

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue May 13 2014 Jerry James <loganjerry@gmail.com> - 2.3.0-2
- Rebuild for coq 8.4pl4

* Mon Apr 21 2014 Jerry James <loganjerry@gmail.com> - 2.3.0-1
- New upstream release
- Remove ocaml_arches macro (bz 1087794)

* Mon Jan 27 2014 Jerry James <loganjerry@gmail.com> - 2.2.2-1
- New upstream release

* Wed Dec 18 2013 Jerry James <loganjerry@gmail.com> - 2.2.0-2
- Rebuild for coq 8.4pl3

* Sat Aug 10 2013 Jerry James <loganjerry@gmail.com> - 2.2.0-1
- New upstream release
- Builds now done with remake instead of make

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue May 14 2013 Jerry James <loganjerry@gmail.com> - 2.1.0-5
- Rebuild for coq 8.4pl2

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Mon Jan  7 2013 Jerry James <loganjerry@gmail.com> - 2.1.0-3
- Rebuild for coq 8.4pl1

* Tue Aug 21 2012 Jerry James <loganjerry@gmail.com> - 2.1.0-2
- Rebuild for coq 8.4

* Sat Jul 28 2012 Jerry James <loganjerry@gmail.com> - 2.1.0-1
- New upstream release
- Build for OCaml 4.0.0 and coq 8.3pl4

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan  7 2012 Jerry James <loganjerry@gmail.com> - 2.0.0-3
- Rebuild for OCaml 3.12.1

* Tue Dec 27 2011 Jerry James <loganjerry@gmail.com> - 2.0.0-2
- Rebuild for coq 8.3pl3

* Mon Dec 12 2011 Jerry James <loganjerry@gmail.com> - 2.0.0-1
- New upstream release
- Change subpackage from -devel to -source to match gappalib-coq.

* Fri Oct 28 2011 Jerry James <loganjerry@gmail.com> - 1.4.0-3
- Fix broken version numbers in BR and Requires

* Wed Oct 26 2011 Jerry James <loganjerry@gmail.com> - 1.4.0-2
- Split out a -devel subpackage

* Tue Jul  5 2011 Jerry James <loganjerry@gmail.com> - 1.4.0-1
- Initial RPM
