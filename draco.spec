# Disable test until a proper fix occurs
%global		gtestflag 0
Name:		draco
Version:	1.5.7
Release:	%autorelease
Summary:	A library for compressing and decompressing 3D geometric meshes and point clouds
License:	Apache-2.0
URL:            https://github.com/google/%{name}
Source:         %{url}/archive/%{version}/%{name}-%{version}.tar.gz

# Downstream-only patch that unconditionally links a system copy of gtest,
# rather than expecting a git submodule as upstream prefers (and gtest upstream
# would recommend).
Patch:		0001-Use-system-gtest.patch

BuildRequires:	cmake
%if %{?gtestflag}
BuildRequires:	cmake(gtest)
%endif
BuildRequires:	gcc
BuildRequires:	gcc-c++
BuildRequires:	help2man
BuildRequires:	ninja-build
BuildRequires:	pkgconfig(python3)

%description
A library for compressing and decompressing 3D geometric meshes and point clouds

%package	devel
Summary: Development files for draco
Requires: %{name}%{?_isa} = %{version}-%{release}

%description	devel
%{summary}.

%package	static
Summary: Static files for draco
Requires: %{name}-devel%{?_isa} = %{version}-%{release}

%description	static
%{summary}.

%prep
%autosetup -p1 -n %{name}-%{version}

# Remove precompiled CSS and Javascript along binaries
rm -fr {javascript,maya,docs/assets}

%build
%cmake -GNinja \
    -DBUILD_SHARED_LIBS=ON \
    -DCMAKE_BUILD_TYPE=Release \
    -DDRACO_TESTS=%{gtestflag}
%cmake_build

%install
%cmake_install

# Create missing man files downstream
mkdir -p %{buildroot}%{_mandir}/man1
LD_LIBRARY_PATH=%{buildroot}%{_libdir} help2man -N --version-string=%{version} \
	-o %{buildroot}%{_mandir}/man1/%{name}_decoder-%{version}.1 \
	%{buildroot}%{_bindir}/%{name}_decoder
LD_LIBRARY_PATH=%{buildroot}%{_libdir} help2man -N --version-string=%{version} \
	-o %{buildroot}%{_mandir}/man1/%{name}_encoder-%{version}.1 \
	%{buildroot}%{_bindir}/%{name}_encoder

%if %{?gtestflag}
%check
# Disable test for s390x architecture
%ifnarch s390x
%{_vpath_builddir}/draco_tests
%endif
%endif

%files
%license LICENSE AUTHORS
%doc README.md
%{_bindir}/%{name}_decoder
%{_bindir}/%{name}_decoder-%{version}
%{_bindir}/%{name}_encoder
%{_bindir}/%{name}_encoder-%{version}
%{_libdir}/lib%{name}.so.9
%{_libdir}/lib%{name}.so.9.0.0
%{_mandir}/man1/%{name}_decoder-%{version}.1*
%{_mandir}/man1/%{name}_encoder-%{version}.1*

%files devel
%{_includedir}/%{name}/
%{_datadir}/cmake/%{name}/
%{_libdir}/lib%{name}.so
%{_libdir}/pkgconfig/%{name}.pc

%files static
%{_libdir}/lib%{name}.a

%changelog
%autochangelog
