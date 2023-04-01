Name:           fim
Version:        0.6
Release:        1%{?dist}
Summary:        Lightweight universal image viewer
License:        GPL-2.0-or-later AND GPL-3.0-or-later
URL:            https://www.nongnu.org/fbi-improved/
Source0:        http://download.savannah.nongnu.org/releases/fbi-improved/fim-%{version}-trunk.tar.gz
Source1:        http://download.savannah.nongnu.org/releases/fbi-improved/fim-%{version}-trunk.tar.gz.sig
Source2:        https://www.nongnu.org/fbi-improved/0xE0E669C8EF1258B8.asc


BuildRequires:  gnupg2
BuildRequires:  readline-devel
BuildRequires:  flex
BuildRequires:  bison
BuildRequires:  gcc-c++
BuildRequires:  make
BuildRequires:  automake
BuildRequires:  autoconf
BuildRequires:  SDL2-devel
BuildRequires:  sdl12-compat-devel
BuildRequires:  libexif-devel
BuildRequires:  libpng-devel
BuildRequires:  giflib-devel
BuildRequires:  libjpeg-devel
BuildRequires:  libtiff-devel
BuildRequires:  libcaca-devel
BuildRequires:  aalib-devel
BuildRequires:  djvulibre-devel

Provides: fim%{?_isa} = %{version}-%{release}


%description
FIM (Fbi IMproved) is a highly customizable and scriptable image viewer 
targeted at the users who are comfortable with software like the Vim. 

FIM is multidevice: it has X support (via the SDL library),
it supports ASCII art output (via the aalib and libcaca libraries), 
and because it derives from the Fbi image viewer (by Gerd Hoffmann), 
it can display images in the Linux framebuffer console, too. 

It offers many options for scaling, orienting, listing and rearranging 
the ordering of images. 


%prep
%{gpgverify} --keyring='%SOURCE2' --signature='%SOURCE1' --data='%SOURCE0'
%autosetup -n %{name}-%{version}-trunk


%build
%configure -q --enable-sdl --enable-aa --enable-caca
%make_build


%install
%make_install


%files
%license COPYING
%doc doc/fim.man.html doc/fimgs.man.html doc/fimrc.man.html
%doc doc/FIM.*
%doc src/fimrc
%doc AUTHORS BUGS ChangeLog NEWS FAQ.TXT README README.FIRST THANKS TODO VERSION
%{_bindir}/%{name}
%{_bindir}/fimgs
%{_mandir}/man1/fim*
%{_mandir}/man5/fim*


%changelog
* Mon Mar 6 2023 Adam Dobes <adobes@redhat.com> - 0.6-1
- Fim packaged
