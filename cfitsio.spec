Name: cfitsio
Version: 4.3.1
Release: %autorelease
Summary: Library for manipulating FITS data files

License: CFITSIO
URL: http://heasarc.gsfc.nasa.gov/fitsio/
Source0: http://heasarc.gsfc.nasa.gov/FTP/software/fitsio/c/cfitsio-%{version}.tar.gz
# Remove soname version check
Patch1: cfitsio-noversioncheck.patch
# Some rearrangements in pkg-config file
Patch2: cfitsio-pkgconfig.patch
# Use builder linker flags
Patch3: cfitsio-ldflags.patch
# Remove rpath
Patch4: cfitsio-remove-rpath.patch

BuildRequires: gcc-gfortran
BuildRequires: make
BuildRequires: zlib-devel
BuildRequires: bzip2-devel
BuildRequires: curl-devel
##BuildRequires: pkgconfig(curl)

%description
CFITSIO is a library of C and FORTRAN subroutines for reading and writing 
data files in FITS (Flexible Image Transport System) data format. CFITSIO 
simplifies the task of writing software that deals with FITS files by 
providing an easy to use set of high-level routines that insulate the 
programmer from the internal complexities of the FITS file format. At the 
same time, CFITSIO provides many advanced features that have made it the 
most widely used FITS file programming interface in the astronomical 
community.

%package devel
Summary: Headers required when building programs against cfitsio
Requires: %{name} = %{version}-%{release}
Requires: pkgconfig

%description devel
Headers required when building a program against the cfitsio library.

%package static
Summary: Static cfitsio library

%description static
Static cfitsio library; avoid use if possible.

%package docs
Summary: Documentation for cfitsio
BuildArch:  noarch

%description docs
Stand-alone documentation for cfitsio.

%package -n fpack
Summary: FITS image compression and decompression utilities
Requires: %{name} = %{version}-%{release}

%description -n fpack
fpack optimally compresses FITS format images and funpack restores them
to the original state.

* Integer format images are losslessly compressed using the Rice
compression algorithm.
    * typically 30% better compression than GZIP
    * about 3 times faster compression speed than GZIP
    * about the same uncompression speed as GUNZIP 

* Floating-point format images are compressed with a lossy algorithm
    * truncates the image pixel noise by a user-specified amount to
      produce much higher compression than by lossless techniques
    * the precision of scientific measurements in the compressed image
      (relative to those in the original image) depends on the selected
       amount of compression

%prep
%autosetup -p1

%build
%configure --enable-reentrant -with-bzip2
make shared
make fpack funpack

%check
make testprog
LD_LIBRARY_PATH=. ./testprog > testprog.lis
cmp -s testprog.lis testprog.out
cmp -s testprog.fit testprog.std

%install
%make_install LIBDIR=%{_libdir} INCLUDEDIR=%{_includedir}/%{name} \
 CFITSIO_LIB=%{buildroot}%{_libdir} \
 CFITSIO_INCLUDE=%{buildroot}%{_includedir}/%{name}
cp -p f{,un}pack %{buildroot}%{_bindir}

chmod 755 %{buildroot}%{_libdir}/libcfitsio.so.*
chmod 755 %{buildroot}%{_bindir}/f{,un}pack


%ldconfig_scriptlets

%files
%doc README License.txt docs/changes.txt
%{_libdir}/libcfitsio.so.10*

%files devel
%doc cookbook.*
%{_includedir}/%{name}
%{_libdir}/libcfitsio.so
%{_libdir}/pkgconfig/cfitsio.pc

%files static
%doc License.txt
%{_libdir}/libcfitsio.a

%files docs
%doc docs/fitsio.doc docs/fitsio.pdf docs/cfitsio.pdf License.txt

%files -n fpack
%doc docs/fpackguide.pdf License.txt
%{_bindir}/fpack
%{_bindir}/funpack

%changelog
%autochangelog
