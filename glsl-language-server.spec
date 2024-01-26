Name:           glsl-language-server
Version:        0.5.0
Release:        3%{?dist}
Summary:        Language server implementation for OpenGL Shading Language
License:        MIT
URL:            https://github.com/svenstaro/glsl-language-server

Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz

Patch1:         0001-Remove-unneeded-libraries.patch

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
%cmake -DUSE_SYSTEM_LIBS=ON -DHTTP_SUPPORT=OFF
%cmake_build

%install
%cmake_install

%files
%license LICENSE
%{_bindir}/glslls

%changelog
* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Oct 11 2023 Marian Koncek <mkoncek@redhat.com> - 0.5.0-1
- Update to upstream version 0.5.0

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jul 01 2023 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.4.1-2
- Rebuild for fmtlib 10

* Thu May 18 2023 Marian Koncek <mkoncek@redhat.com> - 0.4.1-1
- Initial build
