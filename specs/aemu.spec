%global toolchain clang
%global gitdate 20231031
%global gitversion dd8b929c

Name:       aemu
Version:    0.1.2^%{gitdate}git%{gitversion}
Release:    5%{?dist}

Summary:    Android emulator library
License:    Apache-2.0
URL:        https://android.googlesource.com/platform/hardware/google/aemu

#VCS: https://android.googlesource.com/platform/hardware/google/aemu
# git snapshot.  to recreate, run:
# ./make-git-snapshot.sh `cat commitid`
Source0:    aemu-%{gitdate}.tar.xz
Source1:    make-git-snapshot.sh
Patch0000:  del-cuda.patch
Patch0001:  skip-tests.patch

BuildRequires:  cmake
BuildRequires:  clang
BuildRequires:  gmock-devel
BuildRequires:  gtest-devel
ExcludeArch:    %{ix86} %{power64} s390x


%description
Android developper library for emulators.

%package devel
Summary: AEMU development files
Requires: %{name}%{?_isa} = %{version}-%{release}

%description devel
AEMU development files, used by gfxstream to build against.


%prep
%autosetup -n %{name}-%{gitdate} -p1

%build
%cmake \
       -DAEMU_COMMON_GEN_PKGCONFIG=ON \
       -DAEMU_COMMON_BUILD_CONFIG=gfxstream
%cmake_build

%install
%cmake_install

%check
%cmake \
       -DAEMU_COMMON_BUILD_CONFIG=gfxstream \
       -DENABLE_VKCEREAL_TESTS=ON \
       -DBUILD_SHARED_LIBS=OFF
%cmake_build
%ctest


%files
%doc README.md
%license LICENSE
%{_libdir}/libaemu-*.so.0*

%files devel
%{_includedir}/aemu/
%{_libdir}/libaemu-*.so
%{_libdir}/pkgconfig/*.pc


%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.2^20231031gitdd8b929c-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.2^20231031gitdd8b929c-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.2^20231031gitdd8b929c-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.2^20231031gitdd8b929c-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Tue Sep 12 2023 Marc-André Lureau <marcandre.lureau@redhat.com> - 0.1.2^20231031gitdd8b929c-1
- Initial packaging (rhbz#2241701)
