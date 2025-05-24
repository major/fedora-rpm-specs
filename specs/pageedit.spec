Name:           pageedit
Version:        2.4.0
Release:        1%{?dist}
Summary:        ePub visual XHTML editor

License:        GPL-3.0-or-later AND Apache-2.0
URL:            https://sigil-ebook.com/
Source0:        https://github.com/Sigil-Ebook/PageEdit/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  make
BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6Network)
BuildRequires:  cmake(Qt6WebEngineCore)
BuildRequires:  cmake(Qt6WebEngineWidgets)
BuildRequires:  cmake(Qt6Widgets)
BuildRequires:  cmake(Qt6Xml)
BuildRequires:  cmake(Qt6PrintSupport)
BuildRequires:  cmake(Qt6LinguistTools)
BuildRequires:  cmake(Qt6Svg)
BuildRequires:  desktop-file-utils

Provides:       bundled(gumbo) = 0.9.2

ExclusiveArch: %{qt6_qtwebengine_arches}


%description
An ePub visual XHTML editor based on Sigil's Deprecated BookView.


%prep
%autosetup -n PageEdit-%{version}


%build
%cmake -DINSTALL_BUNDLED_DICTS=0 -DSHARE_INSTALL_PREFIX:PATH=%{_prefix}
%cmake_build


%install
%cmake_install

desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop


%files
%license COPYING.txt
%doc ChangeLog.txt README.md
%{_bindir}/%{name}
%{_datadir}/%{name}/
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.png
%{_datadir}/icons/hicolor/*/apps/%{name}.svg


%changelog
* Thu May 22 2025 Dan Horák <dan[at]danny.cz> - 2.4.0-1
- updated to 2.4.0
- switched to Qt6

* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 28 2024 Dan Horák <dan@danny.cz> - 2.2.0-1
- updated to 2.2.0

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Nov 17 2023 Dan Horák <dan@danny.cz> - 2.0.2-1
- updated to 2.0.2

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.20-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.20-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Tue Oct 04 2022 Dan Horák <dan@danny.cz> - 1.9.20-1
- initial Fedora version
