
Summary:       Pro-audio reverb for JACK
Name:          zita-rev1
Version:       0.2.2
Release:       14%{?dist}
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:       GPL-2.0-or-later
URL:           http://kokkinizita.linuxaudio.org/
Source0:       http://kokkinizita.linuxaudio.org/linuxaudio/downloads/%{name}-%{version}.tar.bz2
# desktop file submitted upstream
Source1:       zita-rev1.desktop

# this has been submitted upstream
Patch0:        zita-rev1-fsf-address.patch

BuildRequires: make
BuildRequires: cairo-devel
BuildRequires: gcc-c++
BuildRequires: libpng-devel
BuildRequires: jack-audio-connection-kit-devel
BuildRequires: libXft-devel
BuildRequires: clthreads-devel
BuildRequires: clxclient-devel
BuildRequires: desktop-file-utils

%description
%{name} is a reworked version of the reverb originally developed for Aeolus. 
Its character is more 'hall' than 'plate', but it can be used on a wide 
variety of instruments or voices. 
It is not a spatialiser - the early reflections are different for the L and R 
inputs, but do not correspond to any real room. They have been tuned to match 
left and right sources to some extent.

In Stereo mode a dry/wet mix control is provided, so it can be used either as
an insert or in send/return mode. For mono just connect one of the two 
channels.

In Ambisonic mode (selected by the -B command line option) the only option is 
the send/return mode. 

%prep
%setup -q
%patch -P0 -p1

# use Fedora build flags
sed -e '/^CXXFLAGS += -march=native/d' -i source/Makefile

%build
%set_build_flags
cd source
%make_build PREFIX=%{_prefix}

%install
cd source
make DESTDIR=%{buildroot} PREFIX=%{_prefix} LIBDIR=%{_lib} install

# .desktop file
mkdir -p %{buildroot}%{_datadir}/applications
desktop-file-install  \
   --dir=%{buildroot}%{_datadir}/applications %{SOURCE1}

mkdir -p %{buildroot}%{_datadir}/pixmaps
install -m 644 %{_builddir}/%{name}-%{version}/doc/redzita.png %{buildroot}%{_datadir}/pixmaps/%{name}.png

%files
%doc AUTHORS doc/*
%license COPYING
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_datadir}/pixmaps/%{name}.png
%{_datadir}/applications/%{name}.desktop



%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.2-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 26 2024 Miroslav Suchý <msuchy@redhat.com> - 0.2.2-13
- convert license to SPDX

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.2-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.2-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Thu Jan 28 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Feb 05 2019 Guido Aulisi <guido.aulisi@gmail.com> - 0.2.2-1
- New upstream release 0.2.2

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.1-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.1-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sun Mar 11 2018 Orcan Ogetbil <oget [DOT] fedora [AT] gmail [DOT] com> - 0.2.1-18
- Use Fedora link flags
- Add BR: gcc-c++
- Some cleanup

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.1-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.1-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.1-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.1-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.1-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 0.2.1-11
- Rebuilt for GCC 5 C++11 ABI change

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sun Jul 22 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Fri Nov 11 2011 Brendan Jones <brendan.jones.it@gmail.com> - 0.2.1-4
- add desktop file and icon

* Sat Nov 05 2011 Brendan Jones <brendan.jones.it@gmail.com> - 0.2.1-3
- remove unnecessary BuildRoot tag

* Fri Nov 04 2011 Brendan Jones <brendan.jones.it@gmail.com> - 0.2.1-2
- remove file permissions

* Wed Oct 26 2011 Brendan Jones <brendan.jones.it@gmail.com> - 0.2.1-1
- initial build

