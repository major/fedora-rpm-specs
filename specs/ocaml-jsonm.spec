%ifnarch %{ocaml_native_compiler}
%global debug_package %{nil}
%endif

Name:           ocaml-jsonm
Version:        1.0.2
Release:        %autorelease
Summary:        Non-blocking streaming JSON codec for OCaml

License:        ISC
URL:            https://erratique.ch/software/jsonm
VCS:            git:https://erratique.ch/repos/jsonm.git
Source:         https://github.com/dbuenzli/jsonm/archive/v%{version}/jsonm-%{version}.tar.gz

# OCaml packages not built on i686 since OCaml 5 / Fedora 39.
ExcludeArch:    %{ix86}

BuildRequires:  ocaml >= 4.05.0
BuildRequires:  ocaml-compiler-libs
BuildRequires:  ocaml-findlib
BuildRequires:  ocaml-ocamlbuild
BuildRequires:  ocaml-rpm-macros
BuildRequires:  ocaml-topkg-devel >= 1.0.3
BuildRequires:  ocaml-uutf-devel >= 1.0.0

%description
Jsonm is an OCaml non-blocking streaming codec to decode and encode the
JSON data format.  It can process JSON text without blocking on IO and
without a complete in-memory representation of the data.

The uncut codec also processes whitespace and (non-standard) JSON with
JavaScript comments.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.

%prep
%autosetup -n jsonm-%{version}

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
ocaml pkg/pkg.ml build --tests true --dev-pkg false

%install
%ocaml_install

%check
ocaml pkg/pkg.ml test

%files -f .ofiles
%doc CHANGES.md README.md
%license LICENSE.md

%files devel -f .ofiles-devel

%changelog
%autochangelog
