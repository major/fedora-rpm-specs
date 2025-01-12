# OCaml packages not built on i686 since OCaml 5 / Fedora 39.
ExcludeArch: %{ix86}

%global giturl  https://github.com/ocaml/odoc

Name:           ocaml-odoc
Version:        2.4.4
Release:        %autorelease
Summary:        Documentation compiler for OCaml and Reason

# ISC: The project as a whole
# BSD-3-Clause: src/html_support_files/highlight.pack.js
License:        ISC AND BSD-3-Clause
URL:            https://ocaml.github.io/odoc/
VCS:            git:%{giturl}.git
Source:         %{giturl}/releases/download/%{version}/odoc-%{version}.tbz

BuildRequires:  jq
BuildRequires:  ocaml >= 4.02.0
BuildRequires:  ocaml-astring-devel
BuildRequires:  ocaml-bisect-ppx-devel > 2.5.0
BuildRequires:  ocaml-bos-devel
BuildRequires:  ocaml-camlp-streams-devel
BuildRequires:  ocaml-cmdliner-devel >= 1.0.0
BuildRequires:  ocaml-cppo >= 1.1.0
BuildRequires:  ocaml-crunch-devel > 2.0.0
BuildRequires:  ocaml-dune >= 3.7.0
BuildRequires:  ocaml-findlib
BuildRequires:  ocaml-fmt-devel
BuildRequires:  ocaml-fpath-devel
BuildRequires:  ocaml-mdx-devel
BuildRequires:  ocaml-ppx-expect-devel
BuildRequires:  ocaml-result-devel
BuildRequires:  ocaml-sexplib0-devel
BuildRequires:  ocaml-tyxml-devel >= 4.4.0
BuildRequires:  ocaml-yojson-devel >= 1.6.0

Requires:       ocaml-odoc-parser%{?_isa} = %{version}-%{release}

%description
This package contains odoc, a documentation generator for OCaml and
Reason.  It reads doc comments, delimited with `(** ... *)`, and outputs
HTML.  Text inside doc comments is marked up in ocamldoc syntax.

Odoc's main advantage over ocamldoc is an accurate cross-referencer,
which handles the complexity of the OCaml module system.  Odoc also
offers a good opportunity to improve HTML output compared to ocamldoc,
but this is very much a work in progress.

%package        devel
License:        ISC
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       %{name}-parser-devel%{?_isa} = %{version}-%{release}
Requires:       ocaml-astring-devel%{?_isa}
Requires:       ocaml-fmt-devel%{?_isa}
Requires:       ocaml-fpath-devel%{?_isa}
Requires:       ocaml-result-devel%{?_isa}
Requires:       ocaml-tyxml-devel%{?_isa}

%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.

%package        parser
License:        ISC
Summary:        Parser for OCaml documentation comments

%description    parser
Odoc-parser is a parser for odoc markup, which is an extension of the
original markup language parsed by ocamldoc.

OCaml code can contain specially formatted comments that are used to
document the interfaces of modules.  These comments are delimited by
`(**` and `*)`.  This parser is intended to be used to parse the
contents of these comments.

%package        parser-devel
Summary:        Development files for %{name}-parser
Requires:       %{name}-parser%{?_isa} = %{version}-%{release}
Requires:       ocaml-astring-devel%{?_isa}
Requires:       ocaml-camlp-streams-devel%{?_isa}
Requires:       ocaml-result-devel%{?_isa}

%description    parser-devel
The %{name}-parser-devel package contains libraries and signature
files for developing applications that use %{name}-parser.

%package        doc
License:        ISC
Summary:        Documentation for %{name}
BuildArch:      noarch

%description    doc
Documentation for %{name}.

%prep
%autosetup -n odoc-%{version}

%build
%dune_build @install @doc

%install
%dune_install -s

# Install the man page
mkdir -p %{buildroot}%{_mandir}/man1
_build/install/default/bin/odoc --help groff > %{buildroot}%{_mandir}/man1/odoc.1

# We don't want the benchmark package
rm -fr %{buildroot}%{ocamldir}/odoc-bench

%check
%dune_check

%files -f .ofiles-odoc
%doc CHANGES.md README.md
%license LICENSE
%{_mandir}/man1/odoc.1*

%files devel -f .ofiles-odoc-devel

%files parser -f .ofiles-odoc-parser
%license LICENSE

%files parser-devel -f .ofiles-odoc-parser-devel

%files doc
%doc _build/default/_doc/_html/*
%license LICENSE

%changelog
%autochangelog
