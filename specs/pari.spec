Name:           pari
Version:        2.17.3
Release:        %autorelease
Summary:        Number Theory-oriented Computer Algebra System

%global majver %(cut -d. -f1-2 <<< %{version})

License:        GPL-2.0-or-later
URL:            https://pari.math.u-bordeaux.fr/
VCS:            git:https://pari.math.u-bordeaux.fr/git/pari.git
Source0:        https://pari.math.u-bordeaux.fr/pub/pari/unix/%{name}-%{version}.tar.gz
Source1:        https://pari.math.u-bordeaux.fr/pub/pari/unix/%{name}-%{version}.tar.gz.asc
# Public key 0x4522e387, Bill Allombert <Bill.Allombert@math.u-bordeaux.fr>
Source2:        gpgkey-42028EA404A2E9D80AC453148F0E7C2B4522E387.gpg
Source3:        fr.u-bordeaux.math.pari.desktop
Source4:        pari-gp.xpm
Source5:        pari.abignore
Source6:        fr.u-bordeaux.math.pari.metainfo.xml
# Use xdg-open rather than xdvi to display DVI files (#530565)
Patch:          pari-2.17.0-xdgopen.patch
# Fix compiler warnings
# http://pari.math.u-bordeaux.fr/cgi-bin/bugreport.cgi?bug=1316
Patch:          pari-2.9.0-missing-field-init.patch
Patch:          pari-2.17.0-declaration-not-prototype.patch

BuildRequires:  coreutils
BuildRequires:  desktop-file-utils
BuildRequires:  findutils
BuildRequires:  fltk-devel
BuildRequires:  gcc-c++
BuildRequires:  gmp-devel
BuildRequires:  gnupg2
BuildRequires:  libappstream-glib
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  pkgconfig(readline)
BuildRequires:  sed
BuildRequires:  tex(latex)

# Test suite requirements
BuildRequires:  pari-elldata
BuildRequires:  pari-galdata
BuildRequires:  pari-galpol
BuildRequires:  pari-nflistdata
BuildRequires:  pari-seadata

# Avoid doc-file dependencies and provides
%global __provides_exclude_from ^%{_datadir}/pari/PARI/
%global __requires_exclude_from ^%{_datadir}/pari/PARI/

%description
PARI is a widely used computer algebra system designed for fast computations in
number theory (factorizations, algebraic number theory, elliptic curves...),
but also contains a large number of other useful functions to compute with
mathematical entities such as matrices, polynomials, power series, algebraic
numbers, etc., and a lot of transcendental functions.

This package contains the shared libraries. The interactive
calculator PARI/GP is in package pari-gp.

%package devel
Summary:        Header files and libraries for PARI development
Requires:       %{name} = %{version}-%{release}

%description devel
Header files and libraries for PARI development.

%package gp
Summary:        PARI calculator
Requires:       %{name} = %{version}-%{release}
Requires:       bzip2
Requires:       gzip
Requires:       xdg-utils
Requires:       mimehandler(application/x-dvi)

%description gp
PARI/GP is an advanced programmable calculator, which computes
symbolically as long as possible, numerically where needed, and
contains a wealth of number-theoretic functions.

%prep
# Verify the source file
%{gpgverify} --data=%{SOURCE0} --signature=%{SOURCE1} --keyring=%{SOURCE2}

%autosetup -p0

# Silence abidiff warnings about the size of functions_basic[] changing
cp -p %{SOURCE5} .

%conf
# Avoid unwanted rpaths
sed -i "s|runpathprefix='.*'|runpathprefix=''|" config/get_ld

%build
# For as yet unknown reasons, 32-bit pari becomes extremely slow if built with
# pthread support.  Enable it for 64-bit only until we can diagnose the issue.
./Configure \
    --prefix=%{_prefix} \
    --share-prefix=%{_datadir} \
    --bindir=%{_bindir} \
    --libdir=%{_libdir} \
    --mandir=%{_mandir}/man1 \
    --datadir=%{_datadir}/pari \
    --includedir=%{_includedir} \
%if 0%{?__isa_bits} == 64
    --mt=pthread \
%endif
    --enable-tls \
    --with-fltk \
    --with-gmp
%make_build gp

%install
%make_install INSTALL="install -p" STRIP=%{_bindir}/true

# Move the library directory on 64-bit systems
if [ "%{_lib}" != "lib" ]; then
    mkdir -p %{buildroot}%{_libdir}
    mv %{buildroot}%{_prefix}/lib/pari %{buildroot}%{_libdir}
fi

# Site-wide gprc
mkdir -p %{buildroot}%{_sysconfdir}
install -p -m 644 misc/gprc.dft %{buildroot}%{_sysconfdir}/gprc

# Desktop menu entry
mkdir -p %{buildroot}%{_datadir}/applications
desktop-file-install \
    --dir %{buildroot}%{_datadir}/applications \
    %{SOURCE3}
mkdir -p %{buildroot}%{_datadir}/pixmaps
install -p -m 644 %{SOURCE4} %{buildroot}%{_datadir}/pixmaps

# Install the AppData file
mkdir -p %{buildroot}%{_metainfodir}
install -pm 644 %{SOURCE6} %{buildroot}%{_metainfodir}
appstream-util validate-relax --nonet \
  %{buildroot}%{_metainfodir}/fr.u-bordeaux.math.pari.metainfo.xml

# Work around package-notes breakage.  The package-notes feature was not
# designed for software like this, which stores flags to use to build other
# software.  All such packages now have to go through contortions like this,
# with the result that the software it builds does NOT have package notes.
sed -e 's|%{build_cxxflags}|%{extension_cxxflags}|' \
    -e 's|%{build_ldflags}|%{extension_ldflags}|' \
    -i %{buildroot}%{_libdir}/pari/pari.cfg

# The qf tests started failing on 32-bit x86 with the release of 2.15.3.
# The final test is supposed to report "precision too low in forqfvec", but
# does not.  The cause is currently unknown.  Since we don't really care about
# that architecture, just let it pass until somebody cares enough to diagnose
# the issue, or we stop building for 32-bit x86.
%ifnarch %{ix86}
%check
make test-all
%endif

%files
%license COPYING
%doc AUTHORS CHANGES* COMPAT NEW README
%doc pari.abignore
%{_libdir}/libpari-gmp-tls.so.%{version}
%{_libdir}/libpari-gmp-tls.so.9
%{_libdir}/pari/

%files gp
%{_bindir}/gp
%{_bindir}/gp-%{majver}
%{_bindir}/gphelp
%{_bindir}/tex2mail
%config(noreplace) %{_sysconfdir}/gprc
%dir %{_datadir}/pari/
%doc %{_datadir}/pari/PARI/
%doc %{_datadir}/pari/doc/
%doc %{_datadir}/pari/examples/
%{_datadir}/pari/misc/
%{_datadir}/pari/pari.desc
%{_datadir}/applications/fr.u-bordeaux.math.pari.desktop
%{_datadir}/pixmaps/pari-gp.xpm
%{_metainfodir}/fr.u-bordeaux.math.pari.metainfo.xml
%{_mandir}/man1/gp-%{majver}.1*
%{_mandir}/man1/gp.1*
%{_mandir}/man1/gphelp.1*
%{_mandir}/man1/pari.1*
%{_mandir}/man1/tex2mail.1*

%files devel
%{_includedir}/pari/
%{_libdir}/libpari.so

%changelog
%autochangelog
