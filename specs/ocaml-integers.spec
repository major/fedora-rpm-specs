# OCaml packages not built on i686 since OCaml 5 / Fedora 39.
ExcludeArch: %{ix86}

Name:           ocaml-integers
Version:        0.7.0
Release:        17%{?dist}
Summary:        Various signed and unsigned integer types for OCaml

License:        MIT
URL:            https://github.com/yallop/ocaml-integers
VCS:            git:%{url}.git
Source:         %{url}/archive/%{version}/%{name}-%{version}.tar.gz
# Fedora does not need stdlib-shims, which is for older OCaml systems
Patch:          %{name}-stdlib-shims.patch

BuildRequires:  ocaml >= 4.02
BuildRequires:  ocaml-dune

# Do not require ocaml-compiler-libs at runtime
%global __ocaml_requires_opts -i Asttypes -i Build_path_prefix_map -i Cmi_format -i Env -i Format_doc -i Ident -i Identifiable -i Load_path -i Location -i Longident -i Misc -i Oprint -i Outcometree -i Parsetree -i Path -i Primitive -i Shape -i Subst -i Toploop -i Type_immediacy -i Types -i Unit_info -i Warnings

%description
The ocaml-integers library provides a number of 8-, 16-, 32- and 64-bit
signed and unsigned integer types, together with aliases such as `long`
and `size_t` whose sizes depend on the host platform.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and signature
files for developing applications that use %{name}.

%prep
%autosetup -p1

%build
%dune_build

%install
%dune_install

%check
%dune_check

%files -f .ofiles
%license LICENSE.md
%doc CHANGES.md README.md

%files devel -f .ofiles-devel

%changelog
* Thu Jan  9 2025 Jerry James <loganjerry@gmail.com> - 0.7.0-17
- OCaml 5.3.0 rebuild for Fedora 42
- Update __ocaml_requires_opts for OCaml 5.3.0

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jun 19 2024 Richard W.M. Jones <rjones@redhat.com> - 0.7.0-15
- OCaml 5.2.0 ppc64le fix

* Wed May 29 2024 Richard W.M. Jones <rjones@redhat.com> - 0.7.0-14
- OCaml 5.2.0 for Fedora 41

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Dec 18 2023 Richard W.M. Jones <rjones@redhat.com> - 0.7.0-11
- OCaml 5.1.1 + s390x code gen fix for Fedora 40

* Tue Dec 12 2023 Richard W.M. Jones <rjones@redhat.com> - 0.7.0-10
- OCaml 5.1.1 rebuild for Fedora 40

* Thu Oct 05 2023 Richard W.M. Jones <rjones@redhat.com> - 0.7.0-9
- OCaml 5.1 rebuild for Fedora 40

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jul 11 2023 Richard W.M. Jones <rjones@redhat.com> - 0.7.0-7
- OCaml 5.0 rebuild for Fedora 39

* Mon Jul 10 2023 Jerry James <loganjerry@gmail.com> - 0.7.0-6
- OCaml 5.0.0 rebuild
- Do not require ocaml-compiler-libs at runtime

* Tue Jan 24 2023 Richard W.M. Jones <rjones@redhat.com> - 0.7.0-5
- Rebuild OCaml packages for F38

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Tue Jan 17 2023 Jerry James <loganjerry@gmail.com> - 0.7.0-3
- New project URL

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jun 25 2022 Jerry James <loganjerry@gmail.com> - 0.7.0-2
- Use new OCaml macros

* Sat Jun 18 2022 Richard W.M. Jones <rjones@redhat.com> - 0.7.0-2
- OCaml 4.14.0 rebuild

* Thu Mar 24 2022 Jerry James <loganjerry@gmail.com> - 0.7.0-1
- Version 0.7.0

* Mon Feb 28 2022 Jerry James <loganjerry@gmail.com> - 0.6.0-1
- Version 0.6.0

* Fri Feb 04 2022 Richard W.M. Jones <rjones@redhat.com> - 0.5.1-5
- Bump release and rebuild.

* Fri Feb 04 2022 Richard W.M. Jones <rjones@redhat.com> - 0.5.1-4
- OCaml 4.13.1 rebuild to remove package notes

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Mon Oct 04 2021 Richard W.M. Jones <rjones@redhat.com> - 0.5.1-2
- OCaml 4.13.1 build

* Fri Aug 13 2021 Jerry James <loganjerry@gmail.com> - 0.5.1-1
- Version 0.5.1

* Fri Aug  6 2021 Jerry James <loganjerry@gmail.com> - 0.5.0-1
- Version 0.5.0
- Reenable debuginfo

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon Mar  1 11:02:39 GMT 2021 Richard W.M. Jones <rjones@redhat.com> - 0.4.0-4
- Disable the debuginfo subpackages.
- Make the -doc subpackage conditional.

* Mon Mar  1 11:02:39 GMT 2021 Richard W.M. Jones <rjones@redhat.com> - 0.4.0-2
- OCaml 4.12.0 build

* Tue Feb 09 2021 Jerry James <loganjerry@gmail.com> - 0.4.0-1
- Initial package
