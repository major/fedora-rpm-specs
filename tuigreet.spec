Name:           tuigreet
Version:        0.8.0
Release:        %autorelease
Summary:        Graphical console greeter for greetd

# Upstream license specification: GPL-3.0
# (MIT OR Apache-2.0) AND Unicode-DFS-2016
# Apache-2.0
# Apache-2.0 OR BSL-1.0
# Apache-2.0 OR MIT
# GPL-3.0
# MIT
# MIT OR Apache-2.0
# Unicode-DFS-2016
# Unlicense OR MIT
License:        GPL-3.0-only AND Apache-2.0 AND (Apache-2.0 OR BSL-1.0) AND (Apache-2.0 OR MIT) AND MIT AND Unicode-DFS-2016 AND (Unlicense OR MIT)
URL:            https://github.com/apognu/%{name}
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz
# Fix crate version (used for tuigreet --version)
Patch0:         tuigreet-fix-metadata.diff
# Bump dependenies to the versions available in Fedora
# https://github.com/apognu/tuigreet/pull/91 supersedes tui bump
# https://github.com/apognu/tuigreet/pull/98 contains greetd_ipc changes
Patch1:         tuigreet-0.8.0-bump-greetd_ipc-tui-crossterm.patch
# Fedora-specific patch: use greetd user home to remember username and last session.
# See the patch header for the rationale.
Patch2:         tuigreet-0.8.0-Store-persistent-data-in-the-greetd-user-home.patch

BuildRequires:  rust-packaging >= 23
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
%cargo_license_summary
%cargo_build
%{cargo_license} >LICENSE.dependencies

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
