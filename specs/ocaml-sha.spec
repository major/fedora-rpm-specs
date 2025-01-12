# OCaml packages not built on i686 since OCaml 5 / Fedora 39.
ExcludeArch: %{ix86}

Name:           ocaml-sha
Version:        1.15.4
Release:        12%{?dist}
Summary:        Binding to the SHA cryptographic functions

License:        ISC
URL:            https://github.com/djs55/ocaml-sha
VCS:            git:%{url}.git
Source0:        %{url}/releases/download/v%{version}/sha-%{version}.tbz

# The OCaml version packaged in Fedora is recent enough, no need to shim stdlib.
Patch1:         ocaml-sha-remove-stdlib-shims-dep.patch

BuildRequires:  ocaml
BuildRequires:  ocaml-dune
BuildRequires:  ocaml-ounit-devel

%description
A binding for SHA interface code in OCaml.  This packages offers the
same interface as the MD5 digest included in the OCaml standard library.
It currently provides SHA1, SHA256 and SHA512 hash functions.


%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}


%description    devel
The %{name}-devel package contains libraries and signature
files for developing applications that use %{name}.


%prep
%autosetup -n sha-%{version} -p1


%build
%dune_build


%install
%dune_install


%check
%dune_check


%files -f .ofiles
%doc README.md CHANGES.md
%license LICENSE.md


%files devel -f .ofiles-devel
%doc README.md CHANGES.md
%license LICENSE.md


%changelog
* Thu Jan  9 2025 Jerry James <loganjerry@gmail.com> - 1.15.4-12
- OCaml 5.3.0 rebuild for Fedora 42

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.15.4-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jun 19 2024 Richard W.M. Jones <rjones@redhat.com> - 1.15.4-10
- OCaml 5.2.0 ppc64le fix

* Wed May 29 2024 Richard W.M. Jones <rjones@redhat.com> - 1.15.4-9
- OCaml 5.2.0 for Fedora 41

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.15.4-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.15.4-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Dec 18 2023 Richard W.M. Jones <rjones@redhat.com> - 1.15.4-6
- OCaml 5.1.1 + s390x code gen fix for Fedora 40

* Tue Dec 12 2023 Richard W.M. Jones <rjones@redhat.com> - 1.15.4-5
- OCaml 5.1.1 rebuild for Fedora 40

* Thu Oct 05 2023 Richard W.M. Jones <rjones@redhat.com> - 1.15.4-4
- OCaml 5.1 rebuild for Fedora 40

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.15.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jul 11 2023 Richard W.M. Jones <rjones@redhat.com> - 1.15.4-2
- OCaml 5.0 rebuild for Fedora 39

* Mon Jul 10 2023 Jerry James <loganjerry@gmail.com> - 1.15.4-1
- Version 1.15.4
- Trim BuildRequires
- Use new dune macros

* Tue Jan 24 2023 Richard W.M. Jones <rjones@redhat.com> - 1.15.2-3
- Rebuild OCaml packages for F38

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.15.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Mon Aug 08 2022 Andy Li <andy@onthewings.net> - 1.15.2-1
- New upstream version. (RHBZ#2051541)

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.15.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sun Jun 19 2022 Richard W.M. Jones <rjones@redhat.com> - 1.15.1-3
- OCaml 4.14.0 rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.15.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Nov 02 2021 Andy Li <andy@onthewings.net> - 1.15.1-1
- New upstream version. (RHBZ#1939312)
- Remove ocaml-sha-1.12-ounit2.patch, which is no longer needed.
- Add ocaml-sha-remove-stdlib-shims-dep.patch.

* Tue Oct 05 2021 Richard W.M. Jones <rjones@redhat.com> - 1.13-8
- OCaml 4.13.1 build

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.13-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon Mar  1 22:00:48 GMT 2021 Richard W.M. Jones <rjones@redhat.com> - 1.13-6
- OCaml 4.12.0 build

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.13-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Sep 01 2020 Richard W.M. Jones <rjones@redhat.com> - 1.13-4
- OCaml 4.11.1 rebuild

* Fri Aug 21 2020 Richard W.M. Jones <rjones@redhat.com> - 1.13-3
- OCaml 4.11.0 rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.13-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed May 20 2020 Andy Li <andy@onthewings.net> - 1.13-1
- New upstream version. (RHBZ#1818607) (RHBZ#1799819)
- Remove patches integrated in 1.13.

* Tue May 05 2020 Richard W.M. Jones <rjones@redhat.com> - 1.12-14
- OCaml 4.11.0+dev2-2020-04-22 rebuild

* Wed Apr 22 2020 Richard W.M. Jones <rjones@redhat.com> - 1.12-13
- OCaml 4.11.0 pre-release attempt 2

* Sat Apr 04 2020 Richard W.M. Jones <rjones@redhat.com> - 1.12-12
- Bump release and rebuild.

* Sat Apr 04 2020 Richard W.M. Jones <rjones@redhat.com> - 1.12-11
- Update all OCaml dependencies for RPM 4.16.

* Thu Feb 27 2020 Richard W.M. Jones <rjones@redhat.com> - 1.12-10
- OCaml 4.10.0 final.
- Include all upstream patches since 1.12 was released.

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.12-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Dec 18 2019 Andy Li <andy@onthewings.net> - 1.12-7
- Rebuild against latest ocaml package.

* Fri Nov 01 2019 Andy Li <andy@onthewings.net> - 1.12-6
- Rebuild against latest ocaml package.

* Sat Jul 27 2019 Andy Li <andy@onthewings.net> - 1.12-5
- Update build system and commands from jbuilder to dune.

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.12-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.12-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.12-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Mar 27 2018 Andy Li <andy@onthewings.net> - 1.12-1
- Initial RPM release.
