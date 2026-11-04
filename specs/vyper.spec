%global git_commit bff19ea204059290da652854cd634abef10f6c43

Summary:	Pythonic Smart Contract Language for the EVM
Name:		vyper
Version:	0.4.3
Release:	%autorelease
BuildArch:	noarch
License:	Apache-2.0
URL:		https://vyperlang.org
Source:		%{pypi_source %{name}}
# Fedora-specific
Patch:		vyper-0001-Use-Cryptodomex.patch
# Reverts https://github.com/vyperlang/vyper/pull/3613
Patch:		vyper-0002-Ease-version-requirements.patch
# Fedora-specific
Patch:		vyper-0003-Remove-unnecessary-shebang.patch
# Fedora-specific
Patch:		vyper-0004-Relax-lark-dependency.patch
# Backported from upstream
Patch:		vyper-0005-fix-codegen-widen-ternary-arms-to-the-result-type-la.patch
# Backported from upstream
Patch:		vyper-0006-fix-parser-fix-source-spans-for-form-feeds-and-non-a.patch
# Backported from upstream
Patch:		vyper-0007-fix-codegen-check-create_from_blueprint-code_offset-.patch
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
