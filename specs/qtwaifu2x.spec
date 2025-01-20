%global commit          2973f6fc99b62346ac954a1192059d3f1c5ede61
%global shortcommit     %(c=%{commit}; echo ${c:0:7})
%global snapshotdate    20200709

Name:           qtwaifu2x
Version:        0
Release:        0.19.%{snapshotdate}git%{shortcommit}%{?dist}
Summary:        Frontend for waifu2x-converter-cpp

# Automatically converted from old format: GPLv2 - review is highly recommended.
License:        GPL-2.0-only
URL:            https://github.com/cmdrkotori/qtwaifu2x
Source0:        %url/archive/%{commit}/%{name}-%{shortcommit}.tar.gz
Source1:        qtwaifu2x.desktop
# Fix noise-scale flag
Patch0:         https://patch-diff.githubusercontent.com/raw/cmdrkotori/qtwaifu2x/pull/3.patch#/0001-Fix-noise-scale-flag.patch

BuildRequires: make
BuildRequires:  gcc-c++
BuildRequires:  desktop-file-utils
BuildRequires:  qt5-qtbase-devel
Requires:       hicolor-icon-theme
Requires:       waifu2x-converter-cpp

%description
Frontend for waifu2x-converter-cpp.


%prep
%autosetup -p1 -n %{name}-%{commit}


%build
%qmake_qt5
%make_build


%install
install -Dpm 0755 qtwaifu2x %{buildroot}%{_bindir}/qtwaifu2x
install -Dpm 0644 images/icon.png %{buildroot}%{_datadir}/icons/hicolor/512x512/apps/qtwaifu2x.png

desktop-file-install                                        \
    --dir=%{buildroot}%{_datadir}/applications              \
    %{SOURCE1}



%files
%license LICENSE
%doc README.md
%{_bindir}/qtwaifu2x
%{_datadir}/applications/qtwaifu2x.desktop
%{_datadir}/icons/hicolor/512x512/apps/qtwaifu2x.png


%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.19.20200709git2973f6f
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Jul 29 2024 Miroslav Suchý <msuchy@redhat.com> - 0-0.18.20200709git2973f6f
- convert license to SPDX

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.17.20200709git2973f6f
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.16.20200709git2973f6f
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.15.20200709git2973f6f
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.14.20200709git2973f6f
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.13.20200709git2973f6f
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.12.20200709git2973f6f
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.11.20200709git2973f6f
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.10.20200709git2973f6f
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.9.20200709git2973f6f
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.8.20200709git2973f6f
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.7.20200709git2973f6f
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 20 12:17:55 CEST 2020 Robert-André Mauchin <zebob.m@gmail.com> - 0-0.6.20200709git2973f6f
- Add patch to fix noise-scale

* Thu Jul 09 14:48:53 CEST 2020 Robert-André Mauchin <zebob.m@gmail.com> - 0-0.5.20200709git2973f6f
- Bump to commit 2973f6fc99b62346ac954a1192059d3f1c5ede61

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.4.20181013git0907ef8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.3.20181013git0907ef8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.2.20181013git0907ef8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Oct 13 2018 Robert-André Mauchin <zebob.m@gmail.com> - 0-0.1.20181013git0907ef8
- Initial release
