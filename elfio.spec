%global debug_package %{nil}

Name:           elfio
Version:        3.12
Release:        %autorelease
Summary:        C++ library for reading and generating ELF files

# This is the proper SPDX license
License:        MIT
URL:            http://elfio.sourceforge.net/
Source0:        https://downloads.sf.net/elfio/elfio-%{version}.tar.gz

BuildRequires:  gcc-c++
BuildRequires:  cmake

%description
ELFIO is a small, header-only C++ library that provides a simple interface for
reading and generating files in ELF binary format.

It is used as a standalone library - it is not dependent on any other product
or project. Adhering to ISO C++, it compiles on a wide variety of
architectures and compilers.

While the library is easy to use, some basic knowledge of the ELF binary
format is required. Such Information can easily be found on the Web.


%package devel
Summary:        %{summary}
Provides:       %{name}-static = %{version}-%{release}
BuildArch:      noarch

%description devel
ELFIO is a small, header-only C++ library that provides a simple interface for
reading and generating files in ELF binary format.

It is used as a standalone library - it is not dependent on any other product
or project. Adhering to ISO C++, it compiles on a wide variety of
architectures and compilers.

While the library is easy to use, some basic knowledge of the ELF binary
format is required. Such Information can easily be found on the Web.


%prep
%autosetup -p1


%build
%cmake -DELFIO_BUILD_EXAMPLES=ON
%cmake_build

%install
%cmake_install
rm -r %{buildroot}%{_datadir}/docs

%check
# Sanity check
%{_vpath_builddir}/examples/elfdump/elfdump %{_bindir}/cmake

%files devel
%license LICENSE.txt
%doc doc/elfio.pdf README.md
%{_includedir}/elfio/
%{_datadir}/elfio/


%changelog
%autochangelog
