%global pypi_name git_dumper

Name:           git-dumper
Version:        1.0.9
Release:        %autorelease
Summary:        A tool to dump a git repository from a website

License:        MIT
URL:            https://github.com/arthaud/git-dumper
Source0:        %pypi_source

BuildArch:      noarch
BuildRequires:  python3-devel

%description
%{summary}.


%prep
%autosetup -n %{pypi_name}-%{version} -p1
sed -i '1{\@^#!/usr/bin/env python@d}' ./git_dumper.py


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files -l %{pypi_name}


%check
%pyproject_check_import


%files -f %{pyproject_files}
%license LICENSE
%doc README.md
%{_bindir}/git-dumper


%changelog
%autochangelog
