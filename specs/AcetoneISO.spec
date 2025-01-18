Name:		AcetoneISO
Version:	6.7
Release:	42%{?dist}
Summary:	CD/DVD Image Manipulator
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:	GPL-2.0-or-later
URL:		http://www.acetoneteam.org/
#Source0:	http://www.acetoneteam.org/Archivia/%{name}-%{version}.tar.gz
# Upstream source includes poweriso binary, closed source, no redistribution permission.
Source0:	%{name}-%{version}-clean.tar.gz
Patch0:		AcetoneISO-6.7-welcome-to-2017.patch
BuildRequires:  gcc
BuildRequires: 	kdewebdev-devel, desktop-file-utils
Requires:	p7zip, xbiso, k3b, kde-runtime, arts, cdrdao, nrg2iso
# There is no konqueror for ppc/ppc64. - 2017-06-15
# Or s390x. - 2017-09-05
ExcludeArch:	ppc %{power64} s390x
# Overkill, but I'm being thorough
Requires:	util-linux, coreutils, kdewebdev
Requires:       kdialog, konsole, kdesu, konqueror

%description
AcetoneISO: The CD/DVD image manipulator for Linux, it can do the following:
- Mount and Unmount ISO, MDF, NRG (if iso-9660 standard)
- Convert / Extract / Browse to ISO : *.bin *.mdf *.nrg *.img *.daa *.cdi 
  *.xbx *.b5i *.bwi *.pdi
- Play a DVD Movie ISO with most used media players
- Generate an ISO from a Folder or CD/DVD
- Generate MD5 file of an image
- Encrypt an image
- Split image into X megabyte chunks
- Highly compress an image
- Rip a PSX cd to *.bin to make it work with epsxe/psx emulators
- Service-Menu support for Konqueror
- Restore a lost CUE file of *.bin *.img

%prep
%setup -q
%patch -P0 -p1 -b .fixup

%build
cd src/
chmod -x *.c
mkdir ../binaries
# xbiso is in its own package
# so is nrg2iso.
for i in b5i2iso.c cdi2iso.c mdf2iso.c pdi2iso.c; do
  SHORTNAME=`echo $i | sed 's/.c//'`
  gcc $RPM_OPT_FLAGS $i -o ../binaries/$SHORTNAME
done

%install
rm -rf $RPM_BUILD_ROOT 
mkdir $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_bindir}
install -p binaries/* $RPM_BUILD_ROOT%{_bindir}
mkdir -p $RPM_BUILD_ROOT%{_datadir}/apps/%{name}/scripts/
sed -i 's|/opt/acetoneiso/|/usr/|g' %{name}-%{version}/AcetoneISO.kmdr
chmod -x %{name}-%{version}/AcetoneISO.kmdr
install -p %{name}-%{version}/AcetoneISO.kmdr $RPM_BUILD_ROOT%{_datadir}/apps/%{name}/scripts
mkdir -p $RPM_BUILD_ROOT%{_datadir}/pixmaps
install -p %{name}-%{version}/*.png $RPM_BUILD_ROOT%{_datadir}/pixmaps
mkdir -p $RPM_BUILD_ROOT%{_sbindir}
sed -i 's|/opt/acetoneiso/.|%{_sbindir}|g' %{name}-%{version}/acetoneiso-*mount.desktop
chmod -x %{name}-%{version}/acetoneiso-*mount.desktop
install -p %{name}-%{version}/*.sh $RPM_BUILD_ROOT%{_sbindir}

sed -i 's|/opt/acetoneiso/|%{_datadir}/apps/%{name}/scripts/|g' %{name}-%{version}/acetoneiso
install -p %{name}-%{version}/acetoneiso $RPM_BUILD_ROOT%{_bindir}

mkdir -p $RPM_BUILD_ROOT%{_datadir}/apps/konqueror/servicemenus/
install -p %{name}-%{version}/acetoneiso-*mount.desktop $RPM_BUILD_ROOT%{_datadir}/apps/konqueror/servicemenus/

mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
mv %{name}-%{version}/AcetoneISO %{name}-%{version}/AcetoneISO.desktop
sed -i 's|/opt/acetoneiso/|%{_datadir}/apps/%{name}/scripts/|g' %{name}-%{version}/AcetoneISO.desktop
sed -i "s|'/usr/share/apps/AcetoneISO/scripts/AcetoneISO.kmdr'|/usr/share/apps/AcetoneISO/scripts/AcetoneISO.kmdr|g" %{name}-%{version}/AcetoneISO.desktop
desktop-file-install --vendor ""			\
	--dir $RPM_BUILD_ROOT%{_datadir}/applications	\
	--add-category System				\
	%{name}-%{version}/AcetoneISO.desktop

%files
%doc GPL README changelog
%{_bindir}/acetoneiso
%{_bindir}/b5i2iso
%{_bindir}/cdi2iso
%{_bindir}/mdf2iso
%{_bindir}/pdi2iso
%{_sbindir}/playiso-unmount.sh
%{_sbindir}/turbo.sh
%{_datadir}/applications/*.desktop
%{_datadir}/apps/%{name}/
%{_datadir}/apps/konqueror/servicemenus/acetoneiso-*.desktop
%{_datadir}/pixmaps/*.png

%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 6.7-42
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 25 2024 Miroslav Suchý <msuchy@redhat.com> - 6.7-41
- convert license to SPDX

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 6.7-40
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 6.7-39
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 6.7-38
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jan 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 6.7-37
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 6.7-36
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 6.7-35
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 6.7-34
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 6.7-33
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 6.7-32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon Jan 25 2021 Fedora Release Engineering <releng@fedoraproject.org> - 6.7-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 6.7-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 6.7-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 6.7-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 6.7-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 6.7-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 6.7-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Sep  5 2017 Tom Callaway <spot@fedoraproject.org> - 6.7-24
- disable s390x

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 6.7-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 6.7-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jun 19 2017 Tom Callaway <spot@fedoraproject.org> - 6.7-21
- more specific ExcludeArch

* Thu Jun 15 2017 Tom Callaway <spot@fedoraproject.org> - 6.7-20
- ExcludeArch ppc ppc64 due to konqueror

* Fri Jun  2 2017 Tom Callaway <spot@fedoraproject.org> - 6.7-19
- scrape barnacles off this thing

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 6.7-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sat Feb 04 2017 Tom Callaway <spot@fedoraproject.org> - 6.7-17
- fix deps (hopefully)

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 6.7-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Jun 16 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 6.7-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Aug 15 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 6.7-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Fri Jun 06 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 6.7-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Aug 02 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 6.7-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 6.7-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 6.7-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 6.7-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 6.7-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 6.7-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon Feb 23 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 6.7-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Wed Feb 13 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 6.7-5
- rebuild for new gcc4.3

* Mon Nov 26 2007 Tom "spot" Callaway <tcallawa@redhat.com> - 6.7-4
- Requires: kdewebdev

* Wed Nov 21 2007 Tom "spot" Callaway <tcallawa@redhat.com> - 6.7-3
- nrg2iso has its own package (bz 394441)

* Thu Nov  8 2007 Tom "spot" Callaway <tcallawa@redhat.com> - 6.7-2
- fix unowned directories
- drop vendor in desktop file
- fix desktop file to actually work

* Mon Jun  4 2007 Tom "spot" Callaway <tcallawa@redhat.com> - 6.7-1
- initial build for Fedora
