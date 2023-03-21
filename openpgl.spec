Name:           openpgl
Version:        0.5.0
Release:        %autorelease
Summary:        Open Path Guiding Library 

License:        Apache-2.0
URL:            https://github.com/OpenPathGuidingLibrary/%{name}
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  cmake
BuildRequires:  embree-devel
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig(tbb) 

# Upstream only supports x86_64 and ARM64 architectures
ExclusiveArch:	aarch64 x86_64

%description
The Intel Open Path Guiding Library (Intel Open PGL) implements
a set of representations and training algorithms needed to 
integrate path guiding into a renderer. 

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%autosetup

# do not install LICENSE.txt
sed -i '/LICENSE.txt/d' openpgl/CMakeLists.txt

%build
# https://github.com/embree/embree/issues/410
%cmake \
	-DCMAKE_CXX_FLAGS="%{optflags} -flax-vector-conversions"
%cmake_build


%install
%cmake_install


%files
%license LICENSE.txt
%doc CHANGELOG.md README.md third-party-programs*.txt
%{_libdir}/lib%{name}.so.*

%files devel
%{_includedir}/%{name}
%{_libdir}/cmake/%{name}-%{version}
%{_libdir}/lib%{name}.so


%changelog
%autochangelog
