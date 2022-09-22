#%%global prerelease beta1
%global with_qt4 0%{?rhel} && 0%{?rhel} < 8
%global with_qt5 (0%{?rhel} && 0%{?rhel} >= 8) || 0%{?fedora}


Name:		qpdfview
Version:	0.4.18
Release:	10%{?dist}
# Use the following format for beta
#Release:	0.1.%%{?prerelease}%%{?dist}
License:	GPLv2+
Summary:	Tabbed PDF Viewer
Url:		https://launchpad.net/qpdfview
Source0:	https://launchpad.net/qpdfview/trunk/%{version}%{?prerelease}/+download/%{name}-%{version}%{?prerelease}.tar.gz
Patch0:		%{name}_model.patch
BuildRequires:	gcc-c++
BuildRequires:	make
BuildRequires:	desktop-file-utils
BuildRequires:	file-devel
BuildRequires:	cups-devel
BuildRequires:	hicolor-icon-theme
BuildRequires:	pkgconfig(libspectre)
BuildRequires:	pkgconfig(zlib)
%if 0%{?fedora}
# check if required for qt4
BuildRequires:	pkgconfig(ddjvuapi)
%endif

%description
qpdfview is a tabbed PDF viewer.
It uses the Poppler library for rendering and CUPS for printing.
It provides a clear and simple graphical user interface using the Qt framework.


%package common
Summary:	Common files for %{name}
BuildArch:	noarch

%description common
This package provides common files for %{name}.

%if %{with_qt4}
%package qt4
Summary:	Tabbed PDF Viewer
BuildRequires:	pkgconfig(poppler-qt4)
BuildRequires:	pkgconfig(QtGui)
BuildRequires:	pkgconfig(QtDBus)
%if 0%{?rhel}
Requires:	qt-sqlite
%endif
Requires:	%{name}-common = %{version}-%{release}
Obsoletes:	%{name} < %{version}-%{release}

%description qt4
qpdfview is a tabbed PDF viewer.
It uses the Poppler library for rendering and CUPS for printing.
It provides a clear and simple graphical user interface using the Qt framework.
%endif


%if %{with_qt5}
%package qt5
Summary:	Tabbed PDF Viewer
BuildRequires:	qt5-qttools-devel
BuildRequires:	pkgconfig(poppler-qt5)
BuildRequires:	pkgconfig(Qt5DBus)
BuildRequires:	pkgconfig(Qt5Gui)
BuildRequires:	pkgconfig(Qt5Svg)
BuildRequires:	pkgconfig(Qt5Widgets)
Requires:	%{name}-common = %{version}-%{release}
%if 0%{?fedora} > 33
Obsoletes:	%{name} < %{version}-%{release}
%endif

%description qt5
qpdfview is a tabbed PDF viewer.
It uses the Poppler library for rendering and CUPS for printing.
It provides a clear and simple graphical user interface using the Qt framework.
%endif


%prep
%setup -qc
%patch0 -p0


%build
%if %{with_qt4}
cp -a %{name}-%{version}%{?prerelease} build-qt4
pushd build-qt4
lrelease-qt4 qpdfview.pro
%{qmake_qt4} \
    PLUGIN_INSTALL_PATH="%{_libdir}/%{name}" \
    DATA_INSTALLPATH="%{_datadir}/%{name}" \
%if 0%{?rhel}
    CONFIG+=without_djvu \
%endif
    qpdfview.pro
make %{?_smp_mflags}
popd
%endif

%if %{with_qt5} 
cp -a %{name}-%{version}%{?prerelease} build-qt5
pushd build-qt5
lrelease-qt5 qpdfview.pro
# Some adjustments to avoid conflict with Qt4 package
sed -i "s/TARGET = qpdfview/TARGET = qpdfview-qt5/g" application.pro
sed -i "s,DESKTOP_FILE = miscellaneous/qpdfview.desktop,DESKTOP_FILE = miscellaneous/qpdfview-qt5.desktop,g" application.pro
sed "s/Exec=qpdfview/Exec=qpdfview-qt5/g" miscellaneous/qpdfview.desktop.in  > miscellaneous/qpdfview-qt5.desktop.in
sed -i "s/Name=qpdfview/Name=qpdfview (Qt5)/g" miscellaneous/qpdfview-qt5.desktop.in
%{qmake_qt5} \
    PLUGIN_INSTALL_PATH="%{_libdir}/%{name}-qt5" \
    DATA_INSTALLPATH="%{_datadir}/%{name}" \
%if 0%{?rhel}
    CONFIG+=without_djvu \
%endif
    qpdfview.pro
make %{?_smp_mflags}
popd
%endif


%install
%if %{with_qt4} 
pushd build-qt4
make INSTALL_ROOT=%{buildroot} install
popd
%endif

%if %{with_qt5}
pushd build-qt5
make INSTALL_ROOT=%{buildroot} install
popd
%endif

%find_lang %{name} --with-qt --without-mo
# Common files are equal for both Qt4 and Qt5
cd %{name}-%{version}%{?prerelease}
install -Dm 0644 icons/%{name}.svg %{buildroot}%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg
%if %{with_qt4}
desktop-file-validate %{buildroot}/%{_datadir}/applications/%{name}.desktop
%endif
%if %{with_qt5}
desktop-file-validate %{buildroot}/%{_datadir}/applications/%{name}-qt5.desktop
%endif
# unknown language (epel7..9, f34)
%if 0%{?rhel} || 0%{?fedora} <= 34
    rm -f %{buildroot}/%{_datadir}/%{name}/%{name}_ast.qm
%endif


%if %{with_qt4}
%ldconfig_scriptlets
%endif


%if %{with_qt5}
# Scriptlets qt5 subpackage
%ldconfig_scriptlets qt5
%endif


%if %{with_qt4}
%files qt4
%{_bindir}/%{name}
%{_libdir}/%{name}
%{_datadir}/applications/%{name}.desktop
%endif

%if %{with_qt5}
%files qt5
%{_bindir}/%{name}-qt5
%{_libdir}/%{name}-qt5
%{_datadir}/applications/%{name}-qt5.desktop
%endif

%files common -f %{name}.lang
%license %{name}-%{version}%{?prerelease}/COPYING
%doc %{name}-%{version}%{?prerelease}/CHANGES %{name}-%{version}%{?prerelease}/CONTRIBUTORS %{name}-%{version}%{?prerelease}/README %{name}-%{version}%{?prerelease}/TODO
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/help*.html
%{_datadir}/appdata/%{name}.appdata.xml
%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg
%{_mandir}/man?/*

%changelog
* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.18-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jan 24 2022 TI_Eugene <ti.eugene@gmail.com> - 0.4.18-9
- EPEL8..9 fix

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.18-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Aug 18 2021 TI_Eugene <ti.eugene@gmail.com> - 0.4.18-8
- F35 fix

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.18-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.18-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jan 06 2021 TI_Eugene <ti.eugene@gmail.com> - 0.4.18-5
- Move Qt4 things into qpdfview-qt4 subpackage
- Disable Qt4 version for F34

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.18-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.18-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jan 17 2020 Marek Kasik <mkasik@redhat.com> - 0.4.18-2
- Rebuild for poppler-0.84.0

* Sat Aug 17 2019 Zamir SUN <sztsian@gmail.com - 0.4.18-1
- Update to 0.4.18

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.17-0.10.beta1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.17-0.9.beta1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.17-0.8.beta1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Mar 23 2018 Marek Kasik <mkasik@redhat.com> - 0.4.17-0.7.beta1
- Rebuild for poppler-0.63.0

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.17-0.6.beta1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Jan 20 2018 Björn Esser <besser82@fedoraproject.org> - 0.4.17-0.5.beta1
- Rebuilt for switch to libxcrypt

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.17-0.4.beta1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.17-0.3.beta1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.17-0.2.beta1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Jan 12 2017 Christian Dersch <lupinix@mailbox.org> - 0.4.17-0.1.beta1
- new version
- added Qt5 build
- added missing scriptlets for icon cache and desktop-database

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.16-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Feb 02 2016 Rex Dieter <rdieter@fedoraproject.org> - 0.4.16-2
- use %%qmake_qt4 macro to ensure proper build flags

* Thu Jan 07 2016 TI_Eugene <ti.eugene@gmail.com> 0.4.16-1
- Version bump

* Fri Oct 09 2015 TI_Eugene <ti.eugene@gmail.com> 0.4.15-1
- Version bump

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.13-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 0.4.13-2
- Rebuilt for GCC 5 C++11 ABI change

* Tue Nov 18 2014 TI_Eugene <ti.eugene@gmail.com> 0.4.13-1
- Version bump

* Mon Oct 06 2014 TI_Eugene <ti.eugene@gmail.com> 0.4.12-1
- Version bump

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Mon Jul 21 2014 TI_Eugene <ti.eugene@gmail.com> 0.4.11-1
- Version bump

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon May 05 2014 TI_Eugene <ti.eugene@gmail.com> 0.4.10-1
- Version bump

* Sun Mar 23 2014 TI_Eugene <ti.eugene@gmail.com> 0.4.9-1
- Version bump

* Thu Jan 30 2014 TI_Eugene <ti.eugene@gmail.com> 0.4.8-1
- Version bump

* Sun Dec 08 2013 TI_Eugene <ti.eugene@gmail.com> 0.4.7-1
- Version bump

* Sun Oct 13 2013 TI_Eugene <ti.eugene@gmail.com> 0.4.6-1
- Version bump

* Fri Sep 06 2013 TI_Eugene <ti.eugene@gmail.com> 0.4.5-1
- Version bump

* Tue Jul 30 2013 TI_Eugene <ti.eugene@gmail.com> 0.4.4-1
- Version bump

* Sun May 26 2013 TI_Eugene <ti.eugene@gmail.com> 0.4.3-1
- Version bump
- Translations added
- post/postun ldconfig added

* Mon Mar 25 2013 TI_Eugene <ti.eugene@gmail.com> 0.4.1-1
- New version
- License changed to GPLv2+

* Sat Mar 23 2013 TI_Eugene <ti.eugene@gmail.com> 0.4-1
- initial packaging for Fedora
