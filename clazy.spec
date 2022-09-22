
Name:           clazy
Summary:        Qt oriented code checker based on clang framework
Version:        1.9
Release:        4%{?dist}
License:        LGPLv2
URL:            https://invent.kde.org/sdk/%{name}/
Source0:        https://download.kde.org/stable/%{name}/%{version}/src/%{name}-%{version}.tar.xz

Patch0:         clazy-no-rpath.patch
# The upstream solution to building under clang-12, while still
# supporting older versions as well. Does raise the C++ standard
# version required to c++17, reportedly.
# See: https://invent.kde.org/sdk/clazy/-/merge_requests/33
Patch1:         clazy-clang12-mr33.patch

BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: clang-devel llvm-devel
BuildRequires: perl-podlators

Requires: clang

%description
clazy is a compiler plugin which allows clang to understand Qt semantics.
You get more than 50 Qt related compiler warnings, ranging from unneeded
memory allocations to misusage of API, including fix-its for automatic
refactoring.


%prep
%autosetup -p1

%build
%{cmake} \
    -DCMAKE_CXX_STANDARD=17 \
    -DCMAKE_CXX_STANDARD_REQUIRED=1

%cmake_build

%install
%cmake_install

%ldconfig_scriptlets

%files
%doc HOWTO
%license COPYING*
%{_bindir}/clazy
%{_bindir}/clazy-standalone
%dir %{_docdir}/clazy
%{_docdir}/clazy/*
%{_mandir}/man1/clazy.1.gz
%{_libdir}/ClazyPlugin.so
%{_datadir}/metainfo/org.kde.clazy.metainfo.xml


%changelog
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
