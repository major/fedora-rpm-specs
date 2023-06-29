Name:           glsl-language-server
Version:        0.4.1
Release:        1%{?dist}
Summary:        Language server implementation for OpenGL Shading Language
License:        MIT
URL:            https://github.com/svenstaro/glsl-language-server

Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz

Patch1:         0001-Remove-support-for-HTTP-and-mongoose-dependency.patch
Patch2:         0002-Port-to-current-CLI11.patch
Patch3:         0003-Use-system-libraries.patch

BuildRequires:  gcc-c++
BuildRequires:  cmake

BuildRequires:  cli11-devel
BuildRequires:  fmt-devel
BuildRequires:  glslang-devel
BuildRequires:  json-devel

%description
Language server implementation for OpenGL Shading Language.

%prep
%autosetup -p1

%build
%cmake
%cmake_build

%install
%cmake_install

%files
%license LICENSE
%{_bindir}/glslls

%changelog
* Thu May 18 2023 Marian Koncek <mkoncek@redhat.com> - 0.4.1-1
- Initial build
