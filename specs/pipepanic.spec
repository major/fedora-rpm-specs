Name: pipepanic
Version: 0.1.3
Release: 40%{?dist}
Summary: A pipe connecting game

# Automatically converted from old format: GPLv2+ - review is highly recommended.
License: GPL-2.0-or-later
URL: http://www.users.waitrose.com/~thunor/pipepanic/
Source0: http://www.users.waitrose.com/~thunor/pipepanic/dload/%{name}-%{version}-source.tar.gz
Source1: pipepanic.desktop
# Use standard Fedora CFLAGS to compile
Patch0: pipepanic-0.1.3-Makefile.patch
# Hans de Goede
# Set a window title and icon
Patch1: pipepanic-0.1.3-window-title.patch
# Miroslav Lichvar
# Fix wrong score with long pipes (BZ #847344)
Patch2: pipepanic-0.1.3-score.patch

BuildRequires: make
BuildRequires: gcc
BuildRequires: SDL-devel
BuildRequires: desktop-file-utils
BuildRequires: ImageMagick
Requires: hicolor-icon-theme


%description
Pipepanic is a pipe connecting game using libSDL. Connect as many 
different shaped pipes together as possible within the time given.


%prep
%setup -q -n %{name}-%{version}-source
%patch -P0 -p0
%patch -P1 -p1
%patch -P2 -p1

# Fix file encoding
iconv --from=ISO-8859-1 --to=UTF-8 COPYING-ARTWORK > COPYING-ARTWORK.conv 
mv COPYING-ARTWORK.conv COPYING-ARTWORK

# Fix DATADIR
sed -i 's:/opt/QtPalmtop/share/pipepanic/:%{_datadir}/%{name}/:' main.h


%build
%make_build \
  CFLAGS="%{optflags}" \
  LDFLAGS="%{__global_ldflags}"


%install
# Install binary
mkdir -p %{buildroot}%{_bindir}
install -m 755 pipepanic %{buildroot}%{_bindir}

# Install data files
mkdir -p %{buildroot}%{_datadir}/%{name}
install -m 644 *.bmp %{buildroot}%{_datadir}/%{name}/

# Install window icon (needed by patch1)
convert PipepanicIcon32.png bmp3:- | \
  convert - -fill '#FF00FF' -opaque black -colors 256 \
    -compress none bmp3:icon.bmp
install -m 644 icon.bmp %{buildroot}%{_datadir}/%{name}/

# Install icons
mkdir -p %{buildroot}%{_datadir}/icons/hicolor/{16x16,32x32,48x48,64x64}/apps
install -m 644 PipepanicIcon16.png %{buildroot}%{_datadir}/icons/hicolor/16x16/apps/%{name}.png
install -m 644 PipepanicIcon32.png %{buildroot}%{_datadir}/icons/hicolor/32x32/apps/%{name}.png
install -m 644 PipepanicIcon48.png %{buildroot}%{_datadir}/icons/hicolor/48x48/apps/%{name}.png
install -m 644 PipepanicIcon64.png %{buildroot}%{_datadir}/icons/hicolor/64x64/apps/%{name}.png

# Install desktop file
mkdir -p %{buildroot}%{_datadir}/applications
desktop-file-install \
  --dir %{buildroot}%{_datadir}/applications \
  %{SOURCE1}


%files
%{_bindir}/pipepanic
%{_datadir}/%{name}
%{_datadir}/icons/hicolor/16x16/apps/%{name}.png
%{_datadir}/icons/hicolor/32x32/apps/%{name}.png
%{_datadir}/icons/hicolor/48x48/apps/%{name}.png
%{_datadir}/icons/hicolor/64x64/apps/%{name}.png
%if 0%{?fedora} && 0%{?fedora} < 19
%{_datadir}/applications/fedora-%{name}.desktop
%else
%{_datadir}/applications/%{name}.desktop
%endif
%doc AUTHORS ChangeLog README
%license COPYING COPYING-ARTWORK


%changelog
* Mon Jan 20 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.3-40
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 26 2024 Miroslav Suchý <msuchy@redhat.com> - 0.1.3-39
- convert license to SPDX

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.3-38
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.3-37
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.3-36
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.3-35
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.3-34
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.3-33
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.3-32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.3-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.3-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.3-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.3-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.3-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.3-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.3-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat Feb 24 2018 Andrea Musuruane <musuruan@gmail.com> - 0.1.3-24
- Added gcc dependency
- Fixed LDFLAGS usage
- Added license tag
- Spec file clean up

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.3-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 18 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.1.3-22
- Remove obsolete scriptlets

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.3-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.3-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.3-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.3-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.3-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.3-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.3-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.3-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon Feb 18 2013 Toshio Kuratomi <toshio@fedoraproject.org> - 0.1.3-13
- Remove --vendor from desktop-file-install for F19+ https://fedorahosted.org/fesco/ticket/1077

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.3-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sun Aug 12 2012 Andrea Musuruane <musuruan@gmail.com> 0.1.3-11
- Fixed wrong score with long pipes (BZ #847344)
- Fixed desktop file
- Updated icon cache scriptlets

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.3-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.3-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sun Feb 10 2008 Andrea Musuruane <musuruan@gmail.com> 0.1.3-5
- Rebuild against gcc 4.3

* Sat Oct 06 2007 Andrea Musuruane <musuruan@gmail.com> 0.1.3-4
- Fixed COPYING-ARTWORK file encoding
- Updated icon cache scriptlets to be compliant to new guidelines

* Mon Aug 20 2007 Andrea Musuruane <musuruan@gmail.com> 0.1.3-3
- Changed license due to new guidelines
- Removed %%{?dist} tag from changelog
- Updated icon cache scriptlets to be compliant to new guidelines

* Wed May 02 2007 Andrea Musuruane <musuruan@gmail.com> 0.1.3-2
- Fixed package ownership of its datadir
- Changed description
- Added a patch by Hans de Goede to set a window title and icon

* Sun Apr 08 2007 Andrea Musuruane <musuruan@gmail.com> 0.1.3-1
- Initial release

