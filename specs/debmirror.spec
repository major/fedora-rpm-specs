Name:       debmirror
Version:    2.49
Release:    %autorelease
Summary:    Debian partial mirror script, with ftp and package pool support
License:    GPL-2.0-or-later
URL:        https://tracker.debian.org/pkg/debmirror
BuildArch:  noarch

Source:     https://ftp.debian.org/debian/pool/main/d/%{name}/%{name}_%{version}.tar.xz
# Build download URLs with URI->new_abs instead of string concatenation, so a
# --root with a leading slash (e.g. "/" or "/ubuntu") does not produce "//"
# in the URLs.
Patch0:     %{name}-remoteroot-url.patch
# Let command line --arch/--dist/--section override the config file values
# instead of appending to them (e.g. --arch=arm64 must not keep the default
# @arches="i386" from debmirror.conf, which then 404s on ports.ubuntu.com).
Patch1:     %{name}-cli-overrides-config.patch

BuildRequires: perl
BuildRequires: perl-generators
BuildRequires: perl-podlators

Requires:   coreutils
Requires:   diffutils
Requires:   findutils
Requires:   gnupg2
Requires:   gzip
Requires:   rsync
Requires:   xz
# Only needed for --diff (pdiff) mode, debmirror falls back to --diff=none.
Recommends: ed
Recommends: patch

%description
This program downloads and maintains a partial local Debian mirror.
It can mirror any combination of architectures, distributions and sections.
Files are transferred by ftp, http, https or rsync, and package pools are fully
supported. It also does locking and updates trace files.

%prep
%autosetup -p1 -n work

%install
install -Dp -m 0755 %{name} %{buildroot}%{_bindir}/%{name}
# Upstream leaves a stale version string, Debian replaces it at build time
sed -i 's/^\(our \$version=\).*/\1"%{version}";/' %{buildroot}%{_bindir}/%{name}
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
