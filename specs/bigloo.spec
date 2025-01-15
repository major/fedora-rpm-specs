# The hardened build breaks bigloo's plugin architecture.
%undefine _hardened_build

# Bigloo uses the terminology "release" for what Fedora calls version,
# and "version" for a sub-version revision.
# patch_suffix is defined to be empty when patch_ver is not defined,
# so that when updating, the Source and %%setup lines do not have to be
# changed, only the Version and patch_ver
#%%global patch_ver 1
#%%global patch_suffix %%{?patch_ver:-%%{patch_ver}}

# For Emacs subpackages
%global pkg     %{name}
%global pkgname Bigloo

# Bigloo has a customized copy of gc
%bcond customgc 1
%global         bundledgc 8.2.2

# Bigloo bundles libbacktrace, which is intended to be a copylib
%bcond customlbt 1
%global         bundlelbt 1.0.20210529

Name:           bigloo
Version:        4.5b%{?patch_ver:.%{patch_ver}}
Release:        5%{?dist}
Summary:        A compiler for the Scheme programming language

# The compiler and tools are GPL-2.0-or-later.
# The runtime system and libraries are LGPL-2.0-or-later.
# Exceptions:
# - examples/Socket/socket.scm is some unknown form of BSD (not packaged)
# - runtime/Unsafe/sha2.scm is BSD-3-Clause
# - api/packrat/src/Llib/json.scm is MIT
# - api/packrat/src/Llib/packrat.scm is MIT
# - api/text/src/Llib/levenshtein.scm is LGPL-3.0-or-later
License:        GPL-2.0-or-later
URL:            https://www-sop.inria.fr/mimosa/fp/Bigloo
VCS:            git:https://github.com/manuel-serrano/bigloo.git
Source:         ftp://ftp-sop.inria.fr/indes/fp/Bigloo/%{name}-%{version}%{?patch_suffix}.tar.gz
# Not yet sent upstream: fix some bugs in the Emacs interface, and also
# modernizes the code somewhat.
Patch:          %{name}-emacs.patch
# Not yet sent upstream.  Support 64-bit stat on 32-bit platforms.
Patch:          %{name}-stat64.patch
# Not yet sent upstream: add some noreturn attributes
Patch:          %{name}-noreturn.patch
# Fix reading past the limits of a stack buffer
Patch:          %{name}-memread.patch
# Make type declarations match, silences LTO warning
Patch:          %{name}-lto-type.patch
# Make the test suite fail if individual tests fail
Patch:          %{name}-test.patch
# Round top of stack to a multiple of 1024.  Fixes stack overflow on s390x.
Patch:          %{name}-callcc.patch
# Adapt to Java 11
Patch:          %{name}-javac.patch
# Add some missing return statements
# https://github.com/manuel-serrano/bigloo/pull/115
Patch:          %{name}-return.patch
# Fix signal numbers in the Java code
Patch:          %{name}-java-signum.patch
# Adapt to changed semantics in C23, the default in GCC 15
Patch:          %{name}-gcc15.patch

# See https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}

BuildRequires:  emacs
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  gmp-devel
BuildRequires:  indent
%ifarch %{java_arches}
BuildRequires:  java-devel
BuildRequires:  javapackages-tools
%endif
BuildRequires:  libtool
%if %{without customlbt}
BuildRequires:  libbacktrace-devel
%endif
BuildRequires:  libunistring-devel
BuildRequires:  make
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(alsa)
%if %{with customgc}
BuildRequires:  pkgconfig(atomic_ops)
%endif
BuildRequires:  pkgconfig(avahi-client)
%if %{without customgc}
BuildRequires:  pkgconfig(bdw-gc)
%endif
BuildRequires:  pkgconfig(flac)
BuildRequires:  pkgconfig(gstreamer-1.0)
BuildRequires:  pkgconfig(gstreamer-audio-1.0)
BuildRequires:  pkgconfig(libmpg123)
BuildRequires:  pkgconfig(libpcre2-8)
#BuildRequires:  pkgconfig(libphidget22)
BuildRequires:  pkgconfig(libpulse)
BuildRequires:  pkgconfig(libuv)
BuildRequires:  pkgconfig(openssl)
BuildRequires:  pkgconfig(sqlite3)
BuildRequires:  texinfo-tex
BuildRequires:  texi2html
BuildRequires:  zip

Requires:       bigloo-libs%{?_isa} = %{version}-%{release}
Requires:       emacs-filesystem >= %{?_emacs_version}%{!?_emacs_version:0}
%ifarch %{java_arches}
Requires:       javapackages-filesystem
%endif
Requires:       indent
Requires:       gmp-devel%{?_isa}
%if %{without customgc}
Requires:       gc-devel%{?_isa}
%endif
Requires:       gcc
Requires:       glibc-devel%{?_isa}
%if %{with customgc}
Requires:       libatomic_ops-devel%{?_isa}
%endif
Requires:       libgcc%{?_isa}
Requires:       libunistring-devel%{?_isa}
Requires:       libuv-devel%{?_isa}

%if %{with customgc}
Provides:       bundled(gc) = %{bundledgc}
%endif

%if %{with customlbt}
Provides:       bundled(libbacktrace) = %{bundlelbt}
%global __provides_exclude libbacktrace.*
%global __requires_exclude libbacktrace.*
%endif

%description
Bigloo is a Scheme implementation devoted to one goal: enabling a Scheme
based programming style where C(++) is usually required.  Bigloo
attempts to make Scheme practical by offering features usually presented
by traditional programming languages but not offered by Scheme and
functional programming.  Bigloo compiles Scheme modules.  It delivers
small and fast standalone binary executables.  Bigloo enables full
connections between Scheme and C programs.


%package libs
Summary:        Bigloo runtime libraries
License:        LGPL-2.0-or-later AND LGPL-3.0-or-later AND BSD-3-Clause AND MIT

%description libs
Runtime libraries for Bigloo compiled programs.


%package doc
Summary:        Bigloo documentation
BuildArch:      noarch

%description doc
Documentation for the Bigloo compiler and integrated development
environment.


%prep
%autosetup -p0 -n %{name}-%{version}%{?patch_suffix}

%conf
# Remove an example with a dubious license
rm -fr examples/Socket

# encoding fixes
for f in README.md; do
  iconv -f ISO8859-1 -t UTF8 $f | sed 's/=ISO-8859-1/=UTF-8/' > $f.utf8
  touch -r $f $f.utf8
  mv -f $f.utf8 $f
done

# correct examples Makefiles for installation
find examples -name Makefile -exec \
  sed -i 's|include.*Makefile.config|include %{_libdir}/bigloo/%{version}/Makefile.config|g' {} +

# fix missing linkage
%if %{without customgc}
sed -i 's/^extralibs="-lm -lc"/extralibs="-lgc -lm -lc"/' configure
sed -i 's/LDOPTS=\"/&-Wl,--as-needed -lgc /' Makefile.misc
%endif

# Keep generated files for debuginfo
sed -i 's/fcfa-arithmetic/& -rm/' configure
sed -i 's/no-hello/& -rm/' bdb/bdb/Makefile
sed -i 's/-O2/& -rm/' cigloo/Makefile

# Remove warning flags not recognized by gcc
sed -i 's/ -Wno-parentheses-equality//;s/ -Wno-invalid-source-encoding//' \
    autoconf/ccwarning

%build
%define inplace $PWD/inplace

# Large stack needed to build
ulimit -s unlimited

# Enable UTF-8 filename support
export LOCALE="C.utf8"
# The sources are not ready for C23
export CFLAGS="%{build_cflags} -std=gnu17 -D_GNU_SOURCE=1 -fwrapv -Wno-unused"
sed -i 's/TLS=thread_local/TLS=_Thread_local/;s/"thread_local"/"_Thread_local"/' autoconf/pthreadlocalstorage

# Build blib with the correct flags
sed -i "s|^CFLAGS.*|& $CFLAGS|" bdb/blib/Makefile

export LDFLAGS="-Wl,-z,relro -Wl,--as-needed"
./configure \
        --prefix=%{_prefix} \
        --bindir=%{_bindir} \
        --libdir=%{_libdir} \
        --mandir=%{_mandir}/man1 \
        --infodir=%{_infodir} \
        --docdir=%{_docdir} \
        --lispdir=%{_emacs_sitelispdir}/bigloo \
%ifarch %{java_arches}
        --jvm=yes \
        --javaprefix=%{_jvmdir}/java/bin \
%else
        --jvm=no \
%endif
        --bee=full \
        --customgc=%{?with_customgc:yes}%{!?with_customgc:no} \
        --customlibbacktrace=%{?with_customlbt:yes}%{!?with_customlbt:no} \
        --coflags="$CFLAGS" \
        --cpicflags="-fPIC" \
        --sharedbde=yes \
        --sharedcompiler=yes \
        --native-default-backend \
        --customgmp=no \
        --customlibuv=no \
        --strip=no \
        --configureinfo=yes

# Remove extraneous rpath
sed -i '/^RPATH=/s,\$(DESTDIR).*:,,' Makefile.config

%if %{with customlbt}
# Fix broken link line for the bundled libbacktrace
sed -i 's/-llibbacktrace/$(LDBUILDOPTS) -lbacktrace/' Makefile.config
%endif

# _smp_mflags breaks the build
LD_LIBRARY_PATH=$PWD/lib/bigloo/%{version} make
LD_LIBRARY_PATH=$PWD/lib/bigloo/%{version} \
    BIGLOOLIB=%{inplace}%{_libdir}/bigloo/%{version} \
    make DESTDIR=%{inplace} install
LD_LIBRARY_PATH=$PWD/lib/bigloo/%{version} \
    PATH=$PWD/bin:$PATH \
    BIGLOOLIB=%{inplace}%{_libdir}/bigloo/%{version} \
    make compile-bee

# Other permissions are missing from a lot of files
chmod -R o+r .


%install
mkdir -p %{buildroot}%{_emacs_sitelispdir}/bigloo
env LD_LIBRARY_PATH=$PWD/lib/bigloo/%{version} %make_install
env LD_LIBRARY_PATH=$PWD/lib/bigloo/%{version} \
    make DESTDIR=%{buildroot} EMACSDIR=%{_emacs_sitelispdir}/bigloo install-bee
make -C manuals DESTDIR=%{buildroot} install-bee

# Remove empty directory
rmdir %{buildroot}%{_libdir}/pkgconfig

# fix permissions
chmod 755 %{buildroot}%{_bindir}/*
find %{buildroot}%{_libdir} -name \*.so -exec chmod 755 {} +

%ifarch %{java_arches}
# move jigloo to the proper place
mkdir %{buildroot}%{_javadir}
mv %{buildroot}%{_bindir}/jigloo.class %{buildroot}%{_javadir}
%endif

# Remove references to the build root
sed -e 's|^BOOTDIR=.*|BOOTDIR=%{_prefix}|g' \
    -e 's|^BOOTBINDIR=.*|BOOTBINDIR=%{_bindir}|g' \
    -e 's|^BOOTLIBDIR=.*|BOOTLIBDIR=%{_libdir}/bigloo/%{version}|g' \
    -e 's|^BGLBUILDBINDIR=.*|BGLBUILDBINDIR=%{_bindir}|g' \
    -e 's|^BGLBUILDLIBDIR=.*|BGLBUILDLIBDIR=%{_libdir}/bigloo/%{version}|g' \
    -e 's|^\(BIGLOO=.*\)\.sh|\1|' \
    -e 's|^\(BGL.*=.*\)\.sh|\1|' \
    -i %{buildroot}%{_libdir}/bigloo/%{version}/Makefile.config

# Remove references to the build root and the build directory
sed -i 's|\(LIBRARY_PATH=\).*|\1%{_libdir}/bigloo/%{version}:$LD_LIBRARY_PATH|' \
    %{buildroot}%{_bindir}/*.sh

# Fix symlinks that point to the buildroot
for link in $(find %{buildroot}%{_libdir} -type l); do
    target=$(readlink $link)
    if [[ "$target" =~ "%{buildroot}" ]]; then
        rm $link
	ln -s $(basename $target) $link
    fi
done

rm -fr %{buildroot}%{_infodir}/dir %{buildroot}%{_datadir}/doc

# emacs
mkdir -p %{buildroot}%{_emacs_sitestartdir}
cat > %{buildroot}%{_emacs_sitestartdir}/bigloo.el <<EOF
(require 'bmacs)
EOF
pushd %{buildroot}%{_emacs_sitelispdir}/bigloo
rm -f bmacs-xemacs.el xemacs-etags.el
%{_emacs_bytecompile} bmacs.el bmacs-config.el bmacs-gnu-emacs.el
popd

# FIXME: Unexplained segfaults when running tests on ppc64le
%ifnarch %{power64}
%check
ulimit -s unlimited
export TZ=$(date +%%Z)
# Starting with the F38 mass rebuild, "make test" fails due to stdout being
# closed unexpectedly.  This only happens if the tests are run via make.
# The commands below are the exact ones that make executes, but they succeed
# if run this way.  Investigation continues.
NATIVEBACKEND=$(sed -n 's/NATIVEBACKEND=\(.*\)/\1/p' Makefile.config)
JVMBACKEND=$(sed -n 's/JVMBACKEND=\(.*\)/\1/p' Makefile.config)
cd recette
if [ "$NATIVEBACKEND" = yes ]; then
  make recette-static
  ../bin/bglrun.sh ./recette-static
fi
cd -
if [ "$JVMBACKEND" = yes ]; then
  make jvm-test
fi
%endif


%files
%{_bindir}/bdb
%{_bindir}/bgl*
%{_bindir}/bigloo*
%{_bindir}/cigloo
%ifarch %{java_arches}
%{_javadir}/jigloo.class
%endif
%{_infodir}/bdb.info*
%{_infodir}/bigloo.info*
%{_mandir}/man1/bgl*
%{_mandir}/man1/bigloo.1*
%{_emacs_sitelispdir}/bigloo/
%{_emacs_sitestartdir}/bigloo.el
%doc ChangeLog Makefile.config examples
%doc README*


%files libs
%{_libdir}/bigloo/
%license LICENSE COPYING


%files doc
%doc manuals/*.html
%license LICENSE COPYING


%changelog
* Mon Jan 13 2025 Jerry James <loganjerry@gmail.com> - 4.5b-5
- Fix the build with GCC 15 (rhbz#2336442)

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.5b-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed May 22 2024 Jerry James <loganjerry@gmail.com> - 4.5b-4
- Remove references to build directory in /usr/bin (bz 2282390)

* Tue Jan 23 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.5b-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.5b-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Tue Dec 26 2023 Jerry James <loganjerry@gmail.com> - 4.5b-1
- Version 4.5b
- Drop upstreamed configure-c99 and emacs29 patches

* Fri Dec  1 2023 Jerry James <loganjerry@gmail.com> - 4.5a-4.1
- Fix potential GCC 14 errors
- Support Emacs 29
- Stop building for 32-bit x86

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 4.5a-3.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 4.5a-2.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Tue Jan 10 2023 Jerry James <loganjerry@gmail.com> - 4.5a-1.1
- Version 4.5a-1
- Drop upstreamed patches: emacs28, bde-bmem-c99
- Do not build on ppc64le until we can diagnose a segfault
- Minor spec file cleanups

* Fri Dec  9 2022 Florian Weimer <fweimer@redhat.com> - 4.4c-9.4
- Minor fixes for C99 compatibility

* Tue Sep 13 2022 Michel Alexandre Salim <salimma@fedoraproject.org> - 4.4c-8.4
- Rebuilt for flac 1.4.0

* Mon Aug 22 2022 Jerry James <loganjerry@gmail.com> - 4.4c-7.4
- Remove libphidget support until upstream migrates from 21 to 22

* Mon Aug 15 2022 Jerry James <loganjerry@gmail.com> - 4.4c-6.4
- Convert License field to SPDX

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.4c-6.4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jul 18 2022 Jerry James <loganjerry@gmail.com> - 4.4c-5.4
- Fix build with Emacs 28

* Tue Jul  5 2022 Jerry James <loganjerry@gmail.com> - 4.4c-5.4
- Remove Java support on i686 (rhbz#2104022)

* Mon Mar 28 2022 Jerry James <loganjerry@gmail.com> - 4.4c-4.4
- Version 4.4c-4

* Sat Feb 05 2022 Jiri Vanek <jvanek@redhat.com> - 4.4c-3.2
- Rebuilt for java-17-openjdk as system jdk

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.4c-2.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Dec 29 2021 Jerry James <loganjerry@gmail.com> - 4.4c-1.2
- Version 4.4c-2
- Drop obsolete -div-by-zero patch
- Disable LTO again due to symbol collision errors
- Reenable tests on s390x

* Tue Nov  9 2021 Jerry James <loganjerry@gmail.com> - 4.4b-4
- Drop XEmacs support

* Tue Sep 14 2021 Sahana Prasad <sahana@redhat.com> - 4.4b-3
- Rebuilt with OpenSSL 3.0.0

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.4b-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Feb  5 2021 Jerry James <loganjerry@gmail.com> - 4.4b-1
- Version 4.4b
- Drop $date-is-gmt workaround
- Add -div-by-zero patch to work around test failures
- Disable tests on s390x until a Java mutex problem can be diagnosed

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.4a-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Jan 23 2021 Jerry James <loganjerry@gmail.com> - 4.4a-1
- Version 4.4a
- Drop upstreamed -format, -params, -sigtrap, and -underlink patches
- Add -lto-type patch to silence LTO warnings
- Install libraries with upstream's choice of names and places

* Wed Oct 21 2020 Jerry James <loganjerry@gmail.com> - 4.3h-8
- Re-enable LTO on aarch64 and ppc64le
- Improve the -emacs patch
- Fix LTO warnings about mismatched types by adding to the -params patch
- Add the -return, -java-signum, and -sigtrap patches
- Drop division by zero workaround, fixed with the -sigtrap patch
- Move license files to -libs and -doc subpackages

* Fri Oct 09 2020 Jeff Law <law@redhat.com> - 4.3h-7
- Re-enable LTO except on aarch64 and ppc64le

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.3h-6
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.3h-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 21 2020 Jerry James <loganjerry@gmail.com> - 4.3h-4
- Support Java 11

* Mon Jul 13 2020 Jeff Law <law@redhat.com> - 4.3h-3
- Disable LTO

* Fri Jul 10 2020 Jiri Vanek <jvanek@redhat.com> - 4.3h-2
- Rebuilt for JDK-11, see https://fedoraproject.org/wiki/Changes/Java11

* Thu May 14 2020 Jerry James <loganjerry@gmail.com> - 4.3h-1
- Update to 4.3h
- Drop upstreamed -gstreamer1 and -return patches

* Wed Mar  4 2020 Jerry James <loganjerry@gmail.com> - 4.3g-2
- Fix the library sonames

* Fri Feb 28 2020 Jerry James <loganjerry@gmail.com> - 4.3g-1
- Update to 4.3g
- Use the bundled gc again for performance reasons

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.3f-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Nov 21 2019 Jerry James <loganjerry@gmail.com> - 4.3f-3
- Fix underlinked plugins
- Port gstreamer plugin to 1.0 (gstreamer1)
- Move the jigloo class to the Java directory
- Go back to the system gc; the bundled version is too buggy

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.3f-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Jul  5 2019 Jerry James <loganjerry@gmail.com> - 4.3f-1
- Update to 4.3f
- Drop dbus-devel BR; the dbus module is not yet buildable

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.3e-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Jan 30 2019 Jerry James <loganjerry@gmail.com> - 4.3e-1
- Update to 4.3e
- Build with custom GC for performance reasons
- Add -return, -memread, and -params patches to fix runtime issues
- Add -test patch to make %%check exit on test failure (bz 1663605)
- Unlimit stack usage in the check script for s390x

* Sat Jan  5 2019 Tim Landscheidt <tim@tim-landscheidt.de> - 4.3c-2
- Do not set LD_LIBRARY_PATH in %%check

* Fri Jan  4 2019 Tim Landscheidt <tim@tim-landscheidt.de> - 4.3c-2
- Fix setting compiling user for XEmacs byte-compiled files

* Sat Sep 15 2018 Jerry James <loganjerry@gmail.com> - 4.3c-1
- Update to 4.3c

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.3b-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat Jun 16 2018 Jerry James <loganjerry@gmail.com> - 4.3b-1
- Update to 4.3b
- Drop upstreamed -endian patch
- Add -noreturn patch to silence compiler warnings
- Remove scriptlets that call install-info
- Use ldconfig_scriptlets

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.3a-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 17 2017 Jerry James <loganjerry@gmail.com> - 4.3a-3
- Add -endian patch to fix s390x build
- Build for ppc64 as well, since the -endian patch fixed that too

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.3a-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.3a-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Jul 22 2017 Jerry James <loganjerry@gmail.com> - 4.3a-1
- Update to 4.3a
- Drop upstreamed -nameser, -openssl11, and -emacs25 patches
- Add -fwrapv to CFLAGS to address overflow in the Unicode code
- Enable pulseaudio and mpg123 support

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.2c-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 4.2c-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Dec 23 2015 Jerry James <loganjerry@gmail.com> - 4.2c-1
- Update to 4.2c (bz 1264055)

* Tue Oct 27 2015 Jerry James <loganjerry@gmail.com> - 4.2b-1
- Update to 4.2b (bz 1264055)

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.1a-9.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Apr 11 2015 Jerry James <loganjerry@gmail.com> - 4.1a-8.2
- Adapt to new (X)Emacs packaging guidelines
- Do not link with -z now, breaks the configure script and module loading

* Mon Feb  9 2015 Jerry James <loganjerry@gmail.com> - 4.1a-7.2
- Fix build failure due to lack of -fPIC
- Use license macro

* Tue Sep  2 2014 Jerry James <loganjerry@gmail.com> - 4.1a-6.2
- Rebuild for libunistring soname bump

* Fri Aug 15 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.1a-5.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Thu Jun 26 2014 Jerry James <loganjerry@gmail.com> - 4.1a-4.2
- Library renaming must be done in the version-specific directory too

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.1a-3.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon Mar  3 2014 Jerry James <loganjerry@gmail.com> - 4.1a-2.2
- Update to 4.1a-2 bug fix release

* Mon Feb 24 2014 Jerry James <loganjerry@gmail.com> - 4.1a-2
- Main package now Requires libunistring-devel

* Thu Feb 20 2014 Jerry James <loganjerry@gmail.com> - 4.1a-1
- Update to 4.1a
- Add libunistring-devel BR
- Set LOCALE when configuring for UTF-8 filename support

* Fri Aug  2 2013 Jerry James <loganjerry@gmail.com> - 4.0b-1
- Update to 4.0b
- Add -stat64 patch and build with -D_FILE_OFFSET_BITS=64
- Fix the xemacs version of bmacs-config.el

* Wed Feb  6 2013 Jerry James <loganjerry@gmail.com> - 4.0a-1
- Update to 4.0a
- Add texinfo-tex and texi2html BRs for documentation

* Mon Nov 19 2012 Michel Salim <salimma@fedoraproject.org> - 3.9b-0.1.20121118alpha
- Update to 3.9b snapshot

* Tue Oct 23 2012 Jerry James <loganjerry@gmail.com> - 3.9a-1
- Update to 3.9a
- Don't require a multilib gcc, but rather multilib libgcc and glibc
- Enable libphidget and pcre support
- Don't define BIGLOOLIB while compiling; it breaks the build

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.8c-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Jul  2 2012 Michel Salim <salimma@fedoraproject.org> - 3.8c-1
- Update to 3.8c

* Thu May  3 2012 Jerry James <loganjerry@gmail.com> - 3.8b-1
- Update to 3.8b
- Drop upstreamed JDK 1.7 patch

* Fri Mar 30 2012 Jerry James <loganjerry@gmail.com> - 3.8a-1.2
- Update to 3.8a-2
- Drop upstreamed java SSL patch
- Create (X)Emacs install dirs to avoid occasional build failure

* Fri Mar 23 2012 Jerry James <loganjerry@gamil.com> - 3.8a-1
- Update to 3.8a
- Drop upstreamed patches
- Add avahi-devel BR for new API

* Mon Jan  9 2012 Jerry James <loganjerry@gmail.com> - 3.7a-3
- Rebuild for GCC 4.7
- Drop unnecessary BRs

* Wed Nov 23 2011 Jerry James <loganjerry@gmail.com> - 3.7a-2
- Fix (X)Emacs installations (bz 754592)
- Refresh sendfile patch to match upstream's version

* Thu Oct 20 2011 Marcela Mašláňová <mmaslano@redhat.com> - 3.7a-1.2
- rebuild with new gmp without compat lib

* Mon Oct 10 2011 Peter Schiffer <pschiffe@redhat.com> - 3.7a-1.1
- rebuild with new gmp

* Mon Sep 26 2011 Jerry James <loganjerry@gmail.com> - 3.7a-1
- Update to 3.7a
- New source URL
- Drop unnecessary spec file elements (BuildRoot, defattr, etc.)
- Reenable XEmacs subpackages
- Fix more files with non-UTF-8 encodings
- Four patches to fix problems encountered with the new version
- Add alsa-lib-devel, dbus-devel, and flac-devel BRs for new APIs
- The obsoletes were needed for now EOL Fedora releases; remove them
- Add check script

* Mon Feb 14 2011 Gérard Milmeister <gemi@bluewin.ch> - 3.6a-1
- Update to 3.6a

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.4a-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Jul  2 2010 Michel Salim <salimma@fedoraproject.org> - 3.4a-1
- Update to 3.4a

* Fri Jul  2 2010 Michel Salim <salimma@fedoraproject.org> - 3.3a-2.5
- Now complies with Emacs packaging guidelines
- Disable broken XEmacs subpackages

* Sun May  9 2010 Michel Salim <salimma@fedoraproject.org> - 3.3a-1.5
- Update to 3.3a-5

* Fri Aug 21 2009 Tomas Mraz <tmraz@redhat.com> - 3.2b-3
- rebuilt with new openssl

* Sun Aug 16 2009 Gerard Milmeister <gemi@bluewin.ch> - 3.2b-2
- added requires gc-devel

* Sun Aug  9 2009 Gerard Milmeister <gemi@bluewin.ch> - 3.2b-1
- new release 3.2b

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.1b-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon Feb 23 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.1b-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Jan 15 2009 Tomas Mraz <tmraz@redhat.com> - 3.1b-4
- rebuild with new openssl

* Tue Sep 30 2008 Gerard Milmeister <gemi@bluewin.ch> - 3.1b-3
- add BR openssl-devel
- add missing Req. gmp-devel

* Thu Sep 18 2008 Gerard Milmeister <gemi@bluewin.ch> - 3.1b-1
- new release 3.1b

* Sat May 31 2008 Gerard Milmeister <gemi@bluewin.ch> - 3.1a-1
- new release 3.1a

* Mon Apr 14 2008 Gerard Milmeister <gemi@bluewin.ch> - 3.0c-4.1
- new release 3.0c-4

* Mon Feb 18 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 3.0b-2
- Autorebuild for GCC 4.3

* Tue Sep 11 2007 Gerard Milmeister <gemi@bluewin.ch> - 3.0b-1
- new release 3.0b

* Sat Jun  2 2007 Gerard Milmeister <gemi@bluewin.ch> - 3.0a-4
- exclude ppc64

* Fri Jun  1 2007 Gerard Milmeister <gemi@bluewin.ch> - 3.0a-3
- remove java ssl since it does not build with libgcj

* Fri Jun  1 2007 Gerard Milmeister <gemi@bluewin.ch> - 3.0a-1
- new version 3.0a

* Wed Mar 28 2007 Thomas Fitzsimmons <fitzsim@redhat.com> - 2.9a-3
- Patch method calls for Java 1.5.

* Tue Mar 27 2007 Thomas Fitzsimmons <fitzsim@redhat.com> - 2.9a-2
- Require java-1.5.0-gcj-devel for build.

* Thu Dec 28 2006 Gerard Milmeister <gemi@bluewin.ch> - 2.9a-1
- new version 2.9a

* Wed Sep 13 2006 Gerard Milmeister <gemi@bluewin.ch> - 2.8c-5
- final version 2.8c

* Tue Sep  5 2006 Gerard Milmeister <gemi@bluewin.ch> - 2.8c-4
- reenable hard links

* Fri Sep  1 2006 Gerard Milmeister <gemi@bluewin.ch> - 2.8c-2
- updated to 2.8c-beta01Sep06

* Mon Aug 28 2006 Gerard Milmeister <gemi@bluewin.ch> - 2.8b-3
- Rebuild for FE6

* Thu Jun 22 2006 Gerard Milmeister <gemi@bluewin.ch> - 2.8b-1
- new version 2.8b

* Thu Jun  1 2006 Gerard Milmeister <gemi@bluewin.ch> - 2.8a-2
- final 2.8a release

* Tue Mar 21 2006 Gerard Milmeister <gemi@bluewin.ch> - 2.8a-1.20060322
- new version 2.8a-20060322

* Mon Mar 13 2006 Gerard Milmeister <gemi@bluewin.ch> - 2.8a-1.20060313
- new version 2.8a-20060313

* Mon Nov 28 2005 Gerard Milmeister <gemi@bluewin.ch> - 2.7a-2
- disable bmem, causes link problems

* Sun Nov 27 2005 Gerard Milmeister <gemi@bluewin.ch> - 2.7a-1
- New Version 2.7a

* Tue Sep 27 2005 Gerard Milmeister <gemi@bluewin.ch> - 2.6f-3
- Removed --arch

* Fri Feb 18 2005 Gerard Milmeister <gemi@bluewin.ch> - 0:2.6f-1
- New Version 2.6f

* Sun Feb 13 2005 Gerard Milmeister <gemi@bluewin.ch> - 0:2.6e-1
- New Version 2.6e

* Tue Mar 16 2004 Gerard Milmeister <gemi@bluewin.ch> - 0:2.6-0.fdr.1.c
- New Version 2.6c
- Separated Emacs and XEmacs packages

* Tue Dec 16 2003 Gerard Milmeister <gemi@bluewin.ch> - 0:2.6-0.fdr.1.b
- New Version 2.6b

* Thu Nov 27 2003 Gerard Milmeister <gemi@bluewin.ch> - 0:2.6-0.fdr.1.a
- First Fedora release
