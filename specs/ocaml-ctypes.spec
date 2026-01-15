# OCaml packages not built on i686 since OCaml 5 / Fedora 39.
ExcludeArch: %{ix86}

%global giturl  https://github.com/yallop/ocaml-ctypes

Name:           ocaml-ctypes
Version:        0.24.0
Release:        %autorelease
Summary:        Combinators for binding to C libraries without writing any C

License:        MIT
URL:            https://yallop.github.io/ocaml-ctypes/
VCS:            git:%{giturl}.git
Source:         %{giturl}/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:  ocaml >= 4.07.0
BuildRequires:  ocaml-bisect-ppx-devel
BuildRequires:  ocaml-dune >= 3.9
BuildRequires:  ocaml-dune-configurator-devel
BuildRequires:  ocaml-integers-devel >= 0.2.2
BuildRequires:  ocaml-lwt-devel >= 2.4.7
BuildRequires:  ocaml-ounit-devel
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(libffi)
BuildRequires:  pkgconfig(ncurses)

# This can be removed when F42 reaches EOL
Obsoletes:      %{name}-doc < 0.21.0
Provides:       %{name}-doc = %{version}-%{release}

# Do not require ocaml-compiler-libs at runtime
%global __ocaml_requires_opts -i Asttypes -i Build_path_prefix_map -i Cmi_format -i Env -i Format_doc -i Ident -i Identifiable -i Load_path -i Location -i Longident -i Misc -i Oprint -i Outcometree -i Parsetree -i Path -i Primitive -i Shape -i Subst -i Toploop -i Type_immediacy -i Types -i Unit_info -i Warnings

%description
Ctypes is a library for binding to C libraries using pure OCaml.  The primary
aim is to make writing C extensions as straightforward as possible.

The core of ctypes is a set of combinators for describing the structure of C
types — numeric types, arrays, pointers, structs, unions and functions.  You
can use these combinators to describe the types of the functions that you want
to call, then bind directly to those functions — all without writing or
generating any C!

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       ocaml-integers-devel%{?_isa}

%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.

%prep
%autosetup -p1

%conf
# Use Fedora flags
sed -i 's/ "-cclib"; "-Wl,--no-as-needed";//' src/ctypes-foreign/config/discover.ml

%build
%dune_build

%install
%dune_install

%check
%dune_check

%files -f .ofiles
%license LICENSE
%doc CHANGES.md README.md

%files devel -f .ofiles-devel

%changelog
%autochangelog
