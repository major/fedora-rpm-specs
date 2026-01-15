# OCaml packages not built on i686 since OCaml 5 / Fedora 39.
ExcludeArch: %{ix86}

%ifnarch %{ocaml_native_compiler}
%global debug_package %{nil}
%endif

Name:           ocaml-uutf
Version:        1.0.4
Release:        %autorelease
Summary:        Non-blocking streaming Unicode codec for OCaml

License:        ISC
URL:            https://erratique.ch/software/uutf
VCS:            git:https://erratique.ch/repos/uutf.git
Source:         https://github.com/dbuenzli/uutf/archive/v%{version}/uutf-%{version}.tar.gz

BuildRequires:  ocaml >= 4.08.0
BuildRequires:  ocaml-cmdliner-devel >= 1.3.0
BuildRequires:  ocaml-findlib
BuildRequires:  ocaml-ocamlbuild
BuildRequires:  ocaml-ocamldoc
BuildRequires:  ocaml-rpm-macros
BuildRequires:  ocaml-topkg-devel >= 1.0.3

%description
Uutf is a non-blocking streaming codec to decode and encode the UTF-8, UTF-16,
UTF-16LE and UTF-16BE encoding schemes.  It can efficiently work character by
character without blocking on I/O.  Decoders perform character position
tracking and support newline normalization.

Functions are also provided to fold over the characters of UTF-encoded OCaml
string values and to directly encode characters in OCaml Buffer.t values.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.

%prep
%autosetup -n uutf-%{version} -p1

%conf
# Topkg does watermark replacements only if run inside a git checkout.  Github
# tarballs do not come with a .git directory.  Therefore, we do the watermark
# replacement manually.
for fil in $(find . -type f); do
  sed -e 's,%%%%VERSION%%%%,v%{version},' \
      -e 's,%%%%VERSION_NUM%%%%,%{version},' \
      -i.orig $fil
  touch -r $fil.orig $fil
  rm $fil.orig
done

%build
# Build the library and the tests
ocaml pkg/pkg.ml build --dev-pkg false --tests true --with-cmdliner true

# Build the documentation
mkdir html
ocamldoc -html -d html -I _build/src _build/src/uutf.mli

%install
%ocaml_install

%check
ocaml pkg/pkg.ml test

%files -f .ofiles
%doc CHANGES.md README.md
%license LICENSE.md

%files devel -f .ofiles-devel
%doc html/*

%changelog
%autochangelog
