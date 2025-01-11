# OCaml packages not built on i686 since OCaml 5 / Fedora 39.
ExcludeArch: %{ix86}

%global debug_package %{nil}

Name:           ocaml-xmlrpc-light
Version:        0.6.1
Release:        83%{?dist}
Summary:        OCaml library for writing XML-RPC clients and servers
License:        LGPL-2.1-or-later WITH OCaml-LGPL-linking-exception

URL:            https://code.google.com/archive/p/xmlrpc-light/
Source0:        https://storage.googleapis.com/google-code-archive-downloads/v2/code.google.com/xmlrpc-light/xmlrpc-light-%{version}.tar.gz

BuildRequires:  make
BuildRequires:  ocaml >= 3.10.0
BuildRequires:  ocaml-findlib
BuildRequires:  ocaml-ocamldoc
BuildRequires:  ocaml-xml-light-devel
BuildRequires:  ocaml-ocamlnet-devel
BuildRequires:  ocaml-ocamlnet-nethttpd-devel
BuildRequires:  ocaml-camlp-streams-devel
BuildRequires:  ocaml-rpm-macros
BuildRequires:  dos2unix

# Fix the package to work with ocamlnet 3.x.
Patch1:         debian_patches_0002-Compile-with-ocamlnet-3.3.5.patch

# Further fix the package to work with ocamlnet 4.x.
Patch2:         xmlrpc-light-0.6.1-ocamlnet4.patch

# Safe-string patches for OCaml 4.06.
Patch3:         xmlrpc-light-0.6.1-safe-string.patch

# Use camlp-streams for compatibility with OCaml 5.0
Patch4:         xmlrpc-light-0.6.1-camlp-streams.patch


%description
XmlRpc-Light is an XmlRpc library written in OCaml.


%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       ocaml-xml-light-devel%{?_isa}
Requires:       ocaml-ocamlnet-devel%{?_isa}
Requires:       ocaml-ocamlnet-nethttpd-devel%{?_isa}
Requires:       ocaml-camlp-streams-devel%{?_isa}


%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.


%prep
%autosetup -n xmlrpc-light-%{version} -p1
dos2unix LICENSE
dos2unix README.txt

%ifnarch %{ocaml_native_compiler}
# Do not try to build or install the native library
sed -i 's/ xmlrpc-light\.cmxa xmlrpc-light\.a//' Makefile
sed -i '/libinstall:/s/\tall/ byte-code-library/' OCamlMakefile
%endif


%build
%ifarch %{ocaml_native_compiler}
make
%else
make byte-code-library
%endif


%install
export OCAMLFIND_DESTDIR=$RPM_BUILD_ROOT%{_libdir}/ocaml
mkdir -p $OCAMLFIND_DESTDIR
%make_install
%ocaml_files


%files -f .ofiles
%license LICENSE


%files devel -f .ofiles-devel
%doc doc/xmlrpc-light/{html,latex} README.txt
%license LICENSE


%changelog
* Thu Jan  9 2025 Jerry James <loganjerry@gmail.com> - 0.6.1-83
- OCaml 5.3.0 rebuild for Fedora 42

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.1-82
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jun 19 2024 Richard W.M. Jones <rjones@redhat.com> - 0.6.1-81
- OCaml 5.2.0 ppc64le fix

* Wed May 29 2024 Richard W.M. Jones <rjones@redhat.com> - 0.6.1-80
- OCaml 5.2.0 for Fedora 41

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.1-79
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.1-78
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Dec 18 2023 Richard W.M. Jones <rjones@redhat.com> - 0.6.1-77
- OCaml 5.1.1 + s390x code gen fix for Fedora 40

* Tue Dec 12 2023 Richard W.M. Jones <rjones@redhat.com> - 0.6.1-76
- OCaml 5.1.1 rebuild for Fedora 40

* Thu Oct 05 2023 Richard W.M. Jones <rjones@redhat.com> - 0.6.1-75
- OCaml 5.1 rebuild for Fedora 40

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.1-74
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Jul 12 2023 Richard W.M. Jones <rjones@redhat.com> - 0.6.1-73
- OCaml 5.0 rebuild for Fedora 39

* Mon Jul 10 2023 Jerry James <loganjerry@gmail.com> - 0.6.1-72
- OCaml 5.0.0 rebuild
- New project URLs
- Convert License tag to SPDX
- Add patch for OCaml 5.0 compatibility
- Use new OCaml macros

* Thu Feb 23 2023 Richard W.M. Jones <rjones@redhat.com> - 0.6.1-71
- Rebuild for updated ocaml-xml-light

* Tue Jan 24 2023 Richard W.M. Jones <rjones@redhat.com> - 0.6.1-70
- Rebuild OCaml packages for F38

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.1-69
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.1-68
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sun Jun 19 2022 Richard W.M. Jones <rjones@redhat.com> - 0.6.1-67
- OCaml 4.14.0 rebuild

* Fri Feb 04 2022 Richard W.M. Jones <rjones@redhat.com> - 0.6.1-66
- OCaml 4.13.1 rebuild to remove package notes

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.1-65
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Dec 30 2021 Richard W.M. Jones <rjones@redhat.com> - 0.6.1-64
- Build and rebuild for new xml-light (RHBZ#2036236)

* Mon Oct 04 2021 Richard W.M. Jones <rjones@redhat.com> - 0.6.1-63
- OCaml 4.13.1 build

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.1-62
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon Mar  1 17:05:32 GMT 2021 Richard W.M. Jones <rjones@redhat.com> - 0.6.1-61
- OCaml 4.12.0 build

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.1-60
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jan 18 2021 Richard W.M. Jones <rjones@redhat.com> - 0.6.1-59
- Bump and rebuild against new ocaml-ocamlnet (RHBZ#1917354).

* Tue Sep 01 2020 Richard W.M. Jones <rjones@redhat.com> - 0.6.1-58
- OCaml 4.11.1 rebuild

* Fri Aug 21 2020 Richard W.M. Jones <rjones@redhat.com> - 0.6.1-57
- OCaml 4.11.0 rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.1-56
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon May 04 2020 Richard W.M. Jones <rjones@redhat.com> - 0.6.1-55
- OCaml 4.11.0+dev2-2020-04-22 rebuild

* Tue Apr 21 2020 Richard W.M. Jones <rjones@redhat.com> - 0.6.1-54
- OCaml 4.11.0 pre-release attempt 2

* Fri Apr 17 2020 Richard W.M. Jones <rjones@redhat.com> - 0.6.1-53
- OCaml 4.11.0 pre-release

* Fri Apr 03 2020 Richard W.M. Jones <rjones@redhat.com> - 0.6.1-52
- Update all OCaml dependencies for RPM 4.16.

* Wed Feb 26 2020 Richard W.M. Jones <rjones@redhat.com> - 0.6.1-51
- OCaml 4.10.0 final.

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.1-50
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Jan 19 2020 Richard W.M. Jones <rjones@redhat.com> - 0.6.1-49
- OCaml 4.10.0+beta1 rebuild.

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.1-48
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.1-47
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.1-46
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Jul 11 2018 Richard W.M. Jones <rjones@redhat.com> - 0.6.1-45
- OCaml 4.07.0 (final) rebuild.

* Wed Jun 20 2018 Richard W.M. Jones <rjones@redhat.com> - 0.6.1-44
- OCaml 4.07.0-rc1 rebuild.

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.1-43
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Dec 13 2017 Richard W.M. Jones <rjones@redhat.com> - 0.6.1-42
- Rebuild against new ocamlnet.

* Wed Nov 22 2017 Richard W.M. Jones <rjones@redhat.com> - 0.6.1-41
- OCaml 4.06.0 rebuild.
- Fix safe-string issues.

* Wed Aug 09 2017 Richard W.M. Jones <rjones@redhat.com> - 0.6.1-40
- OCaml 4.05.0 rebuild.

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.1-39
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.1-38
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Jun 27 2017 Richard W.M. Jones <rjones@redhat.com> - 0.6.1-37
- OCaml 4.04.2 rebuild.

* Sat May 13 2017 Richard W.M. Jones <rjones@redhat.com> - 0.6.1-36
- OCaml 4.04.1 rebuild.

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.1-35
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Nov 09 2016 Dan Horák <dan@danny.cz> - 0.6.1-34
- remove ExcludeArch

* Mon Nov 07 2016 Richard W.M. Jones <rjones@redhat.com> - 0.6.1-33
- Rebuild for OCaml 4.04.0.

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.1-32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Jul 28 2015 Richard W.M. Jones <rjones@redhat.com> - 0.6.1-31
- OCaml 4.02.3 rebuild.

* Tue Jul 28 2015 Richard W.M. Jones <rjones@redhat.com> - 0.6.1-30
- Revert previous work on enabling bytecode, as it breaks documentation.

* Wed Jun 24 2015 Richard W.M. Jones <rjones@redhat.com> - 0.6.1-28
- ocaml-4.02.2 final rebuild.

* Thu Jun 18 2015 Richard W.M. Jones <rjones@redhat.com> - 0.6.1-27
- ocaml-4.02.2 rebuild.

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.1-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 16 2015 Richard W.M. Jones <rjones@redhat.com> - 0.6.1-25
- Bump and rebuild again for ocamlnet update.

* Wed Feb 18 2015 Richard W.M. Jones <rjones@redhat.com> - 0.6.1-24
- Bump release and rebuild.

* Wed Feb 18 2015 Richard W.M. Jones <rjones@redhat.com> - 0.6.1-23
- Further patching to work with ocamlnet 4.0.

* Tue Feb 17 2015 Richard W.M. Jones <rjones@redhat.com> - 0.6.1-22
- ocaml-4.02.1 rebuild.

* Sun Aug 31 2014 Richard W.M. Jones <rjones@redhat.com> - 0.6.1-21
- ocaml-4.02.0 final rebuild.

* Sun Aug 24 2014 Richard W.M. Jones <rjones@redhat.com> - 0.6.1-20
- ocaml-4.02.0+rc1 rebuild.

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.1-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Aug 02 2014 Richard W.M. Jones <rjones@redhat.com> - 0.6.1-18
- ocaml-4.02.0-0.8.git10e45753.fc22 rebuild.

* Wed Jul 23 2014 Richard W.M. Jones <rjones@redhat.com> - 0.6.1-17
- Bump release and rebuild.

* Wed Jul 23 2014 Richard W.M. Jones <rjones@redhat.com> - 0.6.1-16
- OCaml 4.02.0 beta rebuild.

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.1-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu Sep 19 2013 Richard W.M. Jones <rjones@redhat.com> - 0.6.1-14
- OCaml 4.01.0 rebuild.
- Modernize the spec file.

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.1-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sun Dec 02 2012 Bruno Wolff III <bruno@wolff.to> - 0.6.1-11
- Rebuild for ocaml 4.0.1.

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Jun 11 2012 Richard W.M. Jones <rjones@redhat.com> - 0.6.1-9
- Rebuild for OCaml 4.00.0.

* Fri Jan 06 2012 Richard W.M. Jones <rjones@redhat.com> - 0.6.1-8
- Rebuild for OCaml 3.12.1.

* Wed Sep 21 2011 Richard W.M. Jones <rjones@redhat.com> - 0.6.1-6
- Rebuilt for updated ocamlnet.
- Apply patch from Debian to fix builds against ocamlnet 3
  (thanks Stephane Glondu).

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Jan 06 2011 Richard W.M. Jones <rjones@redhat.com> - 0.6.1-5
- Rebuild for OCaml 3.12 (http://fedoraproject.org/wiki/Features/OCaml3.12).

* Wed Dec 30 2009 Richard W.M. Jones <rjones@redhat.com> - 0.6.1-4
- Rebuild for OCaml 3.11.2.

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Sat May 23 2009 Richard W.M. Jones <rjones@redhat.com> - 0.6.1-2
- Rebuild for OCaml 3.11.1

* Thu Apr 16 2009 S390x secondary arch maintainer <fedora-s390x@lists.fedoraproject.org>
- ExcludeArch sparc64, s390, s390x as we don't have OCaml on those archs
  (added sparc64 per request from the sparc maintainer)

* Tue Mar 10 2009 Richard W.M. Jones <rjones@redhat.com> - 0.6.1-1
- New upstream version 0.6.1.

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Wed Nov 26 2008 Richard W.M. Jones <rjones@redhat.com> - 0.6-5
- Rebuild for OCaml 3.11.0+rc1.

* Wed Nov 19 2008 Richard W.M. Jones <rjones@redhat.com> - 0.6-4
- Rebuild for OCaml 3.11.0

* Wed Apr 23 2008 Richard W.M. Jones <rjones@redhat.com> - 0.6-3
- Rebuild for OCaml 3.10.2

* Mon Mar  3 2008 Richard W.M. Jones <rjones@redhat.com> - 0.6-2
- Added missing BR ocaml-ocamlnet-nethttpd-devel.
- Test build in mock.
- Removed ExcludeArch: ppc64.

* Sat Feb 23 2008 Richard W.M. Jones <rjones@redhat.com> - 0.6-1
- Initial RPM release.
