# https://docs.fedoraproject.org/en-US/packaging-guidelines/#_use_noarch_only_in_subpackages
%global debug_package %{nil}

Name:           parallel-hashmap
Version:        2.0.0
Release:        %autorelease
Summary:        Family of header-only hashmap and btree containers
License:        Apache-2.0
URL:            https://github.com/greg7mdp/parallel-hashmap
Source:         %{url}/archive/v%{version}/parallel-hashmap-%{version}.tar.gz
# https://github.com/greg7mdp/parallel-hashmap/commit/8bd66dc8ed98ba0e941864edf4d3670e60543f8b
Patch:          0001-CMakeLists.txt-use-external-gtest-fallback-to-fetching-the-source-288.patch
# https://github.com/greg7mdp/parallel-hashmap/commit/8d29d955366a90ffbdb50d3b57694a3b765e17eb
Patch:          0002-Download-gtest-unless-PHMAP_DOWNLOAD_GTEST-is-turned-off.patch

BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  gtest-devel
BuildRequires:  gmock-devel


%description
This repository aims to provide a set of excellent hash map implementations, as
well as a btree alternative to std::map and std::set.


%package        devel
Summary:        Development files for %{name}
# https://docs.fedoraproject.org/en-US/packaging-guidelines/#_packaging_header_only_libraries
Provides:       %{name}-static = %{version}-%{release}
BuildArch:      noarch


%description    devel
The %{name}-devel package contains libraries and header files for developing
applications that use %{name}.


%prep
%autosetup -p 1


%conf
%cmake \
    -DPHMAP_DOWNLOAD_GTEST=OFF \
    -DPHMAP_BUILD_EXAMPLES=OFF


%build
%cmake_build


%install
%cmake_install


%check
%ctest


%files devel
%license LICENSE
%{_includedir}/parallel_hashmap


%changelog
%autochangelog
