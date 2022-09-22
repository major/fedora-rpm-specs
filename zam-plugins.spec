%global gittag 3.14
%global dpf DPF

# Disable lto
%define _lto_cflags %{nil}

# DPF git submodule
%global commit1 08669d1bc30c6e971fde800eade4ca40104ba8b2
%global shortcommit1 %(c=%{commit1}; echo ${c:0:7})

Name:           zam-plugins
Version:        %{gittag}
Release:        5%{?dist}
Summary:        A collection of LV2/LADSPA/JACK audio plugins

License:        GPLv2+ and ISC
URL:            http://www.zamaudio.com/
Source0:        https://github.com/zamaudio/%{name}/archive/%{gittag}/%{name}-%{version}.tar.gz
Source1:        https://github.com/DISTRHO/DPF/archive/%{commit1}/%{dpf}-%{shortcommit1}.tar.gz

BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  make
BuildRequires:  jack-audio-connection-kit-devel
BuildRequires:  libX11-devel
BuildRequires:  mesa-libGL-devel
BuildRequires:  liblo-devel
BuildRequires:  lv2-devel >= 1.8.1
BuildRequires:  ladspa-devel
BuildRequires:  fftw-devel >= 3.3.5
BuildRequires:  libsamplerate-devel
BuildRequires:  zita-convolver-devel >= 4.0.0

%package -n lv2-zam-plugins
Summary:        A collection of LV2/LADSPA/JACK audio plugins. LV2 version
Requires:       lv2 >= 1.8.1

%package -n ladspa-zam-plugins
Summary:        A collection of LV2/LADSPA/JACK audio plugins. LADSPA version
Requires:       ladspa

%description
zam-plugins is a collection of LV2/LADSPA/VST/JACK audio plugins
for sound processing developed in-house at ZamAudio.

%description -n lv2-zam-plugins
zam-plugins is a collection of LV2/LADSPA/VST/JACK audio plugins
for sound processing developed in-house at ZamAudio.
This is the LV2 version.

%description -n ladspa-zam-plugins
zam-plugins is a collection of LV2/LADSPA/VST/JACK audio plugins
for sound processing developed in-house at ZamAudio.
This is the LADSPA version.

%prep
%autosetup -a 1 -p 1
# Move submodule DPF to main source directory
rmdir dpf
mv %{dpf}-%{commit1} dpf

%build
%set_build_flags
%make_build VERBOSE=true PREFIX=%{_prefix} LIBDIR=%{_lib} USE_SYSTEM_LIBS=1 SKIP_STRIPPING=true

%install
%make_install VERBOSE=true PREFIX=%{_prefix} LIBDIR=%{_lib} USE_SYSTEM_LIBS=1
# We don't need VST and DSSI plugins
rm -rf %{buildroot}%{_libdir}/vst %{buildroot}/*-dssi*
# Remove executable bit from .ttl files
chmod -x %{buildroot}%{_libdir}/lv2/*.lv2/*.ttl

%files
%{_bindir}/*
%license COPYING
%doc README.md

%files -n lv2-zam-plugins
%{_libdir}/lv2/*
%license COPYING
%doc README.md

%files -n ladspa-zam-plugins
%{_libdir}/ladspa/*
%license COPYING
%doc README.md

%changelog
* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.14-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.14-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.14-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Thu Jan 28 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.14-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Dec 21 11:03:20 CET 2020 Guido Aulisi <guido.aulisi@gmail.com> - 3.14-1
- Version 3.14
- Add BR make

* Wed Aug 05 2020 Guido Aulisi <guido.aulisi@gmail.com> - 3.13-2
- Fix FTBFS on f33
- Disable lto
- Some spec cleanup

* Fri Jul 31 2020 Guido Aulisi <guido.aulisi@gmail.com> - 3.13-1
- Version 3.13

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.12-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.12-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Dec 20 2019 Guido Aulisi <guido.aulisi@gmail.com> - 3.12-1
- Version 3.12

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jun 13 2019 Guido Aulisi <guido.aulisi@gmail.com> - 3.11-1
- Version 3.11

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.10-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.10-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue May 15 2018 Guido Aulisi <guido.aulisi@gmail.com> - 3.10-3
- Escape macros in changelog

* Sun May 13 2018 Guido Aulisi <guido.aulisi@gmail.com> - 3.10-2
- Use set_build_flags macro
- Document Patch0

* Wed May 9 2018 Guido Aulisi <guido.aulisi@gmail.com> - 3.10-1
- Version 3.10
