%global git_hash 73712a01b2de56d9ad91e3b6936f85c90cb7de36
# Not enough memory in our builders since ver. 0.8.30
%global _smp_mflags -j1

Summary:	Object-oriented, high-level language for implementing smart contracts
Name:		solidity
Version:	0.8.30
Release:	%autorelease
# Not enough deps on x86 and does not work on big-endian arches
ExcludeArch:	%{ix86} s390x
URL:		https://soliditylang.org/
Source0:	https://github.com/ethereum/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
# libsolutil/picosha2.h licensed under MIT
SourceLicense:	GPL-3.0-only and MIT
License:	GPL-3.0-only
# Fedora-specific patches
Patch:		solidity-0001-Use-static-linking-for-internal-libs.patch
Patch:		solidity-0002-Don-t-override-Fedora-specific-CXXFLAGS.patch
BuildRequires:	boost-devel
BuildRequires:	cmake >= 3.0
# only for Fedora 40+
BuildRequires:	cmake(fmt) >= 10.1.1
BuildRequires:	cmake(nlohmann_json)
BuildRequires:	cmake(range-v3)
BuildRequires:	cmake(z3)
BuildRequires:	cvc5
BuildRequires:	gcc-c++
BuildRequires:	help2man
# for /usr/bin/cvc5
Requires:	cvc5

%description
Solidity is an object-oriented, high-level language for implementing smart
contracts. Smart contracts are programs which govern the behavior of accounts
within the Ethereum state.

%prep
%autosetup -p1
echo %{git_hash} > commit_hash.txt

%build
%if 0%{?fedora} < 42
export CFLAGS="%{optflags} -Wno-error=array-bounds"
export CXXFLAGS="%{optflags} -Wno-error=array-bounds"
%endif
%{cmake} \
	-DIGNORE_VENDORED_DEPENDENCIES:BOOL=ON \
	-DBoost_USE_STATIC_LIBS:BOOL=OFF \
	-DSTRICT_Z3_VERSION:BOOL=OFF \
	-DTESTS:BOOL=OFF
%cmake_build

help2man --no-discard-stderr --no-info "%{__cmake_builddir}/solc/solc" --version-string=%{version} --output=solc.1
help2man --no-discard-stderr --no-info "%{__cmake_builddir}/tools/yul-phaser" --version-string=%{version} --output=yul-phaser.1

%install
%cmake_install
install -D -pv -m 0644 -t %{buildroot}%{_mandir}/man1/ solc.1 yul-phaser.1

%check
# TODO

%files
%{_bindir}/solc
%{_bindir}/yul-phaser
%doc README.md
%doc SECURITY.md
%license LICENSE.txt
%{_mandir}/man1/solc.1.*
%{_mandir}/man1/yul-phaser.1.*

%changelog
%autochangelog
