# what it's called on pypi
%global srcname m2r
# what it's imported as
%global libname m2r


%global common_description %{expand:
M2R converts a markdown file including reST markups to a valid reST format.}

%bcond_without  check

Name:           python-%{srcname}
Version:        0.3.1
Release:        %autorelease
Summary:        Markdown to reStructuredText converter

License:        MIT
URL:            https://github.com/miyakogi/%{srcname}
Source0:        %{pypi_source %{srcname}}

BuildArch:      noarch

BuildRequires:  make
BuildRequires:  python3-devel

%if %{with check}
BuildRequires:  python3-pygments
BuildRequires:  python3-pytest
%endif


%description
%{desc}


%package -n python3-%{srcname}
Summary:        %{summary}


%description -n python3-%{srcname} %{common_description}


%prep
%autosetup -p1 -n %{srcname}-%{version}

# Remove shebang
sed -i '1{\@^#!/usr/bin/env python@d}' m2r.py


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files %{libname}


%if %{with check}
%check
%pytest
%endif


%files -n python3-%{srcname} -f %{pyproject_files}
%license LICENSE
%doc README.md
%{_bindir}/m2r


%changelog
%autochangelog
