%{?mingw_package_header}

%global pkgname speexdsp

Name:           mingw-%{pkgname}
Version:        1.2.1
Release:        5%{?dist}
Summary:        A voice compression format (DSP)
# Automatically converted from old format: BSD - review is highly recommended.
License:        LicenseRef-Callaway-BSD
URL:            http://www.speex.org/
Source0:        http://downloads.xiph.org/releases/speex/%{pkgname}-%{version}.tar.gz

BuildArch:      noarch

BuildRequires: make
BuildRequires:  mingw32-filesystem >= 95
BuildRequires:  mingw32-gcc

BuildRequires:  mingw64-filesystem >= 95
BuildRequires:  mingw64-gcc


%description
Speex is a patent-free compression format designed especially for
speech. It is specialized for voice communications at low bit-rates in
the 2-45 kbps range. Possible applications include Voice over IP
(VoIP), Internet audio streaming, audio books, and archiving of speech
data (e.g. voice mail).

This is the DSP package, see the speex package for the codec part.


%package -n mingw32-%{pkgname}
Summary:        A voice compression format (DSP)

%description -n mingw32-%{pkgname}
Speex is a patent-free compression format designed especially for
speech. It is specialized for voice communications at low bit-rates in
the 2-45 kbps range. Possible applications include Voice over IP
(VoIP), Internet audio streaming, audio books, and archiving of speech
data (e.g. voice mail).

This is the DSP package, see the speex package for the codec part.


%package -n mingw64-%{pkgname}
Summary:        A voice compression format (DSP)

%description -n mingw64-%{pkgname}
Speex is a patent-free compression format designed especially for
speech. It is specialized for voice communications at low bit-rates in
the 2-45 kbps range. Possible applications include Voice over IP
(VoIP), Internet audio streaming, audio books, and archiving of speech
data (e.g. voice mail).

This is the DSP package, see the speex package for the codec part.


%{?mingw_debug_package}


%prep
%setup -q -n %{pkgname}-%{version}


%build
%{mingw_configure} --disable-static
%mingw_make %{?_smp_mflags}


%install
%mingw_make install DESTDIR=%{buildroot}


%files -n mingw32-%{pkgname}
%license COPYING
%{mingw32_bindir}/libspeexdsp-1.dll
%{mingw32_libdir}/libspeexdsp.dll.a
%{mingw32_libdir}/pkgconfig/speexdsp.pc
%{mingw32_includedir}/speex/speex_echo.h
%{mingw32_includedir}/speex/speex_jitter.h
%{mingw32_includedir}/speex/speex_preprocess.h
%{mingw32_includedir}/speex/speex_resampler.h
%{mingw32_includedir}/speex/speexdsp_config_types.h
%{mingw32_includedir}/speex/speexdsp_types.h
%{mingw32_docdir}/speexdsp/manual.pdf

%files -n mingw64-%{pkgname}
%license COPYING
%{mingw64_bindir}/libspeexdsp-1.dll
%{mingw64_libdir}/libspeexdsp.dll.a
%{mingw64_libdir}/pkgconfig/speexdsp.pc
%{mingw64_includedir}/speex/speex_echo.h
%{mingw64_includedir}/speex/speex_jitter.h
%{mingw64_includedir}/speex/speex_preprocess.h
%{mingw64_includedir}/speex/speex_resampler.h
%{mingw64_includedir}/speex/speexdsp_config_types.h
%{mingw64_includedir}/speex/speexdsp_types.h
%{mingw64_docdir}/speexdsp/manual.pdf

# See https://fedoraproject.org/wiki/Packaging:MinGW

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Sep 02 2024 Miroslav Suchý <msuchy@redhat.com> - 1.2.1-4
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild


* Thu Feb 22 2024 Michał Janiszewski <janisozaur+speexdspfedoramingw@gmail.com> - 1.2.1-2
- Rebuild with properly uploaded sources

* Wed Feb 21 2024 Michał Janiszewski <janisozaur+speexdspfedoramingw@gmail.com> - 1.2.1-1
- Update to 1.2.1 and fix build issues

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Mar 25 2022 Sandro Mani <manisandro@gmail.com> - 1.2.0-8
- Rebuild with mingw-gcc-12

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jul 04 2019 Michał Janiszewski <janisozaur+speexdspfedoramingw@gmail.com> - 1.2.0-1
- Initial MinGW packaging
