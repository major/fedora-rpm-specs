Name:           ocaml-intrinsics-kernel
Version:        0.17.1
Release:        %autorelease
Summary:        OCaml interface to CPU intrinsics

License:        MIT
URL:            https://github.com/janestreet/ocaml_intrinsics_kernel
VCS:            git:%{url}.git
Source:         %{url}/archive/v%{version}/ocaml_intrinsics_kernel-%{version}.tar.gz
# Use the popcnt instruction only if the running CPU supports it
Patch:          %{name}-popcnt.patch

# OCaml packages not built on i686 since OCaml 5 / Fedora 39.
ExcludeArch:    %{ix86}

BuildRequires:  ocaml >= 5.1.0
BuildRequires:  ocaml-dune >= 3.11.0

%description
The ocaml_intrinsics_kernel library provides an OCaml interface to operations
that have dedicated hardware instructions on some micro-architectures.
Currently, it provides the following operations:

- conditional select

See ocaml_intrinsics for details.  Unlike ocaml_intrinsics,
ocaml_intrinsics_kernel can be used by programs compiled to javascript.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.

%prep
%autosetup -n ocaml_intrinsics_kernel-%{version} -p1

%build
%dune_build

%install
%dune_install

%check
%dune_check

%files -f .ofiles
%doc README.md
%license LICENSE.md

%files devel -f .ofiles-devel

%changelog
%autochangelog
