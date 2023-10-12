%global forgeurl https://github.com/Yubico/yubikey-manager/
%global commit 483e2429f4ccabfc0e039b10cee3f9e511844cc4

Name:           yubikey-manager
Version:        5.2.1
Release:        %autorelease
Summary:        Python library and command line tool for configuring a YubiKey
License:        BSD-2-Clause

%forgemeta

URL:            %{forgeurl}
Source0:        %{forgesource}
Source1:        %{name}.rpmlintrc

BuildArch:      noarch
BuildRequires:  swig pcsc-lite-devel ykpers pyproject-rpm-macros
BuildRequires:  python3-devel tox
BuildRequires:  %{py3_dist six pyscard pyusb click cryptography pyopenssl}
BuildRequires:  %{py3_dist tox-current-env poetry-core setuptools}
BuildRequires:  %{py3_dist makefun pytest}
BuildRequires:  %{py3_dist fido2} >= 0.9.0

Requires:       python3-%{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       u2f-hidraw-policy

%description
Command line tool for configuring a YubiKey.

%generate_buildrequires
%pyproject_buildrequires

%package -n python3-%{name}
Summary:        Python library for configuring a YubiKey
Requires:       ykpers pcsc-lite

%description -n python3-%{name}
Python library for configuring a YubiKey.

%prep
%forgesetup
%autosetup -p1 -n %{archivename}

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
