# OCaml packages not built on i686 since OCaml 5 / Fedora 39.
ExcludeArch: %{ix86}

%ifnarch %{ocaml_native_compiler}
%global debug_package %{nil}
%endif

Name:           ocaml-uucp
Version:        15.0.0
Release:        %autorelease
Summary:        Unicode character properties for OCaml

License:        ISC
URL:            https://erratique.ch/software/uucp
Source0:        %{url}/releases/uucp-%{version}.tbz

BuildRequires:  ocaml >= 4.03.0
BuildRequires:  ocaml-cmdliner-devel >= 1.1.0
BuildRequires:  ocaml-findlib
BuildRequires:  ocaml-ocamlbuild
BuildRequires:  ocaml-topkg-devel >= 1.0.3
BuildRequires:  ocaml-uucd-devel
BuildRequires:  ocaml-uunf-devel
BuildRequires:  ocaml-uutf-devel >= 1.0.1
BuildRequires:  python3

%description
Uucp is an OCaml library providing efficient access to a selection of
character properties of the Unicode character database
(http://www.unicode.org/reports/tr44/).

Uucp is independent from any Unicode text data structure and has no
dependencies.  It is distributed under the ISC license.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and signature
files for developing applications that use %{name}.

%prep
%autosetup -n uucp-%{version}

%build
# Build the library and the tests
ocaml pkg/pkg.ml build --dev-pkg false --with-uutf true --with-uunf true \
  --with-cmdliner true --tests true

%install
# Install the library
mkdir -p %{buildroot}%{ocamldir}/uucp
cp -p _build/{opam,pkg/META} %{buildroot}%{ocamldir}/uucp
%ifarch %{ocaml_native_compiler}
cp -a _build/src/*.{a,cma,cmi,cmt,cmti,cmx,cmxa,cmxs,mli} \
  %{buildroot}%{ocamldir}/uucp
%else
cp -a _build/src/*.{cma,cmi,cmt,cmti,mli} %{buildroot}%{ocamldir}/uucp
%endif
%ocaml_files

%check
ocaml pkg/pkg.ml test

%files -f .ofiles
%license LICENSE.md
%doc CHANGES.md README.md

%files devel -f .ofiles-devel

%changelog
%autochangelog
