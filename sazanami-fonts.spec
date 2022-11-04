%global	priority	70
%global	fontname	sazanami
%global	fontconf	%{priority}-%{fontname}
%global catalogue	%{_sysconfdir}/X11/fontpath.d
%global	common_desc	\
The Sazanami type faces are automatically generated from Wadalab font kit.\
They also contains some embedded Japanese bitmap fonts.

Name:		%{fontname}-fonts
Version:	0.20040629
Release:	41%{?dist}
BuildArch:	noarch
BuildRequires:	ttmkfdir >= 3.0.6
BuildRequires:	mkfontdir xorg-x11-fonts-misc >= 7.5-11
BuildRequires:	fontpackages-devel
BuildRequires:	fonttools
URL:		http://efont.sourceforge.jp/

Source0:	http://globalbase.dl.sourceforge.jp/efont/10087/sazanami-20040629.tar.bz2
Source1:	fonts.alias.sazanami-gothic
Source2:	fonts.alias.sazanami-mincho
Source3:	%{fontname}-gothic-fontconfig.conf
Source4:	%{fontname}-mincho-fontconfig.conf
Patch1:		uni7E6B-gothic.patch
Patch2:		uni7E6B-mincho.patch
Patch3:		uni8449-mincho.patch

Summary:	Sazanami Japanese TrueType fonts
License:	BSD

%description
%common_desc

%package	common
Summary:	Common files for Sazanami Japanese TrueType fonts
Requires:	fontpackages-filesystem

%description	common
%common_desc

This package consists of files used by other %{name} packages.

%package -n	%{fontname}-gothic-fonts
Summary:	Sazanami Gothic Japanese TrueType font
License:	BSD
Requires:	%{name}-common = %{version}-%{release}

%description -n	%{fontname}-gothic-fonts
%common_desc

This package contains Japanese TrueType font for Gothic type face.

%package -n	%{fontname}-mincho-fonts
Summary:	Sazanami Mincho Japanese TrueType font
License:	BSD
Requires:	%{name}-common = %{version}-%{release}

%description -n	%{fontname}-mincho-fonts
%common_desc

This package contains Japanese TrueType font for Mincho type face.

%prep
%setup -q -n sazanami-20040629

%build
#rhbz#196433: modify the ttfs to change the glyph for 0x7E6B
ttx -i -a -e sazanami-gothic.ttf
patch -b -z .uni7E6B sazanami-gothic.ttx %{PATCH1}
touch -r sazanami-gothic.ttf sazanami-gothic.ttx
rm sazanami-gothic.ttf
ttx -b sazanami-gothic.ttx
touch -r sazanami-gothic.ttx sazanami-gothic.ttf

ttx -i -a -e sazanami-mincho.ttf
patch -b -z .uni7E6B sazanami-mincho.ttx %{PATCH2}
patch -b -z .uni8449 sazanami-mincho.ttx %{PATCH3}
touch -r sazanami-mincho.ttf sazanami-mincho.ttx
rm sazanami-mincho.ttf
ttx -b sazanami-mincho.ttx
touch -r sazanami-mincho.ttx sazanami-mincho.ttf

%install
rm -rf $RPM_BUILD_ROOT

install -dm 0755 $RPM_BUILD_ROOT%{_fontdir}/{gothic,mincho}
install -pm 0644 sazanami-gothic.ttf $RPM_BUILD_ROOT%{_fontdir}/gothic
install -pm 0644 sazanami-mincho.ttf $RPM_BUILD_ROOT%{_fontdir}/mincho

install -dm 0755 $RPM_BUILD_ROOT%{_fontconfig_templatedir} \
		 $RPM_BUILD_ROOT%{_fontconfig_confdir}
install -pm 0644 %{SOURCE3} $RPM_BUILD_ROOT%{_fontconfig_templatedir}/%{fontconf}-gothic.conf
install -pm 0644 %{SOURCE4} $RPM_BUILD_ROOT%{_fontconfig_templatedir}/%{fontconf}-mincho.conf

for fontconf in %{fontconf}-gothic.conf %{fontconf}-mincho.conf; do
	ln -s %{_fontconfig_templatedir}/$fontconf $RPM_BUILD_ROOT%{_fontconfig_confdir}/$fontconf
done

install -dm 0755 $RPM_BUILD_ROOT%{catalogue}
install -pm 0644 %{SOURCE1} $RPM_BUILD_ROOT%{_fontdir}/gothic/fonts.alias
install -pm 0644 %{SOURCE2} $RPM_BUILD_ROOT%{_fontdir}/mincho/fonts.alias

# Create fonts.scale and fonts.dir
ttmkfdir -d $RPM_BUILD_ROOT%{_fontdir}/gothic -o $RPM_BUILD_ROOT%{_fontdir}/gothic/fonts.scale
mkfontdir $RPM_BUILD_ROOT%{_fontdir}/gothic
ttmkfdir -d $RPM_BUILD_ROOT%{_fontdir}/mincho -o $RPM_BUILD_ROOT%{_fontdir}/mincho/fonts.scale
mkfontdir $RPM_BUILD_ROOT%{_fontdir}/mincho

# Install catalogue symlink
ln -sf %{_fontdir}/gothic $RPM_BUILD_ROOT%{catalogue}/%{name}-gothic
ln -sf %{_fontdir}/mincho $RPM_BUILD_ROOT%{catalogue}/%{name}-mincho


%_font_pkg -n gothic -f %{fontconf}-gothic.conf gothic/sazanami-gothic.ttf

%dir %{_fontdir}/gothic
%{catalogue}/%{name}-gothic
%verify(not md5 size mtime) %{_fontdir}/gothic/fonts.dir
%verify(not md5 size mtime) %{_fontdir}/gothic/fonts.scale
%verify(not md5 size mtime) %{_fontdir}/gothic/fonts.alias

%_font_pkg -n mincho -f %{fontconf}-mincho.conf mincho/sazanami-mincho.ttf

%dir %{_fontdir}/mincho
%{catalogue}/%{name}-mincho
%verify(not md5 size mtime) %{_fontdir}/mincho/fonts.dir
%verify(not md5 size mtime) %{_fontdir}/mincho/fonts.scale
%verify(not md5 size mtime) %{_fontdir}/mincho/fonts.alias

%files common
%doc doc README
%dir %{_fontdir}

%changelog
* Wed Nov  2 2022 Akira TAGOH <tagoh@redhat.com> - 0.20040629-41
- Drop old dependencies.
- Fix validation error in fontconfig config files.

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.20040629-40
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.20040629-39
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.20040629-38
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.20040629-37
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.20040629-36
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.20040629-35
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.20040629-34
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Feb 12 2019 Kalev Lember <klember@redhat.com> - 0.20040629-33
- Avoid hardcoding ttmkfdir and mkfontdir prefix

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.20040629-32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.20040629-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.20040629-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Jan 22 2018 Akira TAGOH <tagoh@redhat.com> - 0.20040629-29
- Update the priority to change the default font to Noto.

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.20040629-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.20040629-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Mar 07 2016 Parag Nemade <pnemade AT redhat DOT com> - 0.20040629-26
- Build against new fonttools-3.0-4 build

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.20040629-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Jan  4 2016 Akira TAGOH <tagoh@redhat.com>
- Use %%global instead of %%define.

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.20040629-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Nov  4 2014 Akira TAGOH <tagoh@redhat.com> - 0.20040629-23
- Rebuilt to get the proper fonts.scale with fixed xorg-x11-fonts-misc. (#1007493)

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.20040629-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.20040629-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.20040629-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.20040629-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed Jul  4 2012 Akira TAGOH <tagoh@redhat.com> - 0.20040629-18
- Correct fontconfig config file. (#837532)

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.20040629-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Thu Aug 25 2011 Akira TAGOH <tagoh@redhat.com> - 0.20040629-16
- Add xorg-x11-fonts-misc to BR. (#733106)

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.20040629-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Jun 23 2010 Akira TAGOH <tagoh@redhat.com> - 0.20040629-14
- Fix the broken outline path of U+8449 in sazanami-mincho. (#606876)

* Tue May 25 2010 Akira TAGOH <tagoh@redhat.com> - 0.20040629-13
- Improve the fontconfig config file to match ja as well.

* Mon Apr 19 2010 Akira TAGOH <tagoh@redhat.com> - 0.20040629-12
- Get rid of compare="contains".

* Mon Apr 19 2010 Akira TAGOH <tagoh@redhat.com> - 0.20040629-11
- Get rid of binding="same" from the fontconfig config file. (#578045)

* Tue Oct  6 2009 Akira TAGOH <tagoh@redhat.com> - 0.20040629-9
- keeps the original timestamps for TTFs.

* Mon Oct 05 2009 Caolán McNamara <caolanm@redhat.com> 
- use ttx and rebuild the font by merging the original .ttfs with the
  custom replacement uni7E6B glyphs

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.20040629-8.20061016
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.20040629-7.20061016
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Wed Jan 28 2009 Akira TAGOH <tagoh@redhat.com> - 0.20040629-6.20061016
- Rename the package name again.

* Thu Dec 25 2008 Akira TAGOH <tagoh@redhat.com> - 0.20040629-5.20061016
- Update the spec file to fit into new guideline. (#477453)

* Tue Aug 28 2007 Jens Petersen <petersen@redhat.com> - 0.20040629-4.20061016
- use the standard font scriptlets (#259041)

* Thu Aug 23 2007 Akira TAGOH <tagoh@redhat.com> - 0.20040629-3.20061016
- Update %%description.
- Separate package for gothic and mincho.

* Fri Aug 17 2007 Akira TAGOH <tagoh@redhat.com> - 0.20040629-1.20061016
- Split sazanami*ttf up from fonts-japanese.

