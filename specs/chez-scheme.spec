%if %{defined rhel} && "0%{?rhel}" < "10"
# Empty /builddir/build/BUILD/csv10.0.0/debugsourcefiles.list
%global debug_package %{nil}
%endif

Name:           chez-scheme
Summary:        Scheme incremental optimizing compiler
# need to rebuild dependents when bumping version: idris2 schemesh
# (`fedora-repoquery --koji rawhide --whatrequires chez-scheme`)
Version:        10.3.0
Release:        %autorelease
URL:            https://cisco.github.io/ChezScheme
# zlib and lz4 source are removed in prep
# $ licensecheck -r . | grep -v UNKNOWN | grep -v Apache
# ./nanopass/Copyright: MIT License
# ./stex/ReadMe: MIT License (unused)
# ./zuo/configure: FSF Unlimited License [generated file]
License:        Apache-2.0 AND MIT
Source0:        https://github.com/cisco/ChezScheme/releases/download/v%{version}/csv%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  libX11-devel
%ifarch ppc64le s390x
BuildRequires:  libffi-devel
%endif
BuildRequires:  lz4-devel
BuildRequires:  make
BuildRequires:  ncurses-devel
BuildRequires:  zlib-devel
Provides:       bundled(nanopass)

%description
Chez Scheme is both a programming language and an implementation of
that language, with supporting tools and documentation.

As a superset of the language described in the Revised6 Report on the
Algorithmic Language Scheme (R6RS), Chez Scheme supports all standard
features of Scheme, including first-class procedures, proper treatment
of tail calls, continuations, user-defined records, libraries,
exceptions, and hygienic macro expansion.

Chez Scheme also includes extensive support for interfacing with C and
other languages, support for multiple threads possibly running on
multiple cores, non-blocking I/O, and many other features.

The Chez Scheme implementation consists of a compiler, run-time
system, and programming environment. Although an interpreter is
available, all code is compiled by default. Source code is compiled
on-the-fly when loaded from a source file or entered via the shell. A
source file can also be precompiled into a stored binary form and
automatically recompiled when its dependencies change. Whether
compiling on the fly or precompiling, the compiler produces optimized
machine code, with some optimization across separately compiled
library boundaries. The compiler can also be directed to perform
whole-program compilation, which does full cross-library optimization
and also reduces a program and the libraries upon which it depends to
a single binary.

The run-time system interfaces with the operating system and supports,
among other things, binary and textual (Unicode) I/O, automatic
storage management (dynamic memory allocation and generational garbage
collection), library management, and exception handling. By default,
the compiler is included in the run-time system, allowing programs to
be generated and compiled at run time, and storage for dynamically
compiled code, just like any other dynamically allocated storage, is
automatically reclaimed by the garbage collector.

The programming environment includes a source-level debugger, a
mechanism for producing HTML displays of profile counts and program
"hot spots" when profiling is enabled during compilation, tools for
inspecting memory usage, and an interactive shell interface (the
expression editor, or "expeditor" for short) that supports multi-line
expression editing.


%package examples
Summary:        Chez-Scheme examples files
Requires:       %{name} = %{version}-%{release}
BuildArch:      noarch

%description examples
The package provides the examples files from Chez-Scheme.


# see https://github.com/cisco/ChezScheme/issues/836 for upstream discussion
%package devel
Summary:        Chez-Scheme development files
Requires:       %{name}%{?_isa} = %{version}-%{release}
Provides:       %{name}-static = %{version}-%{release}

%description devel
The package provides extra development files for Chez-Scheme.


%prep
%autosetup -n csv%{version} -p1
# use system libs
rm -r lz4 zlib

%build
case %{_arch} in
     x86_64) MACHINE=-m=ta6le ;;
     i386) MACHINE=-m=ti3le ;;
     aarch64) MACHINE=-m=tarm64le ;;
     riscv64) MACHINE=-m=trv64le ;;
     ppc64le) MACHINE="-m=tpb64l --enable-libffi" ;;
     s390x) MACHINE="-m=tpb64b --enable-libffi" ;;
esac

./configure --installbin=%{_bindir} --installlib=%{_libdir} --installman=%{_mandir} --temproot=%{buildroot} --threads $MACHINE ZLIB=-lz LZ4=-llz4
make ZUO_JOBS=$RPM_BUILD_NCPUS

%install
%make_install

chmod u+w %{buildroot}%{_libdir}/csv%{version}/*/{main.o,petite,scheme,scheme-script,lib*.a}

rm -rf %{buildroot}%{_libdir}/csv%{version}/examples


# https://github.com/cisco/ChezScheme/issues/956
%ifnarch ppc64le s390x
%check
make ZUO_JOBS=$RPM_BUILD_NCPUS test-some-fast
%endif


%files
%license LICENSE nanopass/Copyright
%doc *.md
%{_bindir}/petite
%{_bindir}/scheme
%{_bindir}/scheme-script
%{_libdir}/csv%{version}
%exclude %{_libdir}/csv%{version}/*/libkernel.a
%exclude %{_libdir}/csv%{version}/*/main.o
%exclude %{_libdir}/csv%{version}/*/scheme.h
%{_mandir}/man1/*.1.*


%files examples
%doc examples/*


%files devel
%{_libdir}/csv%{version}/*/libkernel.a
%{_libdir}/csv%{version}/*/main.o
%{_libdir}/csv%{version}/*/scheme.h


%changelog
%autochangelog
