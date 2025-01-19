Name:           kbilliards
# Note: the "b" in 0.8.7b is supposed to go in the Release tag.
# Keep that in mind when/if you next upgrade the package
# https://fedoraproject.org/wiki/Packaging:NamingGuidelines
Version:        0.8.7b
Release:        47%{?dist}
Summary:        A Fun Billiards Simulator Game
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
URL:            http://www.hostnotfound.it/kbilliards.php
Source:         http://www.hostnotfound.it/%{name}/%{name}-%{version}.tar.bz2
Patch0:         sqrtl.patch
Patch1:         %{name}-%{version}-compiler_warnings.patch
Patch2:         %{name}-destdir.patch
Patch3:         %{name}-%{version}-gcc43.patch
Patch4:         %{name}-%{version}-fix-configure-checks.patch
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
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.7b-47
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 26 2024 Miroslav Suchý <msuchy@redhat.com> - 0.8.7b-46
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.7b-45
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.7b-44
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.7b-43
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 27 2023 Hans de Goede <hdegoede@redhat.com> - 0.8.7b-42
- Fix FTBFS (rhbz#2225944)
- Trim changelog

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.7b-41
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.7b-40
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.7b-39
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.7b-38
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild
