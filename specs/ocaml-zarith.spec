# OCaml packages not built on i686 since OCaml 5 / Fedora 39.
ExcludeArch: %{ix86}

Name:           ocaml-zarith
Version:        1.14
Release:        %autorelease
Summary:        OCaml interface to GMP

License:        LGPL-2.1-only WITH OCaml-LGPL-linking-exception
URL:            https://github.com/ocaml/Zarith
VCS:            git:%{url}.git
Source:         %{url}/archive/release-%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  gmp-devel
BuildRequires:  make
BuildRequires:  ocaml >= 4.04.0
BuildRequires:  ocaml-findlib
BuildRequires:  ocaml-ocamldoc
BuildRequires:  ocaml-rpm-macros
BuildRequires:  perl-interpreter

# Replace config.guess with a more up to date version which knows about POWER.
BuildRequires:  redhat-rpm-config

# Do not require ocaml-compiler-libs at runtime
%global __ocaml_requires_opts -i Asttypes -i Build_path_prefix_map -i Cmi_format -i Env -i Format_doc -i Ident -i Identifiable -i Load_path -i Location -i Longident -i Misc -i Oprint -i Outcometree -i Parsetree -i Path -i Primitive -i Shape -i Subst -i Toploop -i Type_immediacy -i Types -i Unit_info -i Warnings

%description
This library implements arithmetic and logical operations over
arbitrary-precision integers.

The module is simply named "Z".  Its interface is similar to that of the
Int32, Int64 and Nativeint modules from the OCaml standard library, with
some additional functions.  See the file z.mlip for documentation.

The implementation uses GMP (the GNU Multiple Precision arithmetic
library) to compute over big integers.  However, small integers are
represented as unboxed Caml integers, to save space and improve
performance.  Big integers are allocated in the Caml heap, bypassing
GMP's memory management and achieving better GC behavior than e.g. the
MLGMP library.  Computations on small integers use a special, faster
path (coded in assembly for some platforms and functions) eschewing
calls to GMP, while computations on large integers use the low-level
MPN functions from GMP.

Arbitrary-precision integers can be compared correctly using OCaml's
polymorphic comparison operators (=, <, >, etc.).

Additional features include:
- a module Q for rationals, built on top of Z (see q.mli)
- a compatibility layer Big_int_Z that implements the same API as Big_int,
  but uses Z internally

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       gmp-devel%{?_isa}

%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.

%prep
%autosetup -n Zarith-release-%{version}

# Fix compilation flags
sed -i "s|^ccdef=''|ccdef='%{build_cflags}'|" configure
sed -i "s/-shared/-g &/" project.mak

%build
export CC="gcc"
# This is NOT an autoconf-generated configure script; %%configure doesn't work
./configure
# %%{?_smp_mflags} is not safe; same action performed by multiple CPUs
make
make doc

%install
mkdir -p %{buildroot}%{ocamldir}/stublibs
make install INSTALLDIR=%{buildroot}%{ocamldir}

# Install missing files
cp -p {big_int_Z,q,z}.cmt zarith_version.cm{i,t} zarith_top.{cm{i,t},ml} \
      z_mlgmpidl.mli %{buildroot}%{ocamldir}/zarith
cp -p zarith.opam %{buildroot}%{ocamldir}/zarith/opam

%ocaml_files

%ifarch %{ocaml_native_compiler}
# The tests assume the availability of ocamlopt
%check
export LD_LIBRARY_PATH=$PWD
make tests
%endif

%files -f .ofiles
%doc README.md
%license LICENSE

%files devel -f .ofiles-devel
%doc Changes html

%changelog
%autochangelog
