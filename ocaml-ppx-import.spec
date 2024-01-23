# OCaml packages not built on i686 since OCaml 5 / Fedora 39.
ExcludeArch: %{ix86}

Name:           ocaml-ppx-import
Version:        1.10.0
Release:        13%{?dist}
Summary:        Syntax extension for importing declarations from interface files

License:        MIT
URL:            https://ocaml-ppx.github.io/ppx_import/
Source0:        https://github.com/ocaml-ppx/ppx_import/archive/%{version}/ppx_import-%{version}.tar.gz

BuildRequires:  ocaml >= 4.05.0
BuildRequires:  ocaml-dune >= 1.11.0
BuildRequires:  ocaml-ounit-devel
BuildRequires:  ocaml-ppx-deriving-devel >= 4.2.1
BuildRequires:  ocaml-ppx-sexp-conv-devel >= 0.13.0
BuildRequires:  ocaml-ppxlib-devel >= 0.26.0

%description
Import is an OCaml syntax extension that enables pulling in types or
signatures from other compiled interface files.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       ocaml-ppxlib-devel%{?_isa}

%description    devel
The %{name}-devel package contains libraries and signature
files for developing applications that use %{name}.

%prep
%autosetup -n ppx_import-%{version}

# Fix the ounit name
sed -i 's/oUnit/ounit2/' src_test/ppx_deriving/dune

%build
%dune_build

%install
%dune_install

%check
%dune_check

%files -f .ofiles
%doc CHANGES.md README.md
%license LICENSE.md

%files devel -f .ofiles-devel

%changelog
* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Dec 18 2023 Richard W.M. Jones <rjones@redhat.com> - 1.10.0-12
- OCaml 5.1.1 + s390x code gen fix for Fedora 40

* Tue Dec 12 2023 Richard W.M. Jones <rjones@redhat.com> - 1.10.0-11
- OCaml 5.1.1 rebuild for Fedora 40

* Thu Oct 05 2023 Richard W.M. Jones <rjones@redhat.com> - 1.10.0-10
- OCaml 5.1 rebuild for Fedora 40

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Jul 12 2023 Richard W.M. Jones <rjones@redhat.com> - 1.10.0-8
- OCaml 5.0 rebuild for Fedora 39

* Mon Jul 10 2023 Jerry James <loganjerry@gmail.com> - 1.10.0-7
- OCaml 5.0.0 rebuild

* Tue Jan 24 2023 Richard W.M. Jones <rjones@redhat.com> - 1.10.0-6
- Rebuild OCaml packages for F38

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Tue Nov  1 2022 Jerry James <loganjerry@gmail.com> - 1.10.0-4
- Rebuild for ocaml-ppxlib 0.28.0

* Thu Aug 18 2022 Jerry James <loganjerry@gmail.com> - 1.10.0-3
- Rebuild for ocaml-ppxlib 0.27.0

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jul  6 2022 Jerry James <loganjerry@gmail.com> - 1.10.0-1
- Initial RPM
