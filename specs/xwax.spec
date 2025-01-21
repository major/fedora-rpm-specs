Name:           xwax
Version:        1.9
Release:        6%{?dist}
Summary:        Open source vinyl emulation software for Linux
# Automatically converted from old format: GPLv2 - review is highly recommended.
License:        GPL-2.0-only
URL:            https://www.xwax.org
Source0:        https://xwax.org/releases/%{name}-%{version}.tar.gz

BuildRequires: alsa-lib-devel
BuildRequires: make
BuildRequires: gcc
BuildRequires: SDL-devel SDL_ttf-devel jack-audio-connection-kit-devel
Requires: sox cdparanoia

%description
xwax is open-source vinyl emulation software for Linux. 
It allows DJs and turntablists to playback digital audio files 
(MP3, Ogg Vorbis, FLAC, AAC and more), controlled using a normal
pair of turntables via timecoded vinyls.

It's designed for both beat mixing and scratch mixing. Needle drops, pitch 
changes, scratching, spinbacks and rewinds are all supported, and feel just
like the audio is pressed onto the vinyl itself.

The focus is on an accurate vinyl feel which is efficient, stable and fast.

%prep
%autosetup

%build
%configure
make %{?_smp_mflags} ALSA=yes JACK=yes PREFIX=%{_prefix} EXECDIR=%{_libexecdir}/%{name}

# Note even though xwax is a GUI application I don't think it deserves a .desktop file because the program
# is entirely controlled through keyboard and it's options are only adjustable on the command line
# Options depend on the hardware that the user has available and can't be known ahead of time.

%install
make ALSA=yes JACK=yes install PREFIX=%{buildroot}/%{_prefix} EXECDIR=%{buildroot}/%{_libexecdir}/%{name} DOCDIR=/tmp

%files
%{_bindir}/xwax
%{_libexecdir}/xwax/
%doc CHANGES COPYING README
%doc %{_mandir}/man1/xwax.1.gz

%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.9-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Jul 29 2024 Miroslav Suchý <msuchy@redhat.com> - 1.9-5
- convert license to SPDX

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.9-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.9-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jun 09 2023 Filipe Rosset <rosset.filipe@gmail.com> - 1.9-1
- Update to 1.9 fixes rhbz#2204460

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.8-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Sep 29 2021 Filipe Rosset <rosset.filipe@gmail.com> - 1.8-1
- Update to 1.8, fixes rhbz#1974107 rhbz#1988055 and rhbz#1995356

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.7-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Thu Jan 28 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.7-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.7-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.7-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.7-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.7-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sun Sep 23 2018 Filipe Rosset <rosset.filipe@gmail.com> - 1.7-4
- rebuilt to fix FTBFS rhbz #1606762 and #1370846 + spec cleanup

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sun Feb 04 2018 Filipe Rosset <rosset.filipe@gmail.com> - 1.7-1
- Rebuilt for new upstream version 1.7, fixes rhbz #1370846

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun Dec 04 2016 Filipe Rosset <rosset.filipe@gmail.com> - 1.6-1
- Rebuilt for new upstream version 1.6, fixes rhbz #1370846

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat May 24 2014 Filipe Rosset <rosset.filipe@gmail.com> - 1.5-2
- Rebuilt for new upstream version, fixes rhbz #1063828

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sun Jul 22 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jul 5 2012 John Brier <jbrier@redhat.com> 1.2-3
- SPEC file fixes

* Sun Jul 1 2012 John Brier <jbrier@redhat.com> 1.2-2
- SPEC file fixes

* Sun Jun 10 2012 John Brier <jbrier@redhat.com> 1.2-1
- rebuild for new upstream version

* Sun May 1 2011  John Brier <jbrier@redhat.com> 0.9-3
- changed License from GPL to GPLv2
- fixed inconsistent macros for build root
- fixed debuginfo package by adding configure macro in build

* Thu Apr 28 2011 John Brier <jbrier@redhat.com> 0.9-2
- Removed flac and vorbis-tools from Requires in favor of sox
  as fallback decoder

* Fri Apr 22 2011 John Brier <jbrier@redhat.com> 0.9-1
- New upstream version 0.9

* Mon Apr 18 2011 John Brier <jbrier@redhat.com> 0.8-2
- Changed summary and added flac, vorbis-tools, sox and cdparanoia
  to Requires

* Mon Apr 11 2011 John Brier <jbrier@redhat.com> 0.8-1
- First RPM package of xwax for Fedora 14
