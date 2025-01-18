Name:           cava
Version:        0.10.2
Release:        4%{?dist}
Summary:        Console-based Audio Visualizer for Alsa

License:        MIT
URL:            https://github.com/karlstav/cava
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:  alsa-lib-devel
BuildRequires:  fftw-devel
BuildRequires:  pulseaudio-libs-devel
BuildRequires:  libtool
BuildRequires:  ncurses-devel
BuildRequires:  iniparser-devel
BuildRequires: make

%description
C.A.V.A. is a bar spectrum analyzer for audio using ALSA for input.

%prep
%autosetup -p1
./autogen.sh


%build
%configure FONT_DIR=/lib/kbd/consolefonts LIBS=-lrt
make %{?_smp_mflags} \
    cava_LDFLAGS=


%install
%make_install
rm -f %{buildroot}%{_libdir}/libiniparser.{a,la,so}

%files
%license LICENSE
%doc README.md
%doc example_files
%{_bindir}/cava
/lib/kbd/consolefonts/cava.psf


%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Tue Jun 18 2024 David Cantrell <dcantrell@redhat.com> - 0.10.2-2
- Rebuild for iniparser-4.2.4

* Wed May 29 2024 Adam Williamson <awilliam@redhat.com> - 0.10.2-1
- updated to 0.10.2
- rebuild for newer iniparser

* Tue Jan 23 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.2-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.2-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.2-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.2-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 22 2020 Lars Kellogg-Stedman <lars@redhat.com> - 0.7.2-7
- updated to 0.7.2

* Wed May 27 2020 Lars Kellogg-Stedman <lars@redhat.com> - 0.7.0-6
- update to 0.7.0

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon May 07 2018 Lars Kellogg-Stedman <lars@oddbit.com> - 0.6.1-1
- update to 0.6.1

* Mon Mar 12 2018 Lars Kellogg-Stedman <lars@oddbit.com> - 0.6.0-8
- fixes from review (rhbz#1553999): remove defattr
- correct typo in URL
- stop mixing spaces and tabs

* Sat Mar 10 2018 Lars Kellogg-Stedman <lars@oddbit.com> - 0.6.0-5
- fixes from review (rhbz#1553999): remove bundled iniparser

* Sat Mar 10 2018 Lars Kellogg-Stedman <lars@oddbit.com> - 0.6.0-3
- rpmlint fixes

* Fri Mar 09 2018 Lars Kellogg-Stedman <lars@oddbit.com> - 0.6.0-2
- initial package
