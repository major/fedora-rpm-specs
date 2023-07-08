%global apiver 2.4
%global so_version 1

%bcond autoreconf 1

# Doxygen HTML help is not suitable for packaging due to a minified JavaScript
# bundle inserted by Doxygen itself. See discussion at
# https://bugzilla.redhat.com/show_bug.cgi?id=2006555.
#
# We can enable the Doxygen PDF documentation as a substitute.
#
# We still generate the HTML documentation, but strip out all the JavaScript
# that causes policy issues. This degrades it in the browser, but is sufficient
# to keep the Devhelp documentation working.
%bcond doc_pdf 1

Name:           libglademm24
Version:        2.6.7
Release:        %autorelease -b 5
Summary:        C++ wrapper for libglade

# Although the COPYING file contains version 2.1 of the LGPL, the copyright
# statements in the source file headers (e.g. libglade/libglademm.h) read
# “version 2 of the License, or (at your option) any later version”; therefore,
# the entire source is LGPL-2.0-or-later, except the following files, which do
# not contribute to the license of the binary RPMs because they belong to the
# build system, are Windows-specific, or are otherwise not compiled and/or
# installed.
#   • The following are FSFULLR, or since they are derived from the corresponding
#     Makefile.am files, perhaps more properly (LGPL-2.0-or-later AND FSFULLR):
#       - Makefile.in */Makefile.in, */*/Makefile.in, and */*/*/Makefile.in
#   • The following are FSFUL, or since they are derived from the corresponding
#     configure.in file, perhaps more properly (LGPL-2.0-or-later AND FSFUL):
#       - configure
#   • The following are (clearly only) FSFULLR:
#       - aclocal.m4
#   • The following are GPL-2.0-or-later:
#       - scripts/config.guess
#       - scripts/config.sub
#       - scripts/depcomp
#       - scripts/ltmain.sh
#       - scripts/missing
#       - MSVC_Net2005/gendef/gendef.cc
#   • The following are GPL-2.0-only:
#       - examples/derived/deriveddialog.cc
#       - examples/derived/deriveddialog.h
#       - examples/derived/main.cc
#       - examples/variablesmap/examplewindow.cc
#       - examples/variablesmap/examplewindow.h
#       - examples/variablesmap/main.cc
#   • The following are X11:
#       - scripts/install-sh
License:        LGPL-2.0-or-later
URL:            https://www.gtkmm.org/
Source:         https://ftp.gnome.org/pub/GNOME/sources/libglademm/2.6/libglademm-%{version}.tar.bz2

BuildRequires:  gcc-c++
BuildRequires:  make
BuildRequires:  m4

%if %{with autoreconf}
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
%endif

BuildRequires:  gtkmm24-devel >= 2.6.0
BuildRequires:  libglade2-devel >= 2.6.1

BuildRequires:  doxygen
# dot
BuildRequires:  graphviz
# xsltproc
BuildRequires:  libxslt
%if %{with doc_pdf}
BuildRequires:  doxygen-latex
%endif

%description
This package provides a C++ interface for libglademm. It is a
subpackage of the GTKmm project.  The interface provides a convenient
interface for C++ programmers to create Gnome GUIs with GTK+'s
flexible object-oriented framework.


%package devel
Summary:        Headers for developing programs that will use libglademm
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
This package contains the headers that programmers will need to develop
applications which will use libglademm, part of GTKmm, the C++ interface to the
GTK+.


%package        doc
Summary:        Documentation for %{name}
BuildArch:      noarch

%description    doc
Documentation for %{name}.


%prep
%setup -q -n libglademm-%{version}

%if %{with autoreconf}
# - AC_PROG_LIBTOOL is obsolete
# - Need some help finding m4 macros
# - Drop obsolete and unavailable GLIBMM_CHECK_PERL macro
#   (https://mail.gnome.org/archives/commits-list/2009-September/msg01850.html)
sed -r -i \
    -e 's/AC_PROG_LIBTOOL/LT_INIT/' \
    -e 's/(AC_CONFIG_)AUX(_DIR\(.*\))/\1AUX\2\n\1MACRO\2/' \
    -e 's/(GLIBMM_CHECK_PERL)/dnl \1/' \
    configure.in
%endif

# Remove pre-built Doxygen output
pushd docs/reference
rm -rvf html xml libglademm_doxygen_tags libglademm-2.4.devhelp
popd
# Note that we will still install the HTML documentation, since the devhelp XML
# requires it, but we will strip out the JavaScript, which will degrade the
# documentation in a web browser.
%if %{with doc_pdf}
# We enable the Doxygen PDF documentation as a substitute. We must
# enable GENERATE_LATEX and LATEX_BATCHMODE; the rest are precautionary and
# should already be set as we like them.
sed -r -i \
    -e "s/^([[:blank:]]*(GENERATE_LATEX|LATEX_BATCHMODE|USE_PDFLATEX|\
PDF_HYPERLINKS)[[:blank:]]*=[[:blank:]]*)NO[[:blank:]]*/\1YES/" \
    -e "s/^([[:blank:]]*(LATEX_TIMESTAMP)\
[[:blank:]]*=[[:blank:]]*)YES[[:blank:]]*/\1NO/" \
    docs/reference/Doxyfile.in
%endif

# The generated installdox script is a thing of the distant past. So is the
# beautify_docs.pl script.
sed -r -i '/\b(installdox|beautify_docs)\b/d' docs/reference/Makefile.am
# The HTML documetation no longer has .dot files, but it does have an SVG. We
# won’t install it anyway.
sed -r -i 's/\.dot\b/\.svg/g' docs/reference/Makefile.am



%build
%if %{with autoreconf}
AUTOHEADER=/bin/true autoreconf -fiv
%endif
%configure
%make_build

%if %{with doc_pdf}
%make_build -C 'docs/reference/latex'
%endif


%install
%make_install
find %{buildroot} -type f -name '*.la' -print -delete

install -d %{buildroot}%{_pkgdocdir}
install -t %{buildroot}%{_pkgdocdir} -m 0644 \
    AUTHORS ChangeLog NEWS README
# The TODO file is omitted, as it is an empty file.
mv -v %{buildroot}%{_datadir}/doc/gnomemm-*/libglademm-%{apiver}/* \
    %{buildroot}%{_pkgdocdir}/

# Strip out bundled and/or pre-minified JavaScript; this degrades the browser
# experience, but the HTML is still usable for devhelp.
find '%{buildroot}%{_pkgdocdir}/docs/reference/html' \
    -type f \( -name '*.js' -o -name '*.js.*' \) -print -delete
%if %{with doc_pdf}
install 'docs/reference/latex/refman.pdf' -p -m 0644 \
    '%{buildroot}%{_pkgdocdir}/docs/reference/libglademm-%{apiver}.pdf'
%endif

%files
%license COPYING
%{_libdir}/libglademm-%{apiver}.so.%{so_version}{,.*}


%files devel
%{_includedir}/libglademm-%{apiver}
%{_libdir}/libglademm-%{apiver}.so
%{_libdir}/libglademm-%{apiver}/
%{_libdir}/pkgconfig/libglademm-%{apiver}.pc


%files doc
%license COPYING
# Note: JavaScript has been removed from HTML reference manual, degrading the
# browser experience. It is still needed for Devhelp support.
%doc %{_pkgdocdir}/
%doc %{_datadir}/devhelp/


%changelog
%autochangelog
