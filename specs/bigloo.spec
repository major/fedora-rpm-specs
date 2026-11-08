# I have given up on building the Java support. First, something is wrong with
# the makefiles. Install targets for Java often fail because the thing they are
# trying to install hasn't been built yet. Second, the bytecode doesn't pass
# verification. That could be ignored with older JDKs, but modern JDKs are not
# happy about that at all.
#
# If those two problems are fixed, we can bring Java support back.

# The hardened build breaks bigloo's plugin architecture.
%undefine _hardened_build

%global giturl  https://github.com/manuel-serrano/bigloo

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

# Bigloo needs itself to build, because the compiler is written in Scheme
%bcond bootstrap 0

# Whether to build Java support
%ifarch %{java_arches}
%bcond java %[%{without bootstrap} && 0]
%else
%bcond java 0
%endif

%if %{with java}
%global build_java yes
%else
%global build_java no
%endif

Name:           bigloo
Version:        4.7b%{?patch_ver:.%{patch_ver}}
Release:        %autorelease
Summary:        A compiler for the Scheme programming language

# The compiler and tools are GPL-2.0-or-later.
# The runtime system and libraries are LGPL-2.0-or-later.
# Exceptions:
# - api/csv is LGPL-3.0-or-later
# - api/mail/src/Llib/imap.stk is GPL-2.0-or-later
# - api/packrat/src/Llib/json.scm is MIT
# - api/packrat/src/Llib/packrat.scm is MIT
# - api/text/src/Llib/levenshtein.scm is LGPL-3.0-or-later
# - examples/Socket/socket.scm is some unknown form of BSD (not packaged)
# - manuals is Latex2e, except:
# - manuals/r5rs.texi is SchemeReport
# - runtime/Unsafe/sha2.scm is BSD-3-Clause
# - www/lib is MIT
# - the bundled GC library is Boehm-GC
License:        GPL-2.0-or-later
# Files not shipped in any binary with additional licenses:
# - bench/fft/fft.scm is LicenseRef-Fedora-Public-Domain
# - libunistring/config.guess is GPL-3.0-or-later WITH Autoconf-exception-generic-3.0
SourceLicense:  %{shrink:%{license}
                  AND LGPL-2.0-or-later
                  AND LGPL-3.0-or-later
                  AND BSD-3-Clause
                  AND MIT
                  AND Boehm-GC
                  AND GPL-3.0-or-later WITH Autoconf-exception-generic-3.0
                  AND Latex2e
                  AND SchemeReport
                }
URL:            https://www-sop.inria.fr/mimosa/fp/Bigloo
VCS:            git:%{giturl}.git
%if %{with bootstrap}
# The bootstrap compiler has pregenerated C files for the Scheme compiler
Source:         http://www-sop.inria.fr/indes/fp/Bigloo/download/bigloo-unstable.tar.gz
%else
Source:         %{giturl}/archive/v%{version}%{?patch_suffix}/%{name}-%{version}%{?patch_suffix}.tar.gz
%endif
# Not yet sent upstream: fix some bugs in the Emacs interface, and also
# modernizes the code somewhat.
Patch:          %{name}-emacs.patch
# Not yet sent upstream.  Support 64-bit stat on 32-bit platforms.
Patch:          %{name}-stat64.patch
# Not yet sent upstream: add some noreturn attributes
Patch:          %{name}-noreturn.patch
# Make type declarations match, silences LTO warning
Patch:          %{name}-lto-type.patch
# Round top of stack to a multiple of 1024.  Fixes stack overflow on s390x.
Patch:          %{name}-callcc.patch
# Adapt to Java 25
Patch:          %{name}-javac.patch
# Fix signal numbers in the Java code
Patch:          %{name}-java-signum.patch
# Avoid undefined behavior in the hashing code
Patch:          %{name}-hash-undefined.patch

# See https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}

%if %{without bootstrap}
BuildRequires:  bigloo
%endif
BuildRequires:  emacs-nox
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  gmp-devel
BuildRequires:  indent
%if %{with java}
BuildRequires:  java-25-devel
BuildRequires:  javapackages-tools
%endif
%if %{with customgc}
BuildRequires:  libatomic
%endif
BuildRequires:  libunistring-devel
BuildRequires:  make
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(alsa)
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
%if %{with java}
Requires:       javapackages-filesystem
%endif
Requires:       indent
Requires:       gmp-devel%{?_isa}
%if %{without customgc}
Requires:       gc-devel%{?_isa}
%endif
Requires:       gcc
Requires:       glibc-devel%{?_isa}
Requires:       libgcc%{?_isa}
Requires:       libunistring-devel%{?_isa}
Requires:       libuv-devel%{?_isa}

%if %{with customgc}
Provides:       bundled(gc) = %{bundledgc}
%endif

# Bigloo bundles libbacktrace, which is intended to be a copylib
Provides:       bundled(libbacktrace) = 1.0.20231209
%global __provides_exclude libbacktrace.*
%global __requires_exclude libbacktrace.*

# This can be removed when Fedora 49 reaches EOL
Obsoletes:      %{name}-doc < 4.6b-1
Provides:       %{name}-doc = %{version}-%{release}

%description
Bigloo is a Scheme implementation devoted to one goal: enabling a Scheme based
programming style where C(++) is usually required.  Bigloo attempts to make
Scheme practical by offering features usually presented by traditional
programming languages but not offered by Scheme and functional programming.
Bigloo compiles Scheme modules.  It delivers small and fast standalone binary
executables.  Bigloo enables full connections between Scheme and C programs.

%package libs
Summary:        Bigloo runtime libraries
# See above
License:        %{shrink:GPL-2.0-or-later
                  AND LGPL-2.0-or-later
                  AND LGPL-3.0-or-later
                  AND BSD-3-Clause
                  AND MIT
                  AND Boehm-GC
                 }

%description libs
Runtime libraries for Bigloo compiled programs.

%prep
%if %{with bootstrap}
%autosetup -p0 -n %{name}-unstable
%else
%autosetup -p0 -n %{name}-%{version}%{?patch_suffix}
%endif

%conf
# Remove prebuilt binaries
rm api/{mqtt,text}/recette/recette

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
%if %{with bootstrap}
bgver=$(sed -n 's/^release=\(.*\)/\1/p' configure)
%else
bgver=%{version}
%endif

# Large stack needed to build
ulimit -s unlimited

# Enable UTF-8 filename support
export LOCALE=C.utf8

# Work around a TLS definition issue
sed -i 's/TLS=thread_local/TLS=_Thread_local/;s/"thread_local"/"_Thread_local"/' autoconf/pthreadlocalstorage

# Build blib with the correct flags
sed -i "s|^CFLAGS.*|& $CFLAGS|" bdb/blib/Makefile

%if %{without bootstrap}
# Use the system bigloo to build
export BGLBUILDBINDIR=%{_bindir}
export BUILDBIGLOO=%{_bindir}/bigloo
# Look for whatever version the bootstrap compiler claims to be
bootver=$(bigloo -q -eval "(exit (print (bigloo-config 'release-number)))")
sed -i "s/^\(buildrelease=\).*/\1$bootver/" configure
%endif

# Help the bigloo binary find its libraries
sed -i "/EXTRA_LD_OPT/s|\$(LDCOMPLIBS)|& -Wl,-rpath=%{_libdir}/bigloo/$bgver|" comptime/Makefile

export LDFLAGS="-Wl,-z,relro -Wl,--as-needed"
./configure \
        --cflags='%{build_cflags} -D_GNU_SOURCE=1 -fno-strict-aliasing -Wno-unused' \
        --ldflags='-Wl,-z,relro -Wl,--as-needed' \
        --prefix=%{_prefix} \
        --bindir=%{_bindir} \
        --libdir=%{_libdir} \
        --mandir=%{_mandir} \
        --infodir=%{_infodir} \
        --docdir=%{_docdir} \
        --lispdir=%{_emacs_sitelispdir}/bigloo \
        --javaprefix=%{_jvmdir}/java/bin \
        --jvm=%{build_java} \
%ifarch %{power64} s390x
        --no-c-musttail \
%endif
        --bee=full \
        --customgc=%{?with_customgc:yes}%{!?with_customgc:no} \
        --customlibbacktrace=yes \
        --coflags="$CFLAGS" \
        --cpicflags="-fPIC" \
        --sharedbde=yes \
        --sharedcompiler=yes \
        --native-default-backend \
        --customgmp=no \
        --customlibuv=no \
        --strip=no \
        --configureinfo=yes

# Work around missing Makefile dependency
%make_build -C libbacktrace

# _smp_mflags breaks the build
LD_LIBRARY_PATH=$PWD/lib/bigloo/$bgver make
LD_LIBRARY_PATH=$PWD/lib/bigloo/$bgver \
    BIGLOOLIB=$PWD/inplace%{_libdir}/bigloo/$bgver \
    make DESTDIR=$PWD/inplace install
LD_LIBRARY_PATH=$PWD/lib/bigloo/$bgver \
    PATH=$PWD/bin:$PATH \
    BIGLOOLIB=$PWD/inplace%{_libdir}/bigloo/$bgver \
    make compile-bee
make -C manuals info info-bee

# Other permissions are missing from a lot of files
chmod -R o+r .

%install
%if %{with bootstrap}
bgver=$(sed -n 's/^release=\(.*\)/\1/p' configure)
%else
bgver=%{version}
%endif

mkdir -p %{buildroot}%{_emacs_sitelispdir}/bigloo
LD_LIBRARY_PATH=$PWD/lib/bigloo/$bgver %make_install
LD_LIBRARY_PATH=$PWD/lib/bigloo/$bgver make DESTDIR=%{buildroot} install-bee
touch %{buildroot}%{_infodir}/dir
make -C manuals DESTDIR=%{buildroot} install-bee

# fix permissions
find %{buildroot}%{_libdir} -name \*.so -exec chmod 755 {} +

%if %{with java}
# move jigloo to the proper place
mkdir %{buildroot}%{_javadir}
mv %{buildroot}%{_bindir}/jigloo.class %{buildroot}%{_javadir}
%endif

# Remove references to the build root
sed -e 's|^BOOTDIR=.*|BOOTDIR=%{_prefix}|g' \
    -e 's|^BOOTBINDIR=.*|BOOTBINDIR=%{_bindir}|g' \
    -e 's|^BOOTLIBDIR=.*|BOOTLIBDIR=%{_libdir}/bigloo/'"$bgver"'|g' \
    -e 's|^BGLBUILDBINDIR=.*|BGLBUILDBINDIR=%{_bindir}|g' \
    -e 's|^BGLBUILDLIBDIR=.*|BGLBUILDLIBDIR=%{_libdir}/bigloo/'"$bgver"'|g' \
    -e 's|^\(BIGLOO=.*\)\.sh|\1|' \
    -e 's|^\(BGL.*=.*\)\.sh|\1|' \
    -i %{buildroot}%{_libdir}/bigloo/$bgver/Makefile.config

# Remove references to the build root and the build directory
sed -i 's|\(LIBRARY_PATH=\).*|\1%{_libdir}/bigloo/'"$bgver"':$LD_LIBRARY_PATH|' \
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
cd %{buildroot}%{_emacs_sitelispdir}/bigloo
rm -f bmacs-xemacs.el xemacs-etags.el
%{_emacs_bytecompile} bmacs.el bmacs-config.el bmacs-gnu-emacs.el
cd -

# FIXME: bigloo-4.7b doesn't install these
# The current unstable version does, though, so check on next release
cp -p manuals/bigloo.info* %{buildroot}%{_infodir}
cp -p manuals/bigloo.man %{buildroot}%{_mandir}/man1/bigloo.1

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
cd recette
if [ "$NATIVEBACKEND" = yes ]; then
  make recette-static
  ../bin/bglrun.sh ./recette-static
fi
cd -
%if %{with java}
JVMBACKEND=$(sed -n 's/JVMBACKEND=\(.*\)/\1/p' Makefile.config)
if [ "$JVMBACKEND" = yes ]; then
  make jvm-test
fi
%endif
%endif

%files
%{_bindir}/bdb
%{_bindir}/bgl*
%{_bindir}/bigloo*
%{_bindir}/cigloo
%if %{with java}
%{_javadir}/jigloo.class
%endif
%{_infodir}/bdb.info*
%{_infodir}/bigloo.info*
%{_mandir}/man1/bgl*
%{_mandir}/man1/bigloo.1*
%{_emacs_sitelispdir}/bigloo/
%{_emacs_sitestartdir}/bigloo.el
# Omitted from the 4.7b release
#%%doc ChangeLog
%doc Makefile.config examples
%doc README*

%files libs
%{_libdir}/bigloo/
%license LICENSE COPYING

%changelog
%autochangelog
