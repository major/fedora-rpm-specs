Name:           python-poi-tracker
Version:        0.0.1
Release:        %autorelease
Summary:        Tool for tracking packages of interest

License:        GPL-2.0-or-later
URL:            https://pagure.io/michel-slm/poi-tracker
Source:         %{pypi_source poi_tracker}

BuildArch:      noarch
BuildRequires:  python3-devel


%global _description %{expand:
poi-tracker is a tool for tracking packages of interest.}

%description %_description

%package -n     poi-tracker
Summary:        %{summary}

%description -n poi-tracker %_description


%prep
%autosetup -p1 -n poi_tracker-%{version}


%generate_buildrequires
%pyproject_buildrequires -x test


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files -l poi_tracker


%check
%pyproject_check_import


%files -n poi-tracker -f %{pyproject_files}
%{_bindir}/poi-tracker


%changelog
%autochangelog
