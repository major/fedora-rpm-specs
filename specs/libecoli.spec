# SPDX-License-Identifier: BSD-3-Clause
# Copyright (c) 2024 Robin Jarry

%global forgeurl https://github.com/rjarry/libecoli

Name: libecoli
Version: 0.11.7
Summary: Extensible COmmand LIne library
License: BSD-3-Clause AND LicenseRef-Fedora-Public-Domain

%forgemeta

URL: %{forgeurl}
Release: %{autorelease}
Source: %{forgesource}

BuildRequires: doxygen
BuildRequires: doxygen2man
BuildRequires: gcc
BuildRequires: libedit-devel
BuildRequires: libxml2
BuildRequires: meson
BuildRequires: ninja-build
BuildRequires: pkgconf

%description
libecoli stands for Extensible COmmand LIne library.

This library provides helpers to build interactive command line interfaces.

What can it be used for?

* Complex interactive command line interfaces in C (e.g.: a router CLI).
* Application arguments parsing, native support for bash completion.
* Generic text parsing.

Main Features

* Dynamic completion.
* Contextual help.
* Integrated with libedit, but can use any readline-like library.
* Modular: the CLI behavior is defined through an assembly of basic nodes.
* Extensible: the user can write its own nodes to provide specific features.
* C API.

%package devel
Summary: Development files for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: libedit-devel

%description devel
This package contains development files for %{name}.

%package doc
BuildArch: noarch
Summary: Documentation for %{name}

%description doc
This package contains the HTML documentation for %{name}.

%prep
%forgesetup

%build
%meson -Dexamples=disabled -Dyaml=disabled
%meson_build

%check
%meson_test

%install
%meson_install

%files
%doc README.md
%license LICENSE
%{_libdir}/%{name}.so.0*

%files devel
%{_mandir}/man3/*
%{_includedir}/ecoli.h
%{_includedir}/ecoli/*.h
%{_libdir}/%{name}.so
%{_libdir}/pkgconfig/libecoli.pc

%files doc
%license LICENSE
%{_datadir}/doc/libecoli

%changelog
%autochangelog
