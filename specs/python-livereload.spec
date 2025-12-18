Name:           python-livereload
Version:        2.7.1
Release:        %autorelease
Summary:        Reload webpages on changes
License:        BSD-3-Clause
URL:            https://github.com/lepture/python-livereload
Source:         %{pypi_source livereload}
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-pytest

%global _description %{expand:
Reload webpages on changes, without hitting refresh in your browser.}


%description %_description


%package -n python3-livereload
Summary:        %{summary}


%description -n python3-livereload %_description


%prep
%autosetup -p1 -n livereload-%{version}


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files -l livereload


%check
%pytest


%files -n python3-livereload -f %{pyproject_files}
%{_bindir}/livereload


%changelog
%autochangelog
