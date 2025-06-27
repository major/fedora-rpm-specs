%global srcname guessit

Name: python-%{srcname}
Version: 3.8.0
Release: 8%{?dist}
Summary: Library to extract as much information as possible from a video filename
# Automatically converted from old format: LGPLv3 - review is highly recommended.
License: LGPL-3.0-only
URL: https://guessit.readthedocs.org/
Source: https://github.com/guessit-io/%{srcname}/archive/v%{version}/%{srcname}-%{version}.tar.gz
BuildArch: noarch
BuildRequires: python3-devel

%global _description %{expand:
GuessIt is a python library that extracts as much information as possible from
a video filename.

It has a very powerful matcher that allows to guess properties from a video
using its filename only. This matcher works with both movies and TV shows
episodes.}

%description %_description

%package -n python3-%{srcname}
Summary: %{summary}
Suggests: %{name}-doc = %{version}-%{release}

%description -n python3-%{srcname} %_description

%package doc
Summary: Documentation for %{srcname} python library

%description doc %_description

%prep
%autosetup -p1 -n %{srcname}-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
# Remove shebang from Python3 libraries
for lib in `find %{buildroot}%{python3_sitelib} -name "*.py"`; do
 sed '1{\@^#!/usr/bin/env python@d}' $lib > $lib.new &&
 touch -r $lib $lib.new &&
 mv $lib.new $lib
done

%pyproject_save_files -l %{srcname}

# Checks disabled because they require access to the Internet
#%%check
#%%pytest

%files -n python3-%{srcname} -f %{pyproject_files}
%doc README.md
%{_bindir}/%{srcname}

%files doc
%doc README.md AUTHORS.md CONTRIBUTING.md CHANGELOG.md docs
%license LICENSE

%changelog
%autochangelog
