# EL8 and earlier does not have _vpath_builddir defined
%{?!_vpath_builddir:%define _vpath_builddir %{_target_platform}}

%if %{?cmake_build:1}%{?!cmake_build:0}
%global old_build 0
%else
%global old_build 1
%endif

%if 0%{?rhel} > 0
# bug 1883094 - hexchat-autoaway failed to build in aarch64 because hexchat-devel is missing
excludearch:    aarch64
# bug 1883095 - hexchat-autoaway failed to build in 390x because hexchat-devel is missing
excludearch:    s390x
%if 0%{?rhel} == 9
# hexchat-devel is missing for ppc64le
excludearch:    ppc64le
%endif
%endif

Name:           hexchat-autoaway
Version:        2.0
Release:        17%{?dist}
Summary:        HexChat plugin that automatically mark you away

# Automatically converted from old format: GPLv3+ - review is highly recommended.
License:        GPL-3.0-or-later
URL:            https://github.com/andreyv/hexchat-autoaway
Source0:        https://github.com/andreyv/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz

## Upstream PR#3 "feat(away-nick-suffix): append away suffix to nickname"
Patch0:         https://patch-diff.githubusercontent.com/raw/andreyv/hexchat-autoaway/pull/3.patch#/0001-append-away-suffix-to-nickname.patch

BuildRequires:  cmake3
BuildRequires:  gcc-c++
BuildRequires:  git
BuildRequires:  gtk2-devel >= 2.14
BuildRequires:  hexchat-devel
BuildRequires:  libXScrnSaver-devel
BuildRequires: make
Requires: gtk2 >= 2.14
Requires: hexchat

%description
This HexChat plugin will automatically mark you away when your
computer is idle. It works on systems that use the GTK+ X11
backend, such as GNU/Linux.

%prep
%autosetup -S git_am

%build
%if %old_build
mkdir -p %_vpath_builddir
cd %_vpath_builddir && %cmake3 -DCMAKE_BUILD_TYPE=Release ..
%make_build
cd -
%else
%cmake -DCMAKE_BUILD_TYPE=Release
%cmake_build
%endif

%install
%if %old_build
%make_install -C %_vpath_builddir
%else
%cmake_install
%endif

%files
%license COPYING
%doc README.md
%{_libdir}/hexchat/plugins/libautoaway.so

%changelog
* Mon Jan 20 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 25 2024 Miroslav Suchý <msuchy@redhat.com> - 2.0-16
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jan 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Aug 24 2022 Ding-Yi Chen <dchen@redhat.com> - 2.0-10
- ExcludeArch ppc64le for EL9

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Sep 29 2020 Ding-Yi Chen <dchen@redhat.com> - 2.0-5
- Fix conditional build

* Mon Sep 28 2020 Ding-Yi Chen <dchen@redhat.com> - 2.0-4
- ExcludeArch s390x and aarch64 because hexchat-devel is missing

* Sun Sep 20 2020 Ding-Yi Chen <dchen@redhat.com> - 2.0-3
- Change the patch filename as suggested in package review.
- Fix for koji build

* Mon Sep 07 2020 Ding Yi Chen <dchen@redhat.com> - 2.0-2
- Remove upstream pull request #2, as it is invalid.
- Add upstream pull request #3
  feat(away-nick-suffix): append away suffix to nickname

* Sun Jul 26 2020 Ding Yi Chen <dchen@redhat.com> - 2.0-1
- Initial packaging
