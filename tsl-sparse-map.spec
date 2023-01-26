%global debug_package %{nil}

%global srcname sparse-map

%global _description %{expand:
The sparse-map library is a C++ implementation of a memory efficient hash map
and hash set. It uses open-addressing with sparse quadratic probing. The goal
of the library is to be the most memory efficient possible, even at low load
factor, while keeping reasonable performances.}

Name:           tsl-%{srcname}
Version:        0.6.2
Release:        %autorelease
Summary:        C++ implementation of a memory efficient hash map and hash set 

License:        MIT
URL:            https://github.com/Tessil/%{srcname}
Source0:        %{url}/archive/v%{version}/%{srcname}-%{version}.tar.gz

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  sed

BuildRequires:  boost-devel

%description    %{_description}

%package        devel
Summary:        %{summary}

%description    devel %{_description}

%prep
%autosetup -n %{srcname}-%{version}

# Warnings shouldn't break the build
sed -i 's/-Werror//' tests/CMakeLists.txt

%build
%cmake
%cmake_build

%install
%cmake_install

%check
pushd tests
%cmake
%cmake_build
./%{_vpath_builddir}/tsl_sparse_map_tests

%files devel
%license LICENSE
%doc README.md
# Directory shared with other libraries by the same author, e.g. robin-map
%dir %{_includedir}/tsl
%{_includedir}/tsl/sparse_*.h
%{_datadir}/cmake/%{name}

%changelog
%autochangelog
