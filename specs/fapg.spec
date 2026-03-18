Name:       fapg
Version:    0.45
Release:    %autorelease
License:    GPL-2.0-or-later
Summary:    Fast Audio Playlist Generator
URL:        http://royale.zerezo.com/fapg/
Source:     http://royale.zerezo.com/fapg/%{name}-%{version}.tar.gz

BuildRequires: gcc
BuildRequires: make
BuildRequires: uriparser-devel

%description
FAPG means Fast Audio Playlist Generator.
It is a tool to generate list of audio files (Wav, MP3, Ogg, etc)
in various formats (M3U, PLS, HTML, etc).
It is very useful if you have a large amount of audio files 
and you want to quickly and frequently build a playlist.

It is coded in C to be as fast as possible, and does not use 
any specific audio library (like ID3Lib).
This allows you to deploy it faster and easier, and to have
better performance since less information is loaded.
On the other hand, this tool is not (yet) compatible with
all the known formats.

%prep
%autosetup

%build
%configure
%make_build

%check
make check

%install
%make_install

%files
%doc AUTHORS ChangeLog README
%license COPYING
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*

%changelog
%autochangelog
