Name:           calceph
Version:        3.5.1
Release:        2%{?dist}
Summary:        Astronomical library to access planetary ephemeris files

License:        CeCILL or CeCILL-B or CeCILL-C
URL:            https://www.imcce.fr/inpop/calceph
Source0:        https://www.imcce.fr/content/medias/recherche/equipes/asd/%{name}/%{name}-%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  gcc-gfortran
BuildRequires:  make

%description
This library is designed to access the binary planetary ephemeris files,
such INPOPxx, JPL DExxx and SPICE ephemeris files.


%package        libs
Summary:        %{name} shared libraries
License:        CeCILL or CeCILL-B or CeCILL-C

%description    libs
Calceph shared libraries.


%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%package        doc
Summary:        Documentation files for %{name}
BuildArch:      noarch

%description    doc
The %{name}-doc package contains documentation for %{name}.


%package        fortran-devel
Summary:        Development files for using %{name} Fortran bindings
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       %{name}-devel%{?_isa} = %{version}-%{release}
%if 0%{?fedora}
Requires:       gcc-gfortran%{?_isa}
%else
Requires:       gcc-gfortran
%endif

%description    fortran-devel
%{summary}.


%prep
%autosetup

# Remove executable bit set on license files
chmod -x COPYING*


%build
%configure --enable-fortran=yes \
    --enable-python=no \
    --enable-python-package-system=no \
    --enable-python-package-user=no \
    --enable-thread=yes \
    --disable-static \
    --docdir=%{_pkgdocdir}
%make_build


%install
%make_install

# Remove static lib
rm %{buildroot}%{_libdir}/libcalceph.la

# Remove sources for Octave / Mathlib interface
rm -r %{buildroot}%{_libexecdir}

# Remove hidden files from docdir
find %{buildroot}%{_pkgdocdir} -name .buildinfo -exec rm -f {} \;

%if 0%{?epel} && 0%{?epel} < 8
%ldconfig_scriptlets
%endif


%check
make check


%files
%{_bindir}/*


%files      libs
%license COPYING_CECILL_V2.1.LIB COPYING_CECILL_B.LIB COPYING_CECILL_C.LIB
%{_libdir}/*.so.1
%{_libdir}/*.so.1.*


%files      devel
%{_libdir}/*.so
%{_includedir}/*.h


%files      doc
%{_pkgdocdir}


%files      fortran-devel
%{_includedir}/%{name}.mod


%changelog
* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.5.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Mar 02 2022 Mattia Verga <mattia.verga@protonmail.com> - 3.5.1-1
- Update to 3.5.1 (fedora#2059202)

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Sat Aug 28 2021 Mattia Verga <mattia.verga@protonmail.com> - 3.5.0-1
- Update to 3.5.0

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sun Nov 08 2020 Mattia Verga <mattia.verga@protonmail.com> - 3.4.7-2
- Removed hidden files from docdir
- Move Fortran headers to -fortran-devel subpackage

* Fri Nov 6 2020 Mattia Verga <mattia.verga@protonmail.com> - 3.4.7-1
- Update to 3.4.7
- Fix build errors on s390x
- Fix FCFLAGS transmission to fortran compiler
- Enable multi-threading support

* Tue Nov 3 2020 Mattia Verga <mattia.verga@protonmail.com> - 3.4.6-3
- Enable fortran module build

* Sun Nov  1 2020 Mattia Verga <mattia.verga@protonmail.com> - 3.4.6-2
- Split libs subpackage
- Add ldconfig macro for EPEL7 compatibility

* Sun Nov  1 2020 Mattia Verga <mattia.verga@protonmail.com> - 3.4.6-1
- Initial packaging
