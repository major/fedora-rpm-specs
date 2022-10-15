# what it's called on pypi
%global srcname m2r
# what it's imported as
%global libname m2r


%global common_description %{expand:
M2R converts a markdown file including reST markups to a valid reST format.}

%bcond_without  check

%global commit          66f4a5a500cdd9fc59085106bff082c9cadafaf3
%global shortcommit     %(c=%{commit}; echo ${c:0:7})
%global snapshotdate    20190604

Name:           python-%{srcname}
Version:        0.2.1
Release:        %autorelease -s %{snapshotdate}git%{shortcommit}
Summary:        Markdown to reStructuredText converter

License:        MIT
URL:            https://github.com/miyakogi/%{srcname}
Source0:        %url/archive/%{commit}/%{srcname}-%{shortcommit}.tar.gz

# https://github.com/miyakogi/m2r/pull/62
Patch0:         test_no_file.patch
# https://github.com/miyakogi/m2r/pull/43
Patch1:         %url/pull/43.patch#/lock_mistune_version.patch

BuildArch:      noarch

BuildRequires:  make
BuildRequires:  python3-devel


%description
%{desc}


%package -n python3-%{srcname}
Summary:        %{summary}

%description -n python3-%{srcname} %{common_description}

%package doc
Summary:        Documentation for %{name}

%description doc
%{common_description}

Documentation for %name.

%prep
%autosetup -p1 -n %{srcname}-%{commit}

# https://github.com/sphinx-doc/sphinx/issues/10474
sed -i "s/language = None/language = 'en'/" docs/conf.py

# Remove shebang
sed -i '1{\@^#!/usr/bin/env python@d}' m2r.py

%generate_buildrequires
%pyproject_buildrequires -t

%build
%pyproject_wheel

PYTHONPATH=${PWD} sphinx-build-3 docs html
# remove the sphinx-build leftovers
rm -rf html/.{doctrees,buildinfo}

%install
%pyproject_install
%pyproject_save_files %{libname}

%if %{with check}
%check
%tox
%endif

%files -n python3-%{srcname} -f %{pyproject_files}
%doc README.md
%{_bindir}/m2r

%files doc
%doc html
%license LICENSE

%changelog
%autochangelog
