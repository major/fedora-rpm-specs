%global forgeurl https://github.com/Yubico/yubikey-manager/
%global commit 49f3c73596ce1596d431bc019e98cf60849cb2eb

Name:           yubikey-manager
Version:        5.6.0
Release:        %autorelease
Summary:        Python library and command line tool for configuring a YubiKey
License:        BSD-2-Clause

%forgemeta

URL:            %{forgeurl}
Source0:        %{forgesource}
Source1:        %{name}.rpmlintrc

# Define Patch0 ONLY for Fedora 41 and 42
%if 0%{?fedora} == 41 || 0%{?fedora} == 42
Patch0:         rhbz-2335653.patch
%endif

BuildArch:      noarch
BuildRequires:  swig pcsc-lite-devel ykpers pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  %{py3_dist makefun pytest}

Requires:       python3-%{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       u2f-hidraw-policy

%description
Command line tool for configuring a YubiKey.

%package -n python3-%{name}
Summary:        Python library for configuring a YubiKey
Requires:       ykpers pcsc-lite

%description -n python3-%{name}
Python library for configuring a YubiKey.

%prep
%forgesetup
%autosetup -p1 -n %{archivename}
# Do not upper-bound the version of keyring, since its major version increases
# frequently, usually without significant incompatibilities.
sed -r -i 's/(keyring = ">=[^"]+), <[^"]+"/\1"/' pyproject.toml

%generate_buildrequires
%pyproject_buildrequires -t

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files ykman yubikit

%check
%tox

%files -n python3-%{name} -f %{pyproject_files}
%license COPYING
%doc README.adoc NEWS

%files
%{_bindir}/ykman

%changelog
%autochangelog
