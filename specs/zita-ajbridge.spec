Summary: Allows ALSA devices to be JACK clients
Name: zita-ajbridge
Version: 0.8.4
Release: 12%{?dist}
# Automatically converted from old format: GPLv3 - review is highly recommended.
License: GPL-3.0-only
URL: https://kokkinizita.linuxaudio.org/linuxaudio/
Source0: https://kokkinizita.linuxaudio.org/linuxaudio/downloads/%{name}-%{version}.tar.bz2

BuildRequires: make
BuildRequires: pkgconfig(jack)
BuildRequires: pkgconfig(alsa)
BuildRequires: zita-resampler-devel
BuildRequires: zita-alsa-pcmi-devel
BuildRequires: gcc-c++

%description
Zita-ajbridge provides two applications, zita-a2j and zita-j2a. They
allow to use an ALSA device as a Jack client, to provide additional
capture (a2j) or playback (j2a) channels. Functionally these are
equivalent to the alsa_in and alsa_out clients that come with Jack,
but they provide much better audio quality. The resampling ratio will
typically be stable within 1 PPM and change only very smoothly. Delay
will be stable as well even under worst case conditions, e.g. the Jack
client running near the end of the cycle.

%prep
%setup -q

%build
rm -rf $RPM_BUILD_ROOT

# Force Fedora's optflags
sed -i 's|-O2|%{optflags}|' source/Makefile

pushd source
make %{?_smp_mflags}
popd

%install
pushd source
mkdir -p $RPM_BUILD_ROOT%{_bindir}
mkdir -p $RPM_BUILD_ROOT%{_mandir}/man1
make PREFIX=%{_prefix} DESTDIR=$RPM_BUILD_ROOT install
popd

%files
%doc AUTHORS README
%license COPYING
%{_bindir}/zita-a2j
%{_bindir}/zita-j2a
%{_mandir}/man1/zita-a2j.*
%{_mandir}/man1/zita-j2a.*
%{_mandir}/man1/zita-ajbridge.*

%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.4-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Jul 29 2024 Miroslav Suchý <msuchy@redhat.com> - 0.8.4-11
- convert license to SPDX

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.4-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.4-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.4-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.4-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Thu Jan 28 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Apr 06 2020 - Erich Eickmeyer <erich@ericheickmeyer.com> 0.8.4-1
- Updated to 0.8.4

* Sat Feb 15 2020 - Erich Eickmeyer <erich@ericheickmeyer.com> 0.8.2-3
- Initial relase for Fedora

* Fri Dec 13 2019 - David Va <davidva AT tuta DOT io> 0.8.2-2
- Rebuilt

* Fri Sep 07 2018 - David Va <davidva AT tuta DOT io> 0.8.2-1
- Updated to 0.8.2

* Thu Aug 10 2017 David Vásquez <davidjeremias82 AT gmail DOT com> - 0.7.0-1
- Updated to 0.7.0
- Upstream

* Thu Sep 22 2016 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> - 0.6.0-1
- update to 0.6.0

* Wed Aug  6 2014 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> - 0.4.0-1
- initial build.
