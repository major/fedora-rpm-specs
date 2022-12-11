Name:           openpgl
Version:        0.4.1
Release:        %autorelease -p -e beta
Summary:        Open Path Guiding Library 

License:        Apache-2.0
URL:            https://github.com/OpenPathGuidingLibrary/%{name}
Source0:        %{url}/archive/refs/tags/v%{version}-beta.tar.gz#/%{name}-%{version}-beta.tar.gz

BuildRequires:  cmake
BuildRequires:  embree-devel
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig(tbb) 

# Upstream only supports x86_64 architecture
ExclusiveArch:	x86_64

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
%autosetup -n %{name}-%{version}-beta


%build
%cmake
%cmake_build


%install
%cmake_install
find %{buildroot} -name '*.la' -exec rm -f {} ';'

# Remove duplicated license file
rm %{buildroot}%{_datadir}/doc/%{name}/LICENSE.txt

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
