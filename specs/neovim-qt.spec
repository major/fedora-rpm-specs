%bcond_without  tests
# disable shared libraries to avoid building libneovim-qt-gui.so
# it's only needed for devel package which we're not providing
%undefine       _cmake_shared_libs

Name:           neovim-qt
Version:        0.2.19
Release:        2%{?dist}
Summary:        Qt GUI for Neovim

# src/gui/shellwidget/konsole_wcwidth.cpp: HPND-Markus-Kuhn
# third_party/DejaVuSans*: Bitstream-Vera AND LicenseRef-Fedora-Public-Domain
License:        ISC AND HPND-Markus-Kuhn
URL:            https://github.com/equalsraf/neovim-qt
Source:         %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  cmake
BuildRequires:  desktop-file-utils
BuildRequires:  gcc-c++

BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6Network)
BuildRequires:  cmake(Qt6SvgWidgets)
BuildRequires:  cmake(Qt6Test)
BuildRequires:  cmake(Qt6Widgets)
BuildRequires:  cmake(msgpack)
BuildRequires:  neovim
%if %{with tests}
BuildRequires:  font(dejavusansmono)
BuildRequires:  xwfb-run
%endif

Requires:       hicolor-icon-theme
Requires:       neovim

%description
%{summary}.

%prep
%autosetup -p1

%build
%cmake \
    -DWITH_QT:STRING=Qt6 \
    -DUSE_SYSTEM_MSGPACK:BOOL=ON  \
    -DENABLE_TESTS:BOOL=%{?with_tests:ON}%{!?with_tests:OFF}
%cmake_build

%install
%cmake_install

%check
desktop-file-validate %{buildroot}/%{_datadir}/applications/nvim-qt.desktop
%if %{with tests}
# UI component tests require running X server
%global __ctest xwfb-run -- %{__ctest}
%ctest
%endif

%files
%license LICENSE
%doc README.md
%{_bindir}/nvim-qt
%{_datadir}/applications/nvim-qt.desktop
%{_datadir}/icons/hicolor/192x192/apps/nvim-qt.png
%{_datadir}/icons/hicolor/scalable/apps/nvim-qt.svg
%{_datadir}/nvim-qt/

%changelog
* Thu Jul 24 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.19-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_43_Mass_Rebuild

* Fri Jan 24 2025 Aleksei Bavshin <alebastr@fedoraproject.org> - 0.2.19-1
- Update to 0.2.19
- Build with Qt6
- Convert License tag to SPDX
- Use xwfb-run for tests instead of xvfb-run

* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.18-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.18-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.18-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.18-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Oct 22 2023 Aleksei Bavshin <alebastr@fedoraproject.org> - 0.2.18-1
- Update to 0.2.18

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.17-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.17-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.17-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sun Jul 03 2022 Aleksei Bavshin <alebastr@fedoraproject.org> - 0.2.17-1
- Update to 0.2.17

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.16.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Aleksei Bavshin <alebastr@fedoraproject.org> - 0.2.16.1-3
- Skip tests if neovim is build without luajit
- Display ctest failure logs in %%check

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.16.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.16.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Nov 07 2020 Aleksei Bavshin <alebastr89@gmail.com> - 0.2.16.1-1
- Initial import (#1891160)
