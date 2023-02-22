#
Name:           sevmgr
Version:        1.00.7
Release:        4%{?dist}

Summary:        C++ Simulation-Oriented Discrete Event Management Library

License:        LGPLv2+
URL:            https://github.com/airsim/%{name}
Source0:        %{url}/archive/%{name}-%{version}.tar.gz

BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  boost-devel
BuildRequires:  soci-mysql-devel, soci-sqlite3-devel
BuildRequires:  readline-devel
BuildRequires:  stdair-devel


%description
%{name} is a C++ library of discrete event queue management classes and
functions, exclusively targeting simulation purposes.

%{name} makes an extensive use of existing open-source libraries for
increased functionality, speed and accuracy. In particular the
Boost (C++ Standard Extensions: https://www.boost.org) library is used.

Install the %{name} package if you need a library of basic C++ objects
for the discrete event queue management of your simulation project.

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
(http://doxygen.org). The content is the same as what can be browsed
online (http://%{name}.org).


%prep
%autosetup -n %{name}-%{name}-%{version} 


%build
%cmake 
%cmake_build

%install
%cmake_install

# Remove the Doxygen installer
rm -f %{buildroot}%{_docdir}/%{name}/html/installdox

# Remove additional documentation files (those files are already available
# in the project top directory)
rm -f %{buildroot}%{_docdir}/%{name}/{NEWS,README.md,AUTHORS}

%check
#ctest


%files
%doc AUTHORS ChangeLog NEWS README.md
%license COPYING
%{_bindir}/%{name}
%{_bindir}/%{name}_demo
%{_libdir}/lib%{name}.so.*
%{_mandir}/man1/%{name}.1.*
%{_mandir}/man1/%{name}_demo.1.*

%files devel
%{_includedir}/%{name}
%{_bindir}/%{name}-config
%{_libdir}/lib%{name}.so
%{_libdir}/pkgconfig/%{name}.pc
%{_datadir}/aclocal/%{name}.m4
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/CMake
%{_mandir}/man1/%{name}-config.1.*
%{_mandir}/man3/%{name}-library.3.*

%files doc
%doc %{_docdir}/%{name}/html
%license COPYING


%changelog
* Mon Feb 20 2023 Jonathan Wakely <jwakely@redhat.com> - 1.00.7-4
- Rebuilt for Boost 1.81

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.00.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.00.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

%autochangelog
