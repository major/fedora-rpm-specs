%bcond gui 1

Name:           OpenCTM
Version:        1.0.3
# https://docs.fedoraproject.org/en-US/packaging-guidelines/#_downstream_so_name_versioning
# Please consider versioning the shared library
# https://github.com/Danny02/OpenCTM/issues/16
%global downstream_so_version 1
%global so_version 0.%{downstream_so_version}
Release:        %autorelease
Summary:        Software supporting a file format for compression of 3D triangle meshes

License:        Zlib
URL:            https://github.com/Danny02/OpenCTM
# Note that the last release was on SourceForge, 
#   %%global forgeurl https://sourceforge.net/projects/openctm
#   Source:         %%{forgeurl}/files/OpenCTM-%%{version}/OpenCTM-%%{version}-src.tar.bz2
# but some later development was on GitHub, and any post-release snapshot would
# come from there:
#   Source:         %%{url}/archive/%%{commit}/OpenCTM-%%{commit}.tar.gz
# This package is intended as a dependency for a python-openctm package based
# on https://pypi.org/project/openctm/. The bundled version there is based on
# the latest commit from https://github.com/Danny02/OpenCTM,
# 91b3b71009ade4b036570526327a7e547fe43cbf. However, the Python extension does
# not appear to actually require any of the changes since the 1.0.3 release, so
# we stick with that for now. We can always use a post-release snapshot *if
# necessary*.
#
# Even though we are packaging the release, we still use the GitHub archive
# because it has the original documentation sources, and the SourceForge
# release archive only has the “rendered” documentation. We don’t use a
# snapshot information field in the Version because we believe this commit
# corresponds exactly to the release (although there are no tags on GitHub).
%global commit e2e588db50a1d2a6b63f668f703bf899e0daf8ee
Source:        %{url}/archive/%{commit}/OpenCTM-%{commit}.tar.gz

# Make the Makefile.linux build system flexible enough for distribution packaging
# https://github.com/Danny02/OpenCTM/pull/19
# Rebased on the 1.0.3 release (mostly whitespace differences)
Patch:          OpenCTM-1.0.3-Makefile.linux-distro.patch

# Fix possible double-free of temporary indices buffer in compressMG1.c
# https://github.com/Danny02/OpenCTM/pull/17
Patch:          %{url}/pull/17.patch

# Update to the current release of rply, 1.1.4
# https://github.com/Danny02/OpenCTM/pull/18
Patch:          %{url}/pull/18.patch

# Add a .desktop file and SVG icon
# https://github.com/Danny02/OpenCTM/pull/20
Patch:          %{url}/pull/20.patch

# Fix out-of-bounds access when exporting an empty mesh to CTM (fix #21)
# https://github.com/Danny02/OpenCTM/pull/22
#   Fixes:
# The CTM export routine for ctmconv can access out of bounds
# https://github.com/Danny02/OpenCTM/issues/21
#   Rebased on 1.0.3
Patch:          0001-Fix-out-of-bounds-access-when-exporting-an-empty-mes.patch

# Make TrimString() safe for empty strings (fix #23)
# https://github.com/Danny02/OpenCTM/pull/24
#   Fixes:
# The OFF import routine for ctmconv can access out of bounds
# https://github.com/Danny02/OpenCTM/issues/23
Patch:          %{url}/pull/24.patch

# Adapt viewer to libepoxy instead of GLEW
#
# Actually upstreaming this would require some additional build-system work
# (and upstream is inactive anyway), but the source patch was offered upstream
# as part of:
#
# Please consider migrating away from GLEW
# https://github.com/Danny02/OpenCTM/issues/26
Patch:          0001-Adapt-viewer-to-libepoxy-instead-of-GLEW.patch

BuildRequires:  dos2unix

BuildRequires:  make
BuildRequires:  gcc-c++

# Needed for both ctmconv and ctmviewer:
# The command-line tool is called directly, so we depend on it explicitly.
BuildRequires:  /usr/bin/pkgconf
# Unbundled:
BuildRequires:  rply-devel
BuildRequires:  pkgconfig(tinyxml)

%if %{with gui}
# Needed only for ctmviewer:
BuildRequires:  desktop-file-utils
BuildRequires:  pkgconfig(glut)
BuildRequires:  pkgconfig(gtk+-2.0)
# See: “Fixed a linker error under Ubuntu 10.04.”
# https://github.com/Danny02/OpenCTM/commit/83ac60ebeaeb9b9ee86b7646a9ad5d4034898465
BuildRequires:  pkgconfig(gl)
BuildRequires:  pkgconfig(glu)
# Unbundled (epoxy replaces bundled glew):
BuildRequires:  pnglite-devel
BuildRequires:  pkgconfig(epoxy)
BuildRequires:  pkgconfig(libjpeg)
BuildRequires:  pkgconfig(zlib)
%endif

Requires:       OpenCTM-cli%{?_isa} = %{version}-%{release}
%if %{with gui}
Requires:       OpenCTM-viewer%{?_isa} = %{version}-%{release}
%endif

%global common_description %{expand:
OpenCTM is a file format, a software library and a tool set for compression of
3D triangle meshes. The geometry is compressed to a fraction of comparable file
formats (3DS, STL, COLLADA, VRML...), and the format is easily accessible
through a simple, portable API.}

%description %{common_description}

This package installs all command-line and GUI tools for OpenCTM.
%if %{without gui}

(No GUI tools are currently packaged.)
%endif


%package cli
Summary:        OpenCTM command-line tools

Requires:       OpenCTM-libs%{?_isa} = %{version}-%{release}

%description cli %{common_description}

The OpenCTM-cli package contains command-line tools for the OpenCTM file
format: specifically, the ctmconv conversion utility.


%if %{with gui}
%package viewer
Summary:        OpenCTM Viewer desktop application

Requires:       OpenCTM-libs%{?_isa} = %{version}-%{release}
Requires:       hicolor-icon-theme

%description viewer %{common_description}

The OpenCTM-viewer package contains the OpenCTM Viewer desktop application.
%endif


%package libs
Summary:        Libraries for OpenCTM
# The contents of lib/liblzma/ are LicenseRef-Fedora-Public-Domain.
License:        Zlib AND LicenseRef-Fedora-Public-Domain

# Contents of lib/liblzma/ are forked from Igor Pavlov’s liblzma, version 4.65;
# current versions of the liblzma shared library are distributed in the xz-libs
# package, so we use that for the virtual Provides.
#
# The changes in the fork are minimal: mostly, the lowest compression level was
# tweaked for lower memory usage in
# https://github.com/Danny02/OpenCTM/commit/917bdece68a90363c52a24cb8ae921d72c0381c1.
Provides:       bundled(xz-libs) = 4.65

%description libs %{common_description}

The OpenCTM-libs package contains OpenCTM libraries.


%package devel
Summary:        Development files for OpenCTM
Requires:       OpenCTM-libs%{?_isa} = %{version}-%{release}

%description devel %{common_description}

The OpenCTM-devel package contains libraries and header files for
developing applications that use OpenCTM.


%package doc
Summary:        Development files for OpenCTM

BuildArch:      noarch

BuildRequires:  doxygen
BuildRequires:  doxygen-latex
BuildRequires:  groff

%description doc %{common_description}

The OpenCTM-doc package contains documentation for OpenCTM.


%prep
%autosetup -p1 -n OpenCTM-%{commit}
dos2unix --keepdate *.txt
# README.txt has mixed CRLF, CR, LF line terminators. It takes two passes with
# dos2unix to clean it up completely. See:
# https://github.com/Danny02/OpenCTM/commit/f7bbad425b691f1b42e9518da3f7fb04280a65f9
# https://github.com/Danny02/OpenCTM/commit/17eae7b929f8f0bcaf2d7dfa76f82a5ce2f1aeb9
dos2unix --keepdate README.txt

# Use the system copies of a number of dependencies that are bundled upstream.

# Provides: bundled(pkgconfig(glew))
# License was BSD-3-Clause AND MIT
rm -rvf tools/glew
# Provides: bundled(pkgconfig(libjpeg))
# License was BSD-3-Clause AND MIT
rm -rvf tools/jpeg
# Provides: bundled(pnglite)
# License was Zlib
rm -rvf tools/pnglite
# Provides: bundled(rply) = 1.01 (1.1.4 after patch)
# License was MIT
rm -rvf tools/rply
# Provides: bundled(pkgconfig(tinyxml)) = 2.5.3
# License was Zlib
rm -rvf tools/tinyxml
# Provides: bundled(pkgconfig(zlib)) = 1.2.3
# License was Zlib
rm -rvf tools/zlib

# Upstream already generates a couple of PDFs with LaTeX. We generate the API
# documentation as a PDF too (instead of HTML) in order to avoid issues with
# bundled and precompiled JavaScript, fonts, CSS, and so on.  We must enable
# GENERATE_LATEX and LATEX_BATCHMODE; the rest are precautionary and should
# already be set as we like them. We also disable GENERATE_HTML, since we will
# not use it.
sed -r -i \
    -e "s/^([[:blank:]]*(GENERATE_LATEX|LATEX_BATCHMODE|USE_PDFLATEX|\
PDF_HYPERLINKS)[[:blank:]]*=[[:blank:]]*)NO[[:blank:]]*/\1YES/" \
    -e "s/^([[:blank:]]*(LATEX_TIMESTAMP|GENERATE_HTML)\
[[:blank:]]*=[[:blank:]]*)YES[[:blank:]]*/\1NO/" \
    doc/Doxyfile

%if %{without gui}
# Remove commands pertaining to ctmviewer from the install target
sed -r -i 's/\$\(CP\) .*ctmviewer/# &/' Makefile.linux
%endif


%build
# For EPEL9 and older (redundant in Fedora):
%set_build_flags

# Upstream defaults (after patching):
# CFLAGS = -O3 -W -Wall -fPIC -std=c99 -pedantic
# We omit the optimization flags and supply the distro flags per
# https://docs.fedoraproject.org/en-US/packaging-guidelines/#_compiler_flags.
CFLAGS="-W -Wall -fPIC -std=c99 -pedantic ${CFLAGS}"
%make_build -C lib -f Makefile.linux \
    ABI_VERSION='%{so_version}' \
    CC="${CC-gcc}" \
    CFLAGS="${CFLAGS}" \
    LDFLAGS="${LDFLAGS}"

CXXFLAGS_INCLUDE="-I../lib"
CXXFLAGS_INCLUDE="${CXXFLAGS_INCLUDE} -Itinyxml"
%if %{with gui}
CXXFLAGS_INCLUDE="${CXXFLAGS_INCLUDE} $(pkgconf --cflags 'gtk+-2.0')"
%endif
# Unbundled:
CXXFLAGS_INCLUDE="${CXXFLAGS_INCLUDE} -I%{_includedir}/rply"
%if %{with gui}
CXXFLAGS_INCLUDE="${CXXFLAGS_INCLUDE} $(pkgconf --cflags 'gtk+-2.0')"
CXXFLAGS_INCLUDE="${CXXFLAGS_INCLUDE} $(pkgconf --cflags zlib)"
CXXFLAGS_INCLUDE="${CXXFLAGS_INCLUDE} $(pkgconf --cflags epoxy)"
# CXXFLAGS_INCLUDE="${CXXFLAGS_INCLUDE} -Ipnglite"
CXXFLAGS_INCLUDE="${CXXFLAGS_INCLUDE} $(pkgconf --cflags libjpeg)"
CXXFLAGS_INCLUDE="${CXXFLAGS_INCLUDE} $(pkgconf --cflags tinyxml)"
%endif

CTMCONVLIBS='-lopenctm'
# Unbundled:
CTMCONVLIBS="${CTMCONVLIBS} -lrply"
CTMCONVLIBS="${CTMCONVLIBS} $(pkgconf --libs tinyxml)"

%if %{with gui}
CTMVIEWERLIBS='-lopenctm'
CTMVIEWERLIBS="${CTMVIEWERLIBS} $(pkgconf --libs glut)"
CTMVIEWERLIBS="${CTMVIEWERLIBS} $(pkgconf --libs 'gtk+-2.0')"
# See: “Fixed a linker error under Ubuntu 10.04.”
# https://github.com/Danny02/OpenCTM/commit/83ac60ebeaeb9b9ee86b7646a9ad5d4034898465
CTMVIEWERLIBS="${CTMVIEWERLIBS} $(pkgconf --libs glu)"
CTMVIEWERLIBS="${CTMVIEWERLIBS} $(pkgconf --libs gl)"
# Unbundled:
CTMVIEWERLIBS="${CTMVIEWERLIBS} -lrply"
CTMVIEWERLIBS="${CTMVIEWERLIBS} $(pkgconf --libs zlib)"
CTMVIEWERLIBS="${CTMVIEWERLIBS} -lpnglite"
CTMVIEWERLIBS="${CTMVIEWERLIBS} $(pkgconf --libs epoxy)"
CTMVIEWERLIBS="${CTMVIEWERLIBS} $(pkgconf --libs libjpeg)"
CTMVIEWERLIBS="${CTMVIEWERLIBS} $(pkgconf --libs tinyxml)"
%endif

# Build ctmconv and ctmviewer, but don’t bother with the benchmark tool
# ctmbench.
%make_build -C tools -f Makefile.linux \
    CPP=${CXX-g++} \
    CPPFLAGS="-W -Wall ${CXXFLAGS} -fPIE" \
    CPPFLAGS_INCLUDE="${CXXFLAGS_INCLUDE}" \
    LDFLAGS="${LDFLAGS} -fPIE" \
    CTMCONVLDFLAGS='-L../lib' \
    CTMCONVLIBS="${CTMCONVLIBS}" \
%if %{with gui}
    CTMVIEWERLDFLAGS='-L../lib' \
    CTMVIEWERLIBS="${CTMVIEWERLIBS}" \
%endif
    CTMBENCHLDFLAGS='-L../lib' \
    CTMBENCHLIBS='-lopenctm' \
    GLEWOBJS='' \
    PNGLITEOBJS='' \
    RPLYOBJS='' \
    JPEGSTATIC='' \
    TINYXMLSTATIC='' \
    ZLIBSTATIC='' \
    ctmconv %{?with_gui:ctmviewer}

# Build the non-Doxygen documentation. Note that the all target would include
# APIReference/index.html, but we don’t want to generate the HTML version of
# the Doxygen API docs.
%make_build -C doc -f Makefile.linux \
    DevelopersManual.pdf \
    FormatSpecification.pdf \
%if %{with gui}
    ctmviewer.html \
%endif
    ctmconv.html

# Build the Doxygen-generated API docs.
pushd doc
doxygen
popd
%make_build -C doc/latex
mv doc/latex/refman.pdf doc/APIReference.pdf


%install
# CP='cp -p':
#   https://docs.fedoraproject.org/en-US/packaging-guidelines/#_timestamps
%make_install -f Makefile.linux \
    CP='cp -p' \
    DESTDIR='%{buildroot}' \
    LIBDIR='%{_libdir}' \
    INCDIR='%{_includedir}' \
    BINDIR='%{_bindir}' \
    MAN1DIR='%{_mandir}/man1'

%if %{with gui}
desktop-file-install \
    --dir=%{buildroot}/%{_datadir}/applications \
    data/ctmviewer.desktop

install -t '%{buildroot}%{_datadir}/icons/hicolor/scalable/apps/' \
    -D -p -m 0644 data/ctmviewer.svg
%endif


# The base package has no %%files; there is no “OpenCTM” binary RPM


%check
# Upstream does not provide any tests.


%files
# (Metapackage)


%files cli
%{_bindir}/ctmconv
%{_mandir}/man1/ctmconv.1*


%if %{with gui}
%files viewer
%{_bindir}/ctmviewer
%{_mandir}/man1/ctmviewer.1*

%{_datadir}/applications/ctmviewer.desktop
%{_datadir}/icons/hicolor/scalable/apps/ctmviewer.svg
%endif


%files libs
%license LICENSE.txt
%{_libdir}/libopenctm.so.%{so_version}


%files devel
%{_includedir}/openctm{,pp}.h
%{_libdir}/libopenctm.so


%files doc
%license LICENSE.txt
%doc README.txt
%doc doc/DevelopersManual.pdf
%doc doc/FormatSpecification.pdf
%doc doc/APIReference.pdf
%doc doc/ctmconv.html
%if %{with gui}
%doc doc/ctmviewer.html
%endif


%changelog
%autochangelog
