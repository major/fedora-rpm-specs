%global so_version 1
%global apiver 1.0

# “Let mm-common-get copy some files to untracked/”, i.e., replace scripts from
# the tarball with those from mm-common. This is (potentially) required if
# building an autotools-generated tarball with meson, or vice versa.
%bcond maintainer_mode 1

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

Name:           cairomm
Summary:        C++ API for the cairo graphics library
Version:        1.14.5
Release:        %autorelease

URL:            https://www.cairographics.org
License:        LGPL-2.0-or-later

%global src_base https://www.cairographics.org/releases
Source0:        %{src_base}/cairomm-%{version}.tar.xz
# No keyring with authorized GPG signing keys is published
# (https://gitlab.freedesktop.org/freedesktop/freedesktop/-/issues/331), but we
# are able to verify the signature using the key for Kjell Ahlstedt from
# https://gitlab.freedesktop.org/freedesktop/freedesktop/-/issues/290.
Source1:        %{src_base}/cairomm-%{version}.tar.xz.asc
Source2:        https://gitlab.freedesktop.org/freedesktop/freedesktop/uploads/0ac64e9582659f70a719d59fb02cd037/gpg_key.pub

BuildRequires:  gnupg2

BuildRequires:  gcc-c++
BuildRequires:  meson

BuildRequires:  pkgconfig(cairo)
BuildRequires:  pkgconfig(sigc++-2.0)
BuildRequires:  pkgconfig(fontconfig)

# Everything mentioned in data/cairomm*.pc.in, except the Quartz and Win32
# libraries that do not apply to this platform:
BuildRequires:  pkgconfig(cairo-ft)
BuildRequires:  pkgconfig(cairo-pdf)
BuildRequires:  pkgconfig(cairo-png)
BuildRequires:  pkgconfig(cairo-ps)
BuildRequires:  pkgconfig(cairo-svg)
BuildRequires:  pkgconfig(cairo-xlib)
BuildRequires:  pkgconfig(cairo-xlib-xrender)

%if %{with maintainer_mode}
# mm-common-get
BuildRequires:  mm-common >= 1.0.4
%endif

BuildRequires:  doxygen
# dot
BuildRequires:  graphviz
# xsltproc
BuildRequires:  libxslt
BuildRequires:  pkgconfig(mm-common-libstdc++)
%if %{with doc_pdf}
BuildRequires:  doxygen-latex
BuildRequires:  make
%endif

# For tests:
BuildRequires:  boost-devel

# Based on discussion in
# https://src.fedoraproject.org/rpms/pangomm/pull-request/2, cairomm will
# continue to provide API/ABI version 1.0 indefinitely, with the cairomm1.16
# package providing the new 1.16 API/ABI series. This virtual Provides is
# therefore no longer required, as dependent packages requiring the 1.0 API/ABI
# may safely require cairomm and its subpackages.
Provides:       cairomm%{apiver}%{?_isa} = %{version}-%{release}

%description
This library provides a C++ interface to cairo.

The API/ABI version series is %{apiver}.


%package        devel
Summary:        Development files for cairomm
Requires:       cairomm%{?_isa} = %{version}-%{release}

Provides:       cairomm%{apiver}-devel%{?_isa} = %{version}-%{release}

%description    devel
The cairomm-devel package contains libraries and header files for developing
applications that use cairomm.

The API/ABI version series is %{apiver}.


%package        doc
Summary:        Documentation for cairomm

BuildArch:      noarch

Provides:       cairomm%{apiver}-doc = %{version}-%{release}

%description    doc
Documentation for cairomm can be viewed through the devhelp documentation
browser.

The API/ABI version series is %{apiver}.


%prep
%{gpgverify} \
    --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'

%autosetup
# Fix stray executable bit:
chmod -v a-x NEWS

# We must remove the jQuery/jQueryUI bundle with precompiled/minified/bundled
# JavaScript that is in untracked/docs/reference/html/jquery.js, since such
# sources are banned in Fedora. (Note also that the bundled JavaScript had a
# different license.) We also remove the tag file, which triggers a rebuild of
# the documentation. While we are at it, we might as well rebuild the devhelp
# XML too. Note that we will still install the HTML documentation, since the
# devhelp XML requires it, but we will strip out the JavaScript, which will
# degrade the documentation in a web browser.
rm -rf untracked/docs/reference/html
rm untracked/docs/reference/cairomm-%{apiver}.tag \
   untracked/docs/reference/cairomm-%{apiver}.devhelp2
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


%build
%meson \
  -Dmaintainer-mode=%{?with_maintainer_mode:true}%{?!with_maintainer_mode:false} \
  -Dbuild-documentation=true \
  -Dbuild-examples=false \
  -Dbuild-tests=true \
  -Dboost-shared=true \
  -Dwarnings=max
%meson_build

%if %{with doc_pdf}
%make_build -C '%{_vpath_builddir}/docs/reference/latex'
%endif


%install
%meson_install

install -t %{buildroot}%{_docdir}/cairomm-%{apiver} -m 0644 -p \
    ChangeLog NEWS README.md
cp -rp examples %{buildroot}%{_docdir}/cairomm-%{apiver}/

# Strip out bundled and/or pre-minified JavaScript; this degrades the browser
# experience, but the HTML is still usable for devhelp.
find '%{buildroot}%{_docdir}/cairomm-%{apiver}/reference/html' \
    -type f \( -name '*.js' -o -name '*.js.*' \) -print -delete
%if %{with doc_pdf}
install '%{_vpath_builddir}/docs/reference/latex/refman.pdf' -p -m 0644 \
    '%{buildroot}%{_docdir}/cairomm-%{apiver}/reference/cairomm-%{apiver}.pdf'
%endif


%check
%meson_test


%files
%license COPYING
%{_libdir}/libcairomm-%{apiver}.so.%{so_version}{,.*}


%files devel
%{_includedir}/cairomm-%{apiver}/
%{_libdir}/libcairomm-%{apiver}.so
%{_libdir}/pkgconfig/cairomm-%{apiver}.pc
%{_libdir}/pkgconfig/cairomm-*-%{apiver}.pc
%{_libdir}/cairomm-%{apiver}/


%files doc
%license COPYING
# Note: JavaScript has been removed from HTML reference manual, degrading the
# browser experience. It is still needed for Devhelp support.
%doc %{_docdir}/cairomm-%{apiver}/
%doc %{_datadir}/devhelp/


%changelog
%autochangelog
