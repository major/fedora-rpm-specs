# Tests requires network access
%bcond_with test

# https://docs.fedoraproject.org/en-US/packaging-guidelines/#_do_not_use_noarch
%global debug_package %{nil}

Name:       toml11
Version:    3.7.1
Release:    2%{?dist}
Summary:    TOML for Modern C++ 

License:    MIT
URL:        https://github.com/ToruNiina/toml11
Source0:    %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: ninja-build

%if %{with test}
BuildRequires: boost-devel
BuildRequires: git-core
%endif

%global _description %{expand:
toml11 is a C++11 (or later) header-only toml parser/encoder depending only on
C++ standard library.

  * It is compatible to the latest version of TOML v1.0.0.
  * It is one of the most TOML standard compliant libraries, tested with the
    language agnostic test suite for TOML parsers by BurntSushi.
  * It shows highly informative error messages. You can see the error messages
    about invalid files at CircleCI.
  * It has configurable container. You can use any random-access containers
    and key-value maps as backend containers.
  * It optionally preserves comments without any overhead.
  * It has configurable serializer that supports comments, inline tables,
    literal strings and multiline strings.
  * It supports user-defined type conversion from/into toml values.
  * It correctly handles UTF-8 sequences, with or without BOM, both on posix
    and Windows.}

%description %{_description}


%package    devel
Summary:    Development files for %{name}
Provides:   %{name}-static = %{version}-%{release}

%description devel %{_description}

Development files for %{name}.


%prep
%autosetup -p1


%build
%cmake \
    -G Ninja \
    %if %{with test}
    -Dtoml11_BUILD_TEST=ON \
    %endif
    %{nil}
%cmake_build


%install
%cmake_install


%files devel
%license LICENSE
%doc README.md
%{_includedir}/*.hpp
%{_includedir}/toml/
%{_libdir}/cmake/%{name}/


%changelog
* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.7.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Mar 12 2022 Artem Polishchuk <ego.cordatus@gmail.com> - 3.7.1-1
- chore(update): 3.7.1

* Mon Feb 21 2022 Lukáš Hrázký <lhrazky@redhat.com> - 3.6.1-5
- Backport from upstream: 21732fc - Resolve g++ warning: free-nonheap-object

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.6.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.6.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Apr 27 2021 Artem Polishchuk <ego.cordatus@gmail.com> - 3.6.1-2
- fix: Do not use noarch | RH#1954188

* Wed Apr 21 2021 Artem Polishchuk <ego.cordatus@gmail.com> - 3.6.1-1
- Initial package
