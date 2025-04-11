Name:           python-lxml-html-clean
Version:        0.4.2
Release:        %autorelease
Summary:        HTML cleaner from lxml project
License:        BSD-3-Clause
URL:            https://github.com/fedora-python/lxml_html_clean/
Source:         %{url}/archive/refs/tags/%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python3-devel

%global _description %{expand:
HTML cleaner from lxml project.}

%description %_description

%package -n     python3-lxml-html-clean
Summary:        %{summary}

%description -n python3-lxml-html-clean %_description


%prep
%autosetup -p1 -n lxml_html_clean-%{version}
sed -i "/memory_profiler/d" tox.ini


%generate_buildrequires
%pyproject_buildrequires -t


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files -l lxml_html_clean


%check
%tox


%files -n python3-lxml-html-clean -f %{pyproject_files}
%doc CHANGES.rst README.md


%changelog
%autochangelog
