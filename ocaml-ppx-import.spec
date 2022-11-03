%undefine _package_note_flags

Name:           ocaml-ppx-import
Version:        1.10.0
Release:        4%{?dist}
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
* Tue Nov  1 2022 Jerry James <loganjerry@gmail.com> - 1.10.0-4
- Rebuild for ocaml-ppxlib 0.28.0

* Thu Aug 18 2022 Jerry James <loganjerry@gmail.com> - 1.10.0-3
- Rebuild for ocaml-ppxlib 0.27.0

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jul  6 2022 Jerry James <loganjerry@gmail.com> - 1.10.0-1
- Initial RPM
