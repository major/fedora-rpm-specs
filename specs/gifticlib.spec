Name:           gifticlib
Version:        1.0.9
Release:        %{autorelease}
Summary:        IO library for the GIFTI cortical surface data format

License:        LicenseRef-Fedora-Public-Domain
URL:            http://www.nitrc.org/projects/gifti/
Source0:        http://www.nitrc.org/frs/download.php/2262/%{name}-%{version}.tgz
# Taken from Debian
Source1:        http://anonscm.debian.org/cgit/pkg-exppsy/gifticlib.git/plain/debian/gifti_test.1
Provides:       gifti = %{version}-%{release}

BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  gcc
BuildRequires:  zlib-devel
BuildRequires:  expat-devel
BuildRequires:  nifticlib-devel

%description
GIFTI is an XML-based file format for cortical surface data. This reference
IO implementation is developed by the Neuroimaging Informatics Technology
Initiative (NIfTI).
This package also provides the tools that are shipped with the GIFTI library
(gifti_tool and gifti_test).

%package        devel
Summary:        Development files for %{name}
Provides:       gifti-devel = %{version}-%{release}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%autosetup
# Remove using ITK-bundled EXPAT and ZLIB (we're not shipping them
# and use proper libsuffix
sed -i \
  -e '/FIND_PACKAGE(ITK)/d' \
  -e '/SET(GIFTI_INSTALL_LIB_DIR/s/lib/%{_lib}/' \
  CMakeLists.txt
rm -rf build/

%build
export CMAKE_POLICY_VERSION_MINIMUM=3.5
%cmake
%cmake_build

%install
%cmake_install

# Remove static libs
rm -f %{buildroot}%{_libdir}/*.a
mkdir -p %{buildroot}%{_mandir}/man1/
install -p -m0644 %{SOURCE1} %{buildroot}%{_mandir}/man1/


%files
%license LICENSE.gifti
%{_bindir}/gifti_*
%{_libdir}/libgifti*.so.*
%{_mandir}/man1/gifti_*.1.*

%files devel
%doc README.gifti
%{_includedir}/gifti/
%{_libdir}/libgifti*.so

%changelog
%autochangelog
