Name: zswap-cli
Version: 0.9.1
Release: 4%{?dist}

License: MIT
Summary: Command-line tool to control zswap options
URL: https://github.com/xvitaly/%{name}
Source0: %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires: boost-devel
BuildRequires: cmake
BuildRequires: fmt-devel
BuildRequires: gcc-c++
BuildRequires: glibc-headers
BuildRequires: kernel-headers
BuildRequires: ninja-build
BuildRequires: pandoc
BuildRequires: semver-devel
BuildRequires: systemd

%{?systemd_requires}

%description
Zswap-cli is a command-line tool to control zswap Linux kernel module
options.

Zswap is a compressed cache for swap pages. It takes pages that are in the
process of being swapped out to disk and tries to compress them into a
RAM-based memory pool with dynamic allocation.

It trades CPU cycles for a significant performance boost since reading from
a compressed cache is much faster than reading from a swap device.

%prep
%autosetup

%build
%cmake -G Ninja \
    -DCMAKE_BUILD_TYPE=Release \
    -DBUILD_DOCS:BOOL=OFF \
    -DBUILD_MANPAGE:BOOL=ON \
    -DSYSTEMD_INTEGRATION:BOOL=ON
%cmake_build

%post
%systemd_post %{name}.service

%preun
%systemd_preun %{name}.service

%postun
%systemd_postun_with_restart %{name}.service

%install
%cmake_install

%files
%doc docs/*
%license LICENSE
%{_sbindir}/%{name}
%{_unitdir}/%{name}.service
%{_mandir}/man1/%{name}.*
%dir %{_sysconfdir}/%{name}
%config(noreplace) %{_sysconfdir}/%{name}/%{name}.conf

%changelog
* Wed Jun 28 2023 Vitaly Zaitsev <vitaly@easycoding.org> - 0.9.1-4
- Rebuilt due to fmt 10 update.

* Mon Feb 20 2023 Jonathan Wakely <jwakely@redhat.com> - 0.9.1-3
- Rebuilt for Boost 1.81

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sun Oct 02 2022 Vitaly Zaitsev <vitaly@easycoding.org> - 0.9.1-1
- Updated to version 0.9.1.

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sun Jul 10 2022 Vitaly Zaitsev <vitaly@easycoding.org> - 0.9.0-3
- Rebuilt due to fmt library update.

* Wed May 04 2022 Thomas Rodgers <trodgers@redhat.com> - 0.9.0-2
- Rebuilt for Boost 1.78

* Wed Mar 02 2022 Vitaly Zaitsev <vitaly@easycoding.org> - 0.9.0-1
- Updated to version 0.9.0.

* Sat Feb 12 2022 Vitaly Zaitsev <vitaly@easycoding.org> - 0.8.0-1
- Updated to version 0.8.0.

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Dec 22 2021 Vitaly Zaitsev <vitaly@easycoding.org> - 0.7.0-1
- Updated to version 0.7.0.

* Tue Dec 07 2021 Vitaly Zaitsev <vitaly@easycoding.org> - 0.6.0-1
- Updated to version 0.6.0.

* Sat Aug 07 2021 Jonathan Wakely <jwakely@redhat.com> - 0.5.0-4
- Rebuilt for Boost 1.76

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Sun Jul 04 2021 Vitaly Zaitsev <vitaly@easycoding.org> - 0.5.0-2
- Rebuilt due to fmt library update.

* Thu Apr 01 2021 Vitaly Zaitsev <vitaly@easycoding.org> - 0.5.0-1
- Updated to version 0.5.0.

* Tue Mar 02 2021 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 0.4.1-5
- Rebuilt for updated systemd-rpm-macros
  See https://pagure.io/fesco/issue/2583.

* Thu Jan 28 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sat Jul 04 2020 Igor Raits <ignatenkobrain@fedoraproject.org> - 0.4.1-2
- Switch to the new CMake macros.

* Mon Apr 27 2020 Vitaly Zaitsev <vitaly@easycoding.org> - 0.4.1-1
- Updated to version 0.4.1.

* Sun Apr 26 2020 Vitaly Zaitsev <vitaly@easycoding.org> - 0.4.0-1
- Updated to version 0.4.0.

* Wed Apr 22 2020 Vitaly Zaitsev <vitaly@easycoding.org> - 0.3.0-1
- Updated to version 0.3.0.

* Mon Apr 13 2020 Vitaly Zaitsev <vitaly@easycoding.org> - 0.2.0-1
- Updated to version 0.2.0.

* Sat Apr 04 2020 Vitaly Zaitsev <vitaly@easycoding.org> - 0.1.0-1
- Initial SPEC release.
