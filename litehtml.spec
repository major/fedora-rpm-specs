#global commit e7fa81d19b2f752f9f68b0494442f34a94e8f143
#global shortcommit %(c=%{commit}; echo ${c:0:7})
#global gitdate 20220107

Name:           litehtml
Version:        0.6
Release:        4%{?commit:.%{gitdate}git%{shortcommit}}%{?dist}
Summary:        Fast and lightweight HTML/CSS rendering engine

License:        BSD
URL:            https://github.com/litehtml/litehtml
%if 0%{?commit:1}
Source0:        https://github.com/litehtml/litehtml/archive/%{commit}/%{name}-%{shortcommit}.tar.gz
%else
Source0:        https://github.com/litehtml/litehtml/archive/v%{version}/%{name}-%{version}.tar.gz
%endif
# Downstream patch
# The Fedora gumbo-parser package does not contain a cmake module,
# so don't look for it
Patch0:         litehtml_gumbo.patch
# Use system gtest
Patch1:         litehtml_gtest.patch

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  gtest-devel
BuildRequires:  gumbo-parser-devel
BuildRequires:  make
BuildRequires:  /usr/bin/xxd


%description
litehtml is the lightweight HTML rendering engine with CSS2/CSS3 support.
Note that litehtml itself does not draw any text, pictures or other graphics
and that litehtml does not depend on any image/draw/font library.


%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       gumbo-parser-devel

%description devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%if 0%{?commit:1}
%autosetup -p1 -n %{name}-%{commit}
%else
%autosetup -p1 -n %{name}-%{version}
%endif

# Ensure no bundled gumbo and xxd are used
rm -rf src/gumbo
rm -rf xxd

# Since 1.13.0, gtest requires C++14 or later
sed -r -i 's/(CXX_STANDARD[[:blank:]]+)11/\114/' CMakeLists.txt

%build
%cmake -DBUILD_TESTING=ON -DEXTERNAL_GUMBO=ON
%cmake_build


%install
%cmake_install


%check
%ctest


%files
%license LICENSE
%doc README.md
%{_libdir}/lib%{name}.so.0*

%files devel
%{_includedir}/%{name}/
%{_libdir}/lib%{name}.so
%{_libdir}/cmake/%{name}


%changelog
* Mon Jan 30 2023 Benjamin A. Beasley <code@musicinmybrain.net> - 0.6-4
- Compile as C++14 instead of C++11 for gtest-0.13.0 compatibility

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon May 30 2022 Sandro Mani <manisandro@gmail.com> - 0.6-1
- Update to 0.6

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.5-7.20220107gite7fa81d
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jan 07 2022 Sandro Mani <manisandro@gmail.com> - 0.5-6.20220107gite7fa81
- Update to git e7fa81

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.5-5.20210323gitb4c815c
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Mar 24 2021 Sandro Mani <manisandro@gmail.com> - 0.5-4.20210323gitb4c815c
- Add litehtml_gumbo.patch

* Tue Mar 23 2021 Sandro Mani <manisandro@gmail.com> - 0.5-3.20210323gitb4c815c
- Update to git b4c815c
- Drop upstreamed patches

* Tue Mar 23 2021 Sandro Mani <manisandro@gmail.com> - 0.5-2.20210317gitb6442d9
- Delete bundled xxd.exe in prep
- Fix changelog formatting

* Fri Mar 19 2021 Sandro Mani <manisandro@gmail.com> - 0.5-1.20210317gitb6442d9
- Update to git b6442d9
- Drop upstreamed patches
- Unbundle downstream
- Enable tests

* Wed Mar 17 2021 Sandro Mani <manisandro@gmail.com> - 0.5-1.gitdb7f59d
- Initial package
