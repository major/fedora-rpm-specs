# DPF git submodule
%global dpf_commit f60444f27480383005d488d82c834529fa1440f6
%global dpf_shortcommit %(c=%{dpf_commit}; echo ${c:0:7})
%global dpf_date 20250517

# pugl git submodule
%global pugl_commit d4d964f129b4bf999c53ba40381bd1095fafb649
%global pugl_shortcommit %(c=%{pugl_commit}; echo ${c:0:7})
%global pugl_date 20250208

Name:           zam-plugins
Version:        4.4
Release:        %autorelease
Summary:        A collection of audio plugins for LV2, LADSPA, JACK, CLAP, VST3

# Automatically converted from old format: GPLv2+ and ISC - review is highly recommended.
License:        GPL-2.0-or-later AND ISC
URL:            http://www.zamaudio.com/
Source0:        https://github.com/zamaudio/%{name}/archive/%{version}/%{name}-%{version}.tar.gz
Source1:        https://github.com/DISTRHO/DPF/archive/%{dpf_commit}/DPF-%{dpf_shortcommit}.tar.gz
Source2:        https://github.com/DISTRHO/pugl/archive/%{pugl_commit}/pugl-%{pugl_shortcommit}.tar.gz

BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  ladspa-devel
BuildRequires:  make
BuildRequires:  pkgconfig(jack)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(gl)
BuildRequires:  pkgconfig(liblo)
BuildRequires:  pkgconfig(lv2) >= 1.8.1
BuildRequires:  pkgconfig(fftw3f) >= 3.3.5
BuildRequires:  pkgconfig(samplerate)
BuildRequires:  zita-convolver-devel >= 4.0.0

Provides:       bundled(dpf) = 0~git%{dpf_date}.%{dpf_shortcommit}
Provides:       bundled(pugl) = 0~git%{pugl_date}.%{pugl_shortcommit}

%package -n lv2-zam-plugins
Summary:        A collection of LV2 audio plugins

%package -n ladspa-zam-plugins
Summary:        A collection of LADSPA audio plugins

%package -n clap-zam-plugins
Summary:        A collection of CLAP audio plugins

%package -n vst3-zam-plugins
Summary:        A collection of VST3 audio plugins

%description
This is a collection of LV2/LADSPA/VST/JACK audio plugins
for sound processing developed in-house at ZamAudio.

This package contains the standalone JACK programs.

%description -n lv2-zam-plugins
This is a collection of LV2 audio plugins for sound processing developed
in-house at ZamAudio.

%description -n ladspa-zam-plugins
This is a collection of LADSPA audio plugins for sound processing
developed in-house at ZamAudio.

%description -n clap-zam-plugins
This is a collection of CLAP audio plugins for sound processing
developed in-house at ZamAudio.

%description -n vst3-zam-plugins
This is a collection of VST3 audio plugins for sound processing
developed in-house at ZamAudio.

%prep
%setup -q -a 1
%setup -q -T -D -a 2

# Move submodule DPF to main source directory
rmdir dpf
mv DPF-%{dpf_commit} dpf

# Move submodule pugl to main source directory
rmdir dpf/dgl/src/pugl-upstream
mv pugl-%{pugl_commit} dpf/dgl/src/pugl-upstream

# Remove bundled zita-convolver, we want to use the packaged copy
rm -rf lib/zita-convolver*

%build
%set_build_flags

%global common_make_flags \\\
    VERBOSE=true \\\
    PREFIX="%{_prefix}" \\\
    LIBDIR="%{_lib}" \\\
    SKIP_STRIPPING=true \\\
    HAVE_ZITA_CONVOLVER=true

%make_build %common_make_flags

%install
%make_install %common_make_flags

# We don't need VST but the Makefiles make it hard to skip building
rm -rf %{buildroot}%{_libdir}/vst

chmod +x %{buildroot}%{_libdir}/*/{,*/}/*.so

%files
%{_bindir}/*
%license COPYING
%doc README.md

%files -n lv2-zam-plugins
%dir %{_libdir}/lv2
%{_libdir}/lv2/*
%license COPYING
%doc README.md

%files -n ladspa-zam-plugins
%dir %{_libdir}/ladspa
%{_libdir}/ladspa/*
%license COPYING
%doc README.md

%files -n clap-zam-plugins
%dir %{_libdir}/clap
%{_libdir}/clap/*
%license COPYING
%doc README.md

%files -n vst3-zam-plugins
%dir %{_libdir}/vst3
%{_libdir}/vst3/*
%license COPYING
%doc README.md

%changelog
%autochangelog
