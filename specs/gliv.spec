Summary:	Image viewing utility
Name:		gliv
Version:	1.9.7
Release:	%autorelease
License:	GPL-2.0-or-later
URL:		http://guichaz.free.fr/gliv/
VCS:		git://repo.or.cz/gliv.git
Source0:	http://guichaz.free.fr/gliv/files/%{name}-%{version}.tar.bz2
Source1:	gliv.desktop
Source2:	gliv.applications
Patch1:		gliv-0001-Something-is-always-bigger-than-nothing-NULL.patch
Patch2:		gliv-0002-bool-is-a-reserved-word-in-a-new-ANSI-C.patch
BuildRequires:	desktop-file-utils
BuildRequires:	gcc
BuildRequires:	gtk2-devel >= 2.6.0
BuildRequires:	gtkglext-devel >= 0.7.0
BuildRequires:	make

%description
GLiv is an OpenGL image viewer. GLiv is very fast and smooth at rotating,
panning and zooming if you have an OpenGL accelerated graphics board.

%prep
%autosetup -p1

%build
%configure
%make_build

%install
%make_install
%find_lang %{name}

install -D -p -m 0644 %{SOURCE2}  %{buildroot}%{_datadir}/application-registry/gliv.applications

install -D -p -m 0644 gliv.png %{buildroot}%{_datadir}/pixmaps/gliv.png

install -d -m0755 %{buildroot}%{_datadir}/applications/
desktop-file-install \
	--dir %{buildroot}%{_datadir}/applications \
	%{SOURCE1}

%files -f %{name}.lang
%doc NEWS README THANKS
%license COPYING
%{_mandir}/man1/gliv.1*
%{_mandir}/*/man1/gliv.1*
%{_bindir}/gliv
%{_datadir}/applications/*gliv.desktop
%{_datadir}/application-registry/gliv.applications
%{_datadir}/pixmaps/gliv.png

%changelog
%autochangelog
