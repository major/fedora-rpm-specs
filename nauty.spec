Name:           nauty
Version:        2.8.6
Release:        1%{?dist}
Summary:        Graph canonical labeling and automorphism group computation

%global nautytarver %(tr . _ <<< %{version})

# The bundled cliquer code in nautycliquer.c is GPL-2.0-or-later, but we patch
# it out.
License:        Apache-2.0
URL:            https://pallini.di.uniroma1.it/
Source0:        https://pallini.di.uniroma1.it/%{name}%{nautytarver}.tar.gz

# Debian patch to fix the gt_numorbits declaration
Patch0:         %{name}-fix-gt_numorbits.patch
# Use zlib instead of invoking zcat through a pipe
Patch1:         %{name}-zlib-dimacs2g.patch
# Debian patch to improve usage and help information
Patch2:         %{name}-help2man.patch
# Debian patch to add libtool support for building a shared library
Patch3:         %{name}-autotoolization.patch
# Debian patch to canonicalize header file usage
Patch4:         %{name}-includes.patch
# Debian patch to prefix "nauty-" to the names of the generic tools
Patch5:         %{name}-tool-prefix.patch
# Detect availability of the popcnt instruction at runtime
Patch6:         %{name}-popcnt.patch
# Unbundle cliquer
Patch7:         %{name}-unbundle-cliquer.patch
# Fix incorrect printf format strings
Patch8:         %{name}-format.patch
# Fix uninitialized variable warnings
Patch9:         %{name}-uninitialized.patch
# Fix a function that can fall off the end
Patch10:        %{name}-fall-off.patch
# Mark functions as noreturn to improve compiler diagnostics
Patch11:        %{name}-noreturn.patch

BuildRequires:  cliquer-devel
BuildRequires:  gcc
BuildRequires:  gmp-devel
BuildRequires:  help2man
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  pkgconfig(zlib)

# Some version of planarity is bundled.  I do not know which version it is,
# but the interface is completely different from the one provided by Fedora's
# planarity package.
Provides:       bundled(planarity)

# The shortg program invokes sort.
Requires:       coreutils
Requires:       lib%{name}%{?_isa} = %{version}-%{release}

%description
Nauty and Traces are programs for computing automorphism groups of
graphs and digraphs.  (At present, Traces does not accept digraphs.)
They can also produce a canonical label.  They are written in a portable
subset of C, and run on a considerable number of different systems.

There is a small suite of programs called gtools included in the
package.  For example, geng can generate non-isomorphic graphs very
quickly.  There are also generators for bipartite graphs, digraphs, and
multigraphs, and programs for manipulating files of graphs in a compact
format.

%package -n libnauty
Summary:        Library for graph automorphism

%description -n libnauty
Nauty (No AUTomorphisms, Yes?) is a set of procedures for computing
automorphism groups of graphs and digraphs.  This package contains a
library of nauty procedures.

%package -n libnauty-devel
Summary:        Development files for libnauty
Requires:       lib%{name}%{?_isa} = %{version}-%{release}

%description -n libnauty-devel
This package contains files needed to develop programs that use libnauty.

%prep
%autosetup -p1 -n %{name}%{nautytarver}

# Remove the pregenerated makefile
rm -f makefile

# Regenerate the configure script with libtool support
autoreconf -fi

# Fix the pkgconfig file on 64-bit systems
if [ '%{_lib}' != 'lib' ]; then
    sed -i 's,/lib,/lib64,' nauty.pc
fi

%build
# The runtime popcnt support used to work for 32-bit x86 as well.  But then
# GCC 12 arrived, and the runtime popcnt support led to failing tests on CPUs
# that have the popcnt instruction.  I don't care enough about that platform
# to spend time debugging the issue.
export CFLAGS="%{build_cflags} -fwrapv -I%{_includedir}/cliquer"
%configure --disable-static --enable-generic \
%ifarch x86_64
    --enable-runtime-popcnt \
%endif
    --enable-tls

# Get rid of undesirable hardcoded rpaths; workaround libtool reordering
# -Wl,--as-needed after all the libraries.
sed -e 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' \
    -e 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' \
    -e 's|CC="\(.*g..\)"|CC="\1 -Wl,--as-needed"|' \
    -i libtool

%make_build

%install
%make_install

# We do not want the libtool archives
rm %{buildroot}%{_libdir}/*.la

# Link identical executables
rm %{buildroot}%{_bindir}/nauty-pickg
ln -s nauty-countg %{buildroot}%{_bindir}/nauty-pickg

%check
LD_LIBRARY_PATH=$PWD/.libs PATH=$PWD:$PATH make check

%files
%doc README nug28.pdf
%{_bindir}/dreadnaut
%{_bindir}/nauty-*
%{_mandir}/man1/dreadnaut.1*
%{_mandir}/man1/nauty-*.1*

%files -n libnauty
%doc changes24-28.txt formats.txt
%license COPYRIGHT
%{_libdir}/libnauty*.so.2*

%files -n libnauty-devel
%doc schreier.txt
%{_includedir}/nauty/
%{_libdir}/libnauty*.so
%{_libdir}/pkgconfig/%{name}.pc

%changelog
* Wed Nov 16 2022 Jerry James <loganjerry@gmail.com> - 2.8.6-1
- Version 2_8_6
- Convert License tag to SPDX

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jul  1 2022 Jerry James <loganjerry@gmail.com> - 2.7.4-1
- Version 2.7r4
- Add -fall-off and -noreturn patches

* Thu Jan 27 2022 Jerry James <loganjerry@gmail.com> - 2.7.3-2
- Disable popcnt support on i386 due to test failures
- Add -format and -uninitialized patches

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Mon Sep  6 2021 Jerry James <loganjerry@gmail.com> - 2.7.3-1
- Version 2.7.3

* Thu Sep  2 2021 Jerry James <loganjerry@gmail.com> - 2.7.2-1
- Version 2.7.2

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jan 05 2021 Timm Bäder <tbaeder@redhat.com> - 2.7.1-3
- Enable runtime popcount support on clang

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun  2 2020 Jerry James <loganjerry@gmail.com> - 2.7.1-1
- Version 2.7.1

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.12-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Oct 15 2019 Jerry James <loganjerry@gmail.com> - 2.6.12-1
- New upstream version

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.11-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Oct  6 2018 Jerry James <loganjerry@gmail.com> - 2.6.11-1
- New upstream version

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.10-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Oct 23 2017 Jerry James <loganjerry@gmail.com> - 2.6.10-1
- New upstream version

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sat Sep 10 2016 Jerry James <loganjerry@gmail.com> - 2.6.7-1
- New upstream version

* Thu Apr 21 2016 Jerry James <loganjerry@gmail.com> - 2.6.5-1
- New upstream version

* Fri Apr 15 2016 Jerry James <loganjerry@gmail.com> - 2.6.4-1
- Initial RPM
