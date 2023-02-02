Name:          Catch2
Version:       3.3.1
Release:       1%{?dist}
Summary:       A modern, C++-native, test framework

License:       BSL-1.0
URL:           https://github.com/catchorg/Catch2
Source0:       %{url}/archive/refs/tags/v%{version}/%{name}-%{version}.tar.gz

BuildRequires: gcc-c++
BuildRequires: cmake
BuildRequires: doxygen
BuildRequires: pkgconfig
BuildRequires: python3-devel
# The source includes bundled Clara and modified textflow
# https://github.com/catchorg/Catch2/blob/devel/third_party/clara.hpp
# https://github.com/catchorg/textflowcpp
# However, upstream Clara is no longer in development
# https://github.com/catchorg/Clara

%global _description %{expand:
Catch2 is mainly a unit testing framework for C++, but it also provides basic
micro-benchmarking features, and simple BDD macros.}

%description
%_description

%package devel
Summary:   Header files for Catch2 testing framework
Requires:  %{name}%{?_isa} = %{version}-%{release}

%description devel
%_description

%prep
%autosetup
# Do not generate HTML
sed -i 's/GENERATE_HTML          = YES/GENERATE_HTML          = NO/' Doxyfile
sed -i 's/GENERATE_MAN           = NO/GENERATE_MAN           = YES/' Doxyfile

%build
%cmake -DBUILD_SHARED_LIBS=ON \
       -DCATCH_DEVELOPMENT_BUILD=ON \
       -DBUILD_TESTING=ON \
       -DCMAKE_INSTALL_DOCDIR=%{_docdir}/%{name} \
       -DPKGCONFIG_INSTALL_DIR=%{_libdir}/pkgconfig
%cmake_build

%install
%cmake_install

%check
%ctest

%files
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/gdbinit
%{_datadir}/%{name}/lldbinit
%{_docdir}/%{name}/*.md
%dir %{_libdir}/cmake/%{name}
%{_libdir}/cmake/%{name}/*.cmake
%{_libdir}/libCatch2.so.3*
%{_libdir}/libCatch2Main.so.3*
%license LICENSE.txt
%doc README.md SECURITY.md

%files devel
%dir %{_includedir}/catch2
%{_includedir}/catch2/*.hpp
%dir %{_includedir}/catch2/benchmark
%{_includedir}/catch2/benchmark/*.hpp
%dir %{_includedir}/catch2/benchmark/detail
%{_includedir}/catch2/benchmark/detail/*.hpp
%dir %{_includedir}/catch2/generators
%{_includedir}/catch2/generators/*.hpp
%dir %{_includedir}/catch2/interfaces
%{_includedir}/catch2/interfaces/*.hpp
%dir %{_includedir}/catch2/internal
%{_includedir}/catch2/internal/*.hpp
%dir %{_includedir}/catch2/matchers
%{_includedir}/catch2/matchers/*.hpp
%dir %{_includedir}/catch2/matchers/internal
%{_includedir}/catch2/matchers/internal/*.hpp
%dir %{_includedir}/catch2/reporters
%{_includedir}/catch2/reporters/*.hpp
%{_libdir}/pkgconfig/*.pc
%{_libdir}/libCatch2.so
%{_libdir}/libCatch2Main.so

%changelog
* Tue Jan 31 2023 Benson Muite <benson_muite@emailplus.org> 3.3.1-1
- Update based on review
- Indicate directory ownerships
- Add dist tag
- Update version

* Sun Jan 29 2023 Benson Muite <benson_muite@emailplus.org> 3.3.0-1
- Initial packaging based on OpenSUSE spec available at 
https://copr.fedorainfracloud.org/coprs/carlosguirao/Catch2/ 
