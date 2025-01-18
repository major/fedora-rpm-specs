%global major 0
%global libname lib%{name}
%global develname lib%{name}-devel

Name: freecell-solver
Version: 6.12.0
Release: 3%{?dist}
License: MIT
Source0: https://fc-solve.shlomifish.org/downloads/fc-solve/%{name}-%{version}.tar.xz
URL: https://fc-solve.shlomifish.org/
Summary: The Freecell Solver Executable

BuildRequires: cmake
BuildRequires: gcc
BuildRequires: gcc-c++
BuildRequires: gmp-devel
BuildRequires: gperf
BuildRequires: make
BuildRequires: perl(autodie)
BuildRequires: perl(Carp)
BuildRequires: perl(CHI)
BuildRequires: perl(Cwd)
BuildRequires: perl(Data::Dumper)
BuildRequires: perl(Digest::SHA)
BuildRequires: perl(Env::Path)
BuildRequires: perl(File::Path)
BuildRequires: perl(lib)
BuildRequires: perl(File::Spec)
BuildRequires: perl(File::Which)
BuildRequires: perl(Games::Solitaire::Verify)
BuildRequires: perl(Games::Solitaire::Verify::Solution)
BuildRequires: perl(Inline)
BuildRequires: perl(Inline::C)
BuildRequires: perl(IPC::Open2)
BuildRequires: perl(lib)
BuildRequires: perl(List::MoreUtils)
BuildRequires: perl(Moo)
BuildRequires: perl(MooX)
BuildRequires: perl(MooX::late)
BuildRequires: perl(parent)
BuildRequires: perl(Path::Tiny)
BuildRequires: perl(Storable)
BuildRequires: perl(strict)
BuildRequires: perl(String::ShellQuote)
# BuildRequires: perl(Task::FreecellSolver::Testing)
BuildRequires: perl(Template)
BuildRequires: perl(Test::Data::Split)
BuildRequires: perl(Test::Data::Split::Backend::Hash)
BuildRequires: perl(Test::Data::Split::Backend::ValidateHash)
BuildRequires: perl(Test::Differences)
BuildRequires: perl(Test::More)
%ifarch %{valgrind_arches}
BuildRequires: perl(Test::RunValgrind)
%endif
BuildRequires: perl(Test::TrailingSpace)
BuildRequires: perl(Test::Trap)
BuildRequires: perl(warnings)
BuildRequires: perl(YAML::XS)
BuildRequires: perl-devel
BuildRequires: pkgconfig(cmocka)
BuildRequires: pkgconfig(librinutils) >= 0.2.0
BuildRequires: python3-devel
BuildRequires: python3-cffi
BuildRequires: python3-freecell_solver
BuildRequires: python3-pysol-cards
BuildRequires: python3-random2
BuildRequires: python3-rpm-macros
BuildRequires: python3dist(six)
BuildRequires: python3dist(pycotap)
Requires: %{libname}%{?_isa} = %{version}-%{release}
# BuildRequires: tap-devel
BuildRequires: the_silver_searcher
%ifarch %{valgrind_arches}
BuildRequires: valgrind
%endif

%description
The Freecell Solver package contains the fc-solve executable which is
a command-line program that can be used to solve games of Freecell and
similar card solitaire variants.

This package also contains command line executables to generate the initial
boards of several popular Freecell implementations.

%files
%{_bindir}/dbm-fc-solver
%{_bindir}/depth-dbm-fc-solver
%{_bindir}/fc-solve
%{_bindir}/find-freecell-deal-index.py
%{_bindir}/freecell-solver-fc-pro-range-solve
%{_bindir}/freecell-solver-multi-thread-solve
%{_bindir}/freecell-solver-range-parallel-solve
%{_bindir}/gen-multiple-pysol-layouts
%{_bindir}/make_pysol_freecell_board.py
%{_bindir}/pi-make-microsoft-freecell-board
%{_bindir}/transpose-freecell-board.py
%{_mandir}/*/*
%{_docdir}/*

#--------------------------------------------------------------------

%package -n %{libname}
Summary: The Freecell Solver dynamic libraries for solving Freecell games
Requires: %{name}-data = %{version}-%{release}

%description -n %{libname}
Contains the Freecell Solver libraries that are used by some programs to solve
games of Freecell and similar variants of card solitaire.

This package is mandatory for the Freecell Solver executable too.

%files -n %{libname}
%doc COPYING.asciidoc
%{_libdir}/libfreecell-solver.so.%{major}{,.*}

#--------------------------------------------------------------------

%package -n %{name}-data
Summary: The Freecell Solver data files
BuildArch: noarch
%description -n %{name}-data
These are the presets for Freecell Solver

%files -n %{name}-data
%{_datadir}/freecell-solver/
%{python3_sitelib}/fc_solve_find_index_s2ints{.py,.pyc,.pyo}
%{python3_sitelib}/__pycache__/*

#--------------------------------------------------------------------

%package -n %{develname}
Summary: The Freecell Solver development tools for solving Freecell games
Requires: %{libname}%{?_isa} = %{version}-%{release}
Provides: %{name}-devel = %{version}-%{release}
Provides: %{name}-devel%{?_isa} = %{version}-%{release}

%description -n %{develname}
Freecell Solver is a library for automatically solving boards of Freecell and
similar variants of card Solitaire. This package contains the header files and
static libraries necessary for developing programs using Freecell Solver.

You should install it if you are a game developer who would like to use
Freecell Solver from within your programs.

%files -n %{develname}
%{_includedir}/freecell-solver/*.h
%{_libdir}/pkgconfig/*.pc
%{_libdir}/libfreecell-solver.so

#--------------------------------------------------------------------

%prep
%setup -q

%build
# The game limit flags are recommended by the PySolFC README.
%cmake -DLOCALE_INSTALL_DIR=%{_datadir}/locale -DLIB_INSTALL_DIR=%{_libdir} -DMAX_NUM_FREECELLS=8 -DMAX_NUM_STACKS=20 -DMAX_NUM_INITIAL_CARDS_IN_A_STACK=60 -DDISABLE_APPLYING_RPATH=TRUE
%cmake_build

%check
%ifnarch %{valgrind_arches}
export FCS_TEST_WITHOUT_VALGRIND=1
%endif
%__rm -f t/t/py-flake8.t t/t/tidyall.t
src="`pwd`"
cd "%{__cmake_builddir}"
perl "$src"/run-tests.pl

%install
%cmake_install
bn="fc_solve_find_index_s2ints.py"
dest="%{buildroot}/%{python3_sitelib}"
src="%{buildroot}/%{_bindir}/$bn"
mkdir -p "$dest"
%__perl -0777 -p -e 's=\A#!/usr/bin/env python3\r?\n==' < "$src" > "$dest"/"$bn"
rm -f "$src"
fn="%{buildroot}/%{_docdir}/%{name}/INSTALL"
rm -f "${fn}"
chmod a-x "$dest/$bn"
dir="%{buildroot}/%{_datadir}/freecell-solver/presets"
chmod a+x "${dir}"/*.sh
dir="%{buildroot}/%{_mandir}/man6"
mkdir -p "${dir}"
for prog in "depth-dbm-fc-solver" ; do
    printf ".so man6/%s\\n" "dbm-fc-solver" > "${dir}/${prog}.6"
done

for prog in "freecell-solver-fc-pro-range-solve" "freecell-solver-multi-thread-solve" ; do
    printf ".so man6/%s\\n" "freecell-solver-range-parallel-solve" > "${dir}/${prog}.6"
done

# Delete static libraries
find %{buildroot} -name *.a -delete

%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 6.12.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 6.12.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sun Jun 30 2024 Shlomi Fish <shlomif@shlomifish.org> 6.12.0-1
- New upstream version.

* Thu Jun 13 2024 Shlomi Fish <shlomif@shlomifish.org> 6.10.0-1
- New upstream version.
- Remove already-applied-upstream fc-solve-ptr-type.patch.

* Sat Jun 08 2024 Python Maint <python-maint@redhat.com> - 6.8.0-8
- Rebuilt for Python 3.13

* Fri May 31 2024 Shlomi Fish <shlomif@shlomifish.org> 6.8.0-7
- Add man-pages , *.sh files permissions , and other rpmlint warnings silencing.

* Tue Jan 30 2024 Shlomi Fish <shlomif@shlomifish.org> 6.8.0-7
- Add fc-solve-ptr-type.patch to fix GCC errors [FTFBS]

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 6.8.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 6.8.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 6.8.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Jul 05 2023 Python Maint <python-maint@redhat.com> - 6.8.0-3
- Rebuilt for Python 3.12

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 6.8.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Oct 20 2022 Shlomi Fish <shlomif@shlomifish.org> 6.8.0-1
- New version

* Wed Aug 03 2022 Shlomi Fish <shlomif@shlomifish.org> 6.6.0-3
- Add fc-solve-fix-ldd-issue.patch to fix run-tests.pl ldd-output processing
- Add BuildRequires on python3-devel.

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 6.6.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 6.6.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Sat Oct 09 2021 Shlomi Fish <shlomif@shlomifish.org> 6.6.0-1
- New version

* Tue Sep 28 2021 Shlomi Fish <shlomif@shlomifish.org> 6.4.0-1
- New version

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 6.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 6.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Oct 15 2020 Shlomi Fish <shlomif@shlomifish.org> 6.2.0-1
- New version

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 6.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sun Jul 26 2020 Shlomi Fish <shlomif@shlomifish.org> 6.0.1-1
- New version; convert to cmake macros.

* Tue Apr 14 2020 Shlomi Fish <shlomif@shlomifish.org> - 5.22.1-1
- New version

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 5.16.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 5.10.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Oct 19 2018 Shlomi Fish <shlomif@shlomifish.org> - 5.0.0-1
- Adapted from the Mageia .spec.
