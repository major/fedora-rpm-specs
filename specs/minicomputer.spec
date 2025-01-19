Name:		minicomputer
Version:	1.41
Release:	40%{?dist}
Summary:	Software Synthesizer
# Automatically converted from old format: GPLv3+ - review is highly recommended.
License:	GPL-3.0-or-later
URL:		http://minicomputer.sourceforge.net/
Source0:	http://downloads.sourceforge.net/minicomputer/MinicomputerV%{version}.tar.gz
Source1:	%{name}.desktop
# DSO linking fix. Sent upstream by email.
Patch0:		%{name}-linking.patch
# GCC 4.7 fix
Patch1:		%{name}-gcc47.patch
# Build with Python 3
Patch2:		%{name}-build-python3.patch

BuildRequires:	gcc-c++
BuildRequires:	alsa-lib-devel
BuildRequires:	desktop-file-utils
BuildRequires:	fltk-devel
BuildRequires:	jack-audio-connection-kit-devel
BuildRequires:	liblo-devel
BuildRequires:	/usr/bin/scons

Requires:	hicolor-icon-theme

%description
Minicomputer is a standalone Linux software synthesizer for creating 
experimental electronic sounds as its often used in but not limited to
Industrial music, IDM, EBM, Glitch, sound design and minimal electronic. It is
monophonic but can produce up to 8 different sounds at the same time. It uses
Jack as realtime audio infrastructure and can be controlled via Midi.

%prep
%setup -q -c -n MinicomputerV%{version}
%patch -P0 -p1 -b .linking
%patch -P1 -p1 -b .%{name}-gcc47.patch
%patch -P2 -p1 -b .%{name}-build-python3.patch

# Fix optflags
# SSE instruction set, which provides improved functionality, is only available in these archs:
%ifnarch %{ix86} x86_64 ia64
sed -i "s|\(^env.Append(CCFLAGS =\).*|\1 ['%{optflags}'.split() ])|" SConstruct
%else
sed -i "s|\(^env.Append(CCFLAGS =\).*|\1 ['%{optflags}'.split(),'-msse','-mfpmath=sse' ])|" SConstruct
%endif
sed -i "s|\(^guienv.Append(CPPFLAGS =\).*|\1 ['%{optflags}'.split() ])|" SConstruct

%build
scons %{?_smp_mflags}

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{_bindir}
install -pm 755 %{name}{,CPU} %{buildroot}%{_bindir}/

mkdir -p %{buildroot}%{_datadir}/applications
desktop-file-install				\
--dir=%{buildroot}%{_datadir}/applications	\
%{SOURCE1}

mkdir -p %{buildroot}%{_datadir}/icons/hicolor/32x32/apps
install -pm 644 %{name}.xpm \
	%{buildroot}%{_datadir}/icons/hicolor/32x32/apps

%files
%doc CHANGES README minicomputerManual.pdf factoryPresets
%license COPYING
%{_bindir}/%{name}*
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/32x32/apps/%{name}.xpm

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.41-40
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 25 2024 Miroslav Suchý <msuchy@redhat.com> - 1.41-39
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.41-38
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.41-37
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.41-36
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.41-35
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.41-34
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.41-33
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.41-32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.41-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.41-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.41-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Feb 12 2020 Petr Viktorin <pviktori@redhat.com> - 1.41-28
- Make the scons script compatible with Python 3

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.41-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Aug 03 2019 Orcan Ogetbil <oget[DOT]fedora[AT]gmail[DOT]com> - 1.41-26
- scons renamed to scons-2 in the recent Fedora package

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.41-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.41-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 20 2018 Adam Huffman <bloch@verdurin.com> - 1.41-23
- Add BR for gcc-c++

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.41-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.41-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 18 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.41-20
- Remove obsolete scriptlets

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.41-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.41-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.41-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.41-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.41-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 1.41-14
- Rebuilt for GCC 5 C++11 ABI change

* Thu Feb 19 2015 Rex Dieter <rdieter@fedoraproject.org> 1.41-13
- rebuild (fltk)

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.41-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.41-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.41-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.41-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.41-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Feb 28 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.41-7
- Rebuilt for c++ ABI breakage

* Sun Jan 08 2012 Adam Huffman <verdurin@fedoraproject.org> - 1.41-6
- rebuild for GCC 4.7
- patch for GCC 4.7

* Fri May 27 2011 Adam Huffman <bloch@verdurin.com> - 1.41-5
- rebuild for new fltk

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.41-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Jul 20 2010 Orcan Ogetbil <oget[DOT]fedora[AT]gmail[DOT]com> - 1.41-3
- Rebuild against new liblo-0.26

* Sat Feb 13 2010 Orcan Ogetbil <oget [DOT] fedora [AT] gmail [DOT] com> - 1.41-2
- Fix DSO linking RHBZ#565097

* Sat Feb 06 2010 Orcan Ogetbil <oget [DOT] fedora [AT] gmail [DOT] com> - 1.41-1
- Update to 1.41

* Sat Jan 30 2010 Orcan Ogetbil <oget [DOT] fedora [AT] gmail [DOT] com> - 1.4-1
- Update to 1.4

* Wed Aug 05 2009 Orcan Ogetbil <oget [DOT] fedora [AT] gmail [DOT] com> - 1.3-5
- Update .desktop file

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Sat Apr 25 2009 Orcan Ogetbil <oget [DOT] fedora [AT] gmail [DOT] com> - 1.3-3
- Cleanup the compiler flags

* Mon Apr 20 2009 Orcan Ogetbil <oget [DOT] fedora [AT] gmail [DOT] com> - 1.3-2
- Disable SSE on unsupported architectures

* Tue Mar 17 2009 Orcan Ogetbil <oget [DOT] fedora [AT] gmail [DOT] com> - 1.3-1
- Initial build
