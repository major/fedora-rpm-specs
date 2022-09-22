%global srcname openpaperwork-core

Name:           python-%{srcname}
Version:        2.1.1
Release:        %autorelease
Summary:        OpenPaperwork's core

License:        GPLv3+
URL:            https://gitlab.gnome.org/World/OpenPaperwork/paperwork/tree/master/openpaperwork-core
Source0:        %{pypi_source}

BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-psutil

%description
Paperwork is a GUI to make papers searchable.

This is the core part of Paperwork. It manages plugins.


%package -n     python3-%{srcname}
Summary:        %{summary}

%description -n python3-%{srcname}
Paperwork is a GUI to make papers searchable.

This is the core part of Paperwork. It manages plugins.


%prep
%autosetup -n %{srcname}-%{version}

%generate_buildrequires
%pyproject_buildrequires -r

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files openpaperwork_core

%check
PYTHONPATH=%{buildroot}%{python3_sitelib} \
    %{python3} -m unittest discover --verbose -s tests

%files -n python3-%{srcname} -f %{pyproject_files}
%doc README.md
%license LICENSE

%changelog
%autochangelog
