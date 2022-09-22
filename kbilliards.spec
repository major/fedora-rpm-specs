Name:           kbilliards
# Note: the "b" in 0.8.7b is supposed to go in the Release tag.
# Keep that in mind when/if you next upgrade the package
# https://fedoraproject.org/wiki/Packaging:NamingGuidelines
Version:        0.8.7b
Release:        39%{?dist}
Summary:        A Fun Billiards Simulator Game
License:        GPLv2+
URL:            http://www.hostnotfound.it/kbilliards.php
Source:         http://www.hostnotfound.it/%{name}/%{name}-%{version}.tar.bz2
Patch0:         sqrtl.patch
Patch1:         %{name}-%{version}-compiler_warnings.patch
Patch2:         %{name}-destdir.patch
Patch3:         %{name}-0.8.7b-gcc43.patch
BuildRequires:  make gcc gcc-c++
BuildRequires:  kdelibs3-devel bzip2-devel desktop-file-utils gettext
# required to fix the PNGs (vim-common for xxd)
BuildRequires:  pngcrush vim-common
Requires:       hicolor-icon-theme

%description
A billiards simulator game designed for KDE.


%prep
%autosetup -p1
sed -i 's/\r//g' ChangeLog

# fix corrupt PNGs
pngcrush -ow -fix media/balls/ball_shadow.png
pngcrush -ow -fix media/balls/ball_shadowb.png
mv media/maps/kbilliards2004.kbm media/maps/kbilliards2004.xml.bz2
bunzip2 media/maps/kbilliards2004.xml.bz2
grep '<data length="342162">' media/maps/kbilliards2004.xml | sed -e 's/^ *<data length="[^"]*">//g' -e 's!</data>$!!g' | xxd -r -p - media/maps/background.png
grep '<data length="142617">' media/maps/kbilliards2004.xml | sed -e 's/^ *<data length="[^"]*">//g' -e 's!</data>$!!g' | xxd -r -p - media/maps/edges.png
grep '<data length="7910">' media/maps/kbilliards2004.xml | sed -e 's/^ *<data length="[^"]*">//g' -e 's!</data>$!!g' | xxd -r -p - media/maps/holes.png
pngcrush -ow -fix media/maps/background.png
pngcrush -ow -fix media/maps/edges.png
pngcrush -ow -fix media/maps/holes.png
echo 's!<data length="342162">[^<]*</data>!<data length="'`wc -c media/maps/background.png | sed 's/ .*$//g'`'">'`xxd -p -c 999999 media/maps/background.png`'</data>!g;s!<data length="142617">[^<]*</data>!<data length="'`wc -c media/maps/edges.png | sed 's/ .*$//g'`'">'`xxd -p -c 999999 media/maps/edges.png`'</data>!g;s!<data length="7910">[^<]*</data>!<data length="'`wc -c media/maps/holes.png | sed 's/ .*$//g'`'">'`xxd -p -c 999999 media/maps/holes.png`'</data>!g' >media/maps/sedscript.txt
rm -f media/maps/background.png media/maps/edges.png media/maps/holes.png
sed -i -f media/maps/sedscript.txt media/maps/kbilliards2004.xml
rm -f media/maps/sedscript.txt
bzip2 -9 media/maps/kbilliards2004.xml
mv media/maps/kbilliards2004.xml.bz2 media/maps/kbilliards2004.kbm

# fix missing semicolon at the end of the Categories list in the .desktop file
sed -i -e 's/^\(Categories=.*\)$/\1\;/g' src/%{name}.desktop


%build
%configure --disable-rpath
# Don't use rpath!
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool
%make_build


%install
%make_install

# fixup translation stuff
pushd po
for i in *.po; do
   POLANG=`echo $i|sed 's/\.po//'`
   mkdir -p $RPM_BUILD_ROOT%{_datadir}/locale/$POLANG/LC_MESSAGES
   msgfmt $i -o $RPM_BUILD_ROOT%{_datadir}/locale/$POLANG/LC_MESSAGES/%{name}.mo
done
popd
%find_lang %{name}

# below is the desktop file and icon stuff.
mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
desktop-file-install \
  --delete-original \
  --dir $RPM_BUILD_ROOT%{_datadir}/applications --remove-key=DocPath \
  --add-category Simulation \
  $RPM_BUILD_ROOT%{_datadir}/applnk/Games/%{name}.desktop

rm -fr $RPM_BUILD_ROOT%{_datadir}/icons/locolor


%files -f %{name}.lang
%doc AUTHORS ChangeLog TODO src/NOATUN_AUTHORS
%license COPYING
%{_bindir}/%{name}
%{_datadir}/apps/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.*


%changelog
* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.7b-39
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.7b-38
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Mon Aug  2 2021 Hans de Goede <hdegoede@redhat.com> - 0.8.7b-37
- Fix FTBFS (rhbz#1987613)

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.7b-36
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.7b-35
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.7b-34
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.7b-33
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.7b-32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.7b-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Jul 30 2018 Hans de Goede <hdegoede@redhat.com> - 0.8.7b-30
- Fix FTBFS (rhbz#1604470)
- Modernize the spec file a bit

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.7b-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.7b-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 11 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.8.7b-27
- Remove obsolete scriptlets

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.7b-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.7b-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.7b-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun Nov 20 2016 Kevin Kofler <Kevin@tigcc.ticalc.org> - 0.8.7-23
- Fix corrupt PNGs that were making this game almost unplayable
- Fix missing semicolon at the end of the Categories list in the .desktop file

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.7b-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.7b-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 0.8.7b-20
- Rebuilt for GCC 5 C++11 ABI change

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.7b-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.7b-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.7b-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Mar  6 2013 Toshio Kuratomi <toshio@fedoraproject.org> - 0.8.7b-16
- Remove vendor prefix from desktop files in F19+ https://fedorahosted.org/fesco/ticket/1077

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.7b-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.7b-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Feb 28 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.7b-13
- Rebuilt for c++ ABI breakage

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.7b-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.7b-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.7b-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.7b-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sun Sep  7 2008 Hans de Goede <hdegoede@redhat.com> 0.8.7b-8
- Fix patch fuzz build failure

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 0.8.7b-7
- Autorebuild for GCC 4.3

* Tue Jan  8 2008 Hans de Goede <j.w.r.degoede@hhs.nl> 0.8.7b-6
- Fix building with gcc 4.3

* Sun Dec  2 2007 Hans de Goede <j.w.r.degoede@hhs.nl> 0.8.7b-5
- BuildRequire kdelibs3-devel instead of kdelibs-devel as that now is
  kde4 based, and we need kde 3

* Wed Aug 22 2007 Hans de Goede <j.w.r.degoede@hhs.nl> 0.8.7b-4
- Rebuild for buildId

* Sun Aug 12 2007 Hans de Goede <j.w.r.degoede@hhs.nl> 0.8.7b-3
- Update License tag for new Licensing Guidelines compliance
- Add BR bzip2-devel (this no longer gets dragged in by kdelibs-devel)

* Thu Feb 22 2007 Hans de Goede <j.w.r.degoede@hhs.nl> 0.8.7b-2
- Install .po files, add a missing doc file (bz 228295)

* Sat Feb 10 2007 Hans de Goede <j.w.r.degoede@hhs.nl> 0.8.7b-1
- Initial Fedora Extras package
