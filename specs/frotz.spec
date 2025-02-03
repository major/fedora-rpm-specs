#%%global gitref d9676545fc072222d3b50742ee881f8c3570a62e
#%%global gitdate 20250127
#%%global shortref %%(echo %%{gitref} |cut -c1-8)

%if 0%{?shortref:1}
%global buildref .%{gitdate}git%{shortref}
%endif


Name:           frotz
Version:        2.55
Release:        1%{?buildref}%{?dist}
Summary:        Interactive fiction interpreter for Z-Machine (Infocom) games

License:        GPL-2.0-or-later
URL:            https://gitlab.com/DavidGriffith/frotz/
Source0:        https://gitlab.com/DavidGriffith/frotz/-/archive/%{version}/frotz-%{version}.tar.bz2

# Installing the X11 font would seem to be prohibited by the Fonts Policy
# https://docs.fedoraproject.org/en-US/packaging-guidelines/FontsPolicy/
Patch0:         frotz-2.54-no_font_install.patch

BuildRequires:  gcc
BuildRequires:  pkgconfig(ao)
BuildRequires:  pkgconfig(libmodplug)
BuildRequires:  pkgconfig(ncursesw)
BuildRequires:  pkgconfig(samplerate)
BuildRequires:  pkgconfig(sndfile)
BuildRequires:  pkgconfig(vorbisfile)

# For sfrotz
BuildRequires:  pkgconfig(bzip2)
BuildRequires:  pkgconfig(freetype2)
BuildRequires:  pkgconfig(libpng)
BuildRequires:  pkgconfig(libjpeg)
BuildRequires:  pkgconfig(sdl2)
BuildRequires:  pkgconfig(SDL2_mixer)
BuildRequires:  pkgconfig(zlib)

# For xfrotz
BuildRequires:  pkgconfig(xt)
BuildRequires:  pkgconfig(fontutil)
BuildRequires:  bdftopcf

BuildRequires: make

%global _description\
Frotz is an interpreter for Infocom games and other Z-machine games.  It\
complies with standard 1.0 of Graham Nelson's specification.\
\
Free Z-machine game file downloads, as well as more information about\
Infocom, Z-machine games, and interactive fiction can be found at the\
Interactive Fiction Archive, http://mirror.ifarchive.org/.

%description %_description


%package gui
Summary: SDL GUI for frotz interactive fiction interpreter
Requires: %{name}%{?_isa} = %{version}-%{release}

%description gui
%_description

This package contains the sfrotz GUI.


%prep
%autosetup -p1


%build
%make_build all


%install
%make_install PREFIX=%{_prefix} install_all

# Make a version of the config file with all settings commented out,
# to install in /etc
sed -Ee '/(^#|^$)/! s/^/#/' < doc/frotz.conf-big > frotz.conf
install -m0644 -D frotz.conf -t %{buildroot}%{_sysconfdir}


%files
%doc AUTHORS ChangeLog DUMB HOW_TO_PLAY README
%license COPYING
%doc doc/frotz.conf*
%{_bindir}/frotz
%{_bindir}/dfrotz
%{_mandir}/man6/frotz.6*
%{_mandir}/man6/dfrotz.6*
%config(noreplace) %{_sysconfdir}/frotz.conf

%files gui
%{_bindir}/sfrotz
%{_bindir}/xfrotz
%{_mandir}/man6/sfrotz.6*
%{_mandir}/man6/xfrotz.6*


%changelog
* Sat Feb 01 2025 FeRD (Frank Dana) <ferdnyc@gmail.com> - 2.55-1
- New upstream release; drop upstreamed patches

* Wed Jan 29 2025 FeRD (Frank Dana) <ferdnyc@gmail.com> - 2.54-9
- Build from git HEAD (with additional patches) to fix FTBFS on
  rawhide (RHBZ: 2340180)

* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.54-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.54-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.54-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.54-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.54-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.54-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.54-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Apr 14 2022 FeRD (Frank Dana) <ferdnyc@gmail.com> - 2.5.4-1
- New upstream release
- Patch build to avoid installing X11 bitmap font
- Added new X11 interface 'xfrotz' to -gui subpackage

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.52-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.52-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.52-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.52-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sun May 17 2020 FeRD (Frank Dana) <ferdnyc@gmail.com> - 2.52-1
- New upstream release

* Wed Feb 12 2020 FeRD (Frank Dana) <ferdnyc@gmail.com> - 2.51-2
- Incorporate changes to upstream release

* Wed Feb 12 2020 FeRD (Frank Dana) <ferdnyc@gmail.com> - 2.51-1
- New upstream release
- Drop upstreamed patches, adapt to changes to Makefile path handling

* Sat Feb 01 2020 FeRD (Frank Dana) <ferdnyc@gmail.com> - 2.50-3
- Add patch to fix GCC 10 compilation failures

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.50-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Jan 12 2020 FeRD (Frank Dana) <ferdnyc@gmail.com> - 2.50-1
- Update to latest 2.50 release, new gitlab upstream
- Split out SDL interface into separate -gui subpackage

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.43-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.43-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.43-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.43-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.43-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.43-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.43-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.43-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Jun 22 2015 Ralf Corsépius <corsepiu@fedoraproject.org> - 2.43-18
- Use '|' instead of '/' as pattern-delimiter in sed expression to filter
  CFLAGS (Fix FTBFS).

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.43-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.43-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.43-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.43-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.43-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.43-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.43-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.43-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.43-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.43-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Feb 18 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 2.43-7
- Autorebuild for GCC 4.3

* Wed Oct 31 2007 Chris Grau <chris@chrisgrau.com> 2.43-6
- Fixed license tag.

* Thu Sep 14 2006 Chris Grau <chris@chrisgrau.com> 2.43-5
- Rebuild for FC-6.

* Wed Mar 01 2006 Chris Grau <chris@chrisgrau.com> 2.43-4
- Rebuild for FC-5.

* Tue Jul 19 2005 Chris Grau <chris@chrisgrau.com> 2.43-3
- Changed sed command to edit Makefile in place (Michael Schwendt).
- Removed compression of the man page (Michael Schwendt).

* Tue Jul 19 2005 Chris Grau <chris@chrisgrau.com> 2.43-2
- Split up patch files.
- Added a pointer to the IF archive to the %%description.

* Thu Jul 07 2005 Chris Grau <chris@chrisgrau.com> 2.43-1
- Initial build.
