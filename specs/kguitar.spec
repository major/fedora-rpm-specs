# Disable automatic .la file removal
%global __brp_remove_la_files %nil

%define svnver 926svn

Name:		  kguitar
Version:	  0.5.1
Release:	  44.%{svnver}%{?dist}
Summary:	  Guitar Tabulature Music Editor
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:	  GPL-2.0-or-later
URL:		  http://kguitar.sf.net/
Source0:	  %{name}-%{version}-%{svnver}.tar.bz2
# The supplied .desktop file is ancient and doesn't meet the current standards
# We are supplying a new one:
Source1:	  %{name}.desktop
# To fetch the svn trunk:
Source9:	  %{name}-snapshot.sh
# Patch to make kguitar build with automake 1.11 or higher
# https://sourceforge.net/tracker/?func=detail&aid=2804980&group_id=7693&atid=307693
Patch:		  %{name}-automake111.patch
# https://fedoraproject.org/wiki/Changes/PortingToModernC
Patch:		  kguitar-configure-c99.patch
# build with autoconf 2.72 (RHBZ#2183441)
Patch:		  %{name}-autoconf272.patch

BuildRequires:	  autoconf
BuildRequires:	  automake
BuildRequires:	  desktop-file-utils
BuildRequires:	  gettext 
BuildRequires:	  kdelibs3-devel
BuildRequires:	  libtool
BuildRequires:	  texlive-scheme-basic
BuildRequires:	  tse3-devel
BuildRequires:	  make

%description
KGuitar is a powerful KDE-based music tabulature editor with support of
multiple guitar (or any fretted instrument) and drum tracks. KGuitar also 
supports classic note scores, MIDI synthesizer output, chord, scales, modes, 
melody and rhythm construction and analysis tools, lots of tab effects, lyrics,
Guitar Pro files import and lots of other things.

%package tex
Summary:	  MusixTeX support for KGuitar
Requires:	  %{name} == %{version}-%{release}
Requires:	  tex-musixtex
Requires(post):	  /usr/bin/texhash
Requires(postun): /usr/bin/texhash

%description tex
KGuitar is a powerful KDE-based music tabulature editor with support of
multiple guitar (or any fretted instrument) and drum tracks. KGuitar also
supports classic note scores, MIDI synthesizer output, chord, scales, modes,
melody and rhythm construction and analysis tools, lots of tab effects, lyrics,
Guitar Pro files import and lots of other things.

This package provides support for compiling MusixTex files exported from
Kguitar.

%prep
%autosetup -n %{name} -p1

# Add more mime-types since the software is capable of handling them.
sed -i 's|\*.kg|\*.kg;\*.gp3;\*.gp4;\*.mid;\*.tab;\*.xml|' %{name}/x-%{name}.desktop

# Use system libtool. The bundled one screws up and package fails to build
sed -i -e 's|\$(top_builddir)/libtool|%{_bindir}/libtool|g' \
	-e 's|\./libtool|%{_bindir}/libtool|g' \
	admin/*

# Fix for gettext-0.22
sed -i -e 's/CHARSET/ISO-8859-1/' po/es.po

make -f admin/Makefile.common cvs ||:

%build
%configure \
	--disable-rpath \
	--disable-static \
	--disable-debug \
	--program-transform-name="" \
	--enable-final \
	--with-tse3-libraries="%{_libdir}" \
%if 0%{?__isa_bits} == 64
	--enable-libsuffix="64"
%endif

%make_build

%install
%make_install

# Make symlinks relative:
ln -fs ../common $RPM_BUILD_ROOT/%{_datadir}/doc/HTML/en/%{name}/

# Remove the old (it can't pass desktop-file-validate) .desktop file...
rm -fr $RPM_BUILD_ROOT/%{_datadir}/applnk
# ... and replace it with the new one:
desktop-file-install --dir=${RPM_BUILD_ROOT}/%{_datadir}/applications %{SOURCE1}

# Install the TeX support
mkdir -p $RPM_BUILD_ROOT/%{_texmf_main}/tex/generic/kgtabs
install -pm 644 %{name}_shell/kgtabs.tex $RPM_BUILD_ROOT/%{_texmf_main}/tex/generic/kgtabs

# Remove static lib
rm -f %{_libdir}/kde3/lib%{name}part.a

%find_lang %{name}

%post
touch --no-create %{_datadir}/icons/locolor &>/dev/null

%postun
if [ $1 -eq 0 ] ; then
    touch --no-create %{_datadir}/icons/locolor &>/dev/null
fi

%post tex -p /usr/bin/texhash

%postun tex -p /usr/bin/texhash

%files -f %{name}.lang
%doc AUTHORS ChangeLog COPYING README
%doc licenseMusicXML.html
%{_docdir}/HTML/en/%{name}

%{_bindir}/*
%{_libdir}/kde3/*
%{_datadir}/apps/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/mimelnk/application/*
%{_datadir}/services/%{name}_part.desktop
%{_datadir}/icons/*/*/*/*

%files tex
%{_texmf_main}/tex/generic/kgtabs

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.1-44.926svn
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 26 2024 Miroslav Suchý <msuchy@redhat.com> - 0.5.1-43.926svn
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.1-42.926svn
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.1-41.926svn
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.1-40.926svn
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.1-39.926svn
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Apr 14 2023 Florian Weimer <fweimer@redhat.com> - 0.5.1-38.926svn
- Port to C99

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.1-37.926svn
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.1-36.926svn
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.1-35.926svn
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.1-34.926svn
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.1-33.926svn
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.1-32.926svn
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.1-31.926svn
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Sep 09 2019 Kevin Fenzi <kevin@scrye.com> - 0.5.1-30.926svn
- Try and fix package to acutally build.

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.1-29.926svn
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.1-28.926svn
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.1-27.926svn
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.1-26.926svn
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 11 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.5.1-25.926svn
- Remove obsolete scriptlets

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.1-24.926svn
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.1-23.926svn
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.1-22.926svn
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.1-21.926svn
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.1-20.926svn
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.1-19.926svn
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Fri Jun 20 2014 Peter Robinson <pbrobinson@fedoraproject.org> 0.5.1-18.926svn
- Proper 64 bit macro check
- Cleanup spec, update tex dependencies

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.1-17.926svn
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.1-16.926svn
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.1-15.926svn
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.1-14.926svn
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Feb 28 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.1-13.926svn
- Rebuilt for c++ ABI breakage

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.1-12.926svn
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Orcan Ogetbil <oget [DOT] fedora [AT] gmail [DOT] com> - 0.5.1-11-926svn
- Add missing BR: desktop-file-utils.

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.1-10.926svn
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Nov 20 2009 Orcan Ogetbil <oget [DOT] fedora [AT] gmail [DOT] com> - 0.5.1-9-926svn
- Use system libtool. Fixes RHBZ#538944

* Wed Aug 05 2009 Orcan Ogetbil <oget [DOT] fedora [AT] gmail [DOT] com> - 0.5.1-8.926svn
- Update .desktop file

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.1-7.926svn
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Jun 11 2009 Orcan Ogetbil <oget [DOT] fedora [AT] gmail [DOT] com> - 0.5.1-6.926svn
- Patch to enable build with automake-1.11 or higher
- Update scriptlets according to the new guidelines

* Thu Jun 11 2009 Orcan Ogetbil <oget [DOT] fedora [AT] gmail [DOT] com> - 0.5.1-5.926svn
- BR automake17 because kguitar doesn't build with automake-1.11

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.1-4.926svn
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sun Feb 08 2009 Orcan Ogetbil <oget [DOT] fedora [AT] gmail [DOT] com> - 0.5.1-3.926svn
- Change the EVR scheme (use svn revision instead of date in R)
- Use RPM's _texmf_main macro instead of redefining it
- Place the TeX bit into a -tex subpackage
- Specfile cleanup

* Wed Jan 21 2009 Orcan Ogetbil <oget [DOT] fedora [AT] gmail [DOT] com> - 0.5.1-2.20090120svn
- Updated description
- Added TeX support
- Remove the call to ldconfig in post*

* Mon Jan 19 2009 Orcan Ogetbil <oget [DOT] fedora [AT] gmail [DOT] com> - 0.5.1-1.20090120svn
- Initial Fedora build
