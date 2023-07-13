# OCaml packages not built on i686 since OCaml 5 / Fedora 39.
ExcludeArch: %{ix86}

%ifnarch %{ocaml_native_compiler}
%global debug_package %{nil}
%endif

Name:           ocaml-uunf
Version:        15.0.0
Release:        %autorelease
Summary:        Unicode text normalization for OCaml

License:        ISC
URL:            https://erratique.ch/software/uunf
Source0:        %{url}/releases/uunf-%{version}.tbz
# Test-only file
Source1:        https://www.unicode.org/Public/%{version}/ucd/NormalizationTest.txt
# Fix the test executable
# https://erratique.ch/repos/uunf/commit/?id=138dbfd1b847f23b1ed6cfc6ec746c9f8b0b2313
Patch0:         %{name}-test.patch

BuildRequires:  ocaml >= 4.03.0
BuildRequires:  ocaml-cmdliner-devel >= 1.1.0
BuildRequires:  ocaml-findlib
BuildRequires:  ocaml-ocamlbuild
BuildRequires:  ocaml-topkg-devel >= 1.0.3
BuildRequires:  ocaml-uucd-devel >= 15.0.0
BuildRequires:  ocaml-uutf-devel >= 1.0.0
BuildRequires:  python3

%description
Uunf is an OCaml library for normalizing Unicode text.  It supports all
Unicode normalization forms (http://www.unicode.org/reports/tr15/).  The
library is independent from any I/O mechanism or Unicode text data
structure and it can process text without a complete in-memory
representation.

Uunf depends only on Uutf for support of OCaml UTF-X encoded strings.
It is distributed under the ISC license.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       ocaml-uutf-devel%{?_isa}

%description    devel
The %{name}-devel package contains libraries and signature
files for developing applications that use %{name}.

%prep
%autosetup -n uunf-%{version} -p1
cp -p %{SOURCE1} test

%build
ocaml pkg/pkg.ml build \
  --dev-pkg false \
  --with-uutf true \
  --with-cmdliner true \
  --tests true

%install
# Install the binary
mkdir -p %{buildroot}%{_bindir}
%ifarch %{ocaml_native_compiler}
cp -p _build/test/unftrip.native %{buildroot}%{_bindir}/unftrip
%else
cp -p _build/test/unftrip.byte %{buildroot}%{_bindir}/unftrip
%endif

# Install the library
mkdir -p %{buildroot}%{ocamldir}/uunf/string
cp -p _build/{opam,pkg/META} %{buildroot}%{ocamldir}/uunf
%ifarch %{ocaml_native_compiler}
cp -p _build/src/*.{a,cma,cmi,cmt,cmti,cmx,cmxa,cmxs,mli} \
  %{buildroot}%{ocamldir}/uunf
%else
cp -a _build/src/*.{cma,cmi,cmt,cmti,mli} %{buildroot}%{ocamldir}/uunf
%endif
mv %{buildroot}%{ocamldir}/uunf/uunf_string.* \
   %{buildroot}%{ocamldir}/uunf/string

# Generate the man page
mkdir -p %{buildroot}%{_mandir}/man1
%{buildroot}/%{_bindir}/unftrip --help=groff > %{buildroot}%{_mandir}/man1/unftrip.1

%ocaml_files

%check
ocaml pkg/pkg.ml test

%files -f .ofiles
%license LICENSE.md
%doc README.md CHANGES.md

%files devel -f .ofiles-devel

%changelog
%autochangelog
