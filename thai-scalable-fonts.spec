%global fontname thai-scalable
%global fontconf1 90-%{fontname}-synthetic
%global fontconf2 65-0-%{fontname}

%global archivename fonts-tlwg

%global common_desc \
%{archivename} provides a collection of free scalable Thai fonts.

Name:      %{fontname}-fonts
Version:   0.7.3
Release:   4%{?dist}
Summary:   Thai TrueType fonts
License:   GPLv2+ and Bitstream Vera
URL:       http://linux.thai.net/projects/thaifonts-scalable
Source0:   http://linux.thai.net/pub/ThaiLinux/software/%{archivename}/%{archivename}-%{version}.tar.xz
Source1:   %{fontconf1}-garuda.conf
Source2:   %{fontconf1}-kinnari.conf
Source3:   %{fontconf1}-umpush.conf
Source4:   %{fontconf1}-laksaman.conf
Source5:   %{fontconf2}-norasi.conf
Source6:   %{fontconf2}-waree.conf

#Appdata Metainfo
Source11:  %{fontname}-garuda.metainfo.xml
Source12:  %{fontname}-kinnari.metainfo.xml
Source13:  %{fontname}-loma.metainfo.xml
Source14:  %{fontname}-norasi.metainfo.xml
Source15:  %{fontname}-purisa.metainfo.xml
Source16:  %{fontname}-sawasdee.metainfo.xml
Source17:  %{fontname}-tlwgmono.metainfo.xml
Source18:  %{fontname}-tlwgtypewriter.metainfo.xml
Source19:  %{fontname}-tlwgtpist.metainfo.xml
Source20:  %{fontname}-tlwgtypo.metainfo.xml
Source21:  %{fontname}-umpush.metainfo.xml
Source22:  %{fontname}-waree.metainfo.xml
Source23:  %{fontname}-laksaman.metainfo.xml


BuildArch: noarch
BuildRequires: make
BuildRequires: fontforge >= 20071110
BuildRequires: fontpackages-devel

%description
%common_desc

Thai scalable fonts included here are:
- Kinnari, Garuda and Norasi from the National Font project
- DB Thai Text from DearBook
- TlwgMono, PseudoMono, Purisa by TLWG


%package common
Summary:   Common files of %{name}
Requires:  fontpackages-filesystem

%description common
%common_desc

This package consists of files used by other %{name} packages.


%package -n %{fontname}-garuda-fonts
Summary:        Thai Garuda fonts
Requires:       %{name}-common = %{version}-%{release}

%description -n %{fontname}-garuda-fonts
%common_desc

This package provides the Garuda family of Thai fonts.

%_font_pkg -n garuda -f %{fontconf1}-garuda.conf Garuda*.otf
%{_datadir}/appdata/%{fontname}-garuda.metainfo.xml


%package -n %{fontname}-kinnari-fonts
Summary:        Thai Kinnari fonts
Requires:       %{name}-common = %{version}-%{release}

%description -n %{fontname}-kinnari-fonts
%common_desc

This package provides the Kinnari family of Thai fonts.

%_font_pkg -n kinnari -f %{fontconf1}-kinnari.conf Kinnari*.otf
%{_datadir}/appdata/%{fontname}-kinnari.metainfo.xml


%package -n %{fontname}-loma-fonts
Summary:        Thai Loma fonts
Requires:       %{name}-common = %{version}-%{release}

%description -n %{fontname}-loma-fonts
%common_desc

This package provides the Loma family of Thai fonts.

%_font_pkg -n loma Loma*.otf
%{_datadir}/appdata/%{fontname}-loma.metainfo.xml


%package -n %{fontname}-norasi-fonts
Summary:        Thai Norasi fonts
Requires:       %{name}-common = %{version}-%{release}

%description -n %{fontname}-norasi-fonts
%common_desc

This package provides the Norasi family of Thai fonts.

%_font_pkg -n norasi -f %{fontconf2}-norasi.conf Norasi*.otf
%{_datadir}/appdata/%{fontname}-norasi.metainfo.xml


%package -n %{fontname}-purisa-fonts
Summary:        Thai Purisa fonts
Requires:       %{name}-common = %{version}-%{release}

%description -n %{fontname}-purisa-fonts
%common_desc

This package provides the Purisa family of Thai fonts.

%_font_pkg -n purisa Purisa*.otf
%{_datadir}/appdata/%{fontname}-purisa.metainfo.xml


%package -n %{fontname}-sawasdee-fonts
Summary:        Thai Sawasdee fonts
Requires:       %{name}-common = %{version}-%{release}

%description -n %{fontname}-sawasdee-fonts
%common_desc

This package provides the Sawasdee family of Thai fonts.

%_font_pkg -n sawasdee Sawasdee*.otf
%{_datadir}/appdata/%{fontname}-sawasdee.metainfo.xml


%package -n %{fontname}-tlwgmono-fonts
Summary:        Thai TlwgMono fonts
Requires:       %{name}-common = %{version}-%{release}

%description -n %{fontname}-tlwgmono-fonts
%common_desc

This package provides the TlwgMono family of Thai fonts.

%_font_pkg -n tlwgmono TlwgMono*.otf
%{_datadir}/appdata/%{fontname}-tlwgmono.metainfo.xml


%package -n %{fontname}-tlwgtypewriter-fonts
Summary:        Thai TlwgTypewriter fonts
Requires:       %{name}-common = %{version}-%{release}

%description -n %{fontname}-tlwgtypewriter-fonts
%common_desc

This package provides the TlwgTypewriter family of Thai fonts.

%_font_pkg -n tlwgtypewriter TlwgTypewriter*.otf
%{_datadir}/appdata/%{fontname}-tlwgtypewriter.metainfo.xml


%package -n %{fontname}-tlwgtypist-fonts
Summary:        Thai TlwgTypist fonts
Requires:       %{name}-common = %{version}-%{release}

%description -n %{fontname}-tlwgtypist-fonts
%common_desc

This package provides the TlwgTypist family of Thai fonts.

%_font_pkg -n tlwgtypist TlwgTypist*.otf
%{_datadir}/appdata/%{fontname}-tlwgtpist.metainfo.xml


%package -n %{fontname}-tlwgtypo-fonts
Summary:        Thai TlwgTypo fonts
Requires:       %{name}-common = %{version}-%{release}

%description -n %{fontname}-tlwgtypo-fonts
%common_desc

This package provides the TlwgTypo family of Thai fonts.

%_font_pkg -n tlwgtypo TlwgTypo*.otf
%{_datadir}/appdata/%{fontname}-tlwgtypo.metainfo.xml


%package -n %{fontname}-umpush-fonts
Summary:        Thai Umpush fonts
Requires:       %{name}-common = %{version}-%{release}

%description -n %{fontname}-umpush-fonts
%common_desc

This package provides the Umpush family of Thai fonts.

%_font_pkg -n umpush -f %{fontconf1}-umpush.conf Umpush*.otf
%{_datadir}/appdata/%{fontname}-umpush.metainfo.xml

%package -n %{fontname}-laksaman-fonts
Summary:        Thai Laksaman fonts
Requires:       %{name}-common = %{version}-%{release}

%description -n %{fontname}-laksaman-fonts
%common_desc

This package provides the Laksaman family of Thai fonts.

%_font_pkg -n laksaman -f %{fontconf1}-laksaman.conf Laksaman*.otf
%{_datadir}/appdata/%{fontname}-laksaman.metainfo.xml

%package -n %{fontname}-waree-fonts
Summary:        Thai Waree fonts
Requires:       %{name}-common = %{version}-%{release}

%description -n %{fontname}-waree-fonts
%common_desc

This package provides the Waree family of Thai fonts.

%_font_pkg -n waree -f %{fontconf2}-waree.conf Waree*.otf
%{_datadir}/appdata/%{fontname}-waree.metainfo.xml


%prep
%setup -q -n %{archivename}-%{version}


%build
%configure --with-otfdir=%{_fontdir}
make


%install
install -m 0755 -d %{buildroot}%{_fontconfig_templatedir} \
                   %{buildroot}%{_fontconfig_confdir}

make install DESTDIR=%{buildroot} INSTALL="install -p"

# remove upstream font config
# fontconfig's 65-nonlatin.conf covers 65-ttf-thai-tlwg.conf
rm %{buildroot}%{_datadir}/fontconfig/conf.avail/64-15-laksaman.conf
rm %{buildroot}%{_datadir}/fontconfig/conf.avail/64-*-tlwg*.conf
rm %{buildroot}%{_datadir}/fontconfig/conf.avail/89-tlwg*-synthetic.conf

# split up 90-ttf-thai-tlwg-synthetic.conf
install -m 0644 -p %{SOURCE1} \
        %{buildroot}%{_fontconfig_templatedir}/%{fontconf1}-garuda.conf
install -m 0644 -p %{SOURCE2} \
        %{buildroot}%{_fontconfig_templatedir}/%{fontconf1}-kinnari.conf
install -m 0644 -p %{SOURCE3} \
        %{buildroot}%{_fontconfig_templatedir}/%{fontconf1}-umpush.conf
install -m 0644 -p %{SOURCE4} \
        %{buildroot}%{_fontconfig_templatedir}/%{fontconf1}-laksaman.conf

# install 65-0-thai-scalable-*.conf
install -m 0644 -p %{SOURCE5} \
        %{buildroot}%{_fontconfig_templatedir}/%{fontconf2}-norasi.conf
install -m 0644 -p %{SOURCE6} \
        %{buildroot}%{_fontconfig_templatedir}/%{fontconf2}-waree.conf

for fconf in %{fontconf1}-garuda.conf \
             %{fontconf1}-kinnari.conf \
             %{fontconf1}-umpush.conf \
	     %{fontconf1}-laksaman.conf \
	     %{fontconf2}-norasi.conf \
	     %{fontconf2}-waree.conf; do
  ln -s %{_fontconfig_templatedir}/$fconf \
        %{buildroot}%{_fontconfig_confdir}/$fconf
done

# Add AppStream metadata
install -Dm 0644 -p %{SOURCE11} \
        %{buildroot}%{_datadir}/appdata/%{fontname}-garuda.metainfo.xml
install -Dm 0644 -p %{SOURCE12} \
        %{buildroot}%{_datadir}/appdata/%{fontname}-kinnari.metainfo.xml
install -Dm 0644 -p %{SOURCE13} \
        %{buildroot}%{_datadir}/appdata/%{fontname}-loma.metainfo.xml
install -Dm 0644 -p %{SOURCE14} \
        %{buildroot}%{_datadir}/appdata/%{fontname}-norasi.metainfo.xml
install -Dm 0644 -p %{SOURCE15} \
        %{buildroot}%{_datadir}/appdata/%{fontname}-purisa.metainfo.xml
install -Dm 0644 -p %{SOURCE16} \
        %{buildroot}%{_datadir}/appdata/%{fontname}-sawasdee.metainfo.xml
install -Dm 0644 -p %{SOURCE17} \
        %{buildroot}%{_datadir}/appdata/%{fontname}-tlwgmono.metainfo.xml
install -Dm 0644 -p %{SOURCE18} \
        %{buildroot}%{_datadir}/appdata/%{fontname}-tlwgtypewriter.metainfo.xml
install -Dm 0644 -p %{SOURCE19} \
        %{buildroot}%{_datadir}/appdata/%{fontname}-tlwgtpist.metainfo.xml
install -Dm 0644 -p %{SOURCE20} \
        %{buildroot}%{_datadir}/appdata/%{fontname}-tlwgtypo.metainfo.xml
install -Dm 0644 -p %{SOURCE21} \
        %{buildroot}%{_datadir}/appdata/%{fontname}-umpush.metainfo.xml
install -Dm 0644 -p %{SOURCE22} \
        %{buildroot}%{_datadir}/appdata/%{fontname}-waree.metainfo.xml
install -Dm 0644 -p %{SOURCE23} \
        %{buildroot}%{_datadir}/appdata/%{fontname}-laksaman.metainfo.xml

%files common
%doc AUTHORS README COPYING NEWS


%changelog
* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Mon Oct 25 2021 Peng Wu <pwu@redhat.com> - 0.7.3-1
- Update to 0.7.3

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu May  7 2020 Peng Wu <pwu@redhat.com> - 0.7.2-1
- Update to 0.7.2
- Switch to use OpenType Font Format

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.5-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.5-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Jul 17 2019 Peng Wu <pwu@redhat.com> - 0.6.5-5
- Use Waree for sans-serif and Norasi for serif

* Mon Jul 15 2019 Peng Wu <pwu@redhat.com> - 0.6.5-4
- Use Waree as default font for Thai language
- Add 65-0-thai-scalable-waree.conf

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Apr 26 2018 Peng Wu <pwu@redhat.com> - 0.6.5-1
- Update to 0.6.5

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Oct  9 2017 Peng Wu <pwu@redhat.com> - 0.6.4-1
- Update to 0.6.4
- add laksaman subpackage

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Nov 08 2014 Parag Nemade <pnemade AT redhat DOT com> - 0.5.0-9
- Add metainfo file to show this font in gnome-software
- Remove group tag
- Replace %%define with %%global

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Nov 21 2012 Daiki Ueno <dueno@redhat.com> - 0.5.0-5
- change the license field from "GPLv2+" to "GPLv2+ and Bitstream Vera"

* Tue Nov 20 2012 Daiki Ueno <dueno@redhat.com> - 0.5.0-4
- disable X fonts.dir generation
- remove obsolete -compat subpackage
- remove %%defattr from %%files
- add missing "make" in %%build

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jul  5 2012 Daiki Ueno <dueno@redhat.com> - 0.5.0-2
- fix <test> usage in fontconfig files (Closes: #837538)
- refresh fontconfig files with the latest upstream version

* Wed Feb 15 2012 Daiki Ueno <dueno@redhat.com> - 0.5.0-1
- update to 0.5.0
- change %%archivename to fonts-tlwg per upstream

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.17-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Nov  7 2011 Daiki Ueno <dueno@redhat.com> - 0.4.17-1
- update to 0.4.17

* Tue Oct 25 2011 Daiki Ueno <dueno@redhat.com> - 0.4.16-1
- update to 0.4.16

* Tue Mar 22 2011 Daiki Ueno <dueno@redhat.com> - 0.4.15-2
- fix summary of -common subpackage (Bug#688969)

* Thu Mar 17 2011 Daiki Ueno <dueno@redhat.com> - 0.4.15-1
- update to 0.4.15

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.14-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Nov  9 2010 Daiki Ueno <dueno@redhat.com> - 0.4.14-1
- update to 0.4.14
- drop buildroot, %%clean and cleaning of buildroot in %%install
- use only macro style %%buildroot

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.12-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon Jun 22 2009 Jens Petersen <petersen@redhat.com> - 0.4.12-1
- update to 0.4.12 (reported by Manatsawin Hanmongkolchai in #507172)

* Sun Mar 15 2009 Nicolas Mailhot <nicolas.mailhot at laposte.net> - 0.4.11-3
— Make sure F11 font packages have been built with F11 fontforge

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Feb  2 2009 Jens Petersen <petersen@redhat.com> - 0.4.11-1
- update to 0.4.11
- repackage and subpackage for new fontpackages-devel:
- split 90-ttf-thai-tlwg-synthetic.conf per subpackage
- 65-ttf-thai-tlwg.conf is covered by fontconfig 65-nonlatin.conf
- moves docs to common subpackage
- add compat subpackage for upgrades and legacy fonts.*

* Fri Feb  8 2008 Jens Petersen <petersen@redhat.com> - 0.4.9-3
- couple more cleanups (Parag Nemade,#431829):
- use rm instead of /bin/rm
- use install -p

* Fri Feb  8 2008 Jens Petersen <petersen@redhat.com> - 0.4.9-2
- add buildrequires for ttmkfdir and xorg-x11-font-utils (Parag Nemade,#431829)

* Wed Feb  6 2008 Jens Petersen <petersen@redhat.com> - 0.4.9-1
- update to 0.4.9
- spec file cleanup

* Mon Jan 29 2007 Behdad Esfahbod <besfahbo@redhat.com> 0.4.4-1
- Initial package based on package by Theppitak Karoonboonyanan
  and Kamthorn Krairaksa for the OLPC.
