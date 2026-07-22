Summary: Photomosaic Generator
Name: metapixel
Version: 1.0.2
Release: %autorelease
# Automatically converted from old format: GPLv2 and LGPLv2+ - review is highly recommended.
License: GPL-2.0-only AND LicenseRef-Callaway-LGPLv2+
URL: http://www.complang.tuwien.ac.at/schani/metapixel/
Source: http://www.complang.tuwien.ac.at/schani/%{name}/files/%{name}-%{version}.tar.gz
Requires: perl-interpreter
Patch0: metapixel-build-fixes.patch
Patch1: metapixel-copyright.patch
Patch2: metapixel-install.patch
# giflib-5.x compatibility
Patch3: metapixel-giflib5.patch
ExcludeArch:    %{ix86}
BuildRequires:  gcc
BuildRequires:  giflib-devel
BuildRequires:  libjpeg-devel
BuildRequires:  libpng-devel
BuildRequires:  make
BuildRequires:  perl-generators

%description
A program for generating photomosaics.  It can generate classical 
photomosaics, in which the source image is viewed as a matrix of equally sized 
rectangles for each of which a matching image is substituted, as well as 
collage-style photomosaics, in which rectangular parts of the source image 
at arbitrary positions (i.e. not aligned to a matrix) are substituted by 
matching images.

%prep
%autosetup -p1

%build
%set_build_flags
%make_build

%install
make install PREFIX=%{buildroot}%{_prefix}

%files
%license COPYING
%doc NEWS README
%{_bindir}/metapixel
%{_bindir}/metapixel-imagesize
%{_bindir}/metapixel-prepare
%{_bindir}/metapixel-sizesort
%{_mandir}/man1/metapixel.1*

%changelog
%autochangelog
