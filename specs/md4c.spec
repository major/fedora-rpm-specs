Version:        0.5.1
Name:           md4c
Release:        3%{?dist}
Summary:        Markdown for C

License:        MIT
URL:            https://github.com/mity/md4c
Source0:        %{url}/archive/release-%{version}/%{name}-%{version}.tar.gz

BuildRequires: cmake
BuildRequires: gcc 
# Needed for tests
BuildRequires:  python3

%description
MD4C is Markdown parser implementation in C.

%package        devel
Summary:        Development files for md4c
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The md4c-devel package contains libraries and header files for
developing applications that use md4c.

%prep
%autosetup -n %{name}-release-%{version}

%build
%cmake
%cmake_build

%install
%cmake_install

%check
cd %__cmake_builddir
bash %{_builddir}/%{name}-release-%{version}/scripts/run-tests.sh 

%files
%doc README.md
%doc CHANGELOG.md
%license LICENSE.md
%{_bindir}/md2html
%{_libdir}/libmd4c-html.so.0*
%{_libdir}/libmd4c.so.0*
%{_mandir}/man1/md2html.1*

%files devel
%{_includedir}/md4c.h
%{_includedir}/md4c-html.h
%{_libdir}/libmd4c-html.so
%{_libdir}/libmd4c.so
%dir %{_libdir}/cmake/md4c
%{_libdir}/cmake/md4c/*.cmake
%{_libdir}/pkgconfig/md4c.pc
%{_libdir}/pkgconfig/md4c-html.pc

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Mon Jan 29 2024 Benson Muite <benson_muite@emailplus.org> - 0.5.1-1
- Upgrade to latest release

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 29 2023 Benson Muite <benson_muite@emailplus.org> - 0.4.8-1
- Initial packaging
