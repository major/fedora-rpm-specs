Name:           glsl-analyzer
Version:        1.7.1
Release:        %autorelease
Summary:        Language server for GLSL
License:        GPL-3.0-only
URL:            https://github.com/nolanderc/glsl_analyzer
ExclusiveArch:  %{zig_arches}

Source0:        %{url}/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:        https://github.com/nolanderc/glsl-samples/archive/95264d5602cc8542e9e8dbdaab6045f9619ab180.tar.gz#/glsl-samples-95264d5.tar.gz

Patch:          0001-Add-fPIE-compiler-flag.patch
# Updates to 0.15.2
# https://github.com/nolanderc/glsl_analyzer/pull/83
Patch:          0002-update-to-zig-0.15.2.patch

# 0.15.2 introduced changes incompatible with 0.15.1
BuildRequires:  (zig >= 0.15.2 with zig < 0.16)
BuildRequires:  zig-rpm-macros
# testing
BuildRequires:  pytest
BuildRequires:  python3-lsprotocol
BuildRequires:  python3-pytest-subtests
BuildRequires:  python3-pytest-lsp
BuildRequires:  python3-typeguard

%description
Language server for GLSL (OpenGL Shading Language).

%prep
%autosetup -p1 -C
sed -i 's/b.run(&.{ "git", "describe", "--tags", "--always" })/"%{version}"/' build.zig

tar -xf %{SOURCE1} -C tests/glsl-samples --strip-components=1

%build
%zig_prep
%zig_build

%install
%zig_install

%check
# tests stuck on aarch64
%ifnarch aarch64
export PATH="./zig-out/bin:${PATH}"
pytest tests
%endif

%files
%{_bindir}/glsl_analyzer

%license LICENSE.md

%changelog
%autochangelog
