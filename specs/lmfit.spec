Name:           lmfit
Version:        10.0
%global         sover 10
Release:        %autorelease
Summary:        Levenberg-Marquardt least-squares minimization and curve fitting
# software is BSD, documentation is CC-BY
# Automatically converted from old format: BSD and CC-BY - review is highly recommended.
License:        LicenseRef-Callaway-BSD AND LicenseRef-Callaway-CC-BY
URL:            https://jugit.fz-juelich.de/mlz/lmfit
Source0:        https://jugit.fz-juelich.de/mlz/lmfit/-/archive/v%{version}/lmfit-v%{version}.tar.bz2

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
sed -i 's@DESTINATION lib@DESTINATION %{_lib}@' lib/CMakeLists.txt CMakeLists.txt

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
%{_libdir}/lib%{name}.so.%{sover}.*

%files devel
%doc demo
%doc %{_datadir}/doc/lmfit/
%{_includedir}/*
%{_libdir}/lib%{name}.so
%{_libdir}/pkgconfig/*
%{_libdir}/cmake/*
%{_mandir}/man3/*
%{_mandir}/man7/*

%changelog
%autochangelog
