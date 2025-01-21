Name:		xedit
Version:	1.2.4
Release:	4%{?dist}
Summary:	Simple text editor for X
URL:		http://xorg.freedesktop.org
Source0:	http://xorg.freedesktop.org/releases/individual/app/%{name}-%{version}.tar.xz
Source1:	%{name}.desktop
# Automatically converted from old format: MIT and BSD - review is highly recommended.
License:	LicenseRef-Callaway-MIT AND LicenseRef-Callaway-BSD
BuildRequires:	libtool make
BuildRequires:	desktop-file-utils
BuildRequires:	libXaw-devel
BuildRequires:	xorg-x11-util-macros
Patch0:		xedit-hunspell.patch
Requires:	xorg-x11-xbitmaps
Requires:	hunspell
Requires:	hunspell-en
Requires:	grep
Requires:	words
Requires:	ctags
Requires:	xorg-x11-fonts-misc
Requires:	xorg-x11-fonts-75dpi
Requires:	xorg-x11-fonts-100dpi

%description
Xedit provides a simple text editor for X.

%prep
%autosetup -p1

%build
%configure --with-lispdir=%{_datadir}/X11/%{name}

%install
make install DESTDIR=${RPM_BUILD_ROOT} INSTALL="install -p"
install -D -m 644 %{SOURCE1} ${RPM_BUILD_ROOT}%{_datadir}/applications/%{name}.desktop
desktop-file-validate ${RPM_BUILD_ROOT}%{_datadir}/applications/%{name}.desktop

%check
make check

%files
%doc AUTHORS ChangeLog COPYING README
%{_bindir}/%{name}
%{_datadir}/X11/%{name}
%{_datadir}/X11/app-defaults/Xedit
%{_datadir}/X11/app-defaults/Xedit-color
%{_datadir}/applications/%{name}.desktop
%{_mandir}/man1/xedit.1*

%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Sep 04 2024 Miroslav Suchý <msuchy@redhat.com> - 1.2.4-3
- convert license to SPDX

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jul 10 2024 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 1.2.4-1
- Update to latest upstream release

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.2-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Tue Jul 25 2023 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 1.2.2-19
- Use hunspell as ispell engine

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.2-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.2-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.2-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.2-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.2-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.2-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.2-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.2-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Feb 21 2015 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 1.2.2-2
- Update to latest upstream release (#1195020).

* Wed Jul 16 2014 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 1.2.1-1
- Update to latest upstream release.
- Remove patches already in upstream.

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sun Jul 22 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat May 26 2012 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 1.2.0-2
- Patch package to not have BSD 4 clause files.
- Write patch to correct 64 bit overflow tests in a compatible license.
- Update extra patches to use the ones submitted upstream.

* Mon May 21 2012 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 1.2.0-1
- Add proper documentation to package.
- Update to latest upstream release.
- Remove patches already in upstream.

* Mon Apr 23 2012 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 1.1.2-1
- Initial xedit spec.
