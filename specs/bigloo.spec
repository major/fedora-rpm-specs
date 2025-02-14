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
Version:        4.6a%{?patch_ver:.%{patch_ver}}
Release:        %autorelease
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
export CFLAGS="%{build_cflags} -std=gnu17 -D_GNU_SOURCE=1 -fwrapv -fno-strict-aliasing -Wno-unused"
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
%autochangelog
