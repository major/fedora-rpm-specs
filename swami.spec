Name: swami
Version: 2.2.2
Release: %autorelease
Summary: MIDI instrument and sound editor
License: GPL-2.0-only
URL: http://www.swamiproject.org/

Source0: https://github.com/swami/swami/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires: gcc
BuildRequires: cmake
BuildRequires: fftw-devel
BuildRequires: fluidsynth-devel
BuildRequires: libglade2-devel
BuildRequires: libgnomecanvas-devel
BuildRequires: libinstpatch-devel
BuildRequires: librsvg2-devel
BuildRequires: desktop-file-utils

Requires: hicolor-icon-theme
Requires: %{name}-libs%{?_isa} = %{version}-%{release}

%description
The Swami Project - Sampled Waveforms And Musical Instruments - is a collection
of free software for editing and sharing MIDI instruments and sounds. Swami
aims to provide an instrument editing and sharing software for instrument
formats such as SoundFont, DLS and GigaSampler.

%package libs
Summary: MIDI instrument and sound editor library

%description libs
Shared libraries for The Swami Project - Sampled Waveforms And Musical
Instruments.

%package devel
Summary: MIDI instrument and sound editor development files
Requires: %{name}-libs%{?_isa} = %{version}-%{release}

%description devel
Headers and development files for The Swami Project - Sampled Waveforms And
Musical Instruments.

%prep
%autosetup -n %{name}-%{version}

%build

%cmake -DLIB_SUFFIX="" -DPLUGINS_DIR=%{_lib}/swami/
%cmake_build

%install

%cmake_install

desktop-file-install                                    \
    --add-category="AudioVideo"                         \
    --add-category="X-Jack"                             \
    --remove-category="Application"                     \
    --remove-key="Encoding"                             \
    --delete-original                                   \
    --dir=%{buildroot}%{_datadir}/applications          \
    %{buildroot}/%{_datadir}/applications/%{name}.desktop

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop

%files
%doc AUTHORS ChangeLog NEWS README.md HACKERS
%license COPYING
%{_datadir}/%{name}/
%{_bindir}/%{name}
%{_libdir}/%{name}/
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/*
%{_datadir}/mime/packages/%{name}.xml

%files libs
%{_libdir}/lib%{name}*.so.*

%files devel
%{_libdir}/lib%{name}*.so
%{_includedir}/%{name}/

%changelog
%autochangelog
