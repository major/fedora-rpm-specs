Name: fitsverify
Version: 4.22
Release: 2%{?dist}
Summary: A FITS File Format-Verification Tool

License: CFITSIO
URL: https://heasarc.gsfc.nasa.gov/docs/software/ftools/fitsverify/
Source0: %{url}/%{name}-%{version}.tar.gz

BuildRequires: gcc
BuildRequires: cfitsio-devel
BuildRequires: pkgconfig

%description
Fitsverify is a computer program that rigorously checks whether a 
FITS (Flexible Image Transport System) data file conforms to the 
requirements defined in Version 3.0 of the FITS Standard document.

%prep
%autosetup 

%build
# No makefile, so it must be compiled manually
SOURCES="ftverify.c fvrf_data.c fvrf_file.c fvrf_head.c fvrf_key.c fvrf_misc.c"
CFITSIO_CFLAGS=`pkg-config --cflags cfitsio`
CFITSIO_LIBS=`pkg-config --libs cfitsio`
$CC $CFLAGS $LDFLAGS -o fitsverify $SOURCES -DSTANDALONE $CFITSIO_CFLAGS $CFITSIO_LIBS

%install
mkdir -p %{buildroot}%{_bindir}
install -m 755 -p fitsverify %{buildroot}%{_bindir}

%files
%doc README
%license License.txt
%{_bindir}/%{name}

%changelog
* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.22-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jan 03 2024 Sergio Pascual <sergiopr@fedoraproject.org> - 4.22-1
- Initial version
