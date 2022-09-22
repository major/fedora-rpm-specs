# Force out of source build
%undefine __cmake_in_source_build
#%%global prerelease _beta2
# TODO:
# Python Module

Name:           alembic
Version:        1.8.3
Release:        4%{?prerelease}%{?dist}
Summary:        Open framework for storing and sharing scene data
License:        BSD
URL:            http://alembic.io/

Source0:        https://github.com/%{name}/%{name}/archive/%{version}%{?prerelease}.tar.gz#/%{name}-%{version}%{?prerelease}.tar.gz

# Use patch from Gentoo fixing iblmbase root path
# https://gitweb.gentoo.org/repo/gentoo.git/tree/media-gfx/alembic/files/alembic-1.7.11-0002-Find-IlmBase-by-setting-a-proper-ILMBASE_ROOT-value.patch?id=953b3b21db55df987dd8006dcdec19e945294d98
Patch0:         alembic-1.7.11-0002-Find-IlmBase-by-setting-a-proper-ILMBASE_ROOT-value.patch 
BuildRequires:  boost-devel
BuildRequires:  cmake >= 3.13
BuildRequires:	gcc-c++
BuildRequires:  hdf5-devel

# Per https://github.com/alembic/alembic/blob/master/README.txt
# alembic actually needs ilmbase, not OpenEXR.
# As of OpenEXR 3.x Imath is now a standalone library.
%if 0%{?fedora} > 34
BuildRequires:  cmake(Imath)
%else
BuildRequires:  pkgconfig(IlmBase)
%endif
BuildRequires:  pkgconfig(zlib)

%description
Alembic is an open computer graphics interchange framework. Alembic distills
complex, animated scenes into a non-procedural, application-independent set of
baked geometric results. This 'distillation' of scenes into baked geometry is
exactly analogous to the distillation of lighting and rendering scenes into
rendered image data.

%package        libs
Summary:        Core Alembic libraries

%description    libs
Alembic is an open computer graphics interchange framework. Alembic distills
complex, animated scenes into a non-procedural, application-independent set of
baked geometric results. This 'distillation' of scenes into baked geometry is
exactly analogous to the distillation of lighting and rendering scenes into
rendered image data.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       cmake%{?_isa}

%description    devel
The %{name}-devel package contains libraries and header files for developing
applications that use %{name}.

%prep
%autosetup -p1 -n %{name}-%{version}%{?prerelease}

sed -i -e 's/ConfigPackageLocation lib/ConfigPackageLocation %{_lib}/g' \
    lib/Alembic/CMakeLists.txt

iconv -f iso8859-1 -t utf-8 ACKNOWLEDGEMENTS.txt > ACKNOWLEDGEMENTS.txt.conv && \
    mv -f ACKNOWLEDGEMENTS.txt.conv ACKNOWLEDGEMENTS.txt

%build
export CXXFLAGS="%{optflags} -Wl,--as-needed"
%cmake %{?_cmake_skip_rpath} \
    -DALEMBIC_LIB_INSTALL_DIR=%{_libdir} \
    -DALEMBIC_SHARED_LIBS=ON \
    -DCMAKE_CXX_STANDARD=17 \
    -DUSE_BINARIES=ON \
    -DUSE_HDF5=ON \
    -DUSE_EXAMPLES=ON \
    -DUSE_PYALEMBIC=OFF \
    -DUSE_STATIC_BOOST=OFF \
    -DUSE_STATIC_HDF5=OFF \
    -DUSE_TESTS=ON

%cmake_build

%install
%cmake_install

%files
%{_bindir}/abcconvert
%{_bindir}/abcdiff
%{_bindir}/abcecho
%{_bindir}/abcechobounds
%{_bindir}/abcls
%{_bindir}/abcstitcher
%{_bindir}/abctree

%files libs
%license LICENSE.txt
%doc ACKNOWLEDGEMENTS.txt FEEDBACK.txt NEWS.txt README.txt
%{_libdir}/libAlembic.so.*

%files devel
%{_includedir}/Alembic
%{_libdir}/cmake/Alembic
%{_libdir}/libAlembic.so

%changelog
* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Sun Nov 21 2021 Orion Poplawski <orion@nwra.com> - 1.8.3-2
- Rebuild for hdf5 1.12.1

* Sun Sep 12 2021 Luya Tshimbalanga <luya@fedoraproject.org> - 1.8.3-1
- Update to 1.8.3

* Sat Aug 21 2021 Richard Shaw <hobbes1069@gmail.com> - 1.8.2-1.4
- Rebuild for OpenEXR/Imath 3.1.

* Tue Aug 10 2021 Orion Poplawski <orion@nwra.com> - 1.8.2-1.3
- Rebuild for hdf5 1.10.7

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.2-1.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jul 07 2021 Richard Shaw <hobbes1069@gmail.com> - 1.8.2-1.1
- Rebuild with standalone imath package. As of OpenEXR 3.x imath is a separate
  package.

* Fri Jun 11 2021 Luya Tshimbalanga <luya@fedoraproject.org> - 1.8.2-1
- Update to 1.8.2
- Resolves rhbz#1969862

* Sun May 16 2021 Luya Tshimbalanga <luya@fedoraproject.org> - 1.8.1-1
- Update to 1.8.1
- Resolves rhbz#1946083

* Wed Apr 7 2021 Luya Tshimbalanga <luya@fedoraproject.org> - 1.8.0-0.1_beta2
- Update to 1.8.0_beta2
- Resolves: #1946083

* Mon Jan 25 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.16-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sun Jan 24 2021 Luya Tshimbalanga <luya@fedoraproject.org> - 1.7.16-3
- Rebuild for hdf5 and libImath

* Fri Jan 01 2021 Richard Shaw <hobbes1069@gmail.com> - 1.7.16-2
- Rebuild for OpenEXR 2.5.3.

* Mon Oct 26 2020 Luya Tshimbalanga <luya@fedoraproject.org> - 1.7.16-1
- Update to 1.7.16 (#1856031)

* Sun Sep 13 2020 Luya Tshimbalanga <luya@fedoraproject.org> - 1.7.15-1
- Update to 1.7.15 (#1856031)

* Fri Jul 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.13-3
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.13-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 13 2020 Luya Tshimbalanga <luya@fedoraproject.org> - 1.7.13-1
- Update to 1.7.13 (#1856031)	

* Thu Jun 25 2020 Orion Poplawski <orion@cora.nwra.com> - 1.7.12-3
- Rebuild for hdf5 1.10.6

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.12-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Oct 26 2019 Luya Tshimbalanga <luya@fedoraproject.org> - 1.7.12-1
- Update to 1.7.12
- Patch from Gentoo addressing ilbmbase root detection
- Drop ldconfig scriptlets

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat May 18 2019 Luya Tshimbalanga <luya@fedoraproject.org> - 1.7.11-1
- Update to 1.7.11

* Thu Apr 11 2019 Richard Shaw <hobbes1069@gmail.com> - 1.7.8-4
- Rebuild for Ilmbase 2.3.0.

* Sat Mar 16 2019 Orion Poplawski <orion@nwra.com> - 1.7.8-3
- Rebuild for hdf5 1.10.5

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Jul 17 2018 Simone Caronni <negativo17@gmail.com> - 1.7.8-1
- Update to 1.7.8.

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Mar 27 2018 Luya Tshimbalanga <luya@fedoraproject.org> - 1.7.7-1
- Update to 1.7.7

* Sat Mar 24 2018 Luya Tshimbalanga <luya@fedoraproject.org> - 1.7.6-1
- Update to 1.7.6

* Sun Mar 04 2018 Luya Tshimbalanga <luya@fedoraproject.org> - 1.7.5-3
- Added gcc-c++ dependency for BuildRequires

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Dec 25 2017 Luya Tshimbalanga <luya@fedoraproject.org> - 1.7.5-1
- Update to 1.7.5.

* Sat Oct 28 2017 Luya Tshimbalanga <luya@fedoraproject.org> - 1.7.4-1
- Update to 1.7.4.

* Mon Sep 11 2017 Simone Caronni <negativo17@gmail.com> - 1.7.3-1
- Update to 1.7.3.

* Sun Aug 06 2017 Björn Esser <besser82@fedoraproject.org> - 1.7.2-4
- Rebuilt for AutoReq cmake-filesystem

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Jul 23 2017 Simone Caronni <negativo17@gmail.com> - 1.7.2-1
- Update to 1.7.2.

* Tue May 09 2017 Simone Caronni <negativo17@gmail.com> - 1.7.1-3
- Link to hdf5 libraries, fixes undefined references on some architectures.

* Sat May 06 2017 Simone Caronni <negativo17@gmail.com> - 1.7.1-2
- Review fixes.

* Mon Apr 24 2017 Simone Caronni <negativo17@gmail.com> - 1.7.1-1
- First build.
