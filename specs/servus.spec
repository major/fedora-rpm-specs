%global cmake_module_ver 2018.02

%global api_major 6
%global api_minor 0
%global api_patch 0
%global api_version %{api_major}.%{api_minor}.%{api_patch}

Name:          servus
Version:       1.5.2
#%%global version_major %%(ver=%%{version}; echo ${ver%%.*})
#%%global version_minor %%(ver=%%{version}; ver=`echo ${ver#*.}`; echo ${ver%.*})
#%%global version_patch %%(ver=%%{version}; echo ${ver##*.})

# version hardcoded in the macros differs from the package version, upstream bug
%global version_major 1
%global version_minor 6
%global version_patch 0
Release:       14%{?dist}
Summary:       Zeroconf discovery in C++

# RSA license for the MD5 code which is based on the RSA licensed code
# see ACKNOWLEDGEMENTS.txt for details
# Automatically converted from old format: LGPLv3 and RSA - review is highly recommended.
License:       LGPL-3.0-only AND LicenseRef-RSA
URL:           https://github.com/HBPVIS/Servus
Source0:       %{url}/archive/%{version}/%{name}-%{version}.tar.gz
# https://github.com/HBPVIS/Servus/issues/102
Source1:       https://github.com/Eyescale/CMake/archive/refs/tags/%{cmake_module_ver}.tar.gz
# https://github.com/HBPVIS/Servus/issues/106
Source2:       https://www.gnu.org/licenses/gpl-3.0.txt
Source3:       https://www.gnu.org/licenses/lgpl-3.0.txt
# https://github.com/HBPVIS/Servus/issues/107
Source4:       %{name}.desktop
BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: boost-devel
BuildRequires: avahi-devel
BuildRequires: qt5-qtbase-devel
BuildRequires: desktop-file-utils
BuildRequires: sed
Provides:      bundled(eyescale-cmake-common) = %{cmake_module_ver}
# https://github.com/HBPVIS/Servus/pull/100
Patch0:        servus-1.5.2-stdexcept-fix.patch
# https://github.com/HBPVIS/Servus/pull/96
Patch1:        servus-1.5.2-copy-const-fix.patch
# https://github.com/Eyescale/CMake/pull/599
Patch2:        servus-1.5.2-libdir-fix.patch

%description
Servus is a small C++ network utility library that provides a zeroconf API,
URI parsing and UUIDs.

%package devel
Summary:       Development files for servus
Requires:      %{name}%{?_isa} = %{version}-%{release}

%description devel
Development files for servus.

%prep
%setup -q -a 1 -n Servus-%{version}
mv CMake-%{cmake_module_ver}/* CMake/common/
rm -f CMake-%{cmake_module_ver}/.gitignore
rmdir CMake-%{cmake_module_ver}
%autopatch -p1
cp -a %{SOURCE2} COPYING
cp -a %{SOURCE3} COPYING.LESSER

%build
%cmake
%cmake_build

%install
%cmake_install
mkdir -p %{buildroot}%{_datadir}/applications
desktop-file-install \
    --dir=%{buildroot}%{_datadir}/applications \
    %{SOURCE4}

# fix the strange versioning, asked upstream, what's the right version
# in the meantime I am going with the SONAME as the version
pushd %{buildroot}%{_libdir}
for f in libServus.so libServusQt.so;
do
# very simple API check
  [ -f "$f.%{api_major}" ]

  rm -f $f $f.%{api_major}
  mv $f.%{version_major}.%{version_minor}.%{version_patch} $f.%{api_version}
  ln -s $f.%{api_version} $f.%{api_major}
  ln -s $f.%{api_major} $f
done
pushd %{buildroot}%{_datadir}/Servus/CMake
sed -i 's/%{version_major}\.%{version_minor}\.%{version_patch}/%{api_version}/g' \
 ./ServusConfigVersion.cmake ./ServusTargets-debug.cmake
popd

%check
cd %{_vpath_builddir}
make test

%files
%doc AUTHORS.txt LICENSE.txt README.md doc/Changelog.md
# https://github.com/HBPVIS/Servus/issues/103
%license COPYING COPYING.LESSER ACKNOWLEDGEMENTS.txt
%{_bindir}/servusBrowser
%{_libdir}/libServus{,Qt}.so.6*
%{_datadir}/applications/servus.desktop

%files devel
%{_includedir}/%{name}
%{_libdir}/*.so
%{_datadir}/Servus

%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.2-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Aug  7 2024 Miroslav Suchý <msuchy@redhat.com> - 1.5.2-13
- convert license to SPDX

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.2-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.2-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jul 20 2021 Jaroslav Škarvada <jskarvad@redhat.com> - 1.5.2-5
- Fixed version check

* Wed Jul  7 2021 Jaroslav Škarvada <jskarvad@redhat.com> - 1.5.2-4
- Updated according to the review
  Related: rhbz#1972445

* Mon Jul  5 2021 Jaroslav Škarvada <jskarvad@redhat.com> - 1.5.2-3
- Updated according to the review
  Related: rhbz#1972445

* Sun Jun 27 2021 Jaroslav Škarvada <jskarvad@redhat.com> - 1.5.2-2
- Updated according to the review
  Related: rhbz#1972445

* Tue Jun 15 2021 Jaroslav Škarvada <jskarvad@redhat.com> - 1.5.2-1
- Initial version
