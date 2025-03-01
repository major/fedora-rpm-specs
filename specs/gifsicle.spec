Name:           gifsicle
Version:        1.96
Release:        %autorelease
Summary:        Powerful program for manipulating GIF images and animations

# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
URL:            http://www.lcdf.org/gifsicle/
Source0:        http://www.lcdf.org/gifsicle/gifsicle-%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  libX11-devel
BuildRequires: make


%description
Gifsicle is a command-line tool for creating, editing, and getting
information about GIF images and animations.

Some more gifsicle features:

    * Batch mode for changing GIFs in place.
    * Prints detailed information about GIFs, including comments.
    * Control over interlacing, comments, looping, transparency...
    * Creates well-behaved GIFs: removes redundant colors, only uses local
      color tables if it absolutely has to (local color tables waste space
      and can cause viewing artifacts), etc.
    * It can shrink colormaps and change images to use the Web-safe palette
      (or any colormap you choose).
    * It can optimize your animations! This stores only the changed portion
      of each frame, and can radically shrink your GIFs. You can also use
      transparency to make them even smaller. Gifsicle?s optimizer is pretty
      powerful, and usually reduces animations to within a couple bytes of
      the best commercial optimizers.
    * Unoptimizing animations, which makes them easier to edit.
    * A dumb-ass name.

One other program is included with gifsicle
and gifdiff compares two GIFs for identical visual appearance.


%package -n gifview
Summary:        Lightweight animated-GIF viewer

%description -n gifview
gifview is a lightweight animated-GIF viewer which can show animations as
slideshows or in real time,


%prep
%setup -q


%build
%configure
%make_build


%install
%make_install


%files
%license COPYING
%doc NEWS.md README.md
%{_bindir}/gifdiff
%{_bindir}/gifsicle
%{_mandir}/man1/gifdiff.1*
%{_mandir}/man1/gifsicle.1*

%files -n gifview
%license COPYING
%doc NEWS.md README.md
%{_bindir}/gifview
%{_mandir}/man1/gifview.1*


%changelog
%autochangelog
