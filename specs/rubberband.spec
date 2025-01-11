%bcond_without check

%global so_version 3

Name:           rubberband
Version:        4.0.0
Release:        %autorelease
Summary:        Audio time-stretching and pitch-shifting library

License:        GPL-2.0-or-later
URL:            http://www.breakfastquay.com/rubberband/
Source0:        https://breakfastquay.com/files/releases/%{name}-%{version}.tar.bz2
# Two tests fail on ppc64le: https://todo.sr.ht/~breakfastquay/rubberband/29
Patch:          %{name}-disable-failed-ppc64le-tests.diff

BuildRequires:  meson
BuildRequires:  gcc-c++
BuildRequires:  ladspa-devel
BuildRequires:  pkgconfig(fftw3)
BuildRequires:  pkgconfig(lv2)
BuildRequires:  pkgconfig(samplerate)
BuildRequires:  pkgconfig(sndfile)
BuildRequires:  vamp-plugin-sdk-devel
BuildRequires:  boost-devel

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
%meson \
  -Dfft=fftw \
  -Djni=disabled \
  -Dresampler=libsamplerate
%meson_build


%install
%meson_install
find %{buildroot} -name '*.la' -exec rm -f {} ';'
rm -rf %{buildroot}%{_libdir}/*.a


%if %{with check}
%check
%meson_test
%endif


%files
%license COPYING
%doc README.md
%{_bindir}/rubberband
%{_bindir}/rubberband-r3
%{_libdir}/*.so.%{so_version}*
%{_libdir}/ladspa/ladspa-rubberband.*
%dir %{_libdir}/lv2/rubberband.lv2
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
