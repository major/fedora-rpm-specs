%global _find_debuginfo_opts --keep-section .rackboot

Name:           racket
Version:        9.1
Release:        %autorelease
Summary:        General purpose programming language

# see LICENSE.txt
License:        MIT AND Apache-2.0
URL:            https://racket-lang.org
Source0:        https://download.racket-lang.org/installers/%{version}/%{name}-%{version}-src.tgz
# https://github.com/racket/racket/issues/5460
Patch0:         racket-configure-c99.patch
# https://bugzilla.redhat.com/show_bug.cgi?id=2339005
ExcludeArch:    ppc64le s390x

# To compile the program
BuildRequires:  gcc
BuildRequires:  libtool
BuildRequires:  make

# To fix rpath issue with executables.
BuildRequires:  chrpath

# Racket heavily utilizes the system ffi library.
BuildRequires:  libffi-devel

# For the racket/gui library (via libffi)
# https://github.com/racket/gui/blob/master/gui-lib/mred/private/wx/gtk/gtk3.rkt
BuildRequires:  gtk3

# For the racket/draw library (via libffi)
# https://github.com/racket/draw/blob/master/draw-lib/racket/draw/unsafe/cairo-lib.rkt
BuildRequires:  cairo
# https://github.com/racket/draw/blob/master/draw-lib/racket/draw/unsafe/pango.rkt
BuildRequires:  pango
# https://github.com/racket/draw/blob/master/draw-lib/racket/draw/unsafe/png.rkt
BuildRequires:  libpng
# https://github.com/racket/draw/blob/master/draw-lib/racket/draw/unsafe/jpeg.rkt
BuildRequires:  libjpeg-turbo
# https://github.com/racket/draw/blob/master/draw-lib/racket/draw/unsafe/glib.rkt
BuildRequires:  glib2

# To validate desktop file
BuildRequires:  desktop-file-utils

BuildRequires:  git

# Require the subpackages
Requires:       racket-minimal%{?_isa} = %{version}-%{release}
Requires:       racket-pkgs = %{version}-%{release}
Recommends:     racket-doc = %{version}-%{release}

%description
Racket is a general-purpose programming language as well as
the world's first ecosystem for developing and deploying new
languages. Make your dream language, or use one of the dozens
already available.

# Equivalent to upstream's minimal-racket release
%package        minimal
Summary:        A minimal Racket installation
Requires:       racket-collects = %{version}-%{release}
%description    minimal
Racket's core runtime

%package        collects
Summary:        Racket's core collections libraries
BuildArch:      noarch
%description    collects
Libraries providing Racket's core functionality

# Arch independent source and bytecode files
%package        pkgs
Summary:        Racket package collections
# See BuildRequires section for details on dependencies
Requires:       gtk3
Requires:       cairo
Requires:       pango
Requires:       libpng
Requires:       glib2
Requires:       libjpeg-turbo
Requires:       racket-minimal = %{version}-%{release}
BuildArch:      noarch
%description    pkgs
Additional packages and libraries for Racket

# Development headers and links
%package        devel
Summary:        Development files for Racket
Requires:       racket-minimal%{?_isa} = %{version}-%{release}
%description    devel
Files needed to link against Racket.

# HTML documentation
%package        doc
Summary:        Documentation files for Racket
BuildArch:      noarch
%description    doc
A local installation of the Racket documentation system.

%prep
%autosetup -p2

# Remove bundled libffi
rm -r src/bc/foreign/libffi

%build
cd src

%configure \
        --enable-pthread \
        --enable-shared \
        --enable-libffi \
        --disable-libs \
%ifarch ppc64le s390x
        --enable-pb \
%endif
%ifarch ppc64le
        --enable-mach=tpb64l \
%endif
%ifarch s390x
        --enable-mach=tpb64b \
%endif
        --enable-lt="%{_bindir}/libtool" \
        --disable-strip

%make_build

%install
%make_install -C src

# Delete mred binaries and replace them with links.
rm %{buildroot}%{_bindir}/mred
rm %{buildroot}%{_bindir}/mred-text
ln -s gracket %{buildroot}%{_bindir}/mred
ln -s gracket-text %{buildroot}%{_bindir}/mred-text

# Fix the rpath error.
chrpath --delete %{buildroot}%{_bindir}/racket
chrpath --delete %{buildroot}%{_libdir}/racket/gracket

# Fix paths in the desktop files.
sed -i "s#%{buildroot}##g" %{buildroot}/%{_datadir}/applications/*.desktop

# Validate desktop files
desktop-file-validate %{buildroot}/%{_datadir}/applications/*.desktop

# Fix buildroot references in html docs
for i in $(find %{buildroot}/%{_datadir}/doc/racket/ -name '*.html'); do
  sed -i "s#%{buildroot}##g" $i
done

# Remove the executable bit on legacy template file
chmod -x %{buildroot}%{_libdir}/racket/starter-sh

# disable check-buildroot
# (see https://github.com/racket/racket/issues/3878 discussion)
%undefine __arch_install_post

%check
%{buildroot}%{_bindir}/%{name} --version

%ldconfig_scriptlets

%files
%license src/LICENSE*.txt
%{_bindir}/drracket
%{_bindir}/gracket
%{_bindir}/gracket-text
%{_bindir}/mred
%{_bindir}/mred-text
%{_bindir}/mzc
%{_bindir}/mzpp
%{_bindir}/mzscheme
%{_bindir}/mztext
%{_bindir}/pdf-slatex
%{_bindir}/plt-games
%{_bindir}/plt-help
%{_bindir}/plt-r5rs
%{_bindir}/plt-r6rs
%{_bindir}/plt-web-server
%{_bindir}/scribble
%{_bindir}/setup-plt
%{_bindir}/slatex
%{_bindir}/slideshow
%{_bindir}/swindle
%{_datadir}/applications/

%files collects
%license src/LICENSE*.txt
%{_datadir}/racket/collects

%files minimal
%license src/LICENSE*.txt
%{_bindir}/racket
%{_bindir}/raco
%{_libdir}/racket
%dir %{_datadir}/racket/
%{_datadir}/racket/links.rktd
%{_datadir}/racket/pkgs/racket-lib
%{_datadir}/man/man1/racket*
%{_datadir}/man/man1/raco*
%dir %{_sysconfdir}/racket/
%config %{_sysconfdir}/racket/config.rktd

%files pkgs
%license src/LICENSE*.txt
%{_datadir}/racket
%{_datadir}/man/man1/drracket*
%{_datadir}/man/man1/gracket*
%{_datadir}/man/man1/mred*
%{_datadir}/man/man1/mzc*
%{_datadir}/man/man1/mzscheme*
%{_datadir}/man/man1/plt-help*
%{_datadir}/man/man1/setup-plt*
%exclude %{_datadir}/racket/links.rktd
%exclude %dir %{_datadir}/racket/pkgs/racket-lib
%exclude %dir %{_datadir}/racket/collects

%files devel
%license src/LICENSE-*.txt
%{_includedir}/racket

%files doc
%license src/LICENSE*.txt
%{_datadir}/doc/racket

%changelog
%autochangelog
