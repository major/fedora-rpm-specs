Name:           dsp
Version:        1.9
Release:        5%{?dist}
Summary:        An audio processing program with an interactive mode

# Everything is ISC
License:        ISC
URL:            https://github.com/bmc0/dsp
Source0:        https://github.com/bmc0/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  alsa-lib-devel
BuildRequires:  fftw-devel
BuildRequires:  ladspa-devel
BuildRequires:  libao-devel
BuildRequires:  libmad-devel
BuildRequires:  libsndfile-devel
BuildRequires:  libtool-ltdl-devel
BuildRequires:  pulseaudio-libs-devel
BuildRequires:  zita-convolver-devel
BuildRequires:  make


%description
dsp is an audio processing program with an interactive mode.


%package -n ladspa-dsp-plugin
Summary:        dsp's LADSPA frontend

Requires:       ladspa


%description -n ladspa-dsp-plugin
dsp's LADSPA frontend.


%prep
%autosetup -p1


%build
./configure --libdir=/%{_lib} --disable-ffmpeg

export CFLAGS="%{optflags}"
export CXXFLAGS="%{optflags}"
%make_build


%install
%make_install


%files
%license LICENSE
%doc README.md
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*


%files -n ladspa-dsp-plugin
%license LICENSE
%doc README.md
%{_libdir}/ladspa/ladspa_dsp.so


%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.9-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.9-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.9-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 14 2024 Sérgio Basto <sergio@serjux.com> - 1.9-1
- Update dsp to 1.9
- Migrated to SPDX license (noop)

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.6-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.6-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.6-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.6-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.6-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Apr 09 2020 Nikola Forró <nforro@redhat.com> - 1.6-2
- Fix typo in gcc-c++ build dependency

* Thu Feb 27 2020 Nikola Forró <nforro@redhat.com> - 1.6-1
- Initial package
