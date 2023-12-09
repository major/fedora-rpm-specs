# SPDX-License-Identifier: MIT
# Copyright (C) 2023 Maxwell G <maxwell@gtmx.me>

%bcond tests 1

Name:           forge-srpm-macros
Version:        0.2.0
Release:        1%{?dist}
Summary:        Macros to simplify packaging of forge-hosted projects

License:        GPL-1.0-or-later
URL:            https://git.sr.ht/~gotmax23/forge-srpm-macros
Source0:        %{url}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  make
%if %{with tests}
BuildRequires:  python3-pytest
BuildRequires:  python3-pyyaml
# For %%pytest definition
BuildRequires:  python3-rpm-macros
%endif
# We require macros and lua defined in redhat-rpm-config
# We constrain this to the version released after the code was split out that
# doesn't contain the same files.

%if (0%{?fedora} >= 40 || 0%{?rhel} >= 10)
Requires:       redhat-rpm-config >= 266-1
%else
# For testing purposes on older releases,
# we can depend on any version of redhat-rpm-config.
Requires:       redhat-rpm-config
%endif


%description
%{summary}.


%prep
%autosetup -n %{name}-v%{version}


%install
%make_install RPMMACRODIR=%{_rpmmacrodir} RPMLUADIR=%{_rpmluadir}


%check
%if %{with tests}
export MACRO_DIR=%{buildroot}%{_rpmmacrodir}
export MACRO_LUA_DIR="%{buildroot}%{_rpmluadir}"
%pytest
%endif


%files
%license LICENSES/GPL-1.0-or-later.txt
%doc README.md NEWS.md
%{_rpmmacrodir}/macros.forge
%{_rpmluadir}/fedora/srpm/forge.lua


%changelog
* Thu Dec 7 2023 Maxwell G <maxwell@gtmx.me> - 0.2.0-1
- Update to 0.2.0.

* Mon Sep 4 2023 Maxwell G <maxwell@gtmx.me> - 0.1.0-1
- Initial package. Closes rhbz#2237933.
