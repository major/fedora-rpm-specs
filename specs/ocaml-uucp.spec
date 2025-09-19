%ifnarch %{ocaml_native_compiler}
%global debug_package %{nil}
%endif

Name:           ocaml-uucp
Version:        17.0.0
Release:        %autorelease
Summary:        Unicode character properties for OCaml

License:        ISC
URL:            https://erratique.ch/software/uucp
VCS:            git:https://erratique.ch/repos/uucp.git
Source:         %{url}/releases/uucp-%{version}.tbz

# OCaml packages not built on i686 since OCaml 5 / Fedora 39.
ExcludeArch:    %{ix86}

BuildRequires:  ocaml >= 4.14.0
BuildRequires:  ocaml-cmdliner-devel >= 1.1.0
BuildRequires:  ocaml-compiler-libs
BuildRequires:  ocaml-findlib
BuildRequires:  ocaml-ocamlbuild
BuildRequires:  ocaml-rpm-macros
BuildRequires:  ocaml-topkg-devel >= 1.1.0
BuildRequires:  ocaml-uucd-devel >= 17.0.0
BuildRequires:  ocaml-uunf-devel

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
ocaml pkg/pkg.ml build --dev-pkg false --with-uunf true --with-cmdliner true \
  --tests true

%install
%ocaml_install

%check
ocaml pkg/pkg.ml test

%files -f .ofiles
%license LICENSE.md
%doc CHANGES.md README.md

%files devel -f .ofiles-devel

%changelog
%autochangelog
