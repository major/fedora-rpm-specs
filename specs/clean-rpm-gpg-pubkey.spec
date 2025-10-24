%global forgeurl https://github.com/svarshavchik/%{name}
%global commit   71c2a694e7336d2aee1e99665ee8e460451847f7
%global date     20251021
%forgemeta

Name:           clean-rpm-gpg-pubkey
Version:        0
Release:        %{autorelease}
Summary:        Remove old PGP keys from the RPM database
License:        GPL-3.0-only
URL:            %{forgeurl}
Source:         %{forgesource}

BuildArch:      noarch
BuildRequires:  perl-generators
Requires:       /usr/bin/curl
Requires:       /usr/bin/gpg2
Requires:       /usr/bin/rpm
Requires:       /usr/bin/rpmkeys
Requires:       fedora-release-common
Requires:       fedora-repos

%{?perl_default_filter}

%description
A short Perl script for Fedora that removes old PGP keys from the RPM
database. Each Fedora release uses a different PGP keys, but there's
nothing in Fedora (at this time) that automatically removes prior Fedora
releases' PGP keys.


%prep
%forgeautosetup


%install
install -Dt %{buildroot}%{_bindir} %{name}


%files
%doc README.md
%license COPYING
%license COPYING.GPL
%{_bindir}/%{name}


%changelog
%autochangelog
