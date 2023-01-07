%global appid eu.scarpetta.PDFMixTool

Name:           pdfmixtool
Version:        1.1.1
Release:        3%{?dist}
Summary:        An application to split, merge, rotate and mix PDF files

License:        GPLv3+
URL:            https://scarpetta.eu/pdfmixtool
Source0:        https://gitlab.com/scarpetta/pdfmixtool/-/archive/v%{version}/%{name}-v%{version}.tar.gz

BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  cmake(qt5)
BuildRequires:  cmake(qt5svg)
BuildRequires:  pkgconfig(Magick++)
BuildRequires:  pkgconfig(libqpdf)
BuildRequires:  qt5-qttools-devel
BuildRequires:  desktop-file-utils
BuildRequires:  libappstream-glib

Requires:       hicolor-icon-theme

%description
PDF Mix Tool is a simple and lightweight application that allows you to
perform common editing operations on PDF files.

%prep
%autosetup -n %{name}-v%{version}

%build
%cmake
%cmake_build

%install
%cmake_install

%check
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/%{appid}.appdata.xml
desktop-file-validate %{buildroot}%{_datadir}/applications/%{appid}.desktop

%files
%license LICENSE
%doc README.md CHANGELOG.md AUTHORS.md TRANSLATORS.md
%{_bindir}/%{name}
%{_datadir}/applications/%{appid}.desktop
%{_datadir}/icons/hicolor/*/apps/*
%{_metainfodir}/%{appid}.appdata.xml

%changelog
* Thu Jan 05 2023 Neal Gompa <ngompa@fedoraproject.org> - 1.1.1-3
- Rebuild for ImageMagick 7

* Thu Oct 13 2022 Gustavo Costa <xfgusta@gmail.com> - 1.1.1-2
- qpdf 11.1.1 rebuild

* Sun Sep 25 2022 Gustavo Costa <xfgusta@gmail.com> - 1.1.1-1
- Update to 1.1.1 (rhbz#2129512)

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sun Jun 12 2022 Gustavo Costa <xfgusta@fedoraproject.org> - 1.1-1
- Update to 1.1

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Dec 29 2021 Gustavo Costa <xfgusta@fedoraproject.org> - 1.0.2-1
- Initial package
