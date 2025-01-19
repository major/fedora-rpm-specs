Name:           linpsk
Version:        1.3.5
Release:        19%{?dist}
Summary:        Psk31 and RTTY program for Linux

# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
URL:            http://linpsk.sourceforge.net/
Source0:        http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
# Add .desktop file
Source1:        %{name}.desktop
# Install wrapper
Source2:        %{name}.sh.in
# Hi-res icon, rhbz#1157554
Source3:        %{name}_64x64.png

# Patch asoundrc file for default sound card (device 0)
Patch0:         linpsk-1.1-3.sound.conf.patch
Patch1:         linpsk-comparison.patch


BuildRequires:  fftw-devel
BuildRequires:  qt-devel
BuildRequires:  alsa-lib-devel
BuildRequires:  desktop-file-utils
BuildRequires: make

#Requires:

# Spelling error in desc. is intentional. Hobby jargon ignore rpmlint warnings.
%description
LinPsk is a program for operating on digital modes running on Linux.
LinPsk supports BPSK, QPSK and RTTY at the moment.
Main features are:
* the simultaneous decoding of up to four channels.
* The different digital modes may be mixed
* You can define a trigger on each channel to be notified if a text of your
  choice is detected.
* You can log each received channel at a file.
* For easy qso'ing you can define macros and for larger texts to be send you
  can use two files.
* You can view the signal as spectrum or in a waterfall display. Both are
  scale-able in the frequency domain.
At the Moment RTTY only supports 45 baud and 1.5 stop-bits.

%prep
%setup -q

#fix permissions for debuginfo files
chmod 0644 src/{rttydemodulator.cpp,rttydemodulator.h}

%patch -P0 -p1 -b 3.sound.conf
%patch -P1 -p1 -b comparison

%build
%{qmake_qt4} -unix -o Makefile %{name}.pro
make %{?_smp_mflags} CFLAGS="$RPM_OPT_FLAGS"

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{_bindir}

# Move original binary to libexecdir
mkdir -p %{buildroot}/%{_libexecdir}/
install -m 755 %{name} %{buildroot}%{_libexecdir}/%{name}-bin

# Install wrapper script
install -p -D -m 0755 %{SOURCE2} %{buildroot}/%{_bindir}/%{name}

# Install default sound configuration file
mkdir -p %{buildroot}/%{_sysconfdir}/skel/.%{name}/
install -p -D -m 0644 asoundrc %{buildroot}/%{_sysconfdir}/skel/.%{name}/asoundrc

# Install provided icon
mkdir -p %{buildroot}%{_datadir}/pixmaps/
cp %{SOURCE3} %{buildroot}%{_datadir}/pixmaps/%{name}.png
# no upstream .desktop
desktop-file-install \
        --dir=%{buildroot}%{_datadir}/applications %{SOURCE1}
# --vendor obsolete per new guidlines but leaving it in because
# this is an existing package with vendor previously installed

#Remove development files
find %{buildroot} -type f -name "*.a" -exec rm -f {} ';'

%files
%doc COPYING ChangeLog README
%{_bindir}/%{name}
%{_datadir}/pixmaps/%{name}.png
%{_datadir}/applications/*%{name}.desktop
%config(noreplace) %{_sysconfdir}/skel/.%{name}/asoundrc
%{_libexecdir}/%{name}-bin

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.5-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 26 2024 Miroslav Suchý <msuchy@redhat.com> - 1.3.5-18
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.5-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.5-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.5-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.5-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.5-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.5-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.5-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.5-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.5-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.5-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Jeff Law <law@redhat.com> - 1.3.5-7
- Avoid ordered pointer comparison against 0 which is an error in C++17

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.5-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jan 17 2018 Jaroslav Škarvada <jskarvad@redhat.com> - 1.3.5-1
- New version
  Resolves: rhbz#1420142

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Feb 02 2016 Rex Dieter <rdieter@fedoraproject.org> - 1.2-8
- use %%qmake_qt4 macro to ensure proper build flags

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 1.2-6
- Rebuilt for GCC 5 C++11 ABI change

* Mon Nov 24 2014 Jaroslav Škarvada <jskarvad@redhat.com> - 1.2-5
- Used 64x64 icon from SVN
  Resolves: rhbz#1157554

* Fri Nov 21 2014 Jaroslav Škarvada <jskarvad@redhat.com> - 1.2-4
- Switched to built-in icon

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Jan  3 2014 Jaroslav Škarvada <jskarvad@redhat.com> - 1.2-1
- New version
  Resolves: rhbz#1046658
- Dropped compile-fix patch (not needed)
- Various minor fixes

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Apr 26 2013 Jon Ciesla <limburgher@gmail.com> - 1.1-9
- Drop desktop vendor tag.

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed Jan 11 2012 Jaroslav Škarvada <jskarvad@redhat.com> - 1.1-6
- Fixed FTBFS by compile-fix patch
  Resolves: rhbz#715960
- Minor cosmetic changes

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Feb 1 2011 Randall 'Randy' Berry <dp67@fedoraproject.org>  - 1.1-4
- Rebuild to fix broken deps

* Sat May 1 2010 Randall 'Randy' Berry <dp67@fedoraproject.org>  - 1.1-3
- Test build for new spec
- Add wrapper script
- Add upstream icon

* Fri Apr 30 2010 Jon Ciesla <limb@jcomserv.net>  - 1.1-2
- Build, doc fixes.

* Fri Apr 30 2010 Randall 'Randy' Berry <dp67@fedoraproject.org>  - 1.1-1
- Upstream update to 1.1

* Sun Apr 18 2010 Randall 'Randy' Berry <dp67@fedoraproject.org>  - 0.9-8
- Correct .desktop file categories now includes Network;HamRadio;

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Sat Mar 21 2009 Robert Scheck <robert@fedoraproject.org> 0.9-6
- Rebuilt against libtool 2.2

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Tue Sep 16 2008 Tom "spot" Callaway <tcallawa@redhat.com> 0.9-4
- BR: qt3-devel

* Thu Feb 28 2008 Robert 'Bob' Jensen <bob@bobjensen.com> 0.9-3
- Add .desktop and icon for GUI application
- Submit for review

* Thu Nov 22 2007 Sindre Pedersen Bjørdal <foolish@guezz.net> 0.9-2
- Update License to GPLv2+
- Fix permissions for src files

* Thu Nov 22 2007 Robert 'Bob' Jensen <bob@bobjensen.com> 0.9-1
- Correct License

* Tue May 15 2007 Robert 'Bob' Jensen <bob@bobjensen.com> 0.9-0
- Initial RPM release

