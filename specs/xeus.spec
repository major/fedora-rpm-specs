Name:           xeus
Version:        5.2.4
Release:        %autorelease
Summary:        C++ implementation of the Jupyter kernel protocol

License:        BSD-3-Clause
URL:            https://github.com/jupyter-xeus/xeus
Source0:        https://github.com/jupyter-xeus/xeus/archive/%{version}/%{name}-%{version}.tar.gz

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch: %{ix86}

BuildRequires:  cmake >= 3.8
BuildRequires:  cmake(nlohmann_json) >= 3.11.0
BuildRequires:  doctest-devel
BuildRequires:  doxygen
BuildRequires:  gcc-c++
BuildRequires:  libuuid-devel
BuildRequires:  make
BuildRequires:  pkgconfig(uuid)
BuildRequires:  python3dist(breathe)
BuildRequires:  python3dist(jupyter-kernel-test)
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(sphinx)
BuildRequires:  python3dist(sphinx-rtd-theme)

%description
xeus is a library meant to facilitate the implementation of kernels for
Jupyter. It takes the burden of implementing the Jupyter Kernel protocol so
developers can focus on implementing the interpreter part of the kernel.


%package devel
Summary:        %{summary}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
Development files for %{name} library.


%prep
%autosetup -p1


%build
%cmake -DXEUS_BUILD_STATIC_LIBS=OFF -DXEUS_DISABLE_ARCH_NATIVE=ON -DXEUS_BUILD_TESTS=ON
%cmake_build

make -C docs SPHINXBUILD=sphinx-build-3 html
rm docs/build/html/.buildinfo


%install
%cmake_install


%check
%ctest


%files
%doc README.md docs/build/html
%license LICENSE
%{_libdir}/libxeus.so.13{,.*}

%files devel
%{_includedir}/xeus/
%{_libdir}/cmake/xeus/
%{_libdir}/libxeus.so


%changelog
%autochangelog
