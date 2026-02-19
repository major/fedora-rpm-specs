%{?!python3_pkgversion:%global python3_pkgversion 3}

%global srcname steampunk-spotter
%bcond check 1

Name:           python-%{srcname}
Version:        5.10.0
Release:        %autorelease
Summary:        Scan, analyze, enhance, and provide insights for your playbooks using Spotter
License:        Apache-2.0
URL:            https://spotter.steampunk.si/
Source0:        https://gitlab.com/xlab-steampunk/steampunk-spotter-client/spotter-cli/-/archive/%{version}/spotter-cli-%{version}.tar.bz2
BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel
%if %{with check}
BuildRequires:  python%{python3_pkgversion}-pytest
BuildRequires:  python%{python3_pkgversion}-pytest-xdist
%endif

%global _description %{expand:
Steampunk Spotter is an Ansible Playbook Platform that offers valuable insights
into your playbooks to help you optimize and maximize your automation. It was
created by XLAB Steampunk, an IT automation specialist and leading expert in
building Enterprise Ansible Collections.}

%description %_description

%package -n python%{python3_pkgversion}-%{srcname}
Summary:        %{summary}

%description -n python%{python3_pkgversion}-%{srcname} %_description

%prep
%autosetup -p1 -n spotter-cli-%{version}
# work around _ ERROR collecting tests/integration/scan_export_collection_exclude/collection/library/test_info.py _ import file mismatch
mv tests/integration/scan_export_collection_exclude/collection/library/test_info{,_exclude}.py

%generate_buildrequires
export SETUPTOOLS_SCM_PRETEND_VERSION=%{version}
%pyproject_buildrequires

%build
export SETUPTOOLS_SCM_PRETEND_VERSION=%{version}
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l spotter

%check
%pyproject_check_import
%if %{with check}
%pytest
%endif

%files -n python%{python3_pkgversion}-%{srcname} -f %{pyproject_files}
%doc CHANGELOG.txt README.md
%{_bindir}/spotter

%changelog
%autochangelog
