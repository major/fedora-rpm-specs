Name:           duply
Version:        2.5.5
Release:        %autorelease
Summary:        Wrapper for duplicity
# Automatically converted from old format: GPLv2 - review is highly recommended.
License:        GPL-2.0-only
URL:            http://duply.net/
Source0:        http://downloads.sourceforge.net/ftplicity/%{name}_%{version}.tgz
BuildArch:      noarch
BuildRequires:  txt2man >= 1.5.6
Requires:       duplicity


%description
duply is a frontend for the mighty duplicity magic. It simplifies
running duplicity with cron or on command line by:

- keeping recurring settings in profiles per backup job
- automated import/export of keys between profile and keyring
- enabling batch operations e.g. backup_verify_purge
- executing pre/post scripts
- precondition checking for flawless duplicity operation

Since version 1.5.0 all duplicity backends are supported. Hence the
name changed from ftplicity to duply.


%prep
%setup -q -n %{name}_%{version}


%build
# generate the man page
chmod +x %{name}
./%{name} txt2man > %{name}.1


%install
install -p -D -m 0755 %{name} %{buildroot}%{_bindir}/%{name}
install -p -D -m 0644 %{name}.1 %{buildroot}%{_mandir}/man1/%{name}.1
# root's profiles will be stored there
install -d -m 0755 %{buildroot}%{_sysconfdir}/%{name}
# fix shebang line
sed -i "1c#!/bin/bash" %{buildroot}%{_bindir}/%{name}
mv gpl-2.0.txt LICENSE


%files
%license LICENSE
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*
%dir %{_sysconfdir}/%{name}


%changelog
%autochangelog
