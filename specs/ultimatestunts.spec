%global		ver	0771

Name:		ultimatestunts
Version:	0.7.7
Release:	28%{?dist}
Summary:	Remake of the famous DOS-game Stunts

# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:	GPL-2.0-or-later
URL:		http://www.ultimatestunts.nl
Source0:	http://downloads.sf.net/%{name}/%{name}-srcdata-%{ver}.tar.gz
Source1:	%{name}.desktop
Patch0:		ultimatestunts-0761-make.patch
Patch1:		ultimatestunts-0751-locale.patch
Patch2:		ultimatestunts-0761-unistd.patch

BuildRequires: make
BuildRequires:  gcc-c++
BuildRequires:	dos2unix
BuildRequires:	freealut-devel
BuildRequires:	SDL_image-devel
BuildRequires:	freeglut-devel
BuildRequires:	libXi-devel
BuildRequires:	libvorbis-devel
BuildRequires:	desktop-file-utils


%description
UltimateStunts is a remake of the famous DOS-game Stunts. It was a 3D racing
game, with simple CGA/EGA/VGA graphics and no texture or smooth shading, but
because of the spectacular stunts (loopings, bridges to jump over, etc.)
it was really fun to play. One of the best aspects of this game is that it
had a track editor. Because of the tile-based tracks, every gamer was able
to make it's own tracks. This remake works on UNIX-compatible systems (like
Linux), and on windows. It also provides more modern features, like openGL
graphics, 3D sound and internet multiplaying.


%prep
%setup -q -n %{name}-srcdata-%{ver}
%patch -P0 -p0 -b .make
%patch -P1 -p0 -b .locale
%patch -P2 -p1 -b .unistd

# remove SVN control files
find . -name .svn -type d -print0 | xargs -0 rm -rf

# fixup access
find ./data -type d -print0 | xargs -0 chmod a+rx
find ./data -type f -print0 | xargs -0 chmod a+r
find ./doc -type f -print0 | xargs -0 chmod a+r
chmod a-x simulation/metaserver.cpp
chmod a-x shared/usmisc.cpp

# fixup EOL
pushd "doc/nolanguage/Original Stunts Track-Format_files"
dos2unix -q style.css
dos2unix -q stunts.htm
touch -r tree.png style.css stunts.htm
popd

# fixup encoding
pushd "doc/nolanguage/Original Stunts Track-Format_files"
f=stunts.htm
iconv -f ISO8859-1 -t UTF-8 -o $f.new $f
touch -r tree.png $f.new
mv $f.new $f
popd

pushd doc/nl
for f in *.htm
do
	iconv -f ISO8859-1 -t UTF-8 -o $f.new $f
	touch -r $f $f.new
	mv $f.new $f
done
popd

# ensure the config gets regenerated with correct $datadir
rm -f %{name}.conf


%build
%configure
make %{?_smp_mflags}


%install
make install DESTDIR=$RPM_BUILD_ROOT \
	usdatadir=$RPM_BUILD_ROOT%{_datadir}/%{name} \
	localedir=%{_datadir}/locale

rm -rf $RPM_BUILD_ROOT%{_datadir}/%{name}/lang

%find_lang %{name}

desktop-file-install \
	--dir $RPM_BUILD_ROOT%{_datadir}/applications \
	%{SOURCE1}


%files -f %{name}.lang
%doc COPYING doc/*
%{_bindir}/ustunts*
%config(noreplace) %{_sysconfdir}/%{name}.conf
%{_datadir}/applications/%{name}.desktop
%{_datadir}/%{name}


%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.7-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 26 2024 Miroslav Suchý <msuchy@redhat.com> - 0.7.7-27
- convert license to SPDX

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.7-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.7-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.7-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.7-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.7-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.7-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.7-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.7-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.7-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.7-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.7-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.7-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.7-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.7-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.7-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.7-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.7-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.7-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.7-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 0.7.7-7
- Rebuilt for GCC 5 C++11 ABI change

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.7-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.7-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Feb 14 2013 Parag Nemade <paragn AT fedoraproject DOT org> - 0.7.7-2
- Remove vendor tag from desktop file
- spec clean up

* Mon Sep 10 2012 Dan Horák <dan[at]danny.cz> - 0.7.7-1
- update to upstream version 0771

* Sun Jul 22 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.6-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Feb 28 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.6-4
- Rebuilt for c++ ABI breakage

* Sun Jan 15 2012 Dan Horák <dan[at]danny.cz> 0.7.6-3
- fix unistd.h include

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sat Apr 16 2011 Dan Horák <dan[at]danny.cz> 0.7.6-1
- update to upstream version 0761

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.5-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Aug 17 2009 Dan Horák <dan[at]danny.cz> 0.7.5-5
- rebuild with openal-soft

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Tue Nov 25 2008 Dan Horak <dan[at]danny.cz> 0.7.5-2
- shorten Summary

* Mon Jun 23 2008 Dan Horak <dan[at]danny.cz> 0.7.5-1
- update to upstream version 0751
- use locale data from system directory

* Wed Jan 30 2008 Dan Horak <dan[at]danny.cz> 0.7.4-1
- update to upstream version 0741
- remove integrated patches

* Sun Jan 27 2008 Dan Horak <dan[at]danny.cz> 0.7.3-5
- add patch with gcc 4.3 support

* Fri Nov  9 2007 Dan Horak <dan[at]danny.cz> 0.7.3-4
- recode *.htm files without encoding header

* Wed Nov  7 2007 Dan Horak <dan[at]danny.cz> 0.7.3-3
- added COPYING into docs
- added desktop file

* Tue Nov  6 2007 Dan Horak <dan[at]danny.cz> 0.7.3-2
- fix findind ALUT library on development

* Sun Nov  4 2007 Dan Horak <dan[at]danny.cz> 0.7.3-1
- initial package release
