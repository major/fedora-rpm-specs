%undefine _package_note_flags

%ifnarch %{ocaml_native_compiler}
%global debug_package %{nil}
%endif

Name:           ocaml-pp
Version:        1.1.2
Release:        5%{?dist}
Summary:        Pretty printing library for OCaml

License:        MIT
URL:            https://github.com/ocaml-dune/pp
Source0:        %{url}/releases/download/%{version}/pp-%{version}.tbz

BuildRequires:  ocaml >= 4.04.0
BuildRequires:  ocaml-dune >= 2.0

%description
This library provides a lean alternative to the Format [1] module of the
OCaml standard library.  It aims to make it easy for users to do the
right thing.  If you have tried Format before but find its API
complicated and difficult to use, then Pp might be a good choice for
you.

Pp uses the same concepts of boxes and break hints, and the final
rendering is done to formatter from the Format module.  However it
defines its own algebra which some might find easier to work with and
reason about.  No previous knowledge is required to start using this
library, however the various guides for the Format module such as this
one [2] should be applicable to Pp as well.

[1]: https://caml.inria.fr/pub/docs/manual-ocaml/libref/Format.html
[2]: https://caml.inria.fr/resources/doc/guides/format.en.html

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.

%prep
%autosetup -n pp-%{version}

%build
%dune_build

%install
%dune_install

%files -f .ofiles
%doc CHANGES.md README.md
%license LICENSE.md

%files devel -f .ofiles-devel

%changelog
* Tue Jan 24 2023 Richard W.M. Jones <rjones@redhat.com> - 1.1.2-5
- Rebuild OCaml packages for F38

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jul 20 2022 Jerry James <loganjerry@gmail.com> - 1.1.2-2
- Drop explicit python3 dependency

* Thu Jun 30 2022 Jerry James <loganjerry@gmail.com> - 1.1.2-2
- Drop support for building without dune
- Temporarily add python3 dependency until dune 3.x is bootstrapped

* Tue Jun 28 2022 Jerry James <loganjerry@gmail.com> - 1.1.2-1
- Initial RPM
