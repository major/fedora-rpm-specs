#
Name:           airinv
Version:        1.00.12
Release:        %autorelease

Summary:        C++ Simulated Airline Inventory Management System library
License:        LGPL-2.1-or-later
URL:            https://github.com/airsim/%{name}
Source0:        %{url}/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  boost-devel
BuildRequires:  pkgconfig(readline)
BuildRequires:  pkgconfig(libzmq)
BuildRequires:  pkgconfig(cppzmq)
BuildRequires:  soci-devel
BuildRequires:  soci-mysql-devel
BuildRequires:  soci-sqlite3-devel
BuildRequires:  pkgconfig(stdair)
BuildRequires:  pkgconfig(airrac)
BuildRequires:  pkgconfig(rmol)
BuildRequires:  pkgconfig(sevmgr)

%description
%{name} is a C++ library of airline inventory management classes and
functions, mainly targeting simulation purposes.

%{name} makes an extensive use of existing open-source libraries for
increased functionality, speed and accuracy. In particular the
Boost (C++ Standard Extensions: https://www.boost.org) library is used.

Install the %{name} package if you need a library of basic C++ objects
for Airline Inventory Management, mainly for simulation purpose.

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
online (https://github.com/airsim/%{name}).


%prep
%autosetup

%build
%cmake
%cmake_build

%install
%cmake_install

# Remove the Doxygen installer
rm -f %{buildroot}%{_docdir}/%{name}/html/installdox

# Remove additional documentation files (those files are already available
# in the project top directory)
rm -f %{buildroot}%{_docdir}/%{name}/{NEWS,README,AUTHORS}

%check
%ctest


%files
%doc AUTHORS ChangeLog NEWS README.md
%license COPYING
%{_bindir}/%{name}
%{_bindir}/%{name}_parseInventory
%{_bindir}/AirInvClient
%{_bindir}/AirInvServer
%{_libdir}/lib%{name}.so.*
%{_mandir}/man1/%{name}.1.*
%{_mandir}/man1/%{name}_parseInventory.1.*
%{_mandir}/man1/AirInvClient.1.*
%{_mandir}/man1/AirInvServer.1.*

%files devel
%license COPYING
%{_includedir}/%{name}/
%{_bindir}/%{name}-config
%{_libdir}/lib%{name}.so
%{_libdir}/pkgconfig/%{name}.pc
%{_libdir}/cmake/%{name}/
%{_datadir}/aclocal/%{name}.m4
%{_mandir}/man1/%{name}-config.1.*
%{_mandir}/man3/%{name}-library.3.*

%files doc
%doc %{_docdir}/%{name}/
%license COPYING


%changelog
%autochangelog

