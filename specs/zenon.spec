# Coq's plugin architecture requires cmxs files, so:
ExclusiveArch: %{ocaml_native_compiler}

%ifnarch %{ocaml_native_compiler}
%global debug_package %{nil}
%endif
%global coqver  8.20.0
%global giturl  https://github.com/zenon-prover/zenon

Name:		zenon
Version:	0.8.5
Release:	30%{?dist}
Summary:	Automated theorem prover for first-order classical logic
License:	BSD-3-Clause
URL:		http://zenon-prover.org/
VCS:		git:%{giturl}.git
Source0:	%{giturl}/archive/%{version}/%{name}-%{version}.tar.gz
Source1:	http://zenon-prover.org/zenlpar07.pdf
Source2:	%{name}-tptp-COM003+2.p
Source3:	%{name}-tptp-ReadMe
# Basic documentation (man pages). Submitted upstream 2008-07-25:
Source4:	%{name}.1
Source5:	%{name}-format.5

BuildRequires:	coq = %{coqver}
BuildRequires:	ghostscript
BuildRequires:	ImageMagick
BuildRequires:	make
BuildRequires:	ocaml

Requires:	coq%{?_isa} = %{coqver}
Requires:	coreutils

%description
Zenon is an automated theorem prover for first order classical logic
with equality, based on the tableau method.  Zenon can read input files
in TPTP, Coq, Focal, and its own Zenon format.  Zenon can directly
generate Coq proofs (proof scripts or proof terms), which can be
reinserted into Coq specifications.  Zenon can also be extended.

%prep
%autosetup

cp -p %{SOURCE1} .

# Generate debuginfo
sed -i 's/^\(CAMLFLAGS = \).*/\1-g/' Makefile

%build
./configure -prefix %{_prefix} -libdir %{_datadir}/%{name} -sum md5sum

mkdir examples
cp -p %{SOURCE2} examples/tptp-COM003+2.p
cp -p %{SOURCE3} examples/tptp-ReadMe

# Work around Makefile errors (fails if no ocamlopt, uses _bytecode_ otherwise)
%ifarch %{ocaml_native_compiler}
  make %{?_smp_mflags} zenon.bin
  cp -p zenon.bin zenon
%else
  make %{?_smp_mflags} zenon.byt
  cp -p zenon.byt zenon
%endif
# Use of %%{?_smp_mflags} sometimes leads to build failures
make coq

%install
%make_install

install -d %{buildroot}%{_mandir}/man1/
install -d %{buildroot}%{_mandir}/man5/
cp -p %{SOURCE4} %{buildroot}%{_mandir}/man1/
cp -p %{SOURCE5} %{buildroot}%{_mandir}/man5/

# Put the coq files where coq can find them
mkdir -p %{buildroot}%{_libdir}/coq/user-contrib
mv %{buildroot}%{_datadir}/%{name} %{buildroot}%{_libdir}/coq/user-contrib/Zenon

%check
# Sanity test. Can we prove TPTP v3.4.2 test COM003+2 (the halting problem)?
# tptp-ReadMe has test's license conditions ("must credit + note changes").
# TPTP from: http://www.cs.miami.edu/~tptp/TPTP/Distribution/TPTP-v3.4.2.tgz
result=`./zenon -p0 -itptp examples/tptp-COM003+2.p`
if [ "$result" = "(* PROOF-FOUND *)" ] ; then
 echo "Test succeeded"
else
 echo "TEST FAILED"
 false
fi

%files
%doc zenlpar07.pdf examples
%license LICENSE
%{_bindir}/%{name}
%{_libdir}/coq/user-contrib/Zenon
%{_mandir}/man1/zenon.1*
%{_mandir}/man5/zenon-format.5*

%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.5-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jan 10 2025 Jerry James <loganjerry@gmail.com> - 0.8.5-29
- OCaml 5.3.0 rebuild for Fedora 42

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.5-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jun 19 2024 Richard W.M. Jones <rjones@redhat.com> - 0.8.5-27
- OCaml 5.2.0 ppc64le fix

* Wed May 29 2024 Richard W.M. Jones <rjones@redhat.com> - 0.8.5-26
- OCaml 5.2.0 for Fedora 41

* Fri Feb  2 2024 Jerry James <loganjerry@gmail.com> - 0.8.5-25
- Rebuild for rebuilt coq

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.5-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Tue Jan  2 2024 Jerry James <loganjerry@gmail.com> - 0.8.5-23
- Rebuild for coq 8.18.0

* Mon Dec 18 2023 Richard W.M. Jones <rjones@redhat.com> - 0.8.5-22
- OCaml 5.1.1 + s390x code gen fix for Fedora 40

* Tue Dec 12 2023 Richard W.M. Jones <rjones@redhat.com> - 0.8.5-21
- OCaml 5.1.1 rebuild for Fedora 40

* Thu Oct 05 2023 Richard W.M. Jones <rjones@redhat.com> - 0.8.5-20
- OCaml 5.1 rebuild for Fedora 40

* Thu Jul 27 2023 Jerry James <loganjerry@gmail.com> - 0.8.5-19
- Rebuild for ocaml-zarith 1.13

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.5-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Jul 12 2023 Richard W.M. Jones <rjones@redhat.com> - 0.8.5-17
- OCaml 5.0 rebuild for Fedora 39

* Mon Jul 10 2023 Jerry James <loganjerry@gmail.com> - 0.8.5-16
- OCaml 5.0.0 rebuild

* Sat Apr  1 2023 Jerry James <loganjerry@gmail.com> - 0.8.5-15
- Rebuild for coq 8.17.0

* Tue Jan 24 2023 Richard W.M. Jones <rjones@redhat.com> - 0.8.5-14
- Bump release and rebuild

* Tue Jan 24 2023 Richard W.M. Jones <rjones@redhat.com> - 0.8.5-13
- Rebuild OCaml packages for F38

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.5-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Nov 26 2022 Jerry James <loganjerry@gmail.com> - 0.8.5-11
- Rebuild for coq 8.16.1

* Fri Sep 16 2022 Jerry James <loganjerry@gmail.com> - 0.8.5-10
- Rebuild for coq 8.16.0

* Thu Aug 18 2022 Jerry James <loganjerry@gmail.com> - 0.8.5-9
- Rebuild to fix coq dependency
- Convert License tag to SPDX

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.5-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jul 20 2022 Jerry James <loganjerry@gmail.com> - 0.8.5-7
- Remove i686 support

* Sun Jun 19 2022 Richard W.M. Jones <rjones@redhat.com> - 0.8.5-7
- OCaml 4.14.0 rebuild

* Fri Mar 25 2022 Jerry James <loganjerry@gmail.com> - 0.8.5-6
- Rebuild for coq 8.15.1

* Mon Feb 28 2022 Jerry James <loganjerry@gmail.com> - 0.8.5-5
- Rebuild for coq 8.15.0

* Fri Feb 04 2022 Richard W.M. Jones <rjones@redhat.com> - 0.8.5-4
- OCaml 4.13.1 rebuild to remove package notes

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Nov 30 2021 Jerry James <loganjerry@gmail.com> - 0.8.5-2
- Rebuild for coq 8.14.1

* Thu Oct 21 2021 Jerry James <loganjerry@gmail.com> - 0.8.5-1
- Version 0.8.5
- Drop upstreamed -coq89 and -ocaml patches

* Tue Oct 05 2021 Richard W.M. Jones <rjones@redhat.com> - 0.8.4-27
- OCaml 4.13.1 build

* Mon Oct 04 2021 Richard W.M. Jones <rjones@redhat.com> - 0.8.4-26
- Try to build on s390x with OCaml 4.13

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.4-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jun  8 2021 Jerry James <loganjerry@gmail.com> - 0.8.4-24
- Rebuild for coq 8.13.2

* Wed Mar  3 2021 Jerry James <loganjerry@gmail.com> - 0.8.4-23
- Rebuild for coq 8.13.1

* Tue Mar  2 11:03:37 GMT 2021 Richard W.M. Jones <rjones@redhat.com> - 0.8.4-22
- OCaml 4.12.0 build

* Sat Feb 20 2021 Jerry James <loganjerry@gmail.com> - 0.8.4-21
- Rebuild for coq 8.13.0

* Thu Jan 28 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.4-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Dec 23 2020 Jerry James <loganjerry@gmail.com> - 0.8.4-19
- Rebuild for coq 8.12.2

* Wed Dec  2 2020 Jerry James <loganjerry@gmail.com> - 0.8.4-18
- Rebuild for coq 8.12.1

* Wed Sep 02 2020 Richard W.M. Jones <rjones@redhat.com> - 0.8.4-17
- OCaml 4.11.1 rebuild

* Tue Sep  1 2020 Jerry James <loganjerry@gmail.com> - 0.8.4-16
- Rebuild for coq 8.12.0

* Sat Aug 22 2020 Richard W.M. Jones <rjones@redhat.com> - 0.8.4-16
- OCaml 4.11.0 rebuild

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.4-15
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.4-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jun 15 2020 Jerry James <loganjerry@gmail.com> - 0.8.4-13
- Rebuild for coq 8.11.2

* Wed May 20 2020 Jerry James <loganjerry@gmail.com> - 0.8.4-12
- Rebuild for coq 8.11.1

* Tue May 05 2020 Richard W.M. Jones <rjones@redhat.com> - 0.8.4-11
- OCaml 4.11.0+dev2-2020-04-22 rebuild

* Sat Apr 04 2020 Richard W.M. Jones <rjones@redhat.com> - 0.8.4-10
- Update all OCaml dependencies for RPM 4.16.

* Mon Mar 23 2020 Jerry James <loganjerry@gmail.com> - 0.8.4-9
- Rebuild for coq 8.11.0

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.4-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jan 22 2020 Jerry James <loganjerry@gmail.com> - 0.8.4-7
- OCaml 4.10.0+beta1 rebuild.

* Fri Sep  6 2019 Jerry James <loganjerry@gmail.com> - 0.8.4-6
- OCaml 4.08.1 (final) rebuild.

* Thu Aug  1 2019 Jerry James <loganjerry@gmail.com> - 0.8.4-5
- OCaml 4.08.1 (rc2) rebuild.

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Jun  5 2019 Jerry James <loganjerry@gmail.com> - 0.8.4-3
- Rebuild for coq 8.9.1
- Add -coq89 patch to adapt to coq 8.9.x

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jan 26 2019 Jerry James <loganjerry@gmail.com> - 0.8.4-1
- New upstream release
- Drop -unsafe-string workaround

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.2-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Feb 12 2018 Jerry James <loganjerry@gmail.com> - 0.8.2-11
- Rebuild for coq 8.7.1
- Compile with -unsafe-string until the code can be migrated

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Sep  6 2017 Jerry James <loganjerry@gmail.com> - 0.8.2-9
- Rebuild for coq 8.6.1

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Jan 12 2017 Jerry James <loganjerry@gmail.com> - 0.8.2-5
- Rebuild for coq 8.6

* Sat Nov 05 2016 Richard W.M. Jones <rjones@redhat.com> - 0.8.2-4
- Rebuild for OCaml 4.04.0.

* Fri Oct 28 2016 Jerry James <loganjerry@gmail.com> - 0.8.2-3
- Rebuild for coq 8.5pl3

* Wed Jul 13 2016 Jerry James <loganjerry@gmail.com> - 0.8.2-2
- Rebuild for coq 8.5pl2

* Fri Jun 10 2016 Jerry James <loganjerry@gmail.com> - 0.8.2-1
- New upstream release

* Wed Jun  1 2016 Jerry James <loganjerry@gmail.com> - 0.8.1-1
- New upstream release

* Fri Apr 22 2016 Jerry James <loganjerry@gmail.com> - 0.8.0-8
- Rebuild for coq 8.5pl1

* Fri Feb 12 2016 Jerry James <loganjerry@gmail.com> - 0.8.0-7
- Rebuild for coq 8.5

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Apr 11 2015 Jerry James <loganjerry@gmail.com> - 0.8.0-4
- Rebuild for coq 8.4pl6

* Wed Jan  7 2015 Jerry James <loganjerry@gmail.com> - 0.8.0-3
- Update URLs

* Thu Oct 30 2014 Jerry James <loganjerry@gmail.com> - 0.8.0-2
- Rebuild for coq 8.4pl5

* Thu Oct 23 2014 Jerry James <loganjerry@gmail.com> - 0.8.0-1
- New upstream release
- Sources for the icon are no longer provided
- Fix license handling

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.1-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Mon Jun 16 2014 Jerry James <loganjerry@gmail.com> - 0.7.1-13
- Drop bz 921706 workaround; now unnecessary

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue May 13 2014 Jerry James <loganjerry@gmail.com> - 0.7.1-11
- Rebuild for coq 8.4pl4
- Add workaround for bz 921706

* Fri Apr 18 2014 Jerry James <loganjerry@gmail.com> - 0.7.1-10
- Remove ocaml_arches macro (bz 1087794)

* Sat Dec 21 2013 Ville Skyttä <ville.skytta@iki.fi> - 0.7.1-9
- Pass -g to ocamlopt, don't strip executable too early.

* Wed Dec 18 2013 Jerry James <loganjerry@gmail.com> - 0.7.1-8
- Rebuild for coq 8.4pl3
- Enable debuginfo generation

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed May  8 2013 Jerry James <loganjerry@gmail.com> - 0.7.1-6
- Rebuild for coq 8.4pl2

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Mon Jan  7 2013 Jerry James <loganjerry@gmail.com> - 0.7.1-4
- Rebuild for coq 8.4pl1

* Thu Dec 13 2012 Jerry James <loganjerry@gmail.com> - 0.7.1-3
- Rebuild for OCaml 4.00.1

* Tue Aug 21 2012 Jerry James <loganjerry@gmail.com> - 0.7.1-2
- Rebuild for coq 8.4

* Mon Jul 30 2012 Jerry James <loganjerry@gmail.com> - 0.7.1-1
- New upstream release
- Install the coq files where coq can find them automatically

* Sun Jul 22 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Jan  9 2012 Jerry James <loganjerry@gmail.com> - 0.6.3-5
- Rebuild for OCaml 3.12.1

* Tue Dec 27 2011 Jerry James <loganjerry@gmail.com> - 0.6.3-4
- Rebuild for coq 8.3pl3

* Mon Nov 14 2011 Jerry James <loganjerry@gmail.com> - 0.6.3-3
- Change ExclusiveArch to %%{ocaml_arches}

* Thu Jul 14 2011 Jerry James <loganjerry@gmail.com> - 0.6.3-2
- Move the coq files back to /usr/share to avoid a dependency on coq
- Add paper describing zenon to %%doc

* Tue Jul 12 2011 Jerry James <loganjerry@gmail.com> - 0.6.3-1
- New upstream release
- Drop unnecessary spec file elements (BuildRoot, etc.)
- Execstack flag clearing no longer necessary
- Build on exactly the arches that coq builds on
- Build the icons

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Sep 22 2009 Dennis gilmore <dennis@ausil.us> - 0.5.0-7
- ExcludeArch sparc64  no ocaml

* Tue Aug 11 2009 Ville Skyttä <ville.skytta@iki.fi> - 0.5.0-6
- Use bzipped upstream tarball.

* Mon Jul 27 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.0-5.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon Jun 15 2009 Karsten Hopp <karsten@redhat.com> 0.5.0-4.1
- ocaml not available on mainframes, add excludearch

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Fri Jun 27 2008 David A. Wheeler - 0.5.0-3
- Add documentation for Zenon and its built-in format as man pages
  (man pages used so Debian, etc., will use them too)
- Fix release number so it increases everywhere

* Fri Jun 27 2008 David A. Wheeler - 0.5.0-2.1
- macro fc8 failed, minor rebuild for Fedora 8

* Fri Jun 27 2008 David A. Wheeler - 0.5.0-2
- Moved examples to an "examples" subdirectory in /usr/share/doc/NAME-VERSION
- Moved "check" to be after "install" in spec file (that's when it's executed)
- Exclude ppc64 for Fedora 8 (it works on 9 and 10, but not 8)

* Fri Jun 27 2008 David A. Wheeler - 0.5.0-1
- Initial package
