# Created by pyp2rpm-3.3.5

Name:           pmbootstrap
Version:        3.9.0
Release:        %autorelease
Summary:        A sophisticated chroot/build/flash tool to develop and install postmarketOS

License:        GPL-3.0-only
URL:            https://www.postmarketos.org
# cannot use %%{pypi_source} due to
# https://gitlab.com/postmarketOS/pmbootstrap/-/issues/2009
Source0:        https://gitlab.postmarketos.org/postmarketOS/%{name}/-/archive/%{version}/%{name}-%{version}.tar.gz
BuildArch:      noarch
# s390x is currently unsupported:
# https://gitlab.postmarketos.org/postmarketOS/pmbootstrap/-/blob/3.9.0/pmb/core/arch.py#L84
# which is then used in
# https://gitlab.postmarketos.org/postmarketOS/pmbootstrap/-/blob/3.9.0/pmb/core/arch.py#L309
ExcludeArch:    s390x

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
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l pmb

%check
%pytest -k "not pkgrepo_pmaports and not random_valid_deviceinfos"

%files -f %{pyproject_files}
%license LICENSE
%doc README.md
%{_bindir}/%{name}

%changelog
%autochangelog
