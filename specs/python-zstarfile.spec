# Copyright (C) 2024 Maxwell G <maxwell@gtmx.me>
# SPDX-License-Identifier: MIT
# License text: https://spdx.org/licenses/MIT

Name:           python-zstarfile
Version:        0.2.0
Release:        6%{?dist}
Summary:        Tarfile extension with additional compression algorithms and PEP 706 by default


License:        MIT
URL:            https://sr.ht/~gotmax23/zstarfile
%global furl    https://git.sr.ht/~gotmax23/zstarfile
Source0:        %{furl}/refs/download/v%{version}/zstarfile-%{version}.tar.gz
Source1:        %{furl}/refs/download/v%{version}/zstarfile-%{version}.tar.gz.asc
Source2:        https://meta.sr.ht/~gotmax23.pgp

# Test Python 3.13 and add basic support for 3.14 and drop 3.8
# https://git.sr.ht/~gotmax23/zstarfile/commit/be51fe5010c76177547954c4fc7ef6a24b3d4f30
Patch:          0001-Test-Python-3.13-and-add-basic-support-for-3.14-and-.patch

BuildArch:      noarch

BuildRequires:  gnupg2
BuildRequires:  python3-devel

Recommends:     %{py3_dist zstarfile[all]}

%global _description %{expand:
zstarfile is a tarfile extension with additional compression algorithms and
PEP 706 by default.}

%description %_description

%package -n python3-zstarfile
Summary:        %{summary}

%description -n python3-zstarfile %_description


%prep
%gpgverify -d0 -s1 -k2
%autosetup -p1 -n zstarfile-%{version}


%generate_buildrequires
%pyproject_buildrequires -x all,lz4,zstandard,test


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files zstarfile


%check
%pytest


%files -n python3-zstarfile -f %{pyproject_files}
%doc README.md
%license LICENSES/*

%pyproject_extras_subpkg -n python3-zstarfile all lz4 zstandard

%changelog
* Tue Jun 10 2025 Maxwell G <maxwell@gtmx.me> - 0.2.0-6
- Fix build with Python 3.14

* Tue Jun 03 2025 Python Maint <python-maint@redhat.com> - 0.2.0-5
- Rebuilt for Python 3.14

* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 14 2024 Maxwell G <maxwell@gtmx.me> - 0.2.0-2
- Rebuild for Python 3.13

* Sun Apr 07 2024 Maxwell G <maxwell@gtmx.me> - 0.2.0-1
- Initial package (rhbz#2274272).
