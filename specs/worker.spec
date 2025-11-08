Name:		worker
Version:	5.2.2
Release:	%autorelease
Summary:	File Manager for the X11
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:	GPL-2.0-or-later
URL:		http://boomerangsworld.de/worker
Source0:	http://boomerangsworld.de/cms/%{name}/downloads/%{name}-%{version}.tar.zst
Patch0: 	Patch0-Fix-For-Python3.patch
BuildRequires:	dbus-devel
BuildRequires:	desktop-file-utils
BuildRequires:	file-devel
BuildRequires:	gcc-c++
BuildRequires:	libudisks2-devel
BuildRequires:	libX11-devel
BuildRequires:	libXft-devel
BuildRequires:	libXinerama-devel
BuildRequires:	lua-devel
BuildRequires:	make
BuildRequires:	openssl-devel

%description
A X11 file-manager that features low requirements and easy to access archives.

%prep
%autosetup -p0

#Fix Man pages(UTF-8)
for f in ChangeLog man/fr/worker.1 man/it/worker.1; do
	iconv -f ISO-8859-1 -t UTF-8 $f > $f.new && \
	touch -r $f $f.new && \
	mv $f.new $f
done

%build
%configure
%make_build

%install
%make_install

desktop-file-install	\
--delete-original	\
--dir=%{buildroot}%{_datadir}/applications	\
--remove-category="FileManager"		\
--add-category="System;FileTools"	\
%{buildroot}/%{_datadir}/applications/%{name}.desktop


%files
%doc AUTHORS ChangeLog THANKS
%license COPYING
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/WorkerIcon*.xpm
%{_datadir}/metainfo/de.boomerangsworld.worker.metainfo.xml
%{_mandir}/man1/%{name}.1*
%{_mandir}/*/man1/%{name}.1*
%{_datadir}/%{name}/
%{_datadir}/appdata/%{name}.appdata.xml
%{_bindir}/%{name}

%changelog
%autochangelog
