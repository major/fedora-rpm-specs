%global fontname bitmap
%global fontconf 66-%{fontname}
%global common_desc \
The bitmap-fonts package provides a number of bitmap fonts selected\
from the xorg package designed for use locations such as\
terminals.

Name: bitmap-fonts
Version: 0.3
Release: 41%{?dist}
License: GPLv2 and MIT and Lucida
Source0: bitmap-fonts-%{version}.tar.bz2
Source1: fixfont-3.5.tar.bz2
Source2: LICENSE
Source3: 66-bitmap-console.conf
Source4: 66-bitmap-fangsongti.conf
Source5: 66-bitmap-fixed.conf
Source6: 66-bitmap-lucida-typewriter.conf
BuildArch: noarch
Summary: Selected set of bitmap fonts
BuildRequires: bdftopcf fonttosfnt
BuildRequires: fontpackages-devel
BuildRequires: python3
BuildRequires: /usr/bin/ftdump
BuildRequires: make


%description
%common_desc

%package -n %{fontname}-fonts-compat
Summary: Compatibility files of bitmap-font families
Provides: bitmap-fonts = %{version}-%{release}
Requires: %{fontname}-lucida-typewriter-fonts = %{version}-%{release}
Requires: %{fontname}-fangsongti-fonts = %{version}-%{release}
Requires: %{fontname}-console-fonts = %{version}-%{release}
Requires: %{fontname}-fixed-fonts = %{version}-%{release}
Requires: ucs-miscfixed-fonts
Obsoletes: bitmap-fonts < %{version}-%{release}
Conflicts: %{fontname}-opentype-fonts-compat

%description -n %{fontname}-fonts-compat
%common_desc
Meta-package for installing all font families of bitmap.

%files -n %{fontname}-fonts-compat

%package -n %{fontname}-opentype-fonts-compat
Summary:  Compatibility files of bitmap-font families (opentype version)
Requires: %{fontname}-lucida-typewriter-opentype-fonts = %{version}-%{release}
Requires: %{fontname}-fangsongti-opentype-fonts = %{version}-%{release}
Requires: %{fontname}-console-opentype-fonts = %{version}-%{release}
Requires: %{fontname}-fixed-opentype-fonts = %{version}-%{release}
Requires: ucs-miscfixed-opentype-fonts
Conflicts: %{fontname}-fonts-compat

%description -n %{fontname}-opentype-fonts-compat
%common_desc
Meta-package for installing all font families of opentype bitmap.

%files -n %{fontname}-opentype-fonts-compat

%package -n bitmap-lucida-typewriter-fonts
Summary: Selected CJK bitmap fonts for Anaconda
Requires: fontpackages-filesystem
Provides: %{name}-cjk = %{version}-%{release}
License: Lucida
Conflicts: bitmap-lucida-typewriter-opentype-fonts

%description -n bitmap-lucida-typewriter-fonts
%common_desc

%_font_pkg -n lucida-typewriter -f %{fontconf}-lucida-typewriter.conf lut*.pcf.gz
%doc LU_LEGALNOTICE

%package -n bitmap-lucida-typewriter-opentype-fonts
Summary: Selected CJK bitmap fonts for Anaconda (opentype version)
Requires: fontpackages-filesystem
License: Lucida
Conflicts: bitmap-lucida-typewriter-fonts

%description -n bitmap-lucida-typewriter-opentype-fonts
%common_desc

%_font_pkg -n lucida-typewriter-opentype -f %{fontconf}-lucida-typewriter.conf lut*.otb
%doc LU_LEGALNOTICE

%package -n bitmap-fangsongti-fonts
Summary: Selected CJK bitmap fonts for Anaconda
Requires: fontpackages-filesystem
Provides: %{name}-cjk = %{version}-%{release}
License: MIT
Conflicts: bitmap-fangsongti-opentype-fonts

%description -n %{fontname}-fangsongti-fonts
bitmap-fonts-cjk package contains bitmap fonts used by Anaconda. They are
selected from the xorg packages, and the font encoding are converted from 
native encoding to ISO10646. They are only intended to be used in Anaconda.

%_font_pkg -n fangsongti -f %{fontconf}-fangsongti.conf fangsongti*.pcf.gz
%doc LICENSE

%package -n bitmap-fangsongti-opentype-fonts
Summary: Selected CJK bitmap fonts for Anaconda (opentype version)
Requires: fontpackages-filesystem
License: MIT
Conflicts: bitmap-fangsongti-fonts

%description -n %{fontname}-fangsongti-opentype-fonts
%common_desc

%_font_pkg -n fangsongti-opentype -f %{fontconf}-fangsongti.conf fangsongti*.otb
%doc LICENSE

%package -n bitmap-console-fonts
Summary: Selected set of bitmap fonts
Requires: fontpackages-filesystem
License: GPLv2
Conflicts: bitmap-console-opentype-fonts

%description -n %{fontname}-console-fonts
%common_desc

%_font_pkg -n console -f %{fontconf}-console.conf console8x16*.pcf.gz

%package -n bitmap-console-opentype-fonts
Summary: Selected set of bitmap fonts (opentype version)
Requires: fontpackages-filesystem
License: GPLv2
Conflicts: bitmap-console-fonts

%description -n %{fontname}-console-opentype-fonts
%common_desc

%_font_pkg -n console-opentype -f %{fontconf}-console.conf console8x16*.otb

%package -n bitmap-fixed-fonts
Summary: Selected set of bitmap fonts
Requires: fontpackages-filesystem
License: GPLv2
Conflicts: bitmap-fixed-opentype-fonts

%description -n %{fontname}-fixed-fonts
%common_desc

%_font_pkg -n fixed -f %{fontconf}-fixed.conf  console9*.pcf.gz

%package -n bitmap-fixed-opentype-fonts
Summary: Selected set of bitmap fonts (opentype version)
Requires: fontpackages-filesystem
License: GPLv2
Conflicts: bitmap-fixed-fonts

%description -n %{fontname}-fixed-opentype-fonts
%common_desc

%_font_pkg -n fixed-opentype -f %{fontconf}-fixed.conf console9*.otb


%prep
%setup -q -a 1
cp %{SOURCE2} .


%build
%{nil}

%install
rm -rf $RPM_BUILD_ROOT

make install DESTDIR=$RPM_BUILD_ROOT

pushd fixfont-3.5
make install DESTDIR=$RPM_BUILD_ROOT
popd

mv $RPM_BUILD_ROOT/usr/share/fonts/bitmap-fonts %{buildroot}%{_fontdir}

rm %{buildroot}%{_fontdir}/[0-9]*.pcf
rm %{buildroot}%{_fontdir}/console8x8.pcf
rm README

# Convert to OpenType Bitmap Font
rm [0-9]*.bdf fixfont-3.5/[0-9]*.bdf

for bdf in `ls *.bdf`;
do fonttosfnt -b -c -g 2 -m 2 -o ${bdf%%bdf}otb  $bdf;
done
install -m 0644 -p *.otb %{buildroot}%{_fontdir}

pushd fixfont-3.5
for bdf in `ls *.bdf`;
do fonttosfnt -b -c -g 2 -m 2 -o ${bdf%%bdf}otb  $bdf;
done
# For console9x15.otb
fonttosfnt -b -c -g 2 -m 2 -o console9x15.otb console9x15.pcf

install -m 0644 -p *.otb %{buildroot}%{_fontdir}
popd

gzip %{buildroot}%{_fontdir}/*.pcf

install -m 0755 -d %{buildroot}%{_fontconfig_templatedir} \
                   %{buildroot}%{_fontconfig_confdir}

# Repeat for every font family
install -m 0644 -p %{SOURCE3} \
        %{buildroot}%{_fontconfig_templatedir}/%{fontconf}-console.conf

install -m 0644 -p %{SOURCE4} \
        %{buildroot}%{_fontconfig_templatedir}/%{fontconf}-fangsongti.conf

install -m 0644 -p %{SOURCE5} \
        %{buildroot}%{_fontconfig_templatedir}/%{fontconf}-fixed.conf

install -m 0644 -p %{SOURCE6} \
        %{buildroot}%{_fontconfig_templatedir}/%{fontconf}-lucida-typewriter.conf


for fconf in %{fontconf}-console.conf \
             %{fontconf}-fangsongti.conf \
             %{fontconf}-fixed.conf \
             %{fontconf}-lucida-typewriter.conf ; do
  ln -s %{_fontconfig_templatedir}/$fconf \
        %{buildroot}%{_fontconfig_confdir}/$fconf
done


%changelog
* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-41
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-40
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-39
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Mar 02 2021 Parag Nemade <pnemade AT redhat DOT com> - 0.3-38
- Resolves: rhbz#1933563 - Don't BuildRequires xorg-x11-font-utils

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-37
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Dec 29 2020 Peng Wu <pwu@redhat.com> - 0.3-36
- Rebuilt with fonttosfnt 1.2.1

* Fri Sep  4 2020 Peng Wu <pwu@redhat.com> - 0.3-35
- Use BDF fonts for OpenType conversion

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-34
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Feb  6 2020 Peng Wu <pwu@redhat.com> - 0.3-33
- Provide OpenType Bitmap fonts
- Use bitmapfonts2otb.py to combine bitmap fonts
- Add bitmap-*-opentype-fonts sub packages

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.3-28
- Escape macros in %%changelog

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Mar 03 2010 Pravin Satpute <psatpute@redhat.com> - 0.3-16
- fixed lucida license
- added compat package for smooth upgradation

* Tue Mar 02 2010 Pravin Satpute <psatpute@redhat.com> - 0.3-15
- updated as per merge review comments
- bug 225617

* Wed Nov 18 2009 Pravin Satpute <psatpute@redhat.com> - 0.3-14
- removed console8x8.pcf from console sub-package

* Fri Oct 09 2009 Pravin Satpute <psatpute@redhat.com> - 0.3-13
- added lucida-typewriter and fixed subpackage
- removed common subpackage
- added conf file for each subpackage

* Fri Oct 09 2009 Pravin Satpute <psatpute@redhat.com> - 0.3-12
- updates license for each subpackage

* Thu Sep 17 2009 Pravin Satpute <psatpute@redhat.com> - 0.3-11
- second update as per merge review comment, bug 225617

* Thu Sep 17 2009 Pravin Satpute <psatpute@redhat.com> - 0.3-10
- updating as per merge review comment

* Thu Sep 17 2009 Pravin Satpute <psatpute@redhat.com> - 0.3-9
- updating as per new packaging guidelines

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon Feb 23 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Jul 14 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 0.3-6
- fix license tag

* Tue Feb 12 2008 Rahul Bhalerao <rbhalera@redhat.com> - 0.3-5.2
- Rebuild for gcc4.3.

* Tue Feb 27 2007 Mayank Jain <majain@redhat.com> - 0.3-5.1.2
- Changed BuildRoot to %%{_tmppath}/%%{name}-%%{version}-%%{release}-root-%%(%%{__id_u} -n)
- Changed Prereq tag to Requires(pre)
- In the "cjk" subpackage summary, CJK is now spelt with capital letters.
- Added %%{?dist} to the Release tag

* Wed Jul 12 2006 Jesse Keating <jkeating@redhat.com> - 0.3-5.1.1
- rebuild

* Fri Dec 09 2005 Jesse Keating <jkeating@redhat.com>
- rebuilt

* Wed Nov 09 2004 Caolan McNamara <caolanm@redhat.com> - 0.3-5
- build fixfont .pcfs from source .bdfs

* Wed Sep 22 2004 Owen Taylor <otaylor@redhat.com> - 0.3-4
- Update BuildRequires to xorg-x11-font-utils (#118428, Mike Harris)

* Fri Feb 13 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Wed Jan 22 2003 Tim Powers <timp@redhat.com>
- rebuilt

* Tue Jan 21 2003 Owen Taylor <otaylor@redhat.com>
- Version 0.3 adding misc-fixed fonts from ucs-fonts
- Adjust %%post, %%postun

* Mon Jan 13 2003 Owen Taylor <otaylor@redhat.com>
- Patch from Anthony Fok, to fix problem where fangsongti16.bdf
  wasn't considered to cover english because it didn't have
  e-diaresis. (Causing bad font choice in Anaconda)

* Wed Dec 18 2002 Than Ngo <than@redhat.com> 0.2-4
- add some bitmap fonts

* Thu Oct 31 2002 Owen Taylor <otaylor@redhat.com> 0.2-3
- Own the bitmap-fonts directory (Enrico Scholz, #73940)
- Add %%post, %%postun for cjk subpackage

* Fri Aug 30 2002 Alexander Larsson <alexl@redhat.com> 0.2-2
- Call fc-cache from post

* Wed Aug 28 2002 Owen Taylor <otaylor@redhat.com>
- Augment fangsongti fonts with characters from 8x16, 12x24

* Tue Jul 31 2002 Yu Shao <yshao@redhat.com>
- add fangsong*.bdf converted from gb16fs.bdf and gb24st.bdf

* Mon Nov 13 2000 Owen Taylor <otaylor@redhat.com>
- Initial package

