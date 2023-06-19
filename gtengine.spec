%bcond_with debug

Name: gtengine
Summary: Library for computations in mathematics, graphics, image analysis, and physics
Version: 6.6
Release: 1%{?dist}
Epoch: 1
License: Boost
URL: http://www.geometrictools.com
Source0: https://github.com/davideberly/GeometricTools/archive/GTE-version-%{version}/GeometricTools-GTE-version-%{version}.tar.gz

BuildRequires: pkgconfig(gl)
BuildRequires: pkgconfig(xext)
BuildRequires: pkgconfig(x11)
BuildRequires: pkgconfig(libpng)
BuildRequires: pkgconfig(egl)
BuildRequires: glibc-devel
BuildRequires: gcc-c++
BuildRequires: gcc
BuildRequires: cmake
BuildRequires: dos2unix
BuildRequires: libstdc++-devel
BuildRequires: make

%description
A library of source code for computing in the fields of mathematics,
graphics, image analysis, and physics.
The engine is written in C++ 11 and, as such, has portable access
to standard constructs for multithreading programming on cores.
The engine also supports high-performance computing using general
purpose GPU programming (GPGPU).
SIMD code is also available using Intel Streaming SIMD Extensions (SSE).

GTEngine requires OpenGL 4.5.0 (or later).

%package devel
Summary: Development files for %{name}
Requires: %{name}%{?_isa} = 1:%{version}-%{release}
%description devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package samples
Summary: Samples files of %{name}
Requires: %{name}%{?_isa} = 1:%{version}-%{release}
%description samples
This package contains samples files for
testing that use %{name}.

%prep
%autosetup -n GeometricTools-GTE-version-%{version}

# Remove -Werror flags (rhbz#1923590)
find . -type f \( -name "CMakeLists.txt" \) -exec sed -i 's| -Werror||g' '{}' \;

sed -i 's|GTE_VERSION_MINOR 5|GTE_VERSION_MINOR 6|g' -i GTE/CMakeLists.txt

%build
%define __cmake_in_source_build .
pushd GTE
%if %{with debug}
%cmake -DCMAKE_BUILD_TYPE:STRING=Debug -DBUILD_RELEASE_LIB:BOOL=ON -DBUILD_SHARED_LIB:BOOL=ON %_vpath_srcdir
%else
%cmake -DCMAKE_BUILD_TYPE:STRING=Release -DBUILD_RELEASE_LIB:BOOL=ON -DBUILD_SHARED_LIB:BOOL=ON %_vpath_srcdir
%endif
%make_build
popd

pushd GTE/Samples
%if %{with debug}
%cmake -DCMAKE_SKIP_RPATH:BOOL=ON -DCMAKE_SKIP_INSTALL_RPATH:BOOL=ON -DCMAKE_BUILD_TYPE:STRING=Debug \
 -DBUILD_RELEASE_LIB:BOOL=ON -DBUILD_SHARED_LIB:BOOL=ON %_vpath_srcdir
%else
%cmake -DCMAKE_SKIP_RPATH:BOOL=ON -DCMAKE_SKIP_INSTALL_RPATH:BOOL=ON -DCMAKE_BUILD_TYPE:STRING=Release \
 -DBUILD_RELEASE_LIB:BOOL=ON -DBUILD_SHARED_LIB:BOOL=ON %_vpath_srcdir
%endif
%make_build
popd

%install
echo 'Manual installation...'

mkdir -p $RPM_BUILD_ROOT%{_libdir}/pkgconfig
install -pm 755 GTE/lib/ReleaseShared/* $RPM_BUILD_ROOT%{_libdir}/

ln -sf libgtapplications.so.%{version} $RPM_BUILD_ROOT%{_libdir}/libgtapplications.so
ln -sf libgtgraphics.so.%{version} $RPM_BUILD_ROOT%{_libdir}/libgtgraphics.so
ln -sf libgtmathematicsgpu.so.%{version} $RPM_BUILD_ROOT%{_libdir}/libgtmathematicsgpu.so
ln -sf libgtapplications.so.%{version} $RPM_BUILD_ROOT%{_libdir}/libgtapplications.so.6
ln -sf libgtgraphics.so.%{version} $RPM_BUILD_ROOT%{_libdir}/libgtgraphics.so.6
ln -sf libgtmathematicsgpu.so.%{version} $RPM_BUILD_ROOT%{_libdir}/libgtmathematicsgpu.so.6

mkdir -p $RPM_BUILD_ROOT%{_includedir}/GTE
cp -a GTE/Applications $RPM_BUILD_ROOT%{_includedir}/GTE/
cp -a GTE/Graphics $RPM_BUILD_ROOT%{_includedir}/GTE/
cp -a GTE/Mathematics $RPM_BUILD_ROOT%{_includedir}/GTE/
find $RPM_BUILD_ROOT%{_includedir}/GTE -type f -name "*.cpp" -exec rm -f '{}' \;

mkdir -p $RPM_BUILD_ROOT%{_includedir}/GTL
cp -a GTL/Mathematics $RPM_BUILD_ROOT%{_includedir}/GTL/
cp -a GTL/Utility $RPM_BUILD_ROOT%{_includedir}/GTL/
find $RPM_BUILD_ROOT%{_includedir}/GTL -type f -name "*.vcxproj" -exec rm -f '{}' \;
find $RPM_BUILD_ROOT%{_includedir}/GTL -type f -name "*.sln" -exec rm -f '{}' \;

## Install GTL files
mkdir -p $RPM_BUILD_ROOT%{_libexecdir}/%{name}
cp -a GTE/Samples $RPM_BUILD_ROOT%{_libexecdir}/%{name}/

# Remove unused files
find $RPM_BUILD_ROOT%{_libexecdir}/%{name}/Samples -type f -name "*.h" -exec rm -f '{}' \;
find $RPM_BUILD_ROOT%{_libexecdir}/%{name}/Samples -type f -name "*.cpp" -exec rm -f '{}' \;
find $RPM_BUILD_ROOT%{_libexecdir}/%{name}/Samples -type f -name "*.filters" -exec rm -f '{}' \;
find $RPM_BUILD_ROOT%{_libexecdir}/%{name}/Samples -type f -name "*.vcxproj" -exec rm -f '{}' \;
find $RPM_BUILD_ROOT%{_libexecdir}/%{name}/Samples -type f -name "*.csproj" -exec rm -f '{}' \;
find $RPM_BUILD_ROOT%{_libexecdir}/%{name}/Samples -type f -name "*.sln" -exec rm -f '{}' \;
find $RPM_BUILD_ROOT%{_libexecdir}/%{name}/Samples -type f -name "*.gte" -exec rm -f '{}' \;
find $RPM_BUILD_ROOT%{_libexecdir}/%{name}/Samples -type f -name "*.o" -exec rm -f '{}' \;
find $RPM_BUILD_ROOT%{_libexecdir}/%{name}/Samples -type f -name "cmake*" -exec rm -f '{}' \;
find $RPM_BUILD_ROOT%{_libexecdir}/%{name}/Samples -type f -name "CMake*" -exec rm -f '{}' \;
find $RPM_BUILD_ROOT%{_libexecdir}/%{name}/Samples -type f -name "Makefile" -exec rm -f '{}' \;
find $RPM_BUILD_ROOT%{_libexecdir}/%{name}/Samples -type f -name "*.json" -exec rm -f '{}' \;

for i in `find $RPM_BUILD_ROOT%{_libexecdir}/%{name}/Samples -type d -name "CMakeFiles"`; do
 rm -rf $i
done
##

# Edit a pkg-config file
cat > $RPM_BUILD_ROOT%{_libdir}/pkgconfig/gtengine.pc <<EOF
prefix=%{_prefix}
exec_prefix=%{_prefix}
libdir=%{_libdir}
includedir=%{_includedir}

xthreadlib=-lpthread

Name: GTEngine
Description: Library for computations in mathematics, graphics, image analysis, and physics
Version: %{version}
Cflags: -I%{_includedir}/GTE
Libs: -lgtgraphics -lgtmathematicsgpu -lgtapplications
Libs.private: -lpthread
EOF

%files
%license LICENSE
%doc README.md
%{_libdir}/libgt*.so.%{version}
%{_libdir}/libgt*.so.6

%files devel
%{_includedir}/GTE/
%{_includedir}/GTL/
%{_libdir}/libgt*.so
%{_libdir}/pkgconfig/gtengine.pc

%files samples
%doc GTE/*InstallationRelease.pdf GTL/Documentation/GTLUtility.pdf
%{_libexecdir}/%{name}/

%changelog
* Sat Jun 17 2023 Antonio Trande <sagitter@fedoraproject.org> 1:6.6-1
- Release 6.6

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1:6.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1:6.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sun Jul 10 2022 Antonio Trande <sagitter@fedoraproject.org> 1:6.4-1
- Release 6.4

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1:5.12-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Sep 03 2021 Antonio Trande <sagitter@fedoraproject.org> 1:5.12-1
- Release 5.12

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1:5.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon Jun 14 2021 Antonio Trande <sagitter@fedoraproject.org> 1:5.10-1
- Release 5.10

* Wed May 05 2021 Antonio Trande <sagitter@fedoraproject.org> 1:5.9-1
- Release 5.9

* Sun Feb 14 2021 Antonio Trande <sagitter@fedoraproject.org> 1:5.6-1
- Release 5.6
- Remove -Werror flags (rhbz#1923590)

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1:5.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sun Oct 11 2020 Antonio Trande <sagitter@fedoraproject.org> 1:5.1-1
- Release 5.1
- Switch to CMake build method

* Wed Sep 16 2020 Antonio Trande <sagitter@fedoraproject.org> 1:5.0-1
- Release 5.0

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1:4.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jun 12 2020 Antonio Trande <sagitter@fedoraproject.org> 1:4.6-1
- Release 4.6

* Sat Feb 01 2020 Antonio Trande <sagitter@fedoraproject.org> 1:4.5-1
- Release 4.5
- Epoch 1

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.28-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Dec 14 2019 Jeff Law <law@redhat.com> 3.28-3
- Add missing #include for gcc-10

* Tue Sep 17 2019 Gwyn Ciesla <gwync@protonmail.com> - 3.28-2
- Rebuilt for new freeglut

* Thu Sep 05 2019 Antonio Trande <sagitter@fedoraproject.org> 3.28-1
- Release 3.28

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.21-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Feb 19 2019 Antonio Trande <sagitter@fedoraproject.org> 3.21-1
- Release 3.21

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.19-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Dec 13 2018 Antonio Trande <sagitter@fedoraproject.org> 3.19-1
- Release 3.19

* Thu Oct 18 2018 Antonio Trande <sagitter@fedoraproject.org> 3.16-1
- Update to 3.16

* Thu Sep 13 2018 Antonio Trande <sagitter@fedoraproject.org> 3.15-1
- Update to 3.15

* Sun Jul 22 2018 Antonio Trande <sagitter@fedoraproject.org> 3.14-1
- Update to 3.14
- Include EGL support

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.12-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sun May 20 2018 Antonio Trande <sagitter@fedoraproject.org> 3.12-1
- Update to 3.12

* Sat Feb 17 2018 Antonio Trande <sagitter@fedoraproject.org> 3.11-1
- Update to 3.11

* Fri Feb 16 2018 Antonio Trande <sagitter@fedoraproject.org> - 3.10-3
- Use %%ldconfig_scriptlets

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Oct 14 2017 Antonio Trande <sagitter@fedoraproject.org> 3.10-1
- Update to 3.10

* Sun Aug 06 2017 Antonio Trande <sagitter@fedoraproject.org> 3.9-1
- Update to 3.9

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Jun 11 2017 Antonio Trande <sagitter@fedoraproject.org> 3.8-1
- Update to 3.8

* Mon May 15 2017 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_27_Mass_Rebuild

* Tue Feb 07 2017 Antonio Trande <sagitter@fedoraproject.org> 3.7-1
- Update to 3.7

* Sun Feb 05 2017 Antonio Trande <sagitter@fedoraproject.org> 3.6-1
- Update to 3.6

* Sun Dec 25 2016 Antonio Trande <sagitter@fedoraproject.org> 3.5-1
- Update to 3.5

* Tue Nov 15 2016 Antonio Trande <sagitter@fedoraproject.org> 3.4-1
- Update to 3.4

* Sat Oct 01 2016 Antonio Trande <sagitter@fedoraproject.org> 3.3-1
- Update to 3.3

* Thu Jul 07 2016 Antonio Trande <sagitter@fedoraproject.org> 3.2-2
- Make obj directories (strange assembler error)

* Thu Jul 07 2016 Antonio Trande <sagitter@fedoraproject.org> 3.2-1
- Update to 3.2

* Sun Jun 26 2016 Antonio Trande <sagitter@fedoraproject.org> 3.1-1
- Update to 3.1

* Sun May 29 2016 Antonio Trande <sagitter@fedoraproject.org> 2.5-1
- Update to 2.5

* Sat Apr 09 2016 Antonio Trande <sagitter@fedoraproject.org> 2.4-1
- Update to 2.4

* Sat Apr 02 2016 Antonio Trande <sagitter@fedoraproject.org> 2.3-4
- Parallel Make disabled

* Fri Apr 01 2016 Antonio Trande <sagitter@fedoraproject.org> 2.3-3
- Install commands modified

* Fri Apr 01 2016 Antonio Trande <sagitter@fedoraproject.org> 2.3-2
- Renamed as gtengine

* Wed Mar 16 2016 Antonio Trande <sagitter@fedoraproject.org> 2.3-1
- Update to 2.3

* Mon Feb 22 2016 Antonio Trande <sagitter@fedoraproject.org> 2.2-1
- Update to 2.2

* Wed Jan 27 2016 Antonio Trande <sagitter@fedoraproject.org> 2.1-1
- Update to 2.1

* Tue Sep 29 2015 Antonio Trande <sagitter@fedoraproject.org> 2.0-1
- Update to 2.0

* Mon Jun 29 2015 Antonio Trande <sagitter@fedoraproject.org> 1.14-1
- First package
