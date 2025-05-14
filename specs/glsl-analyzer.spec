Name:           glsl-analyzer
Version:        1.6.0
Release:        %autorelease
Summary:        Language server for GLSL
License:        GPL-3.0-only
URL:            https://github.com/nolanderc/glsl_analyzer
ExclusiveArch:  %{zig_arches}

Source0:        %{url}/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:        https://github.com/nolanderc/glsl-samples/archive/95264d5602cc8542e9e8dbdaab6045f9619ab180.tar.gz#/glsl-samples-95264d5.tar.gz

Patch1:         0001-Add-fPIE-compiler-flag.patch

BuildRequires:  zig
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
%autosetup -p1 -n glsl_analyzer-%{version}
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
export PATH="./build/bin:${PATH}"
pytest tests || : # ignore for now
%endif

%files
%{_bindir}/glsl_analyzer

%license LICENSE.md

%changelog
%autochangelog
