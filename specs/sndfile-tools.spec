Name:           sndfile-tools
Version:        1.5
Release:        12%{?dist}
Summary:        A collection of programs to do interesting things with sound files

# The entire source is (GPLv2 or GPLv3) except src/jackplay.c, which is
# GPLv2+, and src/resample.c, which is BSD.
# Automatically converted from old format: (GPLv2 or GPLv3) and GPLv2+ and BSD - review is highly recommended.
License:        (GPL-2.0-only OR GPL-3.0-only) AND GPL-2.0-or-later AND LicenseRef-Callaway-BSD
URL:            https://github.com/libsndfile/%{name}
Source0:        https://github.com/libsndfile/%{name}/releases/download/%{version}/%{name}-%{version}.tar.bz2
# Missing man page
Source1:        https://raw.githubusercontent.com/libsndfile/%{name}/master/man/sndfile-waveform.1

# Patches from upstream
Patch0:         0001-Zero-initialize-sfinfo-in-resample.c-to-fix-Valgrind.patch
Patch1:         0002-Zero-initialize-SF_INFO-structures-everywhere-else-t.patch
Patch2:         0003-Fix-a-leaked-cairo-context-in-render_to_surface-in-w.patch
Patch3:         0001-Fix-76-in-which-Valgrind-reports-a-leaked-FontConfig.patch

BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  pkgconfig(sndfile)
BuildRequires:  pkgconfig(samplerate)
BuildRequires:  pkgconfig(fftw3) >= 0.15.0
BuildRequires:  pkgconfig(cairo)
BuildRequires:  pkgconfig(jack)
BuildRequires:  valgrind

%description
Sndfile-tools is a small collection of programs that use libsndfile
and other libraries to do useful things.
Included tools are:
sndfile-generate-chirp
sndfile-jackplay
sndfile-mix-to-mono
sndfile-resample
sndfile-spectrogram
sndfile-waveform


%prep
%autosetup -p1

%build
%configure
%make_build


%install
%make_install

# Install missing man page for sndfile-waveform
# Fixed upstream https://github.com/libsndfile/sndfile-tools/commit/9dbeefc470a3391afd3a64cc7f80a45f43f35a13
install -p -m 644 %{SOURCE1} %{buildroot}/%{_mandir}/man1/


%check
result="$(./tests/test-wrapper.sh)"
if echo "${result}" | grep -Ev ': ok$' >/dev/null
then
  exit 1
fi


%files
%license COPYING
%doc README AUTHORS
%{_bindir}/*
%{_pkgdocdir}/*
%{_mandir}/man1/*

%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Sep 04 2024 Miroslav Suchý <msuchy@redhat.com> - 1.5-11
- convert license to SPDX

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Sun May 16 2021 Guido Aulisi <guido.aulisi@gmail.com> - 1.5-3
- Add missing man page
- Patch tests

* Sun May 02 2021 Guido Aulisi <guido.aulisi@gmail.com> - 1.5-2
- Correct license
- Run tests

* Tue Apr 27 2021 Guido Aulisi <guido.aulisi@gmail.com> - 1.5-1
- Initial import (#1954842)
