%global git_commit 8a93dd27de503b0a3ace36d961a10c9ea4adee8b

Summary:	Pythonic Smart Contract Language for the EVM
Name:		vyper
Version:	0.4.1
Release:	%autorelease
BuildArch:	noarch
License:	Apache-2.0
URL:		https://vyperlang.org
Source0:	%{pypi_source %{name}}
Patch1:		vyper-0001-Use-Cryptodomex.patch
Patch2:		vyper-0002-Ease-version-requirements.patch
Patch3:		vyper-0003-Remove-unnecessary-shebang.patch
Patch4:		vyper-0004-Relax-lark-dependency.patch
BuildRequires:	git
BuildRequires:	python3-cached_property
BuildRequires:	python3-devel
BuildRequires:	python3-eth-abi
BuildRequires:	python3-eth-keys
BuildRequires:	python3-eth-stdlib
BuildRequires:	python3-hypothesis
BuildRequires:	python3-pytest
BuildRequires:	python3-rlp

%description
%{summary}.

%prep
%autosetup -p1
echo %{sub %git_commit 0 7} > ./vyper/vyper_git_commithash.txt

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l %{name}
rm -f %{buildroot}/usr/vyper_git_commithash.txt

%check
%pyproject_check_import
# FIXME requires https://github.com/ethereum/py-evm
# FIXME requires https://github.com/paradigmxyz/pyrevm
#%%pytest

%files -f %{pyproject_files}
%doc README.md SECURITY.md
%{_bindir}/fang
%{_bindir}/venom
%{_bindir}/vyper
%{_bindir}/vyper-json

%changelog
%autochangelog
