%global debug_package %{nil}

Name: semver
Version: 0.3.0
Release: 7%{?dist}

License: MIT
Summary: Semantic Versioning for modern C++
URL: https://github.com/Neargye/%{name}
Source0: %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

# https://github.com/Neargye/semver/pull/29
Patch100: %{name}-fix-installation.patch

# https://github.com/Neargye/semver/pull/30
Patch101: %{name}-added-missing-slash.patch

BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: ninja-build

# semver currently support only catch v2
%if 0%{?fedora} >= 38 || 0%{?rhel} >= 10
BuildRequires: catch2-devel
%else
BuildRequires: catch-devel
%endif

%description
C++ library compare and manipulate versions are available as extensions to the
<major>.<minor>.<patch>-<prerelease_type>.<prerelease_number> format complying
with Semantic Versioning 2.0.0.

%package devel
Summary: Development files for %{name}
Provides: %{name}-static%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}
Provides: %{name}-static = %{?epoch:%{epoch}:}%{version}-%{release}
Provides: %{name}%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}
Provides: %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires: libstdc++-devel%{?_isa}

%description devel
%{summary}.

%prep
%autosetup -p1

# Unbundling catch...
rm -rf test/3rdparty/Catch2
ln -svf %{_includedir}/catch2 test/3rdparty/Catch2

%build
%cmake -G Ninja \
    -DCMAKE_BUILD_TYPE=Release \
    -DSEMVER_OPT_BUILD_EXAMPLES:BOOL=ON \
    -DSEMVER_OPT_BUILD_TESTS:BOOL=ON \
    -DSEMVER_OPT_INSTALL:BOOL=ON
%cmake_build

%check
%ctest

%install
%cmake_install

%files devel
%doc README.md
%license LICENSE
%{_includedir}/%{name}.hpp
%{_libdir}/cmake/%{name}/

%changelog
* Tue Feb 28 2023 Vitaly Zaitsev <vitaly@easycoding.org> - 0.3.0-7
- Fixed FTBFS in EPEL/ELN due to catch v3 update.

* Tue Feb 28 2023 Vitaly Zaitsev <vitaly@easycoding.org> - 0.3.0-6
- Fixed FTBFS due to catch v3 update.

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 27 2022 Vitaly Zaitsev <vitaly@easycoding.org> - 0.3.0-3
- Fixed FTBFS on Fedora 36.

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Dec 22 2021 Vitaly Zaitsev <vitaly@easycoding.org> - 0.3.0-1
- Initial SPEC release.
