Name:		xscorch
Version:	0.2.1
Release:	28%{?dist}
Summary:	A Scorched Earth clone
License:	GPL-2.0-only
URL:		http://www.xscorch.org/
Source0:	http://www.xscorch.org/releases/%{name}-%{version}.tar.gz
Source1:	xscorch.desktop
Source2:        xscorch.png
Source3:        xscorch.appdata.xml
Patch1:		xscorch-0.2.1-pre2-disable-debug.patch
Patch2:		xscorch-0.2.1-missing-proto.patch
Patch3:		xscorch-0.2.1-memcpy.patch
BuildRequires: make
BuildRequires:  gcc
BuildRequires:	libX11-devel gtk2-devel desktop-file-utils libappstream-glib
BuildRequires:	perl-interpreter
Requires:       hicolor-icon-theme

%description
xscorch is a clone of the classic DOS game, "Scorched Earth". The basic goal
is to annihilate enemy tanks using overpowered guns :). Basically, you buy
weapons, you target the enemy by adjusting the angle of your turret and firing
power, and you hope to destroy their tank before they destroy yours.


%prep
%setup -q
%patch -P1 -p1
%patch -P2 -p1
%patch -P3 -p1
# Fix encoding
for i in AUTHORS ChangeLog; do
	iconv -f ISO-8859-1 -t UTF-8 < ${i} > ${i}.tmp
	mv -f ${i}.tmp ${i}
done


%build
export CPPFLAGS="$CPPFLAGS -fcommon"
%configure --disable-network --disable-sound
make %{?_smp_mflags}


%install
%make_install INSTALL="install -p"

# below is the desktop file and icon stuff.
mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
desktop-file-install --dir $RPM_BUILD_ROOT%{_datadir}/applications %{SOURCE1}
mkdir -p $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/64x64/apps
install -p -m 644 %{SOURCE2} \
  $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/64x64/apps
mkdir -p $RPM_BUILD_ROOT%{_datadir}/appdata
install -p -m 644 %{SOURCE3} $RPM_BUILD_ROOT%{_datadir}/appdata
appstream-util validate-relax --nonet \
  $RPM_BUILD_ROOT%{_datadir}/appdata/xscorch.appdata.xml

%files
%doc doc/AI AUTHORS ChangeLog doc/NETWORK doc/NOTES README
%license COPYING
%{_bindir}/xscorch
%{_datadir}/appdata/xscorch.appdata.xml
%{_datadir}/applications/xscorch.desktop
%{_mandir}/man6/xscorch.6*
%{_datadir}/xscorch/
%{_datadir}/icons/hicolor/64x64/apps/xscorch.png


%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.1-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.1-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Mon Jan 29 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.1-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.1-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.1-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Mar 01 2023 Gwyn Ciesla <gwync@protonmail.com> - 0.2.1-23
- migrated to SPDX license

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.1-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.1-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.1-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.1-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Thu Jan 28 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.1-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.1-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Feb 10 2020 Gwyn Ciesla <gwync@protonmail.com> - 0.2.1-16
- Fix FTBFS.

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.1-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.1-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.1-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 18 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.2.1-10
- Remove obsolete scriptlets

* Mon Aug 07 2017 Gwyn Ciesla <limburgher@gmail.com> - 0.2.1-9
- BR perl-interpreter

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Jan 26 2016 Hans de Goede <hdegoede@redhat.com> - 0.2.1-4
- Fix crash on 64 bit machines (undeclared function prototypes) (rhbz#1294450)
- Add higher-res icon
- Add appdata
- Modernize specfile

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Mon Aug 11 2014 Jon Ciesla <limburgher@gmail.com> - 0.2.1-1
- 0.2.1 final
- memcpy path, BZ 1122154 from Debian bug 753516.

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.1-0.13.pre2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.1-0.12.pre2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Jul 17 2013 Petr Pisar <ppisar@redhat.com> - 0.2.1-0.11.pre2
- Perl 5.18 rebuild

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.1-0.10.pre2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sun Jul 22 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.1-0.9.pre2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.1-0.8.pre2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Thu Nov 10 2011 Jon Ciesla <limb@jcomserv.net> - 0.2.1-0.7.pre2
- Rebuild for libpng 1.5.

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.1-0.6.pre2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Dec 15 2010 Hans de Goede <hdegoede@redhat.com> 0.2.1-0.5.pre2
- Fix compilation with newer gtk versions (#599848)

* Mon Jul 27 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.1-0.4.pre2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Jul 08 2009 Marcin Garski <mgarski[AT]post.pl> 0.2.1-0.3.pre2
- Update to 0.2.1-pre2

* Wed May 27 2009 Marcin Garski <mgarski[AT]post.pl> 0.2.1-0.2.pre1
- Update to 0.2.1-pre1
- Remove stack-smash and 64bit patches (merged upstream)
- Update .desktop file (#485371)

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 0.2.0-13
- Autorebuild for GCC 4.3

* Fri Aug 31 2007 Marcin Garski <mgarski[AT]post.pl> 0.2.0-12
- Fix license tag

* Wed Aug 29 2007 Fedora Release Engineering <rel-eng at fedoraproject dot org> - 0.2.0-11
- Rebuild for selinux ppc32 issue.

* Fri Jun 22 2007 Marcin Garski <mgarski[AT]post.pl> 0.2.0-10
- Create symlinks in pixmaps directory
- Preserve upstream .desktop vendor
- Fix .desktop category

* Sat May 05 2007 Marcin Garski <mgarski[AT]post.pl> 0.2.0-9
- Spec tweak

* Thu Aug 31 2006 Marcin Garski <mgarski[AT]post.pl> 0.2.0-8
- Rebuild for FC6

* Tue Feb 14 2006 Marcin Garski <mgarski[AT]post.pl> 0.2.0-7
- Add Desktop things

* Tue Feb 14 2006 Marcin Garski <mgarski[AT]post.pl> 0.2.0-6
- Rebuild

* Wed Dec 14 2005 Marcin Garski <mgarski[AT]post.pl> 0.2.0-5
- Prepare for modular X.Org

* Fri Aug 26 2005 Marcin Garski <mgarski[AT]post.pl> 0.2.0-4
- Disable network
- Patch fixing stack smashing
- Patch fixing Readline detection

* Tue Aug 23 2005 Marcin Garski <mgarski[AT]post.pl> 0.2.0-3
- Spec improvements for Fedora Extras

* Wed Jun 02 2004 Marcin Garski <mgarski[AT]post.pl> 0.2.0-2.fc2
- Rebuild for Fedora Core 2

* Wed Mar 31 2004 Marcin Garski <mgarski[AT]post.pl> 0.2.0-1
- Update to 0.2.0

* Wed Feb 11 2004 Marcin Garski <mgarski[AT]post.pl> 0.1.16-2
- Disable sound that cause problems

* Sun Feb  1 2004 Marcin Garski <mgarski[AT]post.pl> 0.1.16-1
- Update to 0.1.16

* Sat Jan 31 2004 Marcin Garski <mgarski[AT]post.pl> 0.1.15-2
- Added xscorch.desktop

* Sat Jan 31 2004 Marcin Garski <mgarski[AT]post.pl> 0.1.15-1
- Initial specfile
