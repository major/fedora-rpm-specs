# OCaml packages not built on i686 since OCaml 5 / Fedora 39.
ExcludeArch: %{ix86}

%ifnarch %{ocaml_native_compiler}
%global debug_package %{nil}
%endif

Name:           ocaml-uucd
Version:        15.0.0
Release:        %autorelease
Summary:        Unicode character database decoder for OCaml

License:        ISC
URL:            https://erratique.ch/software/uucd
Source0:        %{url}/releases/uucd-%{version}.tbz

BuildRequires:  ocaml >= 4.01.0
BuildRequires:  ocaml-findlib
BuildRequires:  ocaml-ocamlbuild
BuildRequires:  ocaml-topkg-devel >= 1.0.3
BuildRequires:  ocaml-xmlm-devel
BuildRequires:  python3

%description
Uucd is an OCaml module to decode the data of the Unicode character
database (http://www.unicode.org/reports/tr44/) from its XML
representation (http://www.unicode.org/reports/tr42/).  It provides
high-level (but not necessarily efficient) access to the data so that
efficient representations can be extracted.

Uucd is made of a single module, depends on Xmlm and is distributed
under the ISC license.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       ocaml-xmlm-devel%{?_isa}

%description    devel
The %{name}-devel package contains libraries and signature
files for developing applications that use %{name}.

%prep
%autosetup -n uucd-%{version}

%build
# Build the library and the tests
ocaml pkg/pkg.ml build --dev-pkg false --tests true

%install
# Install the library
mkdir -p %{buildroot}%{ocamldir}/uucd
cp -p _build/{opam,pkg/META} %{buildroot}%{ocamldir}/uucd
%ifarch %{ocaml_native_compiler}
cp -a _build/src/*.{a,cma,cmi,cmt,cmti,cmx,cmxa,cmxs,mli} \
  %{buildroot}%{ocamldir}/uucd
%else
cp -a _build/src/*.{cma,cmi,cmt,cmti,mli} %{buildroot}%{ocamldir}/uucd
%endif
%ocaml_files

%check
ocaml pkg/pkg.ml test

%files -f .ofiles
%license LICENSE.md
%doc README.md CHANGES.md

%files devel -f .ofiles-devel

%changelog
%autochangelog
