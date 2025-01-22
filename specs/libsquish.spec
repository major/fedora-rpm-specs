%global __cmake_in_source_build 1
Name: libsquish
Version: 1.15
Release: 18%{?dist}
URL: https://sourceforge.net/projects/libsquish/
Summary: Open source DXT compression library
License: MIT
Source0: http://download.sourceforge.net/sourceforge/%{name}/%{name}-%{version}.tgz
Patch0:  libsquish-cmake_install.patch
BuildRequires: gcc-c++ cmake
BuildRequires: make

%package devel
Summary: Development files for Open source DXT compression library
Requires: %{name}%{_isa} = %{version}-%{release}

%description
The libSquish library compresses images with the DXT standard
(also known as S3TC). This standard is mainly used by OpenGL and
DirectX for the lossy compression of RGBA textures.

%description devel
The libsquish-devel package contains files needed for developing or compiling
applications which use DXT compression.

%prep
%autosetup -c libsquish-%{version}

%build
%cmake . -DBUILD_SQUISH_WITH_SSE2=OFF
%make_build

%install
%make_install

%ldconfig_scriptlets

%files
%license LICENSE.txt
%doc ChangeLog.txt
%{_libdir}/*.so.0.0

%files devel
%doc README.txt
%{_libdir}/*.so
%{_includedir}/*

%changelog
* Mon Jan 20 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.15-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.15-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.15-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.15-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.15-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Mar 08 2023 Gwyn Ciesla <gwync@protonmail.com> - 1.15-13
- migrated to SPDX license

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.15-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.15-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.15-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.15-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.15-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Aug 04 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.15-7
- Fix FTBFS.

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.15-6
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.15-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.15-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.15-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Apr 22 2019 Gwyn Ciesla <gwync@protonmail.com> - 1.15-2
- Review fixes.

* Mon Apr 22 2019 Gwyn Ciesla <gwync@protonmail.com> - 1.15-1
- Initial package.
