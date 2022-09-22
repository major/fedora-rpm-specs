%global so_version 2

Name:           rubberband
Version:        3.0.0
Release:        %autorelease
Summary:        Audio time-stretching and pitch-shifting library

License:        GPLv2+
URL:            http://www.breakfastquay.com/rubberband/
Source0:        https://breakfastquay.com/files/releases/%{name}-%{version}.tar.bz2

BuildRequires:  meson
BuildRequires:  gcc-c++
BuildRequires:  ladspa-devel
BuildRequires:  pkgconfig(fftw3)
BuildRequires:  pkgconfig(samplerate)
BuildRequires:  pkgconfig(sndfile)
BuildRequires:  pkgconfig(lv2)
BuildRequires:  vamp-plugin-sdk-devel

Requires:       ladspa
Requires:       lv2

%global _description %{expand:
Rubber Band is a library and utility program that permits you to change the
tempo and pitch of an audio recording independently of one another.}

%description    %{_description}

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       pkgconfig

%description    devel %{_description}

The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%autosetup -p1


%build
%meson -Dfft=fftw -Dresampler=libsamplerate
%meson_build


%install
%meson_install
find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'
rm -rf $RPM_BUILD_ROOT%{_libdir}/*.a


# no tests yet
# check
# meson_test


%files
%license COPYING
%doc README.md
%{_bindir}/rubberband
%{_bindir}/rubberband-r3
%{_libdir}/*.so.%{so_version}*
%{_libdir}/ladspa/ladspa-rubberband.*
%{_libdir}/lv2/rubberband.lv2/*
%{_datadir}/ladspa/rdf/ladspa-rubberband.rdf
%{_libdir}/vamp/vamp-rubberband.*

%files devel
%doc CHANGELOG
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/rubberband.pc


%changelog
%autochangelog
