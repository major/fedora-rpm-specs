Name:           mmg
Version:        5.6.0
Release:        3%{?dist}
Summary:        Surface and volume remeshers

License:        LGPL-3.0-or-later
URL:            https://www.mmgtools.org/
Source0:        https://github.com/MmgTools/mmg/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  doxygen
BuildRequires:  cmake
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  make
BuildRequires:  scotch-devel


%description
mmg is an open source software for bidimensional and tridimensional surface and
volume remeshing. It provides:
- The mmg2d application and library: adaptation and optimization of a
  bidimensional triangulation
- The mmgs application and library: adaptation and optimization of a surface
  triangulation and isovalue discretization
- The mmg3d application and library: adaptation and optimization of a
  tetrahedral mesh and implicit domain meshing
- The mmg library, combining the mmg2d, mmgs and mmg3d libraries.


%package devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

###############################################################################

%package -n mmg2d
Summary:        Surface remesher

%description -n mmg2d
The mmg2d application and library: adaptation and optimization of a
bidimensional triangulation.


%package -n mmg2d-devel
Summary:        Development files for mmg2d
Requires:       mmg2d%{?_isa} = %{version}-%{release}

%description -n mmg2d-devel
The mmg2d-devel package contains libraries and header files for
developing applications that use mmg2d.


%package -n mmg2d-devel-doc
Summary:        Development documentation for mmg2d
BuildArch:      noarch

%description -n mmg2d-devel-doc
The mmg2d-devel-doc package contains the documentation for developing
applications that use mmg2d.

###############################################################################

%package -n mmgs
Summary:        Surface remesher

%description -n mmgs
The mmgs application and library: adaptation and optimization of a surface
triangulation and isovalue discretization.


%package -n mmgs-devel
Summary:        Development files for mmgs
Requires:       mmgs%{?_isa} = %{version}-%{release}

%description -n mmgs-devel
The mmgs-devel package contains libraries and header files for
developing applications that use mmgs.


%package -n mmgs-devel-doc
Summary:        Development documentation for mmgs
BuildArch:      noarch

%description -n mmgs-devel-doc
The mmgs-devel-doc package contains the documentation for developing
applications that use mmgs.

###############################################################################

%package -n mmg3d
Summary:        Volume remesher
Obsoletes:      mmg3d-libs < 5.3.10
Provides:       mmg3d-libs = %{version}-%{release}

%description -n mmg3d
The mmg3d application and library: adaptation and optimization of a
tetrahedral mesh and implicit domain meshing.


%package -n mmg3d-devel
Summary:        Development files for mmg3d
Requires:       mmg3d%{?_isa} = %{version}-%{release}

%description -n mmg3d-devel
The mmg3d-devel package contains libraries and header files for
developing applications that use mmg3d

%package -n mmg3d-devel-doc
Summary:        Development documentation for mmg3d
Requires:       mmg3d%{?_isa} = %{version}-%{release}

%description -n mmg3d-devel-doc
The mmg3d-devel-doc package contains the documentation for developing
applications that use mmg3d

###############################################################################


%prep
%autosetup -p1


%build
LDFLAGS="%{__global_ldflags} -Wl,--as-needed" %cmake \
    -DBUILD_SHARED_LIBS=ON \
    -Dlibmmg2d_so_SOVER=%{mmg2d_sover} \
    -Dlibmmg3d_so_SOVER=%{mmg3d_sover} \
    -Dlibmmgs_so_SOVER=%{mmgs_sover} \
    -Dlibmmg_so_SOVER=%{mmg_sover}

%cmake_build
make doc -C %{__cmake_builddir}


%install
%cmake_install

# Install suffix-less symlinks
ln -s mmg2d_O3 %{buildroot}/%{_bindir}/mmg2d
ln -s mmgs_O3 %{buildroot}/%{_bindir}/mmgs
ln -s mmg3d_O3 %{buildroot}/%{_bindir}/mmg3d

# Install man pages
install -Dpm 0644 doc/man/mmg2d.1.gz %{buildroot}%{_mandir}/man1/mmg2d.1.gz
install -Dpm 0644 doc/man/mmgs.1.gz %{buildroot}%{_mandir}/man1/mmgs.1.gz
install -Dpm 0644 doc/man/mmg3d.1.gz %{buildroot}%{_mandir}/man1/mmg3d.1.gz


%ldconfig_scriptlets
%ldconfig_scriptlets -n mmg2d
%ldconfig_scriptlets -n mmgs
%ldconfig_scriptlets -n mmg3d


%files
%doc AUTHORS README.md
%license LICENSE COPYING COPYING.LESSER
%{_libdir}/libmmg.so.*

%files devel
%dir %{_includedir}/mmg
%{_includedir}/mmg/libmmg.h
%{_includedir}/mmg/libmmgf.h
%{_libdir}/libmmg.so
%{_libdir}/cmake/mmg/

%files -n mmg2d
%doc AUTHORS README.md
%license LICENSE COPYING COPYING.LESSER
%{_bindir}/mmg2d_O3
%{_bindir}/mmg2d
%{_libdir}/libmmg2d.so.*
%{_mandir}/man1/mmg2d.1*

%files -n mmg2d-devel
%dir %{_includedir}/mmg
%{_includedir}/mmg/mmg2d/
%{_libdir}/libmmg2d.so

%files -n mmg2d-devel-doc
%doc %{__cmake_builddir}/doc/mmg2d/html

%files -n mmgs
%doc AUTHORS README.md
%license LICENSE COPYING COPYING.LESSER
%{_bindir}/mmgs_O3
%{_bindir}/mmgs
%{_libdir}/libmmgs.so.*
%{_mandir}/man1/mmgs.1*

%files -n mmgs-devel
%dir %{_includedir}/mmg
%{_includedir}/mmg/mmgs/
%{_libdir}/libmmgs.so

%files -n mmgs-devel-doc
%doc %{__cmake_builddir}/doc/mmgs/html

%files -n mmg3d
%doc AUTHORS README.md
%license LICENSE COPYING COPYING.LESSER
%{_bindir}/mmg3d_O3
%{_bindir}/mmg3d
%{_libdir}/libmmg3d.so.*
%{_mandir}/man1/mmg3d.1*

%files -n mmg3d-devel
%dir %{_includedir}/mmg
%{_includedir}/mmg/mmg3d/
%{_libdir}/libmmg3d.so

%files -n mmg3d-devel-doc
%doc %{__cmake_builddir}/doc/mmg3d/html


%changelog
* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 5.6.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 5.6.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Nov 05 2021 Sandro Mani <manisandro@gmail.com> - 5.6.0-1
- Update to 5.6.0

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 5.5.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 5.5.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Nov 20 2020 Sandro Mani <manisandro@gmail.com> - 5.5.2-1
- Update to 5.5.2

* Mon Oct 19 2020 Sandro Mani <manisandro@gmail.com> - 5.5.1-1
- Update to 5.5.1

* Mon Oct 12 2020 Sandro Mani <manisandro@gmail.com> - 5.5.0-1
- Update to 5.5.0

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 5.4.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Mar 02 2020 Sandro Mani <manisandro@gmail.com> - 5.4.3-1
- Update to 5.4.3

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 5.4.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 5.4.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Jun 28 2019 Sandro Mani <manisandro@gmail.com> - 5.4.1-1
- Update to 5.4.1

* Sat Feb 16 2019 Sandro Mani <manisandro@gmail.com> - 5.4.0-1
- Update to 5.4.0

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 5.3.13-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jan 24 2019 Sandro Mani <manisandro@gmail.com> - 5.3.13-1
- Update to 5.3.13

* Wed Aug 29 2018 Sandro Mani <manisandro@gmail.com> - 5.3.11-1
- Update to 5.3.11

* Thu Jul 19 2018 Sandro Mani <manisandro@gmail.com> - 5.3.10-4
- Rebuild (scotch)

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 5.3.10-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sun Jun 10 2018 Sandro Mani <manisandro@gmail.com> - 5.3.10-2
- Use %%ldconfig_scriptlets
- Move documentation to separate subpackages
- Install man pages

* Fri Jun 08 2018 Sandro Mani <manisandro@gmail.com> - 5.3.10-1
- Initial package
