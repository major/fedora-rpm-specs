Name:           lmfit
Version:        8.2.2
%global         sover 8
Release:        %autorelease
Summary:        Levenberg-Marquardt least-squares minimization and curve fitting
# software is BSD, documentation is CC-BY
License:        BSD and CC-BY
URL:            https://jugit.fz-juelich.de/mlz/lmfit
Source0:        https://jugit.fz-juelich.de/mlz/lmfit/-/archive/v%{version}/lmfit-v%{version}.tar.bz2
Patch0:         8828e7071ed30dbded893228b1043b040b5cd26e.patch
Patch1:         version.patch

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  %{_bindir}/pod2man
BuildRequires:  %{_bindir}/pod2html

%description
C/C++ library for Levenberg-Marquardt least-squares minimization and curve
fitting

%package devel
Summary: Development files for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}

%description devel
Development files for %{name}.

%prep
%autosetup -p1 -n %{name}-v%{version}
cp -ra demo _demo

# install to libdir
sed -i 's@${destination}/lib@${destination}/%{_lib}@' lib/CMakeLists.txt CMakeLists.txt

# install to mandir
sed -i 's@${CMAKE_INSTALL_PREFIX}/man@%{_mandir}@' man/CMakeLists.txt


%build
%{cmake}
%cmake_build

%install
%cmake_install
rm -rf %{buildroot}%{_mandir}/html %{buildroot}%{_bindir}/* %{buildroot}%{_libdir}/*.la
rm -rf demo
mv -f _demo demo

%check
%ctest

%files
%doc COPYING CHANGELOG
%{_libdir}/lib%{name}.so.%{sover}
%{_libdir}/lib%{name}.so.%{version}

%files devel
%doc demo
%doc %{_datadir}/doc/lmfit/
%{_includedir}/*
%{_libdir}/lib%{name}.so
%{_libdir}/pkgconfig/*
%{_mandir}/man3/*
%{_mandir}/man7/*

%changelog
%autochangelog
