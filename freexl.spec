# Doxygen HTML help is not suitable for packaging due to a minified JavaScript
# bundle inserted by Doxygen itself. See discussion at
# https://bugzilla.redhat.com/show_bug.cgi?id=2006555.
#
# We can enable the Doxygen PDF documentation as a substitute.
%bcond_without doc_pdf

%bcond_without autoreconf

Name:           freexl
Version:        1.0.6
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
URL:            http://www.gaia-gis.it/FreeXL
Source:         http://www.gaia-gis.it/gaia-sins/freexl-sources/freexl-%{version}.tar.gz

%if %{with autoreconf}
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
%endif

BuildRequires:  gcc
BuildRequires:  make

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


%prep
%autosetup

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


%build
%if %{with autoreconf}
autoreconf --force --install --verbose
%endif
%configure --disable-static
%make_build

%if %{with doc_pdf}
doxygen Doxyfile
%make_build -C latex
mv latex/refman.pdf latex/FreeXL.pdf
%endif


%check
%make_build check


%install
%make_install
# Delete undesired libtool archives
find '%{buildroot}' -type f -name '*.la' -print -delete


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

%doc clean/examples
%if %{with doc_pdf}
%doc latex/FreeXL.pdf
%endif


%changelog
%autochangelog
