Name:           clazy
Summary:        Qt oriented code checker based on clang framework
Version:        1.13
Release:        2%{?dist}
License:        LGPL-2.0-or-later
URL:            https://invent.kde.org/sdk/%{name}

%if 0%{?commitdate}
Source0:        %{url}/-/archive/%{commit}/%{name}-%{commit}.tar.gz
%else
Source0:        https://download.kde.org/stable/%{name}/%{version}/src/%{name}-%{version}.tar.xz
%endif

Patch0:         clazy-no-rpath.patch

BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: clang-devel llvm-devel
BuildRequires: perl-podlators

Requires: clang(major) = %{clang_major_version}

%description
clazy is a compiler plugin which allows clang to understand Qt semantics.
You get more than 50 Qt related compiler warnings, ranging from unneeded
memory allocations to misusage of API, including fix-its for automatic
refactoring.


%prep
%autosetup -p1 %{?commitdate:-n %{name}-%{commit}}

%build
%cmake
%cmake_build

%install
%cmake_install

%ldconfig_scriptlets

%files
%doc HOWTO.md README.md
%license LICENSES/*
%{_bindir}/clazy
%{_bindir}/clazy-standalone
%dir %{_docdir}/clazy
%{_docdir}/clazy/*
%{_mandir}/man1/clazy.1.gz
%{_libdir}/ClazyPlugin.so
%{_datadir}/metainfo/org.kde.clazy.metainfo.xml


%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.13-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Dec 30 2024 Steve Cossette <farchord@gmail.com> - 1.13-1
- 1.13

* Wed Nov 20 2024 Jan Grulich <jgrulich@redhat.com> - 1.12^git20241119.560bdc1-1
- Update to latest snapshot with LLVM-19 support

* Mon Oct 21 2024 Jan Grulich <jgrulich@redhat.com> - 1.11^git20240128.69fedb4-7
- Rebuild (LLVM-19)

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.11^git20240128.69fedb4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Mar 02 2024 Tom Stellard <tstellar@redhat.com> - 1.11^git20240128.69fedb4-5
- Rebuild for clang 18

* Mon Jan 29 2024 Jan Grulich <jgrulich@redhat.com> - 1.11^git20230618.69fedb4-4
- Update to latest git snapshot

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.11^git20230618.b205b52-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.11^git20230618.b205b52-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Tue Sep 19 2023 Alessandro Astone <ales.astone@gmail.com> - 1.11^git20230618.b205b52-1
- Build from git snapshot to fix crash with LLVM17

* Wed Sep 06 2023 Jan Grulich <jgrulich@redhat.com> - 1.11-9
- Rebuild (clang-17)

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.11-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Apr 13 2023 Jan Grulich <jgrulich@redhat.com> - 1.11-7
- Rebuild against fixed clang

* Thu Apr 13 2023 Jan Grulich <jgrulich@redhat.com> - 1.11-6
- Rebuild (clang-16)

* Tue Apr 11 2023 Jan Grulich <jgrulich@redhat.com> - 1.11-5
- Rebuild (clang-16)

* Mon Feb 20 2023 Neal Gompa <ngompa@fedoraproject.org> - 1.11-4
- Explicitly Require: specific major version of Clang

* Tue Jan 31 2023 Jan Grulich <jgrulich@redhat.com> - 1.11-3
- migrated to SPDX license

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Jan 18 2023 Jan Grulich <jgrulich@redhat.com> - 1.11-1
- 1.11

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.9-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.9-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Sat May 01 2021 FeRD (Frank Dana) <ferdnyc@gmail.com> - 1.9-1
- New upstream release 1.9
- Build against LLVM-12 for clang-12 in Fedora 34+
- Drop upstreamed patches

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Jan 22 2021 Tom Stellard <tstellar@redhat.com> - 1.7-2
- Rebuild for clang-11.1.0

* Mon Oct 26 07:05:22 CET 2020 Jan Grulich <jgrulich@redhat.com> - 1.6-7
- Update 1.7

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.6-6
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.6-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jul 09 2020 Jan Grulich <jgrulich@redhat.com> - 1.6-4
- Fix build against LLVM 10

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Dec 13 2019 Tom Stellard <tstellar@redhat.com> - 1.6-2
- Link against libclang-cpp.so
- https://fedoraproject.org/wiki/Changes/Stop-Shipping-Individual-Component-Libraries-In-clang-lib-Package

* Wed Oct 30 2019 Jan Grulich <jgrulich@redhat.com> - 1.6-1
- 1.6

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Apr 30 2019 Tom Stellard <tstellar@redhat.com> - 1.5-2
- Rebuild for clang-8.0.0

* Sun Feb 03 2019 Jan Grulich <jgrulich@redhat.com> - 1.5-1
- Update to 1.5

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Dec 03 2018 Jan Grulich <jgrulich@redhat.com> - 1.4-2
- Require clang

* Tue Oct 02 2018 Jan Grulich <jgrulich@redhat.com> - 1.4-1
- Initial version
