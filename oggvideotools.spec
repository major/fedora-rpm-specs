Name:       oggvideotools
Version:    0.9.1
Release:    %autorelease
Summary:    Toolbox for manipulating Ogg video files

License:    GPL-2.0-or-later
URL:        https://dev.streamnik.de/oggvideotools.html
Source0:    https://downloads.sourceforge.net/project/oggvideotools/oggvideotools/%{name}-%{version}/%{name}-%{version}.tar.gz

Patch:      0001-scripts-install-mkSlideshow-as-well.patch
Patch:      0002-scripts-install-to-bin-not-sbin.patch
Patch:      0003-docs-install-to-share-man.patch
Patch:      0004-make-all-internal-libs-STATIC.patch
Patch:      0005-unbundle-libresample.patch
Patch:      https://sources.debian.org/data/main/o/oggvideotools/0.9.1-3/debian/patches/mayhem-crash-oggjoin.patch
Patch:      https://sources.debian.org/data/main/o/oggvideotools/0.9.1-3/debian/patches/manual-typos.patch
Patch:      https://sources.debian.org/data/main/o/oggvideotools/0.9.1-3/debian/patches/oggThumb-zero-getopt-long.patch
Patch:      https://sources.debian.org/data/main/o/oggvideotools/0.9.1-3/debian/patches/init-for-valgrind.patch
Patch:      https://sources.debian.org/data/main/o/oggvideotools/0.9.1-3/debian/patches/import-cstring.patch
# crude work-around for https://bugzilla.redhat.com/show_bug.cgi?id=2234728 (CVE-2020-21724)
Patch:      stream-serializer.diff


BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig(theoradec)
BuildRequires:  pkgconfig(theoraenc)
BuildRequires:  pkgconfig(vorbis)
BuildRequires:  pkgconfig(vorbisenc)
BuildRequires:  pkgconfig(ogg)
BuildRequires:  pkgconfig(libresample)
BuildRequires:  boost-devel
BuildRequires:  gd-devel

%description
A toolbox for manipulating Ogg video files, which usually consist of a
video stream (Theora) and an audio stream (Vorbis). It includes a
number of handy command line tools for manipulating these video files,
such as for splitting the different streams.

%prep
%autosetup -p1
chmod 644 docs/DocuOggVideoTools.pdf

# Remove bundled libresample
rm -rf src/libresample/

%build
%cmake
%cmake_build

%install
%cmake_install

chmod +x %buildroot%{_bindir}/mkThumbs
chmod +x %buildroot%{_bindir}/mkSlideshow

%global ogg_tool() \
%{_bindir}/ogg%{1}\
%{_mandir}/man1/ogg%{1}.1*

%files
%doc README ChangeLog docs/DocuOggVideoTools.pdf
%license COPYING
%ogg_tool Cat
%ogg_tool Cut
%ogg_tool Dump
%ogg_tool Join
%ogg_tool Length
%ogg_tool Silence
%ogg_tool Slideshow
%ogg_tool Split
%ogg_tool Thumb
%ogg_tool Transcode
%{_bindir}/mkThumbs
%{_mandir}/man1/mkThumbs.1*
%{_bindir}/mkSlideshow

%changelog
%autochangelog
