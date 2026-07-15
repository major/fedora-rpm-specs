# Whether to run tests
%bcond ctest 1

Name:           breakid
Version:        3.1.3
Release:        %autorelease
Summary:        Symmetry detecting and breaking library

License:        MIT
# BSL-1.0: cmake/GetGitRevisionDescription.cmake*
# GPL-2.0-only: scripts/{fix_cnf,rem_dup_cls,xor_to_cnf}.py
# LGPL-3.0-only: src/bliss
# LicenseRef-Fedora-Public-Domain: cmake/FindPkgMacros.cmake
SourceLicense:  %{shrink:%{license}
                  AND BSL-1.0
                  AND GPL-2.0-only
                  AND LGPL-3.0-only
                  AND LicenseRef-Fedora-Public-Domain
                }
URL:            https://github.com/meelgroup/breakid
VCS:            git:%{url}.git
Source:         %{url}/archive/release/%{version}/%{name}-%{version}.tar.gz
# Do not change Fedora build flags
Patch:          %{name}-compiler-flags.patch
# Unbundle bliss, including updating from 0.73 to 0.77
Patch:          %{name}-unbundle-bliss.patch

# See https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}
BuildSystem:    cmake
BuildOption(conf): -DBREAKID_INSTALL_CMAKE_DIR:PATH=%{_lib}/cmake/breakid

BuildRequires:  bliss-devel
BuildRequires:  cmake(argparse)
BuildRequires:  gcc-c++
BuildRequires:  help2man

%description
BreakID is a symmetry detecting and breaking library for SAT solvers.  It is
based on Jo Devriendt's BreakID code.  It has been re-licensed by the original
author to be MIT.  All modifications by Mate Soos.

%package        devel
Summary:        Development files for breakid
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       bliss-devel%{?_isa}

%description    devel
Header files and library links for developing applications that use breakid.

%prep
%autosetup -n %{name}-release-%{version} -p1

# Make sure the bundled bliss cannot be used
rm -fr src/bliss

# Unbundle argparse
rm src/argparse.hpp
ln -s %{_includedir}/argparse/argparse.hpp src/argparse.hpp

# Fix end of line encoding
sed -i.orig 's/\r//' README.md
touch -r README.md.orig README.md
rm README.md.orig

%install -a
mkdir -p %{buildroot}%{_mandir}/man1
cd %{_vpath_builddir}
help2man -N --version-string=%{version} ./breakid \
  -n 'Symmetry detection and breaking' \
  -o %{buildroot}%{_mandir}/man1/breakid.1
cd -

%files
%doc README.md
%license LICENSE
%{_bindir}/breakid
%{_libdir}/libbreakid.so.3{,.*}
%{_mandir}/man1/breakid.1*

%files devel
%{_includedir}/%{name}/
%{_libdir}/cmake/%{name}/
%{_libdir}/libbreakid.so

%changelog
%autochangelog
