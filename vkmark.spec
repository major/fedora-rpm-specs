# vkamrk dynamicly loads modules that reference static functions in the main binary
%undefine _strict_symbol_defs_build

%global codate 20230412
%global commit0 ab6e6f34077722d5ae33f6bd40b18ef9c0e99a15
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})

# Some tests fail on s390x
# https://bugzilla.redhat.com/show_bug.cgi?id=1475561
ExcludeArch:    s390x

Name:           vkmark
Version:        2017.08
Release:        0.19.%{codate}git%{shortcommit0}%{?dist}
Summary:        Vulkan benchmarking suite

License:        LGPL-2.1-or-later
URL:            https://github.com/vkmark/vkmark
Source0:        https://github.com/vkmark/vkmark/archive/%{commit0}.tar.gz#/%{name}-%{version}-%{shortcommit0}.tar.gz

BuildRequires:  gcc-c++
BuildRequires:  meson

BuildRequires:  vulkan-loader-devel
BuildRequires:  glm-devel
BuildRequires:  assimp-devel

BuildRequires:  libxcb-devel
BuildRequires:  xcb-util-wm-devel
BuildRequires:  wayland-devel
BuildRequires:  wayland-protocols-devel
BuildRequires:  libdrm-devel
BuildRequires:  mesa-libgbm-devel


%description
vkmark is an extensible Vulkan benchmarking suite with targeted,
configurable scenes.

%prep
%autosetup -p1 -n %{name}-%{commit0}


%build
%meson
%meson_build


%install
%meson_install


%check
%meson_test


%files
%license COPYING-LGPL2.1
%{_bindir}/%{name}
%{_libdir}/%{name}
%{_datadir}/%{name}
%{_mandir}/man1/%{name}.1*


%changelog
* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2017.08-0.19.20230412gitab6e6f3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Apr 12 2023 Yanko Kaneti <yaneti@declera.com> - 2017.08-0.18.20230312gitab6e6f3
- Pull a recent snapshot. Brings back the kms backend. Drop upstreamed patch
- Migrate to SPDX license identifier

* Sat Jan 21 2023 Yanko Kaneti <yaneti@declera.com> - 2017.08-0.18.20230121git30d2cd3
- Pull a recent snapshot + addtional patch to fixup standard includes

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2017.08-0.17.20220617gitd872846
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2017.08-0.16.20220617gitd872846
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jun 17 2022 Yanko Kaneti <yaneti@declera.com> - 2017.08-0.15.20220617gitd872846
- Pull a recent snapshot to fix various build issues

* Wed Mar 30 2022 Yanko Kaneti <yaneti@declera.com> - 2017.08-0.14.20210727git53abc4f
- Update build requirements

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2017.08-0.13.20210727git53abc4f
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Sun Aug 01 2021 Rich Mattes <richmattes@gmail.com> - 2017.08-0.12.20210727git53abc4f
- Rebuild for assimp-5.0.1

* Tue Jul 27 2021 Yanko Kaneti <yaneti@declera.com> - 2017.08-0.11.20210727git53abc4f
- Pick the latest snapshot
- Fix FTBFS by replacing the bundled catch framework with catch1-devel

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2017.08-0.11.20210201gite8c0720
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon Feb  1 2021 Yanko Kaneti <yaneti@declera.com> - 2017.08-0.10.20210201gite8c0720
- Pull a newer snapshot ro reflect recent years changes and make it build

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2017.08-0.10.20180123git68b6f23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2017.08-0.9.20180123git68b6f23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2017.08-0.8.20180123git68b6f23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2017.08-0.7.20180123git68b6f23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2017.08-0.6.20180123git68b6f23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2017.08-0.5.20180123git68b6f23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Jun 29 2018 Yanko Kaneti <yaneti@declera.com> - 2017.08-0.4.20180123git68b6f23
- vulkan-devel -> vulkan-loader-devel

* Mon Feb 19 2018 Wolfgang Stöggl <c72578@yahoo.de> - 2017.08-0.3.20180123git68b6f23
- Add BuildRequires: gcc-c++

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2017.08-0.2.20180123git68b6f23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Jan 23 2018 Yanko Kaneti <yaneti@declera.com> - 2017.08-0.1.20180123git68b6f23
- Update to 68b6f23 with kms-atomic support.
- Add undefine _strict_symbol_defs_build folowing the -z defs linker flags change

* Mon Sep  4 2017 Yanko Kaneti <yaneti@declera.com> - 2017.08-0.1.20170904git0fed663
- Update to 2017.08, 0fed663
- Upstream license change to only LGPLv2+

* Mon Aug 14 2017 Yanko Kaneti <yaneti@declera.com> - 2017.07-0.9.20170814git7b5bbee
- Update to 7b5bbee

* Wed Aug  9 2017 Yanko Kaneti <yaneti@declera.com> - 2017.07-0.8.20170809git19e128c
- Update to 19e128c

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2017.07-0.7.20170727git1b05d87
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Sun Jul 30 2017 Florian Weimer <fweimer@redhat.com> - 2017.07-0.6.20170727git1b05d87
- Rebuild with binutils fix for ppc64le (#1475636)

* Thu Jul 27 2017 Yanko Kaneti <yaneti@declera.com> - 2017.07-0.5.20170727git1b05d87
- Update to 1b05d87
- Add bug reference to the s390x ExcludeArch issue

* Wed Jul 26 2017 Yanko Kaneti <yaneti@declera.com> - 2017.07-0.5.20170725gitaa0de26
- ExcludeArch s390x for now

* Wed Jul 26 2017 Yanko Kaneti <yaneti@declera.com> - 2017.07-0.4.20170725gitaa0de26
- Vulkan backend only available on x86_64, condition the mesa-vulkan-devel

* Wed Jul 26 2017 Yanko Kaneti <yaneti@declera.com> - 2017.07-0.3.20170725gitaa0de26
- Add %%check, running the meson tests, as per review (#1473320)

* Tue Jul 25 2017 Yanko Kaneti <yaneti@declera.com> - 2017.07-0.2.20170725gitaa0de26
- Add date to the revision, as per review (#1473320)

* Thu Jul 20 2017 Yanko Kaneti <yaneti@declera.com> - 2017.07-0.1.gitfd9f927
- Initial spec
