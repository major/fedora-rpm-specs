%global debug_package %{nil}

Name:           plasma-mobile-sounds
Version:        0.1
Release:        10%{?dist}
# Automatically converted from old format: CC-BY-SA and CC0 and CC-BY - review is highly recommended.
License:        LicenseRef-Callaway-CC-BY-SA AND CC0-1.0 AND LicenseRef-Callaway-CC-BY
Summary:        Plasma Mobile Sound Theme
Url:            https://invent.kde.org/plasma-mobile/plasma-mobile-sounds
Source:         https://download.kde.org/stable/plasma-mobile-sounds/0.1/plasma-mobile-sounds-0.1.tar.xz

# Use cmake datadir
# https://invent.kde.org/plasma-mobile/plasma-mobile-sounds/-/merge_requests/2
Patch1:         0001-Use-cmake-datadir.patch

BuildArch: noarch

BuildRequires: cmake
BuildRequires: kf6-rpm-macros

%description
%{summary}.

%prep
%autosetup

%build
%cmake_kf6
%cmake_build

%install
%cmake_install

%files
%{_datadir}/sounds/plasma-mobile

%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Dec 11 2024 Troy Dawson <tdawson@redhat.com> - 0.1-9
- Use cmake datadir

* Wed Sep 4 2024 Miroslav Suchý <msuchy@redhat.com> - 0.1-8
- convert license to SPDX

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Mar 11 2022 Justin Zobel <justin@1707.io> - 0.1-1
- Initial version of package
