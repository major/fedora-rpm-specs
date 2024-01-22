%{!?_pkgdocdir: %global _pkgdocdir %{_docdir}/%{name}-%{version}}
Name:		luckybackup
Version:	0.5.0
Release:	%autorelease
Summary:	A powerful, fast and reliable backup and sync tool

License:	GPL-3.0-or-later
URL:		http://luckybackup.sourceforge.net/index.html
Source0:	http://downloads.sourceforge.net/project/%{name}/%{version}/source/%{name}-%{version}.tar.gz

BuildRequires:	qt-devel
Buildrequires:	desktop-file-utils
Buildrequires:	gcc-c++
BuildRequires:	make
Requires:	polkit

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch: %{ix86}

%description
luckyBackup is an application that backs-up and/or synchronizes any 
directories with the power of rsync.

It is simple to use, fast (transfers over only changes made and not all data), 
safe (keeps your data safe by checking all declared directories before 
proceeding in any data manipulation ), reliable and fully customizable.

%prep
%setup -q
sed -i 's,/usr/share/doc/luckybackup,%{_pkgdocdir},' luckybackup.pro
sed -i 's,/usr/share/doc/luckybackup/license/gpl.html,%{_pkgdocdir}/license/gpl.html,' src/global.h
sed -i 's,/usr/share/doc/luckybackup/manual/index.html,%{_pkgdocdir}/manual/index.html,' src/global.h
# Upstream switched to pkexec, too, but still carries beesu instructions for Fedora:
sed -i '/Fedora users/d' manual/index.html
chmod a-x manual/index.html

%build
%{qmake_qt4}
%make_build CFLAGS="$RPM_OPT_FLAGS"

%install
INSTALL_ROOT=%{buildroot} \
  make install DESTDIR=%{buildroot}
# We want this in in the license dir:
rm -f %{buildroot}%{_docdir}/%{name}/license/gpl.txt

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}-su.desktop
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop

%files
%doc readme/README readme/changelog
%license license/gpl.txt
%{_bindir}/%{name}
%{_bindir}/%{name}-pkexec
%{_datadir}/applications/%{name}*
%{_datadir}/polkit-1/actions/net.%{name}.su.policy
%{_datadir}/pixmaps/%{name}*
%{_datadir}/%{name}
%{_docdir}/%{name}/license
%{_docdir}/%{name}/manual
%{_mandir}/man8/%{name}*.8.*

%changelog
%autochangelog
