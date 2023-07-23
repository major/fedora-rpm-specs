%global debug_package %{nil}

Name:		socnetv
Version:	3.1
Release:	2%{?dist}
License:	GPLv3
Summary:	A Social Networks Analyser and Visualiser
URL:		https://socnetv.org/
Source0:	https://github.com/socnetv/app/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires: make
BuildRequires:	gcc-c++
BuildRequires:	gzip
BuildRequires:	qt6-linguist
BuildRequires:	desktop-file-utils
# qt6-qtbase-devel
BuildRequires:	pkgconfig(Qt6)
# qt6-qtsvg-devel
BuildRequires:	pkgconfig(Qt6Svg)
# qt6-qtcharts-devel
BuildRequires:	pkgconfig(Qt6Charts)
# qt6-qt5compat-devel
BuildRequires:	pkgconfig(Qt6Core5Compat)

%description
Social Network Visualizer (SocNetV) is a cross-platform, user-friendly
free software application for social network analysis and visualization.


%prep
%autosetup -n app-%{version}
gunzip changelog.gz
chmod -x changelog

%build
lrelease-qt6 socnetv.pro
qmake6
%{make_build}


%install
%{make_install} INSTALL_ROOT=%{buildroot}


%check
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop


%post
/usr/bin/update-desktop-database &> /dev/null || :


%postun
/usr/bin/update-desktop-database &> /dev/null || :


%files
%license COPYING
%doc AUTHORS changelog NEWS README.md
%{_bindir}/%{name}
%{_datadir}/%{name}/%{name}_*.qm
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.png
%{_datadir}/metainfo/%{name}.appdata.xml
%{_mandir}/man1/%{name}.1.gz


%changelog
* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sun Jun 18 2023 TI_Eugene <ti.eugene@gmail.com> 3.1-1
- Version bump
- Qt6

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 TI_Eugene <ti.eugene@gmail.com> 3.0.4-3
- Rebuild with fresh qtchart

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Sep 17 2021 TI_Eugene <ti.eugene@gmail.com> 3.0.4-1
- Version bump

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jun 15 2021 TI_Eugene <ti.eugene@gmail.com> 2.9-1
- Version bump

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Jan 07 2021 TI_Eugene <ti.eugene@gmail.com> 2.8-1
- Version bump

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun 16 2020 TI_Eugene <ti.eugene@gmail.com> 2.5-2
- Spec file fixes

* Tue Jun 09 2020 TI_Eugene <ti.eugene@gmail.com> 2.5-1
- Initital build
