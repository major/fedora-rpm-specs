Summary:        Pro-audio reverb for JACK
Name:           zita-rev1
Version:        0.2.2
Release:        %autorelease
License:        GPL-3.0-or-later
URL:            http://kokkinizita.linuxaudio.org/
Source0:        http://kokkinizita.linuxaudio.org/linuxaudio/downloads/%{name}-%{version}.tar.bz2
# desktop file submitted upstream
Source1:        zita-rev1.desktop

BuildRequires:  cairo-devel
BuildRequires:  clthreads-devel
BuildRequires:  clxclient-devel
BuildRequires:  desktop-file-utils
BuildRequires:  gcc-c++
BuildRequires:  jack-audio-connection-kit-devel
BuildRequires:  libXft-devel
BuildRequires:  libpng-devel
BuildRequires:  make

%description
%{name} is a reworked version of the reverb originally developed for Aeolus. 
Its character is more 'hall' than 'plate', but it can be used on a wide 
variety of instruments or voices. 
It is not a spatializer - the early reflections are different for the L and R
inputs, but do not correspond to any real room. They have been tuned to match 
left and right sources to some extent.

In Stereo mode a dry/wet mix control is provided, so it can be used either as
an insert or in send/return mode. For mono just connect one of the two 
channels.

In Ambisonic mode (selected by the -B command line option) the only option is 
the send/return mode. 

%prep
%autosetup -p1

# use Fedora build flags
sed -e '/^CXXFLAGS += -march=native/d' -i source/Makefile

%build
%set_build_flags
cd source
%make_build PREFIX=%{_prefix}

%install
cd source
make DESTDIR=%{buildroot} PREFIX=%{_prefix} install

# .desktop file
mkdir -p %{buildroot}%{_datadir}/applications
desktop-file-install  \
   --dir=%{buildroot}%{_datadir}/applications %{SOURCE1}

mkdir -p %{buildroot}%{_datadir}/pixmaps
install -m 644 %{_builddir}/%{name}-%{version}/doc/redzita.png %{buildroot}%{_datadir}/pixmaps/%{name}.png

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop

%files
%doc AUTHORS doc/*
%license COPYING
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_datadir}/pixmaps/%{name}.png
%{_datadir}/applications/%{name}.desktop

%changelog
%autochangelog
