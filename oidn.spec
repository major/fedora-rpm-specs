Name:           oidn
Version:        1.4.3
Release:        %autorelease
Summary:        Library of denoising filters for images rendered with ray tracing
License:        ASL 2.0
URL:            https://openimagedenoise.github.io/

Source0:        https://github.com/OpenImageDenoise/%{name}/releases/download/v%{version}/%{name}-%{version}.src.tar.gz

# Library only available on x86_64
ExclusiveArch:  x86_64

BuildRequires:  cmake >= 3.13.0
# Needed to remove rpath from apps
BuildRequires:  chrpath
BuildRequires:  gcc-c++
BuildRequires:  ispc
BuildRequires:  pkgconfig(OpenImageIO)
BuildRequires:  pkgconfig(python3)
BuildRequires:  pkgconfig(tbb)

%description
An open source library of high-performance, high-quality denoising filters for
images rendered with ray tracing.

%package        libs
Summary:        Libraries for %{name}

%description    libs
The %{name}-libs package contains shared library for %{name}.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

%description devel
The %{name}-devel package contains libraries and header files for developing
applications that use %{name}.

%package        docs
Summary:        Documentation for %{name}
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}
BuildArch:      noarch

%description docs
The %{name}-docs package contains documentation for %{name}.

%prep
%autosetup -p1

%build
%cmake \
    -DCMAKE_VERBOSE_MAKEFILE:BOOL=TRUE

%cmake_build

%install
%cmake_install

# Remove rpath
chrpath --delete %{buildroot}%{_bindir}/%{name}{Denoise,Test,Benchmark}
chrpath --delete %{buildroot}%{_libdir}/libOpenImageDenoise.so.*


# Remove duplicated documentation
rm -rf %{buildroot}%{_docdir}/OpenImageDenoise

%files
%license LICENSE.txt
%doc CHANGELOG.md 
%{_bindir}/%{name}{Denoise,Test,Benchmark}

%files libs
%{_libdir}/libOpenImageDenoise.so.*

%files docs
%doc README.md readme.pdf 

%files devel
%{_libdir}/cmake/OpenImageDenoise-%{version}/*.cmake
%{_includedir}/OpenImageDenoise
%{_libdir}/libOpenImageDenoise.so

%changelog
%autochangelog
