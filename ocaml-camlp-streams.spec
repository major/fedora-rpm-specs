%undefine _package_note_flags

Name:           ocaml-camlp-streams
Version:        5.0.1
Release:        3%{?dist}
Summary:        Stream and Genlex libraries for OCaml

License:        LGPL-2.1-only WITH OCaml-LGPL-linking-exception
URL:            https://github.com/ocaml/camlp-streams
Source0:        %{url}/archive/v%{version}/camlp-streams-%{version}.tar.gz

BuildRequires:  ocaml >= 4.02.3
BuildRequires:  ocaml-dune >= 2.7

%description
The camlp-streams package provides two library modules:
- Stream: imperative streams, with in-place update and memoization of
  the latest element produced.
- Genlex: a small parameterized lexical analyzer producing streams of
  tokens from streams of characters.

The two modules are designed for use with Camlp4 and Camlp5:
- The stream patterns and stream expressions of Camlp4/Camlp5 consume
  and produce data of type `'a Stream.t`.
- The Genlex tokenizer can be used as a simple lexical analyzer for
  Camlp4/Camlp5-generated parsers.

The Stream module can also be used by hand-written recursive-descent
parsers, but is not very convenient for this purpose.

The Stream and Genlex modules have been part of the OCaml standard
library for a long time, and have been distributed as part of the core
OCaml system.  They will be removed from the OCaml standard library at
some future point, but will be maintained and distributed separately in
this camlp-streams package.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and signature
files for developing applications that use %{name}.

%prep
%autosetup -n camlp-streams-%{version}

%build
%dune_build

%install
%dune_install

%check
%dune_check

%files -f .ofiles
%doc CHANGES.md README.md
%license LICENSE

%files devel -f .ofiles-devel

%changelog
* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Mon Dec 12 2022 Jerry James <loganjerry@gmail.com> - 5.0.1-2
- Convert License tag to SPDX

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue Jul  5 2022 Jerry James <loganjerry@gmail.com> - 5.0.1-1
- Initial RPM (rhbz#2104283)
