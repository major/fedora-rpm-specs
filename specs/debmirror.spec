Name:       debmirror
Version:    2.47
Release:    %autorelease
Summary:    Debian partial mirror script, with ftp and package pool support
License:    GPL-2.0-or-later
URL:        https://tracker.debian.org/pkg/debmirror
BuildArch:  noarch

Source:     https://ftp.debian.org/debian/pool/main/d/%{name}/%{name}_%{version}.tar.xz
Patch0:     %{name}-no-root.patch

BuildRequires: perl
BuildRequires: perl-generators
BuildRequires: perl-podlators

Requires:   bzip2
Requires:   coreutils
Requires:   ed
Requires:   findutils
Requires:   gnupg
Requires:   gzip
Requires:   patch
Requires:   rsync

%description
This program downloads and maintains a partial local Debian mirror.
It can mirror any combination of architectures, distributions and sections.
Files are transferred by ftp, http, hftp or rsync, and package pools are fully
supported. It also does locking and updates trace files.

%prep
%autosetup -p1 -n work

%install
install -Dp -m 0755 %{name} %{buildroot}%{_bindir}/%{name}
install -Dp -m 0644 examples/%{name}.conf %{buildroot}%{_sysconfdir}/%{name}.conf

# generate a man page
install -d %{buildroot}%{_mandir}/man1
pod2man %{name} %{buildroot}%{_mandir}/man1/%{name}.1

%files
%license GPL debian/copyright
%doc debian/changelog debian/NEWS doc/design.txt
%{_mandir}/man1/%{name}.1.gz
%{_bindir}/%{name}
%config(noreplace) %{_sysconfdir}/%{name}.conf

%changelog
%autochangelog
