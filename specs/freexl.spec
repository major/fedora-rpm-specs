# Doxygen HTML help is not suitable for packaging due to a minified JavaScript
# bundle inserted by Doxygen itself. See discussion at
# https://bugzilla.redhat.com/show_bug.cgi?id=2006555.
#
# We can enable the Doxygen PDF documentation as a substitute.
%bcond doc_pdf 1

%bcond autoreconf 1

# Not (yet) in EPEL10:
# mingw{32,64}-{expat,libcharset,minizip}
%bcond mingw %{undefined el10}

Name:           freexl
Version:        2.0.0
%global so_version 1
Release:        %autorelease
Summary:        Library to extract data from within an Excel spreadsheet

# The entire source is triply-licensed as (MPL-1.1 OR GPL-2.0-or-later OR
# LGPL-2.1-or-later), except for some build-system files that do not contribute
# to the license of the binary RPMs:
#   - aclocal.m4, m4/ltoptions.m4, m4/ltsugar.m4, m4/ltversion.m4, and
#     m4/lt~obsolete.m4 are FSFULLR
#   - compile, config.guess, config.sub, depcomp, ltmain.sh, missing, and
#     test-driver are GPL-2.0-or-later
#   - configure is FSFUL, or, more likely,
#     (FSFUL AND (MPL-1.1 OR GPL-2.0-or-later OR LGPL-2.1-or-later))
#   - install-sh is X11
#   - m4/libtool.m4 is (FSFULLR AND GPL-2.0-or-later)
License:        MPL-1.1 OR GPL-2.0-or-later OR LGPL-2.1-or-later
URL:            https://www.gaia-gis.it/fossil/freexl/index
Source:         https://www.gaia-gis.it/gaia-sins/freexl-%{version}.tar.gz

# Fix incompatible pointer type in the mingw32 build
#
# Freexl calls iconv with incompatible pointer type in mingw32 builds
# https://www.gaia-gis.it/fossil/freexl/tktview/79f730a917ae90257a88acb974490daf115c2192
Patch:          freexl-2.0.0-iconv-mingw32.patch

%if %{with autoreconf}
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
%endif

BuildRequires:  expat-devel
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  minizip-ng-compat-devel

%if %{with mingw}
BuildRequires:  mingw32-filesystem
BuildRequires:  mingw32-gcc
BuildRequires:  mingw32-expat
BuildRequires:  mingw32-libcharset
BuildRequires:  mingw32-minizip
BuildRequires:  mingw32-win-iconv

BuildRequires:  mingw64-filesystem
BuildRequires:  mingw64-gcc
BuildRequires:  mingw64-expat
BuildRequires:  mingw64-libcharset
BuildRequires:  mingw64-minizip
BuildRequires:  mingw64-win-iconv
%endif

%description
FreeXL is a library to extract valid data from within spreadsheets.

Design goals:
  • to be simple and lightweight
  • to be stable, robust and efficient
  • to be easily and universally portable
  • completely ignoring any GUI-related oddity


%package doc
Summary:        Documentation and examples for FreeXL
BuildArch:      noarch
%if %{with doc_pdf}
BuildRequires:  doxygen
BuildRequires:  doxygen-latex
%endif

%description doc
%{summary}.


%package devel
Summary:  Development Libraries for FreeXL
Requires: freexl%{?_isa} = %{version}-%{release}

%description devel
The freexl-devel package contains libraries and header files for
developing applications that use freexl.


%if %{with mingw}
%package -n mingw32-%{name}
Summary:       MinGW Windows freexl library
BuildArch:     noarch

%description -n mingw32-%{name}
MinGW Windows freexl library.


%package -n mingw64-%{name}
Summary:       MinGW Windows freexl library
BuildArch:     noarch

%description -n mingw64-%{name}
MinGW Windows freexl library.


%{?mingw_debug_package}
%endif


%prep
%autosetup -p1

# We want to install a “clean” version of the examples
mkdir -p clean
cp -rp examples clean/
# Automake files don’t work without a configure.ac; don’t bother installing
# them.
rm -vf clean/examples/Makefile.*

%if %{with doc_pdf}
# We enable the Doxygen PDF documentation as a substitute. We must enable
# GENERATE_LATEX and LATEX_BATCHMODE; the rest are precautionary and should
# already be set as we like them. We also disable GENERATE_HTML, since we will
# not use it.
sed -r -i \
    -e "s/^([[:blank:]]*(GENERATE_LATEX|LATEX_BATCHMODE|USE_PDFLATEX|\
PDF_HYPERLINKS)[[:blank:]]*=[[:blank:]]*)NO[[:blank:]]*/\1YES/" \
    -e "s/^([[:blank:]]*(LATEX_TIMESTAMP|GENERATE_HTML)\
[[:blank:]]*=[[:blank:]]*)YES[[:blank:]]*/\1NO/" \
    Doxyfile.in
%endif

# Prepare native build dir with testdata
mkdir build_native
cp -a tests build_native


%conf
%if %{with autoreconf}
autoreconf --force --install --verbose
%endif

pushd build_native
%global _configure ../configure
%configure --disable-static
popd

%if %{with mingw}
%mingw_configure --disable-static
%endif


%build
pushd build_native
%make_build
%if %{with doc_pdf}
doxygen Doxyfile
%make_build -C latex
mv latex/refman.pdf latex/FreeXL.pdf
%endif
popd

%if %{with mingw}
%mingw_make_build
%endif


%install
%make_install -C build_native

%if %{with mingw}
%mingw_make_install
%mingw_debug_install_post
%endif


%check
%make_build -C build_native check


%files
%license COPYING
%{_libdir}/libfreexl.so.%{so_version}{,.*}


%files devel
%{_includedir}/freexl.h
%{_libdir}/libfreexl.so
%{_libdir}/pkgconfig/freexl.pc


%files doc
%license COPYING
%doc AUTHORS
%doc README
%doc clean/examples/
%if %{with doc_pdf}
%doc build_native/latex/FreeXL.pdf
%endif


%if %{with mingw}
%files -n mingw32-%{name}
%license COPYING
%{mingw32_bindir}/libfreexl-1.dll
%{mingw32_includedir}/freexl.h
%{mingw32_libdir}/libfreexl.dll.a
%{mingw32_libdir}/pkgconfig/freexl.pc


%files -n mingw64-%{name}
%license COPYING
%{mingw64_bindir}/libfreexl-1.dll
%{mingw64_includedir}/freexl.h
%{mingw64_libdir}/libfreexl.dll.a
%{mingw64_libdir}/pkgconfig/freexl.pc
%endif


%changelog
%autochangelog
