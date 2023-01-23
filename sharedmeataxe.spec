Name:           sharedmeataxe
Version:        1.0.1
Release:        3%{?dist}
Summary:        Matrix representations over finite fields

License:        GPL-2.0-or-later
URL:            https://users.fmi.uni-jena.de/~king/SharedMeatAxe/
Source0:        https://github.com/simon-king-jena/SharedMeatAxe/releases/download/v%{version}/shared_meataxe-%{version}.tar.bz2
# Template for an environment modules file
Source1:        %{name}.module.in
# Prevent buffer overflows when writing strings.
# Sent upstream 26 Nov 2019.
Patch0:         %{name}-overflow.patch
# Fix the build on big endian machines.
Patch1:         %{name}-big-endian.patch

BuildRequires:  environment(modules)
BuildRequires:  doxygen-latex
BuildRequires:  gcc
BuildRequires:  help2man
BuildRequires:  make

Requires:       %{name}-libs%{?_isa} = %{version}-%{release}
Requires:       environment(modules)

# Due to conflicting man pages named zef.1
Conflicts:      rakudo-zef

%description
The SharedMeatAxe is a dynamic (shared) library together with a set of
programs for working with matrices over finite fields.  It is a fork of
the C MeatAxe, and differs from it mainly by the implementation of
asymptotically fast matrix multiplication and by providing a dynamic
(as opposed to static) library and an autotoolized build system.

MeatAxe's primary purpose is the calculation of modular character
tables, although it can be used for other purposes, such as
investigating subgroup structure, module structure etc.  Indeed, there
is a set of programs to compute automatically the submodule lattice of
a given module.

The primitive objects are of two types: matrices and permutations.
Permutation objects can be handled, but not as smoothly as you might
expect.  For example, it is hoped that programs such as split (zsp) and
multiply (zmu) will be able to work with mixed types, but at present
ZSP is restricted to matrices only, and ZMU can multiply a matrix by a
permutation, but not vice versa.

%package        devel
Summary:        Header files and libraries for SharedMeatAxe development
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

%description    devel
This package contains the header files and library links for building
applications that use the SharedMeatAxe library.

%package        libs
Summary:        Library of matrix representations over finite fields

%description    libs
This package contains the SharedMeatAxe library, which provides
functions for working with matrix representations over finite fields.
Permutation representations are supported to some extent, too.

%package        doc
# The content is GPL-2.0-or-later.  Other licenses are due to files installed
# by doxygen.
# html/bc_s.png: GPL-1.0-or-later
# html/bdwn.png: GPL-1.0-or-later
# html/closed.png: GPL-1.0-or-later
# html/doc.png: GPL-1.0-or-later
# html/doxygen.css: GPL-1.0-or-later
# html/doxygen.svg: GPL-1.0-or-later
# html/dynsections.js: MIT
# html/folderclosed.png: GPL-1.0-or-later
# html/folderopen.png: GPL-1.0-or-later
# html/jquery.js: MIT
# html/menu.js: MIT
# html/menudata.js: MIT
# html/nav_f.png: GPL-1.0-or-later
# html/nav_g.png: GPL-1.0-or-later
# html/nav_h.png: GPL-1.0-or-later
# html/navtree.css: GPL-1.0-or-later
# html/navtree.js: MIT
# html/open.png: GPL-1.0-or-later
# html/resize.js: MIT
# html/splitbar.png: GPL-1.0-or-later
# html/sync_off.png: GPL-1.0-or-later
# html/sync_on.png: GPL-1.0-or-later
# html/tab_a.png: GPL-1.0-or-later
# html/tab_b.png: GPL-1.0-or-later
# html/tab_h.png: GPL-1.0-or-later
# html/tab_s.png: GPL-1.0-or-later
# html/tabs.css: GPL-1.0-or-later
License:        GPL-2.0-or-later AND GPL-1.0-or-later AND MIT
Summary:        API documentation for %{name}
BuildArch:      noarch

%description    doc
API documentation for %{name}.

%prep
%autosetup -p0 -n shared_meataxe-%{version}

# Remove timestamp from the documentation for repeatable builds
sed -i 's/, generated on \$datetime//' etc/meataxe-footer.html

# Set the default binary directory
sed -i.orig 's,/usr/local/mtx/bin,%{_libdir}/%{name}/bin,' src/args.c
touch -r src/args.c.orig src/args.c
rm src/args.c.orig

%build
%configure --disable-silent-rules

# Get rid of undesirable hardcoded rpaths; workaround libtool reordering
# -Wl,--as-needed after all the libraries.
sed -e 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' \
    -e 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' \
    -e 's|CC=.g..|& -Wl,--as-needed|' \
    -i libtool

# Build the library and programs
%make_build

# Build the documentation
mkdir html
DOCDIR=$PWD/html SRCDIR=$PWD doxygen etc/Doxyfile

%install
%make_install

# We do not want the libtool archives
rm -f %{buildroot}%{_libdir}/*.la

# Move the binaries
mkdir -p %{buildroot}%{_libdir}/%{name}
mv %{buildroot}%{_bindir} %{buildroot}%{_libdir}/%{name}

# Install the environment modules file
mkdir -p %{buildroot}%{_modulesdir}
sed 's|@LIBDIR@|'%{_libdir}/%{name}'|' \
  < %{SOURCE1} > %{buildroot}%{_modulesdir}/%{name}-%{_arch}

# Generate the man pages
mkdir -p %{buildroot}%{_mandir}/man1
export LD_LIBRARY_PATH=$PWD/src/.libs
cd %{buildroot}%{_libdir}/%{name}/bin
for cmd in *; do
  help2man -N --version-string="%{version}" ./$cmd > \
    %{buildroot}%{_mandir}/man1/${cmd}.1
done
cd -

# Record the ZZZ value we built the library with
sed -e '/GCC/i#ifndef ZZZ\n#define ZZZ 0\n#endif' \
    -i %{buildroot}%{_includedir}/meataxe.h

%check
LD_LIBRARY_PATH=$PWD/src/.libs make check

%files
%doc NEWS
%{_modulesdir}/%{name}-%{_arch}
%{_libdir}/%{name}/
%{_mandir}/man1/cfcomp.1*
%{_mandir}/man1/chop.1*
%{_mandir}/man1/decomp.1*
%{_mandir}/man1/genmod.1*
%{_mandir}/man1/mkcycl.1*
%{_mandir}/man1/mkdotl.1*
%{_mandir}/man1/mkgraph.1*
%{_mandir}/man1/mkhom.1*
%{_mandir}/man1/mkhom_old.1*
%{_mandir}/man1/mkinc.1*
%{_mandir}/man1/mksub.1*
%{_mandir}/man1/mktree.1*
%{_mandir}/man1/orbrep.1*
%{_mandir}/man1/precond.1*
%{_mandir}/man1/pseudochop.1*
%{_mandir}/man1/pwkond.1*
%{_mandir}/man1/rad.1*
%{_mandir}/man1/soc.1*
%{_mandir}/man1/symnew.1*
%{_mandir}/man1/tcond.1*
%{_mandir}/man1/tuc.1*
%{_mandir}/man1/zad.1*
%{_mandir}/man1/zbl.1*
%{_mandir}/man1/zcf.1*
%{_mandir}/man1/zcl.1*
%{_mandir}/man1/zcp.1*
%{_mandir}/man1/zct.1*
%{_mandir}/man1/zcv.1*
%{_mandir}/man1/zef.1*
%{_mandir}/man1/zev.1*
%{_mandir}/man1/zfr.1*
%{_mandir}/man1/ziv.1*
%{_mandir}/man1/zkd.1*
%{_mandir}/man1/zmo.1*
%{_mandir}/man1/zmu.1*
%{_mandir}/man1/zmw.1*
%{_mandir}/man1/znu.1*
%{_mandir}/man1/zor.1*
%{_mandir}/man1/zpo.1*
%{_mandir}/man1/zpr.1*
%{_mandir}/man1/zpt.1*
%{_mandir}/man1/zqt.1*
%{_mandir}/man1/zro.1*
%{_mandir}/man1/zsc.1*
%{_mandir}/man1/zsi.1*
%{_mandir}/man1/zsp.1*
%{_mandir}/man1/zsy.1*
%{_mandir}/man1/ztc.1*
%{_mandir}/man1/zte.1*
%{_mandir}/man1/ztr.1*
%{_mandir}/man1/zts.1*
%{_mandir}/man1/zuk.1*
%{_mandir}/man1/zvp.1*

%files          libs
%doc AUTHORS README
%license COPYING
%{_libdir}/libmtx.so.0*

%files          devel
%doc ChangeLog
%{_includedir}/meataxe.h
%{_libdir}/libmtx.so

%files          doc
%doc html

%changelog
* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Dec 14 2022 Jerry James <loganjerry@gmail.com> - 1.0.1-2
- Use more explicit man and library globs in %%files
- Convert License tags to SPDX

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue Jul 19 2022 Jerry James <loganjerry@gmail.com> - 1.0.1-1
- Version 1.0.1
- Explicitly conflict with rakudo-zef

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Dec  7 2019 Jerry James <loganjerry@gmail.com> - 1.0-1
- Initial RPM
