Name: mtxclient
Version: 0.9.1
Release: 2%{?dist}

License: MIT
Summary: Client API library for Matrix, built on top of Boost.Asio
URL: https://github.com/Nheko-Reborn/%{name}
Source0: %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

# https://github.com/Nheko-Reborn/mtxclient/pull/91
Patch100: %{name}-gcc13-fixes.patch

BuildRequires: cmake(mpark_variant)
BuildRequires: cmake(nlohmann_json) >= 3.2.0
BuildRequires: cmake(Olm) >= 3.2.12
BuildRequires: cmake(spdlog) >= 1.0.0

BuildRequires: pkgconfig(coeurl) >= 0.3.0
BuildRequires: pkgconfig(libcrypto)
BuildRequires: pkgconfig(libevent)
BuildRequires: pkgconfig(openssl)
BuildRequires: pkgconfig(re2)
BuildRequires: pkgconfig(zlib)

BuildRequires: cmake
BuildRequires: gcc
BuildRequires: gcc-c++
BuildRequires: ninja-build

%description
Client API library for the Matrix protocol, built on top of Boost.Asio.

%package devel
Summary: Development files for %{name}
Requires: %{name}%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}

%description devel
%{summary}.

%prep
%autosetup -p1

%build
%cmake -G Ninja \
    -DCMAKE_BUILD_TYPE=Release \
    -DHUNTER_ENABLED:BOOL=OFF \
    -DUSE_BUNDLED_COEURL:BOOL=OFF \
    -DUSE_BUNDLED_GTEST:BOOL=OFF \
    -DUSE_BUNDLED_JSON:BOOL=OFF \
    -DUSE_BUNDLED_LIBCURL:BOOL=OFF \
    -DUSE_BUNDLED_LIBEVENT:BOOL=OFF \
    -DUSE_BUNDLED_OLM:BOOL=OFF \
    -DUSE_BUNDLED_OPENSSL:BOOL=OFF \
    -DUSE_BUNDLED_SPDLOG:BOOL=OFF \
    -DASAN:BOOL=OFF \
    -DCOVERAGE:BOOL=OFF \
    -DIWYU:BOOL=OFF \
    -DBUILD_LIB_TESTS:BOOL=OFF \
    -DBUILD_LIB_EXAMPLES:BOOL=OFF
%cmake_build

%install
%cmake_install
ln -s libmatrix_client.so.%{version} %{buildroot}%{_libdir}/libmatrix_client.so.0

%files
%doc README.md
%license LICENSE
%{_libdir}/*.so.0*

%files devel
%{_includedir}/%{name}
%{_includedir}/mtx
%{_includedir}/mtx.hpp
%{_libdir}/cmake/MatrixClient
%{_libdir}/*.so

%changelog
* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jan 13 2023 Vitaly Zaitsev <vitaly@easycoding.org> - 0.9.1-1
- Updated to version 0.9.1.

* Thu Nov 03 2022 Vitaly Zaitsev <vitaly@easycoding.org> - 0.8.2-3
- Rebuilt due to spdlog update.

* Fri Sep 09 2022 Vitaly Zaitsev <vitaly@easycoding.org> - 0.8.2-2
- Rebuilt due to incorrect Koji tag usage.

* Fri Sep 09 2022 Vitaly Zaitsev <vitaly@easycoding.org> - 0.8.2-1
- Updated to version 0.8.2.

* Thu Sep 08 2022 Vitaly Zaitsev <vitaly@easycoding.org> - 0.8.1-1
- Updated to version 0.8.1.

* Tue Aug 16 2022 Vitaly Zaitsev <vitaly@easycoding.org> - 0.8.0-2
- Rebuilt due to json update.

* Sat Jul 23 2022 Vitaly Zaitsev <vitaly@easycoding.org> - 0.8.0-1
- Updated to version 0.8.0.

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jul 16 2022 Vitaly Zaitsev <vitaly@easycoding.org> - 0.7.0-3
- Rebuilt due to fmt library update.

* Sat Apr 30 2022 Vitaly Zaitsev <vitaly@easycoding.org> - 0.7.0-2
- Rebuilt due to spdlog update.

* Thu Mar 10 2022 Vitaly Zaitsev <vitaly@easycoding.org> - 0.7.0-1
- Updated to version 0.7.0.

* Wed Feb 23 2022 Vitaly Zaitsev <vitaly@easycoding.org> - 0.6.2-1
- Updated to version 0.6.2.

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Dec 21 2021 Vitaly Zaitsev <vitaly@easycoding.org> - 0.6.1-1
- Updated to version 0.6.1.

* Fri Nov 19 2021 Vitaly Zaitsev <vitaly@easycoding.org> - 0.6.0-1
- Updated to version 0.6.0.

* Mon Sep 27 2021 Vitaly Zaitsev <vitaly@easycoding.org> - 0.5.1-5
- Fixed build against libolm 3.2.6.

* Tue Sep 14 2021 Sahana Prasad <sahana@redhat.com> - 0.5.1-4
- Rebuilt with OpenSSL 3.0.0

* Sat Aug 07 2021 Jonathan Wakely <jwakely@redhat.com> - 0.5.1-3
- Rebuilt for Boost 1.76

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Apr 23 2021 Vitaly Zaitsev <vitaly@easycoding.org> - 0.5.1-1
- Updated to version 0.5.1.

* Sat Jan 30 2021 Vitaly Zaitsev <vitaly@easycoding.org> - 0.4.1-1
- Updated to version 0.4.1.

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Jan 22 2021 Jonathan Wakely <jwakely@redhat.com> - 0.4.0-4
- Rebuilt for Boost 1.75

* Wed Jan 20 2021 Vitaly Zaitsev <vitaly@easycoding.org> - 0.4.0-3
- Backported upstream patch with LTO fixes.

* Wed Jan 20 2021 Vitaly Zaitsev <vitaly@easycoding.org> - 0.4.0-2
- Disabled LTO due to nheko linkage issues.

* Wed Jan 20 2021 Vitaly Zaitsev <vitaly@easycoding.org> - 0.4.0-1
- Updated to version 0.4.0.

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sun Jun 14 2020 Vitaly Zaitsev <vitaly@easycoding.org> - 0.3.1-1
- Updated to version 0.3.1.

* Wed Jun 03 2020 Vitaly Zaitsev <vitaly@easycoding.org> - 0.3.0-1
- Updated to version 0.3.0.

* Sat May 30 2020 Jonathan Wakely <jwakely@redhat.com> - 0.2.1-4
- Rebuilt for Boost 1.73

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu May 23 2019 Vitaly Zaitsev <vitaly@easycoding.org> - 0.2.1-1
- Updated version 0.2.1 (regular release).

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jan 25 2019 Jonathan Wakely <jwakely@redhat.com> - 0.2.0-3
- Rebuilt for Boost 1.69

* Sat Jan 05 2019 Vitaly Zaitsev <vitaly@easycoding.org> - 0.2.0-2
- Rebuilt due to libolm update.

* Sat Sep 22 2018 Vitaly Zaitsev <vitaly@easycoding.org> - 0.2.0-1
- Updated version 0.2.0 (regular release).

* Sun Sep 02 2018 Vitaly Zaitsev <vitaly@easycoding.org> - 0.1.0-11
- Obsolete matrix-structs package correctly.

* Sun Sep 02 2018 Vitaly Zaitsev <vitaly@easycoding.org> - 0.1.0-10
- Updated version 0.1.0 (regular release).

* Sun Aug 12 2018 Vitaly Zaitsev <vitaly@easycoding.org> - 0.1.0-9.20180808git1089467
- Updated to latest snapshot.

* Tue Jul 31 2018 Florian Weimer <fweimer@redhat.com> - 0.1.0-8.20180726gitca66424
- Rebuild with fixed binutils

* Fri Jul 27 2018 Vitaly Zaitsev <vitaly@easycoding.org> - 0.1.0-7.20180726gitca66424
- Updated to latest snapshot.

* Fri Jul 27 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.1.0-6.20180714git2f519d2
- Rebuild for new binutils

* Thu Jul 26 2018 Vitaly Zaitsev <vitaly@easycoding.org> - 0.1.0-5.20180714git2f519d2
- Minor SPEC fixes.

* Sat Jul 14 2018 Vitaly Zaitsev <vitaly@easycoding.org> - 0.1.0-4.20180714git2f519d2
- Updated to latest snapshot.

* Sun Jul 08 2018 Vitaly Zaitsev <vitaly@easycoding.org> - 0.1.0-3.20180707git708c8c6
- Updated to latest snapshot.

* Sun Jul 01 2018 Vitaly Zaitsev <vitaly@easycoding.org> - 0.1.0-2.20180627git7349126
- Updated to latest snapshot.

* Sun Jun 24 2018 Vitaly Zaitsev <vitaly@easycoding.org> - 0.1.0-2.20180622git96fd35e
- Initial SPEC release.
