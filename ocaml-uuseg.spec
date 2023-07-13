# OCaml packages not built on i686 since OCaml 5 / Fedora 39.
ExcludeArch: %{ix86}

%ifnarch %{ocaml_native_compiler}
%global debug_package %{nil}
%endif

Name:           ocaml-uuseg
Version:        15.0.0
Release:        %autorelease
Summary:        Unicode text segmentation for OCaml

License:        ISC
URL:            https://erratique.ch/software/uuseg
Source0:        %{url}/releases/uuseg-%{version}.tbz

BuildRequires:  ocaml >= 4.03.0
BuildRequires:  ocaml-cmdliner-devel >= 1.1.0
BuildRequires:  ocaml-findlib
BuildRequires:  ocaml-ocamlbuild
BuildRequires:  ocaml-topkg-devel >= 1.0.3
BuildRequires:  ocaml-uucp-devel >= 15.0.0
BuildRequires:  ocaml-uutf-devel >= 1.0.0
BuildRequires:  python3
BuildRequires:  unicode-ucd

%description
Uuseg is an OCaml library for segmenting Unicode text.  It implements
the locale-independent Unicode text segmentation algorithms
(http://www.unicode.org/reports/tr29/) to detect grapheme cluster, word
and sentence boundaries and the Unicode line breaking algorithm
(http://www.unicode.org/reports/tr14/) to detect line break
opportunities.

The library is independent from any IO mechanism or Unicode text data
structure and it can process text without a complete in-memory
representation.

Uuseg depends on Uucp and optionally on Uutf for support for OCaml UTF-X
encoded strings.  It is distributed under the ISC license.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       ocaml-uucp-devel%{?_isa}
Requires:       ocaml-uutf-devel%{?_isa}

%description    devel
The %{name}-devel package contains libraries and signature
files for developing applications that use %{name}.

%prep
%autosetup -n uuseg-%{version}

# Files needed for the tests
cp -p %{_datadir}/unicode/ucd/auxiliary/*BreakTest.txt test

%build
# Build the library and the tests
ocaml pkg/pkg.ml build --dev-pkg false --with-uutf true --with-cmdliner true \
  --tests true

%install
# Install the library
mkdir -p %{buildroot}%{ocamldir}/uuseg/string
cp -p _build/{opam,pkg/META} %{buildroot}%{ocamldir}/uuseg
%ifarch %{ocaml_native_compiler}
cp -a _build/src/*.{a,cma,cmi,cmt,cmti,cmx,cmxa,cmxs,mli} \
  %{buildroot}%{ocamldir}/uuseg
%else
cp -a _build/src/*.{cma,cmi,cmt,cmti,mli} %{buildroot}%{ocamldir}/uuseg
%endif
mv %{buildroot}%{ocamldir}/uuseg/uuseg_string.* \
   %{buildroot}%{ocamldir}/uuseg/string

%ocaml_files

%check
ocaml pkg/pkg.ml test

%files -f .ofiles
%license LICENSE.md
%doc CHANGES.md README.md

%files devel -f .ofiles-devel

%changelog
%autochangelog
