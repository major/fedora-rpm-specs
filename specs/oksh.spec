Name:           oksh
Version:        7.6
Release:        %autorelease
Summary:        Portable OpenBSD ksh, based on the Public Domain Korn Shell

# The main license is "public domain", with some support files
# being under ISC and BSD license.
# Automatically converted from old format: Public Domain and ISC and BSD - review is highly recommended.
License:        LicenseRef-Callaway-Public-Domain AND ISC AND LicenseRef-Callaway-BSD
URL:            https://github.com/ibara/%{name}
Source0:        https://github.com/ibara/%{name}/releases/download/%{name}-%{version}/%{name}-%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  pkgconfig(ncursesw)

%description
Portable OpenBSD ksh, based on the Public Domain Korn Shell.

%prep
%autosetup

%build
%configure --no-strip
%make_build

%install
%make_install
install -D -p -m 0644 ksh.kshrc %{buildroot}%{_sysconfdir}/ksh.kshrc

%post
if [ "$1" = 1 ]; then
    if [ ! -f %{_sysconfdir}/shells ] ; then
        echo "%{_bindir}/%{name}" > %{_sysconfdir}/shells
        echo "/bin/%{name}" >> %{_sysconfdir}/shells
    else
        grep -q "^%{_bindir}/%{name}$" %{_sysconfdir}/shells || echo "%{_bindir}/%{name}" >> %{_sysconfdir}/shells
        grep -q "^/bin/%{name}$" %{_sysconfdir}/shells || echo "/bin/%{name}" >> %{_sysconfdir}/shells
    fi
fi

%postun
if [ "$1" = 0 ] && [ -f %{_sysconfdir}/shells ] ; then
    sed -i '\!^%{_bindir}/%{name}$!d' %{_sysconfdir}/shells
    sed -i '\!^/bin/%{name}$!d' %{_sysconfdir}/shells
fi

%files
%license LEGAL
%doc NOTES README.md README.pdksh CONTRIBUTORS
%{_bindir}/oksh
%{_mandir}/man1/%{name}.1.*
%config(noreplace) %{_sysconfdir}/ksh.kshrc

%changelog
%autochangelog
