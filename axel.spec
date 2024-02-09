%global forgeurl https://github.com/axel-download-accelerator/axel

Name:       axel
Version:    2.17.13
Release:    %autorelease
Summary:    Light command line download accelerator for Linux and Unix

%forgemeta

# spdx
License:    GPL-2.0-or-later
URL:        %forgeurl
Source0:    %forgesource
BuildRequires: gettext-devel
BuildRequires: pkgconfig(libssl)
BuildRequires: autoconf
BuildRequires: autoconf-archive
BuildRequires: txt2man
BuildRequires: automake
BuildRequires: gcc
BuildRequires: make

%description
Axel tries to accelerate HTTP/FTP downloading process by using
multiple connections for one file. It can use multiple mirrors for a
download. Axel has no dependencies and is lightweight, so it might
be useful as a wget clone on byte-critical systems.

%prep
%forgesetup

%build
autoreconf -vfi
%{configure}
%make_build


%install
%make_install \

mkdir -p %{buildroot}%{_sysconfdir}
install -m 644 -p -T doc/axelrc.example %{buildroot}%{_sysconfdir}/axelrc

%find_lang %{name}


%files -f %{name}.lang
%{_bindir}/%{name}
%doc ChangeLog README.md doc/API
%license COPYING
%config(noreplace) %{_sysconfdir}/axelrc
%{_mandir}/man1/axel.1*


%changelog
%autochangelog
