%global owner gbcox
%global commit 386b17dd1b5173ce98bc439e51b5d46dc29d425d
%global shortcommit %(c=%{commit}; echo ${c:0:12})

Name:     ykocli
Version:  1.3.2
Release:  %autorelease
Summary:  Front-end script for ykman to obtain TOTP tokens

License:  GPL-3.0-or-later
URL:      https://bitbucket.org/%{owner}/%{name}
Source0:  https://bitbucket.org/%{owner}/%{name}/get/%{commit}.tar.gz#/%{name}-%{shortcommit}.tar.gz
Source1:  %{name}.rpmlintrc

BuildArch:      noarch
BuildRequires:  make
Requires:       figlet
Requires:       copyq
Requires:       yubikey-manager
Requires:       zbar

%description
ykocli is a front-end command line utility (actually, a bash script)
that places ykman obtained TOTP tokens into the CopyQ clipboard.

%prep
%autosetup -n %{owner}-%{name}-%{shortcommit}

%build

%install
%make_install prefix=%{_prefix} sysconfdir=%{_sysconfdir}

%files
%license LICENSE.md
%doc README.md contributors.txt examples/
%config %{_sysconfdir}/ykocli.conf
%{_bindir}/ykocli
%dir %{_libexecdir}/%{name}
%{_libexecdir}/%{name}/src-yko-set-colors.sh
%{_libexecdir}/%{name}/src-yko-set-variables.sh
%{_libexecdir}/%{name}/src-yko-conf-override.sh
%{_libexecdir}/%{name}/src-yko-ck-input.sh
%{_libexecdir}/%{name}/src-yko-ck-touch.sh
%{_libexecdir}/%{name}/src-yko-figlet.sh
%{_libexecdir}/%{name}/src-yko-help.sh
%{_libexecdir}/%{name}/src-yko-table.sh
%{_libexecdir}/%{name}/src-yko-time.sh
%{_libexecdir}/%{name}/src-yko-trap.sh
%{_libexecdir}/%{name}/src-yko-totp.sh
%{_libexecdir}/%{name}/src-yko-add.sh
%{_libexecdir}/%{name}/src-yko-delete.sh
%{_libexecdir}/%{name}/src-yko-rename.sh
%{_libexecdir}/%{name}/src-yko-devinfo.sh
%{_mandir}/man1/ykocli.1*

%changelog
%autochangelog
