Name:           mimic
Version:        1.3.0.1
Release:        15%{?dist}
Summary:        Mycroft's TTS engine

# Automatically converted from old format: BSD - review is highly recommended.
License:        LicenseRef-Callaway-BSD
URL:            https://mimic.mycroft.ai/
Source0:        https://github.com/MycroftAI/mimic/archive/%{version}.tar.gz
Patch0:         mimic-fix-pulse.patch
# upstream fix for GCC 12
Patch1:         mimic-gcc12.patch

BuildRequires: make
BuildRequires:  automake autoconf libtool
BuildRequires:  alsa-lib-devel
BuildRequires:  libcurl-devel
BuildRequires:  libicu-devel
BuildRequires:  pulseaudio-libs-devel


%description
Mimic is a fast, lightweight Text-to-speech engine developed by Mycroft A.I. 
and VocalID, based on Carnegie Mellon University’s FLITE software. Mimic takes 
in text and reads it out loud to create a high quality voice. Mimic's 
low-latency, small resource footprint, and good quality voices set it apart 
from other open source text-to-speech projects.

%package devel
Summary: Development files for Mimic
Requires: %{name}%{?_isa} = %{version}-%{release}

%description devel
Development files for Mimic, a small, fast speech synthesis engine.


%prep
%autosetup -p1 -n %{name}1-%{version}

%build
# This package triggers a fault in GCC when building with LTO enabled.
# Disable LTO until GCC is fixed
%define _lto_cflags %{nil}

autoreconf -vif
%configure --enable-shared --with-audio=alsa --with-audio=pulseaudio
%{make_build}

%install
%{make_install}

# Remove static libraries and libtool archives
find %{buildroot} -type f -name "*.a" -delete
find %{buildroot} -type f -name "*.la" -delete


%ldconfig_scriptlets


%files
%license COPYING
%doc ACKNOWLEDGEMENTS
%{_libdir}/libttsmimic*.so.*
%{_bindir}/mimic*
%{_bindir}/compile_regexes
%{_bindir}/t2p
%{_datadir}/man/man1/mimic.1*
%{_datadir}/%{name}

%files devel
%{_libdir}/libttsmimic*.so
%{_libdir}/pkgconfig/mimic.pc
%{_includedir}/ttsmimic

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0.1-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Sep 02 2024 Miroslav Suchý <msuchy@redhat.com> - 1.3.0.1-14
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0.1-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0.1-4
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jul 10 2020 Jeff Law <law@redhat.com> - 1.3.0.1-2
- Disable LTO

* Sun May 10 2020 Peter Robinson <pbrobinson@fedoraproject.org> - 1.3.0.1-1
- New upstream 1.3.0.1

* Mon Feb 24 2020 Peter Robinson <pbrobinson@fedoraproject.org> - 1.3.0.0-1
- New upstream 1.3.0.0

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0.2-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Nov 01 2019 Pete Walter <pwalter@fedoraproject.org> - 1.2.0.2-13
- Rebuild for ICU 65

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0.2-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Jul  2 2019 Peter Robinson <pbrobinson@fedoraproject.org> 1.2.0.2-11
- Fix building against PulseAudio 1.1

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Jan 23 2019 Pete Walter <pwalter@fedoraproject.org> - 1.2.0.2-9
- Rebuild for ICU 63

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jul 10 2018 Pete Walter <pwalter@fedoraproject.org> - 1.2.0.2-7
- Rebuild for ICU 62

* Mon Apr 30 2018 Pete Walter <pwalter@fedoraproject.org> - 1.2.0.2-6
- Rebuild for ICU 61.1

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Nov 30 2017 Pete Walter <pwalter@fedoraproject.org> - 1.2.0.2-4
- Rebuild for ICU 60.1

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Mar 19 2017 Peter Robinson <pbrobinson@fedoraproject.org> 1.2.0.2-1
- New upstream 1.2.0.2
- Package review updates

* Fri Oct 28 2016 Peter Robinson <pbrobinson@fedoraproject.org> 1.1.0-1
- Initial package
