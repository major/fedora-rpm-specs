Name:           keepassx0
Version:        0.4.4
Release:        19%{?dist}
Summary:        Cross-platform password manager

# apg/ and crypto/ directory contains BSD files
# only crypto/arcfour* files are GPLv2+ 
# all other source is GPLv2 licensed files
License:        GPLv2 and BSD
URL:            http://keepassx.sourceforge.net
Source0:        https://www.keepassx.org/releases/%{version}/keepassx-%{version}.tar.gz
Patch1:         keepassx-0.3.3-gcc43.patch
Patch2:         keepassx-0.4.3-gcc47.patch
BuildRequires:  qt4-devel > 4.1, libXtst-devel, ImageMagick, desktop-file-utils
BuildRequires: make
Requires:       hicolor-icon-theme
Obsoletes:      keepassx < 0:2.0

%description
KeePassX is an application for people with extremely high demands on secure
personal data management.
KeePassX saves many different information e.g. user names, passwords, urls,
attachements and comments in one single database. For a better management
user-defined titles and icons can be specified for each single entry.
Furthermore the entries are sorted in groups, which are customizable as well.
The integrated search function allows to search in a single group or the
complete database.
KeePassX offers a little utility for secure password generation. The password
generator is very customizable, fast and easy to use. Especially someone who
generates passwords frequently will appreciate this feature.
The complete database is always encrypted either with AES (alias Rijndael) or
Twofish encryption algorithm using a 256 bit key. Therefore the saved
information can be considered as quite safe. KeePassX 0.4.x uses a database format
that is compatible with KeePass Password Safe v1 for MS Windows.

%prep
%setup -qn keepassx-%{version}
%patch1 -p0 -b .gcc43
%patch2 -p1 -b .gcc47

sed -i s/keepassx/keepassx0/g src/src.pro
sed -i s/keepassx0.h/keepassx.h/g src/src.pro

%build
qmake-qt4 PREFIX=%{_prefix} \
      QMAKE_CFLAGS="$RPM_OPT_FLAGS" \
      QMAKE_CXXFLAGS="$RPM_OPT_FLAGS"
make %{?_smp_mflags}

%install
make install INSTALL_ROOT=$RPM_BUILD_ROOT 

# Use png in _datadir/icons/hicolor instead of xpm in pixmaps
mkdir -p $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/32x32/apps/
convert $RPM_BUILD_ROOT%{_datadir}/pixmaps/keepassx.xpm \
        $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/32x32/apps/keepassx0.png
rm -f $RPM_BUILD_ROOT%{_datadir}/pixmaps/keepassx.xpm

mkdir -p $RPM_BUILD_ROOT%{_datadir}/keepassx
cp -r share/keepassx/* $RPM_BUILD_ROOT%{_datadir}/keepassx/

# Menu
mv $RPM_BUILD_ROOT%{_datadir}/applications/keepassx.desktop $RPM_BUILD_ROOT%{_datadir}/applications/keepassx0.desktop

# Rename the Exec file name
sed -i -e 's/^Exec=keepassx %f/Exec=keepassx0 %f/g' \
        $RPM_BUILD_ROOT%{_datadir}/applications/keepassx0.desktop
desktop-file-install \
        --dir $RPM_BUILD_ROOT%{_datadir}/applications \
        --delete-original \
        --add-mime-type application/x-keepass \
        $RPM_BUILD_ROOT%{_datadir}/applications/keepassx0.desktop

sed -i s/Name=KeePassX/Name=KeePassX\ 0.4.x/g %{buildroot}%{_datadir}/applications/keepassx0.desktop
sed -i s/Icon=keepassx/Icon=keepassx0/g %{buildroot}%{_datadir}/applications/keepassx0.desktop

# Associate KDB files
cat > x-keepassx0.desktop << EOF
[Desktop Entry]
Comment=
Hidden=false
Icon=keepassx0
MimeType=application/x-keepass;
Patterns=*.kdb;*.KDB
Type=MimeType
EOF
install -D -m 644 -p x-keepassx0.desktop \
  $RPM_BUILD_ROOT%{_datadir}/mimelnk/application/x-keepassx0.desktop


%files
%license share/keepassx/license.html
%{_bindir}/keepassx0
%{_datadir}/keepassx
%{_datadir}/applications/*.desktop
%{_datadir}/mimelnk/application/*.desktop
%{_datadir}/mime/packages/*.xml
%{_datadir}/icons/hicolor/*/apps/keepassx0.png

%changelog
* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.4-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.4-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.4-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.4-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.4-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.4-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.4-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.4-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.4-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.4-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 11 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.4.4-9
- Remove obsolete scriptlets

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.4-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.4-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Jun 23 2016 Jon Ciesla <limburgher@gmail.com> - 0.4.4-5
- Correct icon, BZ 1349348

* Tue Jun 14 2016 Jon Ciesla <limburgher@gmail.com> - 0.4.4-4
- Update description, desktop file display name.

* Sat Jun 04 2016 Parag Nemade <pnemade AT redhat DOT com> - 0.4.4-3
- Fix Exec key in desktop file to keepassx0
- Add license breakup
- Fix some English words spelling in %%description
- Honor the compiler flags 
- Remove Obsolete Group tag

* Fri Jun 03 2016 Parag Nemade <pnemade AT redhat DOT com> - 0.4.4-2
- Correct the license tag, Source URL
- Use %%license for license.html file

* Mon Apr 25 2016 Jon Ciesla <limburgher@gmail.com> - 0.4.4-1
- Created from keepassx, FESCO 1569

* Wed Apr 13 2016 Jon Ciesla <limburgher@gmail.com> - 1:0.4.4-1
- Revert to 0.4.x, incompatible db change.

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Dec 23 2015 Francesco Frassinelli <fraph24@gmail.com> - 2.0.0-1
- Version bump
  Project moved to GitHub

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.3-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 0.4.3-12
- Rebuilt for GCC 5 C++11 ABI change

* Mon Aug 18 2014 Rex Dieter <rdieter@fedoraproject.org> 0.4.3-11
- update mime scriptlets

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.3-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.3-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue Feb 12 2013 Jon Ciesla <limburgher@gmail.com> - 0.4.3-7
- Drop desktop vendor tag.

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Mar 30 2012 Tom Callaway <spot@fedoraproject.org> - 0.4.3-5
- fix FTBFS on gcc 4.7

* Tue Feb 28 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.3-4
- Rebuilt for c++ ABI breakage

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sun Mar 14 2010 Aurelien Bompard <abompard@fedoraproject.org> -  0.4.3-1
- version 0.4.3

* Sun Jan 03 2010 Aurelien Bompard <abompard@fedoraproject.org> -  0.4.1-1
- version 0.4.1

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Sat Apr 18 2009 Aurelien Bompard <abompard@fedoraproject.org> 0.4.0-2
- add patch0 to fix bug 496035

* Thu Mar 26 2009 Aurelien Bompard <abompard@fedoraproject.org> 0.4.0-1
- version 0.4.0
- drop patch0 (upstream)

* Thu Mar 12 2009 Aurelien Bompard <abompard@fedoraproject.org> 0.3.4-3
- backport fix from upstream for bug #489820

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Tue Nov 11 2008 Aurelien Bompard <abompard@fedoraproject.org> 0.3.4-1
- version 0.3.4

* Sat Aug 23 2008 Aurelien Bompard <abompard@fedoraproject.org> 0.3.3-2
- rebase patch for version 0.3.3

* Tue Aug 12 2008 Aurelien Bompard <abompard@fedoraproject.org> 0.3.3-1
- version 0.3.3

* Mon Jul 21 2008 Aurelien Bompard <abompard@fedoraproject.org> 0.3.2-1
- version 0.3.2

* Sun Mar 16 2008 Aurelien Bompard <abompard@fedoraproject.org> 0.3.1-1
- version 0.3.1
- drop xdg patch, keepassx now uses QDesktopServices

* Wed Mar 05 2008 Aurelien Bompard <abompard@fedoraproject.org> 0.3.0-3.a
- version 0.3.0a

* Wed Mar 05 2008 Aurelien Bompard <abompard@fedoraproject.org> 0.3.0-2
- patch for gcc 4.3

* Sun Mar 02 2008 Aurelien Bompard <abompard@fedoraproject.org> 0.3.0-1
- version 0.3.0
- drop helpwindow patch (feature dropped upstream)

* Mon Feb 18 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 0.2.2-5
- Autorebuild for GCC 4.3

* Sun Oct 07 2007 Aurelien Bompard <abompard@fedoraproject.org> 0.2.2-4
- use xdg-open instead of htmlview

* Sat Aug 25 2007 Aurelien Bompard <abompard@fedoraproject.org> 0.2.2-3
- fix license tag
- rebuild for BuildID

* Wed Jun 27 2007 Aurelien Bompard <abompard@fedoraproject.org> 0.2.2-2
- fix help button
- use htmlview instead of the hardcoded konqueror

* Sun Mar 04 2007 Aurelien Bompard <abompard@fedoraproject.org> 0.2.2-1
- initial package
