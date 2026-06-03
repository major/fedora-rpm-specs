# Header only library
%global debug_package %{nil}

Name:           crcpp
Version:        1.2.1.0
Release:        %{autorelease}
Summary:        Easy to use and fast C++ CRC library

License:        BSD-3-Clause
URL:            https://github.com/d-bahr/CRCpp
Source0:        %{url}/archive/release-%{version}/CRCpp-release-%{version}.tar.gz

BuildRequires:  cmake
BuildRequires:  doxygen
BuildRequires:  gcc-c++

%description
Tired of writing CRC code over and over again? Don't want to include a dozen
boost header files just for a little bit of functionality? CRC++ is a portable
and extremely lightweight alternative that is incredibly simple, fast, and
clean.

CRC++ supports bit-by-bit and byte-by-byte calculation of full and multipart
CRCs.  The algorithms used are highly optimized and can even be configured
to be branch less (as always, be sure to profile your code to choose the most
efficient option). CRC++ is a great option for embedded C++ projects with a
need for efficiency.

CRC++ consists of a single header file which can be included in any existing
C++ application. No libraries, no boost, no mess, no fuss.

Any CRC width is supported - even CRCs larger than 64 bits, provided there is
an integer type large enough to contain it. Trying to compute a 57-bit CRC?
Got you covered.

Many common CRCs are provided out-of-the-box, such as CRC-32 (used in PKZip and
Ethernet), CRC-XMODEM, and CRC-CCITT.

CRC++ will compile with any reasonably compliant C++03 or C++11 compiler.
Compiling with C++11 is recommended, as it allows a number of static
computations to be performed at compile-time instead of runtime.


%package devel
Summary:  Header file for CRCpp
Provides:  crcpp-static = %{version}-%{release}

%description devel
Header file for CRCpp.

%prep
%autosetup -n CRCpp-release-%{version}
sed -i 's/GENERATE_MAN           = NO/GENERATE_MAN           = YES/g' \
  doxygen/Doxyfile.dox 
sed -i 's/GENERATE_HTML           = YES/GENERATE_HTML           = NO/g' \
  doxygen/Doxyfile.dox 
sed -i 's/GENERATE_LATEX           = NO/GENERATE_LATEX           = NO/g' \
  doxygen/Doxyfile.dox 


%build
%cmake
%cmake_build
pushd doxygen
doxygen Doxyfile.dox
popd

%install
%cmake_install
mkdir -p %{buildroot}%{_mandir}/man3
install -m644 doxygen/man/man3/CRC.3 %{buildroot}%{_mandir}/man3/
install -m644 doxygen/man/man3/CRC.h.3 %{buildroot}%{_mandir}/man3/
install -m644 doxygen/man/man3/CRC_Parameters.3 %{buildroot}%{_mandir}/man3/
install -m644 doxygen/man/man3/CRC_Table.3 %{buildroot}%{_mandir}/man3/

%check
%ctest

%files devel
%license LICENSE
%doc README.md
%{_includedir}/CRC.h
%{_mandir}/man3/CRC.3*
%{_mandir}/man3/CRC.h.3*
%{_mandir}/man3/CRC_Parameters.3*
%{_mandir}/man3/CRC_Table.3*

%changelog
%autochangelog
