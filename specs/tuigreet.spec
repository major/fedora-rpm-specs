Name:           tuigreet
Version:        0.9.1
Release:        %autorelease
Summary:        Graphical console greeter for greetd

# Upstream license specification: GPL-3.0
# (MIT OR Apache-2.0) AND Unicode-DFS-2016
# Apache-2.0
# Apache-2.0 OR BSL-1.0
# Apache-2.0 OR MIT
# BSD-2-Clause OR Apache-2.0 OR MIT
# GPL-3.0-only
# MIT
# MIT OR Apache-2.0
# Unicode-3.0
# Unlicense OR MIT
License:        GPL-3.0-only AND Apache-2.0 AND (Apache-2.0 OR BSL-1.0) AND (Apache-2.0 OR MIT) AND (BSD-2-Clause OR Apache-2.0 OR MIT) AND MIT AND Unicode-3.0 AND Unicode-DFS-2016 AND (Unlicense OR MIT)
# LICENSE.dependencies contains a full license breakdown
URL:            https://github.com/apognu/%{name}
Source:         %{url}/archive/%{version}/%{name}-%{version}.tar.gz
# upgrade i18n-embed 0.14 -> 0.16
# upgrade i18n-embed-fl 0.8 -> 0.10
Patch:          tuigreet-fix-metadata.diff
# Fedora-specific patch: use greetd user home to remember username and last session.
# See the patch header for the rationale.
Patch:          tuigreet-0.9.1-Store-persistent-data-in-the-greetd-user-home.patch
Patch:          tuigreet-0.9.1-adjust-for-i18n-embed-0.16.patch

BuildRequires:  cargo-rpm-macros >= 24
BuildRequires:  scdoc

Requires:       greetd >= 0.6
Provides:       greetd-greeter = 0.6
Provides:       greetd-%{name} = %{version}
# upgrade path for copr builds
Obsoletes:      greetd-%{name} <= 0.8.0-1

%description
%{summary}.


%prep
%autosetup -p1
%cargo_prep


%generate_buildrequires
%cargo_generate_buildrequires


%build
%cargo_build
%{cargo_license_summary}
%{cargo_license} > LICENSE.dependencies

scdoc <contrib/man/tuigreet-1.scd >contrib/man/tuigreet.1


%install
%cargo_install
install -D -m644 -vp contrib/man/tuigreet.1 \
    %{buildroot}%{_mandir}/man1/%{name}.1


%files
%license LICENSE
%license LICENSE.dependencies
%doc README.md
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*


%changelog
%autochangelog
