%global git_commit e9db8d9f7486eae38f5b86531629019ad28f514e

Summary:	Pythonic Smart Contract Language for the EVM
Name:		vyper
Version:	0.4.0
Release:	%autorelease
BuildArch:	noarch
License:	Apache-2.0
URL:		https://vyperlang.org
Source0:	%{pypi_source %{name}}
Patch1:		vyper-0001-Use-Cryptodomex.patch
Patch2:		vyper-0002-Ease-version-requirements.patch
Patch3:		vyper-0003-Lark-should-go-to-the-main-install-section-as-it-use.patch
Patch4:		vyper-0004-Remove-unnecessary-shebang.patch
Patch5:		vyper-0005-Relax-lark-requirement-testing-only-anyway.patch
Patch6:		vyper-0006-fix-lang-define-rounding-mode-for-sqrt-4486.patch
Patch7:		vyper-0007-fix-codegen-cache-result-of-iter-eval-4488.patch
Patch8:		vyper-0008-fix-codegen-disable-augassign-with-overlap-4487.patch
Patch9:		vyper-0009-fix-codegen-fix-assertions-for-certain-precompiles-4.patch
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
%{_bindir}/vyper
%{_bindir}/vyper-json

%changelog
%autochangelog
