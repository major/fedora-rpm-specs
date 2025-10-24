# Copyright 2025 Enactic, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

%global commit 010ea250f7ffdcc0d16d16bafd29a713f89df070
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global commitdate 20251016

Name:           openarm-can
Version:        1.1.0^%{commitdate}git%{shortcommit}
Release:        %{autorelease}
Summary:        OpenArm CAN control library

License:        Apache-2.0
URL:            https://docs.openarm.dev/software/can
Source:         https://github.com/enactic/openarm_can/archive/%{commit}/openarm_can-%{shortcommit}.tar.gz

BuildRequires:  cmake
BuildRequires:  gcc-c++
# Needed for old package name
# https://docs.fedoraproject.org/en-US/packaging-guidelines/#renaming-or-replacing-existing-packages
Provides:       openarm_can = %{version}-%{release}
Obsoletes:      openarm_can <= 1.1.0

%description
A C++ library for CAN communication with OpenArm robotic hardware,
supporting Damiao motors over CAN/CAN-FD interfaces. This library
is a part of OpenArm.

%package devel
Summary:   Development files for OpenARM CAN control library
Requires:  %{name}%{?_isa} = %{version}-%{release}

%description devel
Header files and development libraries for OpenARM CAN control library.

%package utils
Summary: Setup and configuration utility scripts

%description utils
Setup and configuration utility scripts.

%prep
%autosetup -n openarm_can-%{commit}


%build
%cmake
%cmake_build


%install
%cmake_install


%files
%license LICENSE.txt
%doc README.md
%{_libdir}/libopenarm_can.so.1{,.*}

%files devel
%{_includedir}/openarm/
%{_libdir}/cmake/OpenArmCAN/
%{_libdir}/libopenarm_can.so
%{_libdir}/pkgconfig/openarm-can.pc

%files utils
%license LICENSE.txt
%{_libexecdir}/openarm-can/

%changelog
%autochangelog
