Name:           tralics
Version:        3.0.0
Release:        %autorelease
Summary:        LaTeX to XML translator
# Automatically converted from old format: CeCILL - review is highly recommended.
License:        CECILL-2.1
%define forgeurl https://github.com/tralics/tralics
%forgemeta
URL:            %{forgeurl}
Source0:        %{forgesource}

BuildRequires:  make
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  texlive-collection-latexextra
BuildRequires:  spdlog-devel

Provides:       bundled(utfcpp) = 4.0.9
# FIXME: unbundle spdlog when updated
# (https://bugzilla.redhat.com/show_bug.cgi?id=2427058)
Provides:       bundled(spdlog) = 1.17.0
Provides:       bundled(ctre) = 3.10.0

ExcludeArch:    %{ix86}

%global _vpath_builddir build

%description
Tralics is a free software whose purpose is to convert a LaTeX document into 
an XML file. It is used since 2002 for instance to produce the INRIA's 
annual activity report.

%prep
%autosetup -p1
# unbundle spdlog
# rm -r external/spdlog-*/*

%conf
%cmake

%build
%cmake
%cmake_build

%install
%cmake_install

%check
cd test && ./alltests

%files
%doc README.md
%license COPYING COPYRIGHT
%{_bindir}/%{name}
%{_datadir}/%{name}/

%changelog
%autochangelog
