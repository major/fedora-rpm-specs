# From src/version.h:#define OCTAVE_API_VERSION
%global octave_api api-v59

%global macrosdir %(d=%{_rpmconfigdir}/macros.d; [ -d $d ] || d=%{_sysconfdir}/rpm; echo $d)

%global builddocs 1

%if 0%{?fedora}
%bcond_without flexiblas
%endif
%if %{with flexiblas}
%global blaslib flexiblas
%else
%global blaslib openblas
%endif

# No more Java on i686
%ifarch %{java_arches}
%bcond_without java
%else
%bcond_with java
%endif

# Compile with ILP64 BLAS - not yet working
%bcond_with blas64

# For rc versions, change release manually
#global rcver 2
%if 0%{?rcver:1}
%global rctag  -rc%{?rcver}
%global relsuf .rc%{?rcver}
%endif

%global optflags %{optflags}
%global build_ldflags %{build_ldflags} -flto

Name:           octave
Epoch:          6
Version:        9.4.0
Release:        %autorelease
Summary:        A high-level language for numerical computations
# Automatically converted from old format: GPLv3+ - review is highly recommended.
License:        GPL-3.0-or-later
URL:            http://www.octave.org

Source0:        https://ftp.gnu.org/gnu/octave/octave-%{version}.tar.lz
#Source0:        https://alpha.gnu.org/gnu/octave/octave-%{version}%{?rctag}.tar.lz
# RPM macros for helping to build Octave packages
Source1:        macros.octave
Source2:        xorg.conf
%if !%{builddocs}
Source3:        octave-%{version}-docs.tar.xz
%endif
# Add needed time.h header
Patch2:         octave-time.patch

Provides:       octave(api) = %{octave_api}
Provides:       bundled(gnulib)
Provides:       bundled(qterminal)
# From liboctave/cruft
Provides:       bundled(amos)
Provides:       bundled(blas-xtra)
Provides:       bundled(daspk)
Provides:       bundled(dasrt)
Provides:       bundled(dassl)
Provides:       bundled(faddeeva)
Provides:       bundled(lapack-xtra)
Provides:       bundled(odepack)
Provides:       bundled(ordered-qz)
Provides:       bundled(quadpack)
Provides:       bundled(ranlib)
Provides:       bundled(slatec-err)
Provides:       bundled(slatec-fn)

# For Source0
BuildRequires: make
BuildRequires:  lzip

# For autoreconf
BuildRequires:  automake
BuildRequires:  libtool
# For validating desktop and appdata files
BuildRequires:  desktop-file-utils
BuildRequires:  libappstream-glib

BuildRequires:  arpack-devel
BuildRequires:  %{blaslib}-devel
BuildRequires:  bison
BuildRequires:  bzip2-devel
BuildRequires:  curl-devel
BuildRequires:  fftw-devel
BuildRequires:  flex
BuildRequires:  fltk-devel
BuildRequires:  gcc-c++
BuildRequires:  gcc-gfortran
BuildRequires:  ghostscript
BuildRequires:  gl2ps-devel
BuildRequires:  glpk-devel
BuildRequires:  gnuplot
BuildRequires:  gperf
BuildRequires:  GraphicsMagick-c++-devel
BuildRequires:  hdf5-devel
%if %{with java}
BuildRequires:  java-devel
%if 0%{?fedora}
BuildRequires:  javapackages-local
%endif
%endif
BuildRequires:  less
BuildRequires:  libsndfile-devel
BuildRequires:  libX11-devel
BuildRequires:  llvm-devel
BuildRequires:  mesa-libGL-devel
BuildRequires:  mesa-libGLU-devel
BuildRequires:  ncurses-devel
BuildRequires:  pcre2-devel
BuildRequires:  portaudio-devel
BuildRequires:  qhull-devel
BuildRequires:  qrupdate-devel
BuildRequires:  qscintilla-qt6-devel
BuildRequires:  qt6-linguist
BuildRequires:  qt6-qttools-devel
BuildRequires:  pkgconfig(Qt6Core5Compat)
BuildRequires:  rapidjson-devel
BuildRequires:  readline-devel
%if %{with blas64}
BuildRequires:  suitesparse64-devel
%else
BuildRequires:  suitesparse-devel
%endif
# EPEL9 is missing sundials - https://bugzilla.redhat.com/show_bug.cgi?id=2063760
%if 0%{?fedora} || 0%{?rhel} != 9
BuildRequires:  sundials-devel
%endif
BuildRequires:  tex(dvips)
BuildRequires:  texinfo
BuildRequires:  texinfo-tex
BuildRequires:  texlive-collection-fontsrecommended
%if 0%{?rhel} >= 7
BuildRequires:  texlive-ec
BuildRequires:  texlive-metapost
%endif
BuildRequires:  zlib-devel
# For check
BuildRequires:  mesa-dri-drivers
%ifnarch s390 s390x
BuildRequires:  xorg-x11-drv-dummy
%endif
BuildRequires:  zip

Requires:       epstool
Requires:       gnuplot
Requires:       gnuplot-common
Requires:       hdf5 = %{_hdf5_version}
Requires:       hicolor-icon-theme
%if %{with java}
Requires:       java-headless
%endif
Requires:       less
Requires:       info
Requires:       texinfo
# Rrom scripts/general/private/__publish_latex_output__.m
Requires:       tex(amssymb.sty)
Requires:       tex(fontenc.sty)
Requires:       tex(graphicx.sty)
Requires:       tex(hyperref.sty)
Requires:       tex(inputenc.sty)
Requires:       tex(listings.sty)
Requires:       tex(lmodern.sty)
Requires:       tex(mathtools.sty)
Requires:       tex(titlesec.sty)
Requires:       tex(xcolor.sty)
# Rrom scripts/plot/util/print.m:
Requires:       tex(color.sty)
Requires:       tex(epsfig.sty)
Requires:       tex(geometry.sty)
Requires:       tex(graphicx.sty)


%description
GNU Octave is a high-level language, primarily intended for numerical
computations. It provides a convenient command line interface for
solving linear and nonlinear problems numerically, and for performing
other numerical experiments using a language that is mostly compatible
with Matlab. It may also be used as a batch-oriented language. Octave
has extensive tools for solving common numerical linear algebra
problems, finding the roots of nonlinear equations, integrating
ordinary functions, manipulating polynomials, and integrating ordinary
differential and differential-algebraic equations. It is easily
extensible and customizable via user-defined functions written in
Octave's own language, or using dynamically loaded modules written in
C++, C, Fortran, or other languages.


%package devel
Summary:        Development headers and files for Octave
Requires:       %{name} = %{epoch}:%{version}-%{release}
Requires:       gcc-c++
Requires:       gcc-gfortran
Requires:       fftw-devel%{?_isa}
Requires:       hdf5-devel%{?_isa}
Requires:       %{blaslib}-devel%{?_isa}
Requires:       readline-devel%{?_isa}
Requires:       zlib-devel
Requires:       libappstream-glib

%description devel
The octave-devel package contains files needed for developing
applications which use GNU Octave.


%package doc
Summary:        Documentation for Octave
BuildArch:      noarch

%description doc
This package contains documentation for Octave.

%prep
%autosetup -p1 -n %{name}-%{version}%{?rctag}
%if %{with blas64}
sed -i -e 's/OCTAVE_CHECK_LIB(suitesparseconfig,/OCTAVE_CHECK_LIB(suitesparseconfig64,/' configure.ac
%endif

%build
export AR=%{_bindir}/gcc-ar
export RANLIB=%{_bindir}/gcc-ranlib
export NM=%{_bindir}/gcc-nm
export F77=gfortran
# TODO: some items appear to be bundled in libcruft..
#   gl2ps.c is bundled.  Anything else?
%if !%{builddocs}
%global disabledocs --disable-docs
%endif
%if %{with java}
# Find libjvm.so for this architecture in generic location
libjvm=$(find /usr/lib/jvm/jre/lib -name libjvm.so -printf %h)
export JAVA_HOME=%{java_home}
%endif
# JIT support is still experimental, and causes a segfault on ARM.
# --enable-float-truncate - https://savannah.gnu.org/bugs/?40560
# sundials headers need to know where to find suitesparse headers
export CPPFLAGS=-I%{_includedir}/suitesparse
# Disable _GLIBCXX_ASSERTIONS for now
# https://savannah.gnu.org/bugs/?55547
export CXXFLAGS="$(echo %optflags | sed s/-Wp,-D_GLIBCXX_ASSERTIONS//)"

verstr=$(%{__cxx} --version | head -1)
if [[ "$verstr" == *"GCC"* ]]; then
  CXXFLAGS="$CXXFLAGS -flto=auto"
else
  CXXFLAGS="$CXXFLAGS -flto"
fi

%configure --enable-shared --disable-static \
 --enable-float-truncate \
 %{?disabledocs} \
 --disable-silent-rules \
 --with-blas=%{blaslib}%{?with_blas64:64}  \
%if %{with java}
 --with-java-includedir=/usr/lib/jvm/java/include \
 --with-java-libdir=$libjvm \
%endif
 --with-qrupdate \
 --with-amd --with-umfpack --with-colamd --with-ccolamd --with-cholmod \
 --with-cxsparse

# Check that octave_api is set correctly (autogenerated file)
make liboctave/version.h
if ! grep -q '^#define OCTAVE_API_VERSION "%{octave_api}"' liboctave/version.h
then
  echo "octave_api variable in spec does not match liboctave/version.h"
  exit 1
fi

%make_build OCTAVE_RELEASE="Fedora %{version}%{?rctag}-%{release}"

%install
%make_install

# Docs - In case we didn't build them and to explicitly install pre-built docs
make install-data install-html install-info install-pdf DESTDIR=%{buildroot}
mkdir -p %{buildroot}%{_pkgdocdir}
cp -ar AUTHORS BUGS ChangeLog examples NEWS README %{buildroot}%{_pkgdocdir}/
cp -a doc/refcard/*.pdf %{buildroot}%{_pkgdocdir}/
%if !%{builddocs}
tar xvf %SOURCE3 -C %{buildroot}
%endif

find %{buildroot}%{_libdir} -name \*.la -delete

# No info directory
rm -f %{buildroot}%{_infodir}/dir

# Make library links
mkdir -p %{buildroot}%{_sysconfdir}/ld.so.conf.d
echo "%{_libdir}/octave/%{version}%{?rctag}" > %{buildroot}%{_sysconfdir}/ld.so.conf.d/octave-%{_arch}.conf

# Remove RPM_BUILD_ROOT from ls-R files
perl -pi -e "s,%{buildroot},," %{buildroot}%{_libdir}/%{name}/ls-R
perl -pi -e "s,%{buildroot},," %{buildroot}%{_datadir}/%{name}/ls-R
# Make sure ls-R exists
touch %{buildroot}%{_datadir}/%{name}/ls-R

desktop-file-validate %{buildroot}%{_datadir}/applications/org.octave.Octave.desktop
# RHEL7 still doesn't like the GNU project_group
%{?el7:sed -i -e /project_group/d %{buildroot}/%{_datadir}/metainfo/org.octave.Octave.metainfo.xml}
appstream-util validate-relax --nonet %{buildroot}/%{_datadir}/metainfo/org.octave.Octave.metainfo.xml

# Create directories for add-on packages
HOST_TYPE=`%{buildroot}%{_bindir}/octave-config -p CANONICAL_HOST_TYPE`
mkdir -p %{buildroot}%{_libdir}/%{name}/site/oct/%{octave_api}/$HOST_TYPE
mkdir -p %{buildroot}%{_libdir}/%{name}/site/oct/$HOST_TYPE
mkdir -p %{buildroot}%{_datadir}/%{name}/packages
mkdir -p %{buildroot}%{_libdir}/%{name}/packages
touch %{buildroot}%{_datadir}/%{name}/octave_packages

# Fix multilib installs
for include in octave-config defaults
do
   mv %{buildroot}%{_includedir}/%{name}-%{version}%{?rctag}/%{name}/${include}.h \
      %{buildroot}%{_includedir}/%{name}-%{version}%{?rctag}/%{name}/${include}-%{__isa_bits}.h
   cat > %{buildroot}%{_includedir}/%{name}-%{version}%{?rctag}/%{name}/${include}.h <<EOF
#include <bits/wordsize.h>

#if __WORDSIZE == 32
#include "${include}-32.h"
#elif __WORDSIZE == 64
#include "${include}-64.h"
#else
#error "Unknown word size"
#endif
EOF
done
for script in octave-config-%{version}%{?rctag} mkoctfile-%{version}%{?rctag}
do
   mv %{buildroot}%{_bindir}/${script} %{buildroot}%{_libdir}/%{name}/%{version}%{?rctag}/${script}
   cat > %{buildroot}%{_bindir}/${script} <<EOF
#!/bin/bash
ARCH=\$(uname -m)

case \$ARCH in
x86_64 | ia64 | s390x | aarch64 | ppc64 | ppc64le | riscv64) LIB_DIR=/usr/lib64
                       SECONDARY_LIB_DIR=/usr/lib
                       ;;
* )
                       LIB_DIR=/usr/lib
                       SECONDARY_LIB_DIR=/usr/lib64
                       ;;
esac

if [ ! -x \$LIB_DIR/%{name}/%{version}%{?rctag}/${script} ] ; then
  if [ ! -x \$SECONDARY_LIB_DIR/%{name}/%{version}%{?rctag}/${script} ] ; then
    echo "Error: \$LIB_DIR/%{name}/%{version}%{?rctag}/${script} not found"
    if [ -d \$SECONDARY_LIB_DIR ] ; then
      echo "   and \$SECONDARY_LIB_DIR/%{name}/%{version}%{?rctag}/${script} not found"
    fi
    exit 1
  fi
  LIB_DIR=\$SECONDARY_LIB_DIR
fi
exec \$LIB_DIR/%{name}/%{version}%{?rctag}/${script} "\$@"
EOF
   chmod +x %{buildroot}%{_bindir}/${script}
done
%if %{builddocs}
# remove timestamp from doc-cache
sed -i -e '/^# Created by Octave/d' %{buildroot}%{_datadir}/%{name}/%{version}%{?rctag}/etc/doc-cache
%else
cp -p doc/interpreter/macros.texi %{buildroot}%{_datadir}/%{name}/%{version}/etc/macros.texi
%endif

# rpm macros
mkdir -p %{buildroot}%{macrosdir}
cp -p %SOURCE1 %{buildroot}%{macrosdir}


%check
cp %SOURCE2 .
if [ -x /usr/libexec/Xorg ]; then
   Xorg=/usr/libexec/Xorg
else
   Xorg=/usr/libexec/Xorg.bin
fi
$Xorg -noreset +extension GLX +extension RANDR +extension RENDER -logfile ./xorg.log -config ./xorg.conf :99 &
sleep 2
export DISPLAY=:99
export FLEXIBLAS=netlib
%ifarch ppc64le riscv64
# liboctave/array/dMatrix.cc-tst segfaults
# riscv: image/getframe.m ...............................................LLVM ERROR: Relocation type not implemented yet!
make check || :
%else
make check
%endif

%ldconfig_scriptlets

%files
%license COPYING
%dir %{_pkgdocdir}
%{_pkgdocdir}/AUTHORS
%{_pkgdocdir}/BUGS
%{_pkgdocdir}/ChangeLog
%{_pkgdocdir}/NEWS
%{_pkgdocdir}/README
# FIXME: Create an -emacs package that has the emacs addon
%config(noreplace) %{_sysconfdir}/ld.so.conf.d/octave-*.conf
%{_bindir}/octave*
%dir %{_libdir}/octave/
%dir %{_libdir}/octave/%{version}
%{_libdir}/octave/%{version}/liboctave.so.11*
%{_libdir}/octave/%{version}/liboctgui.so.12*
%{_libdir}/octave/%{version}/liboctinterp.so.12*
%{_libdir}/octave/%{version}/mkoctfile-%{version}
%{_libdir}/octave/%{version}/oct/
%{_libdir}/octave/%{version}/octave-config-%{version}
%{_libdir}/octave/%{version}/site/
%{_libdir}/octave/packages/
%{_libdir}/octave/site/
%{_libexecdir}/octave/
%{_mandir}/man1/octave*.1.*
%{_infodir}/liboctave.info*
%{_infodir}/octave.info*
%{_datadir}/applications/org.octave.Octave.desktop
%{_datadir}/icons/hicolor/*/apps/octave.png
%{_datadir}/icons/hicolor/scalable/apps/octave.svg
%{_datadir}/metainfo/org.octave.Octave.metainfo.xml
# octave_packages is %ghost, so need to list everything else separately
%dir %{_datadir}/octave
%{_datadir}/octave/%{version}%{?rctag}/
%{_datadir}/octave/ls-R
%ghost %{_datadir}/octave/octave_packages
%{_datadir}/octave/packages/
%{_datadir}/octave/site/

%files devel
%{macrosdir}/macros.octave
%{_bindir}/mkoctfile
%{_bindir}/mkoctfile-%{version}%{?rctag}
%{_includedir}/octave-%{version}%{?rctag}/
%{_libdir}/octave/%{version}/liboctave.so
%{_libdir}/octave/%{version}/liboctgui.so
%{_libdir}/octave/%{version}/liboctinterp.so
%{_libdir}/pkgconfig/octave.pc
%{_libdir}/pkgconfig/octinterp.pc
%{_mandir}/man1/mkoctfile.1.*

%files doc
%{_pkgdocdir}/examples/
%{_pkgdocdir}/liboctave.html/
%{_pkgdocdir}/liboctave.pdf
%{_pkgdocdir}/octave.html
%{_pkgdocdir}/octave.pdf
%{_pkgdocdir}/refcard*.pdf

%changelog
%autochangelog
