%global sover   0.0.0
%global majver  %(cut -d. -f1 <<< %{sover})

Name:           kissat
Version:        3.1.0
Release:        1%{?dist}
Summary:        Keep It Simple SAT solver

License:        MIT
URL:            http://fmv.jku.at/kissat/
Source0:        https://github.com/arminbiere/kissat/archive/rel-%{version}/%{name}-%{version}.tar.gz
# Fedora-only patch: give the shared library an SONAME
Patch0:         %{name}-shared.patch

BuildRequires:  drat-trim-tools
BuildRequires:  gcc
BuildRequires:  glibc-langpack-en
BuildRequires:  help2man
BuildRequires:  make
BuildRequires:  p7zip-plugins
BuildRequires:  xz-lzma-compat

Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

%global _desc %{expand:
KISSAT is a "keep it simple and clean bare metal SAT solver" written in
C.  It is a port of CaDiCaL back to C with improved data structures,
better scheduling of inprocessing and optimized algorithms and
implementation.  Coincidentally 'kissat' also means 'cats' in Finnish.}

%description %_desc

This package contains a command-line interface to KISSAT.

%package libs
Summary:        Keep It Simple SAT solver library

%description libs %_desc

This package contains KISSAT as a library, for use in applications that
need a SAT solver.

%package devel
Summary:        Development files for %{name}
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

%description devel
Library links and header files for developing applications that use
%{name}.

%prep
%autosetup -p1 -n %{name}-rel-%{version}

# Remove handle.c from APPSRC; it defines kissat_signal_name, which is called
# from library code, so handle.c must be in the library as well.
sed -i 's/ handle\.c//' makefile.in

# Set the library soname
sed -i 's/@SOVER@/%{sover}/;s/@MAJVER@/%{majver}/' makefile.in

# Adapt to a drat-trim change
sed -ri '/sqrt|prime/s/false/true/' test/testcnfs.h

%build
# Use Fedora flags by default.  This cannot be done in %%prep.  See
# https://bugzilla.redhat.com/show_bug.cgi?id=2044028
sed -e 's|-W -Wall|%{build_cflags} -fPIC|' \
    -e 's|^\(passtolinker=\)""|\1" %{build_ldflags}"|' \
    -i configure

# This is NOT an autoconf-generated script.  Do NOT use %%configure.
./configure -O2 --test
%make_build

# Make a man page for the command line interface
export LD_LIBRARY_PATH=$PWD/build
help2man --version-string=%{version} -N -o kissat.1 build/kissat

%install
# The makefile has no install target.  Install by hand.
# Install the binary
mkdir -p %{buildroot}%{_bindir}
cp -p build/kissat %{buildroot}%{_bindir}

# Install the library
mkdir -p %{buildroot}%{_libdir}
cp -p build/libkissat.so.%{sover} %{buildroot}%{_libdir}
ln -s libkissat.so.%{sover} %{buildroot}%{_libdir}/libkissat.so.%{majver}
ln -s libkissat.so.%{majver} %{buildroot}%{_libdir}/libkissat.so

# Install the header file
mkdir -p %{buildroot}%{_includedir}
cp -p src/kissat.h %{buildroot}%{_includedir}

# Install the man page
mkdir -p %{buildroot}%{_mandir}/man1
cp -p kissat.1 %{buildroot}%{_mandir}/man1

%check
LD_LIBRARY_PATH=$PWD/build build/tissat

%files
%{_bindir}/kissat
%{_mandir}/man1/kissat.1*

%files libs
%doc README.md
%license LICENSE
%{_libdir}/lib%{name}.so.0*

%files devel
%{_includedir}/%{name}.h
%{_libdir}/lib%{name}.so

%changelog
* Tue Jul 18 2023 Jerry James <loganjerry@gmail.com> - 3.1.0-1
- Version 3.1.0

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jul  6 2022 Jerry James <loganjerry@gmail.com> - 3.0.0-1
- Version 3.0.0

* Fri Jan 28 2022 Jerry James <loganjerry@gmail.com> - 0-0.5.sc2021
- Work around package-notes breakage
- Adapt to a drat-trim change

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.5.sc2021
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.4.sc2021
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Sat Jul 17 2021 Jerry James <loganjerry@gmail.com> - 0-0.3.sc2021
- Version sc2021

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sun Jul 12 2020 Jerry James <loganjerry@gmail.com> - 0-0.1.20200704gitbaef460
- Initial RPM
