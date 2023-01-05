Name:           vorbisgain
Version:        0.37
Release:        %autorelease
Summary:        Adds tags to Ogg Vorbis files to adjust the volume

License:        LGPLv2
URL:            https://sjeng.org/vorbisgain.html
Source0:        https://sjeng.org/ftp/vorbis/%{name}-%{version}.tar.gz
Patch0:         vorbisgain-spelling.patch
Patch1:         001-fprintf_fix.patch
Patch2:         vorbisgain-c99.patch

BuildRequires:  make
BuildRequires:  gcc
BuildRequires:  libvorbis-devel
BuildRequires:  libogg-devel


%description
VorbisGain is a utility that uses a psychoacoustic method to correct the
volume of an Ogg Vorbis file to a predefined standardized loudness.

It needs player support to work. Non-supporting players will play back
the files without problems, but you'll miss out on the benefits.
Nowadays most good players such as ogg123, xmms and mplayer are already
compatible.


%prep
%autosetup


%build
%configure --enable-recursive
%make_build


%install
%make_install


%files
%doc NEWS README
%{_bindir}/%{name}
%{_mandir}/man1/*


%changelog
%autochangelog
