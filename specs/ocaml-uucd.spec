%ifnarch %{ocaml_native_compiler}
%global debug_package %{nil}
%endif

Name:           ocaml-uucd
Version:        17.0.0
Release:        %autorelease
Summary:        Unicode character database decoder for OCaml

License:        ISC
URL:            https://erratique.ch/software/uucd
VCS:            git:https://erratique.ch/repos/uucd.git
Source:         %{url}/releases/uucd-%{version}.tbz

# OCaml packages not built on i686 since OCaml 5 / Fedora 39.
ExcludeArch:    %{ix86}

BuildRequires:  ocaml >= 4.08.0
BuildRequires:  ocaml-compiler-libs
BuildRequires:  ocaml-findlib
BuildRequires:  ocaml-ocamlbuild
BuildRequires:  ocaml-rpm-macros
BuildRequires:  ocaml-topkg-devel >= 1.1.0
BuildRequires:  ocaml-xmlm-devel

%description
Uucd is an OCaml module to decode the data of the Unicode character database
(http://www.unicode.org/reports/tr44/) from its XML representation
(http://www.unicode.org/reports/tr42/).  It provides high-level (but not
necessarily efficient) access to the data so that efficient representations
can be extracted.

Uucd is made of a single module, depends on Xmlm and is distributed under the
ISC license.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       ocaml-xmlm-devel%{?_isa}

%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.

%prep
%autosetup -n uucd-%{version}

%build
# Build the library and the tests
ocaml pkg/pkg.ml build --dev-pkg false --tests true

%install
%ocaml_install

%check
ocaml pkg/pkg.ml test

%files -f .ofiles
%license LICENSE.md
%doc README.md CHANGES.md

%files devel -f .ofiles-devel

%changelog
%autochangelog
