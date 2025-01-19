Summary: Knights flying on ostriches compete against other riders
Name: ostrichriders
Version: 0.6.5
Release: 16%{?dist}
# Automatically converted from old format: GPLv3+ - review is highly recommended.
License: GPL-3.0-or-later
Url: http://www.identicalsoftware.com/ostrichriders
Source: http://www.identicalsoftware.com/ostrichriders/%{name}-%{version}.tgz
BuildRequires: make
BuildRequires: gcc
BuildRequires: gcc-c++
BuildRequires: SFML-devel
BuildRequires: desktop-file-utils
BuildRequires: fontconfig-devel
BuildRequires: pkgconfig
BuildRequires: libappstream-glib
Requires: hicolor-icon-theme

%description
Enemy knights are invading the kingdom. As one of the elite ostrich riders,
it is your duty to defend the kingdom. With lance in hand you fly off.
Remember to stay above your opponent least you fall to his lance. Collect the
eggs least your opponent hatches stronger than before. Work together with
other knights.

%prep
%setup -q

%build
%make_build

%install
%make_install PREFIX=%{_prefix}

%check
appstream-util validate-relax --nonet %{buildroot}/%{_datadir}/appdata/*.appdata.xml

%files
%license LICENCE
%doc README
%{_bindir}/%{name}
%{_datadir}/%{name}/
%{_datadir}/icons/hicolor/*/apps/%{name}.png
%{_datadir}/applications/%{name}.desktop
%{_datadir}/appdata/%{name}.appdata.xml

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.5-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 25 2024 Miroslav Suchý <msuchy@redhat.com> - 0.6.5-15
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.5-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.5-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.5-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Nov 05 2023 Sérgio Basto <sergio@serjux.com> - 0.6.5-11
- Rebuild for SFML-2.6.1

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.5-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.5-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.5-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.5-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.5-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Feb 28 2019 Dennis Payne <dulsi@identicalsoftware.com> - 0.6.5-1
- Add arcade mode.

* Sun Feb 18 2018 Dennis Payne <dulsi@identicalsoftware.com> - 0.6.4-3
- Add build requirement of gcc-c++.

* Fri Sep 16 2016 Dennis Payne <dulsi@identicalsoftware.com> - 0.6.4-2
- Added app data validation
- Used some macros for common tasks
- Require hicolor icon theme
- Mark license file correctly

* Thu Sep 15 2016 Dennis Payne <dulsi@identicalsoftware.com> - 0.6.4-1
- New release.

* Sat Apr 16 2016 Rémi Verschelde <akien@mageia.org> - 0.6.3-2
- Add support for DESTDIR parameter, and overriding BINDIR and PREFIX
- Make binary name lowercase

* Thu Mar 10 2016 Dennis Payne <dulsi@identicalsoftware.com> - 0.6.3-1
- Moved install into the makefile.

* Thu Feb 11 2016 Dennis Payne <dulsi@identicalsoftware.com> - 0.6.2-1
- First ostrich riders spec file.
