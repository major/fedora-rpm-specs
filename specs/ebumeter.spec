Name:          ebumeter
Summary:       Loudness measurement according to EBU-R128
Version:       0.4.2
Release:       16%{?dist}
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:       GPL-2.0-or-later
URL:           http://kokkinizita.linuxaudio.org/linuxaudio
Source0:       http://kokkinizita.linuxaudio.org/linuxaudio/downloads/%{name}-%{version}.tar.bz2
Source1:       %{name}.desktop
Source2:       %{name}.png
# correct FSF address
Patch0:        %{name}-0.4.0-fsf.patch

BuildRequires: desktop-file-utils
BuildRequires: gcc-c++
BuildRequires: libsndfile-devel
BuildRequires: clthreads-devel
BuildRequires: clxclient-devel
BuildRequires: jack-audio-connection-kit-devel
BuildRequires: libXft-devel
BuildRequires: libpng-devel
BuildRequires: zita-resampler-devel
BuildRequires: make

%description
Loudness measurement according to EBU-R128. Presented at LAC 2011 
(thanks to Joern Nettingsmeier!). The only documentation available 
at the moment are the paper, the presentation, slides and the video 
of the LAC 2011 session.

%prep
%setup -q
%patch -P0 -p1
pushd source
sed -i -e "s|-march=native|%{optflags}|" Makefile

%build
pushd source
make PREFIX=%{_prefix} LDFLAGS="$RPM_LD_FLAGS" %{?_smp_mflags}
popd

%install
pushd source
make DESTDIR=%{buildroot} PREFIX=%{_prefix} %{?_smp_mflags} install
popd

mkdir -p %{buildroot}%{_datadir}/applications
desktop-file-install \
  --dir %{buildroot}%{_datadir}/applications    \
  %{SOURCE1}
mkdir -p %{buildroot}%{_datadir}/pixmaps
install -pm 644 %{SOURCE2} \
    %{buildroot}%{_datadir}/pixmaps/%{name}.png
    
%files
%doc AUTHORS README doc/*pdf
%license COPYING
%{_bindir}/%{name}
%{_bindir}/ebur128
%{_datadir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.png

%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.2-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 25 2024 Miroslav Suchý <msuchy@redhat.com> - 0.4.2-15
- convert license to SPDX

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.2-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.2-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.2-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.2-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Sep 08 2018 Nils Philippsen <nils@tiptoe.de> - 0.4.2-1
- version 0.4.2

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Mar 12 2018 Orcan Ogetbil <oget [DOT] fedora [AT] gmail [DOT] com> - 0.4.0-1
- Update version

* Mon Mar 12 2018 Orcan Ogetbil <oget [DOT] fedora [AT] gmail [DOT] com> - 0.1.0-20
- Use Fedora link flags
- Add BR: gcc-c++
- Some cleanup

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 0.1.0-13
- Rebuilt for GCC 5 C++11 ABI change

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Mar 06 2012 Brendan Jones <brendan.jones.it@gmail.com> 0.1.0-7
- desktop file changes and cosmetics

* Tue Mar 06 2012 Brendan Jones <brendan.jones.it@gmail.com> 0.1.0-5
- patch FSF address, preserve icon permissions

* Tue Feb 14 2012 Brendan Jones <brendan.jones.it@gmail.com> 0.1.0-4
- use the upstream icon in pixmaps, remove hicolor scriptlets

* Mon Feb 13 2012 Brendan Jones <brendan.jones.it@gmail.com> 0.1.0-3
- move desktop categories into source

* Fri Feb 10 2012 Brendan Jones <brendan.jones.it@gmail.com> 0.1.0-2
- modified to Fedora package guidelines

* Wed Nov 16 2011 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 0.1.0-1
- initial build
