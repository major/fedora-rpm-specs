Name: python-pysrt
Version: 1.1.2
Release: 22%{?dist}
Summary: Library used to edit or create SubRip files
# Automatically converted from old format: GPLv3 - review is highly recommended.
License: GPL-3.0-only
URL: https://github.com/byroot/pysrt
Source: %{url}/archive/v%{version}/pysrt-%{version}.tar.gz
# https://github.com/byroot/pysrt/issues/92
Patch0: %{name}-1.1.2-use_assertEqual.patch
BuildArch: noarch
BuildRequires: python3-devel
BuildRequires: python3-setuptools
# Tests:
BuildRequires: python3-pytest
BuildRequires: python3-chardet

%global _description %{expand:
pysrt is a Python library used to edit or create SubRip files.}

%description %_description

%package -n python3-pysrt
Summary: %{summary}

%description -n python3-pysrt %_description

%prep
%autosetup -p1 -n pysrt-%{version}

%generate_buildrequires
%pyproject_buildrequires -t

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l pysrt
# Remove shebang from Python3 libraries
for lib in `find %{buildroot}%{python3_sitelib} -name "*.py"`; do
 sed '1{\@^#!/usr/bin/env python@d}' $lib > $lib.new &&
 touch -r $lib $lib.new &&
 mv $lib.new $lib
done

%check
%pytest

%files -n python3-pysrt -f %{pyproject_files}
%doc README.rst
%license LICENCE.txt
%{_bindir}/srt

%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.2-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

%autochangelog
