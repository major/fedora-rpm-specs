%global	priority	65-3
%global	ppriority	65-2
%global	fontname	vlgothic
%global	archivename	VLGothic-%{version}
%global	fontconf	%{priority}-%{fontname}-gothic
%global	pfontconf	%{ppriority}-%{fontname}-pgothic
%global	common_desc	\
VLGothic provides Japanese TrueType fonts from the Vine Linux project.\
Most of the glyphs are taken from the M+ and Sazanami Gothic fonts,\
but some have also been improved by the project.

Name:		%{fontname}-fonts
Version:	20141206
Release:	21%{?dist}
Summary:	Japanese TrueType font

License:	mplus and BSD
URL:		http://dicey.org/vlgothic
Source0:	http://osdn.dl.sourceforge.jp/vlgothic/62375/%{archivename}.tar.bz2
Source1:	%{name}-fontconfig-pgothic.conf
Source2:	%{name}-fontconfig-gothic.conf
Source3:        %{fontname}.metainfo.xml
Source4:        %{fontname}-proportional.metainfo.xml
Patch0:		%{name}-1331050.patch
Patch1:		%{name}-p-1331050.patch

BuildArch:	noarch
BuildRequires:	fontpackages-devel libappstream-glib
BuildRequires:	fonttools

Requires:	fontpackages-filesystem
Obsoletes:	%{name}-common < 20121230-2
Provides:	%{name}-common = %{version}-%{release}
%description
%common_desc

This package provides the monospace VLGothic font.


%package -n	%{fontname}-p-fonts
Summary:	Proportional Japanese TrueType font
Requires:	fontpackages-filesystem
Obsoletes:	%{name}-common < 20121230-2
Provides:	%{name}-common = %{version}-%{release}

%description -n	%{fontname}-p-fonts
%common_desc

This package provides the VLGothic font with proportional glyphs for some
non-Japanese characters.

%prep
%setup -q -n VLGothic


%build
#rhbz#1331050: reassign U+23F4 and U+23F5 each other.
ttx -i -a -e VL-Gothic-Regular.ttf
ttx -i -a -e VL-PGothic-Regular.ttf
sed -ie 's/<!--.*-->//g' VL-Gothic-Regular.ttx
sed -ie 's/<!--.*-->//g' VL-PGothic-Regular.ttx
patch -b -z .1331050 VL-Gothic-Regular.ttx %{PATCH0}
patch -b -z .1331050 VL-PGothic-Regular.ttx %{PATCH1}
touch -r VL-Gothic-Regular.ttf VL-Gothic-Regular.ttx
touch -r VL-PGothic-Regular.ttf VL-PGothic-Regular.ttx
rm VL-Gothic-Regular.ttf
rm VL-PGothic-Regular.ttf
ttx -b VL-Gothic-Regular.ttx
ttx -b VL-PGothic-Regular.ttx
touch -r VL-Gothic-Regular.ttx VL-Gothic-Regular.ttf
touch -r VL-PGothic-Regular.ttx VL-PGothic-Regular.ttf

%{nil}

%install
install -m 0755 -d $RPM_BUILD_ROOT%{_fontdir}
install -m 0644 -p *.ttf $RPM_BUILD_ROOT%{_fontdir}

install -m 0755 -d	$RPM_BUILD_ROOT%{_fontconfig_templatedir} \
			$RPM_BUILD_ROOT%{_fontconfig_confdir}

install -m 0644 -p %{SOURCE1} $RPM_BUILD_ROOT%{_fontconfig_templatedir}/%{pfontconf}.conf
install -m 0644 -p %{SOURCE2} $RPM_BUILD_ROOT%{_fontconfig_templatedir}/%{fontconf}.conf

for fconf in %{pfontconf}.conf %{fontconf}.conf; do
	ln -s %{_fontconfig_templatedir}/$fconf $RPM_BUILD_ROOT%{_fontconfig_confdir}/$fconf
done

# Add AppStream metadata
install -Dm 0644 -p %{SOURCE3} \
        %{buildroot}%{_metainfodir}/%{fontname}.metainfo.xml
install -Dm 0644 -p %{SOURCE4} \
        %{buildroot}%{_metainfodir}/%{fontname}-proportional.metainfo.xml

%check
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/*.metainfo.xml

%_font_pkg -f %{fontconf}.conf VL-Gothic-Regular.ttf
%doc README*
%license LICENSE*
%{_metainfodir}/%{fontname}.metainfo.xml

%_font_pkg -n p -f %{pfontconf}.conf VL-PGothic-Regular.ttf
%doc README*
%license LICENSE*
%{_metainfodir}/%{fontname}-proportional.metainfo.xml

%changelog
* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 20141206-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 20141206-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 20141206-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 20141206-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 20141206-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 20141206-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 20141206-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Jun  5 2019 Akira TAGOH <tagoh@redhat.com> - 20141206-14
- Install metainfo files under %%{_metainfodir}.

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 20141206-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Jul 18 2018 Akira TAGOH <tagoh@redhat.com> - 20141206-12
- Update the fontconfig priority again.

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 20141206-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 20141206-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Jan 22 2018 Akira TAGOH <tagoh@redhat.com> - 20141206-9
- Set the lower priority to change the default font to Noto.

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 20141206-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 20141206-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon May  9 2016 Akira TAGOH <tagoh@redhat.com> - 20141206-6
- Reassign U+23F4 and U+23F5. (#1331050)

* Mon Feb 29 2016 Parag Nemade <pnemade AT redhat DOT com> - 20141206-4
- Fix vlpgothic font metainfo file to showup font correctly in gnome-software
- Clean the spec file to current packaging guidelines

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 20141206-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20141206-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Dec 11 2014 Akira TAGOH <tagoh@redhat.com> - 20141206-1
- New upstream release. (#1172665)

* Fri Nov 07 2014 Parag Nemade <pnemade AT redhat DOT com> - 20140801-2
- Add metainfo file to show this font in gnome-software

* Mon Aug  4 2014 Akira TAGOH <tagoh@redhat.com> - 20140801-1
- New upstream release. (#1125906)

* Tue Jun 10 2014 Akira TAGOH <tagoh@redhat.com> - 20140530-1
- New upstream release. (#1103265)

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20130607-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20130607-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon Jun 10 2013 Akira TAGOH <tagoh@redhat.com> - 20130607-1
- New upstream release. (#972223)

* Fri May 24 2013 Akira TAGOH <tagoh@redhat.com> - 20130510-2
- Work around unnecessary leading whitespace in the pattern. (#966785)

* Mon May 13 2013 Akira TAGOH <tagoh@redhat.com> - 20130510-1
- New upstream release (#956040)

* Wed Feb 20 2013 Akira TAGOH <tagoh@redhat.com> - 20121230-4
- Drop more older Obsoletes and Provides line.

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20121230-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jan 11 2013 Akira TAGOH <tagoh@redhat.com> - 20121230-2
- Drop -common package and keep consistent state of the directory
  by using the macro. (#893789)
- Drop old Obsoletes and Provides line.

* Fri Jan  4 2013 Akira TAGOH <tagoh@redhat.com> - 20121230-1
- New upstream release. (#890992)

* Fri Nov 23 2012 Akira TAGOH <tagoh@redhat.com> - 20121109-2
- the spec file cleanup

* Fri Nov 16 2012 Akira TAGOH <tagoh@redhat.com> - 20121109-1
- New upstream release. (#874981)

* Mon Oct  1 2012 Akira TAGOH <tagoh@redhat.com> - 20120928-1
- New upstream release. (#861431)

* Thu Sep  6 2012 Akira TAGOH <tagoh@redhat.com> - 20120905-1
- New upstream release. (#854525)

* Wed Aug 29 2012 Akira TAGOH <tagoh@redhat.com> - 20120829-1
- New upstream release. (#852673)

* Mon Aug 27 2012 Akira TAGOH <tagoh@redhat.com> - 20120827-1
- New upstream release. (#851879)

* Sun Jul 22 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20120629-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Jul  2 2012 Akira TAGOH <tagoh@redhat.com> - 20120629-1
- New upstream release.

* Mon Jun 18 2012 Akira TAGOH <tagoh@redhat.com> - 20120618-1
- New upstream release.

* Mon Jun 11 2012 Akira TAGOH <tagoh@redhat.com> - 20120610-1
- New upstream release.

* Sun Mar 25 2012 Akira TAGOH <tagoh@redhat.com> - 20120325-1
- New upstream release.

* Wed Mar 14 2012 Akira TAGOH <tagoh@redhat.com> - 20120312-1
- New upstream release.

* Fri Feb 03 2012 Akira TAGOH <tagoh@redhat.com> - 20120130-1
- New upstream release.

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20111122-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Nov 22 2011 Akira TAGOH <tagoh@redhat.com> - 20111122-1
- New upstream release.

* Mon Jul 25 2011 Akira TAGOH <tagoh@redhat.com> - 20110722-1
- New upstream release.

* Thu Apr 14 2011 Akira TAGOH <tagoh@redhat.com> - 20110414-1
- New upstream release.

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20101218-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Dec 22 2010 Akira TAGOH <tagoh@redhat.com> - 20101218-1
- New upstream release.

* Thu Aug 19 2010 Akira TAGOH <tagoh@redhat.com> - 20100818-1
- New upstream release.

* Wed May 26 2010 Akira TAGOH <tagoh@redhat.com> - 20100416-3
- Improve the fontconfig config file to match ja as well.

* Mon Apr 19 2010 Akira TAGOH <tagoh@redhat.com> - 20100416-2
- Get rid of compare="contains" again.

* Mon Apr 19 2010 Akira TAGOH <tagoh@redhat.com> - 20100416-1
- New upstream release.
- Get rid of binding="same" from the fontconfig config file. (#578048)

* Fri Mar 12 2010 Akira TAGOH <tagoh@redhat.com> - 20100126-2
- Fix the locale-specific overrides rule to match with "ja" as well. (#572841)

* Mon Mar  1 2010 Akira TAGOH <tagoh@redhat.com> - 20100126-1
- New upstream release.
- Set the priority to 65-0 for vlgothic-p-fonts to avoid the effects
  of 65-nonlatin.conf and similarly 65-1 to vlgothic-fonts. (#476459)

* Mon Dec  7 2009 Akira TAGOH <tagoh@redhat.com> - 20091202-1
- New upstream release.
- Set the priority to 65 for vlgothic-p-fonts to override the rule in
  vlgothic-fonts for sans-serif.
- Set the priority to 66 and contains both rules for sans-serif and monospace
  to avoid picking up the unrelated fonts in Live. where doesn't have
  vlgothic-p-fonts installed. (#544957)

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20090612-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon Jun 15 2009 Akira TAGOH <tagoh@redhat.com> - 20090612-1
- New upstream release.

* Thu Apr 23 2009 Akira TAGOH <tagoh@redhat.com> - 20090422-1
- New upstream release.

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20090204-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Tue Feb 10 2009 Akira TAGOH <tagoh@redhat.com> - 20090204-2
- clean up.

* Wed Feb  4 2009 Akira TAGOH <tagoh@redhat.com> - 20090204-1
- New upstream release.
- Update spec file for new packaging policy.
  - Renamed VLGothic-fonts to vlgothic-fonts.
  - Renamed VLGothic-fonts-proportional to vlgothic-p-fonts.
  - Added vlgothic-fonts-common.

* Fri Dec  5 2008 Akira TAGOH <tagoh@redhat.com> - 20081203-2
- update fontconfig config according to Fontconfig packaging tips.

* Thu Dec  4 2008 Akira TAGOH <tagoh@redhat.com> - 20081203-1
- update to 20081203 release.
- clean up spec file.
- changed the priority prefix for fontconfig to 66 according to Fontconfig packaging tips.

* Wed Oct 29 2008 Akira TAGOH <tagoh@redhat.com> - 20081029-1
- update to 20081029 release.

* Tue Sep  9 2008 Akira TAGOH <tagoh@redhat.com> - 20080908-1
- update to 20080908 release.

* Thu Jul 31 2008 Jens Petersen <petersen@redhat.com> - 20080624-1.fc10
- update to 20080624 release

* Wed May  7 2008 Jens Petersen <petersen@redhat.com> - 20080429-1
- update to 20080429 release
- rename 59-VLGothic-sans.conf to 59-VLGothic-proportional.conf

* Thu Jan 17 2008 Jens Petersen <petersen@redhat.com> - 20071215-2.fc9
- move monospace font to main package and obsolete monospace subpackage
- rename sans subpackage to proportional and obsolete sans subpackage
- use a separate font dir for the proportional font subpackage
- add fc-cache scriptlets and drop superfluous removal of old font config
- drop the docs subpackage
- use fontname, fontdir, and fontconfdir macros
- improve summaries and descriptions
- do not require fontconfig
- drop VLGothic obsoletes and provides

* Sat Jan 12 2008 Ryo Dairiki <ryo-dairiki@users.sourceforge.net> - 20071215-1
- Update to 20071215

* Thu Oct 18 2007 Ryo Dairiki <ryo-dairiki@users.sourceforge.net> - 20071015-2
- Rename the font directory.
- Fix font selection problem in Flash 9.
- Make it remove the old configuration files on updating.

* Thu Oct 18 2007 Ryo Dairiki <ryo-dairiki@users.sourceforge.net> - 20071015-1
- Update to 20071015
- Make it separated into subpackages

* Sun Sep 09 2007 Ryo Dairiki <ryo-dairiki@users.sourceforge.net> - 20070901-1
- Update to 20070901

* Sat Jun 02 2007 Ryo Dairiki <ryo-dairiki@users.sourceforge.net> - 20070507-1
- Update to 20070507

* Sun Apr 22 2007 Ryo Dairiki <ryo-dairiki@users.sourceforge.net> - 20070328-1
- Update to 20070328

* Wed Jan 03 2007 Ryo Dairiki <ryo-dairiki@users.sourceforge.net> - 20070101-1
- Update to 20070101

* Sun Dec 10 2006 Ryo Dairiki <ryo-dairiki@users.sourceforge.net> - 20061026-5
- Decrease the priority of the VLGothic fonts lower than DejaVu fonts.
- Now config files are replaced by every updating.

* Wed Nov 29 2006 Ryo Dairiki <ryo-dairiki@users.sourceforge.net> - 20061026-4
- Fix the mistyped dist tag.

* Sat Nov 18 2006 Ryo Dairiki <ryo-dairiki@users.sourceforge.net> - 20061026-3
- Modify the specfile along with the Fedora Extras packaging policy.

* Sun Nov 12 2006 Ryo Dairiki <ryo-dairiki@users.sourceforge.net> - 20061026-2
- Modify the specfile.

* Sun Nov 12 2006 Ryo Dairiki <ryo-dairiki@users.sourceforge.net> - 20061026-1
- Preparing for Fedora Extras.

* Sat Oct 28 2006 Ryo Dairiki <ryo-dairiki@users.sourceforge.net> - 20061021-2
- Update to 20061021.

* Tue Sep 19 2006 Ryo Dairiki <ryo-dairiki@users.sourceforge.net> - 20060913-2
- Update to 20060913.

* Thu Aug 31 2006 Ryo Dairiki <ryo-dairiki@users.sourceforge.net> - 20060831-1
- Initial packaging.
