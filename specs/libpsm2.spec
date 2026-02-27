#
#  This file is provided under a dual BSD/GPLv2 license.  When using or
#  redistributing this file, you may do so under either license.
#
#  GPL LICENSE SUMMARY
#
#  Copyright(c) 2015 Intel Corporation.
#
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of version 2 of the GNU General Public License as
#  published by the Free Software Foundation.
#
#  This program is distributed in the hope that it will be useful, but
#  WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
#  General Public License for more details.
#
#  Contact Information:
#  Intel Corporation, www.intel.com
#
#  BSD LICENSE
#
#  Copyright(c) 2015 Intel Corporation.
#
#  Redistribution and use in source and binary forms, with or without
#  modification, are permitted provided that the following conditions
#  are met:
#
#    * Redistributions of source code must retain the above copyright
#      notice, this list of conditions and the following disclaimer.
#    * Redistributions in binary form must reproduce the above copyright
#      notice, this list of conditions and the following disclaimer in
#      the documentation and/or other materials provided with the
#      distribution.
#    * Neither the name of Intel Corporation nor the names of its
#      contributors may be used to endorse or promote products derived
#      from this software without specific prior written permission.
#
#  THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
#  "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
#  LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
#  A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT
#  OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
#  SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
#  LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
#  DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
#  THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
#  (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
#  OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
#
# Copyright (c) 2014-2015 Intel Corporation. All rights reserved.
#
Summary: Intel PSM Libraries
Name: libpsm2
Version: 12.0.1
Release: %autorelease
# Automatically converted from old format: BSD or GPLv2 - review is highly recommended.
License: LicenseRef-Callaway-BSD OR GPL-2.0-only
URL: https://github.com/cornelisnetworks/opa-psm2/

Source0: https://github.com/cornelisnetworks/opa-psm2/archive/refs/tags/PSM2_%{version}.tar.gz

# The OPA product is supported on x86_64 only:
ExclusiveArch: x86_64
BuildRequires: libuuid-devel
BuildRequires: numactl-devel
BuildRequires: systemd
BuildRequires: gcc
BuildRequires: make
Obsoletes: hfi1-psm < 1.0.0

%package devel
Summary: Development files for Intel PSM
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: libuuid-devel

%package compat
Summary: Compat library for Intel PSM
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: systemd-udev

%global _privatelibs libpsm_infinipath[.]so[.]1.*
%global __provides_exclude ^(%{_privatelibs})$
%global __requires_exclude ^(%{_privatelibs})$

%description
The PSM Messaging API, or PSM API, is the low-level
user-level communications interface for the Intel OPA
family of products. PSM users are enabled with mechanisms
necessary to implement higher level communications
interfaces in parallel environments.

%description devel
Development files for the Intel PSM library

%description compat
Support for MPIs linked with PSM versions < 2

%patchlist
# upstream commits PSM2_12.0.1..master
0001-Fix-strlcat-multiple-definition-build-error.patch
0002-Fix-unaligned-heap-allocations-of-aligned-structs.patch

%prep
%autosetup -p1 -n opa-psm2-PSM2_%{version}

%build
%{set_build_flags}
%{make_build} WERROR=

%install
%make_install DISTRO=%{?rhel:rhel}%{!?rhel:fedora}
rm -f %{buildroot}%{_libdir}/*.a

%ldconfig_scriptlets

%files
%license COPYING
%{_libdir}/libpsm2.so.2.*
%{_libdir}/libpsm2.so.2
%if 0%{?rhel} >= 8
%{_udevrulesdir}/40-psm.rules
%endif


%files devel
%{_libdir}/libpsm2.so
%{_includedir}/psm2.h
%{_includedir}/psm2_mq.h
%{_includedir}/psm2_am.h
%{_includedir}/hfi1diag

%files compat
%{_libdir}/psm2-compat
%{_udevrulesdir}/40-psm-compat.rules
%{_prefix}/lib/libpsm2
%if 0%{?fedora}
%{_prefix}/lib/modprobe.d/libpsm2-compat.conf
%endif
%if 0%{?rhel} >= 8
%{_sysconfdir}/modprobe.d/libpsm2-compat.conf
%endif

%changelog
%autochangelog
