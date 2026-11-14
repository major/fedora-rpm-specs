Name:           dash
Version:        0.5.13.6
Release:        %autorelease
Summary:        Small and fast POSIX-compliant shell
# BSD-3-Clause: DASH in general
# GPL-2.0-or-later: From src/mksignames.c
# LicenseRef-Fedora-Public-Domain: From src/bltin/test.c
License:        BSD-3-Clause AND GPL-2.0-or-later AND LicenseRef-Fedora-Public-Domain
URL:            http://gondor.apana.org.au/~herbert/%{name}/
Source0:        http://gondor.apana.org.au/~herbert/%{name}/files/%{name}-%{version}.tar.gz

Provides:       /bin/dash

BuildRequires:  gcc
BuildRequires:  make

%description
DASH is a POSIX-compliant implementation of /bin/sh that aims to be as small as
possible. It does this without sacrificing speed where possible. In fact, it is
significantly faster than bash (the GNU Bourne-Again SHell) for most tasks.

%prep
%autosetup -p1

%build
%configure
%make_build

%install
%make_install

%check
%make_build check

%post
grep -q '^/bin/dash$' %{_sysconfdir}/shells || \
    echo '/bin/dash' >> %{_sysconfdir}/shells

%postun
if [ $1 -eq 0 ]; then
    sed -i '/^\/bin\/dash$/d' %{_sysconfdir}/shells
fi

%files
%doc COPYING ChangeLog
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*

%changelog
%autochangelog
