%global DATE 20240611
%global gitrev 03b1a31f9807251f378fcecb29c4669eed357eb2
%global gcc_version 13.3.1
%global gcc_major 13
# Note, gcc_release must be integer, if you want to add suffixes to
# %%{release}, append them after %%{gcc_release} on Release: line.
%global gcc_release 2
%global _performance_build 1
# Hardening slows the compiler way too much.
%undefine _hardened_build
%undefine _auto_set_build_flags
# Until annobin is fixed (#1519165).
%undefine _annotated_build
%ifarch %{ix86} x86_64 ppc64le
%global build_libquadmath 1
%else
%global build_libquadmath 0
%endif
%ifarch %{ix86} x86_64 ppc64le s390x aarch64 riscv64
%global build_libatomic 1
%else
%global build_libatomic 0
%endif
%ifarch %{ix86} x86_64 ppc64le s390x aarch64
%global build_libitm 1
%else
%global build_libitm 0
%endif
%ifarch %{ix86} x86_64 ppc64le s390x aarch64
%global attr_ifunc 1
%else
%global attr_ifunc 0
%endif
%global build_annobin_plugin 1
Summary: Various compatibility compilers (C, C++, Fortran, ...)
Name: gcc%{gcc_major}
Version: %{gcc_version}
Release: %{gcc_release}%{?dist}.2
# License notes for some of the less obvious ones:
#   gcc/doc/cppinternals.texi: Linux-man-pages-copyleft-2-para
#   isl: MIT, BSD-2-Clause
#   libcody: Apache-2.0
#   libphobos/src/etc/c/curl.d: curl
License: GPL-3.0-or-later AND LGPL-3.0-or-later AND (GPL-3.0-or-later WITH GCC-exception-3.1) AND (GPL-3.0-or-later WITH Texinfo-exception) AND (LGPL-2.1-or-later WITH GCC-exception-2.0) AND (GPL-2.0-or-later WITH GCC-exception-2.0) AND (GPL-2.0-or-later WITH GNU-compiler-exception) AND BSL-1.0 AND GFDL-1.3-or-later AND Linux-man-pages-copyleft-2-para AND SunPro AND BSD-1-Clause AND BSD-2-Clause AND BSD-2-Clause-Views AND BSD-3-Clause AND BSD-4-Clause AND BSD-Source-Code AND Zlib AND MIT AND Apache-2.0 AND (Apache-2.0 WITH LLVM-Exception) AND ZPL-2.1 AND curl
# The source for this package was pulled from upstream's vcs.
# %%{gitrev} is some commit from the
# https://gcc.gnu.org/git/?p=gcc.git;h=refs/vendors/redhat/heads/gcc-%%{gcc_major}-branch
# branch.  Use the following commands to generate the tarball:
# git clone --depth 1 git://gcc.gnu.org/git/gcc.git gcc-dir.tmp
# git --git-dir=gcc-dir.tmp/.git fetch --depth 1 origin %%{gitrev}
# git --git-dir=gcc-dir.tmp/.git archive --prefix=%%{name}-%%{version}-%%{DATE}/ %%{gitrev} | xz -9e > %%{name}-%%{version}-%%{DATE}.tar.xz
# rm -rf gcc-dir.tmp
Source0: gcc-%{version}-%{DATE}.tar.xz
Source1: dummylib.sh
URL: http://gcc.gnu.org
BuildRequires: binutils >= 2.31
# While gcc doesn't include statically linked binaries, during testing
# -static is used several times.
BuildRequires: glibc-static
BuildRequires: zlib-devel, gettext, dejagnu, bison, flex, sharutils
BuildRequires: texinfo, texinfo-tex, /usr/bin/pod2man
BuildRequires: systemtap-sdt-devel >= 1.3
BuildRequires: gmp-devel >= 4.1.2-8, mpfr-devel >= 3.1.0, libmpc-devel >= 0.8.1
BuildRequires: python3-devel, /usr/bin/python
BuildRequires: gcc, gcc-c++, make
# For VTA guality testing
BuildRequires: gdb
# Make sure pthread.h doesn't contain __thread tokens
# Make sure glibc supports stack protector
# Make sure glibc supports DT_GNU_HASH
BuildRequires: glibc-devel >= 2.4.90-13
BuildRequires: elfutils-devel >= 0.147
BuildRequires: elfutils-libelf-devel >= 0.147
BuildRequires: libzstd-devel
%ifarch ppc64le s390x
# Make sure glibc supports TFmode long double
BuildRequires: glibc >= 2.3.90-35
%endif
%if %{build_annobin_plugin}
BuildRequires: annobin-plugin-gcc >= 10.62, rpm-devel, binutils-devel, xz
%endif
BuildRequires: libstdc++, libgomp, libgcc, libgfortran
%if %{build_libitm}
BuildRequires: libitm
%endif
%if %{build_libatomic}
BuildRequires: libatomic
%endif
%if %{build_libquadmath}
BuildRequires: libquadmath
%endif
Requires: binutils >= 2.31
# Make sure gdb will understand DW_FORM_strp
Conflicts: gdb < 5.1-2
Requires: glibc-devel >= 2.2.90-12
%ifarch ppc64le s390x
# Make sure glibc supports TFmode long double
Requires: glibc >= 2.3.90-35
%endif
Requires: libgcc >= %{version}-%{release}
Requires: libgomp >= %{version}-%{release}
# lto-wrapper invokes make
Requires: make
AutoReq: true
AutoProv: false
Provides: bundled(libiberty)
Provides: bundled(libbacktrace)
Provides: bundled(libffi)

Patch0: gcc13-hack.patch
Patch3: gcc13-libgomp-omp_h-multilib.patch
Patch4: gcc13-libtool-no-rpath.patch
Patch8: gcc13-no-add-needed.patch
Patch9: gcc13-Wno-format-security.patch
Patch10: gcc13-rh1574936.patch

%global _gnu %{nil}
%global gcc_target_platform %{_target_platform}

%description
The gcc package contains the GNU Compiler Collection version %{gcc_major}
for compatibility purposes.

%package -n gcc%{gcc_major}-c++
Summary: C++ support for GCC %{gcc_major} compatibility compiler
Requires: gcc%{gcc_major} = %{version}-%{release}
Requires: libstdc++ >= %{version}-%{release}
Requires: libstdc++-devel >= %{version}-%{release}
AutoReq: true
AutoProv: false

%description -n gcc%{gcc_major}-c++
This package adds C++ support to the GNU Compiler Collection
%{gcc_major} compatibility compiler.

%package -n gcc%{gcc_major}-gfortran
Summary: Fortran support for GCC %{gcc_major} compatibility compiler
Requires: gcc%{gcc_major} = %{version}-%{release}
Requires: libgfortran >= %{version}-%{release}
%if %{build_libquadmath}
Requires: libquadmath >= %{version}-%{release}
Requires: libquadmath-devel >= %{version}-%{release}
%endif
AutoReq: true
AutoProv: false

%description -n gcc%{gcc_major}-gfortran
This package provides support for compiling Fortran
programs with the GNU Compiler Collection %{gcc_major}
compatibility compiler.

%prep
%setup -q -n gcc-%{version}-%{DATE}
%patch -P0 -p0 -b .hack~
%patch -P3 -p0 -b .libgomp-omp_h-multilib~
%patch -P4 -p0 -b .libtool-no-rpath~
%patch -P8 -p0 -b .no-add-needed~
%patch -P9 -p0 -b .Wno-format-security~
%patch -P10 -p0 -b .rh1574936~

echo 'Red Hat %{version}-%{gcc_release}' > gcc/DEV-PHASE

cp -a libstdc++-v3/config/cpu/i{4,3}86/atomicity.h

./contrib/gcc_update --touch

LC_ALL=C sed -i -e 's/\xa0/ /' gcc/doc/options.texi

sed -i -e 's/Common Driver Var(flag_report_bug)/& Init(1)/' gcc/common.opt
sed -i -e 's/context->report_bug = false;/context->report_bug = true;/' gcc/diagnostic.cc

%build

# Undo the broken autoconf change in recent Fedora versions
export CONFIG_SITE=NONE

CC=gcc
CXX=g++
OPT_FLAGS="%{optflags}"
OPT_FLAGS=`echo $OPT_FLAGS|sed -e 's/-Wp,-U_FORTIFY_SOURCE,-D_FORTIFY_SOURCE=[123]//g'`
OPT_FLAGS=`echo $OPT_FLAGS|sed -e 's/\(-Wp,\)\?-D_FORTIFY_SOURCE=[123]//g'`
OPT_FLAGS=`echo $OPT_FLAGS|sed -e 's/\(-Wp,\)\?-U_FORTIFY_SOURCE//g'`
OPT_FLAGS=`echo $OPT_FLAGS|sed -e 's/-flto=auto//g;s/-flto//g;s/-ffat-lto-objects//g'`
OPT_FLAGS=`echo $OPT_FLAGS|sed -e 's/-m64//g;s/-m32//g;s/-m31//g'`
OPT_FLAGS=`echo $OPT_FLAGS|sed -e 's/-mfpmath=sse/-mfpmath=sse -msse2/g'`
OPT_FLAGS=`echo $OPT_FLAGS|sed -e 's/ -pipe / /g'`
OPT_FLAGS=`echo $OPT_FLAGS|sed -e 's/-fno-omit-frame-pointer//g;s/-mbackchain//g;s/-mno-omit-leaf-frame-pointer//g'`
OPT_FLAGS=`echo $OPT_FLAGS|sed -e 's/-Werror=format-security/-Wformat-security/g'`
%ifarch %{ix86}
OPT_FLAGS=`echo $OPT_FLAGS|sed -e 's/-march=i.86//g'`
%endif
OPT_FLAGS=`echo "$OPT_FLAGS" | sed -e 's/[[:blank:]]\+/ /g'`
case "$OPT_FLAGS" in
  *-fasynchronous-unwind-tables*)
    sed -i -e 's/-fno-exceptions /-fno-exceptions -fno-asynchronous-unwind-tables /' \
      libgcc/Makefile.in
    ;;
esac

rm -rf obj-%{gcc_target_platform}
mkdir obj-%{gcc_target_platform}
cd obj-%{gcc_target_platform}

CONFIGURE_OPTS="\
	--prefix=%{_prefix} --mandir=%{_mandir} --infodir=%{_infodir} \
	--with-bugurl=http://bugzilla.redhat.com/bugzilla \
	--enable-shared --enable-threads=posix --enable-checking=release \
	--disable-multilib \
	--with-system-zlib --enable-__cxa_atexit --disable-libunwind-exceptions \
	--enable-gnu-unique-object --enable-linker-build-id --with-gcc-major-version-only \
	--enable-libstdcxx-backtrace --with-libstdcxx-zoneinfo=%{_datadir}/zoneinfo \
	--with-linker-hash-style=gnu \
	--enable-plugin --enable-initfini-array \
	--without-isl \
%if %{attr_ifunc}
	--enable-gnu-indirect-function \
%endif
%ifarch ppc64le
	--enable-secureplt \
%endif
%ifarch ppc64le s390x
	--with-long-double-128 \
%endif
%ifarch ppc64le
	--with-long-double-format=ieee \
%endif
%ifarch ppc64le
%if 0%{?rhel} >= 10
	--with-cpu-32=power9 --with-tune-32=power9 --with-cpu-64=power9 --with-tune-64=power9 \
%else
	--with-cpu-32=power8 --with-tune-32=power8 --with-cpu-64=power8 --with-tune-64=power8 \
%endif
%endif
%ifarch %{ix86} x86_64
	--enable-cet \
	--with-tune=generic \
%endif
%ifarch %{ix86}
	--with-arch=i686 \
%endif
%ifarch x86_64
	--with-arch_32=i686 \
%endif
%ifarch s390x
	--with-arch=z13 --with-tune=z14 \
	--enable-decimal-float \
%endif
%ifarch riscv64
	--with-arch=rv64gc --with-abi=lp64d --with-multilib-list=lp64d \
%endif
	--build=%{gcc_target_platform} \
	--with-build-config=bootstrap-lto --enable-link-serialization=1 \
	"

CC="$CC" CXX="$CXX" CFLAGS="$OPT_FLAGS" \
	CXXFLAGS="`echo " $OPT_FLAGS " | sed 's/ -Wall / /g;s/ -fexceptions / /g' \
		  | sed 's/ -Wformat-security / -Wformat -Wformat-security /'`" \
	XCFLAGS="$OPT_FLAGS" TCFLAGS="$OPT_FLAGS" \
	../configure --enable-bootstrap \
	--enable-languages=c,c++,fortran,lto \
	$CONFIGURE_OPTS

make %{?_smp_mflags} BOOT_CFLAGS="$OPT_FLAGS" LDFLAGS_FOR_TARGET=-Wl,-z,relro,-z,now profiledbootstrap

CC="`%{gcc_target_platform}/libstdc++-v3/scripts/testsuite_flags --build-cc`"
CXX="`%{gcc_target_platform}/libstdc++-v3/scripts/testsuite_flags --build-cxx` `%{gcc_target_platform}/libstdc++-v3/scripts/testsuite_flags --build-includes`"

# Make generated man pages even if Pod::Man is not new enough
perl -pi -e 's/head3/head2/' ../contrib/texi2pod.pl
for i in ../gcc/doc/*.texi; do
  cp -a $i $i.orig; sed 's/ftable/table/' $i.orig > $i
done
make -C gcc generated-manpages
for i in ../gcc/doc/*.texi; do mv -f $i.orig $i; done

# Copy various doc files here and there
cd ..
mkdir -p rpm.doc/gfortran
mkdir -p rpm.doc/changelogs/gcc/cp

for i in {gcc,gcc/cp}/ChangeLog*; do
	cp -p $i rpm.doc/changelogs/$i
done

(cd gcc/fortran; for i in ChangeLog*; do
	cp -p $i ../../rpm.doc/gfortran/$i
done)

rm -f rpm.doc/changelogs/gcc/ChangeLog.[1-9]
find rpm.doc -name \*ChangeLog\* | xargs bzip2 -9

%if %{build_annobin_plugin}
mkdir annobin-plugin
cd annobin-plugin
tar xf %{_usrsrc}/annobin/latest-annobin.tar.xz
cd annobin*
touch aclocal.m4 configure Makefile.in */configure */config.h.in */Makefile.in
ANNOBIN_FLAGS=../../obj-%{gcc_target_platform}/%{gcc_target_platform}/libstdc++-v3/scripts/testsuite_flags
ANNOBIN_CFLAGS1="%build_cflags -I %{_builddir}/gcc-%{version}-%{DATE}/gcc"
ANNOBIN_CFLAGS1="$ANNOBIN_CFLAGS1 -I %{_builddir}/gcc-%{version}-%{DATE}/obj-%{gcc_target_platform}/gcc"
ANNOBIN_CFLAGS2="-I %{_builddir}/gcc-%{version}-%{DATE}/include -I %{_builddir}/gcc-%{version}-%{DATE}/libcpp/include"
ANNOBIN_LDFLAGS="%build_ldflags -L%{_builddir}/gcc-%{version}-%{DATE}/obj-%{gcc_target_platform}/%{gcc_target_platform}/libstdc++-v3/src/.libs"
CC="`$ANNOBIN_FLAGS --build-cc`" CXX="`$ANNOBIN_FLAGS --build-cxx`" \
  CFLAGS="$ANNOBIN_CFLAGS1 $ANNOBIN_CFLAGS2 $ANNOBIN_LDFLAGS" \
  CXXFLAGS="$ANNOBIN_CFLAGS1 `$ANNOBIN_FLAGS --build-includes` $ANNOBIN_CFLAGS2 $ANNOBIN_LDFLAGS" \
  ./configure --with-gcc-plugin-dir=%{_prefix}/lib/gcc/%{gcc_target_platform}/%{gcc_major}/plugin \
	      --without-annocheck --without-tests --without-docs --disable-rpath --without-debuginfod \
	      --without-clang-plugin --without-llvm-plugin
make
cd ../..
%endif

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}

# RISC-V ABI wants to install everything in /lib64/lp64d or /usr/lib64/lp64d.
# Make these be symlinks to /lib64 or /usr/lib64 respectively. See:
# https://lists.fedoraproject.org/archives/list/devel@lists.fedoraproject.org/thread/DRHT5YTPK4WWVGL3GIN5BF2IKX2ODHZ3/
%ifarch riscv64
for d in %{buildroot}%{_libdir} %{buildroot}/%{_lib} \
	  %{buildroot}%{_datadir}/gdb/auto-load/%{_prefix}/%{_lib} \
	  %{buildroot}%{_prefix}/include/c++/%{gcc_major}/%{gcc_target_platform}/%{_lib}; do
  mkdir -p $d
  (cd $d && ln -sf . lp64d)
done
%endif

cd obj-%{gcc_target_platform}

TARGET_PLATFORM=%{gcc_target_platform}

# There are some MP bugs in libstdc++ Makefiles
make -C %{gcc_target_platform}/libstdc++-v3

make prefix=%{buildroot}%{_prefix} mandir=%{buildroot}%{_mandir} \
  infodir=%{buildroot}%{_infodir} install

FULLPATH=%{buildroot}%{_prefix}/lib/gcc/%{gcc_target_platform}/%{gcc_major}
FULLEPATH=%{buildroot}%{_prefix}/libexec/gcc/%{gcc_target_platform}/%{gcc_major}

# fix some things
rm -f %{buildroot}%{_infodir}/dir
gzip -9 %{buildroot}%{_infodir}/*.info*

for f in `find %{buildroot}%{_prefix}/include/c++/%{gcc_major}/%{gcc_target_platform}/ -name c++config.h`; do
  for i in 1 2 4 8; do
    sed -i -e 's/#define _GLIBCXX_ATOMIC_BUILTINS_'$i' 1/#ifdef __GCC_HAVE_SYNC_COMPARE_AND_SWAP_'$i'\
&\
#endif/' $f
  done
done

# Nuke bits/*.h.gch dirs
# 1) there is no bits/*.h header installed, so when gch file can't be
#    used, compilation fails
# 2) sometimes it is hard to match the exact options used for building
#    libstdc++-v3 or they aren't desirable
# 3) there are multilib issues, conflicts etc. with this
# 4) it is huge
# People can always precompile on their own whatever they want, but
# shipping this for everybody is unnecessary.
rm -rf %{buildroot}%{_prefix}/include/c++/%{gcc_major}/%{gcc_target_platform}/bits/*.h.gch

FULLLSUBDIR=
FULLLPATH=$FULLPATH

find %{buildroot} -name \*.la | xargs rm -f

mv %{buildroot}%{_prefix}/%{_lib}/libgfortran.spec $FULLPATH/
%if %{build_libitm}
mv %{buildroot}%{_prefix}/%{_lib}/libitm.spec $FULLPATH/
%endif

# For ld(1) purposes create dummy libraries which just export the right symbols
# that gcc %%{gcc_major} libraries normally export and have additionally
# compatibility only symbols from the newer system gcc shared libraries with
# the same SONAME.  The intent is to make sure when linking with the compatibility
# compiler there is diagnostics if one attempts to link also symbols not supported
# by the older gcc.  If one mixes some gcc %%{gcc_major} and some system gcc compiled
# objects, one should use the system gcc to link those together.
sh %{SOURCE1} %{gcc_target_platform}/libgcc/libgcc_s.so.1 $FULLPATH/libgcc_s_dummy.so \
  %{gcc_target_platform}/libgcc/libgcc.map /%{_lib}/libgcc_s.so.1
rm -f %{buildroot}%{_prefix}/%{_lib}/libgcc_s.so.1
%ifarch %{ix86} x86_64 ppc64le aarch64 riscv64
rm -f $FULLPATH/libgcc_s.so
echo '/* GNU ld script
   Use the shared library, but some functions are only in
   the static library, so try that secondarily.  */
OUTPUT_FORMAT('`gcc -Wl,--print-output-format -nostdlib -r -o /dev/null`')
GROUP ( libgcc_s_dummy.so libgcc.a )' > $FULLPATH/libgcc_s.so
%else
ln -sf libgcc_s_dummy.so $FULLPATH/libgcc_s.so
%endif
rm -f %{gcc_target_platform}/libgcc/libgcc_s.so
cp -a $FULLPATH/libgcc_s.so %{gcc_target_platform}/libgcc/libgcc_s.so
cp -a $FULLPATH/libgcc_s_dummy.so %{gcc_target_platform}/libgcc/libgcc_s_dummy.so
ln -sf /%{_lib}/libgcc_s.so.1 %{gcc_target_platform}/libgcc/libgcc.so.1
rm -f gcc/libgcc_s.so
cp -a $FULLPATH/libgcc_s.so gcc/libgcc_s.so
cp -a $FULLPATH/libgcc_s_dummy.so gcc/libgcc_s_dummy.so
ln -sf /%{_lib}/libgcc_s.so.1 gcc/libgcc.so.1

mv -f %{buildroot}%{_prefix}/%{_lib}/libgomp.spec $FULLPATH/

sh %{SOURCE1} %{gcc_target_platform}/libstdc++-v3/src/.libs/libstdc++.so.6.* $FULLPATH/libstdc++.so \
  %{gcc_target_platform}/libstdc++-v3/src/libstdc++-symbols.ver %{_prefix}/%{_lib}/libstdc++.so.6
rm -f %{gcc_target_platform}/libstdc++-v3/src/.libs/libstdc++.so
cp -a $FULLPATH/libstdc++.so %{gcc_target_platform}/libstdc++-v3/src/.libs/libstdc++.so
ln -sf %{_prefix}/%{_lib}/libstdc++.so.6 %{gcc_target_platform}/libstdc++-v3/src/.libs/libstdc++.so.6.*
sh %{SOURCE1} %{gcc_target_platform}/libgfortran/.libs/libgfortran.so.5.* $FULLPATH/libgfortran.so \
  %{gcc_target_platform}/libgfortran/gfortran.ver %{_prefix}/%{_lib}/libgfortran.so.5
rm -f %{gcc_target_platform}/libgfortran/.libs/libgfortran.so
cp -a $FULLPATH/libgfortran.so %{gcc_target_platform}/libgfortran/.libs/libgfortran.so
ln -sf %{_prefix}/%{_lib}/libgfortran.so.5 %{gcc_target_platform}/libgfortran/.libs/libgfortran.so.5.*
sh %{SOURCE1} %{gcc_target_platform}/libgomp/.libs/libgomp.so.1.* $FULLPATH/libgomp.so \
  %{gcc_target_platform}/libgomp/libgomp.ver %{_prefix}/%{_lib}/libgomp.so.1
rm -f %{gcc_target_platform}/libgomp/.libs/libgomp.so
cp -a $FULLPATH/libgomp.so %{gcc_target_platform}/libgomp/.libs/libgomp.so
ln -sf %{_prefix}/%{_lib}/libgomp.so.1 %{gcc_target_platform}/libgomp/.libs/libgomp.so.1.*
%if %{build_libquadmath}
sh %{SOURCE1} %{gcc_target_platform}/libquadmath/.libs/libquadmath.so.0.* $FULLPATH/libquadmath.so \
  ../libquadmath/quadmath.map %{_prefix}/%{_lib}/libquadmath.so.0
rm -f %{gcc_target_platform}/libquadmath/.libs/libquadmath.so
cp -a $FULLPATH/libquadmath.so %{gcc_target_platform}/libquadmath/.libs/libquadmath.so
ln -sf %{_prefix}/%{_lib}/libquadmath.so.0 %{gcc_target_platform}/libquadmath/.libs/libquadmath.so.0.*
%endif
%if %{build_libitm}
sh %{SOURCE1} %{gcc_target_platform}/libitm/.libs/libitm.so.1.* $FULLPATH/libitm.so \
  ../libitm/libitm.map %{_prefix}/%{_lib}/libitm.so.1
rm -f %{gcc_target_platform}/libitm/.libs/libitm.so
cp -a $FULLPATH/libitm.so %{gcc_target_platform}/libitm/.libs/libitm.so
ln -sf %{_prefix}/%{_lib}/libitm.so.1 %{gcc_target_platform}/libitm/.libs/libitm.so.1.*
%endif
%if %{build_libatomic}
sh %{SOURCE1} %{gcc_target_platform}/libatomic/.libs/libatomic.so.1.* $FULLPATH/libatomic.so \
  ../libatomic/libatomic.map %{_prefix}/%{_lib}/libatomic.so.1
rm -f %{gcc_target_platform}/libatomic/.libs/libatomic.so
cp -a $FULLPATH/libatomic.so %{gcc_target_platform}/libatomic/.libs/libatomic.so
ln -sf %{_prefix}/%{_lib}/libatomic.so.1 %{gcc_target_platform}/libatomic/.libs/libatomic.so.1.*
%endif

pushd $FULLPATH
mv -f %{buildroot}%{_prefix}/%{_lib}/libstdc++.*a $FULLLPATH/
mv -f %{buildroot}%{_prefix}/%{_lib}/libstdc++fs.*a $FULLLPATH/
mv -f %{buildroot}%{_prefix}/%{_lib}/libstdc++exp.*a $FULLLPATH/
mv -f %{buildroot}%{_prefix}/%{_lib}/libstdc++_libbacktrace.*a $FULLLPATH/
mv -f %{buildroot}%{_prefix}/%{_lib}/libsupc++.*a $FULLLPATH/
mv -f %{buildroot}%{_prefix}/%{_lib}/libgfortran.*a $FULLLPATH/
mv -f %{buildroot}%{_prefix}/%{_lib}/libgomp.*a $FULLLPATH/
%if %{build_libquadmath}
mv -f %{buildroot}%{_prefix}/%{_lib}/libquadmath.*a $FULLLPATH/
%endif
%if %{build_libitm}
mv -f %{buildroot}%{_prefix}/%{_lib}/libitm.*a $FULLLPATH/
%endif
%if %{build_libatomic}
mv -f %{buildroot}%{_prefix}/%{_lib}/libatomic.*a $FULLLPATH/
%endif

rm -f %{buildroot}%{_prefix}/%{_lib}/lib*.so.*
rm -f %{buildroot}%{_prefix}/%{_lib}/lib*.a

# Strip debug info from Fortran/ObjC/Java static libraries
strip -g `find . \( -name libgfortran.a -o -name libobjc.a -o -name libgomp.a \
		    -o -name libgcc.a -o -name libgcov.a -o -name libquadmath.a \
		    -o -name libgdruntime.a -o -name libgphobos.a -o -name libm2\*.a \
		    -o -name libitm.a -o -name libgo.a -o -name libcaf\*.a \
		    -o -name libatomic.a -o -name libasan.a -o -name libtsan.a \
		    -o -name libubsan.a -o -name liblsan.a -o -name libcc1.a \) \
		 -a -type f`
popd

for h in `find $FULLPATH/include -name \*.h`; do
  if grep -q 'It has been auto-edited by fixincludes from' $h; then
    rh=`grep -A2 'It has been auto-edited by fixincludes from' $h | tail -1 | sed 's|^.*"\(.*\)".*$|\1|'`
    diff -up $rh $h || :
    rm -f $h
  fi
done

cd ..

# Remove binaries we will not be including, so that they don't end up in
# gcc-debuginfo
rm -f %{buildroot}%{_prefix}/%{_lib}/{libffi*,libiberty.a} || :
rm -f $FULLEPATH/install-tools/{mkheaders,fixincl}
rm -f %{buildroot}%{_prefix}/lib/{32,64}/libiberty.a
rm -f %{buildroot}%{_prefix}/%{_lib}/libssp*
rm -f %{buildroot}%{_prefix}/%{_lib}/libvtv* || :
rm -f %{buildroot}%{_prefix}/bin/%{_target_platform}-gfortran || :
rm -f %{buildroot}%{_prefix}/bin/%{_target_platform}-gcc-ar || :
rm -f %{buildroot}%{_prefix}/bin/%{_target_platform}-gcc-nm || :
rm -f %{buildroot}%{_prefix}/bin/%{_target_platform}-gcc-ranlib || :
rm -f %{buildroot}%{_prefix}/bin/c++ || :
rm -f $FULLEPATH/plugin/gengtype || :
rm -f $FULLPATH/plugin/lib{cc1,cp1}plugin.so* || :

rm -f %{buildroot}%{mandir}/man3/ffi*

# Help plugins find out nvra.
echo gcc-%{version}-%{release}.%{_arch} > $FULLPATH/rpmver

%if %{build_annobin_plugin}
mkdir -p $FULLPATH/plugin
rm -f $FULLPATH/plugin/gcc-annobin*
cp -a %{_builddir}/gcc-%{version}-%{DATE}/annobin-plugin/annobin*/gcc-plugin/.libs/annobin.so.0.0.0 \
  $FULLPATH/plugin/gcc-annobin.so.0.0.0
ln -sf gcc-annobin.so.0.0.0 $FULLPATH/plugin/gcc-annobin.so.0
ln -sf gcc-annobin.so.0.0.0 $FULLPATH/plugin/gcc-annobin.so
ln -sf gcc-annobin.so $FULLPATH/plugin/annobin.so
%endif

rm -f %{buildroot}%{_prefix}/bin/*-gcc-%{gcc_major}
for i in %{buildroot}%{_prefix}/bin/{*gcc,*++,gcov,gcov-tool,gcov-dump,gcc-ar,gcc-nm,gcc-ranlib,lto-dump,cpp,gfortran}; do
  mv -f $i ${i}-%{gcc_major}
done
for i in %{buildroot}%{_mandir}/man1/{gcc,gcov,gcov-tool,gcov-dump,lto-dump,cpp,g++,gfortran}.1*; do
  mv -f $i `echo $i | sed 's/\(\.1[^/]*\)$/-%{gcc_major}\1/'`
done

rm -rf $FULLPATH/include-fixed || :
rm -rf $FULLPATH/include/sanitizer || :
rm -rf $FULLPATH/include/ssp || :
rm -rf $FULLPATH/install-tools || :
rm -rf $FULLPATH/plugin/gtype.state || :
rm -rf $FULLPATH/plugin/include || :
rm -rf $FULLEPATH/install-tools || :
rm -rf %{buildroot}%{_prefix}/share/gcc-%{gcc_major}/python || :
rm -rf %{buildroot}%{_infodir} || :
rm -rf %{buildroot}%{_prefix}/share/locale || :
rm -rf %{buildroot}%{_mandir}/man7 || :
rm -rf %{buildroot}%{_prefix}/%{_lib}/*.so || :
rm -rf %{buildroot}%{_prefix}/%{_lib}/*.spec || :
rm -rf %{buildroot}%{_prefix}/%{_lib}/*.o || :
%ifarch ppc64le
rm -rf $FULLPATH/{e,n}crt{i,n}.o || :
%endif

%check
cd obj-%{gcc_target_platform}

# run the tests.
LC_ALL=C make %{?_smp_mflags} -k check ALT_CC_UNDER_TEST=gcc ALT_CXX_UNDER_TEST=g++ \
     RUNTESTFLAGS="--target_board=unix/'{,-fstack-protector-strong}'" || :
%if !%{build_annobin_plugin}
if [ -f %{_prefix}/lib/gcc/%{gcc_target_platform}/%{gcc_major}/plugin/annobin.so ]; then
  # Test whether current annobin plugin won't fail miserably with the newly built gcc.
  echo -e '#include <stdio.h>\nint main () { printf ("Hello, world!\\n"); return 0; }' > annobin-test.c
  echo -e '#include <iostream>\nint main () { std::cout << "Hello, world!" << std::endl; return 0; }' > annobin-test.C
  `%{gcc_target_platform}/libstdc++-v3/scripts/testsuite_flags --build-cc` \
  -O2 -g -Wall -Werror=format-security -Wp,-D_FORTIFY_SOURCE=2 -Wp,-D_GLIBCXX_ASSERTIONS \
  -fexceptions -fstack-protector-strong -grecord-gcc-switches -o annobin-test{c,.c} \
  -Wl,-rpath,%{gcc_target_platform}/libgcc/ \
  -fplugin=%{_prefix}/lib/gcc/%{gcc_target_platform}/%{gcc_major}/plugin/annobin.so \
  2> ANNOBINOUT1 || echo Annobin test 1 FAIL > ANNOBINOUT2;
  `%{gcc_target_platform}/libstdc++-v3/scripts/testsuite_flags --build-cxx` \
  `%{gcc_target_platform}/libstdc++-v3/scripts/testsuite_flags --build-includes` \
  -O2 -g -Wall -Werror=format-security -Wp,-D_FORTIFY_SOURCE=2 -Wp,-D_GLIBCXX_ASSERTIONS \
  -fexceptions -fstack-protector-strong -grecord-gcc-switches -o annobin-test{C,.C} \
  -Wl,-rpath,%{gcc_target_platform}/libgcc/:%{gcc_target_platform}/libstdc++-v3/src/.libs/ \
  -fplugin=%{_prefix}/lib/gcc/%{gcc_target_platform}/%{gcc_major}/plugin/annobin.so \
  -B %{gcc_target_platform}/libstdc++-v3/src/.libs/ \
  2> ANNOBINOUT3 || echo Annobin test 2 FAIL > ANNOBINOUT4;
  [ -f ./annobin-testc ] || echo Annobin test 1 MISSING > ANNOBINOUT5;
  [ -f ./annobin-testc ] && \
  ( ./annobin-testc > ANNOBINRES1 2>&1 || echo Annobin test 1 RUNFAIL > ANNOBINOUT6 );
  [ -f ./annobin-testC ] || echo Annobin test 2 MISSING > ANNOBINOUT7;
  [ -f ./annobin-testC ] && \
  ( ./annobin-testC > ANNOBINRES2 2>&1 || echo Annobin test 2 RUNFAIL > ANNOBINOUT8 );
  cat ANNOBINOUT[1-8] > ANNOBINOUT
  touch ANNOBINRES1 ANNOBINRES2
  [ -s ANNOBINOUT ] && echo Annobin testing FAILed > ANNOBINRES
  cat ANNOBINOUT ANNOBINRES[12] >> ANNOBINRES
  rm -f ANNOBINOUT* ANNOBINRES[12] annobin-test{c,C}
fi
%endif
echo ====================TESTING=========================
( LC_ALL=C ../contrib/test_summary || : ) 2>&1 | sed -n '/^cat.*EOF/,/^EOF/{/^cat.*EOF/d;/^EOF/d;/^LAST_UPDATED:/d;p;}'
%if !%{build_annobin_plugin}
[ -f ANNOBINRES ] && cat ANNOBINRES
%endif
echo ====================TESTING END=====================
mkdir testlogs-%{_target_platform}-%{version}-%{release}
for i in `find . -name \*.log | grep -F testsuite/ | grep -v 'config.log\|acats.*/tests/'`; do
  ln $i testlogs-%{_target_platform}-%{version}-%{release}/ || :
done
tar cf - testlogs-%{_target_platform}-%{version}-%{release} | xz -9e \
  | uuencode testlogs-%{_target_platform}.tar.xz || :
rm -rf testlogs-%{_target_platform}-%{version}-%{release}

%files -n gcc%{gcc_major}
%{_prefix}/bin/cpp-%{gcc_major}
%{_prefix}/bin/gcc-%{gcc_major}
%{_prefix}/bin/gcov-%{gcc_major}
%{_prefix}/bin/gcov-tool-%{gcc_major}
%{_prefix}/bin/gcov-dump-%{gcc_major}
%{_prefix}/bin/gcc-ar-%{gcc_major}
%{_prefix}/bin/gcc-nm-%{gcc_major}
%{_prefix}/bin/gcc-ranlib-%{gcc_major}
%{_prefix}/bin/lto-dump-%{gcc_major}
%{_prefix}/bin/%{gcc_target_platform}-gcc-%{gcc_major}
%{_mandir}/man1/cpp-%{gcc_major}.1*
%{_mandir}/man1/gcc-%{gcc_major}.1*
%{_mandir}/man1/gcov-%{gcc_major}.1*
%{_mandir}/man1/gcov-tool-%{gcc_major}.1*
%{_mandir}/man1/gcov-dump-%{gcc_major}.1*
%{_mandir}/man1/lto-dump-%{gcc_major}.1*
%dir %{_prefix}/lib/gcc
%dir %{_prefix}/lib/gcc/%{gcc_target_platform}
%dir %{_prefix}/lib/gcc/%{gcc_target_platform}/%{gcc_major}
%dir %{_prefix}/libexec/gcc
%dir %{_prefix}/libexec/gcc/%{gcc_target_platform}
%dir %{_prefix}/libexec/gcc/%{gcc_target_platform}/%{gcc_major}
%dir %{_prefix}/lib/gcc/%{gcc_target_platform}/%{gcc_major}/include
%{_prefix}/libexec/gcc/%{gcc_target_platform}/%{gcc_major}/cc1
%{_prefix}/libexec/gcc/%{gcc_target_platform}/%{gcc_major}/lto1
%{_prefix}/libexec/gcc/%{gcc_target_platform}/%{gcc_major}/lto-wrapper
%{_prefix}/libexec/gcc/%{gcc_target_platform}/%{gcc_major}/liblto_plugin.so*
%{_prefix}/lib/gcc/%{gcc_target_platform}/%{gcc_major}/rpmver
%{_prefix}/lib/gcc/%{gcc_target_platform}/%{gcc_major}/include/stddef.h
%{_prefix}/lib/gcc/%{gcc_target_platform}/%{gcc_major}/include/stdarg.h
%{_prefix}/lib/gcc/%{gcc_target_platform}/%{gcc_major}/include/stdfix.h
%{_prefix}/lib/gcc/%{gcc_target_platform}/%{gcc_major}/include/varargs.h
%{_prefix}/lib/gcc/%{gcc_target_platform}/%{gcc_major}/include/float.h
%{_prefix}/lib/gcc/%{gcc_target_platform}/%{gcc_major}/include/limits.h
%{_prefix}/lib/gcc/%{gcc_target_platform}/%{gcc_major}/include/stdbool.h
%{_prefix}/lib/gcc/%{gcc_target_platform}/%{gcc_major}/include/iso646.h
%{_prefix}/lib/gcc/%{gcc_target_platform}/%{gcc_major}/include/syslimits.h
%{_prefix}/lib/gcc/%{gcc_target_platform}/%{gcc_major}/include/unwind.h
%{_prefix}/lib/gcc/%{gcc_target_platform}/%{gcc_major}/include/omp.h
%{_prefix}/lib/gcc/%{gcc_target_platform}/%{gcc_major}/include/openacc.h
%{_prefix}/lib/gcc/%{gcc_target_platform}/%{gcc_major}/include/acc_prof.h
%{_prefix}/lib/gcc/%{gcc_target_platform}/%{gcc_major}/include/stdint.h
%{_prefix}/lib/gcc/%{gcc_target_platform}/%{gcc_major}/include/stdint-gcc.h
%{_prefix}/lib/gcc/%{gcc_target_platform}/%{gcc_major}/include/stdalign.h
%{_prefix}/lib/gcc/%{gcc_target_platform}/%{gcc_major}/include/stdnoreturn.h
%{_prefix}/lib/gcc/%{gcc_target_platform}/%{gcc_major}/include/stdatomic.h
%{_prefix}/lib/gcc/%{gcc_target_platform}/%{gcc_major}/include/gcov.h
%if %{build_libquadmath}
%{_prefix}/lib/gcc/%{gcc_target_platform}/%{gcc_major}/include/quadmath.h
%{_prefix}/lib/gcc/%{gcc_target_platform}/%{gcc_major}/include/quadmath_weak.h
%endif
%ifarch %{ix86} x86_64
%{_prefix}/lib/gcc/%{gcc_target_platform}/%{gcc_major}/include/mmintrin.h
%{_prefix}/lib/gcc/%{gcc_target_platform}/%{gcc_major}/include/xmmintrin.h
%{_prefix}/lib/gcc/%{gcc_target_platform}/%{gcc_major}/include/emmintrin.h
%{_prefix}/lib/gcc/%{gcc_target_platform}/%{gcc_major}/include/pmmintrin.h
%{_prefix}/lib/gcc/%{gcc_target_platform}/%{gcc_major}/include/tmmintrin.h
%{_prefix}/lib/gcc/%{gcc_target_platform}/%{gcc_major}/include/ammintrin.h
%{_prefix}/lib/gcc/%{gcc_target_platform}/%{gcc_major}/include/smmintrin.h
%{_prefix}/lib/gcc/%{gcc_target_platform}/%{gcc_major}/include/nmmintrin.h
%{_prefix}/lib/gcc/%{gcc_target_platform}/%{gcc_major}/include/bmmintrin.h
%{_prefix}/lib/gcc/%{gcc_target_platform}/%{gcc_major}/include/wmmintrin.h
%{_prefix}/lib/gcc/%{gcc_target_platform}/%{gcc_major}/include/immintrin.h
%{_prefix}/lib/gcc/%{gcc_target_platform}/%{gcc_major}/include/avxintrin.h
%{_prefix}/lib/gcc/%{gcc_target_platform}/%{gcc_major}/include/x86intrin.h
%{_prefix}/lib/gcc/%{gcc_target_platform}/%{gcc_major}/include/fma4intrin.h
%{_prefix}/lib/gcc/%{gcc_target_platform}/%{gcc_major}/include/xopintrin.h
%{_prefix}/lib/gcc/%{gcc_target_platform}/%{gcc_major}/include/lwpintrin.h
%{_prefix}/lib/gcc/%{gcc_target_platform}/%{gcc_major}/include/popcntintrin.h
%{_prefix}/lib/gcc/%{gcc_target_platform}/%{gcc_major}/include/bmiintrin.h
%{_prefix}/lib/gcc/%{gcc_target_platform}/%{gcc_major}/include/tbmintrin.h
%{_prefix}/lib/gcc/%{gcc_target_platform}/%{gcc_major}/include/ia32intrin.h
%{_prefix}/lib/gcc/%{gcc_target_platform}/%{gcc_major}/include/avx2intrin.h
%{_prefix}/lib/gcc/%{gcc_target_platform}/%{gcc_major}/include/bmi2intrin.h
%{_prefix}/lib/gcc/%{gcc_target_platform}/%{gcc_major}/include/f16cintrin.h
%{_prefix}/lib/gcc/%{gcc_target_platform}/%{gcc_major}/include/fmaintrin.h
%{_prefix}/lib/gcc/%{gcc_target_platform}/%{gcc_major}/include/lzcntintrin.h
%{_prefix}/lib/gcc/%{gcc_target_platform}/%{gcc_major}/include/rtmintrin.h
%{_prefix}/lib/gcc/%{gcc_target_platform}/%{gcc_major}/include/xtestintrin.h
%{_prefix}/lib/gcc/%{gcc_target_platform}/%{gcc_major}/include/adxintrin.h
%{_prefix}/lib/gcc/%{gcc_target_platform}/%{gcc_major}/include/prfchwintrin.h
%{_prefix}/lib/gcc/%{gcc_target_platform}/%{gcc_major}/include/rdseedintrin.h
%{_prefix}/lib/gcc/%{gcc_target_platform}/%{gcc_major}/include/fxsrintrin.h
%{_prefix}/lib/gcc/%{gcc_target_platform}/%{gcc_major}/include/xsaveintrin.h
%{_prefix}/lib/gcc/%{gcc_target_platform}/%{gcc_major}/include/xsaveoptintrin.h
%{_prefix}/lib/gcc/%{gcc_target_platform}/%{gcc_major}/include/avx512cdintrin.h
%{_prefix}/lib/gcc/%{gcc_target_platform}/%{gcc_major}/include/avx512erintrin.h
%{_prefix}/lib/gcc/%{gcc_target_platform}/%{gcc_major}/include/avx512fintrin.h
%{_prefix}/lib/gcc/%{gcc_target_platform}/%{gcc_major}/include/avx512pfintrin.h
%{_prefix}/lib/gcc/%{gcc_target_platform}/%{gcc_major}/include/shaintrin.h
%{_prefix}/lib/gcc/%{gcc_target_platform}/%{gcc_major}/include/mm_malloc.h
%{_prefix}/lib/gcc/%{gcc_target_platform}/%{gcc_major}/include/mm3dnow.h
%{_prefix}/lib/gcc/%{gcc_target_platform}/%{gcc_major}/include/cpuid.h
%{_prefix}/lib/gcc/%{gcc_target_platform}/%{gcc_major}/include/cross-stdarg.h
%{_prefix}/lib/gcc/%{gcc_target_platform}/%{gcc_major}/include/avx512bwintrin.h
%{_prefix}/lib/gcc/%{gcc_target_platform}/%{gcc_major}/include/avx512dqintrin.h
%{_prefix}/lib/gcc/%{gcc_target_platform}/%{gcc_major}/include/avx512ifmaintrin.h
%{_prefix}/lib/gcc/%{gcc_target_platform}/%{gcc_major}/include/avx512ifmavlintrin.h
%{_prefix}/lib/gcc/%{gcc_target_platform}/%{gcc_major}/include/avx512vbmiintrin.h
%{_prefix}/lib/gcc/%{gcc_target_platform}/%{gcc_major}/include/avx512vbmivlintrin.h
%{_prefix}/lib/gcc/%{gcc_target_platform}/%{gcc_major}/include/avx512vlbwintrin.h
%{_prefix}/lib/gcc/%{gcc_target_platform}/%{gcc_major}/include/avx512vldqintrin.h
%{_prefix}/lib/gcc/%{gcc_target_platform}/%{gcc_major}/include/avx512vlintrin.h
%{_prefix}/lib/gcc/%{gcc_target_platform}/%{gcc_major}/include/clflushoptintrin.h
%{_prefix}/lib/gcc/%{gcc_target_platform}/%{gcc_major}/include/clwbintrin.h
%{_prefix}/lib/gcc/%{gcc_target_platform}/%{gcc_major}/include/mwaitxintrin.h
%{_prefix}/lib/gcc/%{gcc_target_platform}/%{gcc_major}/include/xsavecintrin.h
%{_prefix}/lib/gcc/%{gcc_target_platform}/%{gcc_major}/include/xsavesintrin.h
%{_prefix}/lib/gcc/%{gcc_target_platform}/%{gcc_major}/include/clzerointrin.h
%{_prefix}/lib/gcc/%{gcc_target_platform}/%{gcc_major}/include/pkuintrin.h
%{_prefix}/lib/gcc/%{gcc_target_platform}/%{gcc_major}/include/avx5124fmapsintrin.h
%{_prefix}/lib/gcc/%{gcc_target_platform}/%{gcc_major}/include/avx5124vnniwintrin.h
%{_prefix}/lib/gcc/%{gcc_target_platform}/%{gcc_major}/include/avx512vpopcntdqintrin.h
%{_prefix}/lib/gcc/%{gcc_target_platform}/%{gcc_major}/include/sgxintrin.h
%{_prefix}/lib/gcc/%{gcc_target_platform}/%{gcc_major}/include/gfniintrin.h
%{_prefix}/lib/gcc/%{gcc_target_platform}/%{gcc_major}/include/cetintrin.h
%{_prefix}/lib/gcc/%{gcc_target_platform}/%{gcc_major}/include/cet.h
%{_prefix}/lib/gcc/%{gcc_target_platform}/%{gcc_major}/include/avx512vbmi2intrin.h
%{_prefix}/lib/gcc/%{gcc_target_platform}/%{gcc_major}/include/avx512vbmi2vlintrin.h
%{_prefix}/lib/gcc/%{gcc_target_platform}/%{gcc_major}/include/avx512vnniintrin.h
%{_prefix}/lib/gcc/%{gcc_target_platform}/%{gcc_major}/include/avx512vnnivlintrin.h
%{_prefix}/lib/gcc/%{gcc_target_platform}/%{gcc_major}/include/vaesintrin.h
%{_prefix}/lib/gcc/%{gcc_target_platform}/%{gcc_major}/include/vpclmulqdqintrin.h
%{_prefix}/lib/gcc/%{gcc_target_platform}/%{gcc_major}/include/avx512vpopcntdqvlintrin.h
%{_prefix}/lib/gcc/%{gcc_target_platform}/%{gcc_major}/include/avx512bitalgintrin.h
%{_prefix}/lib/gcc/%{gcc_target_platform}/%{gcc_major}/include/pconfigintrin.h
%{_prefix}/lib/gcc/%{gcc_target_platform}/%{gcc_major}/include/wbnoinvdintrin.h
%{_prefix}/lib/gcc/%{gcc_target_platform}/%{gcc_major}/include/movdirintrin.h
%{_prefix}/lib/gcc/%{gcc_target_platform}/%{gcc_major}/include/waitpkgintrin.h
%{_prefix}/lib/gcc/%{gcc_target_platform}/%{gcc_major}/include/cldemoteintrin.h
%{_prefix}/lib/gcc/%{gcc_target_platform}/%{gcc_major}/include/avx512bf16vlintrin.h
%{_prefix}/lib/gcc/%{gcc_target_platform}/%{gcc_major}/include/avx512bf16intrin.h
%{_prefix}/lib/gcc/%{gcc_target_platform}/%{gcc_major}/include/enqcmdintrin.h
%{_prefix}/lib/gcc/%{gcc_target_platform}/%{gcc_major}/include/avx512vp2intersectintrin.h
%{_prefix}/lib/gcc/%{gcc_target_platform}/%{gcc_major}/include/avx512vp2intersectvlintrin.h
%{_prefix}/lib/gcc/%{gcc_target_platform}/%{gcc_major}/include/serializeintrin.h
%{_prefix}/lib/gcc/%{gcc_target_platform}/%{gcc_major}/include/tsxldtrkintrin.h
%{_prefix}/lib/gcc/%{gcc_target_platform}/%{gcc_major}/include/amxtileintrin.h
%{_prefix}/lib/gcc/%{gcc_target_platform}/%{gcc_major}/include/amxint8intrin.h
%{_prefix}/lib/gcc/%{gcc_target_platform}/%{gcc_major}/include/amxbf16intrin.h
%{_prefix}/lib/gcc/%{gcc_target_platform}/%{gcc_major}/include/x86gprintrin.h
%{_prefix}/lib/gcc/%{gcc_target_platform}/%{gcc_major}/include/uintrintrin.h
%{_prefix}/lib/gcc/%{gcc_target_platform}/%{gcc_major}/include/hresetintrin.h
%{_prefix}/lib/gcc/%{gcc_target_platform}/%{gcc_major}/include/keylockerintrin.h
%{_prefix}/lib/gcc/%{gcc_target_platform}/%{gcc_major}/include/avxvnniintrin.h
%{_prefix}/lib/gcc/%{gcc_target_platform}/%{gcc_major}/include/mwaitintrin.h
%{_prefix}/lib/gcc/%{gcc_target_platform}/%{gcc_major}/include/avx512fp16intrin.h
%{_prefix}/lib/gcc/%{gcc_target_platform}/%{gcc_major}/include/avx512fp16vlintrin.h
%{_prefix}/lib/gcc/%{gcc_target_platform}/%{gcc_major}/include/avxifmaintrin.h
%{_prefix}/lib/gcc/%{gcc_target_platform}/%{gcc_major}/include/avxvnniint8intrin.h
%{_prefix}/lib/gcc/%{gcc_target_platform}/%{gcc_major}/include/avxneconvertintrin.h
%{_prefix}/lib/gcc/%{gcc_target_platform}/%{gcc_major}/include/cmpccxaddintrin.h
%{_prefix}/lib/gcc/%{gcc_target_platform}/%{gcc_major}/include/amxfp16intrin.h
%{_prefix}/lib/gcc/%{gcc_target_platform}/%{gcc_major}/include/prfchiintrin.h
%{_prefix}/lib/gcc/%{gcc_target_platform}/%{gcc_major}/include/raointintrin.h
%{_prefix}/lib/gcc/%{gcc_target_platform}/%{gcc_major}/include/amxcomplexintrin.h
%endif
%ifarch ppc64le
%{_prefix}/lib/gcc/%{gcc_target_platform}/%{gcc_major}/include/ppc-asm.h
%{_prefix}/lib/gcc/%{gcc_target_platform}/%{gcc_major}/include/altivec.h
%{_prefix}/lib/gcc/%{gcc_target_platform}/%{gcc_major}/include/ppu_intrinsics.h
%{_prefix}/lib/gcc/%{gcc_target_platform}/%{gcc_major}/include/si2vmx.h
%{_prefix}/lib/gcc/%{gcc_target_platform}/%{gcc_major}/include/spu2vmx.h
%{_prefix}/lib/gcc/%{gcc_target_platform}/%{gcc_major}/include/vec_types.h
%{_prefix}/lib/gcc/%{gcc_target_platform}/%{gcc_major}/include/htmintrin.h
%{_prefix}/lib/gcc/%{gcc_target_platform}/%{gcc_major}/include/htmxlintrin.h
%{_prefix}/lib/gcc/%{gcc_target_platform}/%{gcc_major}/include/bmi2intrin.h
%{_prefix}/lib/gcc/%{gcc_target_platform}/%{gcc_major}/include/bmiintrin.h
%{_prefix}/lib/gcc/%{gcc_target_platform}/%{gcc_major}/include/xmmintrin.h
%{_prefix}/lib/gcc/%{gcc_target_platform}/%{gcc_major}/include/mm_malloc.h
%{_prefix}/lib/gcc/%{gcc_target_platform}/%{gcc_major}/include/emmintrin.h
%{_prefix}/lib/gcc/%{gcc_target_platform}/%{gcc_major}/include/mmintrin.h
%{_prefix}/lib/gcc/%{gcc_target_platform}/%{gcc_major}/include/x86intrin.h
%{_prefix}/lib/gcc/%{gcc_target_platform}/%{gcc_major}/include/pmmintrin.h
%{_prefix}/lib/gcc/%{gcc_target_platform}/%{gcc_major}/include/tmmintrin.h
%{_prefix}/lib/gcc/%{gcc_target_platform}/%{gcc_major}/include/smmintrin.h
%{_prefix}/lib/gcc/%{gcc_target_platform}/%{gcc_major}/include/amo.h
%{_prefix}/lib/gcc/%{gcc_target_platform}/%{gcc_major}/include/nmmintrin.h
%{_prefix}/lib/gcc/%{gcc_target_platform}/%{gcc_major}/include/immintrin.h
%{_prefix}/lib/gcc/%{gcc_target_platform}/%{gcc_major}/include/x86gprintrin.h
%{_prefix}/lib/gcc/%{gcc_target_platform}/%{gcc_major}/include/rs6000-vecdefines.h
%endif
%ifarch aarch64
%{_prefix}/lib/gcc/%{gcc_target_platform}/%{gcc_major}/include/arm_neon.h
%{_prefix}/lib/gcc/%{gcc_target_platform}/%{gcc_major}/include/arm_acle.h
%{_prefix}/lib/gcc/%{gcc_target_platform}/%{gcc_major}/include/arm_fp16.h
%{_prefix}/lib/gcc/%{gcc_target_platform}/%{gcc_major}/include/arm_bf16.h
%{_prefix}/lib/gcc/%{gcc_target_platform}/%{gcc_major}/include/arm_sve.h
%endif
%ifarch s390x
%{_prefix}/lib/gcc/%{gcc_target_platform}/%{gcc_major}/include/s390intrin.h
%{_prefix}/lib/gcc/%{gcc_target_platform}/%{gcc_major}/include/htmintrin.h
%{_prefix}/lib/gcc/%{gcc_target_platform}/%{gcc_major}/include/htmxlintrin.h
%{_prefix}/lib/gcc/%{gcc_target_platform}/%{gcc_major}/include/vecintrin.h
%endif
%{_prefix}/libexec/gcc/%{gcc_target_platform}/%{gcc_major}/collect2
%{_prefix}/lib/gcc/%{gcc_target_platform}/%{gcc_major}/crt*.o
%{_prefix}/lib/gcc/%{gcc_target_platform}/%{gcc_major}/libgcc.a
%{_prefix}/lib/gcc/%{gcc_target_platform}/%{gcc_major}/libgcov.a
%{_prefix}/lib/gcc/%{gcc_target_platform}/%{gcc_major}/libgcc_eh.a
%{_prefix}/lib/gcc/%{gcc_target_platform}/%{gcc_major}/libgcc_s.so
%{_prefix}/lib/gcc/%{gcc_target_platform}/%{gcc_major}/libgcc_s_dummy.so
%{_prefix}/lib/gcc/%{gcc_target_platform}/%{gcc_major}/libgomp.spec
%{_prefix}/lib/gcc/%{gcc_target_platform}/%{gcc_major}/libgomp.a
%{_prefix}/lib/gcc/%{gcc_target_platform}/%{gcc_major}/libgomp.so
%if %{build_libquadmath}
%{_prefix}/lib/gcc/%{gcc_target_platform}/%{gcc_major}/libquadmath.a
%{_prefix}/lib/gcc/%{gcc_target_platform}/%{gcc_major}/libquadmath.so
%endif
%if %{build_libitm}
%{_prefix}/lib/gcc/%{gcc_target_platform}/%{gcc_major}/libitm.spec
%{_prefix}/lib/gcc/%{gcc_target_platform}/%{gcc_major}/libitm.a
%{_prefix}/lib/gcc/%{gcc_target_platform}/%{gcc_major}/libitm.so
%endif
%if %{build_libatomic}
%{_prefix}/lib/gcc/%{gcc_target_platform}/%{gcc_major}/libatomic.a
%{_prefix}/lib/gcc/%{gcc_target_platform}/%{gcc_major}/libatomic.so
%endif
%if %{build_annobin_plugin}
%dir %{_prefix}/lib/gcc/%{gcc_target_platform}/%{gcc_major}/plugin
%{_prefix}/lib/gcc/%{gcc_target_platform}/%{gcc_major}/plugin/annobin.so
%{_prefix}/lib/gcc/%{gcc_target_platform}/%{gcc_major}/plugin/gcc-annobin.so
%{_prefix}/lib/gcc/%{gcc_target_platform}/%{gcc_major}/plugin/gcc-annobin.so.0
%{_prefix}/lib/gcc/%{gcc_target_platform}/%{gcc_major}/plugin/gcc-annobin.so.0.0.0
%endif
%doc gcc/README* rpm.doc/changelogs/gcc/ChangeLog* 
%license gcc/COPYING* COPYING.RUNTIME

%files -n gcc%{gcc_major}-c++
%{_prefix}/bin/%{gcc_target_platform}-*++-%{gcc_major}
%{_prefix}/bin/g++-%{gcc_major}
%{_mandir}/man1/g++-%{gcc_major}.1*
%dir %{_prefix}/lib/gcc
%dir %{_prefix}/lib/gcc/%{gcc_target_platform}
%dir %{_prefix}/lib/gcc/%{gcc_target_platform}/%{gcc_major}
%dir %{_prefix}/libexec/gcc
%dir %{_prefix}/libexec/gcc/%{gcc_target_platform}
%dir %{_prefix}/libexec/gcc/%{gcc_target_platform}/%{gcc_major}
%{_prefix}/libexec/gcc/%{gcc_target_platform}/%{gcc_major}/cc1plus
%{_prefix}/libexec/gcc/%{gcc_target_platform}/%{gcc_major}/g++-mapper-server
%{_prefix}/lib/gcc/%{gcc_target_platform}/%{gcc_major}/libstdc++.a
%{_prefix}/lib/gcc/%{gcc_target_platform}/%{gcc_major}/libstdc++fs.a
%{_prefix}/lib/gcc/%{gcc_target_platform}/%{gcc_major}/libstdc++exp.a
%{_prefix}/lib/gcc/%{gcc_target_platform}/%{gcc_major}/libstdc++_libbacktrace.a
%{_prefix}/lib/gcc/%{gcc_target_platform}/%{gcc_major}/libsupc++.a
%{_prefix}/lib/gcc/%{gcc_target_platform}/%{gcc_major}/libstdc++.so
%dir %{_prefix}/include/c++
%{_prefix}/include/c++/%{gcc_major}
%doc rpm.doc/changelogs/gcc/cp/ChangeLog*

%files -n gcc%{gcc_major}-gfortran
%{_prefix}/bin/gfortran-%{gcc_major}
%{_mandir}/man1/gfortran-%{gcc_major}.1*
%dir %{_prefix}/lib/gcc
%dir %{_prefix}/lib/gcc/%{gcc_target_platform}
%dir %{_prefix}/lib/gcc/%{gcc_target_platform}/%{gcc_major}
%dir %{_prefix}/libexec/gcc
%dir %{_prefix}/libexec/gcc/%{gcc_target_platform}
%dir %{_prefix}/libexec/gcc/%{gcc_target_platform}/%{gcc_major}
%dir %{_prefix}/lib/gcc/%{gcc_target_platform}/%{gcc_major}/include
%dir %{_prefix}/lib/gcc/%{gcc_target_platform}/%{gcc_major}/finclude
%{_prefix}/lib/gcc/%{gcc_target_platform}/%{gcc_major}/include/ISO_Fortran_binding.h
%{_prefix}/lib/gcc/%{gcc_target_platform}/%{gcc_major}/finclude/omp_lib.h
%{_prefix}/lib/gcc/%{gcc_target_platform}/%{gcc_major}/finclude/omp_lib.f90
%{_prefix}/lib/gcc/%{gcc_target_platform}/%{gcc_major}/finclude/omp_lib.mod
%{_prefix}/lib/gcc/%{gcc_target_platform}/%{gcc_major}/finclude/omp_lib_kinds.mod
%{_prefix}/lib/gcc/%{gcc_target_platform}/%{gcc_major}/finclude/openacc.f90
%{_prefix}/lib/gcc/%{gcc_target_platform}/%{gcc_major}/finclude/openacc.mod
%{_prefix}/lib/gcc/%{gcc_target_platform}/%{gcc_major}/finclude/openacc_kinds.mod
%{_prefix}/lib/gcc/%{gcc_target_platform}/%{gcc_major}/finclude/openacc_lib.h
%{_prefix}/lib/gcc/%{gcc_target_platform}/%{gcc_major}/finclude/ieee_arithmetic.mod
%{_prefix}/lib/gcc/%{gcc_target_platform}/%{gcc_major}/finclude/ieee_exceptions.mod
%{_prefix}/lib/gcc/%{gcc_target_platform}/%{gcc_major}/finclude/ieee_features.mod
%{_prefix}/libexec/gcc/%{gcc_target_platform}/%{gcc_major}/f951
%{_prefix}/lib/gcc/%{gcc_target_platform}/%{gcc_major}/libgfortran.spec
%{_prefix}/lib/gcc/%{gcc_target_platform}/%{gcc_major}/libcaf_single.a
%{_prefix}/lib/gcc/%{gcc_target_platform}/%{gcc_major}/libgfortran.a
%{_prefix}/lib/gcc/%{gcc_target_platform}/%{gcc_major}/libgfortran.so
%doc rpm.doc/gfortran/*

%dir %{_prefix}/lib/gcc/%{gcc_target_platform}/%{gcc_major}/plugin
%{_prefix}/lib/gcc/%{gcc_target_platform}/%{gcc_major}/plugin/gcc-annobin.so
%{_prefix}/lib/gcc/%{gcc_target_platform}/%{gcc_major}/plugin/gcc-annobin.so.0
%{_prefix}/lib/gcc/%{gcc_target_platform}/%{gcc_major}/plugin/gcc-annobin.so.0.0.0

%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 13.3.1-2.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 13.3.1-2.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jul 11 2024 Jakub Jelinek <jakub@redhat.com> 13.3.1-2
- initial package
