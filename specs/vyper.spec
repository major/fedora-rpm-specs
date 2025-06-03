%global git_commit c216787f5e355478733a05fa5f0fce93fa9a7126

Summary:	Pythonic Smart Contract Language for the EVM
Name:		vyper
Version:	0.4.2
Release:	%autorelease
BuildArch:	noarch
License:	Apache-2.0
URL:		https://vyperlang.org
Source0:	%{pypi_source %{name}}
Patch:		vyper-0001-Use-Cryptodomex.patch
Patch:		vyper-0002-Ease-version-requirements.patch
Patch:		vyper-0003-Remove-unnecessary-shebang.patch
Patch:		vyper-0004-Relax-lark-dependency.patch
BuildRequires:	git
BuildRequires:	python3-cached_property
BuildRequires:	python3-eth-abi
BuildRequires:	python3-eth-keys
BuildRequires:	python3-eth-stdlib
BuildRequires:	python3-hypothesis
BuildRequires:	python3-pytest
BuildRequires:	python3-rlp
BuildSystem:	pyproject
BuildOption(install): -l %{name}

%description
%{summary}.

%prep -a
echo %{sub %git_commit 0 7} > ./vyper/vyper_git_commithash.txt

%install -a
rm -f %{buildroot}/usr/vyper_git_commithash.txt

%check -a
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
