Name:           fedora-active-user
Version:        26.06.22
Release:        %autorelease
Summary:        Check whether a given Fedora developer is still active
License:        GPL-2.0-or-later
URL:            https://github.com/hrw/fedora-active-user

Source:         https://github.com/hrw/fedora-active-user/archive/refs/tags/%{version}.tar.gz

BuildArch:      noarch

Requires:       python3-requests
# Kerberos support is needed to login to the FAS
Requires:       python3-requests-kerberos
Requires:       python3-bugzilla
Requires:       python3-gssapi
Requires:       python3-koji
Requires:       bodhi-client


%description
This program performs a number of checks to have an educated guess as to
whether someone can be consider as 'active' or not within the Fedora project.

%prep
%autosetup

%install
install -p -D -m 0755 fedora_active_user.py %{buildroot}%{_bindir}/fedora-active-user
install -p -D -m 0644 fedora-active-user.1  %{buildroot}%{_mandir}/man1/fedora-active-user.1

%files 
%license gpl-2.0.txt
%doc README.md
%{_bindir}/fedora-active-user
%{_mandir}/man1/fedora-active-user.1*

%autochangelog
