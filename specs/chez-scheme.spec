%if %{defined rhel} && "0%{?rhel}" < "10"
# Empty /builddir/build/BUILD/csv10.0.0/debugsourcefiles.list
%global debug_package %{nil}
%endif

Name:           chez-scheme
Summary:        Scheme incremental optimizing compiler
Version:        10.0.0
Release:        9%{?dist}
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
BuildRequires:  lz4-devel
BuildRequires:  make
BuildRequires:  ncurses-devel
BuildRequires:  zlib-devel
Provides:       bundled(nanopass)
# 10.0 fails with "illegal pb instruction"
ExcludeArch:    s390x

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
     i686) MACHINE=-m=ti3le ;;
     aarch64) MACHINE=-m=tarm64le ;;
     riscv64) MACHINE=-m=trv64le ;;
     *) MACHINE=--pb ;;
esac

./configure --installbin=%{_bindir} --installlib=%{_libdir} --installman=%{_mandir} --temproot=%{buildroot} --threads $MACHINE ZLIB=-lz LZ4=-llz4
make

%install
%make_install

chmod u+w %{buildroot}%{_libdir}/csv%{version}/*/{main.o,petite,scheme,scheme-script,lib*.a}

rm -rf %{buildroot}%{_libdir}/csv%{version}/examples


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
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 10.0.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 10.0.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jul 13 2024 Jens Petersen <petersen@redhat.com> - 10.0.0-7
- include nanopass Copyright file (#2281419, Benson Muite)
- drop bundled(stex) provides since not used

* Thu Jun 13 2024 Jens Petersen <petersen@redhat.com> - 10.0.0-6
- remove the isa suffix from the static provides

* Wed Jun 12 2024 Jens Petersen <petersen@redhat.com> - 10.0.0-5
- also subpackage the examples
- rename static to devel

* Wed Jun 12 2024 Jens Petersen <petersen@redhat.com> - 10.0.0-4
- add a static subpackage (#2281419, Benson Muite)

* Sat Jun  1 2024 Jens Petersen <petersen@redhat.com> - 10.0.0-3
- provides bundled(nanopass) and bundled(stex) (#2281419, Benson Muite)

* Sun May 19 2024 Jens Petersen <petersen@redhat.com> - 10.0.0-2
- add license and doc files (#2281419, Benson Muite)
- add source license comments (#2281419, Benson Muite)

* Sat May 18 2024 Jens Petersen <petersen@redhat.com> - 10.0.0-1
- update to 10.0.0
- https://cisco.github.io/ChezScheme/release_notes/v10.0/release_notes.html

* Sun Jan 21 2024 Quentin Dufour <quentin@dufour.io> - 9.6.4
- Skipped 4 versions (9.5.6, 9.5.8, 9.5.8a and 9.6.2)
- Check all the release notes: https://cisco.github.io/ChezScheme/release_notes/v9.6/release_notes.html

* Fri Nov 20 2020 Quentin Dufour <quentin@dufour.io> - 9.5.4
- Upgrade sources from 9.5.2 to 9.5.4 (there is no 9.5.3 release on github). Changelog is available here: https://github.com/cisco/ChezScheme/blob/v9.5.4/LOG

* Wed Jul 01 2020 Quentin Dufour <quentin@dufour.io> - 9.5.2-2
- Compile with thread support (appending --thread to ./configure), thanks Jens-Ulrik Peterson for the notification.

* Mon Jun 15 2020 Quentin Dufour <quentin@dufour.io> - 9.5.2-1
- Upgrade sources from 9.5 to 9.5.2. Changelog is avalaible here: https://github.com/cisco/ChezScheme/blob/v9.5.2/LOG
- Patch makefile to fix binary stripping on fedora rawhide that causes a fatal error

* Mon Jun 11 2018 Quentin Dufour <quentin@dufour.io> - 9.5-2
- Update symlink patch to use a hard link instead as recommended in https://github.com/cisco/ChezScheme/pull/307

* Sat May 19 2018 Quentin Dufour <quentin@dufour.io> - 9.5-1
- Initial packaging of Chez Scheme
