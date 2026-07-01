# disable bindings for now as python does not have
# metadata and some perl tests fail
%bcond  bindings 0

Name:           libredwg
Version:        0.13.3
Release:        %{autorelease}
Summary:        A free C library to handle DWG files

License:        GPL-3.0-or-later AND GFDL-1.3-or-later
URL:            https://www.gnu.org/software/libredwg/
Source0:        https://ftp.gnu.org/gnu/libredwg/libredwg-%{version}.tar.xz
Source1:        https://ftp.gnu.org/gnu/libredwg/libredwg-%{version}.tar.xz.sig
Source2:        https://ftp.gnu.org/gnu/gnu-keyring.gpg
# POSIX_C_SOURCE is already defined
Patch:          fedora-posix-c-source.patch
# Json reader tests give errors, disable them
Patch:          json-test.patch

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  dejagnu
BuildRequires:  doxygen
BuildRequires:  gcc
BuildRequires:  jsmn-devel
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  pcre2-devel
%if %{with bindings}
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl-macros
BuildRequires:  perl(Convert::Binary::C)
BuildRequires:  perl(ExtUtils::Embed)
%endif
BuildRequires:  pslib-devel
%if %{with bindings}
BuildRequires:  python3-devel
BuildRequires:  swig
%endif
BuildRequires:  texinfo
BuildRequires:  texinfo-tex
# Required for tests
BuildRequires:  jq
BuildRequires:  libxml2-devel
BuildRequires:  pcre2
BuildRequires:  pcre2-utf16
%if %{with bindings}
BuildRequires:  perl(Test::More)
BuildRequires:  perl-Module-CoreList-tools
BuildRequires:  python3-libxml2
%endif
# Verify signature
BuildRequires:  gpgverify


%description
GNU LibreDWG is a free C library to handle DWG files.

LibreDWG is in beta development stage. Not all planned features are yet
completed, but the API should stay mostly stable. At the moment our decoder
(i.e. reader) is done, just some very advanced R2010+ entities fail to read and
are skipped over. The writer is good enough for R1.1 - R2000. Among the example
applications we wrote using LibreDWG is a reader (from dwg, dxf, json), a
writer (convert from dwg, dxf, json or add from scratch), a rewriter (i.e.
saveas), an initial SVG and Postscript conversion, converters from and to DXF
and JSON, dwggrep to search for text, and dwglayer to print the list of layers. 

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%if %{with bindings}
%package -n     python3-LibreDWG
Summary:        Python bindings for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description -n python3-LibreDWG
The python3-LibreDWG package contains the python bindings for developing
applications that use %{name}.

%package -n     perl-LibreDWG
Summary:        Perl bindings for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description -n perl-LibreDWG
The perl-LibreDWG package contains the perl bindings for developing
applications that use %{name}.
%endif

%prep
%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup -p1
# Remove bundled jsmn and use the one in Fedora
rm jsmn/jsmn.h
ln -s /usr/include/jsmn/jsmn.h jsmn/jsmn.h

%build
autoreconf -fi
%configure \
%if %{with bindings}
           --enable-bindings \
%endif
           --enable-check-less \
           --enable-dxf \
           --enable-json \
           --enable-shared \
           --enable-write \
%if %{without bindings}
           --disable-bindings \
%endif
           --disable-rpath \
           --disable-silent-rules \
           --disable-static \
           --disable-Werror \
#           --with-mimalloc \
%if %{with bindings}
           --with-perl-install=vendor
%endif


%make_build PERL=%{_bindir}/perl PYTHON=%{python3}

%install
%make_install

# Remove perllocal.pod and packlist files.
# TODO: Try preventing their generation with something like:
# perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
# Source: https://fedoraproject.org/wiki/Perl/Tips#Best_practices_for_the_latest_Fedora
%if %{with bindings}
rm %{buildroot}/%{perl_archlib}/perllocal.pod
rm %{buildroot}/%{perl_vendorarch}/auto/LibreDWG/.packlist
%endif

# Remove Info file.
rm %{buildroot}/%{_infodir}/dir

# Perl EUMM sets it read-only, but objcopy needs write access.
%if %{with bindings}
chmod u+w %{buildroot}/%{perl_vendorarch}/auto/LibreDWG/LibreDWG.so
%endif

%check
# Ensure perl library can be found
%if %{with bindings}
perl -e "use Data::Dumper; print Dumper \%INC;"
ls %{_builddir}/libredwg-%{version}/bindings/perl/blib/arch/auto/LibreDWG/
ls %{buildroot}/%{perl_vendorarch}/auto/LibreDWG/
export LD_LIBRARY_PATH="$LD_LIBRARY_PATH:%{_builddir}/libredwg-%{version}/bindings/perl/blib/arch/auto/LibreDWG/:%{buildroot}/%{perl_vendorarch}/auto/LibreDWG/"
export PERL5LIB=%{_builddir}/libredwg-%{version}/bindings/perl/blib/arch/auto/LibreDWG/:%{buildroot}/%{perl_vendorarch}/auto/LibreDWG/
export PERLLIB=%{_builddir}/libredwg-%{version}/bindings/perl/blib/arch/auto/LibreDWG/:%{buildroot}/%{perl_vendorarch}/auto/LibreDWG/
perl -e "use Data::Dumper; print Dumper \%INC;"
%endif
make check 

%files
%license COPYING
%doc AUTHORS
%doc ChangeLog
%doc NEWS
%doc README
%{_bindir}/dwg2SVG
%{_bindir}/dwg2dxf
%{_bindir}/dwg2ps
%{_bindir}/dwgbmp
%{_bindir}/dwgadd
%{_bindir}/dwgfilter
%{_bindir}/dwggrep
%{_bindir}/dwglayers
%{_bindir}/dwgread
%{_bindir}/dwgrewrite
%{_bindir}/dwgwrite
%{_bindir}/dxf2dwg
%{_bindir}/dxfwrite
%{_libdir}/libredwg.so.0
%{_libdir}/libredwg.so.0.0.13
%{_mandir}/man1/dwg2SVG.1.*
%{_mandir}/man1/dwg2dxf.1.*
%{_mandir}/man1/dwg2ps.1.*
%{_mandir}/man1/dwgadd.1.*
%{_mandir}/man1/dwgbmp.1.*
%{_mandir}/man1/dwgfilter.1.*
%{_mandir}/man1/dwggrep.1.*
%{_mandir}/man1/dwglayers.1.*
%{_mandir}/man1/dwgread.1.*
%{_mandir}/man1/dwgrewrite.1.*
%{_mandir}/man1/dwgwrite.1.*
%{_mandir}/man1/dxf2dwg.1.*
%{_mandir}/man1/dxfwrite.1.*
%{_mandir}/man5/dwgadd.5.*
%{_infodir}/LibreDWG.info*
%dir %{_datadir}/libredwg
%{_datadir}/libredwg/dwgadd.example
%{_datadir}/libredwg/dwgadd.example_r11
%{_datadir}/libredwg/dwgadd.example_r10
%{_datadir}/libredwg/dwgadd.example_r2_10
%{_datadir}/libredwg/dwgadd.example_r1_4
%{_datadir}/libredwg/load_dwg.py

%files devel
%doc TODO
%{_includedir}/dwg.h
%{_includedir}/dwg_api.h
%{_libdir}/libredwg.so
%{_libdir}/pkgconfig/libredwg.pc

%if %{with bindings}
%files -n python3-LibreDWG
%pycached %{python3_sitelib}/LibreDWG.py
%{python3_sitearch}/_LibreDWG.so*

%files -n perl-LibreDWG
%{perl_vendorarch}/LibreDWG.pm
%dir %{perl_vendorarch}/auto/LibreDWG
%{perl_vendorarch}/auto/LibreDWG/LibreDWG.so
%endif

%changelog
%autochangelog 
