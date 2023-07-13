# Doxygen HTML help is not suitable for packaging due to a minified JavaScript
# bundle inserted by Doxygen itself. See discussion at
# https://bugzilla.redhat.com/show_bug.cgi?id=2006555.
#
# We can enable the Doxygen PDF documentation as a substitute.
%bcond doc 1

Name:           libfakekey
Version:        0.3
%global so_version 0
Release:        %autorelease
Summary:        Library for converting characters to X key-presses

License:        LGPL-2.0-or-later
URL:            https://git.yoctoproject.org/cgit/cgit.cgi/libfakekey
Source:         %{url}/snapshot/libfakekey-%{version}.tar.bz2

BuildRequires:  gcc
BuildRequires:  make

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool

BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xtst)

%if %{with doc}
BuildRequires:  doxygen
BuildRequires:  doxygen-latex
%endif

%description
libfakekey is a simple library for converting UTF-8 characters into 'fake' X
key-presses.

%package        devel
Summary:        Development files for libfakekey

Requires:       libfakekey%{?_isa} = %{version}-%{release}
Requires:       pkgconfig(x11)
Requires:       pkgconfig(xtst)

%description    devel
The libfakekey-devel package contains libraries and header files for developing
applications that use libfakekey.


%if %{with doc}
%package doc
Summary:        Documentation for the libfakekey library

BuildArch:      noarch

%description doc
Documentation for the libfakekey library.
%endif


%prep
%autosetup

%if %{with doc}
# We enable the Doxygen PDF documentation as a substitute. We must enable
# GENERATE_LATEX and LATEX_BATCHMODE; the rest are precautionary and should
# already be set as we like them. We also disable GENERATE_HTML, since we will
# not use it.
sed -r -i \
    -e "s/^([[:blank:]]*(GENERATE_LATEX|LATEX_BATCHMODE|USE_PDFLATEX|\
PDF_HYPERLINKS)[[:blank:]]*=[[:blank:]]*)NO[[:blank:]]*/\1YES/" \
    -e "s/^([[:blank:]]*(LATEX_TIMESTAMP|GENERATE_HTML)\
[[:blank:]]*=[[:blank:]]*)YES[[:blank:]]*/\1NO/" \
    doc/Doxyfile.in
%endif


%build
# The tarball generated from the git tag has no configure script, so this is
# mandatory. See autogen.sh (which, however, we do not use because we need to
# use the %%configure macro).
autoreconf -f -i -v
%configure --disable-static %{?with_doc:--enable-doxygen-docs}
%make_build
%if %{with doc}
%make_build -C doc/latex
%endif


%install
%make_install
rm -vf '%{buildroot}%{_libdir}/libfakekey.la'


# The only test is more like a demo; running it is not valuable


%files
%license COPYING
%{_libdir}/libfakekey.so.%{so_version}{,.*}


%files devel
%{_includedir}/fakekey/
%{_libdir}/libfakekey.so
%{_libdir}/pkgconfig/libfakekey.pc


%if %{with doc}
%files doc
%license COPYING
%doc doc/latex/refman.pdf
%endif


%changelog
%autochangelog
