Summary:        A C++ JIT assembler for x86
Name:           xbyak
License:        BSD-3-Clause

Version:        7.05.1
Release:        2%{?dist}

URL:            https://github.com/herumi/xbyak
Source0:        %{url}/archive/refs/tags/v%{version}.tar.gz
# exception testing of allocator gets hung up on glibc double free check
Patch0:         xbyak-disable-noexecption-test3.patch

Group:          Development/Libraries
BuildArch:      noarch
ExclusiveArch:  x86_64

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  meson
BuildRequires:  sed

%bcond_with check
%if %{with check}
#  -m32
BuildRequires:  glibc-devel(x86-32), libstdc++(x86-32)
BuildRequires:  nasm, yasm
%endif

%description
Xbyak is a C++ header library that enables dynamically to
assemble x86(IA32), x64(AMD64, x86-64) mnemonic.

The pronunciation of Xbyak is kəi-bja-k, かいびゃく.
It is named from a Japanese word 開闢, which means the beginning
of the world.

%package devel
Summary:        A C++ JIT assembler for x86
Provides:       xbyak-static = %{version}-%{release}

%description devel
Xbyak is a C++ header library that enables dynamically to
assemble x86(IA32), x64(AMD64, x86-64) mnemonic.

The pronunciation of Xbyak is kəi-bja-k, かいびゃく.
It is named from a Japanese word 開闢, which means the beginning
of the world.

%prep
%autosetup -p1

%build
%meson
%meson_build

%install
%meson_install

# Install samples
mkdir -p %{buildroot}%{_datadir}/xbyak/
cp -pr sample %{buildroot}%{_datadir}/xbyak/

%if %{with check}
%check
make test
%endif

%files devel
%license COPYRIGHT
%doc readme.md doc/changelog.md doc/usage.md
%doc %lang(jp) readme.txt
%{_datadir}/%{name}/
%{_includedir}/%{name}/
%{_libdir}/cmake/%{name}/
%{_libdir}/pkgconfig/%{name}.pc

%changelog
* Wed Feb 21 2024 Tom Rix <trix@redhat.com> - 7.05.1-2
- Use meson to build
- Suggested-by: Davide Cavalca

* Tue Feb 20 2024 Tom Rix <trix@redhat.com> - 7.05.1-1
- Update source

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 6.73-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jan 11 2024 Tom Rix <trix@redhat.com> - 6.73-1
- Update to 6.73

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 6.69-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Mar 3 2023 Tom Rix <trix@redhat.com> - 6.69-1
- Update source

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 6.63-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Oct 27 2022 Tom Rix <trix@redhat.com> - 6.63-3
- Make check optional

* Mon Oct 24 2022 Tom Rix <trix@redhat.com> - 6.63-2
- Add tests, samples
- Change license to BSD-3-Clause
- Check directory ownership
- Package as static library

* Fri Oct 21 2022 Tom Rix <trix@redhat.com> - 6.63-1
- Initial release
