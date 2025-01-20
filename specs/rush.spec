Name:             rush
Version:          2.4
Release:          2%{?dist}
Summary:          GNU Restricted User Shell
# Main code and man pages under GPL-3.0-or-later
# Documentation under GFDL1.1-or-later AND GFDL-1.3-or-later
# Files from GNULib under LGPL-2.0-or-later AND LGPL-2.1-or-later AND LGPL-3.0-or-later
License:          GPL-3.0-or-later AND LGPL-2.0-or-later AND LGPL-2.1-or-later AND LGPL-3.0-or-later AND GFDL-1.1-or-later AND GFDL-1.3-or-later
URL:              https://www.gnu.org/software/rush/
Source0:          http://ftp.gnu.org/gnu/%{name}/%{name}-%{version}.tar.xz
Source1:          http://ftp.gnu.org/gnu/%{name}/%{name}-%{version}.tar.xz.sig
Source2:          gpgkey-79FFD94BFCE230B1.gpg
BuildRequires:    gcc
BuildRequires:    gnupg2
BuildRequires:    make
Provides:         bundled(gnulib)

%description
GNU Rush is a Restricted User Shell, designed for sites providing
limited remote access to their resources, such as, for example,
https://savannah.gnu.org/. Its main program, rush, is configured
as a user login shell for users that are allowed only remote access
to the machine. Using a flexible configuration file, GNU Rush gives
administrator complete control over the command lines that users
execute, and allows to tune the usage of system resources, such as
virtual memory, CPU time, etc. on a per-user basis.

%prep
%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup -p1

%build
export CFLAGS="-D_GNU_SOURCE $RPM_OPT_FLAGS"
%configure
%make_build

%check
make check

%install
%make_install
rm -rf %{buildroot}%{_infodir}/dir
%find_lang %{name}

%files -f %{name}.lang
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/rush.rc
%license COPYING
%doc NEWS
%doc ChangeLog
%doc README
%doc AUTHORS
%{_bindir}/rushlast
%{_bindir}/rush-po
%{_bindir}/rushwho
%{_sbindir}/rush
%{_mandir}/man8/rush.8*
%{_mandir}/man1/rush-po.1*
%{_mandir}/man1/rushlast.1*
%{_mandir}/man1/rushwho.1*
%{_mandir}/man5/rush.rc.5*
%{_infodir}/rush.info*

%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Dec 20 2024 Stephane Thiell <sthiell@stanford.edu> - 2.4-1
- Initial release
