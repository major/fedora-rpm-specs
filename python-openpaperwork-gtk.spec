%global srcname openpaperwork-gtk

Name:           python-%{srcname}
Version:        2.1.1
Release:        %autorelease
Summary:        OpenPaperwork GTK plugins

License:        GPLv3+
URL:            https://gitlab.gnome.org/World/OpenPaperwork/paperwork/tree/master/openpaperwork-gtk
Source0:        %{pypi_source}

BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3dist(openpaperwork-core)
BuildRequires:  python3dist(pygobject)

%description
Paperwork is a program to make papers searchable.

A bunch of plugins for Paperwork related to GLib and GTK.


%package -n     python3-%{srcname}
Summary:        %{summary}

Requires:       python3dist(pygobject)
Requires:       gdk-pixbuf2
Requires:       gtk3
Requires:       libhandy1
Requires:       libnotify
Requires:       pango

%description -n python3-%{srcname}
Paperwork is a GUI to make papers searchable.

A bunch of plugins for Paperwork related to GLib and GTK.


%prep
%autosetup -n %{srcname}-%{version}

%generate_buildrequires
%pyproject_buildrequires -r

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files openpaperwork_gtk

%check
PYTHONPATH=%{buildroot}%{python3_sitelib} \
    %{python3} -m unittest discover --verbose -s tests

%files -n python3-%{srcname} -f %{pyproject_files}
%doc README.md
%license LICENSE

%changelog
%autochangelog
