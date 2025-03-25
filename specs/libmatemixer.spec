%global branch 1.28

Name:        libmatemixer
Summary:     Mixer library for MATE desktop
Version:     %{branch}.0
Release:     %autorelease
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:     GPL-2.0-or-later
URL:         http://mate-desktop.org
Source0:     http://pub.mate-desktop.org/releases/%{branch}/%{name}-%{version}.tar.xz

# https://github.com/mate-desktop/libmatemixer/commit/a2b5941
Patch1: libmatemixer_0001-pulse-Don-t-crash-on-failure-to-retrieve-server-info.patch

BuildRequires: mate-common
BuildRequires: pulseaudio-libs-devel
BuildRequires: alsa-lib-devel
BuildRequires: make
BuildRequires: systemd-devel


%description
libmatemixer is a mixer library for MATE desktop.
It provides an abstract API allowing access to mixer functionality
available in the PulseAudio, ALSA and OSS sound systems.

%package devel
Summary:  Development libraries for libmatemixer
Requires: %{name}%{?_isa} = %{version}-%{release}

%description devel
Development libraries for libmatemixer

%prep
%autosetup -p1

#NOCONFIGURE=1 ./autogen.sh

%build
%configure \
        --disable-static \
        --enable-pulseaudio \
        --enable-alsa \
        --enable-udev \
        --enable-gtk-doc

#drop unneeded direct library deps with --as-needed
# libtool doesn't make this easy, so we do it the hard way
sed -i -e 's/ -shared / -Wl,-O1,--as-needed\0 /g' libtool

make %{?_smp_mflags} V=1

%install
%{make_install}

find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'

%find_lang %{name} --with-gnome --all-name


%files -f %{name}.lang
%doc AUTHORS COPYING NEWS README
%{_libdir}/libmatemixer.so.*
%{_libdir}/libmatemixer/

%files devel
%{_includedir}/mate-mixer/
%{_libdir}/pkgconfig/*
%{_libdir}/*.so
%{_datadir}/gtk-doc/html/libmatemixer/


%changelog
%autochangelog
