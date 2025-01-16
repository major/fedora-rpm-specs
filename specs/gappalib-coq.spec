# Coq's plugin architecture requires cmxs files, so:
ExclusiveArch: %{ocaml_native_compiler}

%ifnarch %{ocaml_native_compiler}
%global debug_package %{nil}
%endif

# TESTING NOTE: The testsuite requires that gappalib-coq be installed already.
# Hence, we cannot run it on the koji builders.  The maintainer should always
# install the package and run "remake check" manually before committing.

%global gappadir %{ocamldir}/coq/user-contrib/Gappa
%global coqver  8.20.0
%global commit  32cf6128ef2c57c3daee75945b46aa5ae2225b80
%global giturl  https://gitlab.inria.fr/gappa/coq

Name:           gappalib-coq
Version:        1.5.5
Release:        6%{?dist}
Summary:        Coq support library for gappa

License:        LGPL-3.0-or-later
URL:            https://gappa.gitlabpages.inria.fr/
VCS:            git:%{giturl}.git
Source:         %{giturl}/-/archive/%{name}-%{version}/%{name}-%{version}.tar.gz

BuildRequires:  autoconf
BuildRequires:  gcc-c++
BuildRequires:  coq = %{coqver}
BuildRequires:  flocq
BuildRequires:  gappa
BuildRequires:  ocaml
BuildRequires:  ocaml-findlib
BuildRequires:  ocaml-zarith-devel
BuildRequires:  remake

Requires:       coq%{?_isa} = %{coqver}
Requires:       flocq
Requires:       gappa

%description
This support library provides vernacular files so that the certificates
Gappa generates can be imported by the Coq proof assistant.  It also
provides a "gappa" tactic that calls Gappa on the current Coq goal.

Gappa (Génération Automatique de Preuves de Propriétés Arithmétiques --
automatic proof generation of arithmetic properties) is a tool intended
to help verifying and formally proving properties on numerical programs
dealing with floating-point or fixed-point arithmetic.

%package source
Summary:        Source Coq files
Requires:       %{name} = %{version}-%{release}

%description source
This package contains the source Coq files for gappalib-coq.  These
files are not needed to use gappalib-coq.  They are made available for
informational purposes.

%prep
%autosetup -n coq-%{name}-%{version}-%{commit}

%conf
# Enable debuginfo
sed -i 's/-rectypes/-g &/' Remakefile.in

# Generate the configure script
autoconf -f

%build
# The %%configure macro specifies --libdir, which this configure script
# unfortunately uses to identify where the Coq files should go.  We want
# the default (i.e., ask coq itself where they go).
./configure --prefix=%{_prefix} --datadir=%{_datadir}

# Use the system remake
rm -f remake
ln -s %{_bindir}/remake remake

remake -d %{?_smp_mflags}

%install
mkdir -p %{buildroot}%{gappadir}
DESTDIR=%{buildroot} remake install

# Also install the source files
cp -p src/*.v  %{buildroot}%{gappadir}

%check
remake check

%files
%doc AUTHORS NEWS.md README.md
%license COPYING
%{_libdir}/ocaml/coq-gappa/
%{gappadir}
%exclude %{gappadir}/*.v

%files source
%{gappadir}/*.v

%changelog
* Fri Jan 10 2025 Jerry James <loganjerry@gmail.com> - 1.5.5-6
- OCaml 5.3.0 rebuild for Fedora 42

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Tue Jul 16 2024 Jerry James <loganjerry@gmail.com> - 1.5.5-4
- Rebuild for ocaml-zarith 1.14

* Wed Jun 19 2024 Richard W.M. Jones <rjones@redhat.com> - 1.5.5-3
- OCaml 5.2.0 ppc64le fix

* Thu May 30 2024 Richard W.M. Jones <rjones@redhat.com> - 1.5.5-2
- OCaml 5.2.0 for Fedora 41

* Thu May 23 2024 Jerry James <loganjerry@gmail.com> - 1.5.5-1
- Version 1.5.5

* Fri Feb  2 2024 Jerry James <loganjerry@gmail.com> - 1.5.4-4
- Rebuild for flocq 4.1.4

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Tue Jan  2 2024 Jerry James <loganjerry@gmail.com> - 1.5.4-1
- Version 1.5.4

* Mon Dec 18 2023 Richard W.M. Jones <rjones@redhat.com> - 1.5.3-8
- OCaml 5.1.1 + s390x code gen fix for Fedora 40

* Tue Dec 12 2023 Richard W.M. Jones <rjones@redhat.com> - 1.5.3-7
- OCaml 5.1.1 rebuild for Fedora 40

* Thu Oct 05 2023 Richard W.M. Jones <rjones@redhat.com> - 1.5.3-6
- OCaml 5.1 rebuild for Fedora 40

* Tue Sep 12 2023 Jerry James <loganjerry@gmail.com> - 1.5.3-5
- Rebuild for coq 8.18.0

* Thu Jul 27 2023 Jerry James <loganjerry@gmail.com> - 1.5.3-4
- Rebuild for ocaml-zarith 1.13

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Mon Jul 10 2023 Jerry James <loganjerry@gmail.com> - 1.5.3-2
- OCaml 5.0.0 rebuild

* Sat Apr  1 2023 Jerry James <loganjerry@gmail.com> - 1.5.3-1
- Version 1.5.3

* Tue Jan 24 2023 Richard W.M. Jones <rjones@redhat.com> - 1.5.2-7
- Rebuild OCaml packages for F38

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Nov 26 2022 Jerry James <loganjerry@gmail.com> - 1.5.2-5
- Rebuild for coq 8.16.1

* Fri Sep 16 2022 Jerry James <loganjerry@gmail.com> - 1.5.2-4
- Rebuild for coq 8.16.0

* Thu Aug 18 2022 Jerry James <loganjerry@gmail.com> - 1.5.2-3
- Rebuild to fix coq dependency
- Change license to LGPL-3.0-or-later

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jul 20 2022 Jerry James <loganjerry@gmail.com> - 1.5.2-1
- Version 1.5.2

* Tue Jul 19 2022 Jerry James <loganjerry@gmail.com> - 1.5.1-3
- Remove i686 support
- Use new OCaml macros

* Sun Jun 19 2022 Richard W.M. Jones <rjones@redhat.com> - 1.5.1-3
- OCaml 4.14.0 rebuild

* Fri Mar 25 2022 Jerry James <loganjerry@gmail.com> - 1.5.1-2
- Rebuild for coq 8.15.1

* Mon Feb 28 2022 Jerry James <loganjerry@gmail.com> - 1.5.1-1
- Version 1.5.1

* Fri Feb 04 2022 Richard W.M. Jones <rjones@redhat.com> - 1.5.0-4
- OCaml 4.13.1 rebuild to remove package notes

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Nov 30 2021 Jerry James <loganjerry@gmail.com> - 1.5.0-2
- Rebuild for coq 8.14.1

* Thu Oct 21 2021 Jerry James <loganjerry@gmail.com> - 1.5.0-1
- Version 1.5.0

* Tue Oct 05 2021 Richard W.M. Jones <rjones@redhat.com> - 1.4.6-11
- OCaml 4.13.1 build

* Mon Oct 04 2021 Richard W.M. Jones <rjones@redhat.com> - 1.4.6-10
- Try to build on s390x with OCaml 4.13

* Fri Jul 30 2021 Jerry James <loganjerry@gmail.com> - 1.4.6-9
- Rebuild for rebuilt coq

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.6-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jul 14 2021 Jerry James <loganjerry@gmail.com> - 1.4.6-7
- Rebuild for flocq 3.4.2

* Tue Jun  8 2021 Jerry James <loganjerry@gmail.com> - 1.4.6-6
- Rebuild for coq 8.13.2

* Wed Mar  3 2021 Jerry James <loganjerry@gmail.com> - 1.4.6-5
- Rebuild for coq 8.13.1
- Build with ocaml-zarith instead of ocaml-num

* Tue Mar  2 11:18:07 GMT 2021 Richard W.M. Jones <rjones@redhat.com> - 1.4.6-4
- OCaml 4.12.0 build

* Sat Feb 20 2021 Jerry James <loganjerry@gmail.com> - 1.4.6-3
- Rebuild for coq 8.13.0

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jan  4 2021 Jerry James <loganjerry@gmail.com> - 1.4.6-1
- Version 1.4.6

* Sat Jan  2 2021 Jerry James <loganjerry@gmail.com> - 1.4.4-9
- Rebuild for flocq 3.4.0

* Wed Dec 23 2020 Jerry James <loganjerry@gmail.com> - 1.4.4-8
- Rebuild for coq 8.12.2

* Wed Dec  2 2020 Jerry James <loganjerry@gmail.com> - 1.4.4-7
- Rebuild for coq 8.12.1

* Fri Sep 25 2020 Jerry James <loganjerry@gmail.com> - 1.4.4-6
- Rebuild due to flocq rebuild
- The source subpackage cannot be noarch due to its install location

* Wed Sep 02 2020 Richard W.M. Jones <rjones@redhat.com> - 1.4.4-5
- OCaml 4.11.1 rebuild

* Tue Sep  1 2020 Jerry James <loganjerry@gmail.com> - 1.4.4-4
- Rebuild for coq 8.12.0
- Set BuildArch to noarch for the source subpackage

* Mon Aug 24 2020 Richard W.M. Jones <rjones@redhat.com> - 1.4.4-4
- OCaml 4.11.0 rebuild

* Thu Aug  6 2020 Jerry James <loganjerry@gmail.com> - 1.4.4-3
- Rebuild to fix OCaml dependencies

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jun 15 2020 Jerry James <loganjerry@gmail.com> - 1.4.4-1
- Version 1.4.4

* Sat Jun 13 2020 Jerry James <loganjerry@gmail.com> - 1.4.3-4
- Rebuild for flocq 3.3.1

* Wed May 20 2020 Jerry James <loganjerry@gmail.com> - 1.4.3-3
- Rebuild for coq 8.11.1

* Tue May 05 2020 Richard W.M. Jones <rjones@redhat.com> - 1.4.3-2
- OCaml 4.11.0+dev2-2020-04-22 rebuild

* Wed Apr  8 2020 Jerry James <loganjerry@gmail.com> - 1.4.3-1
- Version 1.4.3
- Drop -coq811 patch in favor of upstream's solution

* Mon Mar 30 2020 Jerry James <loganjerry@gmail.com> - 1.4.2-6
- Add -coq811 patch to fix the build with coq 8.11

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jan 22 2020 Jerry James <loganjerry@gmail.com> - 1.4.2-4
- OCaml 4.10.0+beta1 rebuild.

* Fri Dec 06 2019 Richard W.M. Jones <rjones@redhat.com> - 1.4.2-3
- OCaml 4.09.0 (final) rebuild.

* Fri Sep  6 2019 Jerry James <loganjerry@gmail.com> - 1.4.2-2
- OCaml 4.08.1 (final) rebuild.

* Thu Aug  1 2019 Jerry James <loganjerry@gmail.com> - 1.4.2-1
- New upstream release

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Jun  5 2019 Jerry James <loganjerry@gmail.com> - 1.4.1-1
- New upstream release
- Add a check script

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jan 26 2019 Jerry James <loganjerry@gmail.com> - 1.4.0-1
- New upstream release

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Jul 11 2018 Richard W.M. Jones <rjones@redhat.com> - 1.3.3-3
- OCaml 4.07.0 (final) rebuild.

* Wed Jun 20 2018 Richard W.M. Jones <rjones@redhat.com> - 1.3.3-2
- OCaml 4.07.0-rc1 rebuild.

* Mon Feb 12 2018 Jerry James <loganjerry@gmail.com> - 1.3.3-1
- New upstream release
- Build with camlp5 since coq now requires it instead of camlp4
- Drop now unneeded patch for building with camlp4
- Drop upstreamed safe-string patch

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.2-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Nov 17 2017 Richard W.M. Jones <rjones@redhat.com> - 1.3.2-11
- OCaml 4.06.0 rebuild.

* Thu Oct  5 2017 Jerry James <loganjerry@gmail.com> - 1.3.2-10
- Rebuild for flocq 2.6.0

* Wed Sep 06 2017 Richard W.M. Jones <rjones@redhat.com> - 1.3.2-9
- OCaml 4.05.0 rebuild.

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Jun 27 2017 Richard W.M. Jones <rjones@redhat.com> - 1.3.2-6
- OCaml 4.04.2 rebuild.

* Fri May 12 2017 Richard W.M. Jones <rjones@redhat.com> - 1.3.2-5
- OCaml 4.04.1 rebuild.

* Fri Mar 24 2017 Jerry James <loganjerry@gmail.com> - 1.3.2-4
- Rebuild to fix coq consistency issue

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Jan 12 2017 Jerry James <loganjerry@gmail.com> - 1.3.2-2
- Rebuild for coq 8.6

* Mon Nov 28 2016 Jerry James <loganjerry@gmail.com> - 1.3.2-1
- New upstream release

* Mon Nov 07 2016 Richard W.M. Jones <rjones@redhat.com> - 1.3.1-4
- Rebuild for OCaml 4.04.0.

* Fri Oct 28 2016 Jerry James <loganjerry@gmail.com> - 1.3.1-3
- Rebuild for coq 8.5pl3

* Mon Oct 03 2016 Dan Horák <dan[at]danny.cz> - 1.3.1-2
- disable debuginfo subpackage on interpreted builds

* Thu Sep 29 2016 Jerry James <loganjerry@gmail.com> - 1.3.1-1
- New upstream release

* Fri Jul 22 2016 Jerry James <loganjerry@gmail.com> - 1.3.0-1
- New upstream release

* Wed Jul 13 2016 Jerry James <loganjerry@gmail.com> - 1.2.1-3
- Rebuild for coq 8.5pl2

* Fri Apr 22 2016 Jerry James <loganjerry@gmail.com> - 1.2.1-2
- Rebuild for coq 8.5pl1

* Fri Feb 12 2016 Jerry James <loganjerry@gmail.com> - 1.2.1-1
- New upstream release
- Use camlp4 in preference to camlp5

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Oct 14 2015 Jerry James <loganjerry@gmail.com> - 1.2.0-1
- New upstream release

* Thu Jul 30 2015 Richard W.M. Jones <rjones@redhat.com> - 1.1.0-3
- OCaml 4.02.3 rebuild.

* Wed Jun 24 2015 Richard W.M. Jones <rjones@redhat.com> - 1.1.0-2
- ocaml-4.02.2 final rebuild.

* Mon Jun 22 2015 Jerry James <loganjerry@gmail.com> - 1.1.0-1
- New upstream release

* Wed Jun 17 2015 Richard W.M. Jones <rjones@redhat.com> - 1.0.0-21
- ocaml-4.02.2 rebuild.

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.0-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Apr 11 2015 Jerry James <loganjerry@gmail.com> - 1.0.0-19
- Rebuild for coq 8.4pl6

* Tue Feb 17 2015 Richard W.M. Jones <rjones@redhat.com> - 1.0.0-18
- ocaml-4.02.1 rebuild.

* Thu Nov  6 2014 Jerry James <loganjerry@gmail.com> - 1.0.0-17
- Rebuild for ocaml-camlp5 6.12

* Thu Oct 30 2014 Jerry James <loganjerry@gmail.com> - 1.0.0-16
- Rebuild for coq 8.4pl5

* Tue Sep  2 2014 Jerry James <loganjerry@gmail.com> - 1.0.0-15
- Rebuild for flocq 2.4.0

* Sun Aug 31 2014 Richard W.M. Jones <rjones@redhat.com> - 1.0.0-14
- ocaml-4.02.0 final rebuild.

* Mon Aug 25 2014 Jerry James <loganjerry@gmail.com> - 1.0.0-13
- ocaml-4.02.0+rc1 rebuild.

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Mon Aug  4 2014 Jerry James <loganjerry@gmail.com> - 1.0.0-12
- Add workaround for ocamlopt beta version string
- Fix license handling

* Sat Aug 02 2014 Richard W.M. Jones <rjones@redhat.com> - 1.0.0-11
- ocaml-4.02.0-0.8.git10e45753.fc22 rebuild.

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue May 13 2014 Jerry James <loganjerry@gmail.com> - 1.0.0-9
- Rebuild for coq 8.4pl4

* Mon Apr 21 2014 Jerry James <loganjerry@gmail.com> - 1.0.0-8
- Rebuild for flocq 2.3.0

* Tue Apr 15 2014 Richard W.M. Jones <rjones@redhat.com> - 1.0.0-7
- Remove ocaml_arches macro (RHBZ#1087794).

* Mon Mar 24 2014 Jerry James <loganjerry@gmail.com> - 1.0.0-6
- Rebuild for flocq 2.2.2

* Wed Dec 18 2013 Jerry James <loganjerry@gmail.com> - 1.0.0-5
- Rebuild for coq 8.4pl3

* Mon Sep 16 2013 Jerry James <loganjerry@gmail.com> - 1.0.0-4
- Rebuild for OCaml 4.01.0
- Enable debuginfo

* Mon Aug 12 2013 Jerry James <loganjerry@gmail.com> - 1.0.0-3
- Rebuild for flocq 2.2.0

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon Jul 29 2013 Jerry James <loganjerry@gmail.com> - 1.0.0-1
- New upstream release

* Wed Jul  3 2013 Jerry James <loganjerry@gmail.com> - 0.21.1-1
- New upstream release

* Tue May 14 2013 Jerry James <loganjerry@gmail.com> - 0.20.0-1
- New upstream release

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.18.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Mon Jan  7 2013 Jerry James <loganjerry@gmail.com> - 0.18.0-6
- Rebuild for coq 8.4pl1

* Fri Oct 19 2012 Jerry James <loganjerry@gmail.com> - 0.18.0-5
- Rebuild for OCaml 4.00.1

* Tue Aug 21 2012 Jerry James <loganjerry@gmail.com> - 0.18.0-4
- Rebuild for coq 8.4

* Sat Jul 28 2012 Jerry James <loganjerry@gmail.com> - 0.18.0-3
- Rebuild for coq 8.3pl4, OCaml 4.00.0, and gappa 0.16.1

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.18.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Jan  9 2012 Jerry James <loganjerry@gmail.com> - 0.18.0-1
- New upstream release

* Tue Dec 27 2011 Jerry James <loganjerry@gmail.com> - 0.17.0-2
- Rebuild for coq 8.3pl3

* Mon Dec 12 2011 Jerry James <loganjerry@gmail.com> - 0.17.0-1
- New upstream release

* Sat Oct 29 2011 Jerry James <loganjerry@gmail.com> - 0.16.0-3
- BR ocaml

* Wed Oct 26 2011 Jerry James <loganjerry@gmail.com> - 0.16.0-2
- Split out a -devel subpackage

* Tue Jul  5 2011 Jerry James <loganjerry@gmail.com> - 0.16.0-1
- Initial RPM
