
Name:		prestopalette
Version:	0.1.31
Release:	20%{?dist}
Summary:	An artist's tool for creating harmonious color palettes

License:	MIT
URL:		https://github.com/PrestoPalette/PrestoPalette
Source0:	https://github.com/PrestoPalette/PrestoPalette/archive/%{version}/%{version}.tar.gz#/prestopalette-%{version}.tar.gz
Source1:	https://raw.githubusercontent.com/PrestoPalette/PrestoPalette-Packaging/master/Fedora/PrestoPalette.appdata.xml#/PrestoPalette.appdata.xml
Source2:	https://raw.githubusercontent.com/PrestoPalette/PrestoPalette-Packaging/master/Fedora/Icon.png#/PrestoPalette.png

BuildRequires: make
BuildRequires: desktop-file-utils
BuildRequires: libappstream-glib
BuildRequires: gcc-c++
BuildRequires: qt5-qtbase-devel
BuildRequires: qt5-qtmultimedia-devel

ExcludeArch: i686

%{?el7:BuildRequires: tar}

%description
%{name} is an artist's tool for creating harmonious color palettes.

%prep
%autosetup -n PrestoPalette-%{version}

%build
%qmake_qt5 -config release PrestoPalette.pro && \
%make_build all
cat > PrestoPalette.desktop <<EOF
[Desktop Entry]
Name=PrestoPalette
Comment=An artist's tool for creating harmonious color palettes
Exec=PrestoPalette
Icon=%{_datadir}/pixmaps/PrestoPalette.png
Terminal=false
Type=Application
Categories=Graphics
EOF

%install
mkdir -p %{buildroot}/%{_bindir}
mkdir -p %{buildroot}/%{_datadir}/{applications,pixmaps,metainfo}
install -Dp -m 755 build/release/PrestoPalette %{buildroot}/%{_bindir}
desktop-file-install --dir=%{buildroot}/%{_datadir}/applications PrestoPalette.desktop
appstream-util validate-relax --nonet %{SOURCE1}
install -Dp -m 644 %{SOURCE1} %{buildroot}/%{_datadir}/metainfo/
install -Dp -m 644 %{SOURCE2} %{buildroot}/%{_datadir}/pixmaps/

%files
%{_bindir}/PrestoPalette
%{_datadir}/applications/PrestoPalette.desktop
%{_datadir}/metainfo/PrestoPalette.appdata.xml
%{_datadir}/pixmaps/PrestoPalette.png
%license LICENSE

%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.31-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.31-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.31-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.31-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.31-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.31-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.31-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.31-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.31-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.31-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Aug 01 2020 Darryl T. Agostinelli <dagostinelli@gmail.com> - 0.1.31-10
- qt5-devel metapackage was dropped. Replaced dependencies
  https://bugzilla.redhat.com/show_bug.cgi?id=1865253

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.31-9
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.31-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.31-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.31-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.31-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Jul 18 2018 Darryl T. Agostinelli <dagostinelli@gmail.com> 0.1.31-4
- Corrected bodhi lint check against desktop file regarding multiple primary categories

 Wed Jul 18 2018 Darryl T. Agostinelli <dagostinelli@gmail.com> 0.1.31-3
- Corrected bodhi lint check against desktop file regarding icon name with an extension

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.31-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Mar 29 2018 Darryl T. Agostinelli <dagostinelli@gmail.com> 0.1.31-1
- Created the .spec file for version 0.1.31
