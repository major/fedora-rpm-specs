Name:           dcm2niix
Version:        1.0.20220720
Release:        6%{?dist}
Summary:        DICOM to NIfTI converter

License:        BSD
URL:            http://www.nitrc.org/plugins/mwiki/index.php/dcm2nii:MainPage
Source0:        https://github.com/rordenlab/%{name}/archive/v%{version}/%{name}-v%{version}.tar.gz

# Patch for new yaml-cpp using CMake config files
# https://github.com/rordenlab/dcm2niix/issues/647
Patch0:         dcm2niix-yaml-cpp.patch

BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  nifticlib-devel
BuildRequires:  zlib-devel
BuildRequires:  turbojpeg-devel
BuildRequires:  git
BuildRequires:  yaml-cpp-devel
BuildRequires:  CharLS-devel
BuildRequires:  openjpeg2-devel
BuildRequires:  python3-sphinx

Provides:       %{name}%{?_isa} = %{version}-%{release}

# console/ujpeg.{h,cpp}
# https://github.com/neurolabusc/dcm2niix/issues/8
Provides:       bundled(nanojpeg)

%description
dcm2niix is a tool designed to convert neuroimaging data from the NIfTI format
to the DICOM format.

%prep
%autosetup -p1 -n %{name}-%{version}
# Set executable name
sed -i 's/sphinx-build/sphinx-build-3/' docs/CMakeLists.txt

mkdir build/

%build
%cmake -DUSE_STATIC_RUNTIME=OFF -DUSE_TURBOJPEG=ON -DUSE_OPENJPEG=ON  -DUSE_JPEGLS=ON -DZLIB_IMPLEMENTATION=System -DBATCH_VERSION=ON -DBUILD_DOCS=ON
%cmake_build

%install
%cmake_install

%files
%doc README.md VERSIONS.md
%license license.txt
%{_bindir}/%{name}
%{_bindir}/dcm2niibatch
%{_mandir}/man1/%{name}.1*
%{_mandir}/man1/dcm2niibatch.1*


%changelog
* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.20220720-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.20220720-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.20220720-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.20220720-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Tue Nov 08 2022 Richard Shaw <hobbes1069@gmail.com> - 1.0.20220720-2
- Rebuild for yaml-cpp 0.7.0.

* Sun Aug 07 2022 Alessio <alciregi@fedoraproject.org> - 1.0.20220720-1
- Update to new version

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.20190902-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri May 20 2022 Sandro Mani <manisandro@gmail.com> - 1.0.20190902-8
- Rebuild for gdal-3.5.0 and/or openjpeg-2.5.0

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.20190902-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.20190902-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.20190902-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Aug 22 2020 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 1.0.20190902-4
- Fix FTBFS

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.20190902-3
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.20190902-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sat Feb 01 2020 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 1.0.20190902-1
- Update to new version

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.20180622-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Oct 18 2019 Richard Shaw <hobbes1069@gmail.com> - 1.0.20180622-5
- Rebuild for yaml-cpp 0.6.3.

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.20180622-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.20180622-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Nov 09 2018 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 1.0.20180622-2
- Remove unneeded patch from spec

* Fri Nov 09 2018 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 1.0.20180622-1
- Update to latest upstream release
- Enable multiple file formats
- Generate docs
- Generate batch binary

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.0-0.7.gitebc72ae
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.0-0.6.gitebc72ae
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.0-0.5.gitebc72ae
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.0-0.4.gitebc72ae
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.0-0.3.gitebc72ae
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.0-0.2.gitebc72ae
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sat Dec 05 2015 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 0.0.0-0.1.gitebc72ae
- Initial package
