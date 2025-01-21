Name:           xpsk31
Version:        3.6.1
Release:        15%{?dist}
Summary:        GTK+ graphical version of lpsk31 for Ham Radio

# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
URL:            http://www.5b4az.org/

Source0:        http://www.5b4az.org/pkg/psk31/%{name}/%{name}-%{version}.tar.bz2
Source1:        %{name}.desktop
Source2:        %{name}.png
Source3:        %{name}.sh

Patch0:         xpsk31-1.2-configure.patch
Patch1:         xpsk31-no_home.patch
Patch2:         xpsk31-configure-c99.patch

BuildRequires: make
BuildRequires: gcc
BuildRequires: autoconf automake libtool
BuildRequires: alsa-lib-devel
BuildRequires: gettext-devel
BuildRequires: glib2-devel
BuildRequires: gtk3-devel
BuildRequires: desktop-file-utils


%description
xpsk31 is a GTK+ graphical version of lpsk31, using the same basic signal 
decoding and encoding engine but controlled by the user via the GUI. In 
addition it has a FFT-derived "waterfall" display of the incoming signal and a 
"magniphase" display that shows the magnitude, phase and frequency error of the
psk31 signal.

%prep
%autosetup -p1
#autoreconf -fiv
./autogen.sh


%build
%configure --program-suffix=.bin
%make_build


%install
%make_install

# no upstream .desktop or icon yet
mkdir -p $RPM_BUILD_ROOT%{_datadir}/pixmaps/
cp %{SOURCE2} ${RPM_BUILD_ROOT}%{_datadir}/pixmaps/%{name}.png
desktop-file-install %{SOURCE1} --dir=%{buildroot}%{_datadir}/applications/

# Install wrapper to desl with config files needed in $HOME.
install -pm 0755 %{SOURCE3} %{buildroot}%{_bindir}/%{name}


%files
%doc AUTHORS README doc/{*.html,*.pdf}
%license COPYING
%{_bindir}/%{name}*
%{_datadir}/pixmaps/%{name}.png
%{_datadir}/applications/*%{name}.desktop
%{_datadir}/%{name}/
%{_mandir}/man1/%{name}.1.gz


%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 3.6.1-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 26 2024 Miroslav Suchý <msuchy@redhat.com> - 3.6.1-14
- convert license to SPDX

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.6.1-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.6.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.6.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.6.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Tue Jan 10 2023 Florian Weimer <fweimer@redhat.com> - 3.6.1-9
- C99 compatibility fix for the configure script (#2159651)

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.6.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.6.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.6.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Thu Jan 28 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.6.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.6.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.6.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.6.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Mar 03 2019 Richard Shaw <hobbes1069@gmail.com> - 3.6.1-1
- Update to 3.6.1.

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sun Jul 22 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Dec 06 2011 Adam Jackson <ajax@redhat.com> - 1.2-7
- Rebuild for new libpng

* Thu Jul 15 2010 Randall "Randy" Berry, N3LRX <dp67@fedoraproject.org> - 1.2-6
- Fix .desktop file add category Network;HamRadio;

* Sun Feb 14 2010 Lucian Langa <cooly@gnome.eu.org> - 1.2-5
- -fix implicit dso linking (#564903)

* Mon Jul 27 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Fri Feb 27 2009 Lucian Langa <cooly@gnome.eu.org> - 1.2-3
- drop vendor from desktop file install
- ustream modified source

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sat Aug  2 2008 Lucian Langa <cooly@gnome.eu.org> - 1.2-1
- update to 1.2 release

* Wed Jul 16 2008 Lucian Langa <cooly@gnome.eu.org> - 0.8-2
- proper handle of configure
- fix desktop file
- misc cleanups

* Sat Mar 01 2008 Robert 'Bob' Jensen <bob@bobjensen.com> - 0.8-1
- Upstream Version Bump

* Thu Feb 28 2008 Robert 'Bob' Jensen <bob@bobjensen.com> 0.7-3
- Add .desktop and icon for GUI application
- Submit for review

* Tue Nov 20 2007 Robert 'Bob' Jensen <bob@bobjensen.com> 0.7-2
- Fix files section

* Tue Nov 20 2007 Robert 'Bob' Jensen <bob@bobjensen.com> 0.7-1
- Initial Fedora SPEC


