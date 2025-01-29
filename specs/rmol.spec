# Build -python subpackage
%bcond_without python

#
Name:           rmol
Version:        1.00.12
Release:        %autorelease

Summary:        C++ library of Revenue Management and Optimisation classes and functions

License:        LGPL-2.1-or-later
URL:            https://github.com/airsim/%{name}
Source0:        %{url}/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  boost-devel
BuildRequires:  pkgconfig(readline)
BuildRequires:  soci-mysql-devel
BuildRequires:  soci-sqlite3-devel
BuildRequires:  pkgconfig(stdair)
BuildRequires:  pkgconfig(airrac)
BuildRequires:  mysql-devel

%description
%{name} is a C++ library of Revenue Management and Optimisation classes 
and functions. Typically, that library may be used by service providers
(e.g., airlines offering flight seats, hotels offering rooms, rental car
companies offering rental days, broadcasting company offering advertisement 
slots, theaters offering seats, etc.) to help in optimizing their revenues
from seat capacities.
Most of the algorithms implemented are public and documented in the
following book:
The Theory and practice of Revenue Management, by Kalyan T. Talluri and
Garrett J. van Ryzin, Kluwer Academic Publishers, 2004, ISBN 1-4020-7701-7

%{name} makes an extensive use of existing open-source libraries for
increased functionality, speed and accuracy. In particular the
Boost (C++ Standard Extensions: https://www.boost.org) library is used.

Install the %{name} package if you need a library of basic C++ objects
for Airline Revenue Management (RM), mainly for simulation purpose.

%package        devel
Summary:        Header files, libraries and development helper tools for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       pkgconfig

%description    devel
This package contains the header files, shared libraries and
development helper tools for %{name}. If you would like to develop
programs using %{name}, you will need to install %{name}-devel.

%package        doc
Summary:        HTML documentation for the %{name} library
BuildArch:      noarch
BuildRequires:  tex(latex)
BuildRequires:  texlive-epstopdf
BuildRequires:  doxygen
BuildRequires:  ghostscript

%description    doc
This package contains HTML pages, as well as a PDF reference manual,
for %{name}. All that documentation is generated thanks to Doxygen
(https://doxygen.org). The content is the same as what can be browsed
online (https://%{name}.net).

%if %{with python}
%package        -n python3-%{name}
Summary:        Python bindings for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  boost-python3-devel
%{?python_provide:%python_provide python3-%{name}}

%description -n python3-%{name}
This package contains Python libraries for %{name}
%endif


%prep
%autosetup

%build
%cmake
%cmake_build

%install
%cmake_install

# Removed the Doxygen installer
rm -f %{buildroot}%{_docdir}/%{name}/html/installdox

# Remove additional documentation files (those files are already available
# in the project top directory)
rm -f %{buildroot}%{_docdir}/%{name}/{NEWS,README.md,AUTHORS}

%check
%ctest

%if %{with python}
%post -n python3-%{name}
ln -s -f %{python3_sitearch}/py%{name}/py%{name} %{_bindir}/py%{name}

%postun -n python3-%{name}
rm -f %{_bindir}/py%{name}
%endif


%files
%doc AUTHORS ChangeLog NEWS README.md
%license COPYING
%{_bindir}/%{name}
%{_bindir}/%{name}_drawBPC
%{_bindir}/%{name}_extractBPC
%{_libdir}/lib%{name}.so.*
%{_mandir}/man1/%{name}.1.*
%{_mandir}/man1/%{name}_drawBPC.1.*
%{_mandir}/man1/%{name}_extractBPC.1.*

%files devel
%{_includedir}/%{name}/
%{_bindir}/%{name}-config
%{_libdir}/lib%{name}.so
%{_libdir}/pkgconfig/%{name}.pc
%{_datadir}/aclocal/%{name}.m4
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/CMake/%{name}-config-version.cmake
%{_datadir}/%{name}/CMake/%{name}-config.cmake
%{_datadir}/%{name}/CMake/%{name}-library-depends.cmake
%{_datadir}/%{name}/CMake/%{name}-library-depends-debug.cmake
%{_mandir}/man1/%{name}-config.1.*
%{_mandir}/man3/%{name}-library.3.*

%files doc
%doc %{_docdir}/%{name}/
%license COPYING

%if %{with python}
%files -n python3-%{name}
%{python3_sitearch}/py%{name}/
%{_mandir}/man1/py%{name}.1.*
%{_datadir}/%{name}/CMake/%{name}-config-python.cmake
%{_datadir}/%{name}/CMake/%{name}-python-library-depends-debug.cmake
%{_datadir}/%{name}/CMake/%{name}-python-library-depends.cmake
%endif

%changelog
%autochangelog

