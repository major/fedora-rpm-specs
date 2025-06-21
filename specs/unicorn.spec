Name:           unicorn
Version:        2.1.3
Release:        %autorelease
Summary:        Lightweight multi-platform, multi-architecture CPU emulator framework

# GPLv2:        Most of unicorn is licensed under the GPLv2, with exception
#               being the code which followed the project's fork of QEMU.
# LGPLv2:       Portions of code from QEMU
# MIT:          Portions of code from QEMU
# BSD:          Portions of code from QEMU
License:        GPL-2.0-only AND LGPL-2.1-or-later AND MIT AND BSD-2-Clause AND BSD-3-Clause
URL:            https://www.unicorn-engine.org/
Source0:        https://github.com/unicorn-engine/%{name}/archive/%{version}/%{name}-%{version}.tar.gz
Source1:        COPYING

BuildRequires:  cmake
BuildRequires:  gcc
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools

# Much of Unicorn follows from QEMU, which the Unicorn project forked in
# 2015. Since then, the Unicorn team has applied a number of bugfixes to
# the forked QEMU code along with the modifications necessary for Unicorn.
# QEMU 2.2.1 formed the basis of this work. The Unicorn project documents
# the relationship between Unicorn and QEMU at
# http://www.unicorn-engine.org/docs/beyond_qemu.html.
Provides: bundled(qemu) = 2.2.1

%global _description %{expand:
Unicorn is a lightweight multi-platform, multi-architecture CPU emulator
framework.}

%description %_description

%package devel
Summary:        Files needed to develop applications using unicorn
Requires:       %{name} = %{version}-%{release}

%description devel
This package provides the libraries, include files, and other resources
needed for developing applications using unicorn.

%package -n python3-unicorn
Summary:        %{summary}
Requires:       %{name} = %{version}-%{release}
Requires:       python3-setuptools
%{?python_provide:%python_provide python3-%{name}}

%description -n python3-unicorn
The unicorn-python3 package contains python3 bindings for unicorn.

%prep
%autosetup -p1 -n %{name}-%{version}

%generate_buildrequires
%pyproject_buildrequires

cp -p %SOURCE1 .

%build
pushd src
%cmake
%cmake_build
popd

%pyproject_wheel

%install
pushd src
%cmake_install
popd

%pyproject_install

rm $RPM_BUILD_ROOT%{_libdir}/libunicorn.a
rm $RPM_BUILD_ROOT%{_libdir}/unicorn.o

%check

%files
%doc src/AUTHORS.TXT src/CREDITS.TXT src/README.md
%license COPYING
%{_libdir}/libunicorn.so.2

%files devel
%{_libdir}/libunicorn.so
%{_libdir}/pkgconfig/unicorn.pc
%{_includedir}/unicorn/

%files -n python3-unicorn
%{python3_sitearch}/%{name}-%{version}.dist-info/
%{python3_sitearch}/%{name}/

%changelog
%autochangelog
