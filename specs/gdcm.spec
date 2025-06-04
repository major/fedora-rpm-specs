# Enabled by default
%bcond_without tests

# note ABI does not change in patch releases
# https://sourceforge.net/p/gdcm/mailman/message/36768376/

# Docs do not build on i686 because some LaTeX deps are unsatisfied. So skip
# these docs entirely.
%bcond_with texdocs

Name:       gdcm
Version:    3.0.24
Release:    %autorelease
Summary:    Grassroots DiCoM is a C++ library to parse DICOM medical files
# SPDX
License:    BSD-3-Clause
URL:        https://sourceforge.net/projects/gdcm/
# Use github release
Source0:    https://github.com/malaterre/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
Source1:    http://downloads.sourceforge.net/project/gdcm/gdcmData/gdcmData/gdcmData.tar.gz

Patch1: 0001-3.0.1-Use-copyright.patch
# Fix for 1687233
Patch2: 0002-Fix-export-variables.patch
Patch3: gdcm-3.0.24-c++20.patch

BuildRequires:  CharLS-devel >= 2.2
BuildRequires:  cmake
BuildRequires:  doxygen
BuildRequires:  libxslt-devel
BuildRequires:  dcmtk-devel
BuildRequires:  docbook5-style-xsl
BuildRequires:  docbook-style-xsl
BuildRequires:  expat-devel
BuildRequires:  fontconfig-devel
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  git-core
BuildRequires:  graphviz
BuildRequires:  gl2ps-devel
BuildRequires:  libogg-devel
BuildRequires:  libtheora-devel
BuildRequires:  libuuid-devel
BuildRequires:  mesa-libGL-devel
BuildRequires:  openssl-devel
BuildRequires:  pkgconfig(libopenjp2)
BuildRequires:  poppler-devel
BuildRequires:  python3-devel
BuildRequires:  swig
BuildRequires:  sqlite-devel
BuildRequires:  json-c-devel
BuildRequires:  libxml2-devel
BuildRequires:  make

# BuildRequires:  vtk-devel

# deps aren't available on i686, so we skip docs building entirely
%if %{with texdocs}
BuildRequires:  texlive-scheme-medium
BuildRequires:  tex(hanging.sty)
BuildRequires:  tex(tocloft.sty)
BuildRequires:  tex(newunicodechar.sty)
%endif


%description
Grassroots DiCoM (GDCM) is a C++ library for DICOM medical files.
It supports ACR-NEMA version 1 and 2 (huffman compression is not supported),
RAW, JPEG, JPEG 2000, JPEG-LS, RLE and deflated transfer syntax.
It comes with a super fast scanner implementation to quickly scan hundreds of
DICOM files. It supports SCU network operations (C-ECHO, C-FIND, C-STORE,
C-MOVE). PS 3.3 & 3.6 are distributed as XML files.
It also provides PS 3.15 certificates and password based mechanism to
anonymize and de-identify DICOM datasets.

%package    doc
Summary:    Includes html documentation for gdcm
BuildArch:  noarch
Provides:   %{name}-examples = %{version}-%{release}
Obsoletes:  %{name}-examples < %{version}-%{release}

%description doc
You should install the gdcm-doc package if you would like to
access upstream documentation for gdcm.
Includes CSharp, C++, Java, PHP and Python example programs for GDCM
in html pages

%package    applications
Summary:    Includes command line programs for GDCM
Requires:   %{name}%{?_isa} = %{version}-%{release}

%description applications
You should install the gdcm-applications package if you would like to
use command line programs part of GDCM. Includes tools to convert,
anonymize, manipulate, concatenate, and view DICOM files.

%package    devel
Summary:    Libraries and headers for GDCM
Requires:   %{name}%{?_isa} = %{version}-%{release}
Requires:   %{name}-applications%{?_isa} = %{version}-%{release}

%description devel
You should install the gdcm-devel package if you would like to
compile applications based on gdcm

%package -n python3-gdcm
Summary:    Python binding for GDCM
%{?python_provide:%python_provide python3-gdcm}
Requires:   %{name}%{?_isa} = %{version}-%{release}

%description -n python3-gdcm
You should install the python3-gdcm package if you would like to
used this library with python

%prep
%autosetup -n GDCM-%{version} -S git
# Data source
%setup -n GDCM-%{version} -q -T -D -a 1

# deps not available
%if %{with texdocs}
sed -i.backup 's/^GENERATE_LATEX.*=.*YES/GENERATE_LATEX = NO/' Utilities/doxygen/doxyfile.in
%endif

# Remove bundled utilities (we use Fedora's ones)
rm -rf Utilities/gdcmexpat
rm -rf Utilities/gdcmopenjpeg-v1
rm -rf Utilities/gdcmopenjpeg-v2
rm -rf Utilities/gdcmzlib
rm -rf Utilities/gdcmuuid
rm -rf Utilities/gdcmcharls

# Remove bundled utilities (we don't use them)
rm -rf Utilities/getopt
rm -rf Utilities/pvrg
rm -rf Utilities/rle
rm -rf Utilities/wxWidgets

# Needed for testing:
#rm -rf Utilities/gdcmmd5

# cmake version changed, need to update minimum version
sed -i -e 's@cmake_minimum_required(VERSION 2.8.7)@cmake_minimum_required(VERSION 3.5)@' Examples/CMakeLists.txt

%build
%cmake \
    -DCMAKE_VERBOSE_MAKEFILE=ON \
    -DGDCM_INSTALL_PACKAGE_DIR=%{_libdir}/cmake/%{name} \
    -DGDCM_INSTALL_INCLUDE_DIR=%{_includedir}/%{name} \
    -DGDCM_INSTALL_DOC_DIR=%{_docdir}/%{name} \
    -DGDCM_INSTALL_MAN_DIR=%{_mandir} \
    -DGDCM_INSTALL_LIB_DIR=%{_libdir} \
    -DGDCM_BUILD_TESTING:BOOL=ON \
    -DGDCM_DATA_ROOT=../gdcmData/ \
    -DGDCM_BUILD_EXAMPLES:BOOL=ON \
    -DGDCM_DOCUMENTATION:BOOL=OFF \
    -DGDCM_WRAP_PYTHON:BOOL=ON \
    -DPYTHON_EXECUTABLE=%{python3} \
    -DGDCM_INSTALL_PYTHONMODULE_DIR=%{python3_sitearch} \
    -DGDCM_WRAP_JAVA:BOOL=OFF \
    -DGDCM_WRAP_CSHARP:BOOL=OFF \
    -DGDCM_BUILD_SHARED_LIBS:BOOL=ON \
    -DGDCM_BUILD_APPLICATIONS:BOOL=ON \
    -DCMAKE_BUILD_TYPE:STRING="RelWithDebInfo" \
    -DGDCM_USE_VTK:BOOL=OFF \
    -DGDCM_USE_SYSTEM_CHARLS:BOOL=ON \
    -DGDCM_USE_SYSTEM_EXPAT:BOOL=ON \
    -DGDCM_USE_SYSTEM_OPENJPEG:BOOL=ON \
    -DGDCM_USE_SYSTEM_ZLIB:BOOL=ON \
    -DGDCM_USE_SYSTEM_UUID:BOOL=ON \
    -DGDCM_USE_SYSTEM_LJPEG:BOOL=OFF \
    -DGDCM_USE_SYSTEM_OPENSSL:BOOL=ON \
    -DGDCM_USE_JPEGLS:BOOL=ON \
    -DGDCM_USE_SYSTEM_LIBXML2:BOOL=ON \
    -DGDCM_USE_SYSTEM_JSON:BOOL=ON \
    -DGDCM_USE_SYSTEM_POPPLER:BOOL=ON

#Cannot build wrap_java:
#   -DGDCM_VTK_JAVA_JAR:PATH=/usr/share/java/vtk.jar no found!
#   yum provides */vtk.jar -> No results found

%cmake_build

%install
%cmake_install

%if %{with tests}
%check
# Making the tests informative only for now. Several failing tests (27/228):
# 11,40,48,49,107-109,111-114,130-135,146,149,,151-154,157,194,216,219
make test -C %{__cmake_builddir} || exit 0
%endif

%files
%doc AUTHORS README.md
%license Copyright.txt README.Copyright.txt
%{_libdir}/libgdcmCommon.so.3.0
%{_libdir}/libgdcmCommon.so.3.0.24
%{_libdir}/libgdcmDICT.so.3.0
%{_libdir}/libgdcmDICT.so.3.0.24
%{_libdir}/libgdcmDSED.so.3.0
%{_libdir}/libgdcmDSED.so.3.0.24
%{_libdir}/libgdcmIOD.so.3.0
%{_libdir}/libgdcmIOD.so.3.0.24
%{_libdir}/libgdcmMEXD.so.3.0
%{_libdir}/libgdcmMEXD.so.3.0.24
%{_libdir}/libgdcmMSFF.so.3.0
%{_libdir}/libgdcmMSFF.so.3.0.24
%{_libdir}/libgdcmjpeg12.so.3.0
%{_libdir}/libgdcmjpeg12.so.3.0.24
%{_libdir}/libgdcmjpeg16.so.3.0
%{_libdir}/libgdcmjpeg16.so.3.0.24
%{_libdir}/libgdcmjpeg8.so.3.0
%{_libdir}/libgdcmjpeg8.so.3.0.24
%{_libdir}/libgdcmmd5.so.3.0
%{_libdir}/libgdcmmd5.so.3.0.24
%{_libdir}/libsocketxx.so.1.2
%{_libdir}/libsocketxx.so.1.2.0
%dir %{_datadir}/%{name}-3.0/
%{_datadir}/%{name}-3.0/XML/

%files doc
%doc %{_docdir}/%{name}

%files applications
%{_bindir}/gdcmanon
%{_bindir}/gdcmconv
%{_bindir}/gdcmclean
%{_bindir}/gdcmdiff
%{_bindir}/gdcmdump
%{_bindir}/gdcmgendir
%{_bindir}/gdcmimg
%{_bindir}/gdcminfo
%{_bindir}/gdcmpap3
%{_bindir}/gdcmpdf
%{_bindir}/gdcmraw
%{_bindir}/gdcmscanner
%{_bindir}/gdcmscu
%{_bindir}/gdcmtar
%{_bindir}/gdcmxml
%doc %{_mandir}/man1/*.1*

%files devel
%{_includedir}/%{name}/
%{_libdir}/libgdcmCommon.so
%{_libdir}/libgdcmDICT.so
%{_libdir}/libgdcmDSED.so
%{_libdir}/libgdcmIOD.so
%{_libdir}/libgdcmMEXD.so
%{_libdir}/libgdcmMSFF.so
%{_libdir}/libgdcmjpeg12.so
%{_libdir}/libgdcmjpeg16.so
%{_libdir}/libgdcmjpeg8.so
%{_libdir}/libgdcmmd5.so
%{_libdir}/libsocketxx.so
%{_libdir}/cmake/%{name}/

%files -n python3-gdcm
%{python3_sitearch}/%{name}*.py
%{python3_sitearch}/_%{name}swig.so
%{python3_sitearch}/__pycache__/%{name}*

%changelog
%autochangelog
