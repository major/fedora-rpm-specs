# A place to drop systemd-boot shimming utilities that don't yet have
# a better place to live. The name is a play on the grubby package
# which performs a similar function for grub2.

Name: sdubby
Version: 1.0
Release: 6%{?dist}
Summary: Set of systemd-boot shims that don't fit anywhere else in the distro
License: GPLv2+
URL:	 https://pagure.io/sdubby.git
BuildArchitectures: noarch
ExclusiveArch: %{efi}

Source1: updateloaderentries.sh
Source2: COPYING
Source3: entries.srel
Source4: updateloaderentries.8
Source5: README.md

Requires: findutils
Requires: util-linux
Requires: systemd-boot
Requires: gawk
Requires: coreutils

BuildRequires:	gzip

# This conflicts exists to avoid the grubby package pulling
# in grub-tools and therefor much of grub itself.  Which in
# turn confuses many tools about whether they should be doing
# grub things, or systemd-boot things.
Conflicts: grubby
Provides:  grubby = 8.41

%description
This package provides a place to drop systemd-boot shimming
utilities that don't yet have a better place to live. The name
is a play on the grubby package which performs a similar function
for grub2.

%prep
# Make sure the license can be found in mock
cp %{SOURCE2} . || true
cp %{SOURCE5} . || true

%build

%install

mkdir -p %{buildroot}%{_sbindir}/
install -T -m 0755 %{SOURCE1} %{buildroot}%{_sbindir}/updateloaderentries
install --directory %{buildroot}%{efi_esp_root}/loader
install --directory %{buildroot}%{efi_esp_root}/loader/entries
install -T -m 444 %{SOURCE3} %{buildroot}%{efi_esp_root}/loader/entries.srel
ln -sr %{buildroot}%{_sbindir}/updateloaderentries %{buildroot}%{_sbindir}/grubby
install -TD -m 444 %{SOURCE4} %{buildroot}%{_mandir}/man8/updateloaderentries.8
gzip %{buildroot}%{_mandir}/man8/updateloaderentries.8

# should we create /boot/efi/loader/loader.conf here?
# instead we are ghosting the config file, and letting anaconda create it


%post
# we could do a bootctl here too, but anaconda is taking care of it.

%files
%license COPYING
%doc README.md
%{_mandir}/man8/updateloaderentries.8.gz
%attr(0755,root,root) %{_sbindir}/updateloaderentries
%{_sbindir}/grubby
# files on the ESP (fat) will always have 700
%{efi_esp_root}/loader/entries
%config(noreplace) %{efi_esp_root}/loader/entries.srel
%attr(0644,root,root) %ghost %config(noreplace) %{efi_esp_root}/loader/loader.conf


%changelog
* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Dec  4 2023 Jeremy Linton <jeremy.linton@arm.com> - 1.0-5
- BZ 2250498 Add hacky grubby = 8.41 line to assure that anaconda-core, as used by initial-setup-gui, for xfce/etc is satisfied

* Wed Sep 20 2023 Jeremy Linton <jeremy.linton@arm.com> - 1.0-4
- Merge PR#1, fixes independent loaderentries

* Fri Sep 15 2023 Zbigniew Jedrzejewski-Szmek <zbyszek@in.waw.pl> - 1.0-3
- Drop /usr/sbin/installkernel symlink

* Fri Sep  9 2022 Jeremy Linton <jeremy.linton@arm.com> - 1.0-1
- Create package as a grubby alternative on systemd-boot systems
