
Summary:       Audio autotuner for JACK
Name:          zita-at1
Version:       0.6.2
Release:       15%{?dist}
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:       GPL-2.0-or-later
URL:           http://kokkinizita.linuxaudio.org/
Source0:       http://kokkinizita.linuxaudio.org/linuxaudio/downloads/%{name}-%{version}.tar.bz2
# submitted upstream
Source1:       %{name}.desktop

BuildRequires: make
BuildRequires: cairo-devel
BuildRequires: fftw3-devel
BuildRequires: gcc-c++
BuildRequires: zita-resampler-devel
BuildRequires: libpng-devel
BuildRequires: jack-audio-connection-kit-devel
BuildRequires: zita-alsa-pcmi-devel
BuildRequires: clthreads-devel
BuildRequires: clxclient-devel >= 3.9.0
BuildRequires: libXft-devel
BuildRequires: desktop-file-utils

%description
%{name} is an 'autotuner', normally used to correct the pitch of a voice 
singing (slightly) out of tune.

%prep
%setup -q

sed -i -e 's|-march=native|%{optflags}|' -e 's|-ffast-math||' \
    source/Makefile

%build
cd source
make PREFIX=%{_prefix} LDFLAGS="$RPM_LD_FLAGS" %{?_smp_mflags}

%install
cd source
make DESTDIR=%{buildroot} PREFIX=%{_prefix} LIBDIR=%{_lib} install

# .desktop file
mkdir -p %{buildroot}%{_datadir}/applications
desktop-file-install  \
   --dir=%{buildroot}%{_datadir}/applications %{SOURCE1}

mkdir -p %{buildroot}%{_datadir}/pixmaps
install -m 644 %{_builddir}/%{name}-%{version}/doc/redzita.png \
    %{buildroot}%{_datadir}/pixmaps/%{name}.png


%files
%doc AUTHORS doc/*
%license COPYING
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.png

%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.2-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 26 2024 Miroslav Suchý <msuchy@redhat.com> - 0.6.2-14
- convert license to SPDX

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.2-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.2-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.2-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Thu Jan 28 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Sep 08 2018 Nils Philippsen <nils@tiptoe.de> - 0.6.2-1
- version 0.6.2

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sun Mar 11 2018 Orcan Ogetbil <oget [DOT] fedora [AT] gmail [DOT] com> - 0.4.0-7
- Use Fedora link flags
- Add BR: gcc-c++
- Some cleanup

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun Apr 24 2016 Brendan Jones <brendan.jones.it@gmail.com> 0.4.0-2
- Add missing BR

* Sun Apr 24 2016 Brendan Jones <brendan.jones.it@gmail.com> 0.4.0-1
- Update to 0.4.0

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.3-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.3-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 0.2.3-12
- Rebuilt for GCC 5 C++11 ABI change

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.3-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.3-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.3-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sun Jul 22 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed Jul 04 2012 Brendan Jones <brendan.jones.it@gmail.com> 0.2.3-6
- Rebuild for new zita-resampler

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sat Nov 19 2011 Brendan Jones <brendan.jones.it@gmail.com> - 0.2.3-4
- Removed -ffast-math
- Consistent use of macros

* Tue Nov 15 2011 Brendan Jones <brendan.jones.it@gmail.com> - 0.2.3-3
- Removed -msse flag removal for powerpc
- Comment patch and sources

* Fri Nov 11 2011 Brendan Jones <brendan.jones.it@gmail.com> - 0.2.3-2
- add desktop file and icon
- removed unneccessary constructs

* Wed Oct 26 2011 Brendan Jones <brendan.jones.it@gmail.com> - 0.2.3-1
- initial build

