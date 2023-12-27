# Header-only library.
%global debug_package %{nil}

Name:           xtl
Version:        0.7.7
Release:        %autorelease
License:        BSD-3-Clause
Summary:        QuantStack tools library
Url:            https://github.com/QuantStack/xtl
Source0:        https://github.com/QuantStack/%{name}/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:  binutils
BuildRequires:  cmake
BuildRequires:  doctest-devel
BuildRequires:  doxygen
BuildRequires:  gcc-c++
BuildRequires:  make
BuildRequires:  cmake(nlohmann_json)
BuildRequires:  python3dist(breathe)
BuildRequires:  python3dist(sphinx)
BuildRequires:  python3dist(sphinx-rtd-theme)

%description
Basic tools (containers, algorithms) used by other QuantStack packages.


%package devel
Summary:        %{summary}
Provides:       xtl-static = %{version}-%{release}
Requires:       cmake-filesystem

%description devel
Development files for %{name} library.


%package doc
Summary:        %{summary}

%description doc
Documentation files for %{name} library.


%prep
%autosetup -p1


%build
%cmake -DBUILD_TESTS=ON
%cmake_build

pushd docs
make html SPHINXBUILD=sphinx-build-3
rm build/html/.buildinfo
popd


%install
%cmake_install


%check
make -C "%{_vpath_builddir}" xtest


%files devel
%doc README.md
%license LICENSE
%{_includedir}/xtl/
%{_datadir}/cmake/xtl/
%{_datadir}/pkgconfig/xtl.pc

%files doc
%doc docs/build/html


%changelog
%autochangelog
