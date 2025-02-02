# Created by pyp2rpm-3.3.5

Name:           pmbootstrap
Version:        3.2.0
Release:        %autorelease
Summary:        A sophisticated chroot/build/flash tool to develop and install postmarketOS

License:        GPL-3.0-only
URL:            https://www.postmarketos.org
# cannot use %%{pypi_source} due to
# https://gitlab.com/postmarketOS/pmbootstrap/-/issues/2009
Source0:        https://gitlab.postmarketos.org/postmarketOS/%{name}/-/archive/%{version}/%{name}-%{version}.tar.gz
BuildArch:      noarch

# pmbootstrap obtains the native arch via from_machine_type
# https://gitlab.postmarketos.org/postmarketOS/pmbootstrap/-/blob/3.0.0/pmb/core/arch.py?ref_type=tags#L52
# this function only supports the following arches and hence these must be the exclusive arch
# see also: https://gitlab.postmarketos.org/postmarketOS/pmbootstrap/-/issues/2501
ExclusiveArch:  %x86_64 %arm64 armv6l armv7l armv8l noarch

BuildRequires:  python3-devel
BuildRequires:  python3dist(argcomplete)
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(wheel)

BuildRequires:  /usr/bin/openssl
BuildRequires:  git
BuildRequires:  kpartx
BuildRequires:  /usr/bin/ps

Requires:       openssl
Requires:       git
Requires:       kpartx
Requires:       util-linux
Requires:       /usr/bin/ps


%description
Sophisticated chroot/build/flash tool to develop and install postmarketOS.

%prep
%autosetup -n %{name}-%{version}
# Remove bundled egg-info
rm -rf %{name}.egg-info

%generate_buildrequires
%pyproject_buildrequires -t

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l pmb

%check
pytest_args="not pkgrepo_pmaports"
# the valid_chroots test fails on non x86_64
# https://gitlab.postmarketos.org/postmarketOS/pmbootstrap/-/issues/2500
if [[ ! $(uname -m) = "x86_64" ]]; then pytest_args+=" and not valid_chroots"; fi
%pytest -k "${pytest_args}"

%files -f %{pyproject_files}
%license LICENSE
%doc README.md
%{_bindir}/%{name}

%changelog
%autochangelog
