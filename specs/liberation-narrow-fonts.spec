%global priority 59
%global fontname liberation-narrow
%global fontconf %{priority}-%{fontname}.conf
%global catalogue %{_sysconfdir}/X11/fontpath.d

Name:		%{fontname}-fonts
Summary:	Sans-serif Narrow fonts to replace commonly used Microsoft Arial Narrow
Version:	1.07.6
Release:	17%{?dist}
Epoch:		2
# The license of the Liberation Fonts is a EULA that contains GPLv2 and two
# exceptions:
# The first exception is the standard FSF font exception.
# The second exception is an anti-lockdown clause somewhat like the one in
# GPLv3. This license is Free, but GPLv2 and GPLv3 incompatible.
License:	LicenseRef-Liberation
URL:		https://github.com/liberationfonts/liberation-sans-narrow
Source0:	%{url}/files/2579431/%{name}-ttf-%{version}.tar.gz
Source1:	%{name}.conf
Source2:	%{name}.metainfo.xml
BuildArch:	noarch
BuildRequires:	fontpackages-devel
BuildRequires:	mkfontscale mkfontdir
BuildRequires:	libappstream-glib
Requires:	fontpackages-filesystem

%description
The Liberation Sans Narrow Fonts are intended to be replacements for
the Arial Narrow.

%prep
%autosetup -n %{name}-ttf-%{version}


%build

%install
# fonts .ttf
install -m 0755 -d %{buildroot}%{_fontdir}
install -m 0644 -p *.ttf %{buildroot}%{_fontdir}

# catalogue
install -m 0755 -d %{buildroot}%{catalogue}
ln -s %{_fontdir} %{buildroot}%{catalogue}/%{name}

# fonts.{dir,scale}
mkfontscale %{buildroot}%{_fontdir}
mkfontdir %{buildroot}%{_fontdir}

install -m 0755 -d %{buildroot}%{_fontconfig_templatedir} \
		%{buildroot}%{_fontconfig_confdir}
install -m 0644 -p %{SOURCE1} \
		%{buildroot}%{_fontconfig_templatedir}/%{fontconf}
install -Dm 0644 -p %{SOURCE2} \
	%{buildroot}%{_datadir}/metainfo/%{fontname}.metainfo.xml

ln -s %{_fontconfig_templatedir}/%{fontconf} \
		%{buildroot}%{_fontconfig_confdir}/%{fontconf}


%check
appstream-util validate-relax --nonet \
	%{buildroot}%{_datadir}/metainfo/%{fontname}.metainfo.xml

%_font_pkg -f %{fontconf} *.ttf

%doc AUTHORS ChangeLog COPYING README.rst TODO
%license License.txt
%{_datadir}/metainfo/%{fontname}.metainfo.xml
%verify(not md5 size mtime) %{_fontdir}/fonts.dir
%verify(not md5 size mtime) %{_fontdir}/fonts.scale
%{catalogue}/%{name}

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2:1.07.6-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2:1.07.6-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Mon Jun 17 2024 Parag Nemade <pnemade AT redhat DOT com> - 2:1.07.6-15
- Move this package to use binary font files instead of source SFD files

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2:1.07.6-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2:1.07.6-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Aug 21 2023 Parag Nemade <pnemade AT fedoraproject DOT org> - 2:1.07.6-12
- Migrate to SPDX license expression

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2:1.07.6-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2:1.07.6-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2:1.07.6-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2:1.07.6-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2:1.07.6-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Thu Mar 04 2021 Peter Hutterer <peter.hutterer@redhat.com> 2:1.07.6-6
- Require mkfontscale and mkfontdir directly, not xorg-x11-font-utils
  (#1933537)

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2:1.07.6-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2:1.07.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2:1.07.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Sep 4 2019 Vishal Vijayraghavan<vishalvijayraghavan@gmail.com> - 2:1.07.6-2
- Resolves:rh#1747737 packages with conflicts

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.07.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.07.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Jul 23 2018 Vishal Vijayraghavan<vishalvijayraghavan@gmail.com> - 1.07.5-1
- new release since liberation-narrow font is seperted from liberation 1.x

* Fri Nov 23 2012 Pravin Satpute <psatpute@redhat.com> - 1.07.2-10
- added fontpackages-filesystem in requires

* Thu Nov 22 2012 Pravin Satpute <psatpute@redhat.com> - 1.07.2-9
- spec file clean up

* Thu Jul 26 2012 Pravin Satpute <psatpute@redhat.com> - 1.07.2-8
- updated as per pkg review comments #840878

* Tue Jul 17 2012 Pravin Satpute <psatpute@redhat.com> - 1.07.2-7
- Initial release after splitting it from liberation-fonts tarball due to license incompatibility.
