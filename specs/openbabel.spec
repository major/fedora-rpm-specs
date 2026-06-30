%{!?perl_vendorarch:%global perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)}

# we don't want to provide private Perl or Python extension libs
%global __provides_exclude_from ^(%{perl_vendorarch}/auto|%{python3_sitearch})/.*\\.so$

# Avoid LTO flags in these architectures:
# eigen3/Eigen/src/Core/arch/AltiVec/MatrixProduct.h:1199:26:
# error: inlining failed in call to 'always_inline' 'Eigen::internal::bload<Eigen::internal::blas_data_mapper<double, long, 0, 0, 1>, double __vector(2), long, 2l, 0, 
%if 0%{?rhel}
%ifarch %{power64}
%define _lto_cflags %{nil}
%endif
%endif

Name: openbabel
Version: 3.2.0
Release: %autorelease
Summary: Chemistry software file format converter
License: GPL-2.0-only
URL: https://openbabel.org/
Source0: https://github.com/openbabel/openbabel/archive/openbabel-openbabel-%(echo %{version} | tr '.' '-').tar.gz
Source1: obgui.desktop
Source2: openbabel-inchi-license-lgpl-2.1.txt

# fix perl modules install path
Patch0: %{name}-perl.patch

# fix openbabel version + cmake config files
Patch1: %{name}-plugindir.patch

# Fix path to libdir in .pc file
# https://bugzilla.redhat.com/show_bug.cgi?id=1669664
Patch5: %{name}-fix-libdir-in-pkgconfig.patch

# (temporarily) disable some tests on: riscv64
Patch11: %{name}-disable-tests-riscv64.patch

BuildRequires: make
BuildRequires: boost-devel
BuildRequires: swig
BuildRequires: cmake
BuildRequires: dos2unix
BuildRequires: desktop-file-utils
BuildRequires: eigen3-devel
BuildRequires: gcc-c++
%if 0%{?fedora}
BuildRequires: inchi-devel >= 1.0.3
%endif
%if 0%{?fedora} || 0%{?rhel} >= 10
BuildRequires: wxGTK-devel
%else
BuildRequires: wxGTK3-devel
%endif
BuildRequires: libxml2-devel
BuildRequires: ImageMagick
BuildRequires: rapidjson-devel
Requires:      %{name}-libs%{?_isa} = %{version}-%{release}
%description
Open Babel is a free, open-source version of the Babel chemistry file
translation program. Open Babel is a project designed to pick up where
Babel left off, as a cross-platform program and library designed to
interconvert between many file formats used in molecular modeling,
computational chemistry, and many related areas.
This package contains the command-line utility, which is intended to
be used as a replacement for the original babel program, to translate
between various chemical file formats as well as a wide variety of
utilities to foster development of other open source scientific
software.

%package devel
Summary: Development tools for programs which will use the Open Babel library
Requires: %{name}-libs%{?_isa} = %{version}-%{release}
Requires: eigen3-devel
%description devel
The %{name}-devel package includes the header files and libraries
necessary for developing programs using the Open Babel library.

%package doc
Summary: Additional documentation for the Open Babel library
BuildArch: noarch
%description doc
This package contains additional documentation for Open Babel.

%package gui
Summary: Chemistry software file format converter - GUI version
Requires: %{name}-libs%{?_isa} = %{version}-%{release}
%description gui
Open Babel is a free, open-source version of the Babel chemistry file
translation program. Open Babel is a project designed to pick up where
Babel left off, as a cross-platform program and library designed to
interconvert between many file formats used in molecular modeling,
computational chemistry, and many related areas.
This package contains the graphical interface.

%package libs
Summary: Chemistry software file format converter - libraries
%if 0%{?rhel}
License: GPL-2.0-only AND LGPL-2.1-or-later
Provides: bundled(libinchi) = 1.07.4
%endif
%description libs
Open Babel is a free, open-source version of the Babel chemistry file
translation program. Open Babel is a project designed to pick up where
Babel left off, as a cross-platform program and library designed to
interconvert between many file formats used in molecular modeling,
computational chemistry, and many related areas.
This package contains the C++ library, which includes all of the
file-translation code.

%package -n perl-%{name}
Summary: Perl wrapper for the Open Babel library
Requires: %{name}-libs%{?_isa} = %{version}-%{release}
BuildRequires: perl-devel
BuildRequires: perl-generators
%description -n perl-%{name}
Perl wrapper for the Open Babel library.

%package -n python3-%{name}
Summary: Python wrapper for the Open Babel library
Requires: %{name}-libs%{?_isa} = %{version}-%{release}
BuildRequires: python3-devel
BuildRequires: python3-setuptools
%{?python_provide:%python_provide python3-%{name}}
Obsoletes: python2-%{name} < 0:%{version}-%{release}
%description -n python3-%{name}
Python3 wrapper for the Open Babel library.

%package -n ruby-%{name}
Summary: Ruby wrapper for the Open Babel library
Requires: ruby(release)
Requires: %{name}-libs%{?_isa} = %{version}-%{release}
BuildRequires: ruby-devel
%description -n ruby-%{name}
Ruby wrapper for the Open Babel library.

%prep
%setup -q -n %{name}-%{name}-%(echo %{version} | tr '.' '-')
%patch -P 0 -p1 -b .perl_path
%patch -P 1 -p1 -b .plugindir
%patch -P 5 -p1 -b .backup
%ifarch riscv64
#patch -P 11 -p1 -b .riscv64
%endif

%if 0%{?fedora}
rm -rf src/formats/libinchi
%else
cp -p %{SOURCE2} ./inchi-license-lgpl-2.1.txt
%endif

# convert to Unix line endings
dos2unix -k \
  data/chemdrawcdx.h \
  include/openbabel/{tautomer.h,math/align.h} \
  src/math/align.cpp \
  test/testsmartssym.py \

magick src/GUI/babel.xpm -transparent white babel.png

# Remove duplicate html files
pushd doc
for man in *.1; do
 html=`basename $man .1`.html
 if [ -f $html ]; then
   rm $html
 fi
done
popd

%build
%if 0%{?fedora} || 0%{?rhel}
# RHBZ #1996330
%ifarch %{power64}
export CXXFLAGS="%{optflags} -DEIGEN_ALTIVEC_DISABLE_MMA"
%endif
%endif
%cmake \
 -Wno-dev \
 -DCMAKE_SKIP_RPATH:BOOL=ON \
 -DBUILD_GUI:BOOL=ON \
 -DPYTHON_BINDINGS:BOOL=ON \
 -DPYTHON_EXECUTABLE=%{__python3} \
 -DPERL_BINDINGS:BOOL=ON \
 -DRUBY_BINDINGS:BOOL=ON \
 -DWITH_MAEPARSER:BOOL=OFF \
 -DWITH_COORDGEN:BOOL=OFF \
 -DOB_PLUGIN_INSTALL_DIR:PATH=%{_lib}/openbabel3 \
%if 0%{?rhel}
 -DOPENBABEL_USE_SYSTEM_INCHI=false \
%else
 -DOPENBABEL_USE_SYSTEM_INCHI=true \
 -DINCHI_INCLUDE_DIR:PATH=%{_includedir}/inchi \
 -DINCHI_LIBRARY:FILEPATH=%{_libdir}/libinchi.so \
%endif
 -DENABLE_VERSIONED_FORMATS=false \
 -DRUN_SWIG:BOOL=ON \
 -DENABLE_TESTS:BOOL=ON \
 -DOPTIMIZE_NATIVE=OFF \
 -DGLIBC_24_COMPATIBLE:BOOL=OFF \
 -DEigen3_DIR:PATH=%{_datadir}/cmake/eigen3 \
 -DRUBY_INSTDIR:PATH=%{_libdir}/ruby/vendor_ruby

%cmake_build

%install
%cmake_install

rm -f %{buildroot}%{_libdir}/cmake/openbabel2/*.cmake

desktop-file-install --dir=%{buildroot}%{_datadir}/applications %{SOURCE1}
install -Dpm644 babel.png %{buildroot}%{_datadir}/pixmaps/babel.png

# Create profile files
mkdir -p %{buildroot}%{_sysconfdir}/profile.d
cat > %{buildroot}%{_sysconfdir}/profile.d/openbabel3.sh <<EOF
BABEL_LIBDIR=%{_libdir}/%{name}3
export BABEL_LIBDIR
BABEL_DATADIR=%{_datadir}/%{name}
export BABEL_DATADIR
EOF
cat > %{buildroot}%{_sysconfdir}/profile.d/openbabel3.csh <<EOF
setenv BABEL_LIBDIR %{_libdir}/%{name}3
setenv BABEL_DATADIR %{_datadir}/%{name}
EOF

%if 1
%check
# rm the built ruby bindings for testsuite to succeed (Red Hat bugzilla ticket #1191173)
rm -f %{_vpath_builddir}/%{_lib}/openbabel.so

export CTEST_OUTPUT_ON_FAILURE=1
export PYTHONPATH=%{buildroot}%{python3_sitearch}
# See https://github.com/openbabel/openbabel/issues/2138, https://github.com/openbabel/openbabel/issues/2766
%ctest -E 'pybindtest_bindings|pybindtest_obconv_writers|test_align_4|test_align_5'
%endif

%files
%config(noreplace) %{_sysconfdir}/profile.d/openbabel3.sh
%config(noreplace) %{_sysconfdir}/profile.d/openbabel3.csh
%{_bindir}/ob*
%{_bindir}/roundtrip
%{_mandir}/man1/*.1*
%exclude %{_bindir}/obgui
%exclude %{_mandir}/man1/obgui.1*

%files devel
%{_includedir}/%{name}3/
%{_libdir}/libopenbabel.so
%{_libdir}/pkgconfig/openbabel-3.pc
%{_libdir}/cmake/openbabel3/
%if 0%{?rhel}
%{_libdir}/libinchi.so
%{_includedir}/inchi/
%endif

%files doc
%doc doc/*.html doc/README* doc/dioxin.*

%files gui
%{_bindir}/obgui
%{_datadir}/applications/obgui.desktop
%{_datadir}/pixmaps/babel.png
%{_mandir}/man1/obgui.1*

%files libs
%license COPYING
%doc THANKS AUTHORS authors.txt README.md
%{_datadir}/%{name}/
%{_libdir}/%{name}3/
%{_libdir}/libopenbabel.so.8
%{_libdir}/libopenbabel.so.8.0.0
%if 0%{?rhel}
%license inchi-license-lgpl-2.1.txt
%{_libdir}/libinchi.so.1.07.4
%{_libdir}/libinchi.so.1
%endif

%files -n perl-%{name}
%{perl_vendorarch}/Chemistry/OpenBabel.pm
%dir %{perl_vendorarch}/*/Chemistry/OpenBabel
%{perl_vendorarch}/*/Chemistry/OpenBabel/OpenBabel.so

%files -n python3-%{name}
%{python3_sitearch}/openbabel/

%files -n ruby-%{name}
%{ruby_vendorarchdir}/openbabel.so

%changelog
%autochangelog
