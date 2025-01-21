Name:           x2godesktopsharing
Version:        3.2.0.0
Release:        16%{?dist}
Summary:        Share X11 desktops with other users via X2Go

# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
URL:            https://www.x2go.org
Source0:        https://code.x2go.org/releases/source/%{name}/%{name}-%{version}.tar.gz

BuildRequires: make
BuildRequires:  desktop-file-utils
BuildRequires:  qt5-qtbase-devel
BuildRequires:  qt5-qtsvg-devel
BuildRequires:  qt5-linguist
Requires:       hicolor-icon-theme
Requires:       x2goserver >= 4.0.0.0
%if 0%{?fedora}
Recommends:     x2goserver-desktopsharing >= 4.1.0.3
%else
Requires:       x2goserver-desktopsharing >= 4.1.0.3
%endif


%description
X2Go Desktop Sharing is an X2Go add-on tool that allows a user to 
grant other X2Go users access to the current session (shadow session
support). The current session may be an X2Go session itself or simply
a local X11 session.


%prep
%setup -q


%build
lrelease-qt5 x2godesktopsharing.pro
%{qmake_qt5}
%make_build


%install
mkdir -p %{buildroot}%{_bindir} %{buildroot}%{_datadir}/{applications,x2go}
cp -p %{name} %{buildroot}%{_bindir}/
desktop-file-install --dir %{buildroot}%{_datadir}/applications %{name}.desktop
mkdir -p %{buildroot}%{_datadir}/%{name}/icons
install -p -m 644 icons/%{name}.xpm %{buildroot}%{_datadir}/%{name}/icons/%{name}.xpm
mkdir -p %{buildroot}%{_datadir}/icons/hicolor/{16x16,32x32,64x64,128x128}/apps
install -p -m 644 icons/128x128/%{name}.png %{buildroot}%{_datadir}/icons/hicolor/128x128/apps/%{name}.png
install -p -m 644 icons/16x16/%{name}.png %{buildroot}%{_datadir}/icons/hicolor/16x16/apps/%{name}.png
install -p -m 644 icons/64x64/%{name}.png %{buildroot}%{_datadir}/icons/hicolor/64x64/apps/%{name}.png
install -p -m 644 icons/32x32/%{name}.png %{buildroot}%{_datadir}/icons/hicolor/32x32/apps/%{name}.png
mkdir -p %{buildroot}%{_datadir}/x2go/versions
install -p -m 644 VERSION.x2godesktopsharing %{buildroot}%{_datadir}/x2go/versions/VERSION.x2godesktopsharing
cp -rp man %{buildroot}%{_datadir}/


%pre
# Needed for sharing a desktop with another user
getent group x2godesktopsharing >/dev/null || groupadd -r x2godesktopsharing

%files
%license COPYING
%doc ChangeLog
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/%{name}/
%{_datadir}/icons/hicolor/128x128/apps/%{name}.png
%{_datadir}/icons/hicolor/16x16/apps/%{name}.png
%{_datadir}/icons/hicolor/32x32/apps/%{name}.png
%{_datadir}/icons/hicolor/64x64/apps/%{name}.png
%{_datadir}/x2go/versions/VERSION.x2godesktopsharing
%{_mandir}/man1/%{name}.1.gz


%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.0.0-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 26 2024 Miroslav Suchý <msuchy@redhat.com> - 3.2.0.0-15
- convert license to SPDX

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.0.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.0.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.0.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.0.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.0.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.0.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.0.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.0.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.0.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.0.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.0.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Dec  4 2018 Orion Poplawski <orion@nwra.com> - 3.2.0.0-2
- Add Recommends x2goserver-desktopsharing

* Wed Nov 28 2018 Orion Poplawski <orion@cora.nwra.com> - 3.2.0.0-1
- Update to 3.2.0.0

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.1.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.1.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.1.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.1.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.1.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Jun 7 2016 Orion Poplawski <orion@cora.nwra.com> - 3.1.1.3-1
- Update to 3.1.1.3
- Drop time patch fixed upstream

* Sat Feb 6 2016 Orion Poplawski <orion@cora.nwra.com> - 3.1.1.2-6
- Add patch to fix abs compile error

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.1.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Feb 02 2016 Rex Dieter <rdieter@fedoraproject.org> - 3.1.1.2-4
- use %%qmake_qt4 macro to ensure proper build flags

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.1.1.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 3.1.1.2-2
- Rebuilt for GCC 5 C++11 ABI change

* Tue Mar 10 2015 Orion Poplawski <orion@cora.nwra.com> - 3.1.1.2-1
- Update to 3.1.1.2

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.1.1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.1.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon Mar 31 2014 Orion Poplawski <orion@cora.nwra.com> - 3.1.1.1-1
- Update to 3.1.1.1 (fixes bug #1065575)

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.1.1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Aug 1 2013 Orion Poplawski <orion@cora.nwra.com> - 3.1.1.0-3
- Fix description formatting
- Install scripts with correct permissions
- Fix FSF address

* Thu Aug 1 2013 Orion Poplawski <orion@cora.nwra.com> - 3.1.1.0-2
- Create x2godesktopsharing group
- Preserve timestamps on install
- Update icon cache

* Wed Jul 31 2013 Orion Poplawski <orion@cora.nwra.com> - 3.1.1.0-1
- Update to 3.1.1.0

* Mon Jun 10 2013 Orion Poplawski <orion@cora.nwra.com> - 3.1.0.7-1
- Update to 3.1.0.7

* Wed Feb 6 2013 Orion Poplawski <orion@cora.nwra.com> - 3.1.0.6-1
- Initial Fedora package
