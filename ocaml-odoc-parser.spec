%undefine _package_note_flags

%ifnarch %{ocaml_native_compiler}
%global debug_package %{nil}
%endif

Name:           ocaml-odoc-parser
Version:        2.0.0
Release:        4%{?dist}
Summary:        Parser for OCaml documentation comments

License:        ISC
URL:            https://ocaml-doc.github.io/odoc-parser/
Source0:        https://github.com/ocaml-doc/odoc-parser/releases/download/%{version}/odoc-parser-%{version}.tbz

BuildRequires:  ocaml >= 4.02.0
BuildRequires:  ocaml-astring-devel
BuildRequires:  ocaml-camlp-streams-devel
BuildRequires:  ocaml-dune >= 2.8
BuildRequires:  ocaml-ppx-expect-devel
BuildRequires:  ocaml-result-devel
BuildRequires:  ocaml-sexplib0-devel

%description
Odoc-parser is a parser for odoc markup, which is an extension of the
original markup language parsed by ocamldoc.

OCaml code can contain specially formatted comments that are used to
document the interfaces of modules.  These comments are delimited by
`(**` and `*)`.  This parser is intended to be used to parse the
contents of these comments.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       ocaml-astring-devel%{?_isa}
Requires:       ocaml-camlp-streams-devel%{?_isa}
Requires:       ocaml-result-devel%{?_isa}

%description    devel
The %{name}-devel package contains libraries and signature
files for developing applications that use %{name}.

%prep
%autosetup -n odoc-parser-%{version}

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
* Tue Jan 24 2023 Richard W.M. Jones <rjones@redhat.com> - 2.0.0-4
- Bump release and rebuild

* Tue Jan 24 2023 Richard W.M. Jones <rjones@redhat.com> - 2.0.0-3
- Rebuild OCaml packages for F38

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Tue Aug  2 2022 Jerry James <loganjerry@gmail.com> - 2.0.0-1
- Version 2.0.0

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jul 20 2022 Jerry James <loganjerry@gmail.com> - 1.0.0-4
- Use new OCaml macros

* Sun Jun 19 2022 Richard W.M. Jones <rjones@redhat.com> - 1.0.0-4
- OCaml 4.14.0 rebuild

* Fri Feb 04 2022 Richard W.M. Jones <rjones@redhat.com> - 1.0.0-3
- OCaml 4.13.1 rebuild to remove package notes

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Dec 31 2021 Jerry James <loganjerry@gmail.com> - 1.0.0-1
- Initial RPM
