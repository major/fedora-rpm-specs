# OCaml packages not built on i686 since OCaml 5 / Fedora 39.
ExcludeArch: %{ix86}

Name:           ocaml-cryptokit
Version:        1.20.1
Release:        2%{?dist}
Summary:        OCaml library of cryptographic and hash functions

%global upver %(tr -d . <<< %{version})

# LGPL-2.0-or-later WITH OCaml-LGPL-linking-exception: the project as a whole
# LGPL-2.1-or-later: src/blowfish.{c,h}
License:        LGPL-2.0-or-later WITH OCaml-LGPL-linking-exception AND LGPL-2.1-or-later
URL:            https://github.com/xavierleroy/cryptokit/
VCS:            git:%{url}.git
Source0:        %{url}/archive/release%{upver}/cryptokit-%{version}.tar.gz
# Use zlib-ng directly instead of via the zlib compatibility API
Patch:          %{name}-zlib-ng.patch

BuildRequires:  ocaml >= 4.08.0
BuildRequires:  ocaml-dune >= 2.5
BuildRequires:  ocaml-dune-configurator-devel
BuildRequires:  ocaml-zarith-devel >= 1.4
BuildRequires:  pkgconfig(gmp)
BuildRequires:  pkgconfig(zlib-ng)


%description
The Cryptokit library for Objective Caml provides a variety of
cryptographic primitives that can be used to implement cryptographic
protocols in security-sensitive applications. The primitives provided
include:

* Symmetric-key cryptography: AES, Chacha20, DES, Triple-DES, Blowfish,
  ARCfour, in ECB, CBC, CFB, OFB and counter modes.
* Authenticated encryption: AES-GCM, Chacha20-Poly1305.
* Public-key cryptography: RSA encryption and signature; Diffie-Hellman
  key agreement.
* Hash functions and MACs: SHA-3, SHA-2, BLAKE2, BLAKE3, RIPEMD-160;
  MACs based on AES and DES; SipHash.  (SHA-1 and MD5, despite being
  broken, are also provided for historical value.)
* Random number generation.
* Encodings and compression: base 64, hexadecimal, Zlib compression. 

Additional ciphers and hashes can easily be used in conjunction with
the library. In particular, basic mechanisms such as chaining modes,
output buffering, and padding are provided by generic classes that can
easily be composed with user-provided ciphers. More generally, the
library promotes a "Lego"-like style of constructing and composing
transformations over character streams.


%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       ocaml-zarith-devel%{?_isa}


%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.


%prep
%autosetup -n cryptokit-release%{upver} -p1


%build
# On x86 and x86_64, the configure script finds support for the -maes flag in
# the compiler, and uses it to compile src/aesni.{c,h}.  This is okay because
# use of the compiled code is conditional.  The function aesni_check_available()
# is called first, which checks the CPUID to verify that the instructions exist
# on the CPU.  Therefore, older CPUs can still run the compiled code.
%dune_build


%check
# This opens /dev/random but never reads from it.
%dune_check


%install
%dune_install


%files -f .ofiles
%license LICENSE


%files devel -f .ofiles-devel
%doc README.md Changes


%changelog
* Fri Dec 27 2024 Jerry James <loganjerry@gmail.com> - 1.20.1-2
- Use zlib-ng instead of zlib

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.20.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Tue Jul 16 2024 Jerry James <loganjerry@gmail.com> - 1.20.1-1
- Version 1.20.1

* Wed Jun 19 2024 Richard W.M. Jones <rjones@redhat.com> - 1.19-3
- OCaml 5.2.0 ppc64le fix

* Wed May 29 2024 Richard W.M. Jones <rjones@redhat.com> - 1.19-2
- OCaml 5.2.0 for Fedora 41

* Thu May 23 2024 Jerry James <loganjerry@gmail.com> - 1.19-1
- Version 1.19

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.18-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.18-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Dec 18 2023 Richard W.M. Jones <rjones@redhat.com> - 1.18-8
- Bump release and rebuild

* Mon Dec 18 2023 Richard W.M. Jones <rjones@redhat.com> - 1.18-7
- OCaml 5.1.1 + s390x code gen fix for Fedora 40

* Tue Dec 12 2023 Richard W.M. Jones <rjones@redhat.com> - 1.18-6
- OCaml 5.1.1 rebuild for Fedora 40

* Thu Oct 05 2023 Richard W.M. Jones <rjones@redhat.com> - 1.18-5
- OCaml 5.1 rebuild for Fedora 40

* Thu Jul 27 2023 Jerry James <loganjerry@gmail.com> - 1.18-4
- Rebuild for ocaml-zarith 1.13

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.18-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Jul 12 2023 Richard W.M. Jones <rjones@redhat.com> - 1.18-2
- OCaml 5.0 rebuild for Fedora 39

* Mon Jul 10 2023 Jerry James <loganjerry@gmail.com> - 1.18-1
- Version 1.18
- Convert License tag to SPDX
- Use new dune macros
- Update description from upstream README.md

* Tue Jan 24 2023 Richard W.M. Jones <rjones@redhat.com> - 1.16.1-13
- Bump release and rebuild

* Tue Jan 24 2023 Richard W.M. Jones <rjones@redhat.com> - 1.16.1-12
- Rebuild OCaml packages for F38

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.16.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.16.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sun Jun 19 2022 Richard W.M. Jones <rjones@redhat.com> - 1.16.1-9
- OCaml 4.14.0 rebuild

* Fri Feb 04 2022 Richard W.M. Jones <rjones@redhat.com> - 1.16.1-8
- OCaml 4.13.1 rebuild to remove package notes

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.16.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Mon Oct 04 2021 Richard W.M. Jones <rjones@redhat.com> - 1.16.1-6
- OCaml 4.13.1 build

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.16.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon Jul 19 2021 Jerry James <loganjerry@gmail.com> - 1.16.1-4
- Move META file to main package
- Drop obsolete workaround for dune bug

* Wed Mar  3 2021 Jerry James <loganjerry@gmail.com> - 1.16.1-4
- Rebuild for ocaml-zarith 1.12
- Build -doc again; there is no circular dependency

* Mon Mar  1 17:24:19 GMT 2021 Richard W.M. Jones <rjones@redhat.com> - 1.16.1-3
- OCaml 4.12.0 build
- Make -doc subpackage conditional.

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.16.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Nov 16 2020 Jerry James <loganjerry@gmail.com> - 1.16.1-1
- Version 1.16.1, built with ocaml-zarith 1.11
- New project and source URLs
- Dune is now used to build
- Add -doc subpackage

* Fri Sep 25 2020 Jerry James <loganjerry@gmail.com> - 1.11-30
- Rebuild for ocaml-zarith 1.10

* Tue Sep 01 2020 Richard W.M. Jones <rjones@redhat.com> - 1.11-29
- OCaml 4.11.1 rebuild

* Fri Aug 21 2020 Richard W.M. Jones <rjones@redhat.com> - 1.11-28
- OCaml 4.11.0 rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.11-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon May 04 2020 Richard W.M. Jones <rjones@redhat.com> - 1.11-26
- OCaml 4.11.0+dev2-2020-04-22 rebuild

* Tue Apr 21 2020 Richard W.M. Jones <rjones@redhat.com> - 1.11-25
- OCaml 4.11.0 pre-release attempt 2

* Fri Apr 17 2020 Richard W.M. Jones <rjones@redhat.com> - 1.11-24
- OCaml 4.11.0 pre-release

* Thu Apr 02 2020 Richard W.M. Jones <rjones@redhat.com> - 1.11-23
- Update all OCaml dependencies for RPM 4.16.

* Wed Feb 26 2020 Richard W.M. Jones <rjones@redhat.com> - 1.11-22
- OCaml 4.10.0 final.

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.11-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Jan 19 2020 Richard W.M. Jones <rjones@redhat.com> - 1.11-20
- OCaml 4.10.0+beta1 rebuild.

* Fri Dec 06 2019 Richard W.M. Jones <rjones@redhat.com> - 1.11-19
- OCaml 4.09.0 (final) rebuild.

* Tue Oct 29 2019 Jerry James <loganjerry@gmail.com> - 1.11-18
- Rebuild for ocaml-zarith 1.9.1

* Fri Aug 16 2019 Richard W.M. Jones <rjones@redhat.com> - 1.11-17
- OCaml 4.08.1 (final) rebuild.

* Wed Jul 31 2019 Richard W.M. Jones <rjones@redhat.com> - 1.11-16
- OCaml 4.08.1 (rc2) rebuild.

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.11-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.11-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.11-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Jul 11 2018 Richard W.M. Jones <rjones@redhat.com> - 1.11-12
- OCaml 4.07.0 (final) rebuild.

* Wed Jun 20 2018 Richard W.M. Jones <rjones@redhat.com> - 1.11-11
- OCaml 4.07.0-rc1 rebuild.

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.11-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Nov 17 2017 Richard W.M. Jones <rjones@redhat.com> - 1.11-9
- OCaml 4.06.0 rebuild.

* Tue Aug 08 2017 Richard W.M. Jones <rjones@redhat.com> - 1.11-8
- OCaml 4.05.0 rebuild.

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.11-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.11-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Jun 27 2017 Richard W.M. Jones <rjones@redhat.com> - 1.11-5
- OCaml 4.04.2 rebuild.

* Sat May 13 2017 Richard W.M. Jones <rjones@redhat.com> - 1.11-4
- OCaml 4.04.1 rebuild.

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.11-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Nov 09 2016 Dan Horák <dan@danny.cz> - 1.11-2
- rebuild for s390x codegen bug

* Mon Nov 07 2016 Richard W.M. Jones <rjones@redhat.com> - 1.11-1
- New upstream version 1.11.
- New BR ocaml-zarith.

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.9-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Jul 28 2015 Richard W.M. Jones <rjones@redhat.com> - 1.9-16
- OCaml 4.02.3 rebuild.

* Mon Jul 27 2015 Richard W.M. Jones <rjones@redhat.com> - 1.9-15
- Remove ExcludeArch since bytecode build should now work.

* Wed Jun 24 2015 Richard W.M. Jones <rjones@redhat.com> - 1.9-14
- ocaml-4.02.2 final rebuild.

* Thu Jun 18 2015 Richard W.M. Jones <rjones@redhat.com> - 1.9-13
- ocaml-4.02.2 rebuild.

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.9-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Feb 17 2015 Richard W.M. Jones <rjones@redhat.com> - 1.9-11
- ocaml-4.02.1 rebuild.

* Mon Nov 03 2014 Richard W.M. Jones <rjones@redhat.com> - 1.9-10
- Fix missing OCaml uint32 special types, use standard types instead.

* Sun Aug 31 2014 Richard W.M. Jones <rjones@redhat.com> - 1.9-8
- Bump release and rebuild.

* Sun Aug 31 2014 Richard W.M. Jones <rjones@redhat.com> - 1.9-7
- ocaml-4.02.0 final rebuild.

* Sat Aug 23 2014 Richard W.M. Jones <rjones@redhat.com> - 1.9-6
- ocaml-4.02.0+rc1 rebuild.

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.9-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Aug 02 2014 Richard W.M. Jones <rjones@redhat.com> - 1.9-4
- ocaml-4.02.0-0.8.git10e45753.fc22 rebuild.

* Mon Jul 21 2014 Richard W.M. Jones <rjones@redhat.com> - 1.9-3
- OCaml 4.02.0 beta rebuild.

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Sep 14 2013 Richard W.M. Jones <rjones@redhat.com> - 1.9-1
- New upstream version 1.9.
- Rebuild for OCaml 4.01.0.
- Enable debuginfo.
- Modernize the spec file.

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sun Dec 02 2012 Bruno Wolff III <bruno@wolff.to> - 1.6-3
- Rebuild for ocaml 4.0.1.

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Jul  2 2012 Richard W.M. Jones <rjones@redhat.com> - 1.6-1
- New upstream version 1.6.

* Sun Jun 10 2012 Richard W.M. Jones <rjones@redhat.com> - 1.4-6
- Rebuild for OCaml 4.00.0.

* Thu Jan 12 2012 Richard W.M. Jones <rjones@redhat.com> - 1.4-5
- Rebuild for OCaml 3.12.1.

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Jan  5 2011 Richard W.M. Jones <rjones@redhat.com> - 1.4-3
- New upstream version 1.4.
- Project has moved to a new location.
- META file is included in the project.
- Rebuild for OCaml 3.12.0.
- Build system changed.
- *.cmx files are no longer installed during build.
- Missing BR ocamldoc.
- Missing BR findlib.

* Wed Dec 30 2009 Richard W.M. Jones <rjones@redhat.com> - 1.3-11
- Rebuild for OCaml 3.11.2.

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Fri May 22 2009 Richard W.M. Jones <rjones@redhat.com> - 1.3-9
- Rebuild for OCaml 3.11.1.

* Thu Apr 16 2009 S390x secondary arch maintainer <fedora-s390x@lists.fedoraproject.org>
- ExcludeArch sparc64, s390, s390x as we don't have OCaml on those archs
  (added sparc64 per request from the sparc maintainer)

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Wed Nov 26 2008 Richard W.M. Jones <rjones@redhat.com> - 1.3-7
- Rebuild for OCaml 3.11.0+rc1.

* Wed Nov 19 2008 Richard W.M. Jones <rjones@redhat.com> - 1.3-6
- Rebuild for OCaml 3.11.0

* Tue Sep  2 2008 Richard W.M. Jones <rjones@redhat.com> - 1.3-5
- Install in cryptokit subdirectory.
- Include a META file (from Debian) (resolves rhbz#460844).

* Wed Apr 23 2008 Richard W.M. Jones <rjones@redhat.com> - 1.3-4
- Rebuild for OCaml 3.10.2

* Fri Feb 29 2008 David Woodhouse <dwmw2@infradead.org> 1.3-3
- Build on PPC64

* Fri Feb 15 2008 Richard W.M. Jones <rjones@redhat.com> - 1.3-2
- Don't duplicate the README file in both packages.
- Change the license to LGPLv2 with exceptions.

* Tue Feb 12 2008 Richard W.M. Jones <rjones@redhat.com> - 1.3-1
- Initial RPM release.
