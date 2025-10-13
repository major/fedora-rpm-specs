%global commit 0bcb874deeb3e6448783e79c602ecd2192ab6f68
%global commitdate 20251007
%{?commit:%global shortcommit %(c=%{commit}; echo ${c:0:7})}

# For now, I don't want to make any "releases". The script is
# very much a WIP, so we may just as well do a snapshot.

Name:           fedora-repro
Version:        0.1^%{commitdate}g%{shortcommit}
Release:        %autorelease
Summary:        Scripts to reproduce builds of Fedora packages

License:        LGPL-2.1-or-later
URL:            https://github.com/keszybz/fedora-repro
Source0:        https://github.com/keszybz/fedora-repro/archive/%{commit}/%{name}-%{shortcommit}.tar.gz

BuildRequires:  python3-devel
Requires:       /usr/bin/rpmdiff

BuildArch:      noarch

%description
This package provide the fedora-repro-build script which can be used to
do a local mock rebuild of a build that was previously done in koji,
and the fedora-repro-listener/fedora-repro-worker scripts to listen
for notifications about finished builds and do rebuilds.

See https://docs.fedoraproject.org/en-US/reproducible-builds/.

%prep
%autosetup -p1 -n %{name}-%{commit}

%generate_buildrequires
%pyproject_buildrequires

%build
%py3_shebang_fix fedora_repro/*.py
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l fedora_repro

# %%check
# no tests yet

%files -f %{pyproject_files}
%doc README.md
%_bindir/%{name}-build
%_bindir/%{name}-listen
%_bindir/%{name}-work

%changelog
%autochangelog
