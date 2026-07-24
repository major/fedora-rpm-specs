%ifnarch %{ocaml_native_compiler}
%global debug_package %{nil}
%endif

Name:           ocaml-b0
Version:        0.0.6
Release:        %autorelease
Summary:        Software construction and deployment kit

License:        ISC
# These files are not included in any binary RPM:
# BSD-2-Clause: src/std/vendor/xxhash.{c,h}
# CC0-1.0: test/example_*.ml
SourceLicense:  %{license} AND BSD-2-Clause AND CC0-1.0
URL:            https://erratique.ch/software/b0
VCS:            git:https://erratique.ch/repos/b0.git
Source:         %{url}/releases/b0-%{version}.tbz
# Unbundle xxhash
Patch:          %{name}-unbundle-xxhash.patch

# OCaml packages not built on i686 since OCaml 5 / Fedora 39.
ExcludeArch:    %{ix86}

BuildSystem:    topkg
BuildOption(build): --dev-pkg false
BuildOption(build): --tests true

BuildRequires:  ocaml >= 4.14.0
BuildRequires:  ocaml-cmdliner-devel >= 2.0.0
BuildRequires:  ocaml-compiler-libs
BuildRequires:  ocaml-findlib
BuildRequires:  ocaml-ocamlbuild
BuildRequires:  ocaml-rpm-macros
BuildRequires:  ocaml-topkg-devel >= 1.1.0
BuildRequires:  pkgconfig(libxxhash)

# ocamlfind is invoked at runtime
Requires:       ocaml-findlib%{?_isa}

%description
WARNING: this package is unstable and a work in progress.  Do not depend on it.

B0 describes software construction and deployments using modular and
customizable definitions written in OCaml.

B0 describes:

- Build environments.
- Software configuration, build and testing.
- Source and binary deployments.
- Software life-cycle procedures.

B0 also provides the B00 build library which provides arbitrary build
abstraction with reliable and efficient incremental rebuilds.  The B00 library
can be – and has been – used on its own to devise domain specific build
systems.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       %{name}-tools%{?_isa} = %{version}-%{release}
Requires:       ocaml-cmdliner-devel%{?_isa}

%description    devel
The %{name}-devel package contains libraries and signature
files for developing applications that use %{name}.

%package        tools
Summary:        Command line b0 tools
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    tools
The tools package contains the command line b0 tools; i.e., b0, b0-cache,
b0-hash, b0-log, b0-sttyle, and show-url.

%prep
%autosetup -n b0-%{version} -p1

# Ensure the bundled xxhash is not used
rm -rf src/std/vendor

%install -a
sed -i '\%%%{_bindir}%d' .ofiles

%check
OCAMLPATH=%{buildroot}%{ocamldir}:%{ocamldir} %{buildroot}%{_bindir}/b0 test

%files -f .ofiles
%license LICENSE.md
%doc README.md CHANGES.md
%exclude %{ocamldir}/b0/std/*.c

%files devel -f .ofiles-devel

%files tools
%{_bindir}/b0
%{_bindir}/b0-cache
%{_bindir}/b0-hash
%{_bindir}/b0-log
%{_bindir}/b0-sttyle
%{_bindir}/show-url

%changelog
%autochangelog
