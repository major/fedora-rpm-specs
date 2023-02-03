Name:          maeparser
Version:       1.3.1
Release:       %autorelease
Summary:       A parser for Schrodinger Maestro files
License:       MIT
URL:           https://github.com/schrodinger/%{name}/
Source0:       %{url}archive/refs/tags/v%{version}.tar.gz

# put cmake config in architecture-correct location
# pull request: https://github.com/schrodinger/maeparser/pull/73

BuildRequires:  boost-devel
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  git
BuildRequires:  make
BuildRequires:  zlib-devel


%global common_description %{expand: \
 Maestro is a commercial "all-purpose molecular modeling environment",
 produced and distributed by the company Schrödinger. Maestro has its
 own cognate file format, typically associated with the ".mae" file
 extension. This package provides an open-source parser for the Maestro
 file format, released and maintained by the Maestro developers.
 This facilitates a lossless transition from the widely accepted suite
 of Schrödinger into local custom developments or the open-source world
 at large. Maeparser handles output from:
 * Molecular Dynamics applications, such as Desmond and FEP+
 * Ligand-Protein Docking applications, such as Glide
 * Homology Modeling and folding applications, such as Prime
 * Ligand-based search applications, such as Phase and Phase Shape
 * Quantum Mechanics applications, such as Jaguar
 * Protein-Protein Docking applications
 * ... many other backends used in both Life and Material Sciences}

%description
%{common_description}

%package devel
Requires: %{name}%{_isa} = %{version}-%{release}
Summary: Header files for maeparser
%description devel
 .
 This package contains header files needed for developing applications with
 maeparser.

%prep
%autosetup -n %{name}-%{version}


%build
%set_build_flags
%cmake
%cmake_build

%install
%cmake_install

%files
%license LICENSE.txt
%doc README.md
%{_libdir}/lib%{name}.so.1
%{_libdir}/lib%{name}.so.%{version}

%files devel
%{_includedir}/%{name}
%{_libdir}/lib%{name}.so
%{_libdir}/cmake/%{name}*.cmake

%changelog
%autochangelog
