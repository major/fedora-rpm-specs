
Summary:       JACK and ALSA Audio Analyzer
Name:          jaaa
Version:       0.8.4
Release:       15%{?dist}
License:       GPLv2+
URL:           http://kokkinizita.linuxaudio.org/
Source0:       http://kokkinizita.linuxaudio.org/linuxaudio/downloads/%{name}-%{version}.tar.bz2
# desktop file submitted upstream
Source1:       %{name}.desktop
Source2:       %{name}.png

BuildRequires: alsa-lib-devel
BuildRequires: desktop-file-utils
BuildRequires: clthreads-devel >= 2.4.0
BuildRequires: clxclient-devel >= 3.9.0
BuildRequires: fftw-devel
BuildRequires: gcc
BuildRequires: gcc-c++
BuildRequires: jack-audio-connection-kit-devel
BuildRequires: libX11-devel
BuildRequires: libXft-devel
BuildRequires: zita-alsa-pcmi-devel >= 0.2.0
BuildRequires: make

%description
%{name} (JACK and ALSA Audio Analyzer, is an audio signal generator and
spectrum analyzer designed to make accurate measurements.

%prep
%setup -q
cd source
sed -i -e "s|-march=native|%{optflags}|" Makefile

%build
cd source
make "PREFIX=%{_prefix}" %{?_smp_mflags}

%install
cd source
make "DESTDIR=%{buildroot}" "PREFIX=%{_prefix}" install

mkdir -p %{buildroot}%{_datadir}/applications
desktop-file-install \
  --dir %{buildroot}%{_datadir}/applications    \
  %{SOURCE1}
mkdir -p %{buildroot}%{_datadir}/pixmaps
install -m 0644 %{SOURCE2} %{buildroot}%{_datadir}/pixmaps/

%files
%doc AUTHORS README
%license COPYING
%{_bindir}/*
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.png


%changelog
* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.4-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.4-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.4-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.4-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.4-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.4-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.4-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.4-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.4-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Feb 20 2018 Nils Philippsen <nils@tiptoe.de> - 0.8.4-4
- require gcc, gcc-c++ for building

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Mon Jul 31 2017 Nils Philippsen <nils@tiptoe.de> - 0.8.4-1
- version 0.8.4
- reorder and add some versions to build dependencies
- use %%license
- remove trailing whitespace

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 0.6.0-8
- Rebuilt for GCC 5 C++11 ABI change

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Nov 04 2011 Brendan Jones <brendan.jones.it@gmail.com> - 0.6.0-2
- Modified to Fedora packaging guidelines

* Wed Oct 26 2011 Brendan Jones <brendan.jones.it@gmail.com> - 0.6.0-1
- Copied from Planet CCRMA

